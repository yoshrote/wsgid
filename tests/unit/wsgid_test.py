#encoding: utf-8


import unittest

from wsgid.core import Wsgid

class WsgidTest(unittest.TestCase):

  def setUp(self):
    self.wsgid = Wsgid()
    self.sample_headers = {
          'METHOD': 'GET',
          'VERSION': 'HTTP/1.1',
          'PATTERN': '/root',
          'URI': '/more/path/',
          'PATH': '/more/path',
          'QUERY': 'a=1&b=4&d=4',
          'host': 'localhost'
        }

  '''
   Creates the SCRIPT_NAME header from the mongrel2 PATTERN header.
   SCRIPT_NAME should be the PATTERN without any regex parts.
  '''
  def test_script_name_header(self):
    # /py/ -> /py/
    # /py/(.+) -> /py/
    self.sample_headers['PATTERN'] = "/py"
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("/py", environ['SCRIPT_NAME'])

    self.sample_headers['PATTERN'] = '/some/more/path/'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("/some/more/path", environ['SCRIPT_NAME'])

    self.sample_headers['PATTERN'] = '/'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("", environ['SCRIPT_NAME'])


  '''
   PATH_INFO comes from (URI - SCRIPT_NAME) or (PATH - SCRIPT_NAME)
  '''
  def test_eniron_path_info(self):

    self.sample_headers['PATTERN'] = '/py'
    self.sample_headers['PATH'] = '/py/some/py/path'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("/some/py/path", environ['PATH_INFO'])

    self.sample_headers['PATTERN'] = '/py'
    self.sample_headers['PATH'] = '/py'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("", environ['PATH_INFO'])


  def test_environ_unquoted_path_info(self):
    self.sample_headers['PATTERN'] = '/py/'
    self.sample_headers['PATH'] = '/py/so%20me/special%3f/user%40path'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals('/so me/special?/user@path', environ['PATH_INFO'])

  '''
   Generates de REQUEST_METHOD variable
  '''
  def test_environ_request_method(self):
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertTrue(environ.has_key('REQUEST_METHOD'))
    self.assertEquals('GET', environ['REQUEST_METHOD'])

  
  def test_environ_query_string(self):
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("a=1&b=4&d=4", environ['QUERY_STRING'])

    #Not always we have a QUERY_STRING
    del self.sample_headers['QUERY']
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals("", environ['QUERY_STRING'])


  def test_environ_server_port(self):
    self.sample_headers['host'] = 'localhost:443'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals('443', environ['SERVER_PORT'])

    self.sample_headers['host'] = 'localhost'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals('80', environ['SERVER_PORT'])

  def test_environ_server_name(self):
    self.sample_headers['host'] = 'localhost:8080'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals('localhost', environ['SERVER_NAME'])

    self.sample_headers['host'] = 'someserver'
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals('someserver', environ['SERVER_NAME'])

  '''
   Have to be calculated from len(body) ?
  '''
  def test_environ_content_type(self):
    self.fail("Not Implemented")

  '''
   Comes from mongrel2 VERSION header
  '''
  def test_environ_server_protocol(self):
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertTrue(environ.has_key('SERVER_PROTOCOL'))
    self.assertEquals('HTTP/1.1', environ['SERVER_PROTOCOL'])

  '''
   All headers (but HTTP common headers) must be HTTP_ suffixed
  '''
  def test_environ_other_headers(self):
    self.fail("Not Implemented")
  
  '''
   Some values are fixed:
    * wsgi.multithread = False
    * wsgi.multiprocess = True
    * wsgi.run_once = True
    * wsgi.version = (1,0)
  '''
  def test_environ_fixed_values(self):
    environ = self.wsgid._create_wsgi_environ(self.sample_headers)
    self.assertEquals(False, environ['wsgi.multithread'])
    self.assertEquals(True, environ['wsgi.multiprocess'])
    self.assertEquals(True, environ['wsgi.run_once'])
    self.assertEquals((1,0), environ['wsgi.version'])
    

