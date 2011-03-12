#encoding: utf-8

import sys

import unittest
import ludibrio
from wsgid.core.cli import Cli

class CliTest(unittest.TestCase):

  def setUp(self):
    self.cli = Cli()
    self.params = {'uuid': '8ecdaafb-4746-4b1d-adb3-c904764f67a8',\
        'recv': 'tcp://127.0.0.1:8888',\
        'send': 'tcp://127.0.0.1:8889'}
    # As we are dealing with a command line test, we have do clean the passed arguments
    # so the tested applications does not try to use them
    sys.argv[1:] = []
  
  def test_uuid_is_empty(self):
    self.params['uuid'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

  def test_recv_is_empty(self):
    self.params['recv'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)
  
  def test_send_is_empty(self):
    self.params['send'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

  '''
   --app-path is not mandatory when --wsgi-app is passed
  '''
  def test_app_path_not_mandatory(self):
    self.params['wsgi_app'] = 'my.package.application'
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

