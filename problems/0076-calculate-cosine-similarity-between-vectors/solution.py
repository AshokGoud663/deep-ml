import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    # def norm(vec):
    #     res=0
    #     for i in vec:
    #         res+=i**2
    #     return res**0.5
    # def dot(a,b):
    #     res=0
    #     for i in range(len(a)):
    #         res+=a[i]*b[i]
    #     return res
    # return dot(v1,v2)/(norm(v1)*norm(v2))

    #numpy

    return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    pass