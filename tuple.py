# Tuple :

"""
     - A tuple is a collection of python objects separated by commas.
     - In someways tuple is similar to a list in terms of indexing,
       nested objects and repetition but a tuple is immutable unlike lists
       which are mutable.
     - Tuple items are ordered, unchangeable, and allow duplicate values.
     - Tuple items are indexed, the first index [0],...

     => Unchangeable :
            - Tuples are unchangeable that means we cannot change, add, or remove
              items after the tuple has created.
"""

# Access tuple :

tuple1 = (1,2,3,4,5)
print(tuple1)
print(tuple1[2])

# Negative indexing :

print(tuple1[-2])


# Update tuple

"""
    - Convert tuple to list and make changes that we need and then convert that
      list into tuple again. 
"""

tuple_to_list = list(tuple1)
print(tuple_to_list)

tuple_to_list.insert(2,"hello")
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)

# Tuple methods :


# Count() :
"""Return the number of elements with the specified value
   occurs in tuple."""

print(tuple1.count(2))

# index() :
"""Search the tuple for specified value and return the
   position of where it was found."""

print(tuple1.index(4))

# Delete tuple : You can delete tuple completely.

del tuple1
print(tuple1)

"""
Difference between list and tuple

            list                              tuple
    - Lists are mutable              - Tuples are immutable
    - Implication of iterations      - The implication of iteration is 
      is time consuming                comparatively faster.
    - The list is better for         - Tuple datatype is appropriate
      performing operations,           for accessing the elements.
      such as, insertion and
      deletion. 
    - Lists consume more memory.     - Tuple consume less memory as 
                                       compare to list.                                   
      
"""
