import datetime
from datetime import date
from xml.dom.minidom import getDOMImplementation
from prettytable import PrettyTable
import os
import json

# Sprint 1

#marriage before divorce

GedcomFile = open(os.getcwd() + '/TESTCOM_dict.json', 'r')
Gedcom_dict = json.load(GedcomFile)

def us04(GEDCOM_dict):

    marriageBeforeDiv = PrettyTable()
    marriageBeforeDiv.field_names = ['FAM ID', 'Married', 'Divorced']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']

    div_id = []

    for key, value in familyData.items():
        if 'N/A' in value['DIV']:
            continue
        else:
            div_id.append([value['HUSB'],value['WIFE'],value['DIV']])

    for x in enumerate(div_id):
        print(x[1][0])
        print(div_id[x[0]+1:])
        try:
            if x[1][0] in div_id[x[0]+1:][0]:
                #should test if marrigae is before or after div
                print(".")
                if familyData[x[1][3]]['MARR'] > x[1][2]:
                    marriageBeforeDiv.add_row([key, familyData[x[1][3]]['MARR'], x[1][2]])
        except:
            #list index not out of range, continue
            pass
    
    return marriageBeforeDiv

us04(Gedcom_dict)

#Sprint 3

#list orphans

def us33(GEDCOM_dict):

    listOrphans = PrettyTable()
    listOrphans.field_names = ['FAM ID', 'Kid IDs']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']

    for key, value in familyData.items():
        fam_ids = []
        fam_ids.append([value['HUSB'],value['WIFE'],value['CHIL']])

        dead = 0
        for indKey, indValue in individualData.items():
            if indKey in fam_ids[0]:
                if indValue['DEAT'] != 'N/A':
                    dead +=1

            if dead == 2:
                kidsUnder18 = []
                for kids in fam_ids[0][2]:
                    age = date.today() - datetime.datetime.strptime(individualData[kids]['BIRT'], '%Y-%m-%d').date()
                    if age.days/365 < 18:
                        kidsUnder18.append(kids)
                        listOrphans.add_row([key,kidsUnder18])

    return listOrphans

#list recent survivors

def us37(GEDCOM_dict):

    recentSurvivors = PrettyTable()
    recentSurvivors.field_names = ['FAM ID', 'ID', 'Death Date', 'Survivors']

    familyData = GEDCOM_dict['familyData']
    individualData = GEDCOM_dict['individualData']

    for key, value in individualData.items():
        if value['DEAT'] != 'N/A':
            recent = date.today() - datetime.datetime.strptime(value['DEAT'], '%Y-%m-%d').date()
            
            if recent.days < 30:
                for famKey, famValue in familyData.items():
                    if key in famValue['HUSB']:
                        recentSurvivors.add_row([famKey, key, value['DEAT'], [famValue['WIFE'], famValue['CHIL']]])
                    elif key in famValue['WIFE']:
                        recentSurvivors.add_row([famKey, key, value['DEAT'], [famValue['HUSB'], famValue['CHIL']]])
                    else:
                        recentSurvivors.add_row([famKey, key, value['DEAT'], [famValue['HUSB'], famValue['WIFE'], famValue['CHIL'].pop(famValue['CHIL'].index(key))]])

    return recentSurvivors