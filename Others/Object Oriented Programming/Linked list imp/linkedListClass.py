class node():
    def __init__(self, value):
        self.next = None
        self.value = value
    
    def __str__(self):
        return str(self.value)
    


class linkedList():
    def __init__(self, head):
        self.head = head

    def printList(self):
        x = self.head
        print("List:")
        while x.next != None:
            print(x.value)
            x = x.next
        print(x.value)

    def addNode(self, node1, location, s=0):    # Switch modes - 0, 1, 2
        match s:
            case 0:   # Add at start
                node1.next = self.head
                self.head = node1
            case 1:   # Add at end
                x = self.head
                while x.next != None:
                    x = x.next
                x.next = node1
                node1.next = None
            case 2: # Insert
                x = self.head
                count = 0
                while count != location:
                    x = x.next
                    count += 1
                temp = x.next
                x.next = node1
                node1.next = temp


if __name__ == "__main__":
    def main():
        node1 = node("Apple")
        node2 = node("Orange")
        node3 = node("Pear")
        node4 = node("Potato")
        node1.next = node2
        node2.next = node3
        linList = linkedList(node1)
        linList.addNode(node4, 2, 2)
        linList.printList()
        
    main()
