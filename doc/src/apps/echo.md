Module src.apps.echo
====================
This module represents the echo bash command.

Classes
-------

`EchoApp(args)`
:   echo [INPUT] [INPUT] ...

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :   Returns all the input args as a space seperated string.

    `validate_args(self)`
    :   Checks whether the given arguments are valid.