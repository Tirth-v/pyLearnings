def myfunc():
    print("hello")


myfunc()


# function with arguments

def add(a, b):
    c = a + b
    print(f"Sum is {c}")


add(1, 5)
add(6, 10)


# Types of arguments :

# positional arguments :

def greet(name, dept):
    print(f"Hey {name}")
    print(f"You are from {dept} department.")


greet("hopper", "IT")

# keyword arguments :


def greet1(name, dept):
    print(f"Hey {name}")
    print(f"You are from {dept} department.")


greet1(dept="CS", name="Eleven")

# default arguments :


def default(subject, name="johnson"):
    print(f"Hello {name}", f"Do you teach {subject}?")


default("maths")

# Arbitrary arguments/ variable length arguments :

# arbitrary positional arguments


def sum1(*numbers):
    c = 0
    for i in numbers:
        c = c + i
    print(f"Sum is {c}")


sum1(5, 8, 9)


# *args and **kwargs

# **kwargs arbitrary keyword argument

def addition(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"Sum is {c}")


addition(1,2)
addition(5,10,50,60)
addition(-5,-59,86,54,4,8,7,3)


# Arbitrary keyword arguments :

def kwargs(*numbers,name):
    c = 0
    print(numbers)
    print(name)
    for i in numbers:
        c += i
        print(f"Sum is {c}")


kwargs(1,2,name="shiv")

# Convention : normal argument > arbitrary argument > arbitrary keyword argument









