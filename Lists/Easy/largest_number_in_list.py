def largest_number_in_list(l):
    max = l[0]
    for ele in l:
        if ele > max:
            max = ele
    return max


print(largest_number_in_list([2, 4, 6, 7, 3, 6]))
