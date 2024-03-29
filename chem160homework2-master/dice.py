import array
import random

ntrials = 10000
player1win = 0 # Counter for wins
player2win = 0
draws = 0
p1Total = 0 # Current round's max number
p2Total = 0
numbersP1 = [] # Players array of numbers/rolls
numbersP2 = []

for n in range (10000):
    for x in range(0,3):
        randomNum = random.choice(range(1,7))
        numbersP1.append(randomNum)
    numbersP1.sort(reverse = True)
    p1Total = numbersP1[0] + numbersP1[1];
    # print(p1Total)
    # print(numbersP1)

    for j in range(0,2):
        randomNum = random.choice(range(1,7))
        numbersP2.append(randomNum)

    if numbersP2[0] == numbersP2[1]:
        #could be set to a number larger than 12 if desired
        p2Total = 20
    else:
        p2Total = numbersP2[0] + numbersP2[1]
    # print(p2Total)
    # print(numbersP2)

    if p1Total > p2Total:
        player1win = player1win + 1
    elif (p1Total < p2Total):
        player2win = player2win + 1
    else:
        draws = draws + 1

    numbersP1.clear()
    numbersP2.clear()

print("Player 1 wins: " + str(player1win))
print("Player 2 wins: " + str(player2win))
print("Amount of draws: " + str(draws))

#The game is still unfair as player 1 is still more likely to win with three dice regardless of set conditions for player 2
