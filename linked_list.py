"""
Custom singly LinkedList - AddressBookPage
Each node containing - name, address and a point to the next node if any

The Tail of the LinkedList points to none
And the Head is the fist element
"""


class Node:
    address = None
    name = None
    next_node = None

    def __init__(self, name, address):
        """Create an instance node"""
        self.name = name
        self.address = address

    def __repr__(self):
        """Represent a node"""
        return '[%s: %s]' % (self.name, self.address)


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

    def add(self, name, address):
        """Add note in front of the header, simple implementation"""
        self.length += 1
        new_node = Node(name, address)
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
                elements.append('☺ [%s: %s]' % (i.name, i.address))
            elif i.next_node is None:
                elements.append('[%s: %s] ✌ ' % (i.name, i.address))
            else:
                elements.append('[%s: %s]' % (i.name, i.address))
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
        return i  # found and return the element

    # add functionality of iterables to iterate through the list
    # the iterator includes next(), previous(), hasNext(), and the most important - Remove()
    # Include a midCount/check the book/ to indicate new modifications after an iterator is created. page 76 of the book
    # keep truck of size value to operate in constant time ie replace the size function
    # here is a resource https://www.youtube.com/watch?v=jTYiNjvnHZY
    # Add clear method for node to clear its contents
    # check the iterator from the book. Helpful
    # The remove operation is nasty - changing mid-count

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


l = LinkedList()

meron = Node('Mike', 'Stockholm')
l.head = meron
l.add('Yonatan', 'Asmara')
l.add('Teddy', 'Kristianstad city')
l.add('John', 'Morocco')
l.add('Edward', 'Spain')
print('The size is: %s' % l.size())
print(l.get(3))
print(l)
print(l.remove(4))
print(l)
print('The size is: %s' % l.size())
print('---------------')
print(format(l))


print('****************************')
