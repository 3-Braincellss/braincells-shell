Module src.apps.app_factory
===========================

Classes
-------

`AppFactory()`
:   Creates an app object given the app_str

    ### Methods

    `get_app(self, app_str: str, args: list) ‑> apps.app.App`
    :   Returns an app object based on the app_str given.
        :param app_str: The string name of the app being requested.
        :param args: Array of all the options and arguments for the app.
        :return app: