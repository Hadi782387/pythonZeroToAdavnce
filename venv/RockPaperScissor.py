import random as rand
options=("rock","paper","scissors")
player=None
bot = rand.choice(options)

while player not in options:
    player = input("Enter your Move (rock,paper,scissors): ")
print(f"player: {player}")
print(f"computer: {bot}")

if (player=="rock" and bot == "scissors"):
    print("Player win: ")
elif(player == "scissors" and bot == "paper"):
    print("Player win: ")
elif(player == "paper" and bot == "rock"):
    print("Player win: ")
elif(player == bot):
    print("Draw: ")

else:
    print("computer win: ")





