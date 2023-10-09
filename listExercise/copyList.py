# Approach 1 : Using slice operator
"""
def cloning(li1):
    li_copy = li1[:]
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
"""

# Approach 2 : Using extend method
"""
def cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
"""

# Approach 3 : Using assignment operator
"""
def cloning(li1):
    li_copy = li1
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
"""

# Approach 4 : Shallow copy
"""
import copy

li1 = [1, 2, [3, 5], 4] 
li2 = copy.copy(li1)
print(li2)
"""

# Approach 5 : Using list comprehension

""" 
def cloning(li1):
    li_copy = [i for i in li1]
    return li_copy

 
li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
"""

# Approach 6 : Using append method

"""
def cloning(li1):
    li_copy = []
    for item in li1: li_copy.append(item)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
"""