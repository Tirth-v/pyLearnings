# Given a list in Python and provided the positions of the elements,
# write a program to swap the two elements in the list.


# Approach 1 : (Swapping positions)

"""
def swap_list(lst,pos1,pos2):

    lst[pos1],lst[pos2] = lst[pos2], lst[pos1]
    return lst


n = int(input("Enter the number of elements"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("The list that you have entered :",lst)
print("Now Enter the positions that you want to interchange!")
pos1 = int(input("Enter the first position :"))
pos2 = int(input("Enter the second position :"))

print(swap_list(lst,pos1,pos2))
"""

# Approach 2 : (Using pop method)

"""
def swap_lst(lst,pos1,pos2):
    if pos1 < pos2:
        first_ele  = lst.pop(pos1)
        second_ele = lst.pop(pos2 - 1)

        lst.insert(pos1, second_ele)
        lst.insert(pos2, first_ele)
    else :
        first_ele = lst.pop(pos1)
        second_ele = lst.pop(pos2)

        lst.insert(pos1, second_ele)
        lst.insert(pos2, first_ele)
    return lst





n = int(input("Enter the number of elements :"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(f"The list that you have entered is :{lst}\n Now enter the positions that you want to interchange!")
pos1 = int(input("Enter the first position :"))
pos2 = int(input("Enter the second position :"))

print(f"The list after swapping the positions :",swap_lst(lst,pos1,pos2))

"""

# Approach 3 : (Unpack collection)
"""
def swap_pos(lst,pos1,pos2):
    get = lst[pos1], lst[pos2]
    lst[pos1],lst[pos2] = get

    return lst

n = int(input("Enter the number of elements :"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(f"The list that you have entered is :{lst}\n Now enter the positions that you want to interchange!")
pos1 = int(input("Enter the first position :"))
pos2 = int(input("Enter the second position :"))

print(f"The list after swapping the positions :",swap_pos(lst,pos1,pos2))
"""

# Approach 4 : (Using temp variable)
"""
def swap_pos(lst,pos1,pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp
    return lst

n = int(input("Enter the number of elements :"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(f"The list that you have entered is :{lst}\n Now enter the positions that you want to interchange!")
pos1 = int(input("Enter the first position :"))
pos2 = int(input("Enter the second position :"))

print(f"The list after swapping the positions :",swap_pos(lst,pos1,pos2))
"""

