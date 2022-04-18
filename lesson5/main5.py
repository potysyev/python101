with open("ex5.txt", "a+", encoding='utf-8') as w_obj:
    usr_input = " "

    while usr_input != "":
        usr_input = input("Input number to write to file, empty line to finish: ")
        if usr_input != "":
            w_obj.write(usr_input + " ")

    w_obj.seek(0)
    usr_sum = sum([int(el) for el in w_obj.read().split(" ") if el != ""])
    print(f"Sum of all values in file: {usr_sum}")

