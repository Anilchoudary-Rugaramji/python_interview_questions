"""
Problem Statement: Write a function that takes a string as input and returns the number of vowels in the string.

"""


def count_vowels(s: str) -> int:
    """Returns the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


print(count_vowels("hello"))
print(count_vowels("hello world"))
print(count_vowels("AeioU"))
