"""Решить несколько задач из projecteuler.net

Решения должны быть максимально лаконичными, и использовать list comprehensions.

problem9 - list comprehension : one line
problem6 - list comprehension : one line
problem48 - list comprehension : one line
problem40 - list comprehension

Problem6:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

print("Problem 6: ")
print(sum(range(1, 101)) ** 2 - sum([i**2 for i in range(1, 101)]))


