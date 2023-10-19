# Regular expressions :
"""
    A regular expression is a cryptic looking string that
    describes a search pattern.
    Each of these regular expressions describes a way to search a string for a pattern.
"""


# Expressions :
"""
        \  : used to drop the special meaning of character.
        [] : Represents a character class
        ^  : Matches the beginning
        $  : Matches the end
        .  : Mathc any character except newline
        |  : Means OR(Matches with any of the character seperated by it.)
        ?  : Matches zero or one occurrence
        *  : Any number of occurrences(including 0 occurrences)
        +  : One or more occurrences
        {} : Indicates the number of occurrence of preceding
             regex to match.
        () : Enclose a group of regex
"""





import re

names = ['Alec benjamin',
         'Steve harrington',
         'arijit singh',
         'CodingRobo',
         'Hermoini granger',
         'ronald wisley',
         'prataphv']
# match method :
for name in names:
    x = re.match("p",name)
print(x.end())

# re.search(pattern, string) :
"""
The re.search() function in Python's re module is used 
to search a given string for a specified pattern (regular expression) 
and return a match object if a match is found. 
It searches the entire input string for the first occurrence of the pattern, 
and if it finds a match, it stops searching and returns the match object.
"""

#  This is the input string in which you want to search for the pattern.
text = "The quick brown fox jumps over the lazy dog and the fox looks at dog."
# This is the regular expression pattern you want to search for within the input string.
pattern = r"fox"

# Search for the pattern in the text
match = re.search(pattern,text)
print(match)
# <re.Match object; span=(16, 19), match='fox'>
if match:
    print("Pattern found:", match.group())
    # Access the matched string
else:
    print("Pattern not found")

"""
In this example, re.search() looks for the pattern "fox" within the text 
and returns a match object because a match is found. 
The match.group() method is used to access the matched string, 
which, in this case, would be "fox."

If the pattern is not found in the input string, re.search() returns None. 
It's important to check if a match object is returned before attempting to 
access its attributes to avoid potential errors.
"""


# re.match :

"""
The re.match() function is used to determine 
if a regular expression pattern matches at the beginning of a string. 
If a match is found at the beginning of the string, 
it returns a match object; otherwise, it returns None.
"""

text = "The quick brown fox jumps over the lazy dog."
pattern = r"The"

# Attempt to match the pattern at the beginning of the text
match = re.match(pattern, text)

if match:
    print("Pattern matched:", match.group())
    # Access the matched string
else:
    print("Pattern not found at the beginning")

"""
One key difference between re.match() and re.search() is that re.match() 
only looks for a match at the beginning of the string, 
while re.search() searches the entire string for a match. 
This means that re.match() is often used when you specifically want to check 
if a pattern occurs at the very start of the string
"""


# re.fullmatch :
"""
the re.fullmatch() function is used to determine 
if a regular expression pattern matches the entire input string. 
It's similar to re.match(), but it requires that 
the entire string be a match for the pattern. 
If the entire string matches the pattern, 
it returns a match object; otherwise, it returns None.
"""

text = "The quick brown fox jumps over the lazy dog."
pattern = r"The quick brown fox jumps over the lazy dog."

# Attempt to find a full match of the pattern in the text
match = re.fullmatch(pattern, text)

if match:
    print("Pattern fully matched:", match.group())
    # Access the matched string
else:
    print("Pattern not found as a full match")

"""
re.fullmatch() is useful when you want to ensure that the entire input string conforms 
to a specific pattern and not just a partial match. It's particularly handy for cases 
where you need to validate or check if a string is fully compliant with a particular format or pattern.
"""


# re.split() :
"""
the re.split() function is used to split a string into a list of 
substrings based on a specified regular expression pattern. 
It allows you to split a string wherever the pattern matches.
"""

text = "apple,banana-cherry,grape"
pattern = r"[,-]"

# Split the text using a regular expression pattern that matches ',' or '-'
result = re.split(pattern, text)

print(result)

"""
In this example, the re.split() function splits the text string into 
a list of substrings wherever it encounters either a comma (,) or a hyphen (-). 
The resulting list, result, will contain the substrings ['apple', 'banana', 'cherry', 'grape'].

You can use re.split() to tokenize or break down text based on specific patterns, 
which can be helpful for tasks like parsing data, tokenizing natural language text, 
or splitting a string into meaningful components.
"""


# re.findall() :
"""
the re.findall() function is used to find all non-overlapping 
occurrences of a regular expression pattern in a given input string. 
It returns a list of all matches found in the input string.
"""

text = "The quick brown fox jumps over the lazy dog. The fox is fast."
pattern = r"fox \w"

# Find all occurrences of the pattern in the text
matches = re.findall(pattern, text)

print(matches)

"""
In this example, re.findall() looks for all occurrences of the pattern "The \w+" in the text string. 
This pattern matches "The" followed by one or more word characters. 
The resulting matches list will contain all non-overlapping occurrences of this pattern in the input string.

re.findall() is commonly used to extract multiple occurrences of a specific pattern from a string. 
It returns all matches as a list of strings, making it useful for various text processing tasks like extracting words, 
numbers, or other structured data from a text document or input string.
"""


