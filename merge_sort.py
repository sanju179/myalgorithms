#merge_sort
import random
import time
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

arr = [random.randint(0, 100) for i in range(2000)]

start = time.time()
merge_sort(arr)
end = time.time()
diff = end - start
print(arr)
print(f'Time taken:{diff}')