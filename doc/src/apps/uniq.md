Module src.apps.uniq
====================

Classes
-------

`UniqApp(args)`
:   

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :   Executes that uniq command on the given arguments.
        :param inp: The input args of the command, only used for piping
        and redirects.
        :param out: The output deque.
        :return: Returns the output deque.

    `validate_args(self)`
    :   Ensures the options are valid.
        :raises AppRunException: If any other option other than -i is
        given, or multiple paths are given as args