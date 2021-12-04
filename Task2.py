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
        self.s1 = []  # Create stack 1
        self.s2 = []  # Create stack 2

    def enQueue(self, x):

        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into self.s1f
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    # Dequeue an item from the queue
    def deQueue(self):

        # if first stack is empty
        if len(self.s1) == 0:
            print("Queue is Empty")

        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x


class Queue_oneStack:
    def __init__(self):
        self.s = []

    # Enqueue an item to the queue
    def enQueue(self, data):
        self.s.append(data)

    # Dequeue an item from the queue
    def deQueue(self):
        # Return if queue is empty
        if len(self.s) <= 0:
            print('Queue is empty')
            return

        # pop an item from the stack
        x = self.s[len(self.s) - 1]
        self.s.pop()

        # if stack become empty
        # return the popped item
        if len(self.s) <= 0:
            return x

        # recursive call
        item = self.deQueue()

        # push popped item back to
        # the stack
        self.s.append(x)

        # return the result of
        # deQueue() call
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

        # Two inbuilt queues
        self.q1 = Queue()
        self.q2 = Queue()

        # To maintain current number
        # of elements
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1

        # Push x first in empty q2
        self.q2.put(x)

        # Push all the remaining
        # elements in q1 to q2.
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        # swap the names of two queues
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pull(self):

        # if no elements are there in q1
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

    # append operation
    def push(self, x):
        # get previous size of queue
        size = self.curr_size
        self.curr_size += 1
        # Add current element
        self.q.put(x)

        # Pop (or Dequeue) all previous
        # elements and put them after current
        # element
        for i in range(size):
            # this will add front element into
            # rear of queue
            x = self.q.get()
            self.q.put(x)

    # Removes the top element
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
print('here')
print(s)

# a normal queue
s = Queue()
s.put(10)
s.put(20)
s.put(90)
s.get()
print(s)
