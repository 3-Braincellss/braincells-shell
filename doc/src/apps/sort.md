Module src.apps.sort
====================

Classes
-------

`SortApp(args)`
:   Sorts the contents of a file/stdin line by line and prints the result to stdout.
    
    sort [OPTIONS] [FILE]
    
    OPTIONS:
    
        -r sorts lines in reverse order
    
    FILE is the name of the file. If not specified, uses stdin.

    ### Ancestors (in MRO)

    * apps.app.App

    ### Methods

    `run(self, inp, out)`
    :

    `validate_args(self)`
    :   Checks whether the given args are appropriate for the application.