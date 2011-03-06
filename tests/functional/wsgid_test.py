#encoding: utf-8

import unittest
from wsgid.core import Wsgid
from wsgid.test import simple_fork

import os
import urllib2

class WsgidServeTest(unittest.TestCase):

  def setUp(self):
    pass

  def test_app_return_body(self):
    def app(environ, start_response):
      start_response('200 OK', [('Some-Header', 'Some-Value')])
      return ['Body content']
    pid = self._run_wsgid(app)
    r = urllib2.urlopen('http://127.0.0.1:8888/py/abc/')
    body = r.read()
    self._kill_wsgid(pid)
    self.assertEquals(body, 'Body content')

    
  '''
   Ensure that when the WSGI app returns ['Line1', 'Line2', ...]
   Wsgid joins all parts to build the complete body
  '''
  def test_app_return_body_with_more_than_one_item(self):
    def app(env, start_response):
      write = start_response('200 OK', [])
      write('One Line\n')
      write('Two Lines\n')
      return ['More Lines\n', 'And more...\n']
    pid = self._run_wsgid(app)
    try:
      r = urllib2.urlopen('http://127.0.0.1:8888/py/abc/')
      self.assertEquals('One Line\nTwo Lines\nMore Lines\nAnd more...\n', r.read())
    finally:
      self._kill_wsgid(pid)

  def test_app_use_write_callable(self):
    def app(env, start_response):
      write = start_response('200 OK', [])
      write('One Line\n')
      write('Two Lines\n')
      return None
    pid = self._run_wsgid(app)
    try:
      r = urllib2.urlopen('http://127.0.0.1:8888/py/abc/')
      self.assertEquals('One Line\nTwo Lines\n', r.read())
    finally:
      self._kill_wsgid(pid)


  
  def test_app_uses_write_callable_and_return_body(self):
    def app(env, start_response):
      write = start_response('200 OK', [])
      write('Line1\n')
      write('Line2\n')
      return ['Line3\n']
    pid = self._run_wsgid(app)
    try:
      r = urllib2.urlopen('http://127.0.0.1:8888/py/abc/')
      self.assertEquals('Line1\nLine2\nLine3\n', r.read())
    finally:
      self._kill_wsgid(pid)


  def _run_wsgid(self, app):
    def _serve(app):
      w = Wsgid(app, 'e240f04a-acbd-414f-a1b3-e070644713d7', 'tcp://127.0.0.1:8889', 'tcp://127.0.0.1:8890')
      w.serve()
    import multiprocessing
    p = multiprocessing.Process(target=_serve, args=(app,))
    p.start()
    return p.pid
  
  def _kill_wsgid(self, pid):
    import os
    os.kill(pid, 15)


