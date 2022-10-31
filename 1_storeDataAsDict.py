#  Stores Data from a Sanitized GEDCOM File in a Dict for Later Use
#  Creates new Txt File ( {filename}_dict.json ) with the stored dictionary data for the Sanitized GEDCOM File
#  Returns the Sanitzed GEDCOM Data Dictionary

import sys
import json
from collections import defaultdict

from userstories import msUserStories


def storeDataAsDict(validLinesList):
    uniqueTags = ['INDI', 'FAM']
    datedTags = ['BIRT', 'DEAT', 'DIV', 'MARR']
    dynamicTags = ['FAMS', 'CHIL']

    prevTopLevelTag = ""
    prevTopLevelId = ""
    individualData = {}
    familyData = {}
    prevTagPendingDate = ""
    tagsExcludedFromData = ['HEAD', 'NOTE', 'TRLR']

    for line in validLinesList:
        validLineSplit = line.split(" | ")
        tag = validLineSplit[1]
        valid = validLineSplit[2]
        arguments = validLineSplit[3]
        lineNumber = validLineSplit[4]

        if (tag in uniqueTags):
            if (tag == "INDI"):
                # Using defaultdict prevents ValueErrors
                individualData[arguments] = defaultdict(lambda: 'N/A')
                individualData[arguments]["INDILine"] = lineNumber
            if (tag == "FAM"):
                familyData[arguments] = defaultdict(lambda: 'N/A')
                familyData[arguments]["FAMLine"] = lineNumber

            prevTopLevelTag = tag
            prevTopLevelId = arguments
        elif(tag in tagsExcludedFromData):
            continue
        else:
            if (prevTopLevelTag == "INDI"):
                if (tag not in datedTags):
                    if (tag in dynamicTags):
                        individualData[prevTopLevelId].update({tag: []})
                        individualData[prevTopLevelId][tag].append(arguments)
                        individualData[prevTopLevelId].update(
                            {tag + "Line": lineNumber})
                    elif (tag == "DATE"):
                        fillDate = msUserStories.us41(
                            arguments)
                        checkValidDate = msUserStories.us42(
                            fillDate)
                        individualData[prevTopLevelId][prevTagPendingDate] = checkValidDate
                        individualData[prevTopLevelId][prevTagPendingDate
                                                       + "Line"] = lineNumber
                    else:
                        individualData[prevTopLevelId].update({tag: arguments})
                        individualData[prevTopLevelId].update(
                            {tag + "Line": lineNumber})
                else:
                    prevTagPendingDate = tag
                    individualData[prevTopLevelId].update({tag: ""})
                    individualData[prevTopLevelId].update(
                        {tag + "Line": lineNumber})

            if (prevTopLevelTag == "FAM"):
                if (tag not in datedTags):
                    if (tag in dynamicTags):
                        if (tag not in familyData[prevTopLevelId].keys()):
                            familyData[prevTopLevelId].update({tag: []})
                        familyData[prevTopLevelId][tag].append(arguments)
                        familyData[prevTopLevelId][tag + "Line"] = lineNumber
                    elif (tag == "DATE"):
                        fillDate = msUserStories.us41(
                            arguments)
                        checkValidDate = msUserStories.us42(
                            fillDate)
                        familyData[prevTopLevelId][prevTagPendingDate] = checkValidDate
                        familyData[prevTopLevelId][prevTagPendingDate
                                                   + "Line"] = lineNumber
                    else:
                        familyData[prevTopLevelId].update({tag: arguments})
                        familyData[prevTopLevelId].update(
                            {tag + "Line": lineNumber})
                else:
                    prevTagPendingDate = tag
                    familyData[prevTopLevelId].update({tag: ""})
                    familyData[prevTopLevelId].update(
                        {tag + "Line": lineNumber})

    return {'individualData': individualData, 'familyData': familyData}


def main(fileName, validLinesList):

    # Case when the Program is Run Directly from Command Line and on with Valid Input File (cleaned GEDCOM File from 1_cleanedGEDCOM.py)
    if (fileName.endswith('_cleaned.ged')):
        cleanedGEDCOM = open(fileName, 'r')
        for line in cleanedGEDCOM:
            validLinesList.append(line)

        GEDCOM_dict = storeDataAsDict(validLinesList)

        with open(fileName.rstrip('_cleaned.ged') + '_dict.json', 'w+', encoding='utf-8') as outfile:
            json.dump(GEDCOM_dict, outfile, ensure_ascii=False, indent=2)

        return GEDCOM_dict
    # Case when the Program is run from 0_main.py
    else:
        if (len(validLinesList) != 0):
            GEDCOM_dict = storeDataAsDict(validLinesList)

            with open(fileName[:-4] + '_dict.json', 'w+', encoding='utf-8') as outfile:
                json.dump(GEDCOM_dict, outfile, ensure_ascii=False, indent=2)

            return GEDCOM_dict
        else:
            raise 'Empty Input, no cleaned GEDCOM Data to Store in Dict'

    return


if __name__ == '__main__':
    main(sys.argv[1], [])
