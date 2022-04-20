with open("out_file.txt", "w", encoding='utf-8') as f_obj:
    while (usr_str := input("Input data to write to file or empty line to finish: ")) != "":
        f_obj.write(usr_str + "\n")
