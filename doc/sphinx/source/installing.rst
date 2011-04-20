Installing WSGID
================


Dependencies
::::::::::::

Current version of wsgid depends on the following software:

* plugnplay: Implements all plugin infra-structure of wsgid

  * https://github.com/daltonmatos/plugnplay

* pyzmq: Python bindings to the zeromq

  * https://github.com/zeromq/pyzmq

* python-daemon: Implements the daemon functionality

  * http://pypi.python.org/pypi/python-daemon/


You don't need to manually install all these dependencies as the *setup.py* installation script will handle this for your.

Instalation options
:::::::::::::::::::

From the website
****************

The official website (http://wsgid.com) has always the latest release tarball. Grab it, unpack it, and run:

    $ sudo python setup.py install

From Source-code
****************

wsgid source-code is hosted on github (https://github.com). To get a copy run:

    $ git clone git://github.com/daltonmatos/wsgid

Now *cd* into the created folder (wsgid) and run:

    $ sudo python setup.py install


Note that this will get you a **read-only** copy of the code. If you are interested in contributing to the project, please see :doc:`contributing`.

