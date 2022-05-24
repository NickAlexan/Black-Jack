import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

def more(hand):
    rand_card = random.choice(cards)
    if rand_card == 11 and sum(hand) > 10:
        rand_card = 1
    hand.append(rand_card)


def game():
    print("-------------------\n B L A C K J A C K\n-------------------")
    print("Welcome to BlackJack!")
    player = []
    computer = []
    # Random generate player hand:
    player.extend([random.choice(cards),random.choice(cards)])
    if sum(player) == 22: # If generated 2 aces
        player = [11, 1]
    # Random generate PC hand:
    computer.extend([random.choice(cards), random.choice(cards)])
    if sum(computer) == 22: # If generated 2 aces
        computer = [11, 1]

    print(f"Your hand: {player}")
    print(f"PC hands: [{computer[0]}, ?]")

    go_on = True
    while go_on:
        give_more = input("Do you want one more card? y/n ").lower()
        if give_more == "y":
            more(player)
            print(player)
            if sum(player) > 22:
                go_on = False
                return print("You LOSE!")
        if give_more == "n":
            while sum(computer) < 17:
                more(computer)
            go_on = False

    # Compare cards player VS PC
    print("----------------")
    print(f"Your hand: {player}")
    print(f"PC hand: {computer}")

    if sum(computer) > 21:
        print("You WIN!")
    elif sum(player) < sum(computer):
        print("You LOSE!")
    elif sum(player) > sum(computer):
        print("You WIN!")
    else:
        print("DRAW!")


game_on = True
while game_on:
    start = input("\nDo you wanna play BlackJack. y/n ").lower()
    if start == "y":
        game()
    else:
        game_on = False


