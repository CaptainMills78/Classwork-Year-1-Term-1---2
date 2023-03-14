import random


def ran_quest():
    operation = random.randint(0, 3)
    return operation


def random_num():
    x = random.randint(1, 100)
    return x


def add(num1, num2):
    answer = num1 + num2
    return answer


def sub(num1, num2):
    answer = num1 - num2
    return answer


def mult(num1, num2):
    answer = num1 * num2
    return answer


def div(num1, num2):
    answer = num1 // num2
    return answer


def check(user, ans):
    if user == ans:
        return True
    else:
        return False


def get_answer(oper, q_num, number1, number2):
    if oper == 0:
        q_answer = add(number1, number2)
        print("Question " + str(q_num))
        print(str(number1) + " + " + str(number2))
    elif oper == 1:
        q_answer = sub(number1, number2)
        print("Question " + str(q_num))
        print(str(number1) + " - " + str(number2))
    elif oper == 2:
        q_answer = mult(number1, number2)
        print("Question " + str(q_num))
        print(str(number1) + " * " + str(number2))
    elif oper == 3:
        q_answer = div(number1, number2)
        print("Question " + str(q_num))
        print(str(number1) + " DIV " + str(number2))
    else:
        print("Invalid operation")
        q_answer = 0
    return q_answer


# Main code
score = 0
for i in range(0, 10):
    op = ran_quest()
    quest_num = i + 1
    numb1 = random_num()
    numb2 = random_num()
    question_ans = get_answer(op, quest_num, numb1, numb2)
    user_ans = int(input("Please enter your answer"))
    right = check(user_ans, question_ans)
    if right:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")

print("Your score is: " + str(score))
