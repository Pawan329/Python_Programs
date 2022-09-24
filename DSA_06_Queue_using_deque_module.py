
from collections import deque   #deque - double ended queue

q = deque()


def insert(element):
    q.append(element)

def removeRight():  # FIFO -  first IN first OUT
    if q:       # Check if q is not empty
        e = q.pop()
        print("Last remove: ",e)

    else:
        print("*** Queue is empty ***")

def removeLeft():    # # LIFO -  first IN first OUT
    if q:
        e = q.popleft()
        print("Last remove: ",e)

    else:
        print("*** Queue is empty ***")


Elements = [1,10,50,60,70]

for i in Elements:
    insert(i)
    print("Updated Queue: ",q)

for i in range(3):
    removeRight()
    print("Updated Queue: ",q)

# for i in range(3):
#     removeLeft()
#     print("Updated Queue: ",q)




