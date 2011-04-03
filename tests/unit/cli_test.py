#encoding: utf-8

import sys
import signal
import os
import logging

import unittest
from wsgid.core.cli import Cli
from wsgid.options import parser


class CliTest(unittest.TestCase):

  def setUp(self):
    self.cli = Cli()
    # As we are dealing with a command line test, we have do clean the passed arguments
    # so the tested applications does not try to use them
    sys.argv[1:] = []

  def test_nodaemon(self):
    opts = self._parse()
    self.assertTrue(opts['detach_process'])

  def test_daemon_keep_sigterm_handler(self):
    opt = self._parse()
    self.assertTrue(opt['detach_process'])
    handler = signal.getsignal(signal.SIGTERM)
    self.assertEquals(opt['signal_map'][signal.SIGTERM], handler)

  '''
   When not a daemon we must keep std{in, out, err}
  '''
  def test_nodaemon_keep_basic_fds(self):
    opt = self._parse('--no-daemon')
    self.assertFalse(opt['detach_process'])
    self.assertEquals(opt['stdin'], sys.stdin)
    self.assertEquals(opt['stdout'], sys.stdout)
    self.assertEquals(opt['stderr'], sys.stderr)

  '''
    We should not try to chroot if --app-path was not passed
  '''
  def test_no_chroot_if_no_app_path(self):
    opt = self._parse('--chroot')
    self.assertFalse(opt.has_key('chroot_directory'))

  '''
    We shoud not chroot if --chroot is not passed.
  '''
  def test_no_chroot(self):
    opt = self._parse('--app-path=./')
    self.assertFalse(opt.has_key('chroot_directory'))

  '''
    If we are chrooting we must drop privileges.
  '''
  def test_drop_priv(self):
    opt = self._parse('--app-path=./', '--chroot')
    stat = os.stat('./')
    self.assertEquals(opt['uid'], stat.st_uid)
    self.assertEquals(opt['gid'], stat.st_gid)

  '''
   chroot_diretocry should have the absolute path of --app-path
  '''
  def test_chroot_has_absolute_app_path(self):
    opt = self._parse('--chroot', '--app-path=./')
    abspath = os.path.abspath(os.getcwd())
    self.assertEquals(opt['chroot_directory'], abspath)

  def _parse(self, *opts):
    sys.argv[1:] = opts
    return self.cli._create_daemon_options(parser.parse_args())

  '''
    We must generate all logs inside <app-path>/logs
  '''
  def test_ajust_log_path_app_path(self):
    app_path = os.path.join('../', os.path.dirname(__file__), 'app-path')
    sys.argv[1:] = ['--app-path=%s' % app_path]
    opt = parser.parse_args()
    self.cli._set_loggers(opt)
    handlers = self.cli.log.handlers
    self.assertTrue(isinstance(handlers[0], logging.FileHandler))
    self.assertEquals(os.path.join(app_path, 'logs/wsgid.log'), handlers[0].baseFilename)

  def test_full_path_empty_path(self):
    self.assertEquals(self.cli._full_path(None), None)

  '''
    Even if we do not chroot, we must drop priv.
  '''
  def test_should_droppriv_if_app_path_is_passed(self):
    app_path = os.path.join('../', os.path.dirname(__file__), 'app-path')
    argv = ['--app-path=%s' % app_path]
    stat = os.stat(self.cli._full_path(app_path))
    opts = self._parse(*argv)
    self.assertEquals(opts['uid'], stat.st_uid)
    self.assertEquals(opts['gid'], stat.st_gid)


