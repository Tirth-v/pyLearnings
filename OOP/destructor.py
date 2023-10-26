# For any class __del__() is the destructor by default in python
# It is a special method whenever object is destroyed it is called.
# For n objects destructor will execute n times
# Destructor is non-static method and self is compulsory parameter.
# return type should be non
# destructor may not have parameter except self.
# destructor cant be overload
# destructor is compulsory which will execute at last

class Delta:
    def __init__(self,param):
        self.param = param
        print("This is constructor = ", self.param)

    def __del__(self):
        print("Destructor")

print("Process start")
obj1 = Delta(10)
obj2 = Delta(20)
print("Process ends")