import random
lowestNum=1
highestNum=10
answer=random.randint(lowestNum,highestNum)
guesses=0
is_running=True
print("______python number guessing Game_______")
print(f"Select Number {lowestNum} to {highestNum}")

while is_running:
    guess=input("Enter Your guess: ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess>highestNum or guess<lowestNum:
            print("That number is out of range ")
            print(f"Select Number {lowestNum} to {highestNum}")
        elif guess>answer:
            print("low try again:")
        elif guess < answer:
            print("high try again:")
        else:
            print(f"correct the answer was {answer}")
            print(f"Number of Guesses you tried is {guesses}")
            is_running=False
    else:
        print("Invalid guess")
        print(f"Select Number {lowestNum} to {highestNum}")
