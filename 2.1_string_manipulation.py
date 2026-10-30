"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""
# Your code below

from matplotlib.pyplot import title


sentence = input("Please enter a sentence: ")
print("uppercase:", sentence.upper())
print("lowercase:", sentence.lower())
print("title case:", sentence.title())
print("without outer spaces:", sentence.strip())

# 1. In: input a sentence from the user
# 2. Process:do transformations four transformation in the sentence using four functions, capital letters,small letters, title case and without capital.
# 3. Out: to print the transformed sentence in four different ways.
# 4. My four transformations, and when each is useful:
#uppercase: When you want to capitalize the text or make it stand out.
#lowercase: When you want to normalize the text for comparison purposes.
#title case: When you want to format a sentence with proper capitalization.
#strip: When you want to remove any leading or trailing whitespace from the text.
