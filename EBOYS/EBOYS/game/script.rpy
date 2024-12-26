default knowledge = 0
default charm = 0
default guts = 0
default strength = 0
default dexterity = 0

# Initialize variables
init python:
    def increase_attribute (attribute, amount=1):
        global knowledge, charm, guts, strength, dexterity
        if attribute == "knowledge":
            knowledge += amount
        elif attribute == "charm":
            charm += amount
        elif attribute == "guts":
            guts += amount
        elif attribute == "strength":
            strength += amount
        elif attribute == "dexterity":
            dexterity += amount

init:
    $ flash = Fade(.1, 0, .1, color="#fff")
    $ red_flash = Fade(.1, 0, .1, color="#ff0000")
    
# Prologue of the story
label start:
    stop music
    play music "bgmwar.mp3"
    #UI for stats
    show screen gameUI
    # Input for player name
    $ player_name = ("")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "you"  # Default name if left blank

    # Prologue narration
    play sound "intensify.mp3"
    scene bg burningtown with fade

    narrator "The peaceful Town is now a battlefield." 
    "Chaos steels clashing.." 
    "Flames roaring..." 
    "Your ragged breaths fighting to keep pace." # VA = xy
    "Suddenly"

    "A sharp whistle cuts through the air." # VA = xy
    play sound "slash.mp3"
    scene black
    with flash
    scene bg burningtown
    with red_flash
    show slash

    narrator "a blade whistles past inches from your head." # VA = xy

    P "Ugh, th-that was clo-" # VA = xy
    hide slash with flash and red_flash
    play sound "impact.mp3"
    show hammerhit
    narrator "you didn't notice him"
    "as something slams into your chest! its weight like a battering ram."
    hide hammerhit
    scene bg carriage impact
    with red_flash and flash
    scene bg carriage burning with dissolve
    
    "You're thrown twenty feet, crashing into a noble’s gilded carriage." 
    scene bg carriage wounded with dissolve
    "Wood splinters."
    scene bg carriage woundedd with dissolve
    "metal groans under the force."
    scene bg carriage woundeddd with dissolve
    "you struggle to stay on your feet." # VA = xy
    
    scene sorcerer with dissolve
    narrator "you see a hooded figure staring at you.."
    scene sorcererhand with dissolve
    pause 0.5
    scene sorcerercast with dissolve
    pause 0.5
    scene sorcererfire with dissolve
    "you see his hands rise"
    scene sorcererfre with dissolve
    P "a sorcerer.."
    scene sorcererfr with dissolve
    narrator "you muttered."
    scene streak with dissolve

    "as a searing blast of heat tears toward you!" # VA = xy
    scene heat with red_flash
    play sound "fireball.wav"
    narrator "The heat is suffocating. "
    scene injured with dissolve
    "The odds? Even worse..." # VA = xy

    # Menu: First choice
    menu:
        "You're exhausted and injured with indecision. Who is the biggest threat?"

        "The Quick Swordsman?":
            $ increase_attribute ("dexterity", 1)
            $ increase_attribute ("knowledge", 1)
            "you gained 1 knowledge and dexterity!"
            tut "you gain status increase depending on your choices!"
            tut "so choices not only, lead you to routes and paths, but also builds your character"
            tut "into who and what your character is."
            tut "is he observant? is he quick? is he strong? and so on."
            tut "we plan to add more incoming mechanics with these unique choices we thought of."
            tut "now back to the game!"
            jump threat_narration

        "The Tank with Hammer?":
            $ increase_attribute ("strength", 1)
            $ increase_attribute ("guts", 1)
            "you gained 1 strength and guts!"
            tut "you gain status increase depending on your choices!"
            tut "so choices not only, lead you to routes and paths, but also builds your character"
            tut "into who and what your character is."
            tut "is he observant? is he quick? is he strong?"
            tut "carefully pick your choice that leads to your route and character path!"
            tut "we plan to add more incoming mechanics with these unique choice mechanics we thought of."
            tut "now back to the game!"
            jump threat_narration

        "The Pyro Sorcerer?":
            $ increase_attribute ("charm", 1)
            $ increase_attribute ("knowledge", 1)
            "you gained 1 charm and knowledge!"
            tut "you gain status increase depending on your choices!"
            tut "so choices not only, lead you to routes and paths, but also builds your character"
            tut "into who and what your character is."
            tut "is he observant? is he quick? is he strong?"
            tut "carefully pick your choice that leads to your route and character path!"
            tut "we plan to add more incoming mechanics with these unique choice mechanics we thought of."
            tut "now back to the game!"
            jump threat_narration





