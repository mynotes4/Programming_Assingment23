"""
Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits
in 512 is (5+1+2)/3(number of digits) = 8/3=2).
The mean will always be an integer.
"""

def mean(n):
    c = 0
    s = 0
    while n > 0:
        s = s + n%10
        c = c + 1
        n = int(n/10)
    return int(s/c)

n = int(input("Enter Number "))
m =mean(n)
print("mean(",n,") ➞",m)