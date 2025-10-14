from datetime import date
year=date.today().year
birthyear=int(input("which year did you born?"))
age=year-birthyear
if age<9:
    print("You are Benjamin.")
elif age<14:
    print("You are Infatil.")
elif age<19:
    print("You are Junior.")
elif age<25:
    print("You are senior.")
else:
    print("You are Master.")