label combat:
    narrator "You are now facing a goblin!"

    while player_health > 0 and enemy_health > 0:
        menu:
            "Attack the enemy":
                $ damage = renpy.random.randint(5, player_attack)
                $ enemy_health -= damage
                narrator "You deal [damage] damage to the enemy."
            
            "Defend yourself":
                $ reduced_damage = max(0, enemy_attack - renpy.random.randint(3, 7))
                $ player_health -= reduced_damage
                narrator "You brace yourself, reducing the damage taken to [reduced_damage]."
            
            "Use a healing potion":
                if "healing_potion" in player_choices:
                    $ heal = renpy.random.randint(10, 20)
                    $ player_health += heal
                    $ player_choices.remove("healing_potion")
                    narrator "You use a healing potion and restore [heal] health."
                else:
                    narrator "You don't have any healing potions left!"
            
        # Enemy's turn
        if enemy_health > 0:
            $ damage = renpy.random.randint(5, enemy_attack)
            $ player_health -= damage
            narrator "The enemy attacks, dealing [damage] damage to you."

        # Display stats
        narrator "Your Health: [player_health] | Enemy Health: [enemy_health]"

    # Determine outcome
    if player_health > 0:
        narrator "You have defeated the enemy!"
        jump victory
    else:
        narrator "You have been defeated!"
        jump game_over
