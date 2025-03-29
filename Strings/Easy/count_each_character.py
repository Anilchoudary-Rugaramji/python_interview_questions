def count_character(s):
    """Counnts the number of each character in the input string."""
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


print(count_character("banana"))
