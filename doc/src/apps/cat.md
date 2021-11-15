Module src.apps.cat
===================

Classes
-------

`CatApp(args)`
:   

    ### Ancestors (in MRO)

    * apps.app.App

    ### Class variables

    `allowed_options`
    :

    ### Methods

    `run(self, inp, out)`
    :   Executes that cat command on the given arguments.
        :param inp: The input args of the command, only used for piping
        and redirects.
        :param out: The output queue.
        :return: Returns the output queue.

    `validate_args(self)`
    :   Checks whether the given args are appropriate for the application.