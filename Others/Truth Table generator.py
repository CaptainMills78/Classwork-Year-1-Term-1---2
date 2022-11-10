# Existing things
# Truth Table Generator - www.101computing.net/truth-table-generator/
def inputs2(exp1):
    print("  -------------")
    print("  | A | B | X |")
    print("  -------------")

    for a in range(0, 2):
        for b in range(0, 2):
            x = eval(exp1)
            print("  | " + str(a) + " | " + str(b) + " | " + str(x) + " |")
            print("  -------------")


def inputs3(exp2):
    print("  -----------------")
    print("  | A | B | C | X |")
    print("  -----------------")

    for a in range(0, 2):
        for b in range(0, 2):
            for c in range(0, 2):
                x = eval(exp2)
                print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |")
                print("  -----------------")


def inputs4(exp3):
    print("  ---------------------")
    print("  | A | B | C | D | X |")
    print("  ---------------------")

    for a in range(0, 2):
        for b in range(0, 2):
            for c in range(0, 2):
                for d in range(0, 2):
                    x = eval(exp3)
                    print(
                        "  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d) + " | " + str(x) + " |")
                    print("  ---------------------")


def truthTable(expression, inputs=2):
    print("Boolean Expression:")
    print("  X = " + expression.upper())
    expression = expression.lower()

    # replace Boolean Operators with bitwise operators
    expression = expression.replace("and", "&")
    expression = expression.replace("xor", "^")
    expression = expression.replace("or", "|")
    expression = expression.replace("not", "~")

    print("\nTruth Table:")
    if inputs == 2:
        inputs2(expression)

    elif inputs == 3:
        inputs3(expression)

    elif inputs == 4:
        inputs4(expression)


##############################################

expression = "A AND NOT (B XOR C)"
truthTable(expression, 3)
