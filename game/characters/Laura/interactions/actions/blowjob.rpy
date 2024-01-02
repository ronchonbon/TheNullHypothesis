label Laura_rejects_blowjob:
    $ Laura.change_face("confused3", blush = 1)

    ch_Laura "You want me to suck your. . ." 

    $ Laura.change_face("neutral", eyes = "squint", blush = 1) 

    if not Laura.History.check("blowjob"):
        ch_Laura "I've never heard of that. . ."
        ch_Laura "Not starting now."

    return

label Laura_accepts_blowjob_first_time:
    $ Laura.change_face("surprised2", blush = 1)

    ch_Laura "You want me to suck on it?" 

    if not Laura.History.check("rejected_blowjob"):
        $ Laura.change_face("confused1", blush = 2)

        ch_Laura "I've never heard of that. . ."

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2)

    ch_Laura "I'm not opposed to trying."

    return

label Laura_accepts_blowjob_second_time:

    return

label Laura_accepts_blowjob:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Alright. . ."

        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "I actually like the way you taste."
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "You know I'm not stopping until I get you to cum, right?"

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "Let's see how quick I can make it."

    return

label Laura_accepts_blowjob_love:

    return

label Laura_rejects_suck_balls:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1) 

    ch_Laura "No."

    return

label Laura_accepts_suck_balls_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Uh, okay?" 
    "Apparently you should've specified, gently. . ."

    return

label Laura_accepts_suck_balls_second_time:

    return

label Laura_accepts_suck_balls:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Okay. . ."
    "She latches on forcefully, alternating between sucking, and gently biting them."

    return

label Laura_accepts_suck_balls_love:

    return

label Laura_rejects_deepthroat:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1) 

    ch_Laura "No."

    return

label Laura_accepts_deepthroat_first_time:
    $ Laura.change_face("surprised2", blush = 1)

    ch_Laura "You want it to go deeper?" 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Laura "I do need to get used to it. . ."

    return

label Laura_accepts_deepthroat_second_time:

    return

label Laura_accepts_deepthroat:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "Let's do it."

    $ Laura.change_face("sexy", blush = 2) 

    ch_Laura "Eventually I want you all the way down."
    
    return

label Laura_accepts_deepthroat_love:

    return