usr_string = input("input several words separated with spaces ")
string_list = usr_string.split()
for i, el in enumerate(string_list):
    print(i + 1, el[:10])
