
# getter() setter()
class Student:
    def __init__(self,name,rollno,age):
        self.name = name
        self._rollno = rollno
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age > 35:
            print("You have entered invalid age")
        else:
            self.__age = age

#     def __display(self):
#         print(f"Hi myself {self.name} I am {self.__age} years old.and my rollno is {self._rollno} from Student class.")
#
#     def display_private_data(self):
#         self.__display()
#
#
# class Branch(Student):
#     def show(self):
#         print(f"My roll no. is {self._rollno}")


s1 = Student("Ram",108,24)
print(s1.get_age())
print(s1.set_age(38))
