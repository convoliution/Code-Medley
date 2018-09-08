import numpy as np


def eigval_from_vec(A: np.ndarray, eigvec: np.ndarray) -> float:
    '''
    Finds the eigenvalue of `A` that corresponds to the eigenvector `eigvec`.

    It's not feasible to internally verify that `eigvec` is an eigenvector
    of `A` due to floating point imprecision, so use with caution.

    Parameters
    ----------
    A : np.ndarray of shape (M, M)
        Matrix.
    eigvec : np.ndarray of shape (M, 1)
        Eigenvector of `A`.

    Returns
    -------
    eigval : float
        Eigenvalue of `A` corresponding to eigenvector `eigvec`.

    '''
    return np.mean((A @ eigvec)/eigvec)


def eigvec_from_val(A: np.ndarray, eigval: float) -> np.ndarray:
    '''
    Estimates the eigenvector of `A` that corresponds to the eigenvalue `eigval`

    Calculated via inverse iteration [1]_.

    It's not feasible to internally verify that `eigval` is an eigenvalue
    of `A` due to floating point imprecision, so use with caution.

    Parameters
    ----------
    A : np.ndarray of shape (M, M)
        Matrix.
    eigval : float
        Eigenvalue of `A`.

    Returns
    -------
    eigvec : np.ndarray of shape (M, 1)
        Eigenvector of `A` corresponding to eigenvalue `eigval`.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Inverse_iteration

    '''
    eigeye = eigval*np.eye(A.shape[-1])
    x = np.random.random((A.shape[-1], 1)) # random vector
    x /= np.linalg.norm(x) # scale to length 1
    while(True):
        Ax = (np.linalg.inv(A - eigeye)) @ x
        x_old = x
        x = Ax/(np.linalg.norm(Ax)+1e-16)
        if np.linalg.norm(np.abs(x) - np.abs(x_old)) < 1e-8:
            return x


def cov(A: np.ndarray) -> np.ndarray:
    '''
    Estimates the covariance matrix of `A`.

    Parameters
    ----------
    A : np.ndarray of shape (M, N)
        Matrix.

    Returns
    -------
    cov_mat : np.ndarray of shape (N, N)
        Estimate of the covariance matrix of `A`.

    '''
    mean = A.mean(axis=0, keepdims=True)
    diff = A - mean
    return (diff.T @ diff)/(A.shape[0] - 1)


def top_eigvec(A: np.ndarray) -> np.ndarray:
    '''
    Estimates the top eigenvector of `A`.

    Calculated via the power iteration algorithm [1]_.

    Parameters
    ----------
    A : np.ndarray of shape (M, M)
        Matrix.

    Returns
    -------
    eigvec : np.ndarray of shape (M, 1)
        Top eigenvector of `A`.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Power_iteration

    '''
    x = np.random.random((A.shape[-1], 1)) # random vector
    x /= np.linalg.norm(x) # scale to length 1
    while(True):
        Ax = A @ x
        x_old = x
        x = Ax/(np.linalg.norm(Ax)+1e-16)
        if np.linalg.norm(np.abs(x) - np.abs(x_old)) < 1e-8:
            return x


def deflate(A: np.ndarray, eigvec: np.ndarray) -> np.ndarray:
    '''
    Performs Wielandt deflation [1]_ on `A` to remove the influence of `eigvec`.

    It's not feasible to internally verify that `eigvec` is an eigenvector
    of `A` due to floating point imprecision, so use with caution.

    Parameters
    ----------
    A : np.ndarray of shape (M, M)
        Matrix to be deflated.
    eigvec : np.ndarray of shape (M, 1)
        Eigenvector of `A`.

    Returns
    -------
    deflated_A : np.ndarray of shape (M, M)
        `A` without the influence of `eigvec`.

    References
    ----------
    .. [1] https://www.colorado.edu/engineering/cas/courses.d/IFEM.d/IFEM.AppE.d/IFEM.AppE.pdf

    '''
    eigvec = eigvec.reshape((-1, 1))
    eigval = eigval_from_vec(A, eigvec)

    w = 1/(eigvec.size*eigvec) # w.T @ eigvec == 1
    return A - eigval*(eigvec @ w.T)
