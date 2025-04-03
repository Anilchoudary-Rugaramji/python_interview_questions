"""
* Lists are used to store multiple items in a single variable.

* Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

* Lists are created using square brackets.

*List items are ordered, changeable, and allow duplicate values.

*List items are indexed, the first item has index [0], the second item has index [1] etc.

*When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

*If you add new items to a list, the new items will be placed at the end of the list.

"""

# Accessing the list itmes

my_list = ['hi', 'these', 'excercises', 'gives', 'dopamine', 'shot']

print(my_list[0])

# Chnage the list items

my_list[1] = 'that'

print(my_list)

# Change the range of items from 2nd to last but one

my_list[1:-1] = ['1', '2', '3', '4']

print(my_list)

# add in bw

my_list[2] = ['100', '200']

print(my_list)

my_list.insert(2, 'ok_added_to_3nd_positiom')

print(my_list)

# Using APPEND


my_list.append([1, 2, 3])

print(my_list)

my_list = [1, 2, 3, 4, 5]

your_list = ['I', 'am', 'a', 'boy']

my_list.extend(your_list)

print(my_list)


# Removing items with item name

my_list = ['1', '2', '3', '4', '2']

my_list.remove('2')

print(my_list)

# Removing items with item index

my_list = ['1', '2', '3', '4', '2']

# so here 4th value that is 4 must be removed

my_list.pop(3)

print(my_list)

# del keyword also removes the specified index

this_list = ['apple', 'banana', 'cherry']

del this_list[2]

print(this_list)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
