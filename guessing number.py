from random import randint
playernumber=int(input("Choose a number between 1 and 5?"))
PCnumber= randint(1, 5)
if playernumber==PCnumber:
    print("You win, you get the same number as the computer.")
else:
    print("You lost, you have a different number compare to the computer")