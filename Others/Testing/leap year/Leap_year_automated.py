# this function has logical error,

# to read about Leap year go to   https://www.mathsisfun.com/leap-years.html

def IsLeap(year):

    Year = int(year)

    if Year <=0:

        return "Years cannot have zero or negative values"

    if (Year % 100 ==0 and Year % 400 == 0) or (Year % 4 ==0):

        return "this is a leap year"

    else:

        return "this is not a Leap Year"

if __name__ == "__main__":
          year_input = input("Year:")
          print(IsLeap(year_input))