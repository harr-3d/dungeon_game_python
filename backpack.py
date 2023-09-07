class Backpack:
    """A model of a backpack to hold player inventory"""
    def __init__(self):
        self.sword = ""
        self.shield = ""
        self.potions = 1

    def list_contents(self):
        """Print the contents of the backpack"""
        print("\nThe backpack contains: ")
        if self.sword != "":
            print(f"- A {self.sword}")
        if self.shield != "":
            print(f"- A {self.shield}")
        print(f"- {self.potions} potions")

    def add_potion(self):
        """Add a potion to the backpack's inventory"""
        self.potions += 1

    def add_sword(self, new_sword):
        """Add a sword to the backpack"""
        self.sword = new_sword

    def add_shield(self, new_shield):
        """Add a sword to the backpack"""
        self.shield = new_shield
