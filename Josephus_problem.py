"""
Josephus problem
"""


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
        return "%s" % tobe_removed.data


# --------------------------------------------------------------------------------------------------------------


def josephus(ls, skip, data_structure):
    idx = skip
    if data_structure == "arrayList":
        while len(ls) > 1:
            ls.pop(idx)
            idx = (idx + skip) % len(ls)
        return ls[0]
    if data_structure == "myLinkedList":
        while ls.size() > 1:
            ls.remove(idx)
            idx = (idx + skip) % ls.size()
        return ls.get(0)
    if data_structure == "deQueue":
        while len(ls) > 1:
            del ls[idx]
            idx = (idx + skip) % len(ls)
        return ls[0]

def josephus_show(ls, skip, data_structure):
    idx = skip
    if data_structure == "arrayList":
        # pop automatically skips the dead guy
        while len(ls) > 1:
            print('Eliminated: %s, at index: %s' % (ls.pop(idx), idx))  # kill prisoner at idx
            idx = (idx + skip) % len(ls)
        print('Remaining survivor ---> ', ls[0])

    if data_structure == "myLinkedList":
        while ls.size() > 1:
            print('Eliminated: %s, at index: %s' % (ls.remove(idx), idx))  # kill prisoner at idx
            idx = (idx + skip) % ls.size()
        print('Remaining survivor ---> ', ls.get(0))
    if data_structure == "deQueue":
        while len(ls) > 1:
            print('Eliminated: %s, at index: %s' % (ls[idx], idx))  # kill prisoner at idx
            del ls[idx]
            idx = (idx + skip) % len(ls)
        print('Remaining survivor ---> ', ls[0])
