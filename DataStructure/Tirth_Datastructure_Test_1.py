# Question 1 : Write a Python program to get the week number.

import datetime


def week_number():
    try:
        day = int(input("Enter the day :"))
        month = int(input("Enter the month :"))
        year = int(input("Enter the year :"))
        week = datetime.date(year,month,day).isocalendar()[1]
        print("The week of the date that you have entered is :")
        return week
    except ValueError:
        print("Enter valid date")


print(week_number())


# Question 2 : Write a Python program to split a list every Nth element.


def split_list():
    if n <= len(lst):
        for i in range(n):
            lst1.append(lst[i::n])
        print(lst1)
    else:
        print("You have entered range out of index")

while True:
    try:
        l = int(input("Enter the number of elements :"))
        break
    except ValueError:
        print("Enter valid number of elements")
lst = []
for i in range(0,l):
    ele = input()
    lst.append(ele)
print("The list that you have entered is :",lst)
while True:
    try:
        n = int(input("Enter the value of n :"))
        break
    except ValueError:
        print("Enter valid value of n")
lst1 = []

split_list()
