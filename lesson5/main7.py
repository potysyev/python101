import json

try:
    with open("ex7.txt", "r", encoding='utf-8') as f_obj, open("ex7_out.json", "w", encoding='utf-8') as json_obj:
        firm_dict = {}
        avg_profit = []
        firm_stat = []
        for line in f_obj:
            firm_name = line.split(" ")[0]
            profit = int(line.split(" ")[2]) - int(line.split(" ")[3])
            firm_dict[firm_name] = profit
            if profit > 0:
                avg_profit.append(profit)
        avg_profit = sum(avg_profit) / len(avg_profit)
        firm_stat = [firm_dict, {"Average profit": avg_profit}]
        print(firm_stat)

        json.dump(firm_stat, json_obj)

except IOError:
    print("Impossible to read file")
