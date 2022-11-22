# Initial Linked List:

names = [["Abid", 3],
         ["Jason", 2],
         ["Mazen", -1],
         ["James", 1]]
Head = 0  # Starts the linked list at row 0 (Abid)
# Value is ALWAYS names[x][0]
# Pointer is ALWAYS names[x][1]

# Adding a value:

names.append(["Adam", 2])
names[1][1] = 4


# Deleting a value:
names[2][1] = -1
names[4][1] = 3