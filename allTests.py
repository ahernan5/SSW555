from prettytable import PrettyTable
from userstories.ahUserStories import us02, us03
from userstories.msUserStories import us35, us36, us41, us42
from userstories.fdUserStories import us07, us06
import unittest
import sys
import os
sys.path.append(os.path.abspath('../userstories'))


class Tests(unittest.TestCase):

    def test_us02(self):
        input = {'individualData': {'@I1@': {'NAME': 'HUSB', 'BIRT': '2018-03-07'}, '@I2@': {'NAME': 'WIFE', 'BIRT': '2018-03-07'}},
                 'familyData': {'@F1@': {'HUSB': '@I1@', 'HUSB_NAME': 'HUSB', 'WIFE': '@I2@', 'WIFE_NAME': 'WIFE', 'MARR': '2018-03-06', 'MARRLine': '18'}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name',
                                 'Husband Birthday', 'Wife ID', 'Wife Name', 'Wife Birthday', '[US40] Line Number']
        testTable.add_row(['@F1@', '2018-03-06', '@I1@', 'HUSB',
                          '2018-03-07', '@I2@', 'WIFE', '2018-03-07', '18'])

        output = testTable
        self.assertEqual(us02(input).get_string(), output.get_string())


    def test_us41(self):
        input = "MAR 2000"  # Date without Days
        output = "01 MAR 2000"

        self.assertEqual(us41(input), output)

    def test_us41_2(self):
        input = "1900"  # Date without Days and Months
        output = "01 JAN 1900"

        self.assertEqual(us41(input), output)

    def test_us42(self):
        input = "29 FEB 2015"   # Illegitimate Date - Leap Day on non-Leap Year
        output = "N/A"

        self.assertEqual(us42(input), output)

    def test_us42_2(self):
        input = "42 MAR 2018"   # Illegitimate Date - Illegal Day
        output = 'N/A'

        self.assertEqual(us42(input), output)

    def test_us42_3(self):
        input = "04 APR 1908"   # Legitimate Date
        output = "04 APR 1908"

        self.assertEqual(us42(input), output)

    def test_us42_4(self):
        input = "07 NOV 3000"   # Date in the future
        output = "07 NOV 3000"

        self.assertEqual(us42(input), output)

    # Frankie Test Cases

    # def test_us07(self):
    #     self.maxDiff = None
    #     input = {'individualData': {'@I1@': {'NAME': 'HUSB', 'BIRT': '1700-03-07', 'DEAT': '2020-02-27'}, '@I2@': {'NAME': 'WIFE', 'BIRT': '1700-03-07', 'DEAT': 'N/A'}},
    #              'familyData': {}}

    #     invalidAgeTable = PrettyTable()
    #     invalidAgeTable.field_names = ['ID', 'Name', 'Birthday', 'Deathday']

    #     invalidAgeTable.add_row(['@I1@', 'HUSB', '1700-03-07', '2020-02-27'])
    #     invalidAgeTable.add_row(['@I2@', 'WIFE', '1700-03-07', 'N/A'])

    #     output = invalidAgeTable
    #     self.assertEqual(us07(input).get_string(), output.get_string())


unittest.main()
