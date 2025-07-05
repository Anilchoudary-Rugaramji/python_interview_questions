nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = []

for i in nums:
    if i % 2 == 0:
        even_list.append(i)

sum = 0
for i in range(len(even_list)):
    sum = sum + even_list[i]

print(f"sum of all the even number in the lists is {sum}")
