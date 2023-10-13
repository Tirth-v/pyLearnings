from functools import reduce

# filter :
def is_even(n):
    return n % 2 == 0


nums = [22,8,9,7,5,12,56,89,85,67,19,38,65,16,37,16]

evens = list(filter(is_even,nums))

print(evens)

# We can use lambda in above example :

nums = [22,8,9,7,5,12,56,89,85,67,19,38,65,16,37,16]

evens = list(filter(lambda n : n%2 == 0, nums))
print(evens)

# map :

nums = [22,8,9,7,5,12,56,89,85,67,19,38,65,16,37,16]

evens = list(filter(lambda n : n%2 == 0, nums))

doubles = list(map(lambda n : n*2, evens))
print(doubles)

# reduce :


nums = [22,8,9,7,5,12,56,89,85,67,19,38,65,16,37,16]

evens = list(filter(lambda n : n%2 == 0, nums))

doubles = list(map(lambda n : n*2, evens))

sum = reduce(lambda a,b : a+b, doubles)

print(sum)

