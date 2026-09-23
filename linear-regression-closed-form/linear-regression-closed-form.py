import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    x_new, y_new = np.array(X), np.array(y)
    a = np.linalg.inv(x_new.T @ x_new)
    b = (x_new.T @ y)
    z = a @ b
    return (z.tolist())
    pass