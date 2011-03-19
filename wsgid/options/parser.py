#encoding: utf-8

import optparse
from wsgid import __version__, __progname__

optparser = optparse.OptionParser(prog=__progname__,\
    description='A complete WSGI environment for mongrel2 handlers',\
    version="%s" % __version__)

optparser.add_option('--app-path', help="Path to the WSGI application",\
    action="store", dest="app_path")

optparser.add_option('--wsgi-app', help="Full qualified name for the WSGI application object",\
    action="store", dest="wsgi_app")

optparser.add_option('--loader-dir', help="Aditional dir for custom Application Loaders",\
    action="append", dest="loader_dir")

optparser.add_option('--debug', help="Runs wsgid in debug mode. Lots of logging.",\
    action="store_true", dest="debug")

optparser.add_option('--no-daemon', help="Runs wsgid in the foreground, printing all logs to stderr",\
    action="store_true", dest="nodaemon")

optparser.add_option('--workers', help="Starts a fixed number of wsgid processes. Defaults to 1",\
    action="store", default="1", type="int", dest="workers")

optparser.add_option('--keep-alive', help="Automatically respawn any dead worker. Killink the master process kills any pending worker",\
    action="store_true", dest="keep_alive")

optparser.add_option('--chroot', help="Chroot to the value of --app-path, before loading the app.",\
    action="store_true", dest="chroot")

optparser.add_option('--recv', help="TCP socket used to receive data from mongrel2. Format is IP:Port or *:Port to listen on any local IP",\
    action="store", dest="recv")

optparser.add_option('--send', help="TCP socket used to return data to mongrel2. Format is IP:Port",\
    action="store", dest="send")

def parse_args():
  (options, args) = optparser.parse_args()
  return options







