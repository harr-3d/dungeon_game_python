import dice

class CombatSystem:
    """This class provides the methods necessary to run the combat system"""
    def __init__(self, hit_chance1, damage1, health1,
                 name, hit_chance2, damage2, health2):
        self.turn_number = 0
        self.player_hit_chance = hit_chance1
        self.player_attack_strength = damage1
        self.player_health = health1
        self.enemy_name = name
        self.enemy_hit_chance = hit_chance2
        self.enemy_attack_strength = damage2
        self.enemy_health = health2

    def increase_turn_number(self):
        """Increase the turn count"""
        self.turn_number += 1

    def print_turn_number(self):
        """Prints the turn number"""
        print(f"Round {self.turn_number}")

    def health_check(self):
        """Checks the health of the player and monster to determine game over"""
        if self.player_health <= 0:
            print("You lose. Game Over.")
            return False
        
        if self.enemy_health <= 0:
            print(f"You have defeated the {self.enemy_name}")
            # award xp
            return False
        
        return True

    def player_turn(self):
        """The player attacks, and monster defends"""
        attack = input("<Press any key to attack>")
        if self.enemy_health <= 0:
            return False
        elif dice.roll_d(6) <= self.player_hit_chance:
            print(f"\nYou hit the {self.enemy_name} for "
                  f"{self.player_attack_strength} damage!")
            self.enemy_health -= self.player_attack_strength
        else:
            print("\nYou missed!")

    def enemy_turn(self):
        """The monster attacks, and the player defends"""
        if self.player_health <= 0:
            return False
        elif dice.roll_d(6) <= self.player_hit_chance:
            print(f"\nThe {self.enemy_name} hit you for "
                  f"{self.enemy_attack_strength} damage!")
            self.player_health -= self.player_attack_strength
        else:
            print(f"\nThe {self.enemy_name} missed!")