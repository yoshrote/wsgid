WSGID Command line Options
==========================

Here we will document only the main options of wsgid. Other options you can read directly on the man page.

    $ man wsgid

app-path
**********

  --app-path

Path to the WSGI application. This should be the path where the code of your application is located. If the app is installed system wide, you don't need this.
This path will be added to sys.path so any module below this hirearchy can be imported with a simple *import <modulename>*.
The directory that contains your application must obey some rules, please see :doc:`appstructure`.

wsgi-app
**************

  --wsgi-app

Full qualified name for the WSGI application object. This options is used in two main ocasions. One: When wsgid cannot load your app automatically just by looking at **--app-path**. Two: When yout app is installed system wide. Supose you have inside in your app an package name *web*, and in this pachage you have a module names *frontends*. Supose frontends/wsgi.py is the module that defines the WSGI application object, as specified by PEP-333.::


    myapp/
      __init__.py
      mdolue1.py
      module2.py
      web/
        __init__.py
        frontends/
          __init__.py
          wsgi.py


In this example you would call wsgid with **--wsgi-app=myapp.web.frontends.wsgi.application**

The WSGI application object does not necessarily have to be named *application*. So if your app defines an object named *wsgi_entry_point*, no problem just pass to wsgid **--wsgi-app=myapp.web.frontends.wsgi.wsgi_entry_point**

loader-dir
***********************

    --loader-dir=LOADER_DIR

If wsgid can not auto-load your app you can write your own loader and point its locations to wsgid with this option. This path is just an folder with some .py files. wsgid will try to load all .py files searching for custom application loaders. The first loader that reports the ability to load the given application will be used

When this option is used at the same time that the --chroot option, the value passed will be realtive to the --app-path folder.

chroot
******

When this options is used, wsgid does a chroot to the --app-path folder. Remember that you have to run wsgid as root so this options takes effect. As running a daemon as root is not a good idea, wsgid will drop privileges to the user/group hat owns the --app-path folder

recv
****

  --recv=RECV_SOCKET

TCP socket used to receive data from mongrel2. This is the same value that is in the *send_spec* of *handler* table of mongrel2 config database. By passing this option to wsgid your application will respond to requests for any mongrel2's routes associated with this socket.

The format of *RECV_SOCKET* can be any format accpeted by zeromq

send
****
  --send=SEND_SOCKET

TCP socket used to return data to mongrel2. This is the same value that is in the *recv_spec* of *handler* table of mongrel2 config database. This value must belong to the same registry from where you got your **--recv** socket.

The format of *SEND_SOCKET* can be any format accpeted by zeromq

no-dameon
*********
  --no-daemon

Used mainly for debug purposes. When this option is passed wsgid will not fork to background and will write all logs to stderr.

workers
*******
  --workers=N

Set the number of wsgid workers processes. Each process has its own PID and is responsible for handling one request at a time.

keep-alive
**********
  --keep-alive

This option will make wsgid watch for its child processes. If any child process dies a new process is created imediately.


