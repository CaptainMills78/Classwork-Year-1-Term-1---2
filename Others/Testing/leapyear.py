# this function has logical error,

# to read about Leap year go to   https://www.mathsisfun.com/leap-years.html


def IsLeap(Year):
    # Year is an integer

    Year = int(Year)

    if Year <= 0:  # Made this condition part of the overall if statement
        print("Years cannot have zero or negative values")

    elif Year % 4 == 0 and Year % 100 == 0 and Year % 400 != 0:  # Added to make sure some years are detected as not a leap year

        print("this is not a leap year")

    elif (Year % 100 == 0 and Year % 400 == 0) or (Year % 4 == 0):

        print("this is a leap year")

    else:

        print("this is not a Leap Year")


TestYear = input("Enter Year and I will check it if it is leap or not... ")

IsLeap(TestYear)
