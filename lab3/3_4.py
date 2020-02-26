import math
def find_equation_root(a,b):
    left = a
    right = b
    eps = 0.00000001
    while right - left >eps:
        x = (left+right)/2
        if math.sin(x) == x/3:
            right = x
        else:
            left = x

    return left

print(find_equation_root(1.6,3))
