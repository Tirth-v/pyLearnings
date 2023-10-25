"""
Write a Python program to count the frequency of words in a file. [TIRTH]
Number of words in the file : Counter({'this': 7, 'Append': 5, 'text.': 5, 'text.Append': 2, 'Welcome': 1, 'to
': 1, 'w3resource.com.': 1})
"""

import re


def count_word(file_path):
    word_freq = {}
    print(type(word_freq))
    f = open(file_path, 'r')
    for i in f:
        words = re.findall(r'\b\w+\b', i)
        for word in words:
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1
            else:
                word_freq[word] = 1
    return word_freq


path_ = 'file.txt'
words = count_word(path_)
print(words)


"""
Write a Python program to create a decorator function 
[use Comprehension and regex].[spacial character place will remain same] [TIRTH]
Input: H#1&TR%KL
Output: 1#H&RT%LK
"""


txt = "1#H&RT%LK"
ptn1 = r"\w"
ptn2 = r"\W"
k = re.findall(ptn1, txt)
m = re.findall(ptn2, txt)
print(k)
print(m)


for x in range(0,len(k),2):
    print(x)
    temp = k[x]
    k[x] = k[x+1]
    k[x+1] = temp

updated_txt = k[:]
output = []

x = 0
for char in txt:
    if char.isalnum():
        output.append(updated_txt[x])
        x = x + 1
    else:
        output.append(char)
print("".join(output))
