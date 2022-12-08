def my_func(a):
    a = a + 2
    print(a)
    b = my_funcs(a)
    print(b)

def my_funcs(b):
    b = b + 2
    print(b)
    return b

x = int(input())
my_func(x)