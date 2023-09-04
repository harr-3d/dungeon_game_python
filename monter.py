class Monster:
    """Models the common features that all monsters share"""

    def __init__(self):
        self.name = "monster"
        self.health = 1
        self.attack_strength = 1
        self.xp_reward = 1

    def check_monster_health(self):
        """Prints the monster's current health"""
        print(f"{self.name}'s current health is {self.health}.")

    def damage_dealt(self):
        """Returns the damage done by the monster"""
        return self.attack_strength
    
    def reward_xp(self):
        """How much xp does the player receive for defeating the monster"""


class Orc(Monster):

    def __init__(self):
        self.name = "Orc"
        self.health = 12
        self.attack_strength = 2
        self.xp_reward = 10
