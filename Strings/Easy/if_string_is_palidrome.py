"""
Problem statement: Write a function that takes a string as input and returns True if the string is a palindrome and False if it is not.
"""


def is_palindrome(s: str) -> bool:
    """Returns True if the input string is a palindrome and False if it is not."""
    return s == s[::-1]


print(is_palindrome("hello"))
print(is_palindrome("racecar"))
