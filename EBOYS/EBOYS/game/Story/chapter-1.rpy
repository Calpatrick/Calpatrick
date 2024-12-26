label threat_narration:
    narrator "You are right.." 
    "but if you ignore the others, you'll just die in a different way."
    "after all they are members of the infamous abberant group called.."
    "The distorted five."
    scene Distortedfive with dissolve 
    "Individually, any one of them would be able to challenge an army consisting of 500-800 soldiers."
    "Three of them working together just means your death will be a nightmare."
    pause 0.5
    scene injured with dissolve 

    # Menu: Second choice (Strategy)
    menu:
        "Your eyes dart from left to right."
        "the three abberants surround you."
        "What's your strategy?"

        "Find an opening to escape and regroup":
            $ increase_attribute ("dexterity", 1)
            $ increase_attribute ("guts", -1)
            "you gained 1 dexterity! but you lost 1 guts!"
            tut "we also added these kinds of choice mechanic, what was applicable to only affection levels."
            tut "are now also implemented on character's status"
            tut "now back to the game!"
            jump strategy_escape

        "Clench your weapon and go down fighting":
            $ increase_attribute ("strength", 1)
            $ increase_attribute ("knowledge", -1)
            "you gained 1 strength! but you lost 1 knowledge!"
            tut "we also added these kinds of choice mechanic, what was applicable to only affection levels."
            tut "are now also implemented on character's status"
            tut "now back to the game!"
            jump strategy_fight  # <-- humana


        "They don't seem that bright. Maybe I can talk my way out of this":
            $ increase_attribute ("intelligence", 1)
            $ increase_attribute ("charm", -1)
            "you gained 1 intelligence! but you lost 1 charm!"
            tut "we also added these kinds of choice mechanic, what was applicable to only affection levels."
            tut "are now also implemented on character's status"
            tut "now back to the game!"
            jump strategy_talk  # <-- kulangan pa

# Strategy choice: Escape
label strategy_escape:
    #BG for escaping, BG for Knockout_1 and Knockout_1.2, and 1.3 (alternative stay on BG town on shambles/war) 
    # and just use sfx for immersion.
    scene escape with flash
    narrator "Finding a sliver of space between the Pyro blasting sorcerer and the other two, you leap forward."
    narrator "You're almost through the gap!"
    scene black with red_flash
    "!!!!"
    "until your vision is suddenly blocked by a huge hammer!"
    
    P "No- Ugh!!.."
    narrator "you find yourself in the same carriage you crashed earlier."
    "but with serious injuries."
    scene injured with dissolve
    P "(There seems to be no way out of this...)"
    $ increase_attribute ("dexterity", 1)
    $ increase_attribute ("knowledge", 1)
    "you gained a little bit of dexterity and knowledge from this!"

    jump defeat_narration

# Strategy choice: Fight
label strategy_fight:
    #BG for heatblast, BG for knockout_2 (alternative stay on BG town on shambles/war) and just use sfx for immersion.
    scene last stand with dissolve
    narrator "You reached out to your weapon, preparing to launch your strongest attack."
    narrator "But she reacted too quickly. with a wave of her hand.."
    scene heat with red_flash
    "!!!!"
    "all you could see is a flash of bright and burning light"
    P "No- Ugh!!.."
    scene black with dissolve
    P "(There seems to be no way out of this...)"
    $ increase_attribute ("strength", 1)
    $ increase_attribute ("guts", 1)
    "you gained a little bit of strength and guts from this!"

    jump defeat_narration

# Strategy choice: Talk
label strategy_talk:
    #BG for surrendering, BG for knockout_3 (alternative stay on BG town on shambles/war) and just use sfx for immersion.
    scene surrender with dissolve
    narrator "You raise your hands in surrender, forcing a smile."
    P "I'll tell you what, let's just agree to disagree and we can call it a da-"
    "!!!!!"
    narrator "But it doesn't work. you felt a slashing sword passed by your throat."
    scene black with red_flash
    P "No- Ugh!!.."
    P "(damaged throat.)" 
    "(unable to talk..)" 
    "(unable to breath...)"
    "(There just seems to be no way out of this.)"
    $ increase_attribute ("knowledge", 1)
    $ increase_attribute ("charm", 1)
    "you gained a little bit of knowledge and charm from this!"
    # <-- Add more conversation or negotiation narrative here
    jump defeat_narration

# Defeat narration
label defeat_narration:
    #BG vultures on the sky circling, BG of the three villains and wrecked town, BG for three huge menacing shadows approaching
    #you raise your head and stare them down. (must draw this)
    scene black with dissolve
    narrator "You lack the strength to rise to your feet but refuse to look away in your final moments."
    narrator "They are approaching.."
    "slowly..."
    P "(so this is it huh...)"
    P "(no way out of this...)"
    narrator "In some twisted way, you're responsible for this. After all, it didn’t have to turn out this way."
    narrator "You could have made different decisions. But you didn’t. And you trusted the {color=#ff0000}wrong person{/color}..."
    pause 0.5
    tut "that's all for the basics! now your character stats are going back to 0!"
    $ knowledge = 0
    $ charm = 0
    $ guts = 0
    $ strength = 0
    $ dexterity = 0
    tut "now back to the game!"

    # Time skip choice
    menu:
        "Three years ago":
            jump flashback_intro

