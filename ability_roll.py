"""A Simple Tool to Roll D&D Style Ability Scores"""
from random import randint

# build a dictionary of the character's ability scores
abilities = {
    'Strength' : 0, 
    'Dexterity' : 0, 
    'Constitution' : 0, 
    'Intelligence' : 0, 
    'Wisdom' : 0,
    'Charisma' : 0,
    }

def remove_lowest_value(values):
        """sorts a list and removes the lowest value"""
        values = sorted(values)
        
        values.reverse()
        values.pop()
        
        return values

def roll_four_d6():
    """roll four six sided dice, and return the sum of the 3 highest rolls"""
    # create the list
    rolls = [0, 0, 0, 0]
    
    # roll the dice and populate the list
    for value in range(0, 4):
        rolls[value] = randint(1, 6)

    # return the sum of the 3 highest rolls
    return sum(remove_lowest_value(rolls))

# assign the sum of the 3 highest dice rolls to each ability score
for key, value in abilities.items():
    value = roll_four_d6()
    print(f"{key}: {value}")
    
