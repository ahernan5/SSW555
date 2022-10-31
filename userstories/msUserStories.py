import datetime
import prettytable
from natsort import natsorted

# User stories 35, 36, 41, 42, 30, 39

# __________________Sprint 1__________________

# List all people in a GEDCOM file who were born in the last 30 days


def us35(GEDCOM_dict):

    recentBirtTable = prettytable.PrettyTable()
    recentBirtTable.field_names = ['ID', 'Name', 'Birthday']

    for key, value in GEDCOM_dict['individualData'].items():
        if (value['BIRT'] and value['BIRT'] != 'N/A'):
            birthdate = datetime.datetime.strptime(
                " ".join(value['BIRT'].split('-')), '%Y %m %d')
            today = datetime.datetime.now()

            if(birthdate >= today + datetime.timedelta(-30) and birthdate <= today):
                row = [key, value['NAME'], value['BIRT']]
                recentBirtTable.add_row(row)

    return recentBirtTable


# List all people in a GEDCOM file who died in the last 30 days
def us36(GEDCOM_dict):

    recentDeatTable = prettytable.PrettyTable()
    recentDeatTable.field_names = ["ID", "Name", "Death"]

    for key, value in GEDCOM_dict['individualData'].items():
        if (value['DEAT'] and value['DEAT'] != 'N/A'):
            deathdate = datetime.datetime.strptime(
                " ".join(value['DEAT'].split('-')), '%Y %m %d')
            today = datetime.datetime.now()
            if(deathdate >= today + datetime.timedelta(-30) and deathdate <= today):
                row = [key, value['NAME'], value['DEAT']]
                recentDeatTable.add_row(row)

    return recentDeatTable


# __________________Sprint 2__________________
# Include Partial Dates - Accept and use dates without days or without days and months

def us41(date):
    dateSplit = date.split(" ")
    if (len(dateSplit) < 3):
        if (len(dateSplit) == 2):  # Dates without days
            dateWithDefaultDay = f'01 {dateSplit[0]} {dateSplit[1]}'
            return dateWithDefaultDay
        if (len(dateSplit) == 1):  # Dates without days and months
            dateWithDefaultDayAndMonth = f'01 JAN {dateSplit[0]}'
            return dateWithDefaultDayAndMonth
    elif (len(dateSplit) == 3):
        return date
    else:
        return 'N/A'


# Reject illegitimate dates
def us42(date):

    try:
        datetime.datetime.strptime(date, '%d %b %Y')
    except ValueError:
        return 'N/A'

    return date

# __________________Sprint 3__________________

# List all living married people in a GEDCOM file


def us30(GEDCOM_dict):
    livingMarriedTable = prettytable.PrettyTable()
    livingMarriedTable.field_names = ['ID', 'Name']

    individualData = GEDCOM_dict['individualData']
    familyData = GEDCOM_dict['familyData']
    idListSorted = natsorted(individualData.keys())

    for id in idListSorted:
        if (individualData[id]['ALIVE'] == 'True'):
            if (individualData[id]['FAMS'] == 'N/A'):
                continue
            else:
                fams = individualData[id]['FAMS']
                for famId in fams:
                    if (familyData[famId]['DIV'] == 'N/A'):
                        livingMarriedTable.add_row(
                            [id, individualData[id]['NAME']])
                    else:
                        continue
        else:
            continue

    return livingMarriedTable


# List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
def us39(GEDCOM_dict):

    upcomingAnniversariesTable = prettytable.PrettyTable()
    upcomingAnniversariesTable.field_names = [
        "Family ID", "Husband", "Wife", "Marriage Date"]

    for key, value in GEDCOM_dict['familyData'].items():
        if (value['MARR'] and value['MARR'] != 'N/A'):
            marriagedate = datetime.datetime.strptime(
                " ".join(value['MARR'].split('-')), '%Y %m %d')
            marriagedate = marriagedate.replace(year=2022)
            today = datetime.datetime.now()

            if(marriagedate <= today + datetime.timedelta(30)) and marriagedate >= today:
                row = [key, value['HUSB_NAME'],
                       value['WIFE_NAME'], value['MARR']]
                upcomingAnniversariesTable.add_row(row)

    return upcomingAnniversariesTable
