from itertools import count, cycle

input_flag = True
while input_flag:
    try:
        start_num = int(input("input starting number: "))
        input_flag = False
    except:
        print("Input integer only")
        input_flag = True

steps_limit = 15
for el in count(start_num):
    if el < (start_num + steps_limit):
        print(el)
    else:
        break

iteration_list = ["A", "B", "C"]
cycles_limit = 10
c = 0
for cel in cycle(iteration_list):
    if c < cycles_limit:
        print(cel)
    else:
        break
    c += 1
