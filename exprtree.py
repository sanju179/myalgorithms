#Sanjeevini R
#IT-B
#3122 21 5002 092
#postfix to infix

from LinkedStack import LinkedStack

class ExprTree:
    class _Node:
        def __init__(self, value, left=None, right=None):
            self._val = value
            self._left = left
            self._right = right
    
    def __init__(self):
        self._root = None
    
    def isoperator(self, c):
        oper = ['+','-','*','/']
        if c in oper:
            return c

    def traverse(self, expr):
        x = LinkedStack()
        for i in expr:
            if i.isdigit() or i.isalpha():
                x.push(self._Node(i))
            elif self.isoperator(i):
                a = x.pop()
                b = x.pop()

                new = self._Node(i, b, a)                   #in reversed order, as last popped node is the left child

                self._root = new
                x.push(new)
    
    def inorder(self):
        if self._root is None:
            return "Tree is empty"
        else:
            self._inorder(self._root)
            return '\nDisplayed!'
            
    
    def _inorder(self, node):
        if node is not None:
            if self.isoperator(node._val):
                print('(', end='')
            self._inorder(node._left)
            print(node._val, end='')
            self._inorder(node._right)
            if self.isoperator(node._val):
                print(')',end='')




