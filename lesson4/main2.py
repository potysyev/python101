input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

output_list = [el for i, el in enumerate(input_list) if el > input_list[i - 1] and i > 0]

print(output_list)
