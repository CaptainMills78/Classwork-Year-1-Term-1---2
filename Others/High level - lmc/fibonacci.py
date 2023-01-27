def fibonnacci_it():
    first_term = 0
    second_term = 1
    n = int(input("Please enter the number you want to go up to..."))
    print(first_term)
    print(second_term)
    for x in range(0, n-2):
        third_term = first_term + second_term
        print(third_term)
        first_term = second_term
        second_term = third_term


def fibonnacci_re():
    pass
