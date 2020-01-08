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
from itertools import repeat

print("Problem 40: ")
string = 1
print(int(''.join([str(string+a) for a in range(200000)])[0])*int(''.join([str(string+a) for a in range(200000)])[9])*int(''.join([str(string+a) for a in range(200000)])[99])
      *int(''.join([str(string+a) for a in range(200000)])[999])*int(''.join([str(string+a) for a in range(200000)])[9999])
      *int(''.join([str(string+a) for a in range(200000)])[99999])*int(''.join([str(string+a) for a in range(200000)])[999999]))

#другое решение без list comprehension
string = ''
a = 1
while len(string)<1000000:
    string = string + str(a)
    a +=1
#print(string)
res = int(string[0])*int(string[9])*int(string[99])*int(string[999])*int(string[9999])*int(string[99999])*int(string[999999])
#print(string[0], string[9], string[99], string[999], string[9999], string[99999], string[999999] )
print(res)




