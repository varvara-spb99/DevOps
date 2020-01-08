"""The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2. (Please note that the palindromic number,
in either base, may not include leading zeros.)"""


def is_palindrome(num):
    return str(num) == str(num)[::-1]

def dec_to_bin(num):
    b = ''
    while num > 0:
        b = str(num % 2) + b
        num = num // 2
    return b

count = 1000000
sum = 0
for i in range(count):
    if is_palindrome(i) == True and is_palindrome(dec_to_bin(i)) == True:
        #print(i)
        #print(dec_to_bin(i))
        sum += i
print("Sum =", sum)
