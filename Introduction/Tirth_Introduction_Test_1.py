"""
Write a python program to remove duplicate character from a string
input: sigMa789Python
output: [m]  sigMa789Python
output: [i]  sgMa789Python

"""


str1 = "sigMa789Python"
str2 = input("Enter the character that you want to remove :")
if str2 in str1:
    print("You have entered :",str2)

    str3 = str1.replace(str2,"")
    print(f"The new string :",str3)
else:
    print("The character you have entered is not in the string.")    
        

"""
write a python program for following requirements
input: A3G4B2
output: ADGKBD

"""

string1 = input("Enter the string :")
if string1.isalnum and string1.isupper:
    print("The string you have entered is :",string1)
    for i in string1:
        if i.isnumeric():
            x = chr((int(i)+65))
            string2 = string1.replace(i,x)
            print(string2)
else:
    print("Enter the string which contains alphanumeric and uppercase.")            
            
