# A program called punctuation.py that takes a paragraph as input and:  Removes all punctuation marks (.,!?;:) from a paragraph.  Counts and displays the number of unique words in a paragraph.
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 10-04-2025

import string
paragraph = input("Enter a paragraph of any length:\n")

punctuation = ".,?;:!"
clean_paragraph = ""

for x in paragraph:
    if x not in punctuation:
        
        clean_paragraph += x
print("A paragraph without punctuation:")
print(clean_paragraph)
words = []
current_words = ""


for i in clean_paragraph:
    if i == " ":
        words.append(current_words)
        current_words = ""
    else:
        current_words += i
    
    
if current_words:
    words.append(current_words)
    current_words=""

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
num = len(unique_words)
print("The number of unique words in a paragraph:")
print(num)
print("The unique words are:")
print(unique_words)

