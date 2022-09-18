def apply_to_each(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
numbers = [1, 0, 3.14, -2]

def square(x):
    return x * x

apply_to_each(numbers, square)
print(numbers)

numbers2 = [2, -2, 14, 0, 9.14, -1,25]

def change_direction(x):
    return x * -1

apply_to_each(numbers2,change_direction)
print(numbers2)