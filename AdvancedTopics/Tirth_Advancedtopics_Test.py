"""
Write a Python program to count the frequency of words in a file. [TIRTH]
Number of words in the file : Counter({'this': 7, 'Append': 5, 'text.': 5, 'text.Append': 2, 'Welcome': 1, 'to
': 1, 'w3resource.com.': 1})
"""

import re


def read_file(file_path):
    f = open(file_path, 'r')
    x = f.read()
    return x


def count_word(ok):

    words = re.findall(r'\b\w+\b', ok)
    word_freq = {word: words.count(word) for word in words}

    return word_freq


path_ = 'file.txt'
y = read_file(path_)
z = count_word(y)

print(z)


"""
Write a Python program to create a decorator function 
[use Comprehension and regex].[spacial character place will remain same] [TIRTH]
Input: H#1&TR%KL
Output: 1#H&RT%LK
"""


def swap_alpha(v):
    updated_txt = v[0][:]
    output = []

    x = 0
    for char in v[1]:
        if char.isalnum():
            output.append(updated_txt[x])
            x = x + 1
        else:
            output.append(char)
    print("".join(output))


def static_input():
    mylist = []
    txt = "1#H&RT%LK"
    ptn1 = r"\w"
    k = re.findall(ptn1, txt)

    for x in range(0, len(k), 2):
        temp = k[x]
        k[x] = k[x + 1]
        k[x + 1] = temp

    mylist.append(k)
    mylist.append(txt)

    return mylist


v = static_input()

swap_alpha(v)
