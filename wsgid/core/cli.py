#encoding: utf-8

import sys
import logging

from ..options import parser
from wsgid import Wsgid
from ..loaders import load_app

import plugnplay

class Cli(object):
  '''
   Command Line interface for wsgid
  '''

  def validate_input_params(self, app_path, uuid, recv, send, wsgi_app):
    if not app_path and not wsgi_app:
      raise Exception("--app-path is mandatory when --wsgi-app is not passed\n")
    if not uuid:
      raise Exception("UUID is mandatory\n")
    if not recv:
      raise Exception("Recv socket is mandatory\n")
    if not send:
      raise Exception("Send socker is mandatory\n")

  def run(self):
    (original_parser, options, args) = parser.parse_args()
    daemon = not options.nodaemon
    try:
      self.validate_input_params(app_path=options.app_path,\
          uuid=options.uuid, recv=options.recv, send=options.send,\
          wsgi_app=options.wsgi_app)

      self._set_loggers(options)

      if options.loader_dir:
        plugnplay.set_plugin_dirs(*options.loader_dir)
        plugnplay.load_plugins()

      if daemon:
        pass # daemon code
      else:
        self._call_wsgid(options)
    except Exception, e:
      self.log.exception(e)
      sys.exit(1)

  def _call_wsgid(self, options):
    wsgi_app = load_app(options.app_path, options.wsgi_app)
    wsgid = Wsgid(wsgi_app, options.uuid, options.recv, options.send)
    wsgid.log = logging.getLogger('wsgid')
    wsgid.serve()

  def _set_loggers(self, options):
    level = logging.INFO if not options.debug else logging.DEBUG
    logger = logging.getLogger('wsgid')
    logger.setLevel(level)
    console = logging.StreamHandler()
    console.setLevel(level)

    formatter = logging.Formatter("%(asctime)s - %(name)s [pid=%(process)d] - %(levelname)s - %(message)s")
    console.setFormatter(formatter)

    logger.addHandler(console)
    self.log = logger
