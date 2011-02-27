#encoding: utf-8

import urllib
from ..http import HTTP_HEADERS


class Wsgid(object):
  
  def __init__(self, app_path = None, recv = None, send = None):
    self.environ = {}


  '''
   Start serving requests.
  '''
  def serve(self):
    pass


  '''
   Creates a complete WSGI environ from the JSON encoded headers
   reveived from mongrel2.
   @json_headers should be an already parsed JSON string
  '''
  def _create_wsgi_environ(self, json_headers):
    #Not needed
    json_headers.pop('URI', None)
    
    #First, some fixed values
    self.environ['wsgi.multithread'] = False
    self.environ['wsgi.multiprocess'] = True
    self.environ['wsgi.run_once'] = True
    self.environ['wsgi.version'] = (1,0)

    self.environ['REQUEST_METHOD'] = json_headers.pop('METHOD')
    self.environ['SERVER_PROTOCOL'] = json_headers.pop('VERSION')
    self.environ['SCRIPT_NAME'] = json_headers.pop('PATTERN').rstrip('/')
    self.environ['QUERY_STRING'] = json_headers.pop('QUERY', "")

    script_name = self.environ['SCRIPT_NAME']
    path_info = json_headers.pop('PATH')[len(script_name):]
    self.environ['PATH_INFO'] = urllib.unquote(path_info)

    server_port = '80'
    host_header = json_headers.pop('host')
    if ':' in host_header:
      server_name, server_port = host_header.split(':')
    else:
      server_name = host_header

    self.environ['HTTP_HOST'] = server_name  
    self.environ['SERVER_PORT'] = server_port
    self.environ['SERVER_NAME'] = server_name
    
    self.environ['CONTENT_TYPE'] = json_headers.pop('content-type', '')
    self.environ['CONTENT_LENGTH'] = json_headers.pop('content-length', '')

    #Pass the other headers
    for (header, value) in json_headers.iteritems():
      if header[0] in ('X', 'x') or header.lower() in HTTP_HEADERS:
        self.environ[header] = value
      else:
        self.environ['HTTP_%s' % header] = value

    return self.environ


