import numpy as np  # numpy.* -> np.*


def get_principal_stresses(stress_matrix):
    principal_stresses = np.linalg.eigvals(stress_matrix)
    return principal_stresses
