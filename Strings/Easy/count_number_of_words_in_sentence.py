def count_words_in_sentence(s):
    s = s.strip()
    if not s:
        return 0

    count = 1
    for char in s:
        if char == " ":
            count += 1

    return count


print(count_words_in_sentence(""))
print(count_words_in_sentence("hi, practicing python gives me dopamine shot"))

# using split function


def count_words_using_split(sentence):
    return len(sentence.split())


print(count_words_in_sentence(""))
print(count_words_using_split("hi, practicing python gives me dopamine shot"))
