my_list = [7, 5, 3, 3, 2]
usr_number = 0
while True:
    usr_number = input("input new number for rating or (0) to quit ")
    if usr_number == "0":
        break

    my_list.insert(0, usr_number)
    for i in range(1, len(my_list)):
        if my_list[i] >= my_list[i - 1]:
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
    print(my_list)
