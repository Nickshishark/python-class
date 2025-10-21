from random import randint
player1 = 300
player2 = 300
while 0 < player1 and 0 < player2:
    damage = randint (20,60)
    player2 -= damage
    print(f"player 1 hit a damage of {damage} to player 2")
    damage = randint (20,60)
    player1 -= damage
    print(f"player 2 hit a damage of {damage} to player 1")
    
if player1 < player2:
    print("player 2 wins")
else:
    print("player 1 wins")