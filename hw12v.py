"""Написать функцию Фиббоначи fib(n), которая вычисляет
элементы последовательности Фиббоначи:
1 1 2 3 5 8 13 21 34 55 .......
"""
def fib(n):
    a = 1
    b = 1
    if n==1:
        return [1]
    elif n==2:
        return [1, 1]
    elif n>=3:
        lst = [1, 1]
        for i in range(n-2):
            a, b = b, a + b
            lst.append(b)
        return lst

print(fib(10))
