# Duck typing
# Method overloading
# Method overriding
# Operator overloading

# Duck typing :

#
# class Duck:
#     def swim(self):
#         print("I am duck and I can swim")
#     def speaks(self):
#         print("Quack quack")
#
# class Dog:
#     def swim(self):
#         print("I am a dog and I can swim")
#     def speaks(self):
#         print("Bhau bhau")
#
# def dislpay(duck):
#     duck.swim()
#     duck.speaks()
#     print("Information displayed")
#
# d = Duck()
# d1 = Dog()
# dislpay(d)
# dislpay(d1)
#
# """
#     - In duck typing the class or the object dont matter
#       what matter is the methods the attributes it defines
#       we have created functions which takes an object as
#       argument and then that function calls the methods of the
#       argument which methods exists in the class so that funtion
#       will display the methods of class accordingly.
# """


# Operator overloading :

# Plus overloaded addition to concatenation according to type of variable
# print(1+2)
# print("1"+"2")
# print(int.__add__(1,2))
# print(str.__add__("1","2"))

# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
#
#     def __add__(self, other):
#         return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
#
#
# c1 = ComplexNumber(1,2)
# c2 = ComplexNumber(4,5)
# print(c1+c2)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __gt__(self,other):
#         if self.age > other.age:
#             return True
#         else:
#             return False
# p1 = Person("Ram",24)
# p2 = Person("Shyam",28)
# if p1 > p2:
#     print(f"{p1.name} Will Pay The Bill")
# else:
#     print(f"{p2.name} Will Pay The Bill")


# Method Overloading : python doesn't support method overloading

# class Demo:
#     def add(self, *args):
#         total = 0
#         for i in args:
#             total = total + i
#         return total
#
# d = Demo()
# print(d.add(2,3))
# print(d.add(1,2,3))           runtime polymorphism
# print(d.add(1,2,3,4,5,7,8,3))
#

# Method overriding : compile time polymorphism
# It occurs in inheritance

# class Father:
#     def sleep(self):
#         print("sleeps from 10am to 5am")
#     def eat(self):
#         print("Eating")
#
# class Son(Father):
#     def sleep(self):
#         print("2am to 10 am")
#         super().sleep()
# ram = Son()
# ram.sleep()
#

"""
In method overloading method must have same name but different parameters
In method overriding method must have same name and same number of parameters they
differ location one method in parent class and one method i child class.
"""
