
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Linked list is emplty!!")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head =  new_node

LL1 = LinkedList()

elements = [10,15,20,25,30]

for element in elements:
    LL1.add_begin(element)

LL1.print_LL()