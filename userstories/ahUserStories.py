import datetime
from prettytable import PrettyTable


# __________________Sprint 1__________________
def us02(GEDCOM_dict):

    invalidDateTable = PrettyTable()
    invalidDateTable.field_names = ['FAM ID', 'Married', 'Husband ID', 'Husband Name',
                                    'Husband Birthday', 'Wife ID', 'Wife Name', 'Wife Birthday', '[US40] Line Number']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']
    for key, value in familyData.items():
        if (value['MARR'] != 'N/A'):
            # Checks that the Husband's and Wife's Marriage Date does not occur before their respective birthdays
            marr_date = datetime.datetime.strptime(
                " ".join(value['MARR'].split('-')), '%Y %m %d')
            if (individualData[value['HUSB']]['BIRT'] != 'N/A'):
                husb_birt = datetime.datetime.strptime(
                    " ".join(individualData[value['HUSB']]['BIRT'].split('-')), '%Y %m %d')
            else:
                husb_birt = datetime.datetime.min

            if (individualData[value['WIFE']]['BIRT'] != 'N/A'):
                wife_birt = datetime.datetime.strptime(
                    " ".join(individualData[value['WIFE']]['BIRT'].split('-')), '%Y %m %d')
            else:
                wife_birt = datetime.datetime.min

            if (husb_birt >= marr_date or wife_birt >= marr_date):
                invalidDateTable.add_row([key, value['MARR'], value['HUSB'], value['HUSB_NAME'], individualData[value['HUSB']]
                                         ['BIRT'], value['WIFE'], value['WIFE_NAME'], individualData[value['WIFE']]['BIRT'], value['MARRLine']])

    return invalidDateTable
