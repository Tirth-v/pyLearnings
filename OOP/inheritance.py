# single

# class a:
#     def g1(self):
#         print("parent")
#
# class b(a):
#     def hello(self):
#         super().hello()
#         print("child")


# multi level

# class a:
#     def g1(self):
#         print("parent")
#
# class b(a):
#     def hello(self):
#         super().hello()
#         print("child")
#
# class c(b):
#     def hello(self):
#         print("grand child")


#multiple

# class a:
#     def g1(self):
#         print("parent1")
#
# class b:
#     def hello(self):
#         print("parent2")
#
# class c(a,b):
#     def c1(self):
#         print("child")
#
# c = c()
# c.hello()
# c.g1()

# heirarchical

# class a:
#     def g1(self):
#         print("parent1")
#
# class b(a):
#     def hello(self):
#         print("child1")
#
# class c(a):
#     def c1(self):
#         print("child2")
#
# class d(b):
#     def c1(self):
#         print("child of b")
# class e(b):
#     def c1(self):
#         print("child of b")
#
# class f(c):
#     def c1(self):
#         print("child of c")
#
# e = e()
# e.g1()



