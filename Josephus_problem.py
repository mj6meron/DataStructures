"""
Josephus problem
"""

import collections


# --------------------------------------- LinkedList without Iterator -------------------------------------------


class Node:
    data = None
    next_node = None

    def __init__(self, data):
        """Create an instance node"""
        self.data = data

    def __repr__(self):
        """Represent a node"""
        return '[%s]' % self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        """Check if empty"""
        return self.head is None

    def size(self):
        """Return the size of the linked list"""
        return self.length

    def add(self, data):
        """Add note in front of the header, simple implementation"""
        self.length += 1
        new_node = Node(data)
        if self.length != 1:
            self.tail.next_node = new_node
            new_node.next_node = None
            self.tail = new_node
        else:
            new_node.next_node = self.head  # reference the next node to the current head
            self.head = new_node  # Add at the first of the linked list
            self.tail = new_node

    def __repr__(self):
        """Do the representation fo the Linked List"""
        elements = []
        i = self.head
        while i:
            if i is self.head:
                elements.append('☺ [%s]' % i.data)
            elif i.next_node is None:
                elements.append('[%s] ✌ ' % i.data)
            else:
                elements.append('[%s]' % i.data)
            i = i.next_node
        return '➤'.join(elements)

    def get(self, node_index):
        """Get a node from LinkedList at index"""
        if node_index == 0:  # if index 0 return first element
            return self.head
        if node_index >= self.size() or node_index < 0:  # out of range
            return 'Index out of range'
        position = 0
        i = self.head
        while position < node_index:
            i = i.next_node
            position += 1
        return i.data  # found and return the element

    def remove(self, node_index):
        """Remove node from LinkedList using index"""
        self.length -= 1
        if node_index == 0:  # if index 0 return first element
            old_head = self.head
            self.head = old_head.next_node
            return "Removed : %s" % old_head
        if node_index >= self.size() or node_index < 0:  # out of range
            return 'Index out of range'
        position = 0
        previous_node = self.head
        while position < node_index - 1:
            previous_node = previous_node.next_node
            position += 1
        tobe_removed = previous_node.next_node  # get the to be removed node
        the_next_node = tobe_removed.next_node  # get the its next node
        previous_node.next_node = the_next_node  # point next node, technically removing the middle element
        return "Removed : %s" % tobe_removed


# --------------------------------------------------------------------------------------------------------------


n = 5
m = 2

numbers = []
myLinkedList = LinkedList()
linked_lst = collections.deque()
for e in range(1, n + 1):
    myLinkedList.add(e)
    numbers.append(e)
    linked_lst.append(e)


def josephus(ls, skip, data_structure):

    if data_structure == "arrayList":
        skip -= 1  # pop automatically skips the dead guy
        idx = skip
        while len(ls) > 1:
            print(ls.pop(idx))  # kill prisoner at idx
            idx = (idx + skip) % len(ls)
        print('survivor: ', ls[0])
    if data_structure == "arrayList":
        pass


josephus(numbers, m, 'hey')


def josephus(people, skips):
    if people == 1:
        return 1
    else:

        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (josephus(people - 1, skips) + skips - 1) % people + 1


# print(numbers)

n = 5
k = 2

print("The chosen place is ", josephus(n, k))

# print(myLinkedList.get(7))
# # print(linked_lst)
