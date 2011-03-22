WSGID Internals
===============


Plugin system
:::::::::::::

WSGID internal plugin system is implemented by plgnplay...


App Loaders
:::::::::::

App loaders are classes that knows how to load an specific WSGI app. WSGID comes with some apploaders for some frameworks, like: django, flask, web2py and pyroutes.

As an app for each of this frameworks has a known structure, wsgid will try to discover the *best loader* for your app.

Writting your App Loader
````````````````````````
