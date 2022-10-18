#  Parses Dictionary Data to Output All Errors in Individuals and Families Using Functions Imported from UserStories
#  Creates/Appends to Txt file ( {fileName}_output.txt )
#  Returns Table with Individual Data

# Python Modules
import sys
import json
from prettytable import PrettyTable

# Import userstories
from userstories import ahUserStories, fdUserStories, msUserStories, shUserStories


# Errors:

def displayErrors(fileName, GEDCOM_dict):

    us01 = fdUserStories.us01(GEDCOM_dict)
    with open(fileName + '_output.txt', 'a+') as output:
        output.write("[us01] - Error: Dates (Birth, Marriage, Divorce, Death) should not be after the current date\n")
        output.write(us01.get_string(
            title="[us01] - Error: Dates (Birth, Marriage, Divorce, Death) should not be after the current date")+'\n\n')
    print('\n[us01] Error: Dates (Birth, Marriage, Divorce, Death) should not be after the current date')
    print(us01)

    us02 = ahUserStories.us02(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us02] - Error: Birth Occurs After Marriage Date\n")
        output.write(us02.get_string(
            title="[us02] - Error: Birth Occurs After Marriage Date")+'\n\n')
    print('\n[us02] Error: Birth Occurs After Marriage Date')
    print(us02)

    us03 = ahUserStories.us03(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us03] - Error: Death Occurs Before Birth\n")
        output.write(us03.get_string(
            title="[us03] - Error: Death Occurs Before Birth")+'\n\n')
    print('\n[us03] Error: Death Occurs Before Birth')
    print(us03)

    us06 = fdUserStories.us06(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us06] - Error: Divorce Occurs After Death\n")
    print('\n[us06] Error: Divorce Occurs After Death')
    print(us06)

    us07 = fdUserStories.us07(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us07] - Error: Age is Greater Than 150 Years\n")
        output.write(us07.get_string(
            title="[us07] - Error: Age is Greater Than 150 Years")+'\n\n')
    print('\n[us07] Error: Age is Greater Than 150 Years')
    print(us07)

    us21 = fdUserStories.us21(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us21] - Error: Incorrect gender for role\n")
        output.write(us21.get_string(
            title="[us21] - Error: Incorrect gender for role")+'\n\n')
    print('\n[us21] Error: Incorrect gender for role')
    print(us21)

    us23 = ahUserStories.us23(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us23] - Error: Name/Birthday Combo Not Unique\n")
        output.write(us23.get_string(
            title="[us23] - Error: Name/Birthday Combo Not Unique")+'\n\n')
    print('\n[us23] Error: Name/Birthday Combo Not Unique')
    print(us23)

    us29 = ahUserStories.us29(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us29] - Error: Deceased Individuals\n")
        output.write(us29.get_string(
            title="[us29] - Error: Deceased Individuals")+'\n\n')
    print('\n[us29] List: Deceased Individuals')
    print(us29)
    

def main(fileName, GEDCOM_dict):

    # Case when the Program is Run Directly from Command Line
    # READ FROM JSON DATA
    if (fileName.endswith('_dict.json')):
        with open(fileName) as GEDCOM_JSON:
            GEDCOM_dict = json.loads(GEDCOM_JSON.read())

        displayErrors(fileName, GEDCOM_dict)

        return
    # Case when the Program is run from 0_main.py
    else:
        if (len(GEDCOM_dict) != 0):
            displayErrors(fileName, GEDCOM_dict)

            return
        else:
            raise 'Empty Input, no GEDCOM Dictionary Data to Display'

    return


if __name__ == '__main__':
    main(sys.argv[1], {})
