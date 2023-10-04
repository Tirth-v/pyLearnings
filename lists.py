# Python list :

"""
    - List is a data structure which comes under sequence datatype
    - List need not tobe homogeneous
    - Single list may contain datatypes like Integers, Strings as well as objects.
    - List are mutable, so we can update them after the creation.
    - List in python are ordered, and have definite count.
    - The elements in list are indexed according to a definite sequence
      and the indexing of a list is done with 0 being the first index.
    - Each element in the list has its definite place in the list, which allows
      duplicating of elements in the list, with each element having its own
      distinct place and credibility.
"""

# Creating a list :
list1 = [1, 2, 3]
print(list1)

# Creating a list of numbers and strings :

list2 = [1, 2, 3, "hello"]
print(list2)

# Check length of list :

print(len(list1))

# Accessing elements from the list :

l1 = [1, 2, 3, 4]
print(l1[2])

# Accessing element from the nested list :

l1 = [1, 2, 3, 4, ["hey", "hello", (1, 2, 3, {"key": "value", "key2": "val"})]]
print(l1[4][2][3])


# Negative index :

l2 = [1,2,3,4,5,5]
print(l2[-3])

# Slicing of a list : slicing in list is same as slicing in string

print(l2[:3])
print(l2[1:3])
print(l2[2:]),print(l2[2::]),print(l2[-3:])

# Adding elements to a list :

# append() : adds element at the end one at once, takes one argument.

l2.append(6)
print(l2)

# using for loop :

for i in range(1,4):
    l2.append(i)

print(l2)

# Insert method : adds element at the desired position, takes two args(pos,val).

l2.insert(3,5)
print(l2)

print(l2)

# extend() : adds multiple elements and at the end.

l2.extend([8,"hello"])
print(l2)

# Removing element from list :

# remove() :

"""
    Remove() method only removes one element at a
    time, to remove a range of elements, the iterator is used.
    The remove() method removes the specified item.
    Remove method in list only removes the fist occurrence of the searched element.
 
"""

l2.remove(5)
print(l2)

for i in range(1,3):
    l2.remove(i)

print(l2)


# using pop() method :

"""
        pop() function can also be used to remove and
        return an elements from the list,
        but by default it removes only the last element of
        the list,
        to remove an element from a specific position of the list
        the index of the element is passes as an argument
        to the pop() method.
"""

l2.pop(3)
print(l2)
print(l2.pop(6))



# Methods :

"""
    1. append() : Add an element to the end of the list
    2. clear() : Removes all items from the list
    3. copy() : Returns a copy of the list
    4. count() : Returns the count of the number of items passed as
                 an argument
    5. extend() : Add all elements of a list to another list
    6. index() : Returns the index of the first matched item
    7. insert() : Insert an item at the defined index
    8. pop() : Removes and returns an element at the given index
    9. remove() : Removes an item from the list
    10. reverse() : Reverse the order of items in the list
    11. sort() : Sort items in a list in ascending order
"""





