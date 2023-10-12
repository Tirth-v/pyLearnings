# Variables :

"""
    Value can vary (Variables)
    Variables are like containers which stores some values.
    In python we don't need to declaire variables.
    And no need to spacify it's datatypes.
    

    eg.    name = input("What is your name?")
           print(name)

    len() function :
        - len() is used to check the length of the variable.

        eg.   length = len(name)
              print(length) 
    input() function :

        * By default input function returns string.
        - Input function is used to assign a user input.   

"""

# Rules for declaring variables :

"""
    - Must be meanigful name. (eg. for variable that stores age should be named meaningful like ageUser,ageAdmin...)
    - Must start with a letter or underscore.
    - Can not start with number.
    - Can only contain alpha-numeric characters and underscore.(a-z,A-Z,0-9,_)
    - Case sensitive(a is different then A)

"""

# Multi word variable names :

"""
    - Variable names with more than single word are difficult to read.
    
    => Techniques to make variable name more readable :
        -> Camel Case : myVariableName = "Hey"
        -> Pascal Case : MyVariableName = "Hello"
        -> Snake Case : my_variable_name = "Hii"
"""

# Assigning a single value to multiple variables : 

"""
        eg.
            a = b = c = 10
            print({a},{b},{c})

            a,b,c = 10,20,30
            print({a},{b},{c})

"""

# Overriding variable :

"""
    - Two same variable will be override.

    => Unpack collection :
        - If you have a collection of values in a list, tuple etc.
          Python allows you to extract the values into variables.
          This is called unpacking.

          cars = ["mustang","charger","GT"]
          a,b,c = cars
          print({a},{b},{c})

"""

# Two types of variables 

"""
    1. Global variables : 
        - Global variables are defined and declaired outside the function
          and we need to use them inside a function.

          eg. def func():
                print(a)

              
              s = "This is a global scope" 
              func()

        => Global keyword :
            - Global keyword is a keyword that allows a user to 
              modify a variable outside of the current scope.
            - It is used to create global variables from non-global scope(inside function).
            - Global keyword is used inside a function only when
              we want to do assignments or when we want to change 
              a variable.
            - Global variable is not needed for printing and accessing.  

"""

# Rules of global keyword :

"""
    - If a variable is assigned a value anywhere within the
      function's body, It's assumed to be a local unless explicitly
      declared as global.
    - Variables that are only referenced inside a function are
      implicitly global.
    - There is no need to use global keyword outside a function.

    eg.
        a = 10

        def change():
        
            global a

            a = a + 10
            print("Value of a inside a function :", a)
        change()
        print("Value of a outside a function :", a)

"""