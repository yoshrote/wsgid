#encoding: utf-8

import optparse
from wsgid import __version__

optparser = optparse.OptionParser(prog='wsgid',\
    description='A complete WSGI environment for mongrel2 handlers',\
    version="%s" % __version__)

optparser.add_option('--uuid', help="Sets the server's uuid value",\
    action="store", dest="uuid")

optparser.add_option('--recv', help="TCP socket used to receive data from mongrel2. Format is IP:Port or *:Port to listen on any local IP",\
    action="store", dest="recv")

optparser.add_option('--send', help="TCP socket used to return data to mongrel2. Format is IP:Port",\
    action="store", dest="send")

def parse_args():
  (options, args) = optparser.parse_args()
  return (optparser, options, args)







