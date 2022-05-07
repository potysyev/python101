denominator = 0


def division(numerator, denominator):
    return numerator / denominator


numerator = float(input("Input value for numerator: "))
while denominator == 0:
    denominator = float(input("Input not zero value for denominator: "))

print(division(numerator, denominator))
