import experience, backpack, ability_roll, math

xp_calculator = experience.ExperienceLevel()

class Character:
    """A model of a playable character"""

    def __init__(self, character_name, character_class):
        self.name = character_name
        self.character_class = character_class
        
        self.experience = 1
        self.level = xp_calculator.level_check(self.experience)
        
        # this could just be a single d6 roll, but this does it the D&D way
        self.health_bonus = ability_roll.roll_four_d6() / 3
        self.max_health = 6 + math.floor(self.health_bonus) * 2 * self.level
        self.current_health = self.max_health
        
        self.attack_bonus = ability_roll.roll_four_d6() / 3
        self.attack_strength = 2 + math.floor(self.attack_bonus)
        self.hit_chance = 2
        
        self.gold = 10
        self.backpack = backpack.Backpack()

    def get_description(self):
        """Describe the character's basic info"""
        print(f"{self.name} is a level {self.level} {self.character_class}")

    def get_gold(self):
        """Returns the player's gold total"""
        return self.gold
    
    def add_gold(self, amount):
        """Adds to the player's gold total"""
        self.gold += amount

    def subtract_gold(self, amount):
        """Subtract from the player's gold total"""
        self.gold -= amount

    def penalize_gold(self, amount):
        """Decreases gold by 10%"""
        self.gold = self.gold - amount
    def get_experience(self):
        """Returns the player's current xp points"""
        return self.experience
    
    def penalize_xp(self, amount):
        """Decreases XP by 10%"""
        self.experience = self.experience - amount
    
    def get_xp_for_next_level(self):
        """Returns the player's next level goal"""
        return self.level * 100

    def get_level(self):
        """Returns the player's level"""
        return self.level
    
    def add_experience(self, amount):
        """Adds to the player's xp points"""
        self.experience += amount
        self.level = xp_calculator.level_check(self.experience)
        self.max_health = 6 + 6 * self.level
        print(f"\nCurrent Level: {self.level}")

    def get_health(self):
        """Returns how much health a player has left"""
        return self.current_health
    
    def get_max_health(self):
        """Returns the player's max health"""
        return self.max_health + self.backpack.get_shield_level()
        
    def take_damage(self, damage):
        """Decreases the player's health"""
        self.current_health -= damage

    def get_hit_chance(self):
        """Returns the chance the player will hit the enemy"""
        return self.hit_chance
    
    def get_attack_strength(self):
        """Returns the player's attack strength"""
        return self.attack_strength  + self.backpack.get_sword_level()

    def get_total_damage(self):
        """Returns total damage the player has taken"""
        return self.max_health - self.current_health

    def heal_character(self, amount=0):
        """
        Heals the character for the given amount, or
        returns the player to max health if no amount is specified
        """
        if amount != 0:
            self.current_health += amount
        else:
            self.current_health = self.max_health
