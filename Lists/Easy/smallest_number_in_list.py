def smallest_element_in_list(l):
    smallest = l[0]
    for element in l:
        if element < smallest:
            smallest = element
    return smallest


print(smallest_element_in_list([4, 3, 6, 8, 2]))
