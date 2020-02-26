def find_equation_root(a,b):
    left = a
    right = b
    eps = 0.0000000001
    while right - left >eps:
        x = (left+right)/2
        if x**3 +4*x**2+x==6:
            right = x
        else:
            left = x

    return left

print(find_equation_root(0,2))
