import character as char
import monster as m
import combat as cs
import user_interface
import dice

def load_healer(healing):
    """Loads the healer's shop"""
    if healing == 'y' and player.get_gold() >= 5:
        player.heal_character()
        player.subtract_gold(5)

def load_menu(player_selection):
    """Loads the selected menu"""
    if player_selection == '1':
        monster = monsters[dice.roll_d(4)]
        combat_system = cs.CombatSystem(player, monster)
        combat_system.enter_combat()
    elif player_selection == '2':
        ui.print_shop_menu()
    elif player_selection == '3':
        healing = ui.print_healer_menu()
        load_healer(healing)
    elif player_selection == '4':
        # big boss fight
        pass
    else:
        ui.print_main_menu(player.get_level(),
                        player.get_health(),
                        player.get_max_health(), 
                        player.get_gold(), 
                        player.get_experience(),
                        player.get_xp_for_next_level())
        player_selection = ui.main_menu_selection()
        load_menu(player_selection)

# load the player, monsters, and UI
player = char.Character('Grunnar', 'Druid')
monsters = [m.Orc(), m.Goblin(), m.Bat(), m.Ghost(), m.Werewolf()]
ui = user_interface.UserInterface()

# print the game title screen
ui.print_title_screen()
pause_for_input = input()

# print the main menu
while(True):
    ui.print_main_menu(player.get_level(),
                       player.get_health(),
                       player.get_max_health(), 
                        player.get_gold(), 
                        player.get_experience(),
                        player.get_xp_for_next_level())
    player_selection = ui.main_menu_selection()
    load_menu(player_selection)
