"""
Problem Statement: Write a function that takes a string as input and returns the string 
reversed without using any built-in functions.

Description: Given a string, write a function that returns 
the string reversed without using any built-in functions.

Example:    Input: "hello"  Output: "olleh"             
Constraints: 
- The input string is not empty.
- The input string should return a new string that is reversed.
"""

# Method 1 using string slicing


def reverse_a_string(s: str) -> str:
    """Returns the reversed version of the input string."""
    return s[::-1]


string_input = "hello"
print(reverse_a_string(string_input))


# Method 2 using for loop

def reverse_a_string_using_loop(s: str) -> str:
    """Returns the reversed version of the input string."""

    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


string_input = "hello"
print(reverse_a_string(string_input))
