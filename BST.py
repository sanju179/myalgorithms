from LinkedBinaryTree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):

    def add(self, item, pos):
        if pos == None:
            return self.addRoot(item)
        if pos._item < item:
            if self.right(pos) == None:
                return self.addRight(item, pos)
            self.add(item, self.right(pos))
            
        elif pos._item > item:
            if self.left(pos) == None:
                return self.addLeft(item, pos)
            self.add(item, self.left(pos))
        
        else:
            return None

    def search(self, item):
        pos = False
        start = self._root
        ht = self.height()
        for i in range(ht+1):
            if item < start._item:
                start = start._left
            elif item == start._item:
                return start
            elif item > start._item:
                start = start._right
        return pos

    def getmin(self, node):
        while node._left:
            node = node._left
        return node

    def delete(self, item, temp):
        if temp == None:
            return None
        
        if item > temp._item:
            temp._right = self.delete(item, temp._right)
        elif item < temp._item:
            temp._left = self.delete(item, temp._left)
        else:
            if temp._left is None:
                node = temp._right
                temp = None
                return node

            if temp._right is None:
                node = temp._left
                temp = None
                return node

            node = self.getmin(temp._right)
            temp._item = node._item
            temp._right = self.delete(item, temp._right)                             
        return temp

obj = BinarySearchTree()
rt = obj.add(60, None)
obj.add(70, rt)
obj.add(50, rt)
obj.add(40, rt)
obj.add(55, rt)
obj.add(23, rt)
obj.add(58, rt)
obj.add(79, rt)
obj.add(52, rt)
print(obj.__str__())
print(obj.delete(50, rt))
print("--POSTDELETION--")
print(obj.__str__())