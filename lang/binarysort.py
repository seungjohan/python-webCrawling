# list = [ x for x in input("Type the num list(divide with ,): ").split(',')]
# target = float(input("which num are you looking for?: "))

list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
target = 92
length = len(list)

list.sort()
left, right = 0, length -1

while left <= right:
    mid = (left + right) // 2

    if target == list[mid]:
        print(mid + 1)
        break
    elif (list[mid] < target):
        left = mid - 1
    else:
        right = mid + 1


# def Bsearch(length, target):
#     mid = len / 2
#     if ( target == list[mid]):


# target = 25
# m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
# length = len(m_list)

# m_list.sort()
# left = 0 
# right = length-1

# while left<=right:
#     mid = (left+right)//2
#     if m_list[mid] == target:
#         print(mid+1)
#         break
#     elif m_list[mid]>target:
#         right = mid-1
#     else :
#         left = mid+1