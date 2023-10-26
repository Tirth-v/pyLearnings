class Person:
    def __init__(self,n,o):
        print("Hello")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Tirth","Developer")
b = Person("Hemil","Developer")
a.info()
b.info()

# Two types of constructors default and with parameter both as above

"""
    A CONSTRUCTOR IS A SPECIAL METHOD IN A CLASS USED 
    TO CREATE AND INITIALIZE AN OBJECT OF A CLASS.
    THERE ARE DIFFERENT TYPES OF CONSTRUCTORS.
    CONSTRUCTOR IS INVOKED AUTOMATICALLY WHEN AN OBJECT 
    OF A CLASS IS CREATED.
    A CONSTRUCTOR IS A UNIQUE FUNCTION THAT GETS CALLED 
    AUTOMATICALLY WHEN AN OBJECT IS CREATED OF A CLASS.
    THE MAIN PPURPOSE OF A CONSTRUCTOR IS TO INITIALIZE
    OR ASSIGN VALUES TO THE DATA MEMBERS OF THAT CLASS. IT CANNOT
    RETURN ANY VALUE OTHER THAN NONE.
"""