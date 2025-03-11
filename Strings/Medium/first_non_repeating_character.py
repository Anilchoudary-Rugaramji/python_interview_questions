"""
Write the python function that takes a string as input and returns the first
non repeating charcter in the stirng. If there are no non repeating characters
return None.

"""

# method 1 using count method


def first_non_repeating_character(s: str) -> str:
    """Returns the first non repeating character in the input string."""
    for char in s:
        if s.count(char) == 1:
            return char
    return None


print(first_non_repeating_character("hello"))
print(first_non_repeating_character("hellohworld"))

# method 2 using dictionary


def first_non_repeating_character_with_dict(s: str) -> str:
    """Returns the first non repeating character in the input string."""
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None


print(first_non_repeating_character_with_dict("hello"))
print(first_non_repeating_character_with_dict("hellohworld"))
