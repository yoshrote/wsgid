# encoding: utf-8
from setuptools import setup
from wsgid import __progname__, __version__
import os
import sys

setup(
  name=__progname__,
  version=__version__,
  url="https://github.com/daltonmatos/wsgid",
  license="GPLv2",
  description="A complete WSGI environment for mongrel2 handlers",
  author="Dalton Barreto",
  author_email="daltonmatos@gmail.com",
  long_description=file('README.rst').read(),
  packages=['wsgid', 'wsgid/options', 'wsgid/core', 'wsgid.loaders'],
  scripts=['scripts/wsgid'],
  install_requires = ['plugnplay', 'pyzmq', 'python-daemon'],
  classifiers = [
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Application Frameworks"
    ])


if 'install' in sys.argv:
  pwd = os.path.dirname(os.path.abspath(__file__))
  man_path = '/usr/share/man/man8/'
  if os.path.exists(man_path):
    print "Installing man pages"
    path = "%s/doc/wsgid.8.bz2" % pwd
    input_file = file(path).read()
    ouput_file = file(man_path + 'wsgid.8.bz2', 'wa')
    ouput_file.write(input_file)


