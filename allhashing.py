#Sanjeevini R
#Hashing - Separate Chaining, Linear & Quadratic Probing, Double Hashing

class HashTable:

    def __init__(self, capacity):
        self._capacity = capacity
        self._hashtable = [[] for i in range(self._capacity)]

    def checkprime(self, n):
        if n == 1 or n == 0:
            return False
    
        for i in range(2, n):
            if n % 2 == 0:
                return False
        return True

    def generateprime(self, n):
        if n % 2 == 0:
            n += 1
    
        while not self.checkprime(n):
            n += 2
    
        return n 

    def generateprimesmaller(self, n):
        n -= 1
        while not self.checkprime(n):
            n-= 1
        return n

    def hashval(self, element):
        hashvalue = self.generateprime(self._capacity)
        return element % hashvalue
    
    def hashtwo(self, element):                           #for double hashing
        hashed = self.generateprimesmaller(self._capacity)
        return hashed - (element % hashed)                #commonly used hash2 is prime - (key mod prime)

    def insertintotablelp(self, key, value):              #linear probing
        index = self.hashval(key)
        for i in range(self._capacity):
            if self._hashtable[index] != []:
                index = (index+1) % self.generateprime(self._capacity)
            else:
                self._hashtable[index] = [key, value]
                return

    def insertintotablesc(self, key, value):               #separate chaining
        index = self.hashval(key)
        self._hashtable[index].append([key, value])

    def insertintotableqp(self, key, value):               #quadratic probing
        index = self.hashval(key)
        newind = index
        for i in range(self._capacity):
            if self._hashtable[newind] != []:
                newind = (index + i*i) % self.generateprime(self._capacity)
            else:
                self._hashtable[newind] = [key, value]
                return

    def insertintotabledh(self, key, value):                #double hashing
        index = self.hashval(key)
        secondhash = self.hashtwo(key)
        newind = index
        for i in range(self._capacity):
            if self._hashtable[newind] != []:
                newind = (index + i*secondhash) % self.generateprime(self._capacity)
            else:
                self._hashtable[newind] = [key, value]
                return

    def displaytablelp(self):
        for i in range(len(self._hashtable)):
            print(i,end=':')
            """ for j in table[i]:
                print(j,end=',') """
            print(self._hashtable[i])
            #print()

    def displaytablesc(self):
        for i in range(len(self._hashtable)):
            print(i,end=':')
            for j in table[i]:
                print(j,end=',')
            print()
    
    def displaytableqp(self):
        for i in range(len(self._hashtable)):
            print(i,end=':')
            print(self._hashtable[i])

    def displaytabledh(self):
        for i in range(len(self._hashtable)):
            print(i,end=':')
            print(self._hashtable[i])

""" insertintotablesc(hashtable, 12, 'hello')
insertintotablesc(hashtable, 44, 'my')
insertintotablesc(hashtable, 13, 'name')
insertintotablesc(hashtable, 88, 'is')
insertintotablesc(hashtable, 23, 'nope')
insertintotablesc(hashtable, 94, 'you')
insertintotablesc(hashtable, 11, 'are')
insertintotablesc(hashtable, 39, 'never')
insertintotablesc(hashtable, 20, 'going')
insertintotablesc(hashtable, 16, 'to')
insertintotablesc(hashtable, 5, 'know')

print('Using separate chaining: \n')
displaytablesc(hashtable) """

""" insertintotablelp(hashtable, 12, 'hello')
insertintotablelp(hashtable, 44, 'my')
insertintotablelp(hashtable, 13, 'name')
insertintotablelp(hashtable, 88, 'is')
insertintotablelp(hashtable, 23, 'nope')
insertintotablelp(hashtable, 94, 'you')
insertintotablelp(hashtable, 11, 'are')
insertintotablelp(hashtable, 39, 'never')
insertintotablelp(hashtable, 20, 'going')
insertintotablelp(hashtable, 16, 'to')
#insertintotablelp(hashtable, 5, 'know')
print()
print('using linear probing: \n')
displaytablelp(hashtable) """

""" obj = HashTable(7)
obj.insertintotableqp(45, 'a')
obj.insertintotableqp(87, 'b')
obj.insertintotableqp(47, 'c')
obj.insertintotableqp(63, 'd')
obj.insertintotableqp(18, 'e')
obj.insertintotableqp(72, 'f')
print('using quadratic probing: \n')
obj.displaytableqp() """

#print(obj.generateprimesmaller(13))

obj = HashTable(12)
obj.insertintotabledh(13, 'one')
obj.insertintotabledh(13, 'two')
obj.insertintotabledh(13, 'three')
obj.insertintotabledh(13, 'four')
obj.insertintotabledh(13, 'five')
obj.insertintotabledh(13, 'six')
obj.insertintotabledh(13, 'seven')
obj.insertintotabledh(13, 'eight')
obj.insertintotabledh(13, 'nine')
obj.insertintotabledh(13, 'ten')
obj.insertintotabledh(13, 'eleven')
obj.insertintotabledh(13, 'twelve')
obj.insertintotabledh(14, 'thirteen')
print('using double hashing: \n')
obj.displaytabledh() 