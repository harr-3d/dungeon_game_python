import character as char
import monster as m
import combat as cs

player = char.Character('Grunnar', 'Druid')
orc = m.Orc()
combat_system = cs.CombatSystem(
    player.get_hit_chance(), 
    player.get_attack_strength(),
    player.get_health(),
    orc.get_name(),
    orc.get_hit_chance(),
    orc.get_attack_strength(),
    orc.get_health()
    )

players_turn = True
combat_active = True

print("\nYou see an Orc charging towards you, sword held high!")

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