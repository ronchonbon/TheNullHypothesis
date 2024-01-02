label Laura_rejects_footjob:
    $ Laura.change_face("confused3", blush = 1) 

    ch_Laura "You like feet?"

    $ Laura.change_face("confused1", blush = 1) 
    
    ch_Laura "Weird. No."

    return

label Laura_accepts_footjob_first_time:
    $ Laura.change_face("confused3", blush = 1)

    ch_Laura "You're aroused by feet?"

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura ". . . weird."

    $ Laura.change_face("smirk2", blush = 2)

    ch_Laura "Fine."

    return

label Laura_accepts_footjob_second_time:

    return

label Laura_accepts_footjob:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Laura "I don't get why you like feet. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "But It is fun stepping on you."
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "The feet again. . . ?"

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Fine, [Laura.Player_petname]."
        "She gives your balls a nudge with her foot, causing you to wince."

    return

label Laura_accepts_footjob_love:

    return