def user_data(name, surname, birthday, city, email, tel):
    return f'User data - name: {name}, surname: {surname}, date of birth: {birthday}, ' \
           f'city of living: {city}, email: {email}, telephone {tel}'


name = input("input user name: ")
surname = input("input user surname: ")
birthday = input("input user birthday: ")
city = input("input user city: ")
email = input("input user email: ")
tel = input("input user tel: ")

print(user_data(name=name, surname=surname, birthday=birthday, city=city, email=email, tel=tel))
