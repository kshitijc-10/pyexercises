"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In: to input a list of at least eight items
# 2. Process: to sort the list and compute something from it using the pop() method ans sort() method
# 3. Out: printed the whole sorted list and exluded the last item from the list and printed it
# 4. What my list is about, and what I computed from it: my list is about numbers from 1 to 6 and I computed the last item from the list using the pop() method. The number is interesting because it is the largest number in the list and also sorted the list in ascending order using the sort() method.


# Your code below

number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6
    
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)
print(number6)

list = [1,2,3,4,5,6]
print(list)
print(list[3])

list.sort()
print("sorted list:", list)

sorted_list = list.pop()
print("sorted list:", sorted_list)
