Module src.apps.cat
===================

Classes
-------

`CatApp(args)`
:   Application representing the bash command:
    cat [FILES]...

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
    :   Ensures the options are valid.
        :raises AppRunException: If any option is given.