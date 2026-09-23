import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    y_a, y_b = np.array(y_pred), np.array(y_true)
    a = np.mean((y_a - y_b)**2)
    return float(a)
    
    pass