def my_func(first_num, sec_num, third_num):
    numberlist = [first_num, sec_num, third_num]
    numberlist.sort(reverse=True)
    return numberlist[0] + numberlist[1]


first_num = int(input("input first number: "))
sec_num = int(input("input second number: "))
third_num = int(input("input third number: "))
print(f"Sum of two biggest numbers: {my_func(first_num, sec_num, third_num)}")
