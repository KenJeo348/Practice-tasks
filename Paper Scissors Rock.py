def main_routine():
    import random
    while comp_score < 3 and player_score < 3:
        global comp_choice
        comp_choice = random.randint(1, 3)
        print("Choose one of the options below:")
        print("1: Paper")
        print("2: Scissors")
        print("3: Rock")
        choice = int(input("Enter your choice from 1-3"))

        if choice == comp_choice:
            game_tie()

        elif choice == 1:
            paper()

        elif choice == 2:
            scissors()

        elif choice == 3:
            rock()
        else:
            print("That number is invalid")
    else:
        game_over()


def game_tie():
    print("The result of the game was a tie.")
    print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


def paper():
    global comp_score
    global player_score
    if comp_choice == 2:
        print("The computer is the winner of this game.")
        comp_score += 1
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")
    else:
        print("You are the winner of this game.")
        player_score += 1
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


def scissors():
    global comp_score
    global player_score
    if comp_choice == 3:
        print("The computer is the winner of this game.")
        comp_score += 1
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")
    else:
        print("You are the winner of this game.")
        player_score += 1
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


def rock():
    global comp_score
    global player_score
    if comp_choice == 1:
        print("The computer is the winner of this game.")
        comp_score += 1
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")
    else:
        print("You are the winner of this game.")
        player_score += 1
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


def game_over():
    global comp_score
    global player_score
    if comp_score == 3:
        print("The computer is the winner of this match!")
        rematch = input("Do you want a rematch(Y: yes, N: no): ").upper()
        if rematch == "Y":
            comp_score = 0
            player_score = 0
            main_routine()
        else:
            print("Thank you for playing Paper Scissors Rock")
    elif player_score == 3:
        print("You are the winner of this match!")
        rematch = input("Do you want a rematch(Y: yes, N: no): ").upper()
        if rematch == "Y":
            comp_score = 0
            player_score = 0
            main_routine()
        else:
            print("Thank you for playing Paper Scissors Rock")


# Main Routine
global comp_choice
player_score = 0
comp_score = 0
main_routine()
