from unittest import TestCase
from calculator import Calculator


class CalculatorTest(TestCase):
    def test_simple_expressions(self):
        self.assertEqual(Calculator.calculate('5 + 2 * 3'), float(11), '5 + 2 * 3 = 11 failure')
        self.assertEqual(Calculator.calculate('12 / 3 + 2 * 3'), float(10), '12 / 3 + 2 * 3 = 10 failure')
        self.assertEqual(Calculator.calculate('30 - 18 / 2 * 3'), float(3), '30 - 18 / 2 * 3 = 3 failure')
        self.assertEqual(Calculator.calculate('30 / 5 / 2 + 2'), float(5), '0 / 5 / 2 + 2 = 5 failure')

    def test_parenthesized_expressions(self):
        self.assertEqual(Calculator.calculate('( 5 + 2 ) * ( 3 + 1 )'), float(28), '( 5 + 2 ) * ( 3 + 1 ) = 28 failure')
        self.assertEqual(Calculator.calculate('( 5 + 7 ) / 3 * ( 2 + 1 )'), float(12),
                         '( 5 + 7 ) / 3 * ( 2 + 1 ) = 12 failure')
        self.assertEqual(Calculator.calculate('5 * 6 / 3 + ( ( 2 * 3 ) + 4 )'), float(20),
                         '5 * 6 / 3 + ( ( 2 * 3 ) + 4 ) = 20 failure')

    def test_with_sqrt(self):
        self.assertEqual(Calculator.calculate('sqrt 9 + 7'), float(10), 'sqrt 9 + 7 = 10 failure')
        self.assertEqual(Calculator.calculate('sqrt 9 * sqrt 16 - 2'), float(10), 'sqrt 9 * sqrt 16 - 2 = 10 failure')
        self.assertEqual(Calculator.calculate('sqrt ( ( 2 + 3 ) * 5 * ( 3 + 1 ) )'), float(10),
                         'sqrt ( ( 2 + 3 ) * 5 * ( 3 + 1 ) ) = 10 failure')
c