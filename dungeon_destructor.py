import character as char
import monster as m
import combat as cs
import user_interface
import dice

def load_menu(player_selection):
    """Loads the selected menu"""
    if player_selection == '1':
        monster = monsters[dice.roll_d(4)]
        combat_system = cs.CombatSystem(player, monster)
        combat_system.enter_combat()
    elif player_selection == '2':
        ui.print_shop_menu(player)
    elif player_selection == '3':
        ui.print_healer_menu(player)
    elif player_selection == '4':
        # big boss fight
        monster = monsters[5]
        combat_system = cs.CombatSystem(player, monster)
        combat_system.enter_combat()
    else:
        ui.print_main_menu(player)
        player_selection = ui.main_menu_selection()
        load_menu(player_selection)

# load the player, monsters, and UI
player = char.Character('Hero', 'Warrior')
monsters = [m.Orc(), m.Goblin(), m.Bat(), m.Ghost(), m.Werewolf(), m.BigBoss()]
ui = user_interface.UserInterface()

# print the game title screen
ui.print_title_screen()
pause_for_input = input()

# print the main menu
while(True):
    ui.print_main_menu(player)
    player_selection = ui.main_menu_selection()
    load_menu(player_selection)
