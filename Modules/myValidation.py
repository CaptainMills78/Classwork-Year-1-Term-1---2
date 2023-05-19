######################################################################################
# Adam Atkins:                                                                       #
# Data validation functions                                                          #
# Current validation modules:                                                        #
# Length, value range, email formatting, String type, Integer type, valid date (WIP) #
# Date Started: 28th April 2023                                                      #
# Date Last Updated: 4th May 2023                                                    #
######################################################################################


def isValidLength(text, length, s=0):  # s is a switch for the modes

    # Ensures the length of a given string matches the desired length, or is greater than or less than the desired length

    if not isValidString(text):
        return -2  # Checks to ensure the given text is of the string data type - if not, returns value to signify invalid text

    match s:
        case 0:  # s = 0, check whether length is equal
            if len(text) == length:
                return True
            else:
                return False
        case 1:  # s = 1, check whether length is greater than or equal to
            if len(text) >= length:
                return True
            else:
                return False
        case 2:  # s = 2, check whether length is less than or equal to
            if len(text) <= length:
                return True
            else:
                return False
        case _:  # Returns a value to signify an invalid switch value
            return -1


def isValidRange(data, minimum=0, maximum=100, s=0):

    # Ensures the given data is within a given range - defined by given maximum, minimum, and mode value

    if not isValidInterger(
            data):  # Checks to ensure Variables data, minimum, and maximum are of the integer data type - returns corresponding error values
        return -2
    if not isValidInterger(str(minimum)):
        return -3
    if not isValidInterger(str(maximum)):
        return -4
    data = int(data)
    minimum = int(minimum)
    maximum = int(maximum)
    match s:
        case 0:  # s = 0, Include ranges
            if minimum <= data <= maximum:
                return True
            else:
                return False
        case 1:  # s = 1, Exclude ranges
            if minimum < data < maximum:
                return True
            else:
                return False
        case 2:  # s = 2, check against minimum only, excluding ranges
            if minimum < data:
                return True
            else:
                return False
        case 3:  # s = 3, check against minimum only, including
            if minimum <= data:
                return True
            else:
                return False
        case 4:  # s = 4, check against maximum only, excluding
            if maximum > data:
                return True
            else:
                return False
        case 5:  # s =5, check against maximum only, including
            if maximum >= data:
                return True
            else:
                return False
        case _:  # Returns a different value to signify an invalid mode
            return -1


def isValidEmail(address):

    # Ensures given data follows the format of a valid email address

    import re

    potential_characters = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"     # Lists the format of an email
    if re.fullmatch(potential_characters, address):        # Checks that the given string follows the format provided
        return True                                        # Returns True or False dependant
    else:
        return False


def isValidString(data):

    # Checks whether given data is of the string data type

    if isinstance(data, str):
        return True
    else:
        return False


def isValidInterger(data):

    # Checks whether given data is of the integer data type

    if data.isdigit():
        return True
    else:
        return False

def isLeapYear(year):

    # Check for a year to be a leap year

    year = int(year)

    if year % 4 != 0:      # Year not divisible by 4?
        return False
    elif year % 100 == 0 and year % 400 != 0:    # Year divisible by 100, but not 400?
        return False
    elif year % 400 == 0:    # Year divisible by 400?
        return True
    else:
        return True


def isValidDate(date):

    # Checks whether the given data is of the string data type, and then proceeds to check to a given format.

    if not isValidString(date):
        return -1

    split_date = date.split("/")      # Split date into 3 seperate parts (should be dd, mm, yyyy)
    if len(split_date) != 3:          # Are there three parts?
        return False
    if not isValidLength(split_date[0], 2, 0):     # Different values correct length (dd - 2, mm - 2, yyyy - 4)
        return False
    if not isValidLength(split_date[1], 2, 0):
        return False
    if not isValidLength(split_date[2], 4, 0):
        return False

    if not isValidRange(split_date[1], 1, 12, 0):
        return False

    if split_date[1] == "02":      # Check februrary days?
        if isValidRange(split_date[0], 1, 28, 0):
            return True
        if isValidRange(split_date[0], 1, 29, 0) and isLeapYear(split_date[2]):
            return True
        return False
    else:
        thirty_days = ["04", "06", "09", "11"]
        thirty_one_days = ["01", "03", "05", "07", "08", "10", "12"]
        match split_date[1]:
            case x if x in thirty_days:                  #   FIX NEEDED HERE
                if isValidRange(split_date[0], 1, 30, 0):
                    return True
                else:
                    return False
            case x if x in thirty_one_days:
                if isValidRange(split_date[0], 1, 31, 0):
                    return True
                else:
                    return False
            case _:
                return False


def isValidPostCode(postcode):

    # Check to ensure a postcode exists

    import requests
    import json

    response = requests.get("https://api.postcodes.io/postcodes/" + postcode)
    result = response.json()
    status = result.get("status")     # Getting status code

    if status == 200:     # Successful
        return True
    else:
        return False


if __name__ == "__main__":
    print(isValidEmail("a_a06@hotmail.com"))    # Should be true
    print(isValidEmail("12335@hotmail.com"))    # Should be True
    print(isValidEmail("a_a06@h06.com"))        # Should be True
    print(isValidEmail("a_a06hotmail.com"))     # Should be false
    print(isValidDate("03/05/2006"))            # Should be true
    print(isValidDate("01/12/2006"))            # Should be true
    print(isValidDate("00/05/2006"))  # Should be false
    print(isValidDate("03/05/206"))  # Should be False
    print(isValidDate("29/02/2005"))  # Should be False
    print(isValidDate("29/02/2008"))  # Should be true
    print(isValidDate("31/09/2006"))  # Should be False
    print(isValidDate("31/10/2006"))  # Should be true
    print(isValidDate("30/09/2006"))  # Should be true
    print(isValidPostCode("ST10 1HE"))
    print(isValidPostCode("gft 56d"))
