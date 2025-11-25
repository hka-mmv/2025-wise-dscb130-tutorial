import unittest
from calculation_functions import Calculation

class TestCalculation(unittest.TestCase):
    def setUp(self):
        self.calculation = Calculation()

    def test_addition(self):
        result = self.calculation.calculate("2 + 3")
        self.assertEqual(result, 5)

    def test_substraction(self):
        result = self.calculation.calculate("2 - 3")
        self.assertEqual(result, -1)

    def test_multiplication(self):
        result = self.calculation.calculate("2 * 3")
        self.assertEqual(result, 6)
    
    def test_division(self):
        result = self.calculation.calculate("6 / 3")
        self.assertEqual(result, 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("1 / 0")
        
    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("2 + ")

    def test_multiple_operations(self):
        result = self.calculation.calculate("2 + 3 * 4 - 5 / 5")
        self.assertEqual(result, 13)

    def test_last_char_is_closing_parenthesis(self):
        result = self.calculation.calculate("2 * (3 + 4)")
        self.assertEqual(result, 14)

    def test_unequal_parenthesis(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("2 * (3 + 4))")

    def test_multiple_paraenthesis(self):
        result = self.calculation.calculate("2 * (3 + (4 - 1))")
        self.assertEqual(result, 12)
    
    def test_multiple_paraenthesis1(self):
        result = self.calculation.calculate("2 * (3 + (4 - 1) * (2 + 1))")
        self.assertEqual(result, 24)

    def test_predefined_variables(self):
        result = self.calculation.calculate("c + 3")
        self.assertEqual(result, 299792461)
    
    def test_logarithm(self):
        result = self.calculation.calculate("log(100)")
        self.assertEqual(result, 2.0)

    def test_square_root(self):
        result = self.calculation.calculate("sqrt(8+8)")
        self.assertEqual(result, 4.0)

    def test_wrong_square_root(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("sqrt(-16)")

    def test_matrices_definition(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix1 = [[1, 2], [3, 4]]")

    def test_matrices_addition(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix1 = [[1, 2], [3, 4]]")
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix2 = [[4, 5], [6, 7]]")
        result = self.calculation.calculate("matrix1 + matrix2")
        self.assertEqual(result, [[5, 7], [9, 11]])

    def test_matrices_substraction(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix1 = [[1, 2], [3, 4]]")
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix2 = [[4, 5], [6, 7]]")
        result = self.calculation.calculate("matrix1 - matrix2")
        self.assertEqual(result, [[-3, -3], [-3, -3]])
    
    def test_matrices_multiplication(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("mat1 = [[12,7,3], [4,5,6], [7,8,9]]")
        with self.assertRaises(ValueError):
            self.calculation.calculate("mat2 = [[5,8,1,2], [6,7,3,0], [4,5,9,1]]")
        result = self.calculation.calculate("mat1 * mat2")
        self.assertEqual(result, [[114, 160, 60, 27],[74, 97, 73, 14],[119, 157, 112, 23]])

    def test_determinant(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix1 = [[1, 2], [3, 4]]")
        result = self.calculation.calculate("det(matrix1)")
        self.assertEqual(result, -2)

    def test_inverse(self):
        with self.assertRaises(ValueError):
            self.calculation.calculate("matrix1 = [[2, 1], [3, 4]]")
        result = self.calculation.calculate("inv(matrix1)")
        self.assertEqual(result, [[0.8, -0.2], [-0.6, 0.4]])
        
if __name__ == '__main__':
    unittest.main()