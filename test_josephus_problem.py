import timeit

cycles = 100
setUp = """
n = 100
m = 1

from Josephus_problem import josephus, LinkedList, Node
import collections

linked_lst = collections.deque()
numbers = []
myLinkedList = LinkedList()

for e in range(1, n + 1):
    myLinkedList.add(e)
    numbers.append(e)
    linked_lst.append(e)
"""

print('********************************** List')
usingList = """josephus(numbers, m, 'arrayList')"""
runningTime_arrayList = timeit.repeat(stmt=usingList, repeat=cycles,
                                      setup=setUp,
                                      number=1)
print(" The running time is : " + str(sum(runningTime_arrayList) / len(runningTime_arrayList)))


print('********************************** my Linked list')
usingMyLinkedList = """josephus(myLinkedList, m, 'myLinkedList')"""
runningTime_myLinkedList = timeit.repeat(stmt=usingMyLinkedList, repeat=cycles,
                                         setup=setUp,
                                         number=1)
print(" The running time is : " + str(sum(runningTime_myLinkedList) / len(runningTime_myLinkedList)))


print('********************************** builtin Linked list with iterator(deque)')
using_deQueue = """josephus(linked_lst, m, 'deQueue')"""
runningTime_deQueue = timeit.repeat(stmt=using_deQueue, repeat=cycles,
                                    setup=setUp,
                                    number=1)
print(" The running time is : " + str(sum(runningTime_deQueue) / len(runningTime_deQueue)))
