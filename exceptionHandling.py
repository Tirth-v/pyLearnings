# Python error and exception handling :

"""
        - Errors are the problems in a program due to which the program
          will stop executing.
        - On the other hand, exceptions are raised when some internal events occur
          which changes the normal flow of the program.

        => Two types :
                - Syntax errors
                - Logical errors(exceptions)

            => Syntax error :
                - When the proper syntax of the language is not followed
                 then a syntax error is thrown.

                 if (10<20)
                 SyntaxError: invalid syntax

                - It returns a syntax error message because after the is statement
                  a colon : is missing, we can fix this by writing the correct syntax.

            => Logical error :
                - When in the runtime an error that occurs after passing
                  the syntax test is called exception or logical type.
                    e.g.
                        a = 100/0
                        Traceback (most recent call last):
                            a = 100/0
                        ZeroDivisionError: division by zero
                - In the above example raised the ZeroDivisionError
                  as we are trying to divide a number by 0.
                - Note:Exception is the base class for all exceptions in python.
                - Some of the common built-in exceptions :

                       - ArithmeticError:    Raised when an error occurs in numeric calculations
                       - AssertionError:     Raised when an assert statement fails
                       - AttributeError:     Raised when attribute reference or assignment fails
                       - Exception:          Base class for all exceptions
                       - EOFError:           Raised when the input() method hits an "end of file" condition (EOF)
                       - FloatingPointError: Raised when a floating point calculation fails
                       - GeneratorExit:      Raised when a generator is closed (with the close() method)
                       - ImportError:        Raised when an imported module does not exist
                       - IndentationError:   Raised when indentation is not correct
                       - IndexError:         Raised when an index of a sequence does not exist
                       - KeyError:           Raised when a key does not exist in a dictionary
                       - KeyboardInterrupt:  Raised when the user presses Ctrl+c, Ctrl+z or Delete
                       - LookupError:        Raised when errors raised cant be found
                       - MemoryError:        Raised when a program runs out of memory
                       - NameError:          Raised when a variable does not exist
                       - NotImplementedError:Raised when an abstract method requires an inherited class to override the method
                       - OSError:            Raised when a system related operation causes an error
                       - OverflowError:      Raised when the result of a numeric calculation is too large
                       - ReferenceError:     Raised when a weak reference object does not exist
                       - RuntimeError:       Raised when an error occurs that do not belong to any specific exceptions
                       - StopIteration:      Raised when the next() method of an iterator has no further values
                       - SyntaxError:        Raised when a syntax error occurs
                       - TabError:           Raised when indentation consists of tabs or spaces
                       - SystemError:        Raised when a system error occurs
                       - SystemExit:         Raised when the sys.exit() function is called
                       - TypeError:          Raised when two different types are combined
                       - UnboundLocalError:  Raised when a local variable is referenced before assignment
                       - UnicodeError:       Raised when a unicode problem occurs
                       - UnicodeEncodeError: Raised when a unicode encoding problem occurs
                       - UnicodeDecodeError: Raised when a unicode decoding problem occurs
                       - UnicodeTranslateError:	Raised when a unicode translation problem occurs
                       - ValueError:         Raised when there is a wrong value in a specified data type
                       - ZeroDivisionError:  Raised when the second operator in a division is zero


"""

# Exceptions :
"""
        - Exceptions are raised when the program is syntactically correct, but 
          the code resulted in an error.
        - This error does not stop the exception of the program, however, it 
          changes the normal flow of the program.  
"""

# Try and except statement-catching exception :

"""
        - Try and except statements are used to catch and handle exceptions in
          python.
        - Statements that can raise exception are kept inside the try clause and 
          the statements that handle the exception are written inside except clause.   
                e.g.
                     try :
                            print("second element = %d" %(a[1]))
                            
                            throws error since there are only 3
                            element in array.
                            
                            print("Fourth element = %d" %(a[3]))
                     except :
                            print("An error occured")
                      
                     >> Second element = 2
                        An error occured
                        
        - In the above example, the statement that can cause the error are
          placed inside the try statement(second print statement in our case).
          The second print statement tries to access the fourth element of the 
          list which is not there and this throws an exception. This exception
          is then caught by the except statement.                                     
"""

# Catching specific exception :
"""
        - A try statement can have more than one except clause, to specify
          handlers for different exceptions.
        - One handler will be executed.
        - For example, we can add IndexError on the above code. The genral
          syntax for adding specific exception are :
          
                try :
                    statement
                except IndexError :
                    statement
                except ValueError :
                    statement  
"""

# Example :


def fun(a):
    if a < 4:
        # Throws ZeroDivisionError for a = 3
        b = a/(a-3)
    # throws NameError if a >= 4
    print("Value of b :", b)


try:
    fun(3)
    fun(5)
#Braces are necessary for multiple exceptions.
except ZeroDivisionError :
    print("ZeroDivisionError occurred and handled")
except NameError :
    print("NameError occurred and handled")

# Try with else :
"""
        - We can also use the else clause on the try-except block
          which must be present after all the except clauses.
        - The code enters the else block only if the try clause does not
          raise an exception.
"""


def my_func(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b results in 0")
    else:
        print(0)


my_func(3.0, 3.0)
my_func(2.0, 3.0)


# Finally keyword :
"""
        - Python provides a keyword finaly, which is always executed after the
          try and except blocks.
        - The final block always executes after normal termination of the try
          block terminates due to some exception.
"""

try:
    k = 5//0
    print(k)
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("This is always executed.")


# Raising Exception :
"""
        - The raise statement allows the programmer to force a specific exception
          to occur.
        - The argument in raise indicates the exception to be raised.
        - This must be either an exception instance or an exception class
          (a class that derives from Exception).
"""

try:
    # Raise error
    raise NameError("Hi there")
except NameError:
    print("An Exception")
    raise # To determine whether theexception was raised or not.from


# Assert keyword :
"""
        - Assertions in any programming language are the debugging tools that 
          help in the smooth flow of code.
        - Assertions are mainly assumptions that a programmer knows or
          always wants to be true and hence puts them in code, so that
          failure of these doesnt allow the code to execute.
        - In similar terms, we can say that assertion is the boolean expression
          that checks if the statement is True or False.
        - If the statements is true then it does nothing and continues the 
          execution, but if the statement is False then it stops the execution of
          the program and throws an error.
"""


d = "hello"

# if condition returns True, then nothing happens:
assert d == "hello"

# if condition returns False, AssertionError is raised:
assert d == "bye"

