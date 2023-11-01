label Laura_rejects_sex:
    $ Laura.change_face("confused3", blush = 1)  

    ch_Laura "You want to fuck?" 

    $ Laura.change_face("suspicious1", blush = 1)

    if not Laura.History.check("sex"):
        ch_Laura "You're not even close to earning my first time."
    else:
        ch_Laura "No way."

    return

label Laura_accepts_sex_first_time:
    $ EventScheduler.Events["Laura_first_sex_part_two"].start()

    return

label Laura_accepts_sex_second_time:

    return

label Laura_accepts_sex:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Yeah."
        ch_Laura "I can't stop thinking about the last time. . ."
        ch_Laura "Let's do it again and again. . ."

        $ Laura.change_face("sexy", blush = 2) 
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "Good."
        ch_Laura "I was about to force you inside me anyway. . ."
        ch_Laura "You're not going anywhere until you cum inside me at least once. . ."

    return

label Laura_accepts_sex_love:

    return
    
label Laura_rejects_anal:
    if not Laura.History.check("anal"):
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "That's the wrong hole. . . I don't think it would fit." 
        
        $ Laura.change_face("suspicious1", blush = 2)

        ch_Laura "We haven't even fucked yet."
    else:
        $ Laura.change_face("suspicious1", blush = 2)

        ch_Laura "I don't think so."

    return

label Laura_accepts_anal_first_time:
    $ Laura.change_face("confused2", blush = 1) 

    ch_Laura "Isn't that the wrong hole. . . ?"

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Laura "Will it fit?" 

    $ Laura.change_face("sly", blush = 1) 

    ch_Laura "Eh, might as well try."

    return

label Laura_accepts_anal_second_time:

    return

label Laura_accepts_anal:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "It can actually fit now. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2) 

        ch_Laura "Go for it. . ."
    elif dice_roll == 2:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "It still hurts a bit. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2) 

        ch_Laura "I like that. . ."

    return

label Laura_accepts_anal_love:

    return