def multiply_items_in_list(l):
    product = 1
    for i in l:
        product *= i
    return product


print(multiply_items_in_list([2, 3, 4, 5]))
