Installing WSGID
================


Dependencies
::::::::::::

Current version of wsgid depends on the following softwares:

* plugnplay: Implements all plugin infra-structure of wsgid

  * https://github.com/daltonmatos/plugnplay

* pyzmq: Python bindings to the zeromq

  * https://github.com/zeromq/pyzmq

* python-daemon: Implements the daemon functionality

  * http://pypi.python.org/pypi/python-daemon/


You don't need to manually install all these dependencies as the *setup.py* installation script will handle this for your.

Instalation options
:::::::::::::::::::

Pip
:::

wsgid is registered on Python package index under the name wsgid, so you can install it running te following command:

    $ sudo pip install wsgid

and you're done!


From Source-code
::::::::::::::::

wsgid source-code is hosted on github (https://github.com). To get a copy run:

    $ git clone git://github.com/daltonmatos/wsgid

Now *cd* into the created folder (wsgid) and run:

    $ sudo python setup.py install


Note that this will get your a **read-only** copy of the code. If you are interested in contributing to the project, please se :doc:`contributing`.

