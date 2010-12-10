#encoding: utf-8


import unittest
import optparse

from wsgid.options import parser

class ParserTest(unittest.TestCase):
  
  def test_return_original_parser(self):
    (orig_parser, options, args) = parser.parse_args()
    self.assertTrue(isinstance(orig_parser, optparse.OptionParser))
    self.assertTrue(isinstance(options, optparse.Values))
    self.assertTrue(isinstance(args, list))
