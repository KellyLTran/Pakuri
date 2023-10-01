
# Imports all the code from the pakuri file into this file
from pakuri import *


# Creates class called Pakudex
class Pakudex:

    # Initializes this object to contain exactly capacity objects when completely full, with a default capacity of 20
    def __init__(self, capacity=20):

        # Creates an empty list
        self.pakuris = []

        # Initializes capacity variable
        self.capacity = capacity

        # Defines self.size to start at 0
        self.size = 0


    # Returns the number of critters currently being stored in the pakudex
    def get_size(self):
        return self.size


    # Returns the number of critters that the pakudex has the capacity to hold at most
    def get_capacity(self):
        return self.capacity


    # Returns a string list containing the species of the critters as ordered in the pakudex
    def get_species_array(self):

        # Returns None if the size is 0, indicating there are no species added yet
        if self.size == 0:
            return None
        else:
            # Creates a new list called pakuri list
            pakuri_list = []

            # Loops through the self.pakuris list to get and add species of pakuri to pakuri_list
            for pakuri in self.pakuris:
                pakuri_list.append(pakuri)
        return pakuri_list


    # Returns an int list containing the attack, defense, and speed statistics of species at indices 0, 1, and 2
    def get_stats(self, species):

        # Returns None if self.size returns None, indicating there are no species added yet
        if self.size == None:
            return None
        stat_data = []

        # Loops through self.pakuris list to append pakuri's attack, defense, and speed values to the new list stat_data
        for pakuri in self.pakuris:

            # Checks if the species is equal to the species that is selected to find and gets its values if so
            if pakuri.get_species() == species:
                stat_data.append(pakuri.get_attack())
                stat_data.append(pakuri.get_defense())
                stat_data.append(pakuri.get_speed())
                return stat_data

        # Returns None if species does not match with any species of the pakuri objects
        return None

    # Sorts the pakuri objects in this pakudex according to Python standard lexicographical ordering of species name
    def sort_pakuri(self):

        # Checks to make sure there are species added
        if self.get_species_array() != None:

            # Sorts based on the key parameter with lambda function to compare each pakuri in list based on their name
            self.pakuris.sort(key=lambda a: a.species)

            '''
            Title: COP3502C - Prog Fundamentals 1 - Fall 2022
            Author: Lisha Zhou
            Date: Nov. 3, 2022
            Code Version: Python
            Availability: https://ufl.zoom.us/rec/play/26sVMfwoVdwhd8NMbM3KjPdVJ_gU0GmRiXyDDqxpA6p9j8jcvElNx8ebws9q2uofIf8p4bd_odPXGlI.LsZPgWsZdbYT_EDG
            '''

    # Adds species to the pakudex; if successful, return True, and False otherwise
    def add_pakuri(self, species):

        # Checks to make sure there are species added to the list
        if self.size != None:

            # Checks for duplicates by looping through each pakuri in list to see if the species matches species input
            for pakuri in self.pakuris:
                if pakuri.species == species:

                    # Returns False as the same species cannot be added to the list, so it is unsuccessful
                    return False

        # Otherwise, the species input is added to the list as a new pakuri by calling the Pakuri class and appending it
        new_pakuri = Pakuri(species)
        self.pakuris.append(new_pakuri)

        # Tracks the size of the list by incrementing self.size by 1 since there is a new pakuri added
        self.size += 1
        return True


    # Evolves species within the pakudex; if successful, return True, and False otherwise
    def evolve_species(self, species):

        # Returns False if self.size returns None since there are no species to evolve
        if self.size == None:
            return False

        # Loops through each pakuri to check
        for pakuri in self.pakuris:

            # Checks if the species is equal to the species that is selected to find and evolves its values if so
            if pakuri.get_species() == species:

                # Calls the evolve function to perform the mathematical operations necessary on the pakuri's stat values
                pakuri.evolve()
                return True

        # Returns false if species is not equal to the species that is entered by user
        return False
