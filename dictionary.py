# Dictionary :

"""
        - Dictionary are used to store values in key:value pairs.
        - Key-value is provided in the dictionary to make it more optimized.
        - Key in a dictionary don't allow polymorphism.
        - In python, a dictionary can be created by placing a sequence
          of elements within curly {} braces, separated by 'comma'.
        - Dictionary hold pairs of values, one being the key and the other corresponding
          pair element being its key:value.
        - Values in a dictionary can be of any data type and cant be
          duplicated, whereas keys cant be repeated and must be immutable.
        - Dictionary keys are case-sensitive, the same name but different cases
          of key will be treated distinctly.
"""

dict1 = {"name":"Kaushal","city":"Ahmedabad"}
print(dict1)

# empty dictionary :
dict2 = {}

# creating dictionary by dict() method :

Dict = dict({"abc":"xyz"})

# creating dictionary with each item as a pair
Dict = dict([("key","value"),("key2","value2")])
print(Dict)

# Nested dictionary :

Dict = {"Name":"Ramkrishna","Address":"kolkata",
        "phone":{"home":12345,
                 "office":213235}
        }
print(Dict)

# Adding elements to dictionary :
"""
    - One value at a time can be added to a dictionary by defining
      value along with the key Dict[key]='value'.
    - Updating an existing value in a dictionary can be done by using the built-in
      update() method.
    - Nested key values can also be added to an existing dictionary.
        
"""
# Adding elements one at a time :

Dict = {}
Dict["key"] = "value"
Dict["City"] = "Bhavnagar"
Dict["Contact"] = 9897855621
print(Dict)

# Adding set of value to a single key

Dict["Contact"] = 1213,32215,4546
print(Dict)

# Updating existing key's value :

Dict = {"name":"ramkrishna",
        "city":"kolkata",
        "mobile":548443545}
# updating existing key's value

Dict["name"] = "Swami ramkrishna paramhans"
print(Dict)

# Adding nested key to dictionary :

Dict = {"name":"ramkrishna",
        "city":"kolkata",
        "mobile":548443545}
Dict["phone"] = {"home":36460,"office":35343}

print(Dict)

# Access elements from dictionary :

print(Dict["city"])

# There is method called .get() which will also help in accessing
# the element from a dictionary.

print(Dict.get("mobile"))

# In order to access the value of any key in the nested dictionary, use indexing[] syntax.

print(Dict["phone"]["home"])

# Removing elements from dictionary :

# Using del keyword :
del dict1["city"]
print(dict1)

# Note : The del Dict will delete the entire dictionary
#        and hence printing it after deletion will raise an error.

# pop() method : pop is used to delete and return the value of the key specified.

print(dict1.pop("name"))

# popitem() :
"""
        -The popitem() return and removes an arbitrary element(key,value)
         pair from the dictionary.
"""

# clear() :
"""
        - All the items from dictionary can be deleted at once by using 
          clear() method.
"""

Dict.clear()
print(Dict)

Dict = {"name":"ramkrishna",
        "city":"kolkata",
        "mobile":548443545}

# copy() :
#        return a copy of the dictionary

x = Dict.copy()
print(x)

# fromkeys() : Return a dictionary with the specified keys and value.

x =('key1','key2','key3')
y = 0
dict3 = dict.fromkeys(x,y)
print(dict3)

# get () : return the value of the specified key.

Dict = {"name":"ramkrishna",
        "city":"kolkata",
        "mobile":548443545}

x = Dict.get("city")
print("city")

# items() : Return the list containing a tuple for each key value pair.

x = Dict.items()
print(x)

# keys : Return a list containing the dictionary's keys

print(Dict.keys())

# setdefault() : Return the value of the specified key. if the key does
#                not exist: insert the key, with the specified value.

x = Dict.setdefault("state","guj")
print(x)

# values() : Return a list of all values in the dictionary.

print(Dict.values())




