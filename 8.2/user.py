N = 1000000

def sort(array, a, b):
    if a >= b:
        return
    mas = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < mas:
            left += 1
        while mas < array[right]:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    sort(array, a, right)
    sort(array, right + 1, b)
