def main_routine():
    choice = 0
    comp_choice = 0
    choice_list = [1, 2, 3]
    print("Welcome to Paper Scissors Rock")
    player_name = input("Enter your name: ")
    print(f"Hello {player_name} choose one of the options below: ")
    global comp_choice
    comp_choice = random.choice(choice_list)
    print("1: Paper")
    print("2: Scissors")
    print("3: Rock")
    choice = int(input("Enter your choice from number 1-3: "))

    if choice == 1:
        paper()

    if choice == 2:
        scissors()

    if choice == 3:
        rock()




def paper():
    if comp_choice == 1:
        print("The computer did paper: Tie")
    elif comp_choice == 2:
        print("The computer did scissors: Loss")
    else:
        print("The computer did rock: Win")


def scissors():
    print("Scissors")


def rock():
    print("Rock")


# Main Routine
import random
main_routine()
