#List ADT

class ArrayStack:
    default = 10
    def __init__(self):
        self._data = [None] * ArrayStack.default
        self._data1 = self._data[:ArrayStack.default//2]
        self._data2 = self._data[ArrayStack.default//2:]
        self._n1 = 0
        self._n2 = 0
    
    def __len__(self, n):
        if n == 0:
            return f"Length of Stack One: {self._n1}"
        elif n == 1:
            return f"Length of Stack Two: {self._n2}"
        else:
            return "Invalid Stack"   

    def is_empty(self, n):
        if n == 0:
            return len(self._data1) == 0
        elif n == 1:
            return len(self._data2) == 0
        else:
            return "Invalid stack"

    def is_full(self):
        if len(self._data) == len(self._data1 + self._data2) and None not in (self._data1 + self._data2):
            return "Stack full"
        else:
            return False

    def push(self, n, val):
        if n == 0 and self.is_full() != True:
            self._data1[self._n1] = val
            self._n1 += 1
            self._data = self._data1 + self._data2
        elif n == 1 and self.is_full() != True:
            self._data2[self._n2] = val
            self._n2 += 1
            self._data = self._data1 + self._data2
        else:
            raise StackDoesNotExist

    def top(self, n):
        if n == 0:
            if self.is_empty() == True:
                raise Empty('Stack is empty')
        elif n == 1:
            if self.is_empty() == True:
                raise Empty('Stack is empty')
        return data[-1]
    
    def pop(self, n):
        if n == 0:
            if self.is_empty(0) == True:
                raise Empty('Stack empty')
                self._n1 -= 1
            ans = self._data1[self._n1-1]
            self._data1[self._n1-1] = None
            self._n1 -= 1
            self._data = self._data1 + self._data2
        elif n == 1:
            if self.is_empty(1) == True:
                self._n2 -= 1
            ans = self._data2[self._n2-1]
            self._data2[self._n2-1] = None
            self._n2 -= 1
            self._data = self._data1 + self._data2
        return 'Value popped'
    
    def __str__(self):
        print("Stack One from array:")
        for i in self._data[:len(self._data)//2]:
            print(i)
        print("Stack Two from array:")
        for i in self._data[len(self._data)//2:len(self._data)-1]:
            print(i)
        return self._data[len(self._data)-1]
        
        