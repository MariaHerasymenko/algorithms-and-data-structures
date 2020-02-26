"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""
def bsearch_leftmost(array, x):
    k = -1
    r = len(array)
    while r - k > 1:
        m = (r + k) // 2
        if array[m] < x:
            k = m
        else:
            r = m
    return l


def bsearch_rightmost(array, x):
    k = -1
    r = len(array)
    while r - k > 1:
        m = (r + k) // 2
        if array[m] <= x:
            k = m
        else:
            r = m
    return r
def counter(array, x):
   left = bsearch_leftmost(array,x)
   right = bsearch_rightmost(array,x)
   res= right - left -1
   return res

