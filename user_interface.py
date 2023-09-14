import os

class UserInterface:
    """A set of helpers for formatting the game screen"""
    def clear_screen(self):
        """Clear the game screen"""
        if os.name == 'nt':
            os.system('cls') # windows
        else:
            os.system('clear') # mac/linux

    def pause_for_input(self):
        """Ask the player to press any key to continue"""
        return input("\nPress any key to continue...")

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
        print(f"\nSword Level: {player.backpack.get_sword_level()}"
              f"    Shield Level: {player.backpack.get_shield_level()}"
              f"    Potions: {player.backpack.total_potions()}")
        print("\nGreetings Adventurer! Make a selection: ")
        print("\n(1) Explore the woods")
        print("(2) Visit the shop")
        print("(3) Go to the healer")
        print("(4) Fight the Big Boss! (Warning: player level 10 advised...)")
        

    def main_menu_selection(self):
        """Solicits a menu selection from the player"""
        selection = input("\nWhere will your journey lead today?"
                          " Enter a number: ")
        return selection
    
    def print_shop_menu(self, player):
        """Prints a menu for the shop"""
        self.clear_screen()
        self.print_header()

        print("\nGreetings Warrior. What items do you require?")
        print("\n (1) Upgrade your sword +2 damage dealt: 50 gold")
        print("\n (2) Upgrade your shield +4 max health: 50 gold")
        print("\n (3) A potion of healing: 5 gold")
        print("\n (4) Leave the shop")
    
        selection = input("\nLet me know: ")

        if selection == '1' and player.get_gold() >= 50:
            player.subtract_gold(50)
            player.backpack.upgrade_sword()
            print("\nThat steel will cut deep now, Champion.")
        elif selection == '2' and player.get_gold() >= 50:
            player.subtract_gold(50)
            player.backpack.upgrade_shield()
            player.heal_character(4)
            print("\nThat's a fine shield now, Warrior.")
        elif selection == '3' and player.get_gold() >= 5:
            player.subtract_gold(5)
            player.backpack.add_potion()
            print("\nHere you are, another potion")
        elif selection == '4':
            pass
        elif player.get_gold() < 5:
            print("\nYou don't have enough gold to shop here.")
            self.pause_for_input()
        else:
            print("\nI didn't understand. Try again.")
            self.pause_for_input()
            self.print_shop_menu(player)
        
        

    def print_healer_menu(self, player):
        """Prints a menu for the healer, and allows the player to heal"""
        self.clear_screen()
        print("\nYou seem unwell. Are you in need of healing for 5 gold?")
        healing = input("\n(y) for yes, (n) for no: ")

        if healing == 'y' and player.get_gold() >= 5:
            player.heal_character()
            player.subtract_gold(5)
        elif healing == 'y' and player.get_gold() < 5:
            print("\nNot enough gold for healing. You should have ducked.")
        elif healing == 'n':
            exit
        else:
            print("\nI'm not sure what you said.")
            self.pause_for_input()
            self.print_healer_menu(player)

        

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
        self.pause_for_input()

    def print_player_revive(self, gold, xp):
        """Print that the player has been revived and details the penalty"""
        print(f"\nYou have been revived,")
        print(f"but it cost you {xp} xp and {gold} gold...")
        self.pause_for_input()
              
    def print_game_over(self, player):
        """Prints the game over screen"""
        self.clear_screen()

        # calculate the gold and experience penalty of reviving
        gold = player.get_gold() * 0.1
        gold = round(gold)
        gold = int(gold)

        xp = player.get_experience() * 0.1
        xp = round(xp)
        xp = int(xp)

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
        print(f"\nWant to revive? It costs {gold} gold and {xp} xp points...")
        
        selection = input("\n(y) for yes    (n) for no: ")

        if selection == 'y':
            self.clear_screen()

            gold = player.get_gold() * 0.1
            gold = round(gold)
            gold = int(gold)

            xp = player.get_experience() * 0.1
            xp = round(xp)
            xp = int(xp)

            player.penalize_gold(gold)
            player.penalize_xp(xp)
            player.heal_character()
            
            self.print_player_revive(gold, xp)
        elif selection == 'n':
            exit()
        else:
            self.print_game_over(player)