class Backpack:
    """A model of a backpack to hold player inventory"""
    def __init__(self):
        self.sword_level = 0
        self.shield_level = 0
        self.potions = 5

    def add_potion(self):
        """Add a potion to the backpack's inventory"""
        self.potions += 1

    def use_potion(self):
        """Subtract a potion if there is at least one potion"""
        if self.potions >= 1:
            self.potions -= 1

    def total_potions(self):
        """How many potions does the player have?"""
        return self.potions

    def upgrade_sword(self):
        """Upgrade the sword's level"""
        self.sword_level += 2

    def upgrade_shield(self):
        """Upgrade the shield's level"""
        self.shield_level += 4

    def get_sword_level(self):
        """Returns the sword level"""
        return int(self.sword_level)

    def add_shield(self):
        """Add a sword to the backpack"""
        self.shield_level += 1

    def get_shield_level(self):
        """Returns the shield level"""
        return int(self.shield_level)