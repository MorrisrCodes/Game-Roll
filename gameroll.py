import random

print("   *** Game Roll ***   \n\n")
print("This program will randomly select a game for you to play from a list you provide.")

gameNum = int(input("Enter Number of games: "))
print()
games = []
              
for i in range(gameNum):
    games.append(input("Enter game name: "))

game = random.choice(games)

print()
print(f'The chosen game is... {game}')
print(f'Thank you, goodbye!')
