#encoding: utf-8

import urllib
from ..http import HTTP_HEADERS
from ..core import Message, StartResponse
import zmq
from StringIO import StringIO

class Wsgid(object):
  
  def __init__(self, app = None, recv_ident = None, recv = None, send = None):
    self.environ = {}
    self.app = app
    self.recv_ident = recv_ident
    self.recv = recv
    self.send = send

    self.ctx = zmq.Context()

  '''
   Start serving requests.
  '''
  def serve(self):
    recv_sock = self.ctx.socket(zmq.PULL)
    recv_sock.connect(self.recv)
    recv_sock.setsockopt(zmq.IDENTITY, self.recv_ident)

    send_sock = self.ctx.socket(zmq.PUB)
    send_sock.connect(self.send)

    while True:
      m2message = Message(recv_sock.recv())

      if m2message.is_disconnect():
        continue

      environ = self._create_wsgi_environ(m2message.headers, m2message.body)
      start_response = StartResponse()

      server_id = m2message.server_id
      client_id = m2message.client_id
      response = None
      try:
        body = ''
        response = self.app(environ, start_response)

        if start_response.body_written:
          body = start_response.body
        else:
          for data in response:
            body += data

        status = start_response.status
        headers = start_response.headers
        send_sock.send(str(self._reply(server_id, client_id, status, headers, body)))
      except Exception, e:
        # Internal Server Error
        send_sock.send(self._reply(server_id, client_id, '500 Internal Server Error', headers=[]))
        import sys, traceback
        exc_info = sys.exc_info()
        sys.stderr.write("".join(traceback.format_exception(exc_info[0], exc_info[1], exc_info[2])))
      finally:
        if hasattr(response, 'close'):
          response.close()


  '''
   Constructs a mongrel2 response message based on the
   WSGI app response values.
   @uuid, @conn_id comes from Wsgid itself
   @headers, @body comes from the executed application

   @body is the raw content of the response and not [body]
   as returned by the WSGI app
   @headers is a list of tuples
  '''
  def _reply(self, uuid, conn_id, status, headers = [], body = ''):
    RAW_HTTP = "HTTP/1.1 %(status)s\r\n%(headers)s\r\n%(body)s"
    msg = "%s %d:%s, " % (uuid, len(conn_id), conn_id)
    params = {'status': status, 'body': body}

    headers += [('Content-Length', len(body))]
    raw_headers = ""
    for h,v in headers:
      raw_headers += "%s: %s\r\n" % (h,v)

    params['headers'] = raw_headers
    return msg + RAW_HTTP % params

  '''
   Creates a complete WSGI environ from the JSON encoded headers
   reveived from mongrel2.
   @json_headers should be an already parsed JSON string
  '''
  def _create_wsgi_environ(self, json_headers, body=None):
    #Not needed
    json_headers.pop('URI', None)
    
    #First, some fixed values
    self.environ['wsgi.multithread'] = False
    self.environ['wsgi.multiprocess'] = True
    self.environ['wsgi.run_once'] = True
    self.environ['wsgi.version'] = (1,0)
    self.environ['wsgi.url_scheme'] = "http"

    if body:
      self.environ['wsgi.input'] = StringIO(body)
    else:
      self.environ['wsgi.input'] = StringIO('')


    self.environ['REQUEST_METHOD'] = json_headers.pop('METHOD')
    self.environ['SERVER_PROTOCOL'] = json_headers.pop('VERSION')
    self.environ['SCRIPT_NAME'] = json_headers.pop('PATTERN').rstrip('/')
    self.environ['QUERY_STRING'] = json_headers.pop('QUERY', "")

    script_name = self.environ['SCRIPT_NAME']
    path_info = json_headers.pop('PATH')[len(script_name):]
    self.environ['PATH_INFO'] = str(urllib.unquote(path_info))

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

