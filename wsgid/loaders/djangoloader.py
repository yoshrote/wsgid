


from wsgid.loaders import IAppLoader
from wsgid.core import Plugin

import os
import sys

class DjangoAppLoader(Plugin):
  implements = [IAppLoader]

  def can_load(self, app_path):
    return os.path.exists(os.path.join(app_path, 'urls.py')) 

  def load_app(self, app_path, app_full_name):
    site_name = os.path.basename(app_path)
    site = os.path.dirname(app_path)
    sys.path.insert(1, site)
    os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % site_name
    import django.core.handlers.wsgi
    return django.core.handlers.wsgi.WSGIHandler()
     
