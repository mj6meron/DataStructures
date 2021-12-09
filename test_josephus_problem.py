import timeit

cycles = 10
setUp = """
n = 25
m =0

from Josephus_problem import josephus, LinkedList, Node


numbers = []
myLinkedList = LinkedList()

for e in range(1, n + 1):
    myLinkedList.add(e)
    numbers.append(e)
"""
# ----------------------------------------------------------------------------------------------------------------------
print()
print('-----------------------------------------------')

usingList = """josephus(numbers, m, 'arrayList')"""
runningTime_List = timeit.repeat(stmt=usingList, repeat=cycles,
                                 setup=setUp,
                                 number=1)
averageList = '{:.10f}'.format(sum(runningTime_List) / len(runningTime_List))
print("List:\nAverage running time ( %s cycles )->  %s" % (cycles, averageList))
print('\n')
# ----------------------------------------------------------------------------------------------------------------------

print('-----------------------------------------------')
usingListIterator = """josephus(numbers, m, 'arrayListIterator')"""
runningTime_ListIterator = timeit.repeat(stmt=usingListIterator, repeat=cycles,
                                         setup=setUp,
                                         number=1)
averageListIterator = '{:.10f}'.format(sum(runningTime_ListIterator) / len(runningTime_ListIterator))
print("List with Iterator:\nAverage running time ( %s cycles )->  %s" % (cycles, averageListIterator))
print('\n')
# ----------------------------------------------------------------------------------------------------------------------

print('-----------------------------------------------')
usingMyLinkedList = """josephus(myLinkedList, m, 'myLinkedList')"""
runningTime_myLinkedList = timeit.repeat(stmt=usingMyLinkedList, repeat=cycles,
                                         setup=setUp,
                                         number=1)
averageLinkedList = '{:.10f}'.format(sum(runningTime_myLinkedList) / len(runningTime_myLinkedList))
print("LinkedList:\nAverage running time ( %s cycles )->  %s" % (cycles, averageLinkedList))

print('\n')
# ----------------------------------------------------------------------------------------------------------------------


print('-----------------------------------------------')
usingMyLinkedListIterator = """josephus(myLinkedList, m, 'myLinkedListIterator')"""
runningTime_myLinkedListIterator = timeit.repeat(stmt=usingMyLinkedListIterator, repeat=cycles,
                                                 setup=setUp,
                                                 number=1)
averageLinkedListIterator = '{:.10f}'.format(
    sum(runningTime_myLinkedListIterator) / len(runningTime_myLinkedListIterator))
print("LinkedList with Iterator:\nAverage running time ( %s cycles )->  %s" % (cycles, averageLinkedListIterator))

print('\n')
print('-----------------------------------------------')


print(averageList)
print(averageListIterator)
print(averageLinkedList)
print(averageLinkedListIterator)
