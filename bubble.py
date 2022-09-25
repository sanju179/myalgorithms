#bubble sort
def bubblesort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
    return data

seq = eval(input('Enter list: '))
print(bubblesort(seq))