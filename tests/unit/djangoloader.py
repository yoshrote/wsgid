


import unittest
import os

from wsgid.loaders.djangoloader import DjangoAppLoader

class DjangoLoaderTest(unittest.TestCase):


  def setUp(self):
    dirname = os.path.dirname(__file__)
    abs_path_dirname = os.path.abspath(os.path.expanduser(dirname))
    self.wsgi_app_path = os.path.join(abs_path_dirname, 'app-path/app')
    self.app_loader = DjangoAppLoader()

  '''
   Ensure we can load a djangoapp even with hidden folders
   inside the wsgi-app folder.
  '''
  def test_can_load_django_app(self):
    self.assertTrue(self.app_loader.can_load(self.wsgi_app_path))
