"""Решить несколько задач из projecteuler.net

Решения должны быть максимально лаконичными, и использовать list comprehensions.

problem9 - list comprehension : one line
problem6 - list comprehension : one line
problem48 - list comprehension : one line
problem40 - list comprehension

Problem9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

print("Problem 9: ")
print([a*b*(1000-a-b) for a in range(1, 1000) for b in range(1, 1000) if a*a + b*b == (1000 - a - b)*(1000 - a - b)][0])

