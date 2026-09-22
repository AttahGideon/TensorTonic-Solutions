import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    arr_x, arr_y = np.array(x), np.array(y)
    z = np.sum(np.abs(arr_x - arr_y))
    return float(z)
    pass