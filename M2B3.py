#Alyssa Hernandez
#I pledge my honor that I have abided by the Stevens Honor System. -AH 


#opening the GEDCOM file for reading 
GedcomFile = open('M1B6.txt', 'r')

#tags supported for our project 
supportedTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]

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
    