#  Linked list @ charles madhuku

from collections import deque

stack = deque()

# add items into collection


def push(value):
    stack.appendleft(value)

# display items in the collection


def display():
    print(list(stack))

# find average


def average(mylist):
    return sum(mylist)/len(mylist)

# return first item


def peekitem():
    return list(stack)[0]

# find maximum value


def minimumValue():
    return min(stack)

# find minmum value


def maximumValue():
    return max(stack)


# c(i) push 0.04, 1.45, 16.879, 11.886, 6.7778, 10.456, 3.779, 12.00456
push(0.04)
push(1.45)
push(16.879)
push(11.886)
push(6.7778)
push(10.456)
push(3.779)
push(12.00456)


# c(ii) return or display all values in the stack
print('c(ii) stack items')
display()
print('\n')

# c(iii) find the average
print('c(iii) average')
print(average(stack))
print('\n')

# c(iv) infintelty display 12.00456
print(' c(iv) display 12.00456 infinity')
print(peekitem())
print('\n')

# c(v) find the maximum and minimum value
print('c(v) find the maximum and minimum value')
print('Minimum value')
print(minimumValue())
print('Maximum value')
print(maximumValue())
