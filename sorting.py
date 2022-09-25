""" BUBBLE SORT
repeatedly compares two element and 
swaps if in wrong order
"""

def bubblesort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
    return data

seq = eval(input('Enter list: '))
print(bubblesort(seq))

# Best-case: O(n2)
# Worst-case: O(n)

""" SELECTION SORT
Repeatedly finds the minimum element and sorts.
Maintains two arrays. """

def selsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        
    return arr

arr = eval(input('Enter list to be sorted:'))
print(f'Sorted list:{selsort(arr)}')

# Best-case: O(n)
# Worst-case: O(n2)

""" INSERTION SORT
always sorted sub-array.
inserts element from unsorted array at correct position.
"""

def insertion(arr):
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = eval(input('Enter list to be sorted:'))
print(f'Sorted list:{insertion(arr)}')

# Best-case: O(n)
# Worst-case: O(n2)

""" MERGE SORT
divides array into equal halves and
combines them in a sorted manner """

def merge_sort(arr):
    n = len(arr)
    
    if n == 1:
        return arr
    
    first = arr[:n//2]
    second = arr[n//2:]

    merge_sort(first)
    merge_sort(second)

    i = j = k = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            j += 1
        k += 1
    while i < len(first):
        arr[k] = first[i]
        i += 1
        k += 1
    while j < len(second):
        arr[k] = second[j]
        j += 1
        k += 1
    
    return arr

arr = eval(input('Enter list to be sorted:'))
print(f'Sorted list:{merge_sort(arr)}')

# Best-case: O(nlogn)
# Worst-case: O(nlogn)

""" QUICK SORT
maintains a higher and lower array relative to a pivot """
def quicksort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    else:
        pivot = arr.pop()
   
    high = []
    low = []
    for i in arr:
        if i < pivot:
            low.append(i)
        else:
            high.append(i)
    
    return quicksort(low) + [pivot] + quicksort(high)

arr = eval(input('Enter list to be sorted:'))
print(f'Sorted list:{quicksort(arr)}')

# Best-case: O(nlogn)
# Worst-case: O(n2)