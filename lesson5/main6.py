try:
    with open("ex6.txt", "r", encoding='utf-8') as f_obj:
        data_dict = {}
        for line in f_obj:
            line_key = line[0:line.find(":")]
            line_hrs_sum = sum([int(el[0:el.find("(")]) for el in line[line.find(":") + 1:].split(" ")
                                if el != "-" and el != "" and el != "-\n"])
            data_dict[line_key] = line_hrs_sum

    print(data_dict)
except IOError:
    print("Impossible to read file")
