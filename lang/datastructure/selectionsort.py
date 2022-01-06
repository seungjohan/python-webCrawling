arr = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]

def selection_sort(arr):

    length = len(arr)-1
    for i in range(length):
        min = i

        for j in range(i+1, length + 1):
            if(arr[j] < arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    print(arr)

selection_sort(arr)
