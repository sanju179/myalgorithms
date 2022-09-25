#quick sort

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