# Loop is repeating same action again and again.

# for loop : for loop in python is more like an iterator
#            which is used to iterate over a sequence
#            and do some specific action on that sequence.

names = ["ram","krishna","lakshman","shiva"]
for name in names:
    print(name)
    if name == "krishna":
        print("Jay shree krishna")


str1 = "ramkrishnaparamhans"
for alphabet in str1:
    print(alphabet)

numbers = [2,3,4,6,5,2,1,-3,-2]
squares = []
for i in numbers:
    square = i ** 2
    squares.append(square)
print(squares)


# for else :

# in loops else keyword is used to check if loop is fully executed or not
# else block shows there is no break
"""
Note : The else block just after for/while is excuted only
       when the loop is not termineted by break statement.
"""
tuple1 = (1,2,3,4,5,6)
for i in tuple1:
    print(i)
else:
    print("You have successfully get out of for loop") 

tuple2 = (1,2,3,4,5,6)
for i in tuple1:
    print(i)
    if i == 4:
        break
else:
    print("You have successfully get out of for loop") 

# for loop using dictionary :

dict1 = {
         "name":"rajesh",
         "city": "bhavnagar"
        } 
for x in dict1:
    print(x,":",dict1[x])

# for loop with continue statement :
"""
    The cotntinue statement is loop conntnrol statement 
    that forces the next iteration of the loop while skipping the rest of the 
    code inside the loop for the current iteration only.

    When the continue statement executed in the loop,
    the code inside the loop following the continue statement
    will be skipped for the current iteration of the loop will begin.

    The continue statement can be used in both while and for loops.

"""

for char in "hello this is continue":
    if char == "l" or char == "i" or char == " ":
        continue
    print("current character : ",char)


for q in range(0,10):
    if q == 5:
        continue
    print(q)

# for loop with break statement :

"""
    The break statement in python is a loop control statement
    that is used to terminate the execution of the current loop.
    When a break statement is encountered, the interpreter
    will immediately exit the loop and continue execution with the
    statement that follows the loop.

"""

for t in range(10):
    print(t)
    if t == 5:
        break

"""
    The break statement can also be used in nested loops. 
    When a break statement is encountered in a nested loop, 
    it will only terminate the innermost loop. 
    The outer loop will continue executing.

"""

for i1 in range(10):
    for j in range(5):
        if j == 4:
            break
        print(i1)

for char1 in "hello this is break":
    if char1 == "l" or char1 =="i":
        break
    print(char1)      


# for loop with pass statement :

"""
The pass statement in Python is a null statement that does nothing. 
It can be used as a placeholder for future code, 
or to prevent an error when empty code is not allowed. 
For example, you could use the pass statement inside an 
if statement to prevent an error if the condition is always 
false.

"""

for b in range(10):
    pass

# Here is an example of how a pass statement can be used to skip a particular iteration of a loop:

for f in range(10):
    if f == 5:
        pass
    else:
        print(f)

"""
This loop will print the numbers 0 through 4, 
and then skip 5. The pass statement is used to skip the 
iteration of the loop where i is equal to 5.
Pass statements can be a useful tool for Python programmers.
They can be used in a number of situations, 
such as when you want to placeholder for code that has 
not been written yet, or to skip a particular iteration of a loop.
"""


# nested for loop :

"""
    A loop within another loop
"""
for s in range(2):
    for e in range(1,10):
        print(e, end="")
    print()    

rows = int(input("Enter the number of rows :"))
columns = int(input("Enter the number of columns :"))
symbol = input("Enter the symbol to use :")

for a1 in range(rows):
    for a2 in range(columns):
        print(symbol, end="")
    print()    


# range() function :

"""
   - Python range() function is a built-in function that is
     used when a user needs to perform an action a specific number of times.
   - The range() function is used to generate a sequence of numbers.
     depending on how many arguments the user is passing to the
     function, the user can decide where that series of numbers
     will begin and end as well as how big the difference will be
     between one number and the next.range() takes mainly three arguments.
   
   # start : integer starting from which the sequence of integers is to be returned.

   # stop : integer before which the sequence of integers is to be returned
            the range of integers ends at stop -1.
   
   # step : integer value which determines the increment between each integer in the sequence.
            
"""

# Eg.

for o in range(10):
    print(o,end="")

for e in range(1,11,2):
    print(e,end="")

list1 =[10,20,30]

for w in range(len(list1)):
    print(list1[w],end="")

sum1 = 10
for q in range(1,20,5):
    sum1 = sum1 + q
print("Sum is :", sum1)    




# while loop :

"""
    - While loop is used to execute a block of statements repeatedly until
      a given condition is satisfied.
    - When the condition become false, the line immediately after 
      the loop in the program executed.
    - While loop falls under the category of indefinite iteration.
    - Indefinite iteration means that the number of times the loop
      is executed itsn't specified explicitly in advance.      

"""

count = 0
while count<3:
    count += 1
    print("Hello world")

# single statement while block :

"""
    - Just like the if block, if the while block consists of a single statement
      we can declare the entire loop in a single line.
    - If there are multiple statements in the block that makes up the loop
      body, they can be separated by semicolons(;).
"""

count1 = 0
while (count1 < 3): count1 += 1; print("Hello world")

# while loop with continue statement :

g = 0
h = "hello this is continue"

while g < len(h):
    if h[g] == 'e' or h[g] == 'l':
        g+=1
        continue
    print("current letter : ", h[g])
    g += 1

# while loop with break statement :

o1 = 0
i5 = "hello this is break"

while o1 < len(i5):
    if i5[o1] == 'l' or i5[o1] == 'b':
        o1 += 1
        break
    print("Current letter :", i5[o1])
    o1 += 1 

# while loop with pass :

p = "hello this is pass"
u = 0

while u < len(p):
    u += 1
    pass
print("Value of u:",u)


# while loop with else :

z = 0
while z < 4:
    z += 1
    print(z)
else:
    print("No break\n")   


