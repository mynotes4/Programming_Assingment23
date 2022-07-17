"""
Question 1
Create a function that takes a number as an argument and returns True or False depending on
whether the number is symmetrical or not. A number is symmetrical when it is the same as its
reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True
"""

def is_symmetrical(s):
    n = len(s)
    for i in range(int(n/2)):
        if s[i] != s[n-1-i]:
            return False
    return True

s = input("Enter word ")
print("is_symmetrical(",s,") ➞",is_symmetrical(s))