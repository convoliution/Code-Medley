import numpy as np

def check_type(var, dtype):
    if not isinstance(var, dtype):
        raise TypeError("expected {} to be {}, but was {} instead"
                        .format(var, dtype, type(var)))
