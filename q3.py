"""
Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.
"""

def square_digits(s):
    s1 = ''
    for i in s:
        s1 = s1 + str(int(i)*int(i))
    return s1

s = input("Enter Number ")
s1 = square_digits(s)
print("square_digits(",s,") ➞",s1)