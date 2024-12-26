label Act_two:
    #bg in the written exam.
    #many people.
    #you finished the exam.
    scene exam_room_packed with dissolve
    narrator "you're faced with familiar questions, it seems your interest shows how you've never neglected your studies."
    "but you're still nervous.."
    "not from the exam but"
    "from the numbers of applicants taking the exam"
    "and the fear of being rejected."
    "you know it.. this program only accepts three people.."
    "and there are around 400 people taking the exams."
    "could you really be one of the three who'll pass from the 400 applicants."
    "!!!"
    ins "thank you for taking the written exams, you're given 30 mins to prepare on the white room."
    "startled from the sudden exchange"
    P "oh uhh hahaha, okay t-thank you!"
    ins "after preparing your next exam will start."
    ins "fighting against a goblin.."
    P "(gulps)"
    P "so I'm finally going to be fighting with a real monster..."
    P "no need to worry, I might've not been trained by an instructor."
    P "I still managed to maintain a good physique and mind!."
    "after all, since you were young"
    "you've kinda of participated in alot of physical workouts."
    "from jogging with your dad early in the morning, to using wood cutting as your sword practices"
    "but aside from all of those, the most memorable thing you remember you did to keep your body and mind"
    "at top shape is.."
    menu:

        "winning on a amateur sword competition in your area!":
            $ increase_attribute ("strength", 2)
            $ increase_attribute ("dexterity", 2)
            $ increase_attribute ("guts", 2)
            "you gained strength, dexterity, and guts!"
            jump sword_win
        
        "winning on a bow shooting competition in your area!":
            $ increase_attribute ("dexterity", 2)
            $ increase_attribute ("knowledge", 2)
            $ increase_attribute ("charm", 2)
            "you gained dexterity, knowledge, and charm!"
            jump bow_win
        
        "finishing top 10 on the entire kingdom's scholarly tests!":
            $ increase_attribute ("knowledge", 3)
            $ increase_attribute ("charm", 3)
            "you gained knowledge and charm!"
            jump scholarly_win


label sword_win:
    scene sword_competition with dissolve
    "you remembered now!"
    #hazy flashback memories..
    P "I won the tournament before by using my pure strength and guts to hack and slash my opponents."
    P "I think I was already stronger than my peers, until."
    P "The finals, I fought against a formidable enemy, my strength was useless against her..."
    P "she countered and parried me like it was nothing, I was truly facing a unclimable wall."
    P "still I won through her getting disqualified, some royal guards interrupted the tournament and she started running away.."
    P "I remember her runnning away from them, and the royal guards chasing her.."
    P "that was odd-"
    P "wait no- I gotta prepare!"
    P "soon they'll call my name..."
    P "(wish me luck mom..)"
    "you step forwad into the white room.."
    $ increase_attribute ("strength", 2)
    $ increase_attribute ("guts", 2)
    jump Act_two2


label bow_win:
    #hazy BG
    scene archerytournament with dissolve
    "you remembered now!"
    #hazy flashback memories..
    P "I won the tournament before with by using my pure dexterity and knowledge to shoot my targets without missing."
    P "I think I was already better than my peers, until."
    P "The finals, I fought against a formidable enemy, we were at stalemate for both not missing our targets."
    P "until the organizers decided to do a final tie breaker.."
    P "I think.. yeah.. it was that."
    P "they made us shoot an extremely fast moving target."
    P "and she missed.. while I got it right in the middle of its bullseye."
    P "I remember her crying out, and me and my mom? we were comforting her."
    P "wait, we were both students of my mom? what was her name again?"
    P "(it was years ago.. I can't remember..)"
    P "I wonder how she is now.."
    P "she was an aspiring huntress is all I could remember..."
    P "No use to thinking of her now-"
    P "I've gotta prepare.."
    P "(wish me luck mom..)"
    "you step forward into the white room.."
    $ increase_attribute ("dexterity", 2)
    $ increase_attribute ("knowledge", 2)
    jump Act_two2


label scholarly_win:
    #hazy BG
    scene awarded_a_medal_holding_a_book with dissolve
    "you remembered now!"
    #hazy flashback memories..
    P "I did join knowledge tests, and became on of the top 10 finishers in that scholarly program.."
    P "there were others better than me of course. but I got knowledge thank to that."
    P "and I thought was already better than my peers, until."
    P "I competed against her.. a brilliant scholar who seemed stoic.."
    P "not only is she good at theories, monsternologies, and history.."
    P "at a young age she was also already able to use magic.."
    P "I admired her, for being so talented.."
    P "but deep down I know.."
    P "I wasn't commited to my studies.."
    P "I thought just reading books was enough..."
    P "but I realized that I have to learn things on my own, and I have to learn how to use my knowledge."
    P "and if I want to I think I can to learn magic too.."
    P "she was a big help in me getting to where I am now..."
    P "I'm greatful for that.."
    P "so I must prove that it was all for nothing.."
    P "I've gotta prepare."
    P "wish me luck mom."
    "you step forward into the white room.."
    $ increase_attribute ("knowledge", 3)
    $ increase_attribute ("charm", 1)
    jump Act_two2

label Act_two2:
    scene white_room_with_weapons with dissolve
    #bg in a colloseum in next label.
    #first combat against a goblin!
    "stepping in the white room you found.."
    "a leather padded armor..."
    "and weapons."
    P "hmmm.. what should I choose?"
    menu:

        "A sword?":
            jump wip 
        "A dagger?":
            jump wip
        "A staff?":
            jump wip
        "A Bow?":
            jump wip

label wip:
    "Hello, there! it seemed like you reached the ending of the unfinished game!"
    "Good to see you reach here."
    "unforunately we didn't progress that far yet in our game."
    "But thanks for getting into it!"
    "as you can see there are a lot to be polish and finish in the game."
    "we didn't have that much time to work on this game, but we'll continue on working on this!"
    "slowly but surely!"
    "Advent: Path of The SpellGuard WIP ends here!"
    "Thank you!!"

        

