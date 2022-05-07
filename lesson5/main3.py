try:
    with open("ex3.txt", "r", encoding='utf-8') as f_obj:
        below_threshold = []
        avg_sum = []
        for line in f_obj:
            if float(line.split()[1]) < 20000:
                below_threshold.append(line.split()[0])
            avg_sum.append(float(line.split()[1]))

    print(f"Average salary: {sum(avg_sum) / len(avg_sum)}. People with salary below 20000: {below_threshold}", sep=", ")
except IOError:
    print("Impossible to read file")
