import unittest
import numpy as np
import numpy.testing as npt
import task

class TestMatrixMultiplication(unittest.TestCase):

    def test_matrix_multiplication(self):
        # Exemple de matrices A, x et B
        T=task()
        A = T.a
        x = T.x           # Vecteur x (2x1)
        B = T.b       # Résultat attendu B (2x1)

        result = np.dot(A, x)

        # Vérification que A * x est proche de B (vérification d'égalité numérique)
        npt.assert_allclose(result, B, rtol=1e-5, atol=1e-8, err_msg="A * x n'est pas égal à B")

if __name__ == '__main__':
    unittest.main()
