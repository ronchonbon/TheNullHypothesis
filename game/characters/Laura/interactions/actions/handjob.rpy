label Laura_rejects_handjob:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "You want me to grip your. . ." 

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "I'm not touching {i}that{/i} right now. . ." 

    return

label Laura_accepts_handjob_first_time:
    $ Laura.change_face("confused2", blush = 1) 

    ch_Laura "You want me to grip your. . ." 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2)

    pause 1.0

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)
    
    if not Player.check_traits("cock_out"):
        ch_Laura "Fine, pants off." 
    else:
        ch_Laura "Fine."

    return

label Laura_accepts_handjob_second_time:

    return

label Laura_accepts_handjob:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "I'll try not to squeeze too hard this time. . ."
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1)

        ch_Laura "Alright. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2) 

        ch_Laura "But I'm not stopping until you cum."

    return

label Laura_accepts_handjob_love:

    return

label Laura_rejects_fondle_balls:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("neutral", eyes = "squint", blush = 1)

        ch_Laura "You're only getting one thing at a time for now. . ."
    elif dice_roll == 2:
        $ Laura.change_face("angry1", blush = 1) 

        "She taps your balls forcefully, making you wince, before going back to what she was doing." 

        ch_Laura "That's all you're getting right now."

    return

label Laura_accepts_fondle_balls_first_time:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "Doesn't it hurt?" 
        ". . . she says as she grabs them. . ."
        ". . . a bit too tightly."
    elif dice_roll == 2:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "You like the way it hurts?" 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        "She grabs your balls a bit forcefully."
        ch_Laura "Weirdo."
    elif dice_roll == 3:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "Even though it hurts?" 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "You probably like that, huh?"
        ch_Laura "They are fun to play with. . ."
        "She grabs them and squeezes, forcefully." 

    return

label Laura_accepts_fondle_balls_second_time:

    return

label Laura_accepts_fondle_balls:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Laura "Still don't understand why you enjoy it if it's painful. . ."

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "But they are fun to play with."
        "She grabs them and starts fondling. . . forcefully."
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 2)

        "She grabs them and squeezes, as if she's trying to force you to cum."
    elif dice_roll == 3:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        "She gives them a smack and then forcefully grabs them."
    elif dice_roll == 4:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "You like the way it hurts, huh?"
        "She gives your balls a smack, before taking hold of them, and squeezing."

    return

label Laura_accepts_fondle_balls_love:

    return