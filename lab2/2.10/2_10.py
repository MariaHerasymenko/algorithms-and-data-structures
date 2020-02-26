'''Реалізуйте алгоритм бінарного пошуку з використанням рекурсії.'''
def binarySearch(array, left, right, el):
    if right - left >= 0:
        middle = (left + right) // 2

        if array[middle] == el: return middle
        if array[middle] < el: return binarySearch(array, middle+1, right, el)
        return binarySearch(array, left, middle-1, el)

    return -1




c = list(map(int, input().split()))
n = int(input())

check = binarySearch(c,0,len(c)-1,n)
if check==-1:
    print("Element is not present in array")
else:
    print("Element is in array")
