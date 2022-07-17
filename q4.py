"""
Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
"""

def setify(l):
    l = str_list(l)
    return list(sorted(set(l)))

def str_list(s):
    s = s.split(',')
    return [int(i) for i in s]

l = input("Enter comma seperated list of numbers\neg. 1,2,3 : ")
s = setify(l)
print("multiply_nums(", l, ") ➞",s )