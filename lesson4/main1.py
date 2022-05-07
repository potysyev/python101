from sys import argv

script_name, rate, hrs, premium = argv

print(f"Salary is {float(rate)*float(hrs)+float(premium)}")
