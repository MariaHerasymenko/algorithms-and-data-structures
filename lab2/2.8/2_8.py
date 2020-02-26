'''Реалізуйте алгоритм лінійного пошуку всіх елементів списку,
що є степенями двійки та визначте асимптотичну складність
отриманого алгоритму.'''
def check(el):

    if el & (el-1)==0 and el !=0:
        return 1
    else:
        return 0



array  = [1,2,3,6,8,11,16,23,27,30,32,45,64]
for i in range(len(array)):
    checker = check(array[i])
    if checker == 1:
        print("YES")
    else:
        print("NO")

