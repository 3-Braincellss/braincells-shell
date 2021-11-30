Module src.operations.operation_factory
=======================================

Classes
-------

`OperationFactory()`
:   A class that is used to create operations objects
    
    Attributes
    ----------
    operations: dict
        Maps operation names to concrete operation classes
    
    Methods
    -------
    
    get_operation(op_str, data): Operation
        Returns an operation object given the operation name and context data

    ### Class variables

    `operations`
    :

    ### Static methods

    `get_operation(op_str: str, data: dict) ‑> operations.operation.Operation`
    :   Returns an operation object given the operation name and context data
        
        Parameters
        ----------
        
        op_str: str
            name of the operation
        
        data: dict
            a dictionary containing information required for initialisation of a
            certain concrete Operation object
            Maps property name to arbitrarily typed data.