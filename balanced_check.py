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
# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
comment = ["/", "*"]
lineNumber = 0


# Function to check parentheses
def check_c(myStr):
    stack = []
    openedDocString = False
    for i in myStr:

        if not openedDocString:
            # if it is an opening just append it
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)  # get index of the closing inorder to get the index of corresponding opening
                stackTop = stack[len(stack) - 1]  # top of the stack OPENING symbol
                # if stack not empty ( previously opened) and a closing has to match with stack top
                if (len(stack) > 0) and (open_list[pos] == stackTop):
                    stack.pop()  # then it is balanced
                else:
                    return " Not - balanced "
            elif i == comment[0]:
                pos = myStr.index(i)  # get the current index to check the next /
                next_symbol = myStr[pos + 1]
                if next_symbol == comment[0]:  # if the next symbol / too?
                    return 'we got a comment'
                if next_symbol == comment[1]:  # if the next symbol / too?
                    stack.append(i)
                    stack.append(next_symbol)
                    openedDocString = True
                    print('we got a doc open at index : ' + str(myStr.index(i) + 1))
        # only look for * to close the docstring
        if i == comment[1]:
            pos = myStr.index(i)  # get the current index to check the next /
            next_symbol = myStr[pos + 1]
            print(' we in for ' + i + str(next_symbol))

            if next_symbol == comment[0]:  # if the next symbol / too
                stack.pop(i)
                stack.pop(next_symbol)
                openedDocString = False
                print('Doc closed : ' + str(myStr.index(i) + 1))


string = "{[]/*{*/()}}"
print(string, "-", check_c(string))

string = "[{}{})(]"
print(string, "-", check_c(string))

string = "((()"
print(string, "-", check_c(string))

# print(isinstance(my_variable, int))
