"""
Question 2
Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20
"""

def multiply_nums(l):
    l = str_list(l)
    p = 1
    for i in l:
        p = p * i
    return p

def str_list(s):
    s = s.split(', ')
    return [int(i) for i in s]

l =input("Enter comma and space seperated list of numbers\neg. 1, 2, 3 : ")
p = multiply_nums(l)
print("multiply_nums(",l,") ➞",multiply_nums(l))