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
