# We'll use LIST to inmplemet queue data sctructure
# menthods - append and pop

queue = []

def insert(element):
    queue.append(element)
    print("Element inserted: ",element)

def remove():
    if len(queue)>0:
        element = queue.pop(0)     # here we are using "0" index in pop method to remove first element
        print("Element removed: ",element)

    else:
        print("*** Queue is emmpty ***")


Elemments = [1,12,23,254,1155]

for i in Elemments:
    insert(i)
    print("Updated Queue: ",queue)

for i in range(3):
    remove()
    print("Updated Queue: ",queue)