import datetime
import prettytable

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
