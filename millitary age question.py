from datetime import date
year=date.today().year
age=int(input("Which year did you born"))
birthyear=year-age
if birthyear<18:
    print("You are too young to enter the millitary.")
elif birthyear<25 and 18<birthyear:
    print("You can go to the millitary.")
else:
    print("You are too old for the military.")