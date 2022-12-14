# NOTE: Must run unitTest while in the unittests directory

import sys
import os

sys.path.append(os.path.abspath('../userstories'))

import unittest
from msUserStories import us41, us42 , us30 , us39
from ahUserStories import us02, us03, us23, us29, us31, us32, us14   
from fdUserStories import us15, us38, us16, us25
from prettytable import PrettyTable



class Tests(unittest.TestCase):

# Alyssa User Stories Tests 

    def test_us02(self):
        input = {'individualData': {'@I1@': {'NAME': 'HUSB', 'BIRT': '2018-03-07'}, 
            '@I2@': {'NAME': 'WIFE', 'BIRT': '2018-03-07'}},
            'familyData': {'@F1@': {'HUSB': '@I1@', 'HUSB_NAME': 'HUSB', 'WIFE': '@I2@', 'WIFE_NAME': 'WIFE', 'MARR': '2018-03-06', 'MARRLine': '18'}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name',
                                 'Husband Birthday', 'Wife ID', 'Wife Name', 'Wife Birthday', '[US40] Line Number']
        testTable.add_row(['@F1@', '2018-03-06', '@I1@', 'HUSB',
                          '2018-03-07', '@I2@', 'WIFE', '2018-03-07', '18'])

        output = testTable
        self.assertEqual(us02(input).get_string(), output.get_string())

    def test_us03(self):
        input = {'individualData': {'@I1@': {'NAME': 'Jose', 'BIRT': '2018-03-07', 'DEAT': '2017-05-04'}, 
            '@I2@': {'NAME': 'Pete', 'BIRT': '2016-07-03', 'DEAT': '2017-03-03'}}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday', 'Death'] 
        testTable.add_row(['@I1@', 'Jose', '2018-03-07', '2017-05-04'])

        output = testTable
        self.assertEqual(us03(input).get_string(), output.get_string())

    def test_us23(self):
        input = {'individualData': {'@I1@': {'NAME': 'Jose', 'BIRT': '2018-03-07'}, 
            '@I2@': {'NAME': 'Jose', 'BIRT': '2018-03-07'}}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday']
        testTable.add_row(['@I1@', 'Jose', '2018-03-07'])
        testTable.add_row(['@I2@', 'Jose', '2018-03-07'])

        output = testTable
        self.assertEqual(us23(input).get_string(), output.get_string())

    def test_us29(self):
        input = {'individualData': {'@I1@': {'NAME': 'Jose', 'BIRT': '1985-03-07', 'DEAT': '2018-05-04'}, 
            '@I2@': {'NAME': 'Pete', 'BIRT': '1965-07-03', 'DEAT': '2017-03-03'}, 
            '@I3@': {'NAME': 'Olivia', 'BIRT': '2009-07-03', 'DEAT': 'N/A'}}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday', 'Death']
        testTable.add_row(['@I1@', 'Jose', '1985-03-07', '2018-05-04'])
        testTable.add_row(['@I2@', 'Pete', '1965-07-03', '2017-03-03'])

        output = testTable
        self.assertEqual(us29(input).get_string(), output.get_string())  

    def test_us31(self):
        input = {'individualData': {'@I1@': {'NAME': 'Jose', 'BIRT': '1985-03-07', 'DEAT': 'N/A', 'FAMS': 'N/A'}, 
            '@I2@': {'NAME': 'Pete', 'BIRT': '1965-07-03', 'DEAT': '2017-03-03', 'FAMS': 'N/A'}, 
            '@I3@': {'NAME': 'Olivia', 'BIRT': '2009-07-03', 'DEAT': 'N/A', 'FAMS': 'N/A'}}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Age']
        testTable.add_row(['@I1@', 'Jose', '37'])

        output = testTable
        self.assertEqual(us31(input).get_string(), output.get_string())

    def test_us32(self):
        input = {'individualData': {'@I2@': {'NAME': 'Jose', 'BIRT': '2009-03-07', 'FAMC': '@F1@'}, 
            '@I3@': {'NAME': 'Pete', 'BIRT': '2009-03-07', 'FAMC': '@F1@'}},
            'familyData': {'@F1@': {'CHIL': ['@I2@', '@I3@'], 'WIFE_NAME': 'Olivia'}}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday', 'Family ID', 'Wife Name']
        testTable.add_row(['@I2@', 'Jose', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I3@', 'Pete', '2009-03-07', '@F1@', 'Olivia'])

        output = testTable
        self.assertEqual(us32(input).get_string(), output.get_string())

    def test_us14(self):
        input = {'individualData': {'@I1@': {'NAME': 'Jade', 'BIRT': '2009-03-07', 'FAMC': '@F1@'},
            '@I2@': {'NAME': 'Jose', 'BIRT': '2009-03-07', 'FAMC': '@F1@'}, 
            '@I3@': {'NAME': 'Pete', 'BIRT': '2009-03-07', 'FAMC': '@F1@'},
            '@I4@': {'NAME': 'Kaitlyn', 'BIRT': '2009-03-07', 'FAMC': '@F1@'},
            '@I5@': {'NAME': 'Bryan', 'BIRT': '2009-03-07', 'FAMC': '@F1@'},
            '@I6@': {'NAME': 'Katie', 'BIRT': '2009-03-07', 'FAMC': '@F1@'}},
            'familyData': {'@F1@': {'CHIL': ['@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@'], 'WIFE_NAME': 'Olivia'}}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday', 'Family ID', 'Wife Name']
        testTable.add_row(['@I1@', 'Jade', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I1@', 'Jade', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I1@', 'Jade', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I1@', 'Jade', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I1@', 'Jade', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I2@', 'Jose', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I2@', 'Jose', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I2@', 'Jose', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I2@', 'Jose', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I2@', 'Jose', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I3@', 'Pete', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I3@', 'Pete', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I3@', 'Pete', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I3@', 'Pete', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I3@', 'Pete', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I4@', 'Kaitlyn', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I4@', 'Kaitlyn', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I4@', 'Kaitlyn', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I4@', 'Kaitlyn', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I4@', 'Kaitlyn', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I5@', 'Bryan', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I5@', 'Bryan', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I5@', 'Bryan', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I5@', 'Bryan', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I5@', 'Bryan', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I6@', 'Katie', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I6@', 'Katie', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I6@', 'Katie', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I6@', 'Katie', '2009-03-07', '@F1@', 'Olivia'])
        testTable.add_row(['@I6@', 'Katie', '2009-03-07', '@F1@', 'Olivia'])
        
        output = testTable
        self.assertEqual(us14(input).get_string(), output.get_string())


   
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
        input = {'familyData': {'@F1@': {'MARR': '2017-12-25', 'HUSB_NAME': 'Syed /Uddin/', 'WIFE_NAME': 'Rafia /Syed/'},
                                '@F2@': {'MARR': '1962-06-14', 'HUSB_NAME': 'Tamir /Ahmed/', 'WIFE_NAME': 'Marly /Lee/'}}}

        testTable = PrettyTable()
        testTable.field_names = ['Family ID',
                                 'Husband', 'Wife', 'Marriage Date']
        testTable.add_row(
            ['@F1@', 'Syed /Uddin/', 'Rafia /Syed/', '2017-12-25'])

        output = testTable
        self.assertEqual(us39(input).get_string(), output.get_string())

# Frankie user stories

    def test_us38(self):
        input = {'individualData': {'@I1@': {'NAME': 'Bobby', 'BIRT': '2018-12-25'}, 
            '@I2@': {'NAME': 'Tiffany', 'BIRT': '2018-03-07'}},
            'familyData': {}}

        testTable = PrettyTable()
        testTable.field_names = ['ID', 'Name', 'Birthday']
        testTable.add_row(['@I1@', 'Bobby', '2018-12-25'])

        output = testTable
        self.assertEqual(us38(input).get_string(), output.get_string())

    def test_us15(self):
        input = {'individualData': {'@I2@': {'NAME': 'Jose', 'BIRT': '2009-03-07', 'FAMC': '@F1@'}, 
            '@I3@': {'NAME': 'Pete', 'BIRT': '2009-03-07', 'FAMC': '@F1@'}},
            'familyData': {'@F1@': {'CHIL': ['@I2@', '@I3@', '@I2@', '@I3@', '@I2@', '@I3@', '@I2@', '@I3@', '@I2@', '@I3@', '@I2@', '@I3@','@I2@', '@I3@', '@I2@', '@I3@'], 'WIFE_NAME': 'Olivia'}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM_ID', 'Number of Children']
        testTable.add_row(['@F1@', 16])

        output = testTable
        self.assertEqual(us15(input).get_string(), output.get_string())

    def test_us16(self):
        input = {'individualData': {'@I3@': {'NAME': 'Ray /Hernandez/'}, '@I4@': {'NAME': 'Bobby /Hernandez/', 'SEX': 'M'}, 
            '@I5@': {'NAME': 'Pete /smith/', 'SEX': 'M'}},
            'familyData': {'@F1@': {'HUSB': '@I3@', 'CHIL': ['@I4@', '@I5@']}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM_ID', 'Male Family Member', 'Family Name']
        testTable.add_row(['@F1@', '/smith/', '/Hernandez/'])

        output = testTable
        self.assertEqual(us16(input).get_string(), output.get_string())

    def test_us25(self):
        input = {'individualData': {'@I3@': {'NAME': 'Ray /Hernandez/'}, '@I4@': {'NAME': 'Bobby /Hernandez/', 'SEX': 'M', 'BIRT': '2001-05-26'}, 
            '@I5@': {'NAME': 'Bobby /Hernandez/', 'SEX': 'M', 'BIRT': '2001-05-26'}},
            'familyData': {'@F1@': {'HUSB': '@I3@', 'CHIL': ['@I4@', '@I5@']}}}

        testTable = PrettyTable()
        testTable.field_names = ['FAM_ID', 'Family Member 1', 'Family Member 2']
        testTable.add_row(['@F1@', '@I4@', '@I5@'])
        testTable.add_row(['@F1@', '@I5@', '@I4@'])

        output = testTable
        self.assertEqual(us25(input).get_string(), output.get_string())

unittest.main()
