"""
Josephus problem
"""

# --------------------------------------- LinkedList without Iterator -------------------------------------------
import itertools


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
            return self.head.data
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
        if node_index == 0:  # if index 0 return first element
            old_head = self.head
            self.head = old_head.next_node
            self.length -= 1
            return "%s" % old_head.data
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
        self.length -= 1
        del tobe_removed
        return 'Removed'

    def __iter__(self):
        """ Iterate over the linked list."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next_node


# --------------------------------------------------------------------------------------------------------------


def josephus(ls, skip, data_structure):
    idx = skip
    if data_structure == "arrayList":
        while len(ls) > 1:
            ls.pop(idx)  # constant
            idx = (idx + skip) % len(ls)
        return ls[0]
    if data_structure == "arrayListIterator":
        Iterator = itertools.cycle(ls)
        for person in Iterator:  # linear print(person)
            if len(ls) == 1: break
            print(person)
            if person == ls[idx]:
                print('Inside: ' + str(person))
                ls.pop(idx)  # linear
                idx = (idx + skip) % len(ls)
                print(ls , len(ls), idx)
                print('--------------')
        return ls[0]
    if data_structure == "myLinkedList":
        while ls.size() > 1:
            ls.remove(idx)  # linear
            idx = (idx + skip) % ls.size()
        return ls.get(0)
    if data_structure == "myLinkedListIterator":
        Iterator = itertools.cycle(ls)
        for person in Iterator:  # linear print(person)
            if ls.size() == 1: break
            if person == ls.get(idx):
                print('Inside: ' + str(person))
                ls.remove(idx)  # linear
                idx = (idx + skip) % ls.size()
        return ls.get(0)


n = 5
m = 1
my_list = []
my_linkedlist = LinkedList()

for i in range(1, n + 1):
    my_list.append(i)
    my_linkedlist.add(i)

print(josephus(my_list, m, 'arrayListIterator'))
