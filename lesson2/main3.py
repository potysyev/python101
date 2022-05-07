year_list = ["", "winter", "winter", "spring", "spring", "spring", "summer", "summer",
             "summer", "autumn", "autumn", "autumn", "winter"]
year_dict = {'1': 'winter', '2': 'winter', '3': 'spring', '4': 'spring',
             '5': 'spring', '6': 'summer', '7': 'summer', '8': 'summer',
             '9': 'autumn', '10': 'autumn', '11': 'autumn', '12': 'winter'}
usr_month = 0
while usr_month > 12 or usr_month < 1:
    usr_month = int(input("enter a month in number format (0-12) "))

print("Month name using list: ", year_list[usr_month])
print("Month name using dictionary: ", year_dict[str(usr_month)])
