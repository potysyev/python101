usr_time = int(input("Input time is seconds"))
hrs = usr_time // (60 * 60)
minutes = (usr_time % (60 * 60)) // 60
seconds = usr_time - (hrs * (60 * 60) + minutes * 60)

print("{}:{}:{}".format(hrs, minutes, seconds))
