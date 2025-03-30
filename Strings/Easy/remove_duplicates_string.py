def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)


print(remove_duplicates("BANANA"))
print(remove_duplicates("ANILCHOUDARY"))


# alternate method usiing dict

def remove_duplicated_using_dict(s):
    """ fucntion to get unique characters from the string using dict.keys"""
    return "".join(dict.fromkeys(s))


print(remove_duplicated_using_dict("BANANA"))
print(remove_duplicated_using_dict("ANILCHOUDARY"))
