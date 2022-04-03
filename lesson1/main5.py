revenue = float(input("Input revenue: "))
expense = float(input("input expenses: "))

income = revenue - expense

if income > 0:
    print("we are making money")
else:
    print("we are depleting our savings")