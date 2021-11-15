Module src.exceptions.app_context
=================================

Classes
-------

`AppContextException(app_str, message='GO AWAY >=[')`
:   This exception is raised during TREE TRANSFORMING STAGE
    When an app is created it's validate_args() method is called
    This method will call the context exception in case some arguments don't make sense

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException