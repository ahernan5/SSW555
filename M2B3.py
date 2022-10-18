from datetime import date
import datetime
from email.quoprimime import unquote
import os
import numpy as np

# Custom Functions
from functions import formatDate, toMonths

#NOTE: GitHub repository name: SSW555

todaysDate = date.today()

#opening the GEDCOM file for reading
GedcomFile = open(
    os.getcwd() + '/M1B6.ged', 'r')

#tags supported for our project
supportedTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM",
                 "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

lineNum = 1
famLineNum = 1
errorLineNum = 1

indiStorage = [['ID', 'Name', 'Gender', 'Birthday',
                'Age', 'Alive', 'Death', 'Child', 'Spouse']]
famStorage = [['ID', 'Married', 'Divorced', 'Husband ID',
               'Husband Name', 'Wife ID', 'Wife Name', 'Children']]
errors = [['Type', 'ID', 'Story #', 'Reason']]

birth = False
alive = True
marr = False
divorced = False
husb = ''
husbName = ''
wife = ''
wifeName = ''

uniqueIds = []
uniqueNamesAndBirthday = []
tempFam = []

for inputLine in GedcomFile:

    # Storage for some errors
    deathDate = ""
    birthday = ""

    #level is the first number in the input line
    level = int(inputLine[:1])

    #splits the string into a list and strips the tag from the list
    lineWords = inputLine.split()
    lineTag = lineWords[1].strip()

    #arguments are the following words after level and tag
    arguments = lineWords[2:]

    #checks if tags are valid making sure "1 DATE" and "2 NAME" are not supported
    if level == 1 and lineTag == "DATE":
        valid = "N"
    elif level == 2 and lineTag == "NAME":
        valid = "N"
    elif lineTag in supportedTags:
        valid = "Y"
    else:
        valid = "N"

    #prints input line
    print("-->", inputLine.rstrip("\n"))
    #prints level, tag, valid: Y or N, and arguments
    print("<--", level, "|", lineTag, "|",
          valid, "|", " ".join(arguments), "\n")

    #family storage
    if level == 0 and 'FAM' in arguments:
        famStorage.append([lineTag])
        famLineNum += 1

    if level == 1 and 'MARR' in lineTag:
        marr = True
        continue

    if marr == True:
        famStorage[famLineNum
                   - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
        marr = False

    if level == 1 and 'DIV' in lineTag:
        divorced = True
        continue

    if divorced == True:
        famStorage[famLineNum - 1].pop()
        famStorage[famLineNum - 1].pop()
        famStorage[famLineNum - 1][2] = (arguments[2]
                                         + "-"+toMonths(arguments[1])+"-"+arguments[0])

        divorced = False

    if len(famStorage[famLineNum - 1]) == 2:
        famStorage[famLineNum - 1].append('NA')

    if level == 1 and 'HUSB' in lineTag:
        husb = arguments[0]

    if len(famStorage[famLineNum - 1]) == 3:
        famStorage[famLineNum - 1].append(husb)

    #get husb name
    if len(famStorage[famLineNum - 1]) == 4:
        famStorage[famLineNum - 1].append('')

    if level == 1 and 'WIFE' in lineTag:
        wife = arguments[0]

    if len(famStorage[famLineNum - 1]) == 5:
        famStorage[famLineNum - 1].append(wife)

    #get wife name
    if len(famStorage[famLineNum - 1]) == 6:
        famStorage[famLineNum - 1].append('')

    #indiviual storage
    # User Story - US22
    if level == 0 and 'INDI' in arguments:
        if lineTag in uniqueIds:
            errors.append(["INDI", indiStorage[lineNum - 1][0], "US22", "ID is not unique"])
        uniqueIds.append(lineTag)
        indiStorage.append([lineTag])
        lineNum += 1

    if level == 1 and 'NAME' in lineTag:
        indiStorage[lineNum - 1].append(arguments[0]+" "+arguments[1])

    if level == 1 and 'SEX' in lineTag:
        indiStorage[lineNum - 1].append(arguments[0])

    if level == 1 and 'BIRT' in lineTag:
        birth = True
        continue

    if birth == True:
        indiStorage[lineNum
                    - 1].append(arguments[2]+"-"+toMonths(arguments[1])+"-"+arguments[0])
        indiStorage[lineNum - 1].append(todaysDate.year - int(arguments[2]))

        # User Story - US01
        numbersDate = arguments[2]+"-"+toMonths(arguments[1])+"-"+arguments[0]
        formattedBirthday = formatDate(numbersDate)
        if datetime.datetime.today() < formattedBirthday:
            errors.append(["INDI", indiStorage[lineNum - 1][0],
                          "US01", "Birthday occurs in the future"])

        # User Story - US23
        tempCheckBirthNameCombo = {indiStorage[lineNum - 1][1]: formattedBirthday}
        if(tempCheckBirthNameCombo in uniqueNamesAndBirthday):
            errors.append(["INDI", indiStorage[lineNum - 1][0],
                          "US23", "Name /  birthday combo is not unique"])
        uniqueNamesAndBirthday.append(tempCheckBirthNameCombo)

        birth = False

    if level == 1 and 'DEAT' in lineTag:
        alive = False
        continue

    if alive == False:
        indiStorage[lineNum - 1].pop()
        indiStorage[lineNum - 1].pop()
        indiStorage[lineNum - 1].append('FALSE')
        indiStorage[lineNum
                    - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
        deathDate = arguments[2]+"-"+toMonths(arguments[1])+"-"+arguments[0]

        # User Story - US03
        birthday = indiStorage[lineNum - 1][3]
        if formatDate(birthday) > formatDate(deathDate):
            errors.append(["INDI", indiStorage[lineNum - 1]
                          [0], "US03", "Death before birth"])

        # User Story - US07
        if (formatDate(deathDate) - formatDate(birthday)).days > 365 * 150:
             errors.append(["INDI", indiStorage[lineNum - 1]
                          [0], "US07", "Age of death is over 150"])

        alive = True

    # print(famStorage)
    if len(famStorage[famLineNum-1]) > 2 and 'Married' not in famStorage[famLineNum - 1][1]:

        divorced = famStorage[famLineNum - 1][2]

    # User Story - US06
    if divorced and 'NA' not in divorced:
        # print(divorced)
        if len(arguments) > 2:
            numbersDeathDate = arguments[2]+"-" + \
                toMonths(arguments[1])+"-"+arguments[0]
        numbersDivorceDate = divorced
        if formatDate(numbersDeathDate) > formatDate(numbersDivorceDate):
            errors.append(["FAMILY", indiStorage[lineNum - 1][0],
                          "US06", "Divorce date after death date"])

    if len(indiStorage[lineNum - 1]) == 5:
        indiStorage[lineNum - 1].append('TRUE')
        indiStorage[lineNum - 1].append('NA')

    #save family id, wife, husband and child ids
    if level == 0 and 'FAM' in arguments:
        tempFam.append([lineTag])
        continue

    if level == 1 and 'HUSB' in lineTag:
        tempFam[famLineNum - 2].append(arguments[0])

    if level == 1 and 'WIFE' in lineTag:
        tempFam[famLineNum - 2].append(arguments[0])

    if level == 1 and 'CHIL' in lineTag:
        tempFam[famLineNum - 2].append(arguments[0])


for x in indiStorage:
    for y in tempFam:
        if x[0] in y[2:]:
            if len(x) == 7:
                x.append(y[0])
            else:
                x[7] += ", " + y[0]
        if x[0] in y[1:3]:
            x.append(y[0])

    if len(x) == 7:
        x.append('NA')

    if len(x) == 8:
        x.append('NA')

for a in famStorage:
    for b in indiStorage:
        if len(a) > 4 and a[3] == b[0]:
            a[4] = b[1]
        if len(a) > 4 and a[5] == b[0]:
            a[6] = b[1]

# print(tempFam)

for c in famStorage:
    for d in tempFam:
        if len(d) > 3 and c[0] in d[0]:
            c.append(d[3:])

    if len(c) == 7:
        c.append('NA')

#User Story - This is lowkey US11
# divNames = []
# for e in famStorage:
#     if len(e) > 3 and 'Husband Name' not in e[4]:
#         divNames.append(e[4])
#         divNames.append([e[1], e[2]])
# ind = 1
# for name in divNames:
#     if name in divNames[ind:]:
#         divDate = divNames[ind][1]
#         reMarrDate = divNames[len(divNames) - divNames[::-1].index(name)][0]
#         reMarrDate = reMarrDate[:5] +toMonths(reMarrDate[5:8])+reMarrDate[8:]
#         if formatDate(divDate) > formatDate(reMarrDate):
#             errors.append(["FAMILY", name, "US04", "Marriage date before divorce date"])
#     ind+=1

#User Story - US04
for x in famStorage:
    if len(x) > 2 and x[2] != 'NA' and 'Married' not in x[1]:
        marDate = x[1][:5]+toMonths(x[1][5:8])+x[1][8:]
        if formatDate(marDate) > formatDate(x[2]):
            errors.append(
                ["FAMILY", x[0], "US04", "Marriage date after divorce date"])

#User Story - US02
for x in famStorage[1:]:
    if len(x) > 5:
        marDate = x[1][:5]+toMonths(x[1][5:8])+x[1][8:]
        husbID = x[3]
        wifeID = x[5]
    for y in indiStorage[1:]:
        if y[3] != 'NA':
            birthDate = y[3][:5]+y[3][5:8]+y[3][8:]
        if husbID == y[0]:
            if formatDate(birthDate) > formatDate(marDate):
                errors.append(
                    ["FAMILY", x[0], "US02", "Birth date after marriage date"])
        if wifeID == y[0]:
            if formatDate(birthDate) > formatDate(marDate):
                errors.append(
                    ["FAMILY", x[0], "US02", "Birth date after marriage date"])

#User Story - US05
for x in famStorage[1:]:
    if len(x) > 5:
        marDate = x[1][:5]+toMonths(x[1][5:8])+x[1][8:]
        husbID = x[3]
        wifeID = x[5]
    for y in indiStorage[1:]:
        if y[6] != 'NA':
            deathDate = y[6][:5]+toMonths(y[6][5:8])+y[6][8:]
        if husbID == y[0]:
            if y[5] == 'FALSE' and formatDate(marDate) > formatDate(deathDate):
                errors.append(["FAMILY", x[0], "US05", "Marriage date after death date"])
        if wifeID == y[0]:
            if y[5] == 'FALSE' and formatDate(marDate) > formatDate(deathDate):
                errors.append(["FAMILY", x[0], "US05", "Marriage date after death date"])

# User Story 35 (List Recent births within the last 30 days)


def us35(indiStorage):

    # Define Array to contain data
    us35table = ['ID', 'Story #', 'Birthday']
    for x in indiStorage[1:]:
        birthday = x[3]
        if (birthday):
            birthdate = datetime.datetime.strptime(
                    " ".join(birthday.split('-')), '%Y %m %d')
            today = datetime.datetime.now()

            if(birthdate >= today + datetime.timedelta(-30) and birthdate <= today):
                us35table.append(
                    [x[0], "US35: Recent Birth", x[3]])

        return us35table


# User Story 36 (List Recent deaths within the last 30 days)
def us36(indiStorage):

    # Define Array to contain data
    us36table = ['ID', 'Story #', 'Death Date']
    for x in indiStorage[1:]:
        deathDay = (x[6][:5]+toMonths(x[6][5:8])+x[6][8:])

        if (deathDay != 'NAN/A'):
            deathDate = datetime.datetime.strptime(
                    " ".join(deathDay.split('-')), '%Y %m %d')
            today = datetime.datetime.now()

            if(deathDate >= today + datetime.timedelta(-30) and deathDate <= today):
                us36table.append(
                    [x[0], "US36: Recent Death", x[6]])

    return us36table



# Temporarily format tables
print(np.array(indiStorage))
print(np.array(famStorage))
print(np.array(errors))


# Printing without formatting
# print(indiStorage)
# print('\n')
# print(famStorage)
