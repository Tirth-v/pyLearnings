# Find sum and average of list in python :

# Approach 1 : Iterating over the list

"""
def sum_avg(lst):
    count = 0
    for i in lst:
        count += i
    avg = count/len(lst)
    print("The sum of elements :", count)
    print("The average of elements :", avg)


lst = []
n = int(input("Enter the number of elements :"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("The list you have entered is :",lst)

sum_avg(lst)
"""

# Approach 2 : Using sum() method

"""
def sum_avg(lst):
    count = sum(lst)
    avg = count/len(lst)
    print("The sum of elements :", count)
    print("The average of elements :", avg)

lst = []
n = int(input("Enter the number of elements :"))
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print("The list you have entered is :",lst)

sum_avg(lst)
"""

# Approach 3 : Using recursion
'''
       - Define a recursive function sum_avg_list with parameters lst
         and n that takes a list and its length as input.
       - If the length n of the list is 0, return (0, 0) to 
         indicate that the sum and average of the list is 0.
       - If n is not 0, call the sum_avg_list function recursively
         with lst and n-1 as inputs. This will calculate the sum and average
         of the elements from 0 to n-1 in the list.
       - Store the result of the recursive call in the variables sum and avg.
       - Add the n-1th element of the list to the sum.
       - Increment the avg by 1.
       - Return the sum and avg.
       - Define another function avg_list that takes a list as input and
         calls the sum_avg_list function to calculate the sum and average.
       - Store the result of the sum_avg_list function in variables sum and avg.
       - Divide sum by avg and return the result as the average of the list.
       - Call the avg_list function with two example lists and print the results.
       - The program outputs the sum and average of the two lists.


def sum_avg(lst,n):
    if n == 0:
        return (0,0)
    else:
        sum, avg = sum_avg(lst, n-1)
        return (sum + lst[n-1], avg + 1)


def avg_lst(lst):
    sum, avg = sum_avg(lst,len(lst))
    return sum/avg


lst = []
inp = int(input("Enter the number of elements :"))
for i in range(0,inp):
    ele = int(input())
    lst.append(ele)
print("The list you have entered is :",lst)

print("Sum of the elements of list :", sum_avg(lst,len(lst))[0])
print("Average of the elements of list :", avg_lst(lst))
'''