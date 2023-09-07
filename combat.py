import dice
import user_interface

ui = user_interface.UserInterface()

class CombatSystem:
    """This class provides the methods necessary to run the combat system"""

    def __init__(self, player, monster):
        self.turn_number = 0
        self.player = player
        self.monster = monster

    def increase_turn_number(self):
        """Increase the turn count"""
        self.turn_number += 1

    def print_turn_number(self):
        """Prints the turn number"""
        print(f"Round {self.turn_number}")

    def health_check(self):
        """Checks the health of the player and monster to determine game over"""
        if self.player.get_health() <= 0:
            ui.print_game_over()
            return False
        
        if self.monster.get_health() <= 0:
            print(f"\nYou have defeated the {self.monster.get_name()},")
            print(f"and earned {self.monster.get_gold_reward()} gold and "
                  f"{self.monster.get_xp_reward()} xp.")
            self.player.add_gold(self.monster.get_gold_reward())
            self.player.add_experience(self.monster.get_xp_reward())
            return False
        
        return True

    def player_turn(self):
        """The player attacks, and monster defends"""
        ui.clear_screen()
        ui.print_header()
        
        if dice.roll_d(6) <= self.player.get_hit_chance():
            print(f"\nYou hit the {self.monster.get_name()} for "
                  f"{self.player.get_attack_strength()} damage!")
            self.monster.take_damage(self.player.get_attack_strength())
        else:
            print("\nYou missed!")

    def enemy_turn(self):
        """The monster attacks, and the player defends"""
        if dice.roll_d(6) <= self.player.get_hit_chance():
            print(f"\nThe {self.monster.get_name()} hit you for "
                  f"{self.monster.get_attack_strength()} damage!")
            self.player.take_damage(self.monster.get_attack_strength())
        else:
            print(f"\nThe {self.monster.get_name()} missed!")

    def print_combat_UI(self):
        ui.print_combatant_health(self.player.get_health(), 
                                  self.monster.get_name(), 
                                  self.monster.get_health()
                                  )
        ui.print_combat_round(self.turn_number)

    def fight_or_flight_check(self):
        """Checks if the player wants to continue fighting or run away"""
        attack = input("\nPress (f) to fight or (r) to try to run away: ")

        if attack == "r":
            print("\nYou attempt to run away!")
            self.enemy_turn()
            self.health_check()
            return False

    def enter_combat(self):
        """pick a monster at random and load the combat system"""
        players_turn = True
        combat_active = True

        ui.print_header()
        print(f"\nYou have encountered a {self.monster.get_name()}!"
              " Get ready to fight...")

        while (combat_active == True): 
            if combat_active != self.health_check():
                break
            elif players_turn:
                if self.fight_or_flight_check() == False:
                    combat_active = False
                    break
                self.player_turn()
                players_turn = False
            else:
                self.enemy_turn()
                self.increase_turn_number()
                self.print_combat_UI()
                players_turn = True
            
        print("\n")