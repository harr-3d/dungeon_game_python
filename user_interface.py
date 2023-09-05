class UserInterface:
    """A set of helpers for formatting the game screen"""
    def print_header(self):
        print("\n*********** >>--> Dungeon Destructor -|--- ***********")

    def print_footer(self):    
        print("******************************************************")

    def print_title_screen(self):
        """Prints the title screen"""
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

    def print_main_menu(self):
        """Prints the main menu"""
        print("\n*********** >>--> Dungeon Destructor -|--- ***********")
        print("\nGreetings Adventurer! Make a selection: ")
        print("(1) Explore the woods")
        print("(2) Visit the shop")
        print("(3) Go to the healer")
        print("(4) Fight the Big Boss! (Level 10 required)")

    def main_menu_selection(self):
        """Solicits a menu selection from the player"""
        selection = input("\nWhere will your journey lead today?"
                          "Enter a number: ")
        return selection
    
    def print_shop_menu(self):
        """Prints a menu for the shop"""
        print("Nothing to buy yet. Go away")
        
    def print_combatant_health(self, player_health, enemy_name, enemy_health):
        """Prints the health of the player and monster"""
        print(f"\nPlayer health: {player_health}    "
              f"{enemy_name} health: {enemy_health}")
        
    def print_combat_round(self, turn):
        """Prints the current combat round"""
        print(f"\n*** End of round {turn} ***")
        
    def print_game_over(self):
        """Prints the title screen"""
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