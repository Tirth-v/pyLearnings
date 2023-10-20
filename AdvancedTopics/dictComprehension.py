# {key_expression : value_expression for item in iterable}

numbers = [1,2,3,4]
square_dict = {x: x**2 for x in numbers}
even_square_dict = {x: x**2 for x in numbers if x % 2 == 0}
print(even_square_dict)
print(square_dict)


state = ['gujarat','rajasthan','maharashtra']
capital = ['gandhinagar','jaipur','mumbai']

dict_state = {f"state{key}" : f"capital{value}" for (key,value) in zip(state, capital)}
print(dict_state)

# Generator comprehension :

"""
Generator Comprehensions are very similar to list comprehensions. 
One difference between them is that generator comprehensions use circular 
brackets whereas list comprehensions use square brackets. The major difference 
between them is that generators don’t allocate memory for the whole list. 
Instead, they generate each value one by one which is why they are memory efficient.
"""

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)
print("Output values using generator comprehensions:", end=' ')
for var in output_gen:
    print(var, end=' ')