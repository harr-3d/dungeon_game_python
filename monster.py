import dice

class Monster:
    """Models the common features that all monsters share"""

    def __init__(self):
        self.name = "monster"
        self.health = 1
        self.hit_chance = 1
        self.attack_strength = 1
        self.xp_reward = 1
        self.gold_reward = 1

    def get_name(self):
        """Returns the monster's name"""
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
    
    def get_xp_reward(self):
        """How much xp does the player receive for defeating the monster"""
        return self.xp_reward
    
    def get_gold_reward(self):
        """How much gold does the player receive for defeating the monster"""
        return self.gold_reward

class Orc(Monster):
    """A large green monster"""
    def __init__(self):
        self.name = "Orc"
        self.health = 12
        self.hit_chance = 1
        self.attack_strength = 2
        self.xp_reward = 10
        self.gold_reward = dice.roll_d(10)

class Goblin(Monster):
    """A small green monster"""
    def __init__(self):
        self.name = "Goblin"
        self.health = 6
        self.hit_chance = 1
        self.attack_strength = 1
        self.xp_reward = 5
        self.gold_reward = dice.roll_d(3)

class Bat(Monster):
    """A small flying creature"""
    def __init__(self):
        self.name = "Bat"
        self.health = 3
        self.hit_chance = 4
        self.attack_strength = 1
        self.xp_reward = 10
        self.gold_reward = 1

class Ghost(Monster):
    """A spooky undead monster"""
    def __init__(self):
        self.name = "Ghost"
        self.health = 18
        self.hit_chance = 1
        self.attack_strength = 2
        self.xp_reward = 15
        self.gold_reward = dice.roll_d(20)

class Werewolf(Monster):
    """A wolf man, or man wolf. It howls!"""
    def __init__(self):
        self.name = "Werewolf"
        self.health = 16
        self.hit_chance = 3
        self.attack_strength = 1
        self.xp_reward = 20
        self.gold_reward = dice.roll_d(12)

class BigBoss(Monster):
    """A giant with unpleasent habits of personal hygiene..."""
    def __init__(self):
        self.name = "Big Boxx"
        self.health = 42
        self.hit_chance = 4
        self.attack_strength = 3
        self.xp_reward = 2000
        self.gold_reward = dice.roll_d(1000)
