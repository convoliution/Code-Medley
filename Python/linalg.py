import numpy as np
import utils

def eigval_from_vec(A: np.ndarray, eigvec: np.ndarray) -> float:
    '''
    Finds the eigenvalue of `A` that corresponds to the eigenvector `eigvec`.

    It's not feasible to internally verify that `eigvec` is an eigenvector
    of `A` due to floating point imprecision, so use with caution.

    Parameters
    ----------
    A : np.ndarray
        Two-dimensional array.
    eigvec : np.ndarray
        Eigenvector of `A`.

    Returns
    -------
    eigval : float
        Eigenvalue of `A` corresponding to eigenvector `eigvec`.

    Raises
    ------
    TypeError
        If `A` is not a np.ndarray.
    ValueError
        If `A` is not of dimensionality 2.

    '''
    utils.check_type(A, np.ndarray)
    utils.check_dim(A, 2)

    eigvec = utils.to_col(eigvec)
    return np.mean(np.dot(A, eigvec)/eigvec)

def eigvec_from_val(A: np.ndarray, eigval: float) -> np.ndarray:
    '''
    Estimates the eigenvector of `A` that corresponds to the eigenvalue `eigval`

    Calculated via inverse iteration [1]_.

    It's not feasible to internally verify that `eigval` is an eigenvalue
    of `A` due to floating point imprecision, so use with caution.

    Parameters
    ----------
    A : np.ndarray
        Two-dimensional array.
    eigvec : float
        Eigenvalue of `A`.

    Returns
    -------
    eigvec : np.ndarray
        Eigenvector of `A` corresponding to eigenvalue `eigval`.

    Raises
    ------
    TypeError
        If `A` is not a np.ndarray.
    ValueError
        If `A` is not of dimensionality 2.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Inverse_iteration

    '''
    utils.check_type(A, np.ndarray)
    utils.check_dim(A, 2)

    eigeye = eigval*np.eye(A.shape[-1])
    x = np.random.random((A.shape[-1], 1)) # random vector
    x /= np.linalg.norm(x) # scale to length 1
    while(True):
        Ax = np.dot(np.linalg.inv(A - eigeye), x)
        x_old = x
        x = Ax/(np.linalg.norm(Ax)+1e-16)
        if np.linalg.norm(np.abs(x) - np.abs(x_old)) < 1e-8:
            return x

def cov(A: np.ndarray) -> np.ndarray:
    '''
    Estimates the covariance matrix of `A`.

    Parameters
    ----------
    A : np.ndarray
        Data array of shape (N, D)
        where N is the number of data points
        and D is the dimensionality of the data.

    Returns
    -------
    cov_mat : np.ndarray
        Estimates covariance matrix of `A`

    Raises
    ------
    TypeError
        If `A` is not a np.ndarray.
    ValueError
        If `A` is not of dimensionality 2.

    '''
    utils.check_type(A, np.ndarray)
    utils.check_dim(A, 2)

    mean = np.mean(A, axis=0).reshape((1, -1))
    diff = A - mean
    return np.dot(diff.T, diff)/(A.shape[0] - 1)

def top_eigvec(A: np.ndarray) -> np.ndarray:
    '''
    Estimates the top eigenvector of `A`.

    Calculated via the power iteration algorithm [1]_.

    Parameters
    ----------
    A : np.ndarray
        Two-dimensional array.

    Returns
    -------
    eigvec : np.ndarray
        Top eigenvector of `A`.

    Raises
    ------
    TypeError
        If `A` is not a np.ndarray.
    ValueError
        If `A` is not of dimensionality 2.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Power_iteration

    '''
    utils.check_type(A, np.ndarray)
    utils.check_dim(A, 2)

    x = np.random.random((A.shape[-1], 1)) # random vector
    x /= np.linalg.norm(x) # scale to length 1
    while(True):
        Ax = np.dot(A, x)
        x_old = x
        x = Ax/(np.linalg.norm(Ax)+1e-16)
        if np.linalg.norm(np.abs(x) - np.abs(x_old)) < 1e-8:
            return x

def deflate(A: np.ndarray, eigvec: np.ndarray) -> np.ndarray:
    '''
    Performs Wielandt deflation on `A` to remove the influence of `eigvec`.

    It's not feasible to internally verify that `eigvec` is an eigenvector
    of `A` due to floating point imprecision, so use with caution.

    Parameters
    ----------
    A : np.ndarray
        Array to be deflated.
    eigvec : np.ndarray
        Eigenvector of `A`.

    Returns
    -------
    deflated_A : np.ndarray
        `A` sans the influence of `eigvec`.

    Raises
    ------
    TypeError
        If `A` is not a np.ndarray.
    ValueError
        If `A` is not of dimensionality 2.

    References
    ----------
    .. [1] https://www.colorado.edu/engineering/cas/courses.d/IFEM.d/IFEM.AppE.d/IFEM.AppE.pdf

    '''
    utils.check_type(A, np.ndarray)
    utils.check_dim(A, 2)

    eigvec = utils.to_col(eigvec)
    eigval = eigval_from_vec(A, eigvec)

    w = 1/(eigvec.size*eigvec) # np.dot(w.T, eigvec) == 1
    return A - eigval*np.dot(eigvec, w.T)