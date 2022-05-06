class OnlyNumbersAllowed(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":
    usr_num_list = []
    exit_code = True
    while exit_code:
        usr_num = input("input a number, space for stop: ")
        if " " in usr_num:
            exit_code = False
            continue
        else:
            try:
                if not usr_num.isdigit():
                    raise OnlyNumbersAllowed("Only numbers allowed in this list")
            except OnlyNumbersAllowed as err:
                print(err)
            else:
                usr_num = int(usr_num)
                usr_num_list.append(usr_num)

    print(usr_num_list)
