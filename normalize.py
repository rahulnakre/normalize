import numpy as np


def normalize(a: 'np.ndarray'):
    """Simple function to normalize, for future reference
    """
    if type(a) != np.ndarray:
        raise ValueError("Object passed was not of type numpy.ndarray")
    a_max, a_min = a.max(), a.min()
    a = (a - a_min) / (a_max - a_min)
    return a
