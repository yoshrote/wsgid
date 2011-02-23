# encoding: utf-8
from setuptools import setup
from wsgid import __version__, __progname__

setup(
  name=__progname__,
  version=__version__,
  url="https://github.com/daltonmatos/wsgid",
  license="GPLv2",
  description="A complete WSGI environment for mongrel2 handlers",
  author="Dalton Barreto",
  author_email="daltonmatos@gmail.com",
  long_description=file('README').read(),
  packages=['wsgid', 'wsgid/options', 'wsgid/core'],
  scripts=['scripts/wsgid'],
  classifiers = [
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Application Frameworks"
    ])
