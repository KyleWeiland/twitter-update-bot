import auth
import helpers as h
import os

os.system("cls")

today = h.get_weekday()

if today == 0:
    # Monday
    print("Monday")

elif today == 2:
    # Wednesday
    print("Wednesday")

elif today == 4:
    # Friday
    print("Friday")

else:
    print("Not Hotdog")
