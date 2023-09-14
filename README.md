# dungeon_game_python

This text based dungeon game is meant to be played in the terminal. This is a 
personal project.

## Installation

To run the game, download the files to a single folder, and run 
"dungeon_destructor.py" in the terminal to begin the game.

## Updates

- 9.14.2023 Final update. Pending additional testing, the game is complete.
  It is strongly recommended that the player reach level 10, and upgrade both
  sword and shield multiple times before attempting to fight the big boss.

- 9.14.2023 Added strength and consitution abilities to modify damage
  and health for the player

- 9.14.2023 Fixed death screen. Added revive option with xp/gold penalty

- 9.13.2023 Added a combat summary after victory

- 9.13.2023 Added clear() function to windows as well as mac/linux

- 9.13.2023 Added ability to fight big boss at any level, level 10 advised

- 9.12.2023 Added sword and shields to combat.py and user_interface.py

- 9.12.2023 Added sword_level and shield_level to backpack.py

- 9.12.2023 Removed old named sword and shield system

- 9.12.2023 Added the shop

- 9.12.2023 Fixed an error with the combat turns always showing 0

- 9.12.2023 Added a backpack to character.py

- 9.12.2023 Added potion helper functions to backpack.py

- 9.12.2023 Added potion functionality to combat.py

- 9.12.2023 Cleaned up control flow in dungeon_destructor.py for readability

- 9.12.2023 Monster health is now stored in a local variable in combat.py,
  meaning the player can fight a monster more than once

- 9.12.2023 Removed print_turn_number() from combat.py. It is part of the UI

- 9.12.2023 Simplified most function calls to run once in combat.py 
  when the CombatSystem class is initiated

- 9.6.2023 Added xp system that determines level and health

- 9.6.2023 Added healer and ability to spend gold

- 9.6.2023 Added ability to flee in combat, while enemy gets one more hit

- 9.6.2023 Added screen clear between selections for a cleaner user experience

- 9.6.2023 Added level, health, gold, and xp to main menu

- 9.6.2023 Add backpack
