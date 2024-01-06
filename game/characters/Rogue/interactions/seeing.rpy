label Rogue_seeing_penis(proper_subject = True, undressing = True):
    if not Rogue.History.check("seen_Player_naked"):
        "As you remove your pants, [Rogue.name] fixates on your crotch."

        $ Rogue.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "My lord. . ."

        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "It sure is impressive. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Are they all that big, or are ya just really well endowed. . . ?"

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah ain't confident ah can. . . take it all. . ."

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Ah reckon ah'll get real familiar with it either way."
    elif renpy.random.random() > 0.5:
        if proper_subject:
            $ subject = Rogue.name
            $ object = Rogue.name
            $ owner = Rogue.name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"
            
        $ pool = seeing_penis_narrations(Rogue, proper_subject = proper_subject, undressing = undressing)

        $ dialogue = renpy.random.choice(pool)

        "[dialogue]"

    return