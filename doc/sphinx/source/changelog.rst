Changelog
=========


Version 0.1
***********

  * Initial release

Version 0.2
***********

  * Bugfix: DjangoAppLoader now disconsiders hiddend folders inside ${app-path}/app;
  * Bugfix: Create each request with a fresh environ. Wsgid was keeping values between different requests;
  * Support for REMOTE_ADDR;
  * Wsgid now licensed under New BSD License;
  * Removed pypi package, at least temporarily;
  * Fixed setup.py: Don't try to install man pages on every run;
  * Wsgid is now able to load options from a JSON config file. More on :ref:`json-config`;
  * bugfix: Fatal errors are now correctly logged;
  * Internal refactorings.

