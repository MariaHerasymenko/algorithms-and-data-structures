#Bubble
'''
def sort(array):
    n = len(array)

    
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
'''


#Modified bubble
'''
def sort(array):
    n = len(array)

    
    for pass_num in range(n - 1, 0, -1):
        for i in range(n - 1):
            if (array[i] <= array[i + 1]):
                break
        else:
            return

        
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
'''


#Choose
'''
def sort(array):
    n = len(array)


    for i in range(n):
        m = 0

        
        for j in range(n - i):
            if array[j] > array[m]:
                m = j


        array[n - (i + 1)], array[m] = array[m], array[n - (i + 1)]
'''


#Insertion
'''
def sort(array):
    n = len(array)

    
    for index in range(1, n):
        currentValue = array[index]
        position = index

            
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break

        
            position -= 1
        array[position] = currentValue
'''
