def multiplyList(lst):
    result = 1
    for i in lst:
        result *= i
    return result


lst1 = [1,2,3]
print(multiplyList(lst1))