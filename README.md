# Code Medley
Little things I've written that aren't quite big enough to be in their own repositories, but are nonetheless interesting and worth sharing (in my humble opinion)!

# Contents
## `Julia/`
### `Regression.ipynb`
- Implementation of linear and quadratic regression by gradient descent
## `Python/`
### `Linked_List.ipynb`
- Implementation of a linked list using lambdas
### `PCA.ipynb`
- Demonstration of principal component analysis from `datasci.py`
### `datasci.py`
- Implementation of a [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis)-based algorithm for reducing data to two dimensions
### `linalg.py`
- Function for calculating an eigenvalue of a matrix given a corresponding eigenvector  
- Function for estimating an eigenvector of a matrix given a corresponding eigenvalue
  - Uses the [inverse iteration](https://en.wikipedia.org/wiki/Inverse_iteration) algorithm
- Function for estimating the covariance matrix of a data matrix
- Function for estimating the top eigenvector of a matrix
  - Uses the [power iteration](https://en.wikipedia.org/wiki/Power_iteration) algorithm
- Function for matrix deflation to nullify an eigenpair
  - Uses the Wielandt deflation algorithm
- Function for the LU decomposition of a square matrix
### `utils.py`
- Function for converting a camelCase string to snake_case
### `dnd.py`
- Object and utility class for simulating dice rolls
### `graphs.py`
- Classes and algorithms for graphs
### `binarysearch.py`
- One-liner `Python<3.8` implementation of binary search
## `Rust/`
### `quicksort.rs`
- Implementation of Hoare's partitioning algorithm, with the middle index selected as the pivot
