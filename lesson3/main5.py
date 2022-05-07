def summation(sum, list):
    for number in list:
        if number.isdigit():
            sum = sum + int(number)
    return sum


exit_code = False
sum = 0
while exit_code == False:
    usr_input = input("input space separated list of numbers, 'q' for stop: ")
    usr_input = usr_input.split()
    if "q" in usr_input:
        exit_code = True
    sum = summation(sum, usr_input)
    print(f"Sum of entered numbers: {sum}")
