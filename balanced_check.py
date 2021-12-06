"""
This simple algorithm uses a stack and is as follows:
Make an empty stack.
Read characters until end of file.
If the character is an opening symbol:
    push it onto the stack.
If it is a closing symbol:
    then if the stack is empty report an error.
    Otherwise, pop the stack.
If the symbol popped is not the corresponding opening symbol:
    then report an error.
At end of file, if the stack is not empty:
    report an error.

Runs on linear time and makes only one pass through the input.
Extra work can be done to attempt to decide what to do when an error is reported—such as
identifying the likely cause.

Examples:
([]{}) is balanced.
({[]}) is balanced.
([)] is not balanced.
(} is not balanced.
()} is not balanced.
({} is not balanced.
"""

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
comment = ["/", "*"]
lineNumber = 0


# Function to check parentheses
def check_line(myStr):
    currentIndex = 0
    stack = []
    openedDocString = False
    skipNext = False
    for i in myStr:
        if not openedDocString:
            # if it is an opening just append it
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                position = close_list.index(
                    i)  # get index of the closing in order to get the index of corresponding opening
                # if stack not empty ( previously opened) and a closing has to match with stack top
                if (len(stack) > 0) and (open_list[position] == stack[len(stack) - 1]):
                    stack.pop()  # then it is balanced
                else:
                    return "unBalanced"
            elif i == comment[0]:
                # get the current index to check the next /
                next_symbol = myStr[currentIndex + 1]
                if next_symbol == comment[0]:  # if the next symbol / too?
                    break
                if next_symbol == comment[1]:  # if the next symbol / too?
                    openedDocString = True
        #                  print('we got a doc open at index : ' + str(currentIndex + 1))

        # only look for * to close the docstring

        elif i == comment[1] and not skipNext:
            next_symbol = myStr[currentIndex + 1]
            if next_symbol == comment[0]:  # if the next symbol / too
                #              print('Doc closed : ' + str(myStr.index(i) + 1))
                openedDocString = False
        currentIndex += 1
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


cFile_1 = "test1_balance_check.c"


def programFile(myFile):
    my_list = []
    with open(myFile, 'r') as lines:
        for line in lines:
            my_list.append(lines.readline().strip('\n'))
    return my_list


def check(File):
    stringsList = programFile(cFile_1)
    print(len(stringsList))
 #   for e in range(0, len(stringsList)):
  #      print(e)
   #     print('-------------')
    #    print(check_line(e))


check(cFile_1)

"""
string = "{[]{()}}"
print(string, "-", check_line(string))

string = "[{}{})(]"
print(string, "-", check_line(string))

string = "((()"
print(string, "-", check_line(string))
"""
