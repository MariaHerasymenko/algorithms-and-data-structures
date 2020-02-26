import timeit


def recurrent_func(x):
    p0 = p1 = p2 = 1
    for i in range(x + 1):
        p0, p1, p2 = p1, p2, p2 + p0

    return p0


def recurrent_timer(x):
    begin = timeit.default_timer()
    print("Answer: ", recurrent_func(x), ".Recurrent time: ", timeit.default_timer() - begin)



def recursive_func(x):
    if x <= 1:
        return 1
    return recursive_func(x - 3) + recursive_func(x - 1)


def recursive_timer(x):
    begin = timeit.default_timer()
    print("Answer: ", recursive_func(x), ".Recursive time: ", timeit.default_timer() - begin)


recurrent_timer(10)
recursive_timer(10)
recurrent_timer(15)
recursive_timer(15)
recurrent_timer(25)
recursive_timer(25)
