Module src.apps.app_factory
===========================

Classes
-------

`AppFactory()`
:   A class that is used to create app objects

    ### Class variables

    `apps`
    :   (:obj:`dict`): A dictionary that maps app names to their classes

    `no_glob`
    :   set: A set of apps that don't require globbing

    ### Static methods

    `get_app(app_str: str, opts: list) ‑> apps.app.App`
    :   Returns an app object based on the app_str given.
        
        Args:
            app_str (:obj:`str`): A string that represents the command to be called.
                If app_str starts with '_' the app will be treated as unsafe
            opts (:obj:`list`): A List of arguments that should be passed to the app.
        
        Returns:
            app (:obj:`App`): An app object that is ready to be run