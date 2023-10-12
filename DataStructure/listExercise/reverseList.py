# Approach 1 : Reverse list by swapping present and last numbers at a time :


def reverse_lst(lst,size):

    if size == 1:
        return lst
    elif size == 2:
        lst[0],lst[1] = lst[1],lst[0]
        return lst
    else:
        for i in range(0,size//2):
            lst[i],lst[size-i-1] = lst[size-i-1],lst[i]

            if ((i != i+1 and size-i-1 != size-i-2) and (i != size-i-2 and size-i-1 != i+1)):
                lst[i+1],lst[size-i-2] = lst[size-i-2],lst[i+1]
                i = i + 2
            return lst


n = int(input("Enter the number of element :"))
lst = []
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
size = len(lst)
print("The list that you have entered :",lst)
print("The reversed list :",reverse_lst(lst,size))