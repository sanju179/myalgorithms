
class MinHeap:
    
    def __init__(self, capacity):
        self._data = [0] * capacity
        self._capacity = capacity
        self._size = 0

        self._pre = []
        self._in = []
        self._post = []

    #--------------------helper methods----------------------------
    def ParentIndex(self, index):
        return (index-1) // 2
    
    def LeftIndex(self, index):
        return 2*index + 1
    
    def RightIndex(self, index):
        return 2*index + 2

    def hasparent(self, index):
        return self.ParentIndex(index) >= 0
    
    def hasleft(self, index):
        return self.LeftIndex(index) < self._size
    
    def hasright(self, index):
        return self.RightIndex(index) < self._size
    
    def parent(self, index):
        return self._data[self.ParentIndex(index)]
    
    def leftchild(self, index):
        return self._data[self.LeftIndex(index)]
    
    def rightchild(self, index):
        return self._data[self.RightIndex(index)]

    def isFull(self):
        return self._size == self._capacity

    def toswap(self, ind1, ind2):
        self._data[ind1], self._data[ind2] = self._data[ind2], self._data[ind1]
    

    #-------------adding----------------

    def addtoheap(self, el):
        if self.isFull():
            self._data._resize(2*self._capacity)
        self._data[self._size] = el
        self._size += 1
        self.heapifyUp()
    
    def heapifyUp(self):
        ind = self._size - 1
        while (self.hasparent(ind) and self.parent(ind) > self._data[ind]):
            self.toswap(ind, self.ParentIndex(ind))
            ind = self.ParentIndex(ind)

    def removefromheap(self):
        if self._size == 0:
            raise Empty('Heap is empty')
        ans = self._data[0]
        self._data[0] = self._data[self._size-1]
        #self._data[self._size-1] = 0
        self.heapifyDown()
        self._size -= 1
        return f"Removed Element: {ans}"
    
    def heapifyDown(self):
        index = 0
        while(self.hasleft(index)):
            smallerindex = self.LeftIndex(index)
            if(self.hasright(index) and self.rightchild(index) < self.leftchild(index)):
                smallerindex = self.RightIndex(index)
            if(self._data[index] < self._data[smallerindex]):
                break
            else:
                self.toswap(index,smallerindex)
            index = smallerindex

    def _resize(self, capacity):
        old = self._data
        new = [0]*capacity
        for i in range(old):
            new[i] = old[i]
        self._capacity = capacity
        return new
    
    def preorder(self):
        if self._size == 0:
            return "Heap is empty"
        else:
            self._preorder(0)
            return f"Preordered Heap: {self._pre}"
    
    def _preorder(self, ind):
        self._pre.append(self._data[ind])
        if self.hasleft(ind):
            self._preorder(self.LeftIndex(ind))
        
        if self.hasright(ind):
            self._preorder(self.RightIndex(ind))

    def inorder(self):
        if self._size == 0:
            return "Heap is empty"
        else:
            self._inorder(0)
            return f"Inordered Heap: {self._in}"
    
    def _inorder(self, ind):
        
        if self.hasleft(ind):
            self._inorder(self.LeftIndex(ind))
        self._in.append(self._data[ind])
        if self.hasright(ind):
            self._inorder(self.RightIndex(ind))

    def postorder(self):
        if self._size == 0:
            return "Heap is empty"
        else:
            self._postorder(0)
            return f"Postordered Heap: {self._post}"
    
    def _postorder(self, ind):
        if self.hasleft(ind):
            self._postorder(self.LeftIndex(ind))
        if self.hasright(ind):
            self._postorder(self.RightIndex(ind))
        self._post.append(self._data[ind])

    def __str__(self):
        arr=[]
        for i in range(self._size):
            arr.append(self._data[i])
        return f"Heap: {arr}"

obj = MinHeap(15)
obj.addtoheap(10)
obj.addtoheap(20)
obj.addtoheap(30)
obj.addtoheap(15)

obj.addtoheap(12)
obj.addtoheap(13)
obj.addtoheap(25)
obj.addtoheap(35)
obj.addtoheap(4)
obj.addtoheap(40)
obj.addtoheap(18)
obj.addtoheap(70)
obj.addtoheap(16)
obj.addtoheap(11)
obj.addtoheap(9)

print(obj.__str__())
obj.removefromheap()
print(obj.__str__())
print(obj.preorder())
print(obj.inorder())
print(obj.postorder())