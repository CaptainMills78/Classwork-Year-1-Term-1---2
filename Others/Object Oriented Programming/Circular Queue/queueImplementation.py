class Queue():
    def __init__(self, givenSize):
        self.__head = 0  # Initialise the pointers and list
        self.__tail = 0  # GivenSize parameter used to initialise the list
        self.__aList = []  # Use len(self.__alist) or len(object.get_list())
        # To recieve size later on
        while len(self.__aList) < givenSize:
            self.__aList.append("")

    def isEmpty(self):
        if self.__head == self.__tail:    # Condition for empty queue
            return True
        else:
            return False

    def isFull(self):
        if self.__tail + 1 == self.__head:     # Condition 1
            return True
        elif self.__head == 0 and self.__tail + 1 == len(self.__aList):  # Condition 2
            return True
        else:
            return False

    def enqueue(self, item):
        if not self.isFull():
            self.__aList[self.__tail] = item
            print(f"{item} has been added to the queue.")
            self.__tail += 1
            if self.__tail == len(self.__aList):
                self.__tail = 0
        else:
            print("Queue is full - consider dequeue before trying again")

    def dequeue(self):
        if not self.isEmpty():
            print(f"{self.__aList[self.__head]} has been dequeued")
            self.__head += 1
            if self.__head == len(self.__aList):
                self.__head = 0
        else:
            print("Queue is empty - consider queueing an item before trying again.")

    def get_list(self):
        return self.__aList

    def get_hp(self):
        return self.__head

    def get_tp(self):
        return self.__tail


if __name__ == "__main__":
    queue1 = Queue(5)
    queue1.dequeue()
    queue1.enqueue("This")
    queue1.enqueue("is")
    print(queue1.get_hp())
    print(queue1.get_tp())
    queue1.dequeue()
    print(queue1.get_hp())
    print(queue1.get_tp())
    queue1.enqueue("here")
    queue1.dequeue()
    queue1.enqueue("is")
    print(queue1.get_list())
    print(queue1.get_hp())
    print(queue1.get_tp())
    queue1.enqueue("a")
    queue1.enqueue("queue")
    print(queue1.get_list())
    print(queue1.get_hp())
    print(queue1.get_tp())
    queue1.enqueue("WOW")
    print(queue1.get_list())
