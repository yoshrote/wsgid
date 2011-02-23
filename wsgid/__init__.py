#encoding: utf-8

__all__ = ['Cli']

__progname__ = "wsgid"
__version__ = "v0.1"

import sys
from wsgid.options import parser
import sys

class Cli(object):
  '''
   Command Line interface for wsgid
  '''

  def validate_input_params(self, uuid, recv, send):
    if not uuid:
      raise Exception("UUID is mandatory")
    if not recv:
      raise Exception("Recv socket is mandatory")
    if not send:
      raise Exception("Send socker is mandatory")

  def run(self):
    (original_parser, options, args) = parser.parse_args()
    try:
      self.validate_input_params(uuid=options.uuid,\
          recv=options.recv, send=options.send)
    except Exception, e:
      sys.stderr.write(str(e))
      sys.exit(1)
