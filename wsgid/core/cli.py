#encoding: utf-8

import sys
from ..options import parser
from wsgid import Wsgid
from ..loaders import load_app

import plugnplay

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

      if options.loader_dir:
        plugnplay.set_plugin_dirs(*options.loader_dir)
        plugnplay.load_plugins()

      wsgi_app = load_app(options.app_path, options.wsgi_app_full_name)
      wsgid = Wsgid(wsgi_app, options.uuid, options.recv, options.send)
      wsgid.serve()
    except Exception, e:
      import traceback
      exc_info = sys.exc_info()
      sys.stderr.write("".join(traceback.format_exception(exc_info[0], exc_info[1], exc_info[2])))
      sys.exit(1)
