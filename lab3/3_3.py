def find_min(a,b):
    left = a
    right = b
    eps = 0.0000001
    while right - left >eps:
        x = (left+right)/2
        if x**3  + x + 1 >5:
            right = x
        else:
            left = x

    return left

print(find_min(0,10))
