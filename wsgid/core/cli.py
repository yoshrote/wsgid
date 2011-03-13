#encoding: utf-8

import sys
import logging
import os

from ..options import parser
from wsgid import Wsgid
from ..loaders import load_app

import plugnplay
import daemon
import signal

class Cli(object):
  '''
   Command Line interface for wsgid
  '''

  def validate_input_params(self, app_path, uuid, recv, send, wsgi_app):
    if not app_path and not wsgi_app:
      raise Exception("--app-path is mandatory when --wsgi-app is not passed\n")
    if app_path and not self._full_path(app_path):
      raise Exception("path %s does not exist.\n" % abs_path)
    if not uuid:
      raise Exception("UUID is mandatory\n")
    if not recv:
      raise Exception("Recv socket is mandatory\n")
    if not send:
      raise Exception("Send socker is mandatory\n")

  def run(self):
    options = parser.parse_args()
    self.validate_input_params(app_path=options.app_path,\
        uuid=options.uuid, recv=options.recv, send=options.send,\
        wsgi_app=options.wsgi_app)
    try:
      daemon_options = self._create_daemon_options(options)
      ctx = daemon.DaemonContext(**daemon_options)
      self._set_loggers(options)
      with ctx:
        self.log.info("Master process started")
        self._load_plugins(options)

        if options.nodaemon:
          self._call_wsgid(options)
        else:
          workers = []
          for worker in range(options.workers):
            pid = self._create_worker(options)
            workers.append(pid)
          self._wait_workers(workers)
    except Exception, e:
      import traceback
      exc = sys.exc_info()
      sys.stderr.write("".join(traceback.format_exception(exc[0], exc[1], exc[2])))
      sys.exit(1)

  def _wait_workers(self, workers):
    while True:
      dead_worker = os.wait()
      workers.remove(dead_worker[0])
      self.log.info("Worker finished, pid=%s retval=%s" % dead_worker)
      if not workers:
        self.log.info("No more workers to wait for and no keep alive requested, exiting...")
        sys.exit(0)

  def _load_plugins(self, options):
    if options.loader_dir:
      plugnplay.set_plugin_dirs(*options.loader_dir)
      plugnplay.load_plugins()

  def _create_daemon_options(self, options):
    daemon = {'detach_process': not options.nodaemon}
    daemon.update({ 'stdin': sys.stdin, 
                   'stdout': sys.stdout, 
                   'stderr': sys.stderr})
    if options.nodaemon:
      # If we are not a daemon we must maintain the basic signal handlers
      daemon.update({'signal_map': {
          signal.SIGTTIN: signal.getsignal(signal.SIGTTIN),
          signal.SIGTTOU: signal.getsignal(signal.SIGTTOU),
          signal.SIGTSTP: signal.getsignal(signal.SIGTSTP),
          signal.SIGTERM: signal.getsignal(signal.SIGTERM)
        }})
    else:
      daemon.update({'signal_map':
                      {signal.SIGTERM: signal.getsignal(signal.SIGTERM)}
        })


    if options.chroot and options.app_path:
      full_path = self._full_path(options.app_path)
      stat = os.stat(full_path)
      daemon.update({'chroot_directory': full_path,
                     'uid': stat.st_uid,
                     'gid': stat.st_gid})
    return daemon

  def _full_path(self, path):
    return os.path.abspath(os.path.expanduser(path))

  '''
   Forks a new wsgid worker, return this pid of this worker
  '''
  def _create_worker(self, options):
    pid = os.fork()
    if not pid:
      self.log.info("New wsgid worker created")
      self._call_wsgid(options)
    return pid

  def _call_wsgid(self, options):
    path = options.app_path
    if options.chroot:
      path = '/'
    wsgi_app = load_app(path, options.wsgi_app)
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
