#  Linked list @ charles madhuku


class CharlieLinkedNode:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class CharlieLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insertValue(self, value):
        if self.head == None:  # this is the first node
            self.head = CharlieLinkedNode(value)
        else:
            charlietemp = self.head
            self.head = CharlieLinkedNode(value)
            self.head.next = charlietemp

        self.size += 1

    def showValues(self):
        if self.head is None:
            print("Linked list is empty")
            return
        charlieHead = self.head
        charlies = ''
        while charlieHead:
            charlies += str(charlieHead.data) + ' = > '
            charlieHead = charlieHead.next
        print(charlies)

    def findAverage(self):
        charlieHead = self.head
        total = 0
        length = 1
        while charlieHead.next:
            total = charlieHead.data + total
            charlieHead = charlieHead.next
            length += 1
        print(total / length)

    def minMaxValue(self):
        charlieList = []
        charlieHead = self.head
        while charlieHead is not None:
            charlieList.append(charlieHead.data)
            charlieHead = charlieHead.next
        print(f'Minimun: {min(charlieList)}')
        print(f'Maximum: {max(charlieList)}')

    def showFirstValue(self):
        print(self.head.data)


charlieLink = CharlieLinkedList()

# d(i) push 0.04, 1.45, 16.879, 11.886, 6.7778, 10.456, 3.779, 12.00456
print('c(ii) Linked items')

charlieLink.insertValue(0.04)
charlieLink.insertValue(1.45)
charlieLink.insertValue(16.879)
charlieLink.insertValue(11.886)
charlieLink.insertValue(6.7778)
charlieLink.insertValue(10.456)
charlieLink.insertValue(3.779)
charlieLink.insertValue(12.00456)
charlieLink.showValues()

print('\n')
# c(iii) find the average
print('d(iii) average')
charlieLink.findAverage()

print('\n')
# d(iv) infintelty display 12.00456
print('d(iv) display 12.00456 infinity')

charlieLink.showFirstValue()

print('\n')


# d(v) find the maximum and minimum value
print('d(v) \n')

charlieLink.minMaxValue()
