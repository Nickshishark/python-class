from random import randint
countdown=0
dice1 = 0
dice2 = 1
while dice1 != dice2:
    dice1=randint(1,6)
    dice2=randint(1,6)
    countdown += 1
print(f"it took you {countdown} times to roll the same number")