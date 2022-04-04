a = int(input("How many km have you run in first day: "))
b = int(input("What result you are aiming: "))
day = 1
while a < b:
    a = a * 1.1
    day += 1

print("you will reach your goal on day {}".format(day))
