# Write a program called ‘references.py’ to reformat references as follows:The author names are in title case, The title has only the first letter capitalised and,  The rest remains the same. 
# Name: Nyakallo Nyokong
# Student ID: NYKNYA004
# Date: 10-04-2025

reference = input("Enter the reference:\n")

author= reference[0:reference.find("(")]
author = author.title()
comma = reference.find(",")
title = reference[reference.find(")")+2:reference.find(",",comma+1)]
title= title.capitalize()
brac1 = reference.find("(")
brac2 = reference.find(")")
year =  reference[brac1:brac2+2]

rest = reference[reference.find(",",comma+1):]

print("Reformatted reference:")
print(f"{author}{year}{title}{rest}")


