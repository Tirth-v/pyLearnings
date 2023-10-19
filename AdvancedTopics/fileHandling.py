"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

# In addition, you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

"""
f = open("file.txt",)
print(f.read())

f = open("file.txt",)
print(f.read(5))

f = open("file.txt",)
print(f.readline())

f = open("file.txt",)
print(f.readline())
print(f.readline())

f = open("file.txt", "r")
print(f.readline())
f.close()


"""
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

f = open("file.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("file.txt", "r")
print(f.read())

f = open("file.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("file.txt", "r")
print(f.read())

# Create a new file
"""
To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""
"""
f = open("myfile2.txt", "x")
f = open("myfile1.txt", "w")
"""
# Delete a file :
"""To delete a file, you must import the OS module, and run its os.remove() function:"""
import os
# os.remove("myfile1.txt")

"""
Check if File exist:
To avoid getting an error, you might want to check if the file 
exists before you try to delete it:
"""

if os.path.exists("myfile2.txt"):
  os.remove("myfile2.txt")
else:
  print("The file does not exist")

"""
Delete Folder
To delete an entire folder, use the os.rmdir() method:
"""
os.rmdir("Delete")