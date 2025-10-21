from random import randint
PCnumber = randint (1,100)
player = 0
while PCnumber != player:
    player = int(input("choose a number between 1 and 100. "))
    if PCnumber < player:
        print("smaller")
    elif player < PCnumber:
        print("bigger")
    else:
        print("you get it right")