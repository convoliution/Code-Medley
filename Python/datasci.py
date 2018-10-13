import numpy as np
import linalg


def dim_red_2D(data: np.ndarray) -> np.ndarray:
    """
    Reduces data to two dimensions for easy visualization e.g. via plotting.

    Uses principal component analysis [1]_ for dimensionality reduction.
    Uses power iteration [2]_ to find the first principal component,
    and uses Wielandt deflation [3]_ with power iteration and inverse iteration [4]_ to obtain the second.

    Parameters
    ----------
    data : np.ndarray of shape (N, D)
        N data points in D dimensions.

    Returns
    -------
    data_2D : np.ndarray of shape (N, 2)
        `data` reduced to two dimensions.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Principal_component_analysis
    .. [2] https://en.wikipedia.org/wiki/Power_iteration
    .. [3] https://www.colorado.edu/engineering/cas/courses.d/IFEM.d/IFEM.AppE.d/IFEM.AppE.pdf
    .. [4] https://en.wikipedia.org/wiki/Inverse_iteration

    """
    cov_mat = linalg.cov(data)

    eigvec1 = linalg.top_eigvec(cov_mat)
    deflated_cov_mat = linalg.deflate(cov_mat, eigvec1)
    eigval2 = linalg.eigval_from_vec(deflated_cov_mat, linalg.top_eigvec(deflated_cov_mat))
    eigvec2 = linalg.eigvec_from_val(cov_mat, eigval2)

    transformation = np.concatenate((eigvec1, eigvec2), axis=1)
    return (data - np.mean(data, axis=0)) @ transformation
