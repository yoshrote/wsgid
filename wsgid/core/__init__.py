#encoding: utf-8

__all__ = ['StartResponse', 'StartResponseCalledTwice']

class StartResponse(object):

  def __init__(self):
    self.headers = []
    self.status = ''
    self.body = ''
    self.called = False
    self.body_written = False

  def __call__(self, status, response_headers, exec_info=None):
    if self.called and not exec_info:
      raise StartResponseCalledTwice()

    if exec_info and self.body_written:
      try:
        raise exec_info[0], exec_info[1], exec_info[2]
      finally:
        exec_info = None # Avoid circular reference (PEP-333)

    self.headers = response_headers
    self.status = status

    self.called = True
    return self._write

  def _write(self, body):
    self.body_written = True
    self.body += body


class StartResponseCalledTwice(Exception):
  pass

from message import *
from wsgid import *
