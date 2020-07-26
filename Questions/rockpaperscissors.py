import random
# What we need
# User input
# Random
# control flow

while True:
    options = ["rock", "paper", "scissors"]

    computer = random.choice(options)

    print("Welcome to rock, paper scissors")
    player = input("Please choose: ")
    print("Computer chooses: {}".format(computer))


    if player == computer:
        print("Game tied")
    elif player == "rock" and computer == "scissors":
        print("{} Beats {} player wins".format(player, computer))
    elif player == "scissors" and computer == "paper":
        print("{} Beats {} player wins".format(player, computer))
    elif player == "paper" and computer == "rock":
        print("{} Beats {} player wins".format(player, computer))
    elif computer == "rock" and player == "scissors":
        print("{} Beats {} computer wins".format(computer, player))
    elif computer == "scissors" and player == "paper":
        print("{} Beats {} computer wins".format(computer, player))
    elif computer == "paper" and player == "rock":
        print("{} Beats {} computer wins".format(computer, player))

