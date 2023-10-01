
# Imports all the code from the pakudex file into this file
from pakudex import *


# Defines variables user_selection and input_capacity
user_selection = 0
input_capacity = 0

# Sets pakudex_continue to False
pakudex_continue = False
print("Welcome to Pakudex: Tracker Extraordinaire!")

# Creates a while loop with a try-except block
while pakudex_continue == False:

    # Converts user input to integer, which raises a Value Error input is not only numbers
    try:
        input_capacity = int(input("Enter max capacity of the Pakudex: "))

        # Raises ValueError except statement if user input is a negative integer
        if input_capacity < 0:
            raise ValueError

        # With no error, the program can exit the while loop and continue
        else:
            pakudex_continue = True

    # Value error is handled by the except statement and displays a message to user
    except ValueError:
        print("Please enter a valid size.")

# Formats to put user input into the display message
print(f"The Pakudex can hold {input_capacity} species of Pakuri.")

# Assigns user input to the capacity variable in the Pakudex class
pakudex = Pakudex(capacity=input_capacity)


'''
Title: Chapter 6: Software Engineering - Exceptions
Author: Yasaman Adibi, et al.
Date: n.d.
Code Version: Python
Availability: https://learn.zybooks.com/zybook/UFLCOP3502CFall2022/chapter/6/section/1
'''


# Creates a while loop to continue until the user inputs option 6
while user_selection != "6":
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")

    user_selection = input("\nWhat would you like to do? ")


    if user_selection == "1":

        # Calls the get_species_array function from the pakudex class
        pakuri_list = pakudex.get_species_array()

        # Displays a message to user if the list is empty with no Pakuri elements in it
        if pakuri_list == None:
            print("No Pakuri in Pakudex yet!")

        # Otherwise, the list is formatted with its species to display to the user
        else:

            # Sets index position to 1 so that the printed list starts with "1." rather than "0."
            index = 1
            print("Pakuri In Pakudex:")

            # Loops through each pakuri in pakuri_list to correctly format it for display
            for pakuri in pakuri_list:
                # Prints the list by getting the specie's designated index position number and the species name
                print(str(index) + '.', str(pakuri.get_species()))

                # index position increments by 1 as the program loops through the list
                index += 1


    elif user_selection == "2":
        species = str(input("Enter the name of the species to display: "))

        # Passes the species user entered through get_stats function from the pakudex class
        stat_data = pakudex.get_stats(species)

        # Displays an error message if there are no species added to the list
        if stat_data == None:
            print("Error: No such Pakuri!")

        # Otherwise, the stats are formatted for display
        else:
            print("\nSpecies:", species)

            # Index positions are used to get the correct value in the stat_data list for its designated label
            print("Attack:", stat_data[0])
            print("Defense:", stat_data[1])
            print("Speed:", stat_data[2])


    elif user_selection == "3":

        # Displays an error message if the size of the pakudex is equal to or greater than the assigned max capacity
        if pakudex.get_size() >= pakudex.get_capacity():
            print("Error: Pakudex is full!")

        else:
            species_add = input("Enter the name of the species to add: ")

            # Passes the species user entered through the add_pakuri function from the pakudex class
            # If the function returns False, an error message is displayed to prevent duplicates in the list
            if pakudex.add_pakuri(species_add) == False:
                print("Error: Pakudex already contains this species!")

            # Otherwise, the function works, the species is added, and a message with the species name is displayed
            else:
                print(f"Pakuri species {species_add} successfully added!")


    elif user_selection == "4":
        species_evolve = input("Enter the name of the species to evolve: ")

        # Passes the species user entered through the evolve_species function from the pakudex class
        # If the function returns False, an error message is displayed when no species are in the list
        if pakudex.evolve_species(species_evolve) == False:
            print("Error: No such Pakuri!")

        # Otherwise, the function works, the species is evolved, and a message with the species name is displayed
        else:
            print(f"{species_evolve} has evolved!")


    # Calls the sort_pakuri function from the pakudex class to sort the pakuris when user selects option 5
    elif user_selection == "5":
        pakudex.sort_pakuri()
        print("Pakuri have been sorted!")


    # Displays a goodbye message and exits the program when user selects option 6
    elif user_selection == "6":
        print("Thanks for using Pakudex! Bye!")
        exit()

    # Anything other than the option numbers displays a message to let the user know it is not part of the menu options
    else:
        print("Unrecognized menu selection!")
