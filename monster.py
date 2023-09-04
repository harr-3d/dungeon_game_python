class Monster:
    """Models the common features that all monsters share"""

    def __init__(self):
        self.name = "monster"
        self.health = 1
        self.hit_chance = 1
        self.attack_strength = 1
        self.xp_reward = 1

    def get_name(self):
        return self.name

    def get_health(self):
        """Returns the monster's current health"""
        return self.health
    
    def get_hit_chance(self):
        """Returns the monster's chance to hit the player"""
        return self.hit_chance

    def get_attack_strength(self):
        """Returns the damage done by the monster"""
        return self.attack_strength
    
    def take_damage(self, amount):
        self.health -= amount
    
    def reward_xp(self):
        """How much xp does the player receive for defeating the monster"""


class Orc(Monster):

    def __init__(self):
        self.name = "Orc"
        self.health = 12
        self.hit_chance = 1
        self.attack_strength = 2
        self.xp_reward = 10
