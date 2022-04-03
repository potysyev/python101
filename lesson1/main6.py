revenue = float(input("Input revenue: "))
expense = float(input("input expenses: "))

profit = revenue - expense

if profit > 0:
    e_num = int(input("How many employees works now in company? "))
    profit_rate = profit / expense
    profit_per_employee = profit / e_num
    print("we are making money with profit rate {} and profit per employee is {}".format(profit_rate, profit_per_employee))
else:
    print("we are depleting our savings")