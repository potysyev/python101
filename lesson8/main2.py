class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


usr_num1, usr_num2 = input('Input two numbers, space separated: ').split(" ")

try:
    usr_num1 = int(usr_num1)
    usr_num2 = int(usr_num2)
    if usr_num2 == 0:
        raise ZeroError("Delimiter equals zero!")
    else:
        total = usr_num1 / usr_num2

except ZeroError as err:
    print(err)
    total = None

except ValueError:
    print("One of the values is not digit")
    total = None

print(total)
