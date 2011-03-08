#encoding: utf-8

import unittest

from wsgid.loaders import import_object

class ImportObjectTest(unittest.TestCase):

  def test_import_existing_object(self):
    join_obj = import_object('os.path.join')
    from os.path import join as real_obj
    self.assertEquals(join_obj, real_obj)

  def test_import_non_existing_object(self):
    self.assertRaises(Exception, import_object, 'os.path.joinnames')