# re.sub() :
"""
The re.sub() function is used to search for 
a regular expression pattern in a given input string and replace 
all occurrences of that pattern with a specified replacement string.
It returns a new string with the replacements applied.
"""


text = "The quick brown fox jumps over the lazy dog and the fox hit the dog, so fox is fox."
pattern = r"fox"

# Replace occurrences of "fox" with "cat"
new_text = re.sub(pattern, "cat", text)

print(new_text)

"""
re.sub() is commonly used for text manipulation, 
data cleaning, and text transformation tasks where you 
want to replace specific patterns in a string with new content. 
The replacement can be a simple string or a more complex expression, 
allowing for a wide range of text processing tasks.
"""

# re.escape() :
"""
the re.escape() function is used to escape (i.e., add backslashes to) 
any characters in a string that might have special meaning in a regular 
expression pattern. This function is helpful when you want to treat a string 
as a literal string and prevent any special characters within it from being interpreted 
as part of a regular expression.
"""

raw_string = "This is a dot (.), a plus (+), and some parentheses ( )."
escaped_string = re.escape(raw_string)

print(escaped_string)

"""
In this example, the re.escape() function is used to escape the raw_string, 
which contains characters like "(", ")", ".", and "+," which have special meaning in regular expressions. 

re.escape() is particularly useful when you want to include user-generated 
or dynamically generated strings in regular expressions and ensure that any 
special characters within those strings do not interfere with the regular 
expression's functionality. It's a common practice to use re.escape() when 
incorporating user input into regex patterns to avoid unintentional 
errors or vulnerabilities.
"""

# re.compile :
"""
the re.compile() function is used to compile a regular expression pattern into a regex object, 
which can then be used for various operations like searching, matching, or splitting text. 
Compiling a regular expression pattern into an object can be more efficient when you need to 
perform multiple operations with the same pattern because it precomputes the regex for better performance.
"""

pattern = r"\d+"
text = "There are 42 cats and 7 dogs in the neighborhood."

# Compile the regular expression pattern
regex_object = re.compile(pattern)

# Use the compiled regex object to find all matches in the text
matches = regex_object.findall(text)

print(matches)

"""
In this example, the re.compile() function is used to compile the regular expression pattern 
\d+ into a regex object. The compiled regex_object is then used to find all matches of one 
or more digits in the text string.

Using re.compile() is beneficial when you intend to use the same regular expression
pattern multiple times, as it can lead to better performance compared to recompiling the 
pattern each time you use it. This can be particularly advantageous in situations where you 
need to apply the same regex pattern to a large amount of text data.
"""

# re.finditer() :
"""
the re.finditer() function is used to find all non-overlapping occurrences of a regular
expression pattern in a given input string and return an iterator that yields match objects 
for each match found. This allows you to iterate through the match objects and access information 
about each match, such as the matched string and the location of the match in the input string.
"""

text = "The quick brown fox jumps over the lazy dog. The fox is fast."
pattern = r"The \w+"

# Find all occurrences of the pattern in the text
matches = re.finditer(pattern, text)

for match in matches:
    print("Match found:", match.group(), "at position:", match.start())

"""
In this example, re.finditer() looks for all non-overlapping occurrences 
of the pattern "The \w+" in the text string. The pattern matches "The" followed 
by one or more word characters. The matches variable is an iterator that yields match objects. 
We iterate through the match objects and print the matched string and the starting position 
of each match in the input string.
re.finditer() is particularly useful when you need to locate and analyze multiple 
occurrences of a specific pattern within a text. It allows you to process each match individually, 
providing flexibility and control over your text processing tasks.
"""


# Meta characters :


txt = """Hello there,
I am tirth and
my email id is :
alphabeta11@gamma.com
and my contact number is :
7575897568.
"""
x = re.findall("[a-r]",txt)
#Find all lower case characters alphabetically between "a" and "r":
print(x)
x = re.findall("\d", txt)
# Find all digit characters
print(x)
x = re.findall("e.a", txt)
# Search for a sequence that starts with "e", followed by two (any) characters, and an "a":
print(x)
x = re.findall("^Hello", txt)
# Check if the string starts with 'Hello':
print(x)
x = re.findall("7568.$", txt)
# Check if the string ends with '7568.':
print(x)
if x:
  print("Yes, the string ends with '7568.'")
else:
  print("No match")
x = re.findall("He.*t", txt)
# Search for a sequence that starts with "He", followed by 0 or more  (any) characters, and an "t":
print(x)
x = re.findall("He.+o", txt)
# Search for a sequence that starts with "He", followed by 1 or more  (any) characters, and an "o":
print(x)
x = re.findall("He.?o", txt)
# Search for a sequence that starts with "He", followed by 0 or 1  (any) character, and an "o":
print(x)
# This time we got no match, because there were not zero, not one, but two characters between "He" and the "o"
x = re.findall("He.{2}o", txt)
# Search for a sequence that starts with "He", followed excactly 2 (any) characters, and an "o":
print(x)
x = re.findall("gamma|eta", txt)
# Check if the string contains either "gamma" or "eta":
print(x)
