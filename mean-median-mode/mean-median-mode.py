from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    a = float(np.mean(x))
    b= float(np.median(x))
    counts = Counter(x)
    sorted_v = sorted(counts.keys())
    result = float(max(sorted_v, key=counts.get))
    return {"mean": a, "median": b, "mode": result}
    pass