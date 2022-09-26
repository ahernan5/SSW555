from datetime import date
#NOTE: GitHub repository name: SSW555

todaysDate = date.today()

#opening the GEDCOM file for reading 
GedcomFile = open('C:/Users/user/Documents/SSW555Group/SSW555/M1B6.txt', 'r')

#tags supported for our project 
supportedTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

lineNum = 1
indiStorage = [['ID','Name','Gender','Birthday','Age','Alive','Death','Child','Spouse']]
birth = False
alive = True

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


    if level == 0 and 'INDI' in arguments:
        indiStorage.append([lineTag])
        lineNum += 1

    if level == 1 and 'NAME' in lineTag:
        indiStorage[lineNum - 1].append(arguments[0]+" "+arguments[1])

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
        indiStorage[lineNum - 1].append('FALSE')
        indiStorage[lineNum - 1].append(arguments[2]+"-"+arguments[1]+"-"+arguments[0])
        alive = True

    if len(indiStorage[lineNum - 1]) == 4:
        indiStorage[lineNum - 1].append('TRUE')
        indiStorage[lineNum - 1].append('NA')

    
    # print(lineNum)
    print(indiStorage)