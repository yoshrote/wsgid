WSGID Internals
===============


Plugin system
:::::::::::::

wsgid internal plugin system is implemented by plugnplay. This means that all plugins must inherit one same base class, in this case this classe is *wsgid.core.Plugin*.

For now, wsgid only declares custom AppLoaders. But any other interface declared in the future will have to be implemented subclassing *wsgid.core.Plugin*.

App Loaders
:::::::::::

App loaders are classes that knows how to load an specific WSGI app. WSGID comes with some apploaders for some frameworks, for now django (http://djangoproject.com) and pyroutes (http://pyroutes.com).

As an app for each of this frameworks has a known structure, wsgid will try to discover the *best loader* for your app. The loaders are used in alphabetical order by the loader filename.

Writing your App Loader
************************

Writing your own AppLoader is very easy and simple. As said before every plugin must inherit *wsgid.core.Plugin* class, so it's not different with the AppLoaders.

To inform wsgid that your Plugin class implements the AppLoader interface (*wsgid.loaders.IAppLodaer*) you have to add one attribute to your class.::

  implements = [IAppLoader]

This is plugnplay specific, to know more about plugnplay go to: https://github.com/daltonmatos/plugnplay

Now, you need to fill the methods declared for the interface you are implementing, in this case are only two methods.

 * def can_load(self, app_path)
 * def load_app(self, app_path, app_full_name)

The first should return True/False if your loader, looking at the app_path directory, finds out that is can load this application. The second should return the WSGI application object for this app that is being loaded.

Now just save your loder into a .py file and pass --loader-dir=PATH_TO_LOADER to wsgid command line and your loader will be used to load your application. Feel free to write loader for other WSGI frameworks, see the :doc:`contributing` for more details.
