def fibonnacci_it(n):
    first_term = 0
    second_term = 1
    print(first_term)
    print(second_term)
    for x in range(0, n-2):
        third_term = first_term + second_term
        print(third_term)
        first_term = second_term
        second_term = third_term


def fibonnacci_re(num, count=0, sequ="", f_term=0, s_term=1,):
    while count < num:
        if f_term == 0:
            sequ += str(f_term) + str(s_term)
        else:
            sequ += str(s_term)
        t_term = f_term + s_term
        f_term = s_term
        s_term = t_term
        count += 1
        sequ = fibonnacci_re(num, count, sequ, f_term, s_term)
    return sequ
    pass


number = int(input("Please enter the number you want to go up to..."))
print(fibonnacci_re(number))
