import datetime
import prettytable
from natsort import natsorted

# User stories 35, 36, 41, 42, 30, 39, 27, 34

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

# __________________Sprint 4__________________

# Display Individual Age
def us27(birthday, death, alive):

    if ( birthday != 'N/A' and death != 'N/A' and alive == 'False'):  # Birth and Death Date are Known (alive == 'False')
        #do date arithmetic
        birthdateSplit = birthday.split('-')
        birthMonth = str(birthdateSplit[1])
        birthDayDate = str(birthdateSplit[2])
        birthYear = str(birthdateSplit[0])

        deathdateSplit = death.split('-')
        deathMonth = str(deathdateSplit[1])
        deathDayDate = str(deathdateSplit[2])
        deathYear = str(deathdateSplit[0])

        birthDate = birthYear + birthMonth + birthDayDate
        deathDate = deathYear + deathMonth + deathDayDate

        age = int(deathDate) - int(birthDate)

        if ( age < 0 ):
            return 'N/A'

        return str(age).zfill(7)[:-4].lstrip('0').zfill(1)


    if ( birthday != 'N/A' and death == 'N/A' and alive == 'True' ): # BirthDay is known and alive == 'True', no death date
        #do date arithmetic
        birthdateSplit = birthday.split('-')
        birthMonth = str(birthdateSplit[1])
        birthDayDate = str(birthdateSplit[2])
        birthYear = str(birthdateSplit[0])
        birthDate = birthYear + birthMonth + birthDayDate

        today = datetime.datetime.today()
        dateToday = str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2)

        age = int(dateToday) - int(birthDate)

        if ( age < 0 ):
            return 'N/A'

        return str(age).zfill(7)[:-4].lstrip('0').zfill(1)

    if ( birthday == 'N/A' ):
        # Cannot calculate age
        return 'N/A'

    return 'N/A'



# List all couples who were married when the older spouse was more than twice as old as the younger spouse
def us34(GEDCOM_dict):

    largeAgeDifferenceTable = prettytable.PrettyTable()
    largeAgeDifferenceTable.field_names = [
        "FAMILY ID", "AGE DIFFERENCE", "HUSB NAME", "HUSB AGE", "WIFE NAME", "WIFE AGE"]

    for key, value in GEDCOM_dict['familyData'].items():
        if(value['HUSB'] != 'N/A' and value['WIFE'] != 'N/A'):
            husbAge = GEDCOM_dict['individualData'][value['HUSB']]['AGE']
            wifeAge = GEDCOM_dict['individualData'][value['WIFE']]['AGE']
            if(husbAge != 'N/A' and wifeAge != 'N/A'):
                husbAge = int(husbAge)
                wifeAge = int(wifeAge)
                if (husbAge >= 2*wifeAge or wifeAge >= 2*husbAge):
                    row = [key, abs(husbAge - wifeAge), value['HUSB_NAME'],
                           husbAge, value['WIFE_NAME'], wifeAge]
                    largeAgeDifferenceTable.add_row(row)

    return largeAgeDifferenceTable
