Module src.apps.cd
==================
This module represents the cd bash command

Classes
-------

`CdApp(args=[])`
:   Application representing the bash command:
    cd [DIRECTORY]

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :   Changes current working directory
        
        If a FULL DIRECTORY is supplied changes current directory to the given
        one
        
        If a RELATIVE DIRECTORY is supplied changed current directory to the
        given one
        
        If NO DIRECTORY is given changes directory to the root

    `validate_args(self)`
    :   Check that the number of arguments is greater than 1
        and if the given path exists.