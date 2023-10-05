# Set :
"""
    - Set is an unordered collection datatype that is iterable,
      mutable and has no duplicate elements.
    - We cannot access items using indexes like we do in lists and tuples.
    - Set items can appear in a different order everytime you use them,
      and cannot be referred by index or key.
    - Once a set is created, you cannot change its items, but you can remove
      items and add new items.
    - Sets cannot have two items with the same value.
"""

set1 = {"a",1,"d",4,8,14}
print(set1)

# no duplicates
set2 = {1,1,2,2,3,3,5,5,6,9}
print(set2)

# Methods :

# Adding element :
"""
    - Insertion in set is done through set.add() function.
"""

city = {"Bhavnagar","Vadodara","Ahmedabad"}
city.add("Gandhinagar")
print(city)

# Union :
"""
    - Two sets can be merged using union() function or | operator.
"""
company = {"Volvo","Mercedes","Ford"}
model = {"S90","Benz","Mustang"}
company_model = company.union(model)
company_model1 = company_model | set1
print(company_model)
print(company_model1)


# Intersection :
"""
    Common elements between two sets are selected.
    1. intersection()
    2. operator &
"""

set_one = {"a","b","1",2,3,4}
set_two = {"a","e",1,4,6,7,8}

set3 = set_one.intersection(set_two)
set_3 = set_one & set_two
print(set3)
print(set_3)

# Difference :

"""
    - To find difference in between sets.
      1. difference()
      2. - operator
"""

set_one = {"a","b","1",2,3,4}
set_two = {"a","e",1,4,6,7,8}

set3 = set_one.difference(set_two)
set_3 = set_one - set_two

print(set3)
print(set_3)


# Clear : Empties the whole set.

set_one = {"a","b","1",2,3,4}
set_one.clear()
print(set_one)


# Other Methods of set :

# 1. add() :
set_one = {"a","b","1",2,3,4}
set_one.add("hello")
print(set_one)

# 2. copy() :
set_one = {"a","b","1",2,3,4}
a = set_one.copy()
print(a)

# 3. difference_update() : Removes the items in this set that are also included in another, specified set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)

# 4. discard() : Removes the specified item

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# 5. intersection_update() :
"""
    - Removes the items in this set that are not present
      in other, specified set()
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# 6. isdisjoint() : Returns whether two sets have an intersection or not.

dif = set_one.isdisjoint(set_two)
print(dif)

# 7. issubset() :

subset = set_one.issubset(set_two)
print(subset)

# 8. issuperset() :

superset = set_one.issuperset(set_two)
print(superset)

# 9. pop() : Removes any single element at a time :

set_one.pop()
print(set_one)

# 10. remove() : Removes the specified element.

set_one.remove("a")
print(set_one)

# 11. symmetric_difference() : In Python, difference is the elements present in one set,
# but not on the other. Symmetric difference is the elements from both sets,
# that are not present on the other.

symmdiff = set_one.symmetric_difference(set_two)
print(symmdiff)

# 12. symmetric_difference_update() : Inserts the symmetric differences from this set and another.

s_d_u = set_one.symmetric_difference_update(set_two)
print(s_d_u)

# 13. update() : Update the set with the union of this set and others.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


