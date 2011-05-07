Application Structure
=====================


wsgid can load an app in two forms: 

  * Installed system-wide;
  * Installed inside a folder on disk;

When not system-wide installed, the folder where an app is installed must have a fixed structure. Suppose your app is installed inside */var/apps/myapp*, this location must have this structure.

 * /var/apps/myapp/logs
 * /var/apps/myapp/app

The *logs* directory, as the name suggests is where wsgid generate all logs.

The *app* directory is where you will put the application code. 

If your app resides inside a python module (typically a django app) this same module must exist inside the app folder. Remember that this path (*/var/apps/myapp/app*) will be added to *sys.path*. Taking django as an example, if you have an app named *helloapp* you must have, at the end, the following path: */var/apps/myapp/app/helloapp*.

In this example the value that should be passed to *--app-path* option is */var/apps/myapp*. More details, see :doc:`options`.

.. _pid-folder:

The pid folder
**************

.. versionadded:: 0.2

Now wsgid creates a `pid` folder. Inside this folder it writes the PID of all processes it started. Since we can start as many instances of wsgid we may need, wsgid separates the PID's in two folders: `pid/master` for master processes and `pid/worker` for worker processes. The PIDs are written to a file named <pidnumber>.pid.

So an instance of wsgid with 3 workers would generate:

 * pid/master/<masterpid>.pid
 * pid/worker/<pid-of-worker0>.pid
 * pid/worker/<pid-of-worker1>.pid
 * pid/worker/<pid-of-worker2>.pid

If we start another instance of wsgid with 2 workers we would have two more files:

 * pid/master/<anoter-master-pid>.pid
 * pid/worker/<pid-of-worker0>.pid

Since we write all worker pids inside the same folder, for now it's not possible to know which worker belongs to which master process.

