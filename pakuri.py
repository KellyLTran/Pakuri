
# Creates class called Pakuri
class Pakuri:

    # Initializes the Pakuri object with species attribute
    def __init__(self, species):
        self.species = species

        # Assigns appropriate equations to each attribute
        self.attack = (len(self.species) * 7) + 9
        self.defense = (len(self.species) * 5) + 17
        self.speed = (len(self.species) * 6) + 13


    # Getter functions retrieve the attribute values
    # Returns the species of this critter
    def get_species(self):
        return self.species


    # Returns the attack value for this critter
    def get_attack(self):
        return self.attack


    # Returns the defense value for this critter
    def get_defense(self):
        return self.defense


    # Returns the speed of this critter
    def get_speed(self):
        return self.speed


    # Changes the attack value for this critter to new_attack;  # setter: update the attribute's value
    def set_attack(self, new_attack):
        self.attack = new_attack


    # Evolves the critter by doubling the attack, quadrupling the defense, and tripling the speed
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3


'''
Title: Chapter 7: Classes & Inheritance
Author: Yasaman Adibi, et al.
Date: n.d.
Code Version: Python
Availability: https://learn.zybooks.com/zybook/UFLCOP3502CFall2022/chapter/7/section/1
'''
