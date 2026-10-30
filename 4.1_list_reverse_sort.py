"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input the list used in exercise 4.0
# 2. Process: use the sorted() function to sort the list in ascending and descending order, use the reverse() method to reverse the list, and use the sort() method to sort the list in place.
# 3. Out: print the list in ascending order, descending order, reversed order, and sorted order using the sort() method.
# 4. My four orders, and which ones modify the original: The `sorted()` function returns a new list, so it doesn't modify the original. The `reverse()` method modifies the list in place. The `sort()` method also modifies the list in place.


# Your code below
original_list = [1, 2, 3, 4, 5, 6]
ascending = sorted(original_list)
print("Ascending order:", ascending)
descending = sorted(original_list, reverse=True)
print("Descending order:", descending)
reversed_list = original_list.copy()
reversed_list.reverse()
print("Reversed order:", reversed_list)
sorted_list = original_list.copy()
sorted_list.sort()
print("Sorted using sort():", sorted_list)

