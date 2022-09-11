def apply_to_each(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])

numbers = [1, 0, 3.14, -2]

def square(x):
    return x * x

apply_to_each(numbers, square)
print(numbers)

apply_to_each(numbers,abs)
print(numbers)
apply_to_each(numbers,int)
print(numbers)
apply_to_each(numbers,float)
print(numbers)
apply_to_each(numbers,str)
print(numbers)