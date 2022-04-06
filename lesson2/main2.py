usr_number = int(input("how much numbers you want to enter? "))
usr_list = []

for i in range(usr_number):
    usr_list.append(input("input a number "))

for j in range(1, usr_number, 2):
    usr_list[j - 1], usr_list[j] = usr_list[j], usr_list[j - 1]

print(usr_list)
