import random
print("======================")
print("ROCK PAPER SCISSOR")
print("======================")

print("1) ✊ (Rock)")
print("2) ✋ (Paper)")
print("3) ✌  (Scissor)")

player = input("Select a number from (Rock, Paper, Scissor) : ")
Rock = "✊"
Paper = "✋"
Scissor = "✌"

option = ["Rock", "Paper", "Scissor"]
computer = random.choice(option)

print(f"Your choice : {player}")
print(f"CPU choice : {computer}")

if player == computer:
    print(f"Both selected the same {player}. It's a tie!")
elif player == "Rock":
    if computer == "Scissor":
        print("Rock smashes scissor. You Win!")
    else:
        print("Paper covers Rock. You lose!")
elif player == "Paper":
    if computer == "Rock":
        print("Paper covers Rock. You Win!")
    else:
        print("Scissor cuts paper. You lose!")
elif player == "Scissor":
    if computer == "Paper":
        print("Scissor cuts paper. You Win!")
    else:
        print("Rock smashes scissor. You lose!")