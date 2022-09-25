#selection sort

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