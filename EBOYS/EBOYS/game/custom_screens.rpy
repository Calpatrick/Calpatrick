screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/stats_idle.png"
        action ShowMenu("StatsUI")

screen StatsUI:
    add "UI/greenbg.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Knowledge" size 40
                text "Charm" size 40
                text "Guts" size 40
                text "Strength" size 40
                text "Dexterity" size 40
            
            vbox: 
                spacing 10
                text "[knowledge]" size 40
                text "[charm]" size 40
                text "[guts]" size 40
                text "[strength]" size 40
                text "[dexterity]" size 40
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/return.png"
        action Return()