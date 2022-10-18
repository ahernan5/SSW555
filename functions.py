import datetime


def toMonths(str):
    if str == "JAN":
        return "01"
    elif str == "FEB":
        return "02"
    elif str == "MAR":
        return "03"
    elif str == "APR":
        return "04"
    elif str == "MAY":
        return "05"
    elif str == "JUN":
        return "06"
    elif str == "JUL":
        return "07"
    elif str == "AUG":
        return "08"
    elif str == "SEP":
        return "09"
    elif str == "OCT":
        return "10"
    elif str == "NOV":
        return "11"
    elif str == "DEC":
        return "12"
    else:
        return "N/A"

def formatDate(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d')