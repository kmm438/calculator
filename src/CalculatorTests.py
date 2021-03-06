import unittest
import csv
from CsvReader import CsvReader, ClassFactory
from pprint import pprint
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        # check to ensure this is an object of calculator
        self.assertIsInstance(self.calculator, Calculator);

    def test_addition(self):
        self.csv_reader = CsvReader('/src/Unit Test Addition.csv').data
        print("--------------TEST ADDITION:")
        for theRow in self.csv_reader:
            # pprint(theRow)

            # check to see if the sum of the first two colums equals the third
            self.assertEqual(self.calculator.add(int(theRow['Value 1']), int(theRow['Value 2'])), int(theRow['Result']))
            print("Unit test:", int(theRow['Value 1']), " + ", int(theRow['Value 2']), " = ", self.calculator.result)

    def test_subtraction(self):
        self.csv_reader = CsvReader('/src/Unit Test Subtraction.csv').data
        print("--------------TEST SUBTRACTION:")
        for theRow in self.csv_reader:
            # check to see if the difference of the first two colums equals the third
            self.assertEqual(self.calculator.subtract(int(theRow['Value 1']), int(theRow['Value 2'])),
                             int(theRow['Result']))
            print("Unit test:", int(theRow['Value 2']), " - ", int(theRow['Value 1']), " = ", self.calculator.result)

    def test_multiplication(self):
        self.csv_reader = CsvReader('/src/Unit Test Multiplication.csv').data
        print("--------------TEST MULTIPLICATION:")
        for theRow in self.csv_reader:
            # check to see if the multiple of the first two colums equals the third
            self.assertEqual(self.calculator.multiply(int(theRow['Value 1']), int(theRow['Value 2'])),
                             int(theRow['Result']))
            print("Unit test:", int(theRow['Value 2']), " * ", int(theRow['Value 1']), " = ", self.calculator.result)

    def test_division(self):
        self.csv_reader = CsvReader('/src/Unit Test Division.csv').data
        print("--------------TEST DIVISION:")
        for theRow in self.csv_reader:
            # check to see if the result of the first two colums equals the third
            self.assertEqual(self.calculator.divide(float(theRow['Value 1']), float(theRow['Value 2'])),
                             float(theRow['Result']))
            print("Unit test:", float(theRow['Value 2']), " / ", float(theRow['Value 1']), " = ",
                  self.calculator.result)

    def test_square(self):
        self.csv_reader = CsvReader('/src/Unit Test Square.csv').data
        print("--------------TEST SQUARE:")
        for theRow in self.csv_reader:
            # check to see if raising to the 2nd power of the 1st column equals the 2nd
            self.assertEqual(self.calculator.square(int(theRow['Value 1'])), float(theRow['Result']))
            print("Unit test:", float(theRow['Value 1']), " to the second power  = ",
                  self.calculator.result)

    def test_sqrt(self):
        self.csv_reader = CsvReader('/src/Unit Test Square Root.csv').data
        print("--------------TEST SQUARE ROOT:")
        for theRow in self.csv_reader:
            # check to see if the sqrt of the first column equals the 2nd

            value1 = self.calculator.sqrt(float((theRow['Value 1'])))
            value2 = float(theRow['Result'])
            self.assertEqual(round(value1,8), round(value2,8))
            print("Unit test:", float(theRow['Value 1']), "'s sqrt is = ",
                  self.calculator.result)

    # def test_results_property_calculator(self):
    #     self.assertEqual(self.calculator.result, 4)
    #
    # def test_add_method_calculator(self):
    #     self.assertEqual(self.calculator.add(2, 2), 4)
    #     self.assertEqual(self.calculator.result, 4)
    #
    # def test_subtraction_method_calculator(self):
    #     self.assertEqual(self.calculator.subtract(2, 2), 0)
    #     self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
