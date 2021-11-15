Module src.shellparser.parser
=============================

Functions
---------

    
`run_parser(text)`
:   

Classes
-------

`ShellTransformer(visit_tokens: bool = True)`
:   Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    
    Methods are provided by the user via inheritance, and called according to ``tree.data``.
    The returned value from each method replaces the node in the tree structure.
    
    Transformers work bottom-up (or depth-first), starting with the leaves and ending at the root of the tree.
    Transformers can be used to implement map & reduce patterns. Because nodes are reduced from leaf to root,
    at any point the callbacks may assume the children have already been transformed (if applicable).
    
    ``Transformer`` can do anything ``Visitor`` can do, but because it reconstructs the tree,
    it is slightly less efficient.
    
    To discard a node, return Discard (``lark.visitors.Discard``).
    
    All these classes implement the transformer interface:
    
    - ``Transformer`` - Recursively transforms the tree. This is the one you probably want.
    - ``Transformer_InPlace`` - Non-recursive. Changes the tree in-place instead of returning new instances
    - ``Transformer_InPlaceRecursive`` - Recursive. Changes the tree in-place instead of returning new instances
    
    Parameters:
        visit_tokens (bool, optional): Should the transformer visit tokens in addition to rules.
                                       Setting this to ``False`` is slightly faster. Defaults to ``True``.
                                       (For processing ignored tokens, use the ``lexer_callbacks`` options)
    
    NOTE: A transformer without methods essentially performs a non-memoized partial deepcopy.

    ### Ancestors (in MRO)

    * lark.visitors.Transformer
    * lark.visitors._Decoratable
    * abc.ABC
    * typing.Generic

    ### Class variables

    `DOUBLE_QUOTE_CONTENT`
    :   str(object='') -> str
        str(bytes_or_buffer[, encoding[, errors]]) -> str
        
        Create a new string object from the given object. If encoding or
        errors is specified, then the object must expose a data buffer
        that will be decoded using the given encoding and error handler.
        Otherwise, returns the result of object.__str__() (if defined)
        or repr(object).
        encoding defaults to sys.getdefaultencoding().
        errors defaults to 'strict'.

    `UNQUOTED`
    :   str(object='') -> str
        str(bytes_or_buffer[, encoding[, errors]]) -> str
        
        Create a new string object from the given object. If encoding or
        errors is specified, then the object must expose a data buffer
        that will be decoded using the given encoding and error handler.
        Otherwise, returns the result of object.__str__() (if defined)
        or repr(object).
        encoding defaults to sys.getdefaultencoding().
        errors defaults to 'strict'.

    ### Methods

    `WHITESPACE(self, tok)`
    :

    `arguments(self, args)`
    :

    `backquoted_call(self, args)`
    :

    `call(self, args)`
    :

    `command(self, args)`
    :

    `double_quoted(self, args)`
    :

    `quoted(self, args)`
    :

    `word(self, args)`
    :