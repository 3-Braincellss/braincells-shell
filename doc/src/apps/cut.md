Module src.apps.cut
===================

Classes
-------

`CutApp(args)`
:   Executes bash application cut:
    cut -b [INTERVALS] [PATHS]*
    If paths is empty or '-' stdin is used

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :   Executes the cut command extracting specified bytes from text.
        :param inp: The string text to cut bytes from.
        :param out: The deque used to store the result of the application

    `validate_args(self)`
    :   Ensures the options are valid.
        :raises AppRunException: If -b option is missing or -b is not the only
        option.