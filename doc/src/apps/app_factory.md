Module src.apps.app_factory
===========================

Classes
-------

`AppFactory()`
:   A class that is used to create app objects
    Attributes
    ----------
    apps: dict
        A dictionary that maps app names to concrete app classes.
    
    no_glob: set
        A set of apps that don't require filename expansion or globbing
    
    Methods
    -------
    get_app(self, app_str, args)
        Returns an app object based on the app_str given.

    ### Class variables

    `apps`
    :

    `no_glob`
    :

    ### Static methods

    `get_app(app_str: str, args: list) ‑> apps.app.App`
    :   Returns an app object based on the app_str given.
        
        Parameters
        ----------
        app_str: str
            A string that represents the command to be called.
            If app_str starts with '_' the app will be treated as unsafe
        
        args: list
            A List of arguments that should be passed to the app.
        
        Raises
        ------
        AppNotFountException
            If an app is not found in the apps dictionary.
        
        Returns
        -------
        app: App
            An app object that is ready to be run