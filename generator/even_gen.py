nums = [12, 13, 14, 15, 16]

even_generator = (n for n in nums if n % 2 == 0)
print(f"Even numbers are {even_generator}")

for n in even_generator:
    print(n)
