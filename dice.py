from random import randint

def roll_d(number_of_sides):
    """Returns a random number between 1 and the number of sides of the dice"""
    return randint(1, number_of_sides)