head = 0
linkedList = [["London", 1],["Oxford", 2],["Birmingham", 3],["Manchester", None]]


linkedList.append(["Stoke-On-Trent", None])
linkedList[3][1] = 4

linkedList[2][1] = None
linkedList[1][1] = 3
print(linkedList)
finish = False
count = 0
while not finish:
    if linkedList[count][1] == None:
        finish = True
    else:
        print(linkedList[count][0])
        count = linkedList[count][1]
print(linkedList[count][0])