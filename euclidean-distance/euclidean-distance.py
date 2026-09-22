import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    a = np.array(x)
    b = np.array(y)
    z = np.sqrt(np.sum((a - b)**2))
    return float(z)
    pass