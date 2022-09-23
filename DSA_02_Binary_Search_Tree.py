# Tutorial links
# 1 - https://www.youtube.com/watch?v=5kaVCwKd3hI
# 2 - https://www.youtube.com/watch?v=18YDhu9IFws
# 3 - https://www.youtube.com/watch?v=MD5moPUkTHU


class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None      # intializing root node of tree

    def insert(self, data):
        if self.key is None:  # [None, None, None]
            self.key = data   # [None, data, None]
            return

        if self.key == data:  # if want to insert duplicate value
            return

        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)

            else:
                self.lchild = BST(data)  # [None, data, None]

        else:
            if self.rchild:
                self.rchild.insert(data)

            else:
                self.rchild = BST(data)  # [None, data, None]

list1 = [20,4,30,4,1,5,6]

root = BST(list1[0]) # can be - root = BST(None) if want to create root node without value 

for i in list1:
    root.insert(i)

print(root.key)
print(root.lchild.key)
print(root.rchild.key)

   