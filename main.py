import fileinput
import csv
import os
import datetime

tagNames = []

GedcomFile = open(os.getcwd() + '/M1B6.txt', 'r')
  
supportedTags = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM",
                 "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
  
    

class Person:
    def __init__(self, id, level):
        self.id = id
        self.level = level 
        self.name = None 
        self.sex = None
        self.birth = None
        self.age = None 
        self.isAlive = True
        self.death = None
        self.children = []
        self.spouse = None
        
class Family:
    def __init__(self, id):
        self.id = id
        self.husband = None
        self.wife = None 
        self.children = []
        self.marriage = None
        self.divorce = None 
        
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
        
        
#birth before death
def birthBeforeDeath(self, level, tag):
    if lineWords[0] == "2" and lineWords[1] == "DATE":
        if isInstance(self, Person):
            if tag == "BIRT":
                self.birth = datetime.strptime(lineWords[2].rstrip(), '%d %b %Y').date()
            elif tag == "DEAT":
                self.death = datetime.strptime(lineWords[2].rstrip(), '%d %b %Y').date()
        elif isInstance(self, Family):
            if tag == "MARR":
                self.marriage = datetime.strptime(lineWords[2].rstrip(), '%d %b %Y').date()
            elif tag == "DIV":
                self.divorce = datetime.strptime(lineWords[2].rstrip(), '%d %b %Y').date()