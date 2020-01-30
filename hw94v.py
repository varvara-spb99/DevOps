"""Решить несколько задач из projecteuler.net

Решения должны быть максимально лаконичными, и использовать list comprehensions.

problem9 - list comprehension : one line
problem6 - list comprehension : one line
problem48 - list comprehension : one line
problem40 - list comprehension

Problem40:
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the n-th digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
185185"""

print("Problem 40: ")
string = ''.join([str(1+a) for a in range(200000)])
lst = [int(string[a]) for a in [0, 9, 99, 999, 9999, 99999, 999999]]
res = 1
for i in lst:
    res = res * i
print(res)






