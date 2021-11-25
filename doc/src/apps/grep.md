Module src.apps.grep
====================

Classes
-------

`GrepApp(args)`
:   Application representing the bash command:
    grep [PATTERN] [FILE]*

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :   Performs the grep operation on all specified paths.
        :param inp: The input args of the command, only used for piping
        and redirects.

    `validate_args(self)`
    :   Checks whether the given args are appropriate for the application.