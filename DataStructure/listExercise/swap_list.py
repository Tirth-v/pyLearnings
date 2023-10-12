# Python program to interchange first and last value in list :

#Approach 1:
"""def swap_list(lst):
    size = len(lst)

    temp = lst[0]
    lst[0] = lst[size - 1]
    lst[size - 1] = temp

    return lst


lst = []
n = int(input("Enter the number of elements :"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("The given list is :",lst)


print(f"The list after swaping :",swap_list(lst))
"""

#Approach 2: (swaping indexes)
"""
def swap_list(lst):
    lst[0],lst[-1] = lst[-1],lst[0]
    return lst


lst = []
n = int(input("Enter the number of elements :"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("Your list :",lst)


print(f"List after swapping numbers:",swap_list(lst))
"""

# Approach 3 : (Using unpack collection)

"""
def swap_list(lst):

    n = int(input("Enter the number of elements :"))
    for i in range(0,n):
        ele = int(input())
        lst.append(ele)
    print("Your list :",lst)

    get = lst[-1],lst[0]
    lst[0],lst[-1] = get

    return lst


lst = []
print(swap_list(lst))
"""

# Approach 4 : Using * operator

"""
def swap_list(lst):

    start,*middle,end = lst
    lst = [end,*middle,start]

    return lst
lst =[]
n = int(input("Enter the number of elements :"))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)

print(swap_list(lst))
"""

# Approach 4 : (Using pop method)

"""
def swap_list(lst):
    first = lst.pop(0)
    last = lst.pop(-1)

    lst.insert(0, last)
    lst.append(first)

    return lst

lst = []
n = int(input("Enter the number of elements:"))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("The list that you have entered :",lst)

print(f"The list after swapping",swap_list(lst))
"""
# Approach 5: (Using slicing)


def swap_list(lst):
    if len(lst) >= 2:
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst


n = int(input("Enter the number of elements:"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("The list that you have entered :",lst)

print(f"The list after swapping",swap_list(lst))



