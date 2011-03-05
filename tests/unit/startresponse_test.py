#encoding: utf-8


import unittest
from wsgid.core import StartResponse, StartResponseCalledTwice

class StartResponseTest(unittest.TestCase):

  def setUp(self):
    self.start_response = StartResponse()


  def test_start_response_app_return_iterable(self):
    headers = [('Header', 'Value'), ('Other-Header', 'More-Value')]
    self.start_response('200 OK', headers)
    self.assertEquals(headers, self.start_response.headers)
    self.assertEquals('200 OK', self.start_response.status)

  def test_acumulate_body_data(self):
    write_fn = self.start_response('200 OK', [])
    write_fn('First Line\n')
    write_fn('Second One\n')
    self.assertEquals('First Line\nSecond One\n', self.start_response.body)

  '''
   Ensure that it's possible to change the status/headers values if the write callable
   was called yet
  '''
  def test_change_status_value(self):
    self.start_response('200 OK', [('Header', 'Value')])
    self.assertEquals('200 OK', self.start_response.status)
    self.assertEquals([('Header', 'Value')], self.start_response.headers)
    import sys
    self.start_response('500 Internal Server Error', [('More-Header', 'Other-Value')], sys.exc_info())
    self.assertEquals('500 Internal Server Error', self.start_response.status)
    self.assertEquals([('More-Header', 'Other-Value')], self.start_response.headers)

  '''
   start_response should re-raise the exception raise by the app
  '''
  def test_call_start_response_after_called_write(self):
    write_fn = self.start_response('200 OK', [])
    write_fn('Body\n') # Response sent to client
    try:
      raise Exception()
    except:
      import sys
      exec_info = sys.exc_info()
      self.assertRaises(exec_info[0], self.start_response, '500 Server Error', [], exec_info)

  def test_call_start_response_twice_without_exec_info(self):
    self.start_response('200 OK', [])
    self.assertRaises(StartResponseCalledTwice, self.start_response, '500 OK', [])

