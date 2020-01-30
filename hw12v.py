"""Написать функцию Фиббоначи fib(n), которая вычисляет
элементы последовательности Фиббоначи:
1 1 2 3 5 8 13 21 34 55 ......."""


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

fib(10)
