"""Написать функцию Фиббоначи fib(n), которая вычисляет
элементы последовательности Фиббоначи:
1 1 2 3 5 8 13 21 34 55 .......

def fib(n):
    a = 1
    b = 1
    if n >= 1: # если пользователь захочет, чтобы ему вывели 1 число и больше
        print(str(a)) # если пользователь захочет, чтобы ему вывели одно число, то дальше if и for не будут исполняться
    if n >= 2:
        print(str(b))
    for i in range(n-2):
        a, b = b, a + b
        print(b)
    return

fib(10)

def fib(n, lst=[]):
    if len(lst) == 0:
        lst.append(1)
        lst.append(1)
        if n == 1:
            print("1")
            return
        if n == 2:
            print("1 1")
            return
        n = n-2
    else:
        lst.append()



def fib(n):
    a = 1
    b = 1
    if n >= 1:
        print(str(a))
        if n >= 2:
            print(str(b))
            if n>=3:
                for i in range(n-2):
                    a, b = b, a + b
                    print(b)
    return

fib(10)"""


def fib(n):
    lst=[]
    a = 1
    b = 1
    if n==1:
        lst.append(a)
    elif n==2:
        lst.append(a)
        lst.append(b)
    elif n>=3:
        lst.append(a)
        lst.append(b)
        for i in range(n-2):
            a, b = b, a + b
            lst.append(b)
    return lst

print(fib(10))
