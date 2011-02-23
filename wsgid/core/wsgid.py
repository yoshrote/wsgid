#encoding: utf-8

import urllib


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
    #First, some fixed values
    self.environ['wsgi.multithread'] = False
    self.environ['wsgi.multiprocess'] = True
    self.environ['wsgi.run_once'] = True
    self.environ['wsgi.version'] = (1,0)

    self.environ['REQUEST_METHOD'] = json_headers['METHOD']
    self.environ['SERVER_PROTOCOL'] = json_headers['VERSION']
    self.environ['SCRIPT_NAME'] = json_headers['PATTERN'].rstrip('/')
    self.environ['QUERY_STRING'] = json_headers.get('QUERY', "")

    script_name = self.environ['SCRIPT_NAME']
    path_info = json_headers['PATH'][len(script_name):]
    self.environ['PATH_INFO'] = urllib.unquote(path_info)

    return self.environ
