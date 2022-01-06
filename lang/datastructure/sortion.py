def insertion(list):
    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j-1] > list[i]:
                list[i], list[j-1] = list[j-1], list[i]
    
def bubble(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

def selection(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1,len(list),1):
            if list[j] < min:
                min = j
        list[i], list[min] = list[min], list[i]

def merge_sort(list):
    def sort(low, high):
        if low>high:
            mid = (low+high)/2
            sort(list, low, mid)
            sort(list, mid+1, high)
            merge(list, low, mid, high)

    def merge(low, mid, high):
        arr = []

        l, h = low, mid

        while l <= low and h <= high:
            if list[l] < list[h]:
                arr.append(list[l])
                l+=1
            else:
                arr.append(list[h])
                h+=1

        while l < mid:
            arr.append(list[l])
            l+=1
        while h < high:
            arr.append(list[h])
            h+=1

        for i in range(low, high):
            list[i] = arr[i]






def merge_sort_blog(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


def merge_sort_blog_2(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))


def qsort(list, low, high):
    if low<high:
        pivot = partition(list, low, high)
        qsort(list, low, pivot-1)
        qsort(list, pivot+1, high)

def partition(list, pivot, high):
    i = pivot+1
    j = high
    while True:
        while i < high and list[i] < list[pivot]:
            i+=1
        while j > pivot and list[j] > list[pivot]:
            j -=1
        if j <= i:
            break
        list[i], list[j] = list[j], list[i]
        i+=1
        j-=1

    list[pivot], list[j] = list[j], list[pivot]

    return j


import heapq

list = [23, 45, 67, 86, 43, 25, 75]

heapq.heapify(list)

s = []
while list:
    s.append(heapq.heappop(list))

def adjust(i, size):
    while i*2 <= size:
        k = 2*i
        if k < size and list[k] < list[k+1]:
            k+=1
        if list[i] >= list[k]:
            break
        list[i], list[k] = list[k], list[i]
        i = k

def heap_sort(list):
    hsize = len(list)-1
    for i in reversed(range(1, hsize//2+1)):
        adjust(i, hsize)

    for i in range(hsize):
        list[1], list[hsize] = list[hsize], list[1]
        adjust(1, hsize-1)
        hsize -=1
