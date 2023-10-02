# Conditional statements :
"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

"""

# if statement is written by using the if keyword.

"""
        Indentation is required.
        eg.
            height = int(input("Enter your height:"))

            if height>3:
                print("Buy token")

            print("Out of if block")

"""

# if else

"""
        eg.
            height = int(input("Enter your height:"))

            if height>3:
                print("Buy token")
            else:
                print("No need to buy token")


"""

number = int(input("Enter a number :"))
if number % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")  


# Nested if else & elif

height = float(input("Enter your height in feet:"))
if height > 3:
    print("You can ride!")
    age = int(input("Enter your age :"))
    if age <= 18:
        print("Pay 25 rupees")
    else:
        print("Pay 50 rupees")
else:
    print("You are not eligible for the ride.")


# if elif

number2 = int(input("Enter the number between 1 to 3"))
if number2 == 1:
    print("one")
elif number2 == 2:
    print("two")
elif number2 == 3:
    print("three")
else:
    print("Number out of range.")          