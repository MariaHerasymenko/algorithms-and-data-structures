def bsearch_search(array, x):
    i = 0
    while array[i] <= x:
        if x<=array[i]:
            return i
        if i ==len(array)-1:
            break
        i+=1
    return -1

array = [1,3,4,5,7,9,10,12,58,102]
x= 12
print(bsearch_search(array,x))
