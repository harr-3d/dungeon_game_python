class Character:
    """A model of a playable character"""

    def __init__(self, character_name, character_class):
        self.name = character_name
        self.character_class = character_class
        self.experience = 0
        self.level = 2
        self.max_health = 10 + (2 * self.level)
        self.current_health = self.max_health
        self.attack_strength = 2
        self.hit_chance = 2
        self.gold = 0

    def get_description(self):
        """Describe the character's basic info"""
        print(f"{self.name} is a level {self.level} {self.character_class}")
    
    def get_gold(self):
        return self.gold
    
    def add_gold(self, amount):
        self.gold += amount

    def get_experience(self):
        return self.experience
    
    def add_experience(self, amount):
        self.experience += amount

    def get_health(self):
        """Returns how much health a player has left"""
        return self.current_health
        
    def take_damage(self, damage):
        """Decreases the player's health"""
        self.current_health -= damage

    def get_hit_chance(self):
        """Returns the chance the player will hit the enemy"""
        return self.hit_chance
    
    def get_attack_strength(self):
        """Returns the player's attack strength"""
        return self.attack_strength

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
