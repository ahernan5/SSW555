from datetime import date
#NOTE: GitHub repository name: SSW555

todaysDate = date.today()

#opening the GEDCOM file for reading 
GedcomFile = open('C:/Users/user/Documents/SSW555Group/SSW555/M1B6.txt', 'r')

#tags supported for our project 
supportedTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

lineNum = 1
famLineNum = 1
indiStorage = [['ID','Name','Gender','Birthday','Age','Alive','Death','Child','Spouse']]
famStorage = [['ID','Married','Divorced','Husband ID','Husband Name','Wife ID','Wife Name','Children']]
birth = False
alive = True
marr = False
divorced = False
husb = ''
husbName = ''
wife = ''
wifeName = ''

tempFam = []

for inputLine in GedcomFile:
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
    print("<--", level, "|", lineTag, "|", valid, "|", " ".join(arguments), "\n")

    #family storage
    if level == 0 and 'FAM' in arguments:
        famStorage.append([lineTag])
        famLineNum += 1

    if level == 1 and 'MARR' in lineTag:
        marr = True
        continue

    if marr == True:
        famStorage[famLineNum - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
        marr = False
    
    if level == 1 and 'DIV' in lineTag:
        divorced = True
        continue
    
    if divorced == True:
        famStorage[famLineNum - 1].pop()
        famStorage[famLineNum - 1].pop()
        famStorage[famLineNum - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
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
    if level == 0 and 'INDI' in arguments:
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
        indiStorage[lineNum - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
        indiStorage[lineNum - 1].append(todaysDate.year - int(arguments[2]))
        birth = False

    if level == 1 and 'DEAT' in lineTag:
        alive = False
        continue

    if alive == False:
        indiStorage[lineNum - 1].pop()
        indiStorage[lineNum - 1].pop()
        indiStorage[lineNum - 1].append('FALSE')
        indiStorage[lineNum - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
        alive = True

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
        

    # print(lineNum)
    # print(famLineNum)
print(indiStorage)
print('\n')
print(famStorage)
# print('\n')
# print(tempFam)