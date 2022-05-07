columns = ['name', 'price', 'quantity', 'unit']
stock = []
i = 1
breaker = "y"
tmp_dict = {}
while breaker == 'y':
    tmp_dict = {}
    for col in columns:
        tmp_dict[col] = input("input item {}: ".format(col))
    stock.append((i, tmp_dict))
    i += 1
    breaker = input("add another item? (y to continue) ")

print("Input database:")
print(*stock, sep='\n')

analysis = {}
for col in columns:
    tmp_list = []
    for stock_item in stock:
        tmp_list.append(stock_item[1][col])
    analysis[col] = list(set(tmp_list))

print("Output items by category:")
for key, value in analysis.items():
    print(key, ': ', value)
