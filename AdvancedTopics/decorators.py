# Decorators :

"""
    - Decorators are one of the most helpful and powerful tools of python.
    - These are used to modify the behaviour of the function.
    - Decorators provide the flexibility to wrap another function to expand
      the working of wrapped function, without permanently modifying it.
    - In decorators, functions are passed as an argument into another function and
      then called inside the wrapper function.
    - It is also called meta programming where a part of the program attempts to
      change another part of programming at compile time.
"""


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

# Example 2 :

def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


# Example 3 : Decorator chaining :

# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())