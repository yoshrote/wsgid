Application Structure
=====================


wsgid can load an app in two forms: 

  * Installed system-wide;
  * Installed inside a folder on disk;

When not system-wide installed, the folder where an app is installed must have a fixed structure. Supose your app in */var/apps/myapp*, this location must have this structure.

 * /var/apps/myapp/run
 * /var/apps/myapp/logs
 * /var/apps/myapp/app


The *run* directory is where wsgid will open the *control port*. This *port* is in fact a 0mq socket where wsgid can read commands. The *logs* directory, as the name suggests is where wsgid generate all logs.
The *app* directory is where you will put the application code. This is exactly the same value passed to *--app-path* option. More details, see :doc:`options`. Remember that this path will be added to python's sys.path variable, so if your app resides inside a python module (typically a django app) this same module must exist inside the app folder. Taking django as an example, if you have an app named *helloapp* you must have, at the end, the following path: */var/apps/myapp/app/helloapp*.
