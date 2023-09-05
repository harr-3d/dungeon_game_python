import character as char
import monster as m
import combat as cs
import user_interface
import dice

def enter_combat():
# if selection (1), pick a monster at random and load the combat system
    monster = monsters[dice.roll_d(4)]

    # combat_system = cs.CombatSystem(
    #     player.get_hit_chance(), 
    #     player.get_attack_strength(),
    #     player.get_health(),
    #     monster.get_name(),
    #     monster.get_hit_chance(),
    #     monster.get_attack_strength(),
    #     monster.get_health(),
    #     monster.get_gold_reward(),
    #     monster.get_xp_reward()
    #     )

    combat_system = cs.CombatSystem(player, monster)

    players_turn = True
    combat_active = True

    ui.print_header()
    print(f"You have encountered a {monster.get_name()}! Get ready to fight...")

    # gameplay loop - think of this as the update loop in Unity
    while (combat_active == True): 
        if combat_active != combat_system.health_check():
            break
        elif players_turn:
            combat_system.player_turn()
            players_turn = False
        else:
            combat_system.enemy_turn()
            players_turn = True
        
    print("\n")
    print(f"{player.get_experience()}")

def load_menu(player_selection):
    """Loads the selected menu"""
    if player_selection == '1':
        enter_combat()
    elif player_selection == 2:
        ui.print_shop_menu()
    elif player_selection == 3:
        # healer
        pass
    elif player_selection == 4:
        # big boss fight
        pass
    else:
        ui.print_main_menu()
        player_selection = ui.main_menu_selection()
        load_menu(player_selection)

# load the player, monsters, and UI
player = char.Character('Grunnar', 'Druid')
monsters = [m.Orc(), m.Goblin(), m.Bat(), m.Ghost(), m.Werewolf()]
ui = user_interface.UserInterface()

# print the game title screen
ui.print_title_screen()

# print the main menu
ui.print_main_menu()
player_selection = ui.main_menu_selection()
load_menu(player_selection)






