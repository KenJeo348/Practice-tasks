fun_in_the_sun_list = []
active_kidz_list = []


# This function runs the main routine and sends and receives data from other functions
def main_routine():
    choice = 0
    while choice != 3:
        print("<=============================================>")
        print("Welcome to Kidz Fun")
        print("Please choose one of the below options:")
        print("<=============================================>")
        # Choosing between which function to go to.
        print("1: Apply kid to Fun in the Sun")
        print("2: Apply kid to Active Kidz")
        print("3: Exit the system to complete calculation")
        print("<=============================================>")
        choice = int(input("Enter your choice from number 1-3: "))

        if choice == 1:
            fun_in_the_sun()

        elif choice == 2:
            active_kidz()

        elif choice == 3:
            exit_system()
# Going back to the main program if the number is invalid
        else:
            print("Please enter a valid number")
            main_routine()


# Checking if the user wants to apply to the Fun in the Sun program, and asking the age of their child if they do (otherwise go back to the main program)
def fun_in_the_sun():
    print("")
    print("?:::::::::::::::::::::::::::::::::::::::::::::?")
    check = input("Do you want to apply your child to the Fun in the Sun program? (Y:Yes/N:No):").upper()
    if check == "Y":
        child_age = int(input("How old is your child?: "))
        if child_age > 15 or child_age < 5:
            print("Sorry this program is only for children aged 5 - 15 years old")
        else:
            fun_in_the_sun_list.append(child_age)
    else:
        main_routine()


# Checking if the user wants to apply to the Active Kidz program, and asking the age of their child if they do (otherwise go back to the main program)
def active_kidz():
    print("")
    print("?:::::::::::::::::::::::::::::::::::::::::::::?")
    check = input("Do you want to apply your child to the Active Kidz program? (Y:Yes/N:No):").upper()
    if check == "Y":
        child_age = int(input("How old is your child?: "))
        if child_age > 15 or child_age < 5:
            print("Sorry this program is only for children aged 5 - 15 years old")
        else:
            active_kidz_list.append(child_age)
    else:
        main_routine()


# Checking if the user wants to exit the program, and if they do telling them the total number and average kids in each program. (otherwise go back to the main program)
def exit_system():
    check = input("Are you sure you want to exit the program (Y:Yes/N:No):").upper()
    if check == "N":
        main_routine()
    elif check == "Y":
        if len(fun_in_the_sun_list) == 0:
            print("There are currently no children applied to the Fun in the Sun Program")
        else:
            print("<===================================================================>")
            print(f"In the Fun in the Sun program the sum of the ages is: {sum(fun_in_the_sun_list)} years old")
            print(f"The average age in the Fun in the Sun program is {(sum(fun_in_the_sun_list)/len(fun_in_the_sun_list)):.0f} years old")
        if len(active_kidz_list) == 0:
            print("There are currently no children applied to the Active Kidz Program")
        else:
            print("<===================================================================>")
            print(f"In the Active Kidz the sum of the ages is: {sum(active_kidz_list)} years old")
            print(f"The average of the age in the Active Kidz program is {(sum(active_kidz_list)/len(active_kidz_list)):.0f} years old")


# Main Routine
main_routine()
