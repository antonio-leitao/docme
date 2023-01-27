"""Docstring for the module `module_with_functions.py`.

This module as an example functions with some warnings and deprecations examples.
It is not much different than the other module but its put here for completeness and for adding content to the TOC.

"""


def deprecated_function(var1, var2, long_var_name=None, *args):
    """This function is deprecated.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    *args : iterable
        Other arguments.

    Returns
    -------
    var3 : int
        Returns `var3` which is of type ``int``.

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    $$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

    And even use a Greek symbol like $\omega$ inline.

    Warnings
    --------
    Deprecation Warnign: `deprecated_function` will be removed in version 2.0.0, it is replaced by `better_function` because the new one is blazingly fast.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> b = deprecated_function(a)
    >>> print(b)
    [4,5,6]
    """
    pass


def better_function(var1, var2, long_var_name=None, *args):
    """This function is much better than the one that is deprecated.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    *args : iterable
        Other arguments.

    Returns
    -------
    var3 : int
        Returns `var3` which is of type ``int``.

    Warnings
    --------
    This function will replace the deprecated function in version 2.0.0.
    This is another warning, warning the user that this function is blazingly fast!

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> b = better_function(a)
    >>> print(b)
    [10,11,12]
    """
    pass
