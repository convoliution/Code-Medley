import numpy as np


def camel_to_snake(camel):
    """
    Converts a camelCase string into snake_case.

    Up to twice as fast as a pre-compiled regex.

    Parameters
    ----------
    camel : str
        camelCase string.

    Returns
    -------
    snake : str
        snake_case string.

    """
    uppers = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join(
        [camel[0]]  # avoid prepending an underscore when the first letter is capital
        + ['_'+char
           if char in uppers
           else char
           for char in camel[1:]]
    ).lower()
