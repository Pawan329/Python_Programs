
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

            while self.head is not None:
                print(self.head.data)
                self.head = self.head.ref

    def add_begin(self, data):
        new_node = Node(data)  # creating instance of Node class
        new_node.ref = self.head # assgning address to 1st node
        self.head =  new_node  

LL1 = LinkedList()

elements = [10,15,20,25,30]

for element in elements:
    LL1.add_begin(element)

LL1.print_LL()