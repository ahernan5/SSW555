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
# User Stories: 1, 2 , 3, 6 , 7, 21, 23, 29
# Implemented user story 41 and 42 in file 1_storeDataAsDict.py


def displayErrors(fileName, GEDCOM_dict):

    us01 = fdUserStories.us01(GEDCOM_dict)
    with open(fileName + '_output.txt', 'a+') as output:
        output.write(
            "[us01] - Error: Dates (Birth, Marriage, Divorce, Death) should not be after the current date\n")
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
    
    us14 = ahUserStories.us14(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us14] - Error: More than 5 siblings born at the same time\n")
        output.write(us14.get_string(
            title="[us14] - Error: More than 5 siblings born at the same time")+'\n\n')
    print('\n[us14] Error: More than 5 siblings born at the same time')
    print(us14)

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

    us24 = ahUserStories.us24(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us24] - Error: Unique Families by Spouses\n")
        output.write(us24.get_string(
            title="[us24] - Error: Unique Families by Spouses")+'\n\n')
    print('\n[us24] Error: Unique Families by Spouses')
    print(us24)

    us29 = ahUserStories.us29(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us29] - List: Deceased Individuals\n")
        output.write(us29.get_string(
            title="[us29] - List: Deceased Individuals")+'\n\n')
    print('\n[us29] List: Deceased Individuals')
    print(us29)

    us31 = ahUserStories.us31(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us31] - List: Living Single\n")
        output.write(us31.get_string(
            title="[us31] - List: Living Single")+'\n\n')
    print('\n[us31] List: Living Single Over 30')
    print(us31)

    us32 = ahUserStories.us32(GEDCOM_dict)
    with open(fileName[:-4] + '_output.txt', 'a+') as output:
        output.write("[us32] - List: Multiple Births\n")
        output.write(us32.get_string(
            title="[us32] - List: Multiple Births")+'\n\n')
    print('\n[us32] List: Multiple Births')
    print(us32)



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
