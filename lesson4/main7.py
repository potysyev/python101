def fact(n_loc):
    prod = 1
    for el in range(1, n_loc + 1):
        prod = el * prod
        yield prod


input_flag = True
n = 0
while input_flag:
    try:
        n = int(input("Input number for factorial: "))
        input_flag = False
    except:
        print("Input integer only")
        input_flag = True

for el in fact(n):
    print(el)
