import unittest
import csv
from CsvReader import CsvReader, ClassFactory
from pprint import pprint
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        #check to ensure this is an object of calculator
        self.assertIsInstance(self.calculator, Calculator);

    def test_addition(self):
        self.csv_reader = CsvReader('/src/Unit Test Addition.csv').data
        print("--------------TEST ADDITION:")
        for theRow in self.csv_reader:
            #pprint(theRow)

            #check to see if the sum of the first two colums equals the third
            self.assertEqual(self.calculator.add(int(theRow['Value 1']), int(theRow['Value 2'])), int(theRow['Result']))
            print("Unit test:", int(theRow['Value 1']), " + ", int(theRow['Value 2']), " = ", self.calculator.result)

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
