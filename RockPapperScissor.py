import random

assets = ["r", "p", "s"]
computer = random.choice(assets)
user = input(">Type \nr:rock\np:paper\ns:scissor :")
d = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}

print(f"{d.get(computer)} v/s {d.get(user)}")
if user == computer:
    print("No Win")
elif user == "r":
    if computer == "p":
        print("Computer wins")
    else:
        print("User Wins")
elif user == "p":
    if computer == "s":
        print("Computer wins")
    else:
        print("User Wins")
else:
    if computer == "r":
        print("Computer wins")
    else:
        print("User Wins")
