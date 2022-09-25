class _Node:
    def __init__(self, val):
        self._left = None
        self._right = None
        self._val = val
        self._h = 1

class AVLTree:
    def __init__(self):
        self._node = None
    
    def getnode(self):
        return self._node
    
    def getheight(self, node):
        if node is None:
            return 0
        else:
            return node._h
    
    def balanced(self, node):
        if node is None:
            return 0
        else:
            return self.getheight(node._left) - self.getheight(node._right)

    def insertval(self, val, node):

        if node is None:
            return _Node(val)
        elif val <= node._val:
            node._left = self.insertval(val, node._left)
        elif val > node._val:
            node._right = self.insertval(val, node._right)
        node._h = 1 + max(self.getheight(node._left), self.getheight(node._right))
        balance = self.balanced(node)
        if balance > 1 and node._left._val > val:
            return self.rotateRight(node)                   #rotate clockwise to the right
        if balance < -1 and val > node._right._val:
            return self.rotateLeft(node)                    #rotate anticlockwise to the left
        if balance > 1 and val > node._left._val:
            node._left = self.rotateLeft(node._left)        #double rotation, rotate to left then right
            return self.rotateRight(node)
        if balance < -1 and val < node._right._val:         #double rotation, rotate to right then left
            node._right = self.rotateRight(node._right)
            return self.rotateLeft(node)
        return node

    def rotateLeft(self, node):
        a = node._right
        b = a._left
        a._left = node
        node._right = b

        node._h = 1 + max(self.getheight(node._left), self.getheight(node._right))
        a._h = 1 + max(self.getheight(a._left), self.getheight(a._right))

        return a

    def rotateRight(self, node):
        a = node._left
        b = a._right
        a._right = node
        node._left = b

        node._h = 1 + max(self.getheight(node._left), self.getheight(node._right))
        a._h = 1 + max(self.getheight(a._left), self.getheight(a._right))

        return a

    def MinimumValueNode(self, Node):
        if Node is None or Node._left is None:
            return Node
        else:
            return self.MinimumValueNode(Node._left)

    def delete(self, val, node):
        if node is None:
            return None
        elif val < node._val:
            node._left = self.delete(val, node._left)
        elif val > node._val:
            node._right = self.delete(val, node._right)
        else:                                                       #when val == node._val
            if node._left is None:
                note = node._right
                node = None
                return note
            elif node._right is None:
                note = node._left
                note = None
                return note
            
            note2 = self.MinimumValueNode(node._right)
            node._val = note2._val
            node._right = self.delete(note2._val, node._right)
        if node is None:
            return None
        node_h = 1 + max(self.getheight(node._left), self.getheight(node._right))
        balance = self.balanced(node)
        if balance > 1 and node._left._val > val:
            return self.rotateRight(node)                   #rotate clockwise to the right
        if balance < -1 and val > node._right._val:
            return self.rotateLeft(node)                    #rotate anticlockwise to the left
        if balance > 1 and val > node._left._val:
            node._left = self.rotateLeft(node._left)        #double rotation, rotate to left then right
            return self.rotateRight(node)
        if balance < -1 and val < node._right._val:         #double rotation, rotate to right then left
            node._right = self.rotateRight(node._right)
            return self.rotateLeft(node)
        return node

    def searching(self, val, node):
        try:
            if val < node._val:
                return self.searching(val, node._left)
            if val > node._val:
                return self.searching(val, node._right)
            if val == node._val:
                return "value found"
            return "value not found"
        except:
            return "value not found"

    def preorder(self, node):
        if node is not None:
            print(node._val)
            if node._left:
                self.preorder(node._left)
            if node._right:
                self.preorder(node._right)

Tree = AVLTree()
rt = None
rt = Tree.insertval(0, rt)
rt = Tree.insertval(2, rt)
rt = Tree.insertval(4, rt)
rt = Tree.insertval(6, rt)
rt = Tree.insertval(8, rt)
rt = Tree.insertval(10, rt)
print("PREORDER") 
Tree.preorder(rt) 
rt = Tree.delete(2, rt) 
print("PREORDER") 
Tree.preorder(rt) 
rt = Tree.insertval(12, rt)
rt = Tree.insertval(14, rt)
rt = Tree.insertval(16, rt)
rt = Tree.insertval(18, rt)
print("PREORDER") 
Tree.preorder(rt) 
ch = int(input('Enter element to be searched:'))
print(f'Searching for element {ch}')
print(Tree.searching(ch, rt))