# Flashback introduction
label flashback_intro:
    stop music
    play music "bgm.mp3"
    #everything turn white bg.
    narrator "Three years ago, your story truly began..."
    jump Act_one


label Act_one:


    #BG for the Kingdom, BG for the warriors/heroes, BG for the Academy, and BG for flashback as a kid.
    $ player_name = renpy.input("What is your name?")
    narrator "That's right! you're [player_name]"
    scene white with dissolve
    "and you've always dreamt about becoming a SpellGuard since you were seven years old!"
    scene dreams with dissolve
    "you vividly remember jumping from stacks of hays in your old man's barn recklessly and"
    "hitting trees with your wooden swords and"
    "throwing rocks like fireballs on rivers to enjoy the huge splashes they do."
    "Back then..." 
    pause 0.5
    "you didn't realize it could actually happen."
    "It was just a fantasy. After all.."
    scene GatesofAcademy with dissolve
    P "What kid doesn’t dream of becoming a cool and strong swordsman?" 
    P "or a Magical powerful wizard?"
    P "What kid didn't want to be a Spellguard?"
    narrator "like your mother..."
    pause 0.5
    P "I remember mom kept on asking me about what I dreamed of becoming as a spellguard."
    menu:
        "can you recall what kind of Specialization did you dream of learning when becoming a Spellguard?"
        "The strength to wield a sword and cut through anything":
            $ increase_attribute ("strength", 1)
            $ increase_attribute ("guts", 1)
            "you gained a little bit of strength and guts!"
            jump sword_dream
        
        "The flexibility and speed to be an unnoticed spellguard.":
            $ increase_attribute ("dexterity", 2)
            "you gained a good ammount of dexterity!"
            jump dagger_dream
        
        "To aim with a bow or crossbow and never miss?":
            $ increase_attribute ("dexterity", 1)
            $ increase_attribute ("knowledge", 1)
            "you gained a little bit of dexterity and knowledge!"
            jump range_dream

        "Be able to cast magicspells?":
            $ increase_attribute ("knowledge", 2)
            "you gained a good ammount of knowledge!"
            jump magic_dream
        
label sword_dream:
    #bg and sfx and arts for sword_dream:
    show woodensword
    scene kidwithwoodsword
    narrator "you are reminded of the wooden sword your father gave you."
    narrator "even though your father didn't have enough money to get you a sword tutor."
    "this didn't stop you from swinging your sword everyday and everynight."
    "back when you first got your sword."
    "up to this moment, you've been honing your strength"
    "with nonstop swinging of your sword."
    "and as you grew older, your father carved you a new bigger and heavier sword."
    "he sees and respects your passion towards sword"
    "although you haven't wielded one yet."
    "a real sword.."
    "but it doesn't matter as this is the reason as to why.."
    "you're walking down this path.."
    jump Act_one2 #act 1.2

label dagger_dream:
    #bg and sfx and arts for dagger_dream:
    show woodendaggers
    scene bedtimestory
    narrator "you are reminded of the story your mother and father used to tell you to sleep early."
    "the story of the dark knight"
    "known to be shrouded in the shadows and mystery"
    "he was said to take down his enemies in silent leaving no trace."
    "you loved this story, remember how you started to play hide and seek with your mother"
    "and tag with your father, you tried to go with your mother on the forest."
    "learning to sense others' presence and even hide yours."
    "not only that but you've trained yourself to be quickfooted."
    "thanks to your father's guidance you've been able to develop"
    "your agility to be quickfooted."
    "and thanks to your mother you've been able to develop"
    "your dexterity to be lightfooted and stealthliy."
    jump Act_one2 #act 1.2

label range_dream:
    #bg and sfx and arts for range_dream:
    show bowandarrows
    scene archerywithmom
    narrator "your mother was a ranger spellguard known as the huntress."
    "you remember that she gave you an old small bow before."
    "you fell in love with the bow and the bowstring the moment you pulled and let go of the bowstring."
    "you felt it, the natural feeling of hitting something."
    "you felt connected with the bow and arrow, and it's the only thing that keeps on reminding you.."
    "of your mother.."
    "so you plan on taking on her legacy."
    "the descendant of the huntress."
    "the path that your mother entrusted you.."
    "you'll be taking it with you."
    jump Act_one2 #act 1.2

label magic_dream:
    #bg and sfx and arts for magic_dream:
    show bookandwands
    scene libraryreading
    narrator "you've heard stories of mages and magic"
    "you've always dreamt and wondered of manipulating elements."
    "and shooting them from the tips of your hands."
    "although rare. you believed you have talent in the weave of magic."
    "and so you didn't stop reading magic theory books"
    "you always go to the library"
    "it's just your father couldn't afford to get you into magic lessons"
    "so you only ended up with knowing magic theory.."
    "you haven't really used magic before."
    "but that is the reason as to why you're on your way walking towards this path."
    "to become a wizard..."
    "a great one."
    jump Act_one2 #act 1.2


