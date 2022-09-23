
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
            # insert into left sub-tree
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                #insert into right sub-tree
                self.right.add_child(data)

            else:
                self.right = BinarySearchTreeNode(data)

def build_tree(elements):
    print("Building tree with: ",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print(root)
   