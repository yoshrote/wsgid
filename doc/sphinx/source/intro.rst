Introduction
============

wsgid is a mongrel2 WSGI gateway. With wsgid you will be able to run your WSGI apps as unix daemons. You can have more than one instance of wsgid running the same application, the requests will be distributed among all wsgid processes in a round-robin policy.

About mongrel2
:::::::::::::::

Mongrel2 (http://mongrel2.org) is a language agnostic webserver backed by a high performance queue, ØMQ (http://zeromq.org). This way your have the webserver and the web applications as separated parts.This leads you to a number of advantages compared to the traditional *apache stack*.
Having this two parts separated you can change your app without touching the web server. You can spawn more instances of your app, update the code, restart the whole WSGI app, etc. All this without the webserver ever knowing you did this.


