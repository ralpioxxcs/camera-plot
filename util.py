import numpy as np

def toHomogeneous(A) :
    """ Convert inhomogeneous to homogeneous representation
        (x, y) -> (x, y, 1)
    """
    A = np.atleast_2d(A)
    N = A.shape[0]
    return np.hstack((A, np.ones((N,1))))

def toInHomogeneous(A) :
    """ Convert homogeneous to inhomogeneous representation
        (x,y,z) -> (x/z, y/z)
    """
    A = np.atleast_2d(A)
    A /= A[:,-1][:, np.newaxis]
    return A[:,:-1]

# if __name__ == "__main__":
#     x = np.array([[0,6,1],[0,12,1]])
#     print(toHomogeneous(x))
#     print(toInHomogeneous(x))
