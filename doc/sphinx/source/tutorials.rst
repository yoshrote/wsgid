Tutorials
=========


Here are some example tutorials about running WSGID with different frameworks.


Loading a Django Application
****************************

Supose you have a django project (http://djangoproject.com) named *myproject*. So probably you have an folder named *myroject*, with your *settings.py*, *manage.py*, and other files.
To load this app with wsgid you need to copy your application code to the *app* folder. Just pay attention that you must copy **your django project folder**, no only the contents. Supose you wsgid app will be at */var/wsgid/djangoapp*, so you must have, inside this folder, the correct structure for a wsgid app (see :doc:`appstructure`). 

In this example, we must copy the project folder (*myproject*) to the *app* folder: ::

    $ cp -a myproject/ /var/wsgid/djangoapp/app/

Now we have a *myproject* folder inside */var/wsgid/djangoapp/app*. As this last folder is added to *sys.path*, we are ready to go. Always remember that your django project should me importable with a simple *import myproject*.

Now just call wsgid as always: ::

    $ wsgid --app-path=/var/wsgid/djangoapp <other-options>


Loading a pyroutes Application
******************************

Loading an pyroutes (http://pyroutes.com) app is very easy and straight foward. First we create the new app. ::

    $ pyroutes-admin.py mynewproject

So now, inside this new folder we have the basic files for a pyroutes project. ::


    abc/
    templates/
    tests/
    handler.py
    pyroutes_settings.py

We should now copy **the contents** of this folder to the *app* folder of our wsgid app (see :doc:`appstructure`). Then we can load ou app just passing */path/to/our/wsgid-app* do wsgid's *--app-path* option. Suposing we copied this content to */var/wsgid/myproject/app* we just call wsgid this way: ::

  wsgid --app-path=/var/wsgid/myproject <other-options>

And you are ready to go.


Loading a generic WSGI Application
**********************************

So you tried hard but wsgid was not able to load your app? OK, not everything is lost, yet! To load your app you first need to write a python module that declareds the WSGI application object for your app, then you pass the complete name of this module to wsgid, like this.::

  wsgid --wsgi-app=myproject.frontends.wsgi.entry_point --send=SEND_SOCK --recv=RECV_SOCK --app-path=/path/to/the/wsgid-app

This means that the module *wsgi*, inside the module *frontends* of your project declares an object named *entry_point*. The *entry_point* object is just a callable that receives two parameters, just like PEP-333 says.
