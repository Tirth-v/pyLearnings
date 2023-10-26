# when program completes its execution
# Garbage collector automatically calls destructor
# Garbage collector calls destructor for every objects
"""
When a program is about to end lets say there is an object and there is
a  reference for that object then first the refeence will be destroyed first
then that object will become orphan object.

as soon as an object becomes orphan garbage collector comes in action
garbage collector will call the destructor of that orphan object
destructor will de allocate the memory of that object and clean that memory.

"""


class Delta:
    def __init__(self,param):
        self.param = param
        print("This is constructor = ", self.param)

    def __del__(self):
        print("Destructor : ",self.param)


print("Process starts")
obj1 = Delta("obj1")
obj2 = Delta("obj2")
Delta("obj") # Anonymous objects
del obj1
del obj2

print("Process ends")
"""
If 'del' is used it will delete the reference
'del' will only delete references not the objects
If all references are destroyed then the garbage collector 
takes orphan objects and calls the destructor for de allocation objects.
"""

# Anonymous objects :

"""
    - When no reference is present then object becomes anonymous object.
    - Anonymous object gets destroyed just after the statement of its creation.
""