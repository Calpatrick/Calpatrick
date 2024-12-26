define l = Character("Luna")
define s = Character("Steven")

init python:
    import random

    # Base Character Class
    class Character:
        def __init__(self, name, health, attack, strength, intelligence, charisma, constitution):
            self.name = name
            self.health = health
            self.attack = attack
            self.strength = strength
            self.intelligence = intelligence
            self.charisma = charisma
            self.constitution = constitution
            self.cooldowns = {"Superhuman Attack": 0}  # Initialize cooldowns

        def is_alive(self):
            return self.health > 0

        def take_damage(self, damage):
            self.health -= damage
            self.health = max(self.health, 0)

        def deal_damage(self, target):
            damage = random.randint(self.attack - 5, self.attack + 5)
            target.take_damage(damage)
            return damage

        def reset_cooldowns(self):
            for move in self.cooldowns:
                if self.cooldowns[move] > 0:
                    self.cooldowns[move] -= 1

    # Player Class
    class Player(Character):
        def __init__(self, name, health, attack, strength, intelligence, charisma, constitution):
            super().__init__(name, health, attack, strength, intelligence, charisma, constitution)
            self.defending = False

        def superhuman_attack(self, target):
            if self.cooldowns["Superhuman Attack"] == 0:
                damage = self.strength * 7  # Damage scales with Strength stat
                target.take_damage(damage)
                self.cooldowns["Superhuman Attack"] = 5  # Set cooldown
                return f"You used Superhuman Attack on {target.name} for {damage} damage!"
            else:
                return "Superhuman Attack is on cooldown!"

    # Enemy Class
    class Enemy(Character):
        pass

    # Function for the player's action
    def player_turn(action):
        player.reset_cooldowns()  # Reduce cooldowns at the start of each turn

        if action == "Attack":
            damage = player.deal_damage(enemy)
            return f"You attack {enemy.name} for {damage} damage!"
        elif action == "Superhuman Attack":
            return player.superhuman_attack(enemy)
        elif action == "Defend":
            player.defending = True
            return "You brace yourself for the next attack."

    # Function for enemy action
    def enemy_turn():
        if player.defending:
            damage = random.randint(int(enemy.attack * 0.3), int(enemy.attack * 0.7))
            player.defending = False
        else:
            damage = enemy.deal_damage(player)
        player.take_damage(damage)
        renpy.notify(f"{enemy.name} attacks you for {damage} damage!")

# Initialize player and enemy objects
default player = Player("Luna", health=100, attack=20, strength=7, intelligence=3, charisma=4, constitution=6)
default enemy = Enemy("Steven", health=80, attack=10, strength=4, intelligence=2, charisma=2, constitution=5)

# Battle status screen
screen battle_status():
    vbox:
        text "Player Health: [player.health]"
        text "Enemy Health: [enemy.health]"
        if player.cooldowns["Superhuman Attack"] > 0:
            text "Superhuman Attack Cooldown: [player.cooldowns['Superhuman Attack']] turn(s)"
        if not player.is_alive():
            text "You have been defeated!"
        elif not enemy.is_alive():
            text "The enemy has been defeated!"

# Example game starts here
label start:
    scene bg_villageattacked
    show jewel at left
    l "Hi, I'm Luna."
    show goblindicho at right
    s "And I'm Steven."

    label battle:
        "The battle begins!"
        
        # Temporarily override the menu screen
        screen battle_menu:
            frame:
                align (0.5, 0.9)  # Center horizontally, position near the bottom
                has vbox
                for caption, action in items:
                    textbutton caption action action

        while True:
            show screen battle_status
            call screen battle_menu(items=[
                ("Attack", Function(player_turn, "Attack")),
                ("Defend", Function(player_turn, "Defend")),
                ("Superhuman Attack" if player.strength >= 5 else None, Function(player_turn, "Superhuman Attack"))
            ])
            pause 3.0

            if not enemy.is_alive():
                "You defeated [enemy.name]!"
                jump victory

            $ enemy_turn()
            pause 3.0

            if not player.is_alive():
                "[enemy.name] defeated you!"
                jump game_over

label victory:
    "Congratulations! You won the battle!"
    return

label game_over:
    scene black
    with dissolve



    "Game over!"
    return
return