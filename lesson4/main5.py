from functools import reduce


def product(pr_el, el):
    return pr_el * el


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(product, my_list))
