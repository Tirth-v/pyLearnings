# Approach 1 : using sort() method
"""
lst = [10,45,-885,15]
print("The list you have entered is :")
lst.sort()
print("The largest element of the given list is",lst[-1])
"""

# Approach 2 : Using max() method
"""
lst1 = [10,20,30,40]
print(max(lst1))
"""

# Approach 3 : Using function :
"""
def max_ele(lst):
    largest = lst[0]

    for i in lst:
        if i > largest:
            largest = i

    return largest

list1 = [10,20,40,50]
print("The largest element is :",max_ele(list1))
"""

