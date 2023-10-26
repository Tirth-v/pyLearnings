class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a , b) :
        return a + b

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(a.add(5,5))
print(Math.add(10,20))
# static methods are independent
# we can call them with object or class itself
# we dont need to pass slef argument in class method


