# I was confused in where to put this thing?
dog_list = []


# This function runs the main routine and sends and receives data from other functions
def main_routine():
    choice = 0
    while choice != 5:
        print("<============================================>")
        print("Welcome To DogsRus")
        print("Please choose one of the below options:")
        # Choosing between which function to go to.
        print("<============================================>")
        print("1: Drop off a dog.")
        print("2: Pick up a dog.")
        print("3: Calculate the Cost.")
        print("4: Check dogs currently staying.")
        print("5: Exit system.")
        print("<============================================>")
        choice = int(input("Enter your choice from number 1 - 5:"))

        if choice == 1:
            drop_off()

        elif choice == 2:
            pick_up()

        elif choice == 3:
            calc_cost()

        elif choice == 4:
            check_dog()

        elif choice == 5:
            exit_system()
# Going back to the main program if the number is invalid
        else:
            print("")
            print("Please enter a valid Number!")
            print("")
            main_routine()


# A function that asks if the user wants to drop off a dog and if so they can input their dogs name into a list.
def drop_off():
    print("")
    print("?=================================?")
    check = input("Are you sure you want to drop off a dog?(Y:Yes/N:No)").upper()
    if check == "Y":
        dog_name = input("Enter your Dog's name:")
        print(f"You have successfully checked {dog_name} in to the system")
        print("")
        dog_list.append(dog_name)
    else:
        main_routine()


# A function that asks if the user wants to pick up a dog and if so they can take out a dogs name from a list.
def pick_up():
    print("")
    print("?=================================?")
    check = input("Are you sure you want to drop off a dog?(Y:Yes/N:No)").upper()
    if check == "Y":
        dog_name = input("Enter your Dog's name:")
        print("")
        check = dog_name in dog_list
        if check is False:
            print("We couldn't find that name in our system please try again")
            print("")
        else:
            dog_list.remove(dog_name)
            print(f"You have successfully checked {dog_name} out of the system")
            print("")
    else:
        main_routine()


# Calculating the price for dropping off a dog for a certain number of days
def calc_cost():
    daily_price = 22.5
    print("")
    print("?=================================?")
    day_length = int(input("How many days do you want to leave your dog with us:"))
    print("")
    print(f"For {day_length} day/s you will have to pay ${day_length * daily_price:.2f} Dollars")
    print("")


# Printing the current dogs staying at the shelter
def check_dog():
    if len(dog_list) == 0:
        print("")
        print("There are currently no dogs staying at our boarding house.")
        print("")
    else:
        print("")
        print("The current dogs that are staying at our boarding house are:")
        for dogs in dog_list:
            print("")
            print(dogs)
            print("")


# Exiting the system
def exit_system():
    print("You exited out of the system")


# Main Routine
main_routine()
