import unittest
import csv
from CsvReader import CsvReader, ClassFactory
from pprint import pprint
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator);

    def test_addition(self):
        self.csv_reader = CsvReader('/src/Unit Test Addition.csv').data

        for theRow in self.csv_reader:
            pprint(theRow)
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
