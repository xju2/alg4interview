#!/usr/bin/env python
class Stack:
    def __init__(self):
        print "Stack is created"
        self.currentMin = 9999999
        self.minArray = [] 
        self.array = []

    def push(self, value):
        if(len(self.array) < 1) or self.currentMin >= value:
            self.minArray.append(self.currentMin)
            self.currentMin = value

        self.array.append(value)

    def pop(self):
        outitem = self.array.pop()
        print str(outitem)+" is popped"

        if outitem == self.currentMin:
            self.currentMin = self.minArray.pop()

        return outitem

    def min_item(self):
        return self.currentMin


stack = Stack()
stack.push(2)
stack.push(6)
stack.push(4)
stack.push(1)
stack.push(5)
print stack.min_item()
stack.pop()
print stack.min_item()
stack.pop()
print stack.min_item()
stack.pop()
print stack.min_item()
stack.pop()
