def AverageCal():
    run = True
    TotalMark = int(input("  Enter total marks of the group  "))
    while run:
        No_of_Students = int(input(" Enter the total number of students  "))
        try:
            Average = TotalMark / int(No_of_Students)
            run = False
        except ZeroDivisionError:
            print("Number of students must be a non-zero integer.")
    return Average


print("The average mark is  " + str(AverageCal()))
