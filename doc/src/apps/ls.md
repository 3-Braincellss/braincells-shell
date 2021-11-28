Module src.apps.ls
==================

Classes
-------

`LsApp(args)`
:   Lists all apps in the current or given directory

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :   ls [DIRECTORY]
        
        if NO ARGUMENTS provided print files in the current directory
        
        if ONE OR MORE ARGUMENTS provided print files in directories specified

    `validate_args(self)`
    :   Check is all paths in args exist.
        :raises: AppContextException if the path given does not exist.