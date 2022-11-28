import datetime
from prettytable import PrettyTable


# __________________Sprint 1__________________

# Birth should occur before marriage of an individual
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


# Birth should occur before death of an individual
def us03(GEDCOM_dict):

    deathBeforeBirthTable = PrettyTable()
    deathBeforeBirthTable.field_names = ['ID', 'Name', 'Birthday', 'Death']

    for key, value in GEDCOM_dict['individualData'].items():
        if (value['BIRT'] and value['BIRT'] != 'N/A'):
            birthdate = datetime.datetime.strptime(
                " ".join(value['BIRT'].split('-')), '%Y %m %d')
        if (value['DEAT'] and value['DEAT'] != 'N/A'):
            deathdate = datetime.datetime.strptime(
                " ".join(value['DEAT'].split('-')), '%Y %m %d')
            if(deathdate <= birthdate):
                row = [key, value['NAME'], value['BIRT'], value['DEAT']]
                deathBeforeBirthTable.add_row(row)

    return deathBeforeBirthTable


# __________________Sprint 2__________________

# No more than one individual with the same name and birth date should appear in a GEDCOM file
def us23(GEDCOM_dict):
    
        uniqueNameBirthTable = PrettyTable()
        uniqueNameBirthTable.field_names = ['ID', 'Name', 'Birthday']
    
        individualData = GEDCOM_dict['individualData']
    
        for key, value in individualData.items():
            for key2, value2 in individualData.items():
                if (key != key2 and value['NAME'] == value2['NAME'] and value['BIRT'] == value2['BIRT']):
                    row = [key, value['NAME'], value['BIRT']]
                    uniqueNameBirthTable.add_row(row)
    
        return uniqueNameBirthTable

# List all deceased individuals in a GEDCOM file
def us29(GEDCOM_dict):
    
    deceasedTable = PrettyTable()
    deceasedTable.field_names = ['ID', 'Name', 'Birthday', 'Death']
    
    for key, value in GEDCOM_dict['individualData'].items():
        if (value['DEAT'] != 'N/A'):
            row = [key, value['NAME'], value['BIRT'], value['DEAT']]
            deceasedTable.add_row(row)
    
    return deceasedTable


# __________________Sprint 3__________________

# List all living people over 30 who have never been married in a GEDCOM file 
def us31(GEDCOM_dict):
        
    livingSingleTable = PrettyTable()
    livingSingleTable.field_names = ['ID', 'Name', 'Age']
        
    for key, value in GEDCOM_dict['individualData'].items():
        if (value['DEAT'] == 'N/A'):
            if (value['BIRT'] != 'N/A'):
                birthdate = datetime.datetime.strptime(
                    " ".join(value['BIRT'].split('-')), '%Y %m %d')
                today = datetime.datetime.today()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                if (age >= 30 and value['FAMS'] == 'N/A'):
                    row = [key, value['NAME'], age]
                    livingSingleTable.add_row(row)
        
    return livingSingleTable


# List all multiple births in a GEDCOM file
def us32(GEDCOM_dict):
        
    multipleBirthsTable = PrettyTable()
    multipleBirthsTable.field_names = ['ID', 'Name', 'Birthday', 'Family ID', 'Wife Name']
        
    for key, value in GEDCOM_dict['individualData'].items():
        if (value['BIRT'] != 'N/A'):
            for key2, value2 in GEDCOM_dict['individualData'].items():
                if (key != key2 and value['BIRT'] == value2['BIRT'] and value['FAMC'] == value2['FAMC']):
                    row = [key, value['NAME'], value['BIRT'], value['FAMC'], GEDCOM_dict['familyData'][value['FAMC']]['WIFE_NAME']]
                    multipleBirthsTable.add_row(row)
        
    return multipleBirthsTable


# __________________Sprint 4__________________
        
# No more than five siblings should be born at the same time
def us14(GEDCOM_dict):
            
    multipleSiblingBirthsTable = PrettyTable()
    multipleSiblingBirthsTable.field_names = ['ID', 'Name', 'Birthday', 'Family ID', 'Wife Name']
            
    for key, value in GEDCOM_dict['individualData'].items():
        if (value['BIRT'] != 'N/A'):
            for key2, value2 in GEDCOM_dict['individualData'].items():
                if (key != key2 and value['BIRT'] == value2['BIRT'] and value['FAMC'] == value2['FAMC']):
                    row = [key, value['NAME'], value['BIRT'], value['FAMC'], GEDCOM_dict['familyData'][value['FAMC']]['WIFE_NAME']] 
                    if (len(GEDCOM_dict['familyData'][value['FAMC']]['CHIL']) > 5):
                        multipleSiblingBirthsTable.add_row(row)                         
                            
    return multipleSiblingBirthsTable
            

# No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
def us24(GEDCOM_dict):
            
        uniqueFamilyTable = PrettyTable()
        uniqueFamilyTable.field_names = ['ID', 'Husband Name', 'Wife Name', 'Marriage Date']
            
        for key, value in GEDCOM_dict['familyData'].items():
            for key2, value2 in GEDCOM_dict['familyData'].items():
                if (key != key2 and value['HUSB_NAME'] == value2['HUSB_NAME'] and value['WIFE_NAME'] == value2['WIFE_NAME'] and value['MARR'] == value2['MARR']):
                    row = [key, value['HUSB_NAME'], value['WIFE_NAME'], value['MARR']]
                    uniqueFamilyTable.add_row(row)
            
        return uniqueFamilyTable

                
       