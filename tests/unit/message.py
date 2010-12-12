#encoding: utf-8


import unittest
from wsgid.core import Message



class PaserTest(unittest.TestCase):

  def setUp(self):
    self.server_id = "uuid"
    self.client_id = "42"
    self.path = "/some/path"
    self.netstring = "7:headers,4:body," 


  def test_parse_mongrel2_message(self):
    msg = "%s %s %s %s" % (self.server_id, self.client_id,\
        self.path, self.netstring)
    parsed_message = Message(msg)
    self.assertEquals(self.server_id, parsed_message.server_id)
    self.assertEquals(self.client_id, parsed_message.client_id)
    self.assertEquals(self.path, parsed_message.path)
    self.assertEquals(self.netstring, parsed_message.netstring)

  def test_parse_body_with_space(self):
    body_with_space = "6:header,12:body w space,"
    msg = "%s %s %s %s" % (self.server_id, self.client_id,\
        self.path, body_with_space)
    parsed_message = Message(msg)
    self.assertEquals(self.server_id, parsed_message.server_id)
    self.assertEquals(self.client_id, parsed_message.client_id)
    self.assertEquals(self.path, parsed_message.path)
    self.assertEquals(body_with_space, parsed_message.netstring)

  def test_parse_headers_with_space(self):
    headers_with_space = "15:headers w space,4:body,"
    msg = "%s %s %s %s" % (self.server_id, self.client_id,\
        self.path, headers_with_space)
    parsed_message = Message(msg)
    self.assertEquals(self.server_id, parsed_message.server_id)
    self.assertEquals(self.client_id, parsed_message.client_id)
    self.assertEquals(self.path, parsed_message.path)
    self.assertEquals(headers_with_space, parsed_message.netstring)
