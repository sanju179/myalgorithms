#insertion sort

def insertion(arr):
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = eval(input('Enter list to be sorted:'))
print(f'Sorted list:{insertion(arr)}')