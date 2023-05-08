from stackOOP import *


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