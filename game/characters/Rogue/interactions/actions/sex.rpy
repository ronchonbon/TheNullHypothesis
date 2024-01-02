label Rogue_rejects_sex:
    $ Rogue.change_face("worried3", blush = 1)

    if not Rogue.History.check("sex"):
        ch_Rogue "Sex?!" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)  

        ch_Rogue "Ah'm not ready yet. . ."
        ch_Rogue "My first time's gotta be special."
    else:
        ch_Rogue "Ah think you should set your expectations lower, [Rogue.Player_petname]."

    return

label Rogue_accepts_sex_first_time:
    
    return

label Rogue_accepts_sex_second_time:

    return

label Rogue_accepts_sex:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

        ch_Rogue "Ya wanna make love again?"

        $ Rogue.change_face("sexy", blush = 2)

        ch_Rogue "Ah'd really like that. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

        ch_Rogue "Yer in the mood to use me?"

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "So ah've been a good girl?"

        $ Rogue.change_face("sexy", blush = 2)

        ch_Rogue "And. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "{i}Please{/i} finish inside me. . ."

    return

label Rogue_accepts_sex_love:

    return
    
label Rogue_rejects_anal:
    $ Rogue.change_face("perplexed", blush = 1) 

    if not Rogue.History.check("anal"):
        ch_Rogue "But that's the wrong hole. . ." 

        $ Rogue.change_face("confused1", blush = 1) 

        ch_Rogue "People put it in there?"
    else:
        ch_Rogue "Ah really don't think so, [Rogue.Player_petname]."

    return

label Rogue_accepts_anal_first_time:
    $ Rogue.change_face("confused2", mouth = "lipbite", blush = 1) 

    ch_Rogue "But that's the wrong hole. . ." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)  

    ch_Rogue "We can try it. . ."
    ch_Rogue "You'll be gentle, right [Rogue.Player_petname]?"

    return

label Rogue_accepts_anal_second_time:

    return

label Rogue_accepts_anal:
    if Rogue.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Anal. . . ?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)  

        ch_Rogue "Sure, we can go again."
        ch_Rogue "Ah. . . {i}really{/i} enjoy it."
    elif dice_roll == 2:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "In my ass again. . . ?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)  

        ch_Rogue "Lord. . . ah was hopin' you wanna."
        ch_Rogue "Ah'm really startin' to love it. . ."

    return

label Rogue_accepts_anal_love:

    return