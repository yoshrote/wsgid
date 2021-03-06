WSGId = WSGI Daemon
===================

Description
===========

Wsgid is a mongrel2 (http://mongrel2.org) adapter for WSGI applications. With wsgid you will be able to run your WSGI app as a true unix daemon.

Install
=======

To install just clone this repo and run: (pip package coming soon)
   
   sudo python setup.py install

Use example
===========

To start an application just call wsgid from the command line.

   wsgid --app-path=/path/to/the/app --recv=tcp://127.0.0.1:8889 --send=tcp://127.0.0.1:8890 --uuid=<send_ident>


This will load the app located at /path/to/the/app and be ready to process requests. wsgid automatically detects what kind of application it will load.
The <send_ident> value is the same value that is in mongrel2 config db.

If wsgid is not able do detect the aplication WSGI framework you can use the --wsgi-app option. 
   wsgid --app-path=/path/to/the/app --recv=tcp://127.0.0.1:8889 --send=tcp://127.0.0.1:8890 --uuid=<send_ident> --wsgi-app=my.package.application


--wsgi-app is the full qualified name of the WSGI application object, this way wsgid can find the app's entry point, as defined by pep-333.


Plugable Appication Loaders
===========================

wsgid has a plugable Application Loader subsystem, this way you can write your own AppLoader.  To do this just write an class that extends the wsgid.core.Plugin class and implements the IAppLoader interface. See the PyRoutesLoader (wsgid/loaders/__init__.py) for an actual example. To make wsgid use your loader just pass na aditional option: *--loader-dir*. This must point to the path where yout loader is located. More about this, read the docs on the site: http://wsgid.com

License
=======

wsgid is Licensed under *New BSD*, see LICENSE for details.

Know more
=========

Know more about the wsgid project on the official website: http://wsgid.com


https://github.com/daltonmatos/wsgid
2010-2011 | Dalton Barreto
