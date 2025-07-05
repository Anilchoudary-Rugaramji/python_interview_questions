names = ["alice", "bob", "charlie", "david"]

filter_upper_case = (name.upper() for name in names if len(name) > 4)

print(f"Filtered words and upper case {filter_upper_case}")

for name in filter_upper_case:
    print(name)
