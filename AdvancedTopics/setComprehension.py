

def user_input():
    lst = []
    n = int(input("Enter the number of elements :"))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    return lst
def com_set(lst):
    set_using_comp = {var for var in lst if var % 2 == 0}
    print("Output using set comprehension:", set_using_comp)

l = user_input()
com_set(l)


