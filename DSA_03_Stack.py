# We can use list as stack in python


stack = []
    
def push(element):
    stack.append(element)
    print("Element inserted to the top: ",element)

def pop():
    if len(stack) > 0:
        pop_element = stack.pop()
        print("Element popped: ",pop_element)

    else:
        print("*** Stack is empty ***")

def accessLastElement():
    if len(stack) > 0:
        print("top element: ",stack[-1])

    else:
        print("*** Stack is empty ***")

def viewStack():
    print("Stack: ",stack)

elements = [1,2,3,4,5,6,7]
for i in elements:
    push(i)

viewStack()
pop()
accessLastElement()
viewStack()
