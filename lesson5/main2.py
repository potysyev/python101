try:
    with open("ex2.txt", "r", encoding='utf-8') as f_obj:
        file_stat = []
        for i, line in enumerate(f_obj):
            file_stat.append(len(line.split()))

    print(f"Number of lines: {len(file_stat)} and number of words in each line: {file_stat}", sep=", ")
except IOError:
    print("Impossible to read file")
