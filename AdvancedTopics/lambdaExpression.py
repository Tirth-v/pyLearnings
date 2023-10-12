print("""
******************************************************
                    Lambda()
******************************************************
""")

# syntax

# variable = lambda arg: expression


OddEven = lambda num: "even" if num % 2 == 0 else "odd"

a = OddEven(10)
print(a)

print("""
*********************************************
                Example - 2 
*********************************************
""")

# def Oddeven(*num):
#     even = []
#     odd = []

#     for i in num:
#         if i % 2 ==0:
#             even.append(i)
#         else:
#             odd.append(i)


#     return {"odd": odd, "even": even}


ShortOddEven = lambda num: {"odd": [i for i in num if i % 2 != 0], "even": [i for i in num if i % 2 == 0]}

a = [f"{i}-Even" if i % 2 == 0 else f"{i}-Odd" for i in range(10)]
print(a)

print(ShortOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print("""
*********************************************
                Example - 3
*********************************************
""")

# def OddEven(number):
#     if number % 2 == 0:
#         return f"{number} is even number."
#     else:
#         return f"{number} is odd number."


oddEven = lambda num: "even" if num % 2 == 0 else "odd"

a = lambda FunctionName, number: FunctionName(number)

print(a(oddEven, 10))

print("""
*********************************************
                Example - 4
*********************************************
""")

# Short Only


# def VowelChr(chr1):

#     if chr1 in ["a", "e", "i","o", "u"]:
#         return True
#     else:
#         return False


VowelChr1 = lambda v_chr: True if v_chr in ["a", "e", "i", "o", "u"] else False

Chr_List = [str(i).lower() for i in "adgshkuyegrubcjhsagodfugwabgfhagwefuybasljdcvfEYDFHWKJDCBUOYSgF"]

# print(a)

FilterVowel = list(filter(lambda v_chr: True if v_chr in ["a", "e", "i", "o", "u"] else False, Chr_List))

print(FilterVowel)


