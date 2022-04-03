usr_num = input("Input positive integer: ")
pos = 0
max_num = 0

while pos < len(usr_num):
    if int(usr_num[pos]) > max_num:
        max_num = int(usr_num[pos])
    pos += 1

print("maximum digit in number {} is {}".format(usr_num, max_num))
