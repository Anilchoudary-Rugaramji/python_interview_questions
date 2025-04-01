def match_string_start_and_end(l):
    counter = 0
    for word in l:
        if len(word)>1 and word[0]==word[-1]:
            counter += 1
    return counter

print(match_string_start_and_end(['abc','12345','1221','aba']))