import os

class UserInterface:
    """A set of helpers for formatting the game screen"""
    def clear_screen(self):
        """Clear the game screen"""
        os.system('clear') # developed on a mac

    def print_header(self):
        """Print the game header"""
        self.clear_screen()
        print("\n*********** >>--> Dungeon Destructor -|--- ***********")

    def print_footer(self):
        """Print the game footer"""    
        print("******************************************************")

    def print_title_screen(self):
        """Prints the title screen"""
        self.clear_screen()
        print("\n******************************************************")
        print("*                                                    *")
        print("*                                                    *")
        print("*                  ||                                *")
        print("*              O===||=================>              *")
        print("*                  ||                                *")
        print("*                                                    *")
        print("*                 Dungeon Destructor                 *")
        print("*                                                    *")
        print("*                 <press any key>                    *")
        print("*                                                    *")
        print("******************************************************")

    def print_main_menu(self, player):
        """Prints the main menu"""
        level = player.get_level()
        health = player.get_health()
        max_health = player.get_max_health()
        gold = player.get_gold()
        xp = player.get_experience()
        next_xp = player.get_xp_for_next_level()

        self.clear_screen()
        print("\n*********** >>--> Dungeon Destructor -|--- ***********")
        print(f"\nLevel: {level}    health: {health} / {max_health}"
              f"    gold: {gold}    xp: {xp} / {next_xp}")
        print("\nGreetings Adventurer! Make a selection: ")
        print("\n(1) Explore the woods")
        print("(2) Visit the shop")
        print("(3) Go to the healer")
        print("(4) Fight the Big Boss! (Level 10 required)")

    def main_menu_selection(self):
        """Solicits a menu selection from the player"""
        selection = input("\nWhere will your journey lead today?"
                          " Enter a number: ")
        return selection
    
    def print_shop_menu(self):
        """Prints a menu for the shop"""
        self.clear_screen()
        print("Nothing to buy yet. Go away")
        pause_for_input = input("(press any key to continue)")

    def print_healer_menu(self, player):
        """Prints a menu for the healer, and allows the player to heal"""
        self.clear_screen()
        print("\nYou seem unwell. Are you in need of healing for 5 gold?")
        healing = input("\n(y) for yes, (n) for no: ")

        if healing == 'y' and player.get_gold() >= 5:
            player.heal_character()
            player.subtract_gold(5)
        elif healing == 'y' and player.get_gold() < 5:
            print("Not enough money")

    def print_combat_status(self, player_health, enemy_name, enemy_health,
                            turn):
        """Prints the health of the combatants and the round number"""
        print(f"\nPlayer health: {player_health}    "
              f"{enemy_name} health: {enemy_health}")
        
        print(f"\n*** End of round {turn} ***")
        
    def print_combat_options(self):
        """Prints the player's choices in combat"""
        return "\nWhat do you do? (f)ight, (r)un, (h)ealth potion: "

    def print_player_victory(self, monster, gold, xp):
        """Print that the player defeated the monster, and the rewards"""
        print(f"\nYou have defeated the {monster},")
        print(f"and earned {gold} gold and {xp} xp.")
    
    def print_game_over(self):
        """Prints the game over screen"""
        self.clear_screen()

        print("\n******************************************************")
        print("*                                                    *")
        print("*                 =======       ==================   *")
        print("*                =       =     =                  =  *")
        print("*              =           =   =     GAME OVER    =  *")
        print("*              =   X   X   =   =                  =  *")
        print("*              =           =    = ================   *")
        print("*                =  |  |  =                          *")
        print("*            =   ====  ===   =                       *")
        print("*           =   =====  ====   =                      *")
        print("*          =   ======  =====   =                     *")
        print("*                                                    *")
        print("******************************************************")