""" -------------EXPRESSION TREE------------------ """

from LinkedBinaryTree import LinkedBinaryTree
from LinkedStack import LinkedStack

obj = LinkedBinaryTree()
stack = LinkedStack()

expres = str(input('Enter postfix expression:'))

braces = '({[)}]'
opr = '+-/*'

for i in expres:
    if i not in opr and i not in braces:
        stack.push(obj._BTNode(i))                      #push as BT_NODE, not as str
    elif i in opr:
        b = stack.pop()
        a = stack.pop()

        newnode = obj._BTNode(i, None, a, b)

        obj._root = newnode

        stack.push(newnode)

def inorder(node):
    if node is not None:
        if node._item in opr:
            print('(', end='')
        inorder(node._left)
        print(node._item, end='')
        inorder(node._right)
        if node._item in opr:
            print(')',end='')
    return "Inorder printed!!"

def _inorder(tree):
    if tree._root is None:
        return "Tree is empty"
    else:
        #print(tree._root._item)
        return inorder(tree._root)
    
print(_inorder(obj))