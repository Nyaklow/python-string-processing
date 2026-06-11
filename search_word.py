# A program called punctuation.py that takes a paragraph as input and:  Removes all punctuation marks (.,!?;:) from a paragraph.  Counts and displays the number of unique words in a paragraph.
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 10-04-2025

sentence = input("Enter a sentence:\n")

word = input("Enter the word to find:\n")

sentence = sentence.lower()
word = word.lower()
output = 0

if word in sentence:
           print(f"The word '{word}' is in the sentence.")
           for i in range(len(sentence)):
                      if word[0] == sentence[i]:
                                 output += i
                                 break
           print(f"It first appears at index {output}.")
            
else:
           print(f"The word '{word}' is NOT in the sentence. ")
           
    