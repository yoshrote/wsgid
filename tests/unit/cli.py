#encoding: utf-8

import sys

import unittest
import ludibrio
from wsgid import Cli

class CliTest(unittest.TestCase):

  def setUp(self):
    self.cli = Cli()
    self.params = {'uuid': '8ecdaafb-4746-4b1d-adb3-c904764f67a8',\
        'recv': 'tcp://127.0.0.1:8888',\
        'send': 'tcp://127.0.0.1:8889'}
    # As we are dealing with a command line test, we have do clean the passed arguments
    # so the testes applicatins does not try to use them
    sys.argv[1:] = []
  
  def test_uuid_is_None(self):
    self.params['uuid'] = None
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)
  
  def test_uuid_is_empty(self):
    self.params['uuid'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

  def test_recv_is_None(self):
    self.params['recv'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

  def test_recv_is_empty(self):
    self.params['recv'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)
  
  def test_send_is_None(self):
    self.params['send'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

  def test_send_is_empty(self):
    self.params['send'] = ''
    self.assertRaises(Exception, self.cli.validate_input_params, **self.params)

  def test_run_prints_on_stderr(self):
    with ludibrio.Mock() as exit:
      from sys import exit
      exit(1)

    with ludibrio.Mock() as stderr:
      from sys import stderr
      stderr.write(ludibrio.any())

    self.cli.run()
    #Check that we print messages on stderr
    stderr.validate()
    #Check that we sys.exit(1) on any errors
    exit.validate()
