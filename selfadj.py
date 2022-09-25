#Sanjeevini IT-B
#Self Adjusting Lists

class SelfAdj:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        '''Initialization of instance variables'''
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def insert(self, val):
        '''Insert value at the head of the list'''
        self._head = self._Node(val, self._head)
        self._size += 1
    
    def pop(self):
        '''Pops element from the head of the list'''
        if self.is_empty():
            raise Empty('SelfAdj List is empty')
        a = self._head._element
        self._head = self._head._next
        self._size -= 1
        return a
    
    def finditem(self, item):
        '''Searches and returns the position of the item'''
        val = self._head
        pos = 1
        while val._next is not None:
            if val._element == item:
                self.change(val)
                return f'Item {item} found at position {pos}'
            val = val._next
            pos += 1
        else:
            if val._element == item:
                self.change(val)
                return f'Item {item} found at position {pos}'
            else:
                return 'Value not found!'

    def __str__(self):
        val = self._head
        while val._next is not None:
            print(val._element)
            val = val._next
        return val._element                 #the element which was inserted first

    def change(self, item):
        '''Brings the found item to the head of the list'''
        value = self._head
        while value._next is not item:
            value = value._next
            continue
        else:
            value._next = item._next
        item._next = self._head
        self._head = item
        
            
            