#encoding: utf-8

__all__ = ['Cli']

__version__ = "wsgid v0.1"

import sys
from wsgid.options import parser


class Cli(object):
  '''
   Command Line interface for wsgid
  '''
  def run(self):
    (original_parser, options, args) = parser.parse_args()
    print options
    mandatory = ['uuid', 'recv', 'send']
    for option in mandatory:
      if not getattr(options, option):
        original_parser.error("%s is mandatory" % option)
    if len(args) == 0:
      original_parser.error("Missing application full path")
