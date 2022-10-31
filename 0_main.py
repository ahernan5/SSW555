import sys

cleanGEDCOM = __import__('1_cleanGEDCOM')
storeDataAsDict = __import__('1_storeDataAsDict')
displayIndividualData = __import__('2_displayIndividualData')
displayFamilyData = __import__('2_displayFamilyData')
displaySpecialCases = __import__('3_displaySpecialCases')
displayErrors = __import__('3_displayErrors')


def main(fileName):

    validLinesList = cleanGEDCOM.main(fileName)

    GEDCOM_dict = storeDataAsDict.main(fileName, validLinesList)

    print('Individuals')
    # Changes GEDCOM Dict for indiData to Match What is Printed
    print(displayIndividualData.main(fileName, GEDCOM_dict))
    print('Families')
    # Changes GEDCOM Dict for famData to Match What is Printed
    print(displayFamilyData.main(fileName, GEDCOM_dict))

    displaySpecialCases.main(fileName, GEDCOM_dict)
    displayErrors.main(fileName, GEDCOM_dict)

    return


if __name__ == '__main__':
    main(sys.argv[1])
