label Laura_rejects_self_touch_pussy:
    if not Laura.History.check("self_touch_pussy"):
        $ Laura.change_face("confused2", blush = 1)  

        ch_Laura "I don't know what that is. . ." 

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "But it's not happening."
    else:
        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "Not happening."

    return

label Laura_accepts_self_touch_pussy_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "Rogue did explain what that is. . ." 

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I guess you can watch."
    ch_Laura "But you better let me watch you do your thing some time. . ."

    return

label Laura_accepts_self_touch_pussy_second_time:

    return

label Laura_accepts_self_touch_pussy:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Yeah. . . "
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Pants off so I have something to look at. . ."
        "You do as she says."

        if not Laura.History.check("seen_Player_naked"):
            $ EventScheduler.Events["Laura_seeing_penis"].start()

        $ Laura.History.update("seen_Player_naked")

    return

label Laura_accepts_self_touch_pussy_love:

    return
    
label Laura_rejects_self_finger_ass:
    if not Laura.History.check("self_finger_ass"):
        $ Laura.change_face("confused2", blush = 1)  

        ch_Laura "I don't know what that is. . ." 

        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "But it's not happening."
    else:
        $ Laura.change_face("angry1", blush = 1)

        ch_Laura "Not happening."

    return

label Laura_accepts_self_finger_ass_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "Rogue did explain what that is. . ." 

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I guess you can watch."
    ch_Laura "But you better let me watch you do your thing some time. . ."

    return

label Laura_accepts_self_finger_ass_second_time:

    return

label Laura_accepts_self_finger_ass:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Yeah. . . "
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Pants off so I have something to look at. . ."
        "You do as she says."

        if not Laura.History.check("seen_Player_naked"):
            $ EventScheduler.Events["Laura_seeing_penis"].start()

        $ Laura.History.update("seen_Player_naked")

    return

label Laura_accepts_self_finger_ass_love:

    return

label Laura_rejects_self_vibrator:
    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Not happening."

    return

label Laura_accepts_self_vibrator_first_time:
    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I guess you can watch."
    ch_Laura "But you better let me watch you do your thing some time. . ."

    return

label Laura_accepts_self_vibrator_second_time:

    return

label Laura_accepts_self_vibrator:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Yeah. . . "
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Pants off so I have something to look at. . ."
        "You do as she says."

        if not Laura.History.check("seen_Player_naked"):
            $ EventScheduler.Events["Laura_seeing_penis"].start()

        $ Laura.History.update("seen_Player_naked")

    return

label Laura_accepts_self_vibrator_love:

    return

label Laura_rejects_self_dildo_pussy:
    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Not happening."

    return

label Laura_accepts_self_dildo_pussy_first_time:
    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I guess you can watch."
    ch_Laura "But you better let me watch you do your thing some time. . ."

    return

label Laura_accepts_self_dildo_pussy_second_time:

    return

label Laura_accepts_self_dildo_pussy:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Yeah. . . "
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Pants off so I have something to look at. . ."
        "You do as she says."

        if not Laura.History.check("seen_Player_naked"):
            $ EventScheduler.Events["Laura_seeing_penis"].start()

        $ Laura.History.update("seen_Player_naked")

    return

label Laura_accepts_self_dildo_pussy_love:

    return

label Laura_rejects_self_dildo_ass:
    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Not happening."

    return

label Laura_accepts_self_dildo_ass_first_time:
    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I guess you can watch."
    ch_Laura "But you better let me watch you do your thing some time. . ."

    return

label Laura_accepts_self_dildo_ass_second_time:

    return

label Laura_accepts_self_dildo_ass:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Yeah. . . "
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Pants off so I have something to look at. . ."
        "You do as she says."

        if not Laura.History.check("seen_Player_naked"):
            $ EventScheduler.Events["Laura_seeing_penis"].start()

        $ Laura.History.update("seen_Player_naked")

    return

label Laura_accepts_self_dildo_ass_love:

    return