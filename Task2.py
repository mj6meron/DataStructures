"""
Routine to implement a queue and a stack.

a. Implementation of a queue using two stacks.
b. Implementation of a queue using only one stacks.
c. Implementation of a stack using two queues.
d. Implementation of a stack using a single queue.
"""
from queue import Queue


class Queue_twoStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):

        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):

        if len(self.s1) == 0:
            print("Queue is Empty")

        x = self.s1[-1]
        self.s1.pop()
        return x


class Queue_oneStack:
    def __init__(self):
        self.s = []

    def enQueue(self, data):
        self.s.append(data)

    def deQueue(self):
        if len(self.s) <= 0:
            print('Queue is empty')
            return

        x = self.s[len(self.s) - 1]
        self.s.pop()

        if len(self.s) <= 0:
            return x

        item = self.deQueue()

        self.s.append(x)

        return item


# q = Queue_twoStack()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())

class stack_twoQueues:

    def __init__(self):

        self.q1 = Queue()
        self.q2 = Queue()

        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1

        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pull(self):

        if self.q1.empty():
            return
        self.q1.get()
        self.curr_size -= 1

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

    def size(self):
        return self.curr_size

    def __repr__(self):
        elements = []
        for i in self.q1.queue:
            elements.append(i)
        return str(elements)


# ------------------------------------------------------------------------------------


# Python3 program to implement stack using a
# single queue

class stack_oneQueue:
    def __init__(self):
        self.q = Queue()
        self.curr_size = 0

    def push(self, x):
        size = self.curr_size
        self.curr_size += 1
        self.q.put(x)

        for i in range(size):
            x = self.q.get()
            self.q.put(x)

    def pull(self):
        if self.curr_size == 0:
            print("No elements")
            return -1

        x = self.q.get()
        self.curr_size -= 1
        return x

    def __repr__(self):
        elements = []
        for i in self.q.queue:
            elements.append(i)
        return str(elements)


# ------------------------------------------------------------------------------------
s = stack_oneQueue()
s.push(10)
s.push(20)
s.push(90)
s.pull()
print(s)

s = stack_twoQueues()
s.push(10)
s.push(20)
s.push(90)
s.pull()
print(s)

# a normal queue
s = Queue()
s.put(10)
s.put(20)
s.put(90)
s.get()
print(s)
