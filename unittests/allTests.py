# NOTE: Must run unitTest while in the unittests directory

import sys
import os
sys.path.append(os.path.abspath('C:/Users/user/Documents/SSW555Group/SSW555/userstories'))

import unittest
from msUserStories import us41, us42 , us30 , us39
from ahUserStories import us02, us03
from shUserStories import us04, us33, us37
from prettytable import PrettyTable



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


# Mehrab User Stories Tests

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

    def test_us30(self):
        testDict = {
            'individualData': {
                '@US30_01@': {
                    'NAME': 'Deceased Married /Person/',
                    'ALIVE': 'False',
                    'FAMS': ['@US30@']
                },
                '@US30_02@': {
                    'NAME': 'Living Married /Person/',
                    'ALIVE': 'True',
                    'FAMS': ['@US30@']
                }
            },
            'familyData': {
                '@US30@': {
                    'DIV': 'N/A'
                }
            }
        }

        expectedOutputTable = PrettyTable()
        expectedOutputTable.field_names = ['ID', 'Name']
        expectedOutputTable.add_row(['@US30_02@', 'Living Married /Person/'])

        self.assertEqual(us30(testDict).get_string(),
                         expectedOutputTable.get_string())


    def test_us39(self):
        input = {'familyData': {'@F1@': {'MARR': '2017-11-10', 'HUSB_NAME': 'Syed /Uddin/', 'WIFE_NAME': 'Rafia /Syed/'},
                                '@F2@': {'MARR': '1962-06-14', 'HUSB_NAME': 'Tamir /Ahmed/', 'WIFE_NAME': 'Marly /Lee/'}}}

        testTable = PrettyTable()
        testTable.field_names = ['Family ID',
                                 'Husband', 'Wife', 'Marriage Date']
        testTable.add_row(
            ['@F1@', 'Syed /Uddin/', 'Rafia /Syed/', '2017-11-10'])

        output = testTable

        self.assertEqual(us39(input).get_string(), output.get_string())


    #Austin User Story tests

    def test_us33(self):
        input = {'familyData': {'@F1@': {'MARR': '2017-11-10', 'HUSB': '@I1@', 'WIFE':'@I2@', 'CHIL': ['@I3@']}},
                 'individualData':{'@I1@':{'NAME': 'Bob /Grund/','DEAT':'2010-03-10'},'@I2@':{'NAME':'Susan /Grund/', 'DEAT':'2005-05-20'},'@I3@':{'NAME':'Mo /Grund/', 'DEAT': 'N/A', 'BIRT': '2015-06-02'}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM ID', 'Kid IDs']
        testTable.add_row(['@F1@', ['@I3@']])
        testTable.add_row(['@F1@', ['@I3@']])

        output = testTable

        self.assertEqual(us33(input).get_string(), output.get_string())

    def test_us37(self):
        input = {'familyData': {'@F1@': {'MARR': '2017-11-10', 'HUSB': '@I1@', 'WIFE':'@I2@', 'CHIL': ['@I3@']}},
                 'individualData':{'@I1@':{'NAME': 'Bob /Grund/','DEAT':'2022-10-30'},'@I2@':{'NAME':'Susan /Grund/', 'DEAT':'2005-05-20'},'@I3@':{'NAME':'Mo /Grund/', 'DEAT': 'N/A'}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM ID', 'ID', 'Death Date', 'Survivors']
        testTable.add_row(['@F1@', '@I1@', '2022-10-30', ['@I2@',['@I3@']]])

        output = testTable

        self.assertEqual(us37(input).get_string(), output.get_string())


unittest.main()
