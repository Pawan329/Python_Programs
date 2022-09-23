# in this code we are using queue module to perform stack
# put - to insert element in stack
# get - to pop element from stack

import queue

stack = queue.LifoQueue(10) # here we can set limit of stack else by default there will be no limit
# limit of stack is set to 10

def put(element):
    if not stack.full():
        stack.put(element)
    else:
        print(" *** Stack overflow ***")

def get():
    if not stack.empty():
        stack.get()
    else:
        print("*** stack is empty ***")


Elements = [1,2,3,4,5,6,7,8,9,10]   # try by increasing element more than 10

for i in Elements:
    put(i)

for i in range(11):   # try to remove element more than 10
    get()

stack.empty()



