
# __len__
# class Employee:
#     name = "Tirth"
#
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i + 1
#         return i
#
# e = Employee()
# print(e.name)
# # print(len(e))# It will show error object of type employee has no len()
# print(len(e))

# __dict__
# class Martian:
#     """Someone who lives on universe."""
#
#     def __init__(self,fn,ln):
#         self.first_name = fn
#         self.last_name = ln
#
# m1 = Martian("Swami","Vivekanand")
# m1.arrival_date = "2029-12-16"
# print(m1.__dict__)

# class Martian:
#     """Someone who lives on universe."""
#
#     def __init__(self,fn,ln):
#         self.first_name = fn
#         self.last_name = ln
#
#     def __setattr__(self, key, value):
#         print(f"You set {key} = {value}")
#         self.__dict__[key] = value
#
# m1 = Martian("Swami","Vivekanand")
# print(m1.__dict__)


# __setattr__ __getattr__

# class Martian:
#     """Someone who lives on universe."""
#
#     def __init__(self,fn,ln):
#         self.first_name = fn
#         self.last_name = ln
#
#     def __setattr__(self, key, value):
#         print(f"You set {key} = {value}")
#         self.__dict__[key] = value
#
#     def __getattr__(self, item):
#         print(f"Get the '{item}' attribute")
#
#
# m = Martian("Swami","Vivekanand")
# print(f"FIrst name = {m.first_name}")
# print(f"Last name = {m.last_name}")



# __str__
# class Martian:
#     """Someone who lives on universe."""
#
#     def __init__(self,fn,ln):
#         self.first_name = fn
#         self.last_name = ln
#
#     def __setattr__(self, key, value):
#         print(f"You set {key} = {value}")
#         self.__dict__[key] = value
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#
# m = Martian("Swami","Vivekanand")
# print(m)



# __repr__
# class Martian:
#     """Someone who lives on universe."""
#
#     def __init__(self,fn,ln):
#         self.first_name = fn
#         self.last_name = ln
#
#     def __repr__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f"{self.first_name} "
#
#
# m = Martian("Swami","Vivekanand")
# print(m)


# __mul__
# class Martian:
#     """Someone who lives on universe."""
#
#     def __init__(self,fn,ln):
#         self.first_name = fn
#         self.last_name = ln
#
#     def __repr__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f"{self.first_name} "
#
#     def __mul__(self, x):
#         if type(x) is not int:
#             raise Exception("Invalid argument, must be int")
#
#         self.first_name = self.first_name * x
#
#
#
# m = Martian("Swami","Vivekanand")
# print(m)
#
# p = Martian("hello","world")
# p * 4
# print(p)
#
# __call__
#
# class Call:
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, y):
#         print("Called this function :",y)
#
# p = Call("Hello")
# p(5)

# __del__

# class MyClass:
#     def __init__(self,name):
#         self.name = name
#
#     def __del__(self):
#         print(f"Deleting {self.name} object")
#
# obj1 = MyClass("First object")
# obj2 = MyClass("Second object")
#
# del obj1
