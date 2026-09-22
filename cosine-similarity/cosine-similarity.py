import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    top = np.dot(a, b)
    bots=   np.linalg.norm(a)
    bob=  np.linalg.norm(b)
    turn= bots * bob
    a= (top / turn)
    if turn == 0:
        return 0.0
    return float(a)
    
        
    

    pass