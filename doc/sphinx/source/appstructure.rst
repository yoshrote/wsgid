Application Structure
=====================


wsgid can load an app in two forms: 

  * Installed system-wide;
  * Installed inside a folder on disk;

When not system-wide installed, the folder where an app is installed must have a fixed structure. Suppose your app is installed inside */var/apps/myapp*, this location must have this structure.

 * /var/apps/myapp/run
 * /var/apps/myapp/logs
 * /var/apps/myapp/app


The *run* directory is where wsgid will open the *control port*. This *port* is in fact a 0mq socket where wsgid can read commands. This port is not implemented yet, so the folder *run* is, for now, optional.

The *logs* directory, as the name suggests is where wsgid generate all logs.

The *app* directory is where you will put the application code. 

If your app resides inside a python module (typically a django app) this same module must exist inside the app folder. Remember that this path (*/var/apps/myapp/app*) will be added to *sys.path*. Taking django as an example, if you have an app named *helloapp* you must have, at the end, the following path: */var/apps/myapp/app/helloapp*.

In this example the value that should be passed to *--app-path* option is */var/apps/myapp*. More details, see :doc:`options`.

