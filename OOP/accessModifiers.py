
# public specifier
class Student:
    def __init__(self ,name):
        self.name = name

    def display(self):
        print(self.name)

# we are using methods and attributes outside the class
# by default methods and attributes are public
s1 = Student("Tirth")
print(s1.name)
s1.display()

# protected specifier denoted by _variable(underscore before name of variable or method of function)
"""
     IN PYTHON STILL WE CAN ACCESS THE PROTECTED SPECIFIER OUTSIDE THE
     SCOPE OF CLASS AND THERE IS NO SUCH FUNCTIONALITY IN PYTHON 
     THAT PROVIDES ANY SPECIAL TREATMENT TO THE ATTRIBUTES AND FUNCTIONS
     STARTING WITH UNDERSCORE, ITS JUST FOR THE CONVENTION SO THAT WE CAN 
     DIFFERENTIATE THAT THE ATTRIBUTE OR METHOD IS PUBLIC PRIVATE OR PROTECTED.
"""


class Teacher:
    def __init__(self):
        self._name = "Tirth"


a = Teacher()
print(a._name)

# private specifier

class Employee:
    def __init__(self):
        self.__name = "Tirth"

a = Employee()
# print(a.__name) we cant access directly but,

# Can be accessed indirectly by name mangling
"""
Name mangling in python :
    - Name mangling in Python is a technique used to protect class-private and
      superclass-private attributes from being accidently overwritten by subclasses.
      Names of class-private and superclass-private attributes are transformed by the 
      addition of single leading underscore and a double leading underscore respectively.  
"""
print(a._Employee__name)

