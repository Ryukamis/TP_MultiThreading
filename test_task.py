import unittest
import numpy as np
import numpy.testing as npt

class TestMatrixMultiplication(unittest.TestCase):

    def test_matrix_multiplication(self):
        # Exemple de matrices A, x et B
        A = np.array([[1, 2], [3, 4]])  # Matrice A (2x2)
        x = np.array([10, 30])            # Vecteur x (2x1)
        B = np.array([17, 39])          # Résultat attendu B (2x1)

        result = np.dot(A, x)

        # Vérification que A * x est proche de B (vérification d'égalité numérique)
        npt.assert_allclose(result, B, rtol=1e-5, atol=1e-8, err_msg="A * x n'est pas égal à B")

if __name__ == '__main__':
    unittest.main()
