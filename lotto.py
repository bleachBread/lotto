import time
from os import system
from math import floor

def cls():
    system("cls")



print("podaj koszt wstepu")
cost = input()
cls()

print("podaj liczbe nagrod, nie wliczając jackpot'a")
prizes = input()
cls()

print("podaj wartosc jackpot'a")
jackpot = input()
cls()

prize_values = []
prizes = int(prizes)
for x in range(prizes):
    print("podaj kwote " + str(x + 1) + " nagrody")
    y = input()
    prize_values.append(y)
    cls()

print("podaj minimalna liczbe")
min_num = input()
cls()

print("podaj maxymalna liczbe")
max_num = input()
cls()

range_boi = (int(max_num) - int(min_num)) + 1

chance = []
for x in range(prizes):
    y = (1 / int(range_boi)) ** (x+1)
    chance.append(y)

jackpot_chance = chance[0] ** prizes
grandPrize = float(jackpot_chance) * (float(jackpot) - float(cost))

arr = []
expect_profit = 0
for x in range(prizes):
    y = (float(chance[x]) - float(jackpot_chance)) * (float(prize_values[x]) - float(cost)) + (1.0 - float(jackpot_chance))
    arr.append(y)
    expect_profit += arr[x]

print("liczba slotow: " + str(prizes))
print("przewidziane zarobki: " + str(expect_profit))
for x in range(prizes):
    print(str(x+1) + " szansa: " + str(chance[x]))

for x in range(prizes):
    print(str(x+1) + " nagrody: " + str(prize_values[x]))




x = input()