import dice
import user_interface

ui = user_interface.UserInterface()

class CombatSystem:
    """This class provides the methods necessary to run the combat system"""

    def __init__(self, player, monster):
        self.turn_number = 0
        
        self.player = player
        self.player_hit_chance = player.get_hit_chance()
        self.player_damage = player.get_attack_strength()

        self.monster = monster
        self.monster_name = monster.get_name()
        self.monster_health = monster.get_health() # local monster's health
        self.monster_hit_chance = monster.get_hit_chance()
        self.monster_damage = monster.get_attack_strength()
        
        self.gold_reward = monster.get_gold_reward()
        self.xp_reward = monster.get_xp_reward()

    def increase_turn_number(self):
        """Increase the turn count"""
        self.turn_number += 1

    def health_check(self):
        """Checks the health of the player and monster to determine game over"""
        if self.player.get_health() <= 0:
            ui.print_game_over(self.player)
            return False
        
        if self.monster_health <= 0:
            ui.print_player_victory(self.monster_name, self.gold_reward, 
                                    self.xp_reward)
            
            self.player.add_gold(self.gold_reward)
            self.player.add_experience(self.xp_reward)
            return False
        
        return True

    def player_turn(self):
        """The player attacks, and monster defends"""
        ui.clear_screen()
        ui.print_header()

        if dice.roll_d(6) <= self.player_hit_chance:
            print(f"\nYou hit the {self.monster_name} for "
                  f"{self.player_damage} damage!")
            self.monster_health -= self.player_damage
        else:
            print("\nYou missed!")

    def enemy_turn(self):
        """The monster attacks, and the player defends"""
        if dice.roll_d(6) <= self.player_hit_chance:
            print(f"\nThe {self.monster_name} hit you for "
                  f"{self.monster_damage} damage!")
            self.player.take_damage(self.monster_damage)
        else:
            print(f"\nThe {self.monster_name} missed!")

    def fight_or_flight_check(self):
        """Checks if the player wants to continue fighting or run away"""
        
        attack = input(ui.print_combat_options())

        if attack == "r":
            print("\nYou attempt to run away!")
            self.enemy_turn()
            self.health_check()
            return False
        elif attack == "h" and self.player.backpack.total_potions() >= 1:
            self.player.heal_character()
            self.player.backpack.use_potion()
            print("\Your potion healed you for 4 points")

    def enter_combat(self):
        """pick a monster at random and load the combat system"""
        players_turn = True
        combat_active = True

        ui.print_header()
        print(f"\nYou have encountered a {self.monster_name}!"
              " Get ready to fight...")

        while (combat_active == True): 
            # if player or enemy are dead, end combat
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
                self.turn_number += 1
                ui.print_combat_status(self.player.get_health(), 
                                       self.monster_name, 
                                       self.monster_health, 
                                       self.turn_number)
                players_turn = True
            
        print("\n")