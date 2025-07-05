def read_large_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()
