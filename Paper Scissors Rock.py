# Function for main routine that links with each other functions depending on the persons choice.
def main_routine():
    import random
    while comp_score < 3 and player_score < 3:
        global comp_choice
        comp_choice = random.randint(1, 3) # Computer randomly choosing from the three numbers each number being 1:Paper, 2:Scissors, 3:Rock
        print("<================================================>")
        print(f"Hello {player_name}")
        print("Choose one of the options below:")
        # Giving the player a choice between Paper, Scissors, and Rock
        print("1: Paper")
        print("2: Scissors")
        print("3: Rock")
        print("<================================================>")
        choice = int(input("Enter your choice from 1-3:"))
        # Cooperating with each of the other functions
        if choice == comp_choice:
            game_tie()

        elif choice == 1:
            paper()

        elif choice == 2:
            scissors()

        elif choice == 3:
            rock()
        else:
            # Going back to the main routine if the player didn't input a number from 1-3.
            print("That number is invalid")
            print("Please choose again from numbers 1-3.")
    else:
        game_over()
        # Going to the game over function if someone reaches the score of 3.


def game_tie():
    # Output for if the score was a tie
    print("<================================================>")
    print(f"Tricky game {player_name}")
    print("The result of the game was a tie.")
    print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


# Function that runs if the player chose paper.
def paper():
    global comp_score
    global player_score
    if comp_choice == 2:
        comp_score += 1
        # Output for if the computer won the game and adding a point to the computer
        print("<================================================>")
        print(f"Hard luck {player_name}")
        print("The computer is the winner of this game.")
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")

    else:
        player_score += 1
        # Output for if the player won the game and adding a point to the player
        print("<================================================>")
        print(f"Congratulations {player_name}")
        print("You are the winner of this game.")
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


# Function that runs if the player chose scissors
def scissors():
    global comp_score
    global player_score
    if comp_choice == 3:
        comp_score += 1
        # Output for if the computer won the game and adding point to the computer
        print("<================================================>")
        print(f"Hard luck {player_name}")
        print("The computer is the winner of this game.")
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")

    else:
        player_score += 1
        # Output for if the player won the game and adding a point to the player
        print("<================================================>")
        print(f"Congratulations {player_name}")
        print("You are the winner of this game.")
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


# Function that runs if the player chose rock
def rock():
    global comp_score
    global player_score
    if comp_choice == 1:
        comp_score += 1
        # Output for if the computer won the game and adding a point to the computer
        print("<================================================>")
        print(f"Hard luck {player_name}")
        print("The computer is the winner of this game.")
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")

    else:
        player_score += 1
        # Output for if the player won the game and adding a point to the player
        print("<================================================>")
        print(f"Congratulations {player_name}")
        print("You are the winner of this game.")
        print(f"The current score is Player Score:{player_score}, Computer Score:{comp_score}")


# Function that runs after someone had reached the score of 3.
def game_over():
    global comp_score
    global player_score
    if comp_score == 3:
        # Output for if the computer won the game and asking the player for a rematch
        print("The computer is the winner of this match!")
        rematch = input("Do you want a rematch(Y: yes, N: no): ").upper()
        if rematch == "Y":
            comp_score = 0
            player_score = 0
            main_routine()
        else:
            print("Thank you for playing Paper Scissors Rock")
    elif player_score == 3:
        # Output for if the player won the game and asking the player for a rematch
        print("You are the winner of this match!")
        rematch = input("Do you want a rematch(Y: yes/(any other key to quit)): ").upper()
        if rematch == "Y":
            comp_score = 0
            player_score = 0
            main_routine()
        else:
            print("Thank you for playing Paper Scissors Rock")


# Main Routine
# Welcome screen
print("<================================================>")
print("Welcome to Paper Scissors Rock")
print("You will be versing against a computer.")
print("Whoever gets 3 games first will be the final winner!")
player_name = input("Please enter your name:").title()
global comp_choice
player_score = 0
comp_score = 0
main_routine()
