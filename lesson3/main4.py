def my_func_first(x, y):
    return x ** y


def my_func_second(x, y):
    prod = 1 / x
    for i in range(1, abs(y)):
        prod = prod / x
    return prod


x = int(input("Input positive number: "))
y = 0
while y >= 0:
    y = int(input("Input negative integer: "))
print(f"Result of first function {my_func_first(x, y)}")
print(f"Result of second function {my_func_second(x, y)}")
