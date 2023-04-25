class stack():
    # Constructor
    def __init__(self, slength):
        self.__pointer = 0    # Sets initial pointer to position 0
        self.__sList = []     # Initialises the stack list itself
        while len(self.__sList)<slength:      # Will ensure the list is the size specified
            self.__sList.append("")

    def isFull(self):
        if self.__pointer == len(self.__sList):     # Determines whether the incoming push would overfill the stack
            print("Error - Stack is full.")     # Prints error message
            return True                         # Returns True - Stack is full
        else:
            return False             # Returns false - stack is not full, a push can occur

    def isEmpty(self):
        if self.__pointer == 0:    # Determines whether the stack is empty
            print("Error - Stack is empty.") # Prints error message
            return True   # Stack is empty
        else:
            return False    # Stack is not empty

    def push(self, item):     # Parameter item - data to push
        if not self.isFull():   # If isFull() is false - stack not full
            self.__sList[self.__pointer] = item   # Set pointer value to the new item
            self.__pointer += 1     # Increment the pointer
        else:    # isFull() is true, DO NOT PUSH
            return

    def pop(self):
        if not self.isEmpty():    # If isEmpty() is False
            self.__pointer -= 1     # Decrement pointer - focus on last item added
            print(self.__sList[self.__pointer])  # Print the value
        else:   # isEmpty() is True - DO NOT POP
            return

    def get_pointer(self):
        return self.__pointer

    def get_list(self):
        return self.__sList


if __name__ == "__main__":
    testStack = stack(3)     # Create stack object of length 3
    print(len(testStack.get_list()))    # Ensure stack is of correct length
    testStack.pop()     # Test isEmpty()
    testStack.push("hi")      # Test push()
    testStack.push("hi")
    testStack.push("hi")
    print(testStack.get_list())
    testStack.pop()  # Test pop
    testStack.pop()
    testStack.push("hi there")
    testStack.push("hi")
    print(testStack.get_list())    # Test push override
    testStack.pop()     # Empty stack - Test Push override
    testStack.pop()
    testStack.pop()

