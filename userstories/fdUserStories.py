from bisect import bisect_right
import datetime
from prettytable import PrettyTable


# __________________Sprint 1__________________

# Dates before current date
def us01(GEDCOM_dict):

    invalidDateTable = PrettyTable()
    invalidDateTable.field_names = ['ID', 'Date', 'Type']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']

    for key, value in familyData.items():
        if (value['MARR'] != 'N/A'):
            marr_date = datetime.datetime.strptime(
                " ".join(value['MARR'].split('-')), '%Y %m %d')

            if (datetime.datetime.today() < marr_date or datetime.datetime.today() < marr_date):
                invalidDateTable.add_row([key, marr_date, "Marriage"])

        if (value['DIV'] != 'N/A'):
            div_date = datetime.datetime.strptime(
                " ".join(value['DIV'].split('-')), '%Y %m %d')

            if (datetime.datetime.today() < div_date or datetime.datetime.today() < div_date):
                invalidDateTable.add_row([key, div_date, "Divorce"])


    for key, value in individualData.items():
        if (value['BIRT'] and value['BIRT'] != 'N/A'):
            birthdate = datetime.datetime.strptime(
                " ".join(value['BIRT'].split('-')), '%Y %m %d')
            if(datetime.datetime.today() < birthdate):
                row = [key, birthdate, "Birthday"]
                invalidDateTable.add_row(row)
        if (value['DEAT'] and value['DEAT'] != 'N/A'):
            deathdate = datetime.datetime.strptime(
                " ".join(value['DEAT'].split('-')), '%Y %m %d')
            if(datetime.datetime.today() < deathdate):
                row = [key, deathdate, "Death"]
                invalidDateTable.add_row(row)
        
    return invalidDateTable


# Divorce before death
def us06(GEDCOM_dict):

    invalidDivorceTable = PrettyTable()
    invalidDivorceTable.field_names = ['FAM ID', 'Divorce', 'Husband ID', 'Husband Name',
                                    'Husband Death', 'Wife ID', 'Wife Name', 'Wife Death', 'Div Line Number']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']
    for key, value in familyData.items():
        if (value['DIV'] != 'N/A'):
            # Checks that the Husband's and Wife's Marriage Date does not occur before their respective deaths 
            div_date = datetime.datetime.strptime(
                " ".join(value['DIV'].split('-')), '%Y %m %d')
            if (individualData[value['HUSB']]['DEAT'] != 'N/A'):
                husb_death = datetime.datetime.strptime(
                    " ".join(individualData[value['HUSB']]['DEAT'].split('-')), '%Y %m %d')
            else:
                husb_death = datetime.datetime.min

            if (individualData[value['WIFE']]['DEAT'] != 'N/A'):
                wift_death = datetime.datetime.strptime(
                    " ".join(individualData[value['WIFE']]['DEAT'].split('-')), '%Y %m %d')
            else:
                wift_death = datetime.datetime.min

            if (div_date >= husb_death or  div_date >= wift_death):
                invalidDivorceTable.add_row([key, value['DIV'], value['HUSB'], value['HUSB_NAME'], individualData[value['HUSB']]
                                         ['DEAT'], value['WIFE'], value['WIFE_NAME'], individualData[value['WIFE']]['DEAT'], value['DIVLine']])
    
    return invalidDivorceTable

# __________________Sprint 2__________________

# Less than 150 years old
def us07(GEDCOM_dict):
    
        invalidAgeTable = PrettyTable()
        invalidAgeTable.field_names = ['ID', 'Name', 'Birthday', 'Deathday', 'Age']
    
        individualData = GEDCOM_dict['individualData']
        for key, value in individualData.items():
            if (value['BIRT'] and value['BIRT'] != 'N/A'):
                birthdate = datetime.datetime.strptime(
                    " ".join(value['BIRT'].split('-')), '%Y %m %d')
                if (value['DEAT'] and value['DEAT'] != 'N/A'):
                    deathdate = datetime.datetime.strptime(
                        " ".join(value['DEAT'].split('-')), '%Y %m %d')
                    age = deathdate.year - birthdate.year - \
                        ((deathdate.month, deathdate.day) <
                        (birthdate.month, birthdate.day))
                else:
                    age = datetime.datetime.today().year - birthdate.year - \
                        ((datetime.datetime.today().month, datetime.datetime.today().day) <
                        (birthdate.month, birthdate.day))
                if (age > 150):
                    row = [key, value['NAME'], value['BIRT'], value['DEAT'], age]
                    invalidAgeTable.add_row(row)
        return invalidAgeTable

# Husband in family should be male and wife in family should be female
def us21(GEDCOM_dict):
    invalidGenderRolesTable = PrettyTable()
    invalidGenderRolesTable.field_names = ['FAM ID', 'Name', 'Role', 'Gender']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']
    for key, value in familyData.items():
        if (value['MARR'] != 'N/A'):
            if (individualData[value['HUSB']]['SEX'] != 'M'):
                row = [key, individualData[value['HUSB']]['NAME'], 'Husband', individualData[value['HUSB']]['SEX']]
                invalidGenderRolesTable.add_row(row)
            if (individualData[value['WIFE']]['SEX'] != 'F'):
                row = [key, individualData[value['WIFE']]['NAME'], 'Wife', individualData[value['WIFE']]['SEX']]
                invalidGenderRolesTable.add_row(row)

    return invalidGenderRolesTable

# List upcoming birthdays
def us38(GEDCOM_dict):
    upcomingBirthdays = PrettyTable()
    upcomingBirthdays.field_names = ['ID', 'Name', 'Birthday']

    individualData = GEDCOM_dict['individualData']
    today = datetime.datetime.now()
    for key, value in individualData.items():
        if ('DEAT' not in value or value['DEAT'] == 'N/A'):
            print("Death not here")
            if ('BIRT' in value and value['BIRT'] != 'N/A'):
                birthdate = datetime.datetime.strptime(
                    " ".join(value['BIRT'].split('-')), '%Y %m %d')
                birthdate = birthdate.replace(year=2022)
                print(birthdate)
                if(birthdate <= today + datetime.timedelta(30)) and birthdate >= today:
                    print("Found 30 days")
                    row = [key, value["NAME"], value["BIRT"]]
                    upcomingBirthdays.add_row(row)

    return upcomingBirthdays

# Not more than 15 siblings in a family
def us15(GEDCOM_dict):
    invalidFamilySize = PrettyTable()
    invalidFamilySize.field_names = ['FAM_ID', 'Number of Children']

    familyData = GEDCOM_dict['familyData']
    
    for key, value in familyData.items():
       if (value['CHIL'] and len(value['CHIL']) > 15):
           row = [key, len(value['CHIL'])]
           invalidFamilySize.add_row(row)

    return invalidFamilySize