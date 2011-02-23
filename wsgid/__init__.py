#encoding: utf-8

__all__ = ['Cli']

__progname__ = "wsgid"
__version__ = "v0.1"

import sys
from wsgid.options import parser
from wsgid.core import Wsgid

class Cli(object):
  '''
   Command Line interface for wsgid
  '''

  def validate_input_params(self, app_path, uuid, recv, send):
    if not app_path:
      raise Exception("APP_PATH is mandatory\n")
    if not uuid:
      raise Exception("UUID is mandatory\n")
    if not recv:
      raise Exception("Recv socket is mandatory\n")
    if not send:
      raise Exception("Send socker is mandatory\n")

  def run(self):
    (original_parser, options, args) = parser.parse_args()
    try:
      self.validate_input_params(app_path=options.app_path,\
          uuid=options.uuid, recv=options.recv, send=options.send)
      app = Wsgid(options.app_path, options.recv, options.send)
      app.serve()
    except Exception, e:
      sys.stderr.write(str(e))
      sys.exit(1)
