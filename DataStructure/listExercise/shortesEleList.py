# Program to find shortest element in the list

# Approach 1 : Using sort() method
"""
lst1 = [1,2,3,4,5]
lst1.sort()
print("Smallest element of the list is :",lst1[0])
"""

# Approach 2 : Using min() method
"""
lst1 = [1,2,3,5,0]
print(min(lst1))
"""

# Approach 3 : Comparing all elements

"""
l = [int(l) for l in input("List:").split(",")]
print("The list is", l)

min1 = l[0]
for i in range(0,len(l)):
    if l[i] < min1:
        min1 = l[i]
print(min1)
"""

# Approach 4 : Using recursion

def find_small(itr,ele,lst1):
    if itr == len(lst1):
        print("The smallest number in the list is",ele)
        return
    if lst1[itr]<ele:
        ele = lst1[itr]
    find_small(itr+1,ele,lst1)
    return

lis = [5,2,4,8,9]
ele = lis[0]
find_small(0,ele,lis)