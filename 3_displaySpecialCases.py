#  Parses Dictionary Data to Output All Anomalies and Special Cases in Individuals and Families Using Functions Imported from UserStories
#  Creates/Appends to Txt file ( {fileName}_output.txt )
#  Returns Table with Individual Data


# Python Modules
import sys
import json
from prettytable import PrettyTable

# Import userstories
from userstories import ahUserStories, fdUserStories, msUserStories, shUserStories

# Special Cases:
# User Stories: 35, 36, 30, 39


def displaySpecialCases(fileName, GEDCOM_dict):

    outputFile = fileName[:-4] + '_output.txt'

    us35 = msUserStories.us35(GEDCOM_dict)
    with open(outputFile, 'a+') as output:
        output.write("[us35] - Birth Within the Past 30 Days\n")
        output.write(us35.get_string(
            title="[us35] - Birth Within the Past 30 Days")+'\n\n')
    print('\n[us35] Birth Within the Past 30 Days')
    print(us35)

    us36 = msUserStories.us36(GEDCOM_dict)
    with open(outputFile, 'a+') as output:
        output.write("[us36] - Death Within the Past 30 Days\n")
        output.write(us36.get_string(
            title="[us36] - Death Within the Past 30 Days")+'\n\n')
    print('\n[us36] Death Within the Past 30 Days')
    print(us36)

    us30 = msUserStories.us30(GEDCOM_dict)
    with open(outputFile, 'a+') as output:
        output.write("[us30] - Living Married People\n")
        output.write(us30.get_string(
            title="[us30] - Living Married People")+'\n\n')
    print('\n[us30] Living Married People')
    print(us30)

    us39 = msUserStories.us39(GEDCOM_dict)
    with open(outputFile, 'a+') as output:
        output.write("[us39] - List Upcoming Anniversaries\n")
        output.write(us39.get_string(
            title="[us39] - List Upcoming Anniversaries")+'\n\n')
    print('\n[us39] List Upcoming Anniversaries in the next 30 days')
    print(us39)

    return


def main(fileName, GEDCOM_dict):

    # Case when the Program is Run Directly from Command Line
    if (fileName.endswith('_dict.json')):
        # READ FROM JSON DATA
        with open(fileName) as GEDCOM_JSON:
            GEDCOM_dict = json.loads(GEDCOM_JSON.read())

        displaySpecialCases(fileName, GEDCOM_dict)

        return
    # Case when the Program is run from 0_main.py
    else:
        if (len(GEDCOM_dict) != 0):
            displaySpecialCases(fileName, GEDCOM_dict)

            return
        else:
            raise 'Empty Input'

    return


if __name__ == '__main__':
    main(sys.argv[1], {})
