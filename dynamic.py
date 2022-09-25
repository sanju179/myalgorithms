import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self.makearray(self._capacity)

    def makearray(self, c):
        return (c * ctypes.py_object)()

    def append(self, val):
        if self._n == self._capacity:
            self._resize(-1, 2*self._capacity)
        
        self._A[self._n] = val
        self._n += 1

    def _resize(self, j, c):
        B = self.makearray(c)
        if j == -1:
            for b in range(self._n):
                B[b] = self._A[b]
            self._A = B
            self._capacity = c
            print("capacity now:", self._capacity)
        else:
            return B
        
    def insert(self, k, val):
        if self._n == self._capacity:
            B = self._resize(k, 2 * self._capacity)
        else:
            B = self.makearray(self._capacity)
        for j in range(k):
            B[j] = self._A[j]
        B[k] = None
        for m in range(k+1, self._n+1):
            B[m] = self._A[m-1]
        self._A = B
        self._A[k] = val
        self._n += 1

    def len(self):
        return self._n
        
    def __str__(self):
        for i in range(self._n):
            print(self._A[i])
    