label Act_one2:
    #act 1.2
    scene Thegreatrift with dissolve
    narrator "The rise of the Aberrant Beasts marked the turning point of an already fragile world."
    "When the first Rift opened fifty years ago, it was a distant concern a single, isolated tragedy."
    "But.."
    pause 0.5
    "Multiple rifts started to open, and soon overwhelmed humanity."
    scene Morerifts with flash
    "Lands invaded, corrupted, lost.."
    #BG of invasion
    scene invasion with flash
    narrator "Desperate to fight back, humanity consolidated its resources, founding the Academy in the shadow of the first Great Rift."
    scene councilofpeople with dissolve
    "It was a last ditch effort to train a new generation of warriors, mages, and leaders to stem the tide."
    "They emerged as Spellguards and became humanity's shield and sword."
    "They are the ones standing between civilization and total annihilation."
    scene ofhereoes with dissolve
    pause 0.5
    #BG of heroes  
    "Now, as the Academy trains its newest recruits."
    scene academy with dissolve
    "the world is barely hanging on the edge of disaster."
    "The Rifts grow larger."
    "The beasts more numerous."
    #BG of Academy, students, and students and spellguards fighting monster
    scene spellguardsvmonster with dissolve
    jump Act_one3

label Act_one3:
    scene kingdomwithwalls with dissolve
    narrator "An entire generation has grown up in a world under siege."
    "For as long as you can remember, the Aberrant Beasts have threatened humanity’s survival." 
    scene darkerlands with dissolve
    #BG of the Academy with huge walls around, the academy is not literally an academy, there are towns and places in it as well. 
    #people managing it are graduates from the academy
    scene kingdomwithwallsanddarkerlands with dissolve
    "Cities fortified themselves with towering walls and enchanted barriers."
    "The Academy became the last hope a place where the best and brightest trained to become Spellguards, protectors of humanity."
    #BG different streets inside the academy and towns
    scene townstreets with dissolve
    "But the cost of safety was steep."
    "Regions beyond the Academy’s reach became 'Lost Zones,' abandoned to the beasts."
    "Life inside the cities, though safer, was stifling."
    "Opportunities were scarce for those not born into privilege."
    pause 1

    "Despite the odds, you’ve always dreamed of becoming a Spellguard."
    "Just like your mother, who was a hero to you." 
    scene mother with dissolve
    "To protect those who couldn’t protect themselves."
    scene main_character with dissolve
    "Now, standing at the gates of the Academy, you feel the weight of that dream."
    scene mc_atacademy with dissolve #must transition perfectly with main_character scene
    "The journey ahead won’t be easy."
    "But you already know that, which is why you're here."
    scene mc_clenched_slingbad with dissolve #2-3 frame animation of mc getting ready
    pause 0.5
    jump Act_one4

label Act_one4:
    #BG suggestion: Majestic Academy gates with towering stone walls, an enchanted emblem glowing faintly overhead. Students mill about, bags slung over their shoulders, buzzing with excitement.
    scene academy with dissolve
    # narrator "You've been accepted to the prestigious Hero Academy a place revered across the continent as the ultimate training ground for humanity’s defenders against the Aberration Beasts."
    # narrator "After years of dreaming, you’re finally here, standing among hundreds of others who have made it past the grueling entrance trials. The Academy's gates seem impossibly tall, as if daring you to measure up."
    narrator "You've been invited to the entrance examination for scholarships in the Guardians Academy."
    "stormed with people from different cities, towns, and even kingdoms."
    scene academy_entrance_packed with dissolve
    "all of these people including you, are dreaming high."
    "as you feel the tension grow as the test for the Guardians Academy became closer."
    "although you know you'll pass the written test."
    "you're worried."
    "worried about the practical test."
    "as you heard from the instructor."
    "it will be fighting against goblins.."
    #removed to cut long dialogues.
    #"known to be one of the weakest monster."
    #"but the catch is, everytime you beat one they will come again and double the number of the previous goblins.."
    #"so defeating one goblin, means you'll have to fight two more, and defeating two, will end up on fighting four goblins."
    #"which are rumored to be the number of goblins required to fatally injured a low grade spellguard."
    #"and we're not even low grade yet, nor even a spellguard."
    #"so this test is a measurement of our talents."
    #"we could also give up the test anytime."
    #"when we deem it impossible for our levels.."

    P "So... this is it. The Hero Academy. The first step towards becoming a Spellguard."

    #BG suggestion: Shift to an overhead view of the Academy campus, showcasing a sprawling mix of modern magic-infused structures and ancient stone towers.


    
    P "That’s where I want to be... maybe one day, I'll be able to stand tall as a Spellguard."
    
    "you've entered the written examination room."
    scene exam_room with dissolve

    jump Act_two


