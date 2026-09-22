import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    a= np.array(x)
    b= np.array(y)
    z= np.dot(a, b)
    return float(z) 
    pass