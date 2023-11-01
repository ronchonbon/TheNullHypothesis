label Jean_rejects_handjob:
    $ Jean.change_face("confused2", blush = 1)

    ch_Jean "You want me to. . ." 

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "I'm not ready to touch your. . . thing, yet. . ." 
    
    return

label Jean_accepts_handjob_first_time:
    $ Jean.change_face("surprised2", blush = 1)

    ch_Jean "You want me to jerk you off?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Jean "Oh all right, [Jean.Player_petname]."
    ch_Jean "I'm willing to try."

    $ Jean.change_face("neutral", eyes = "squint", blush = 2)

    ch_Jean "I've never done this before, so cut me some slack. . ."
    
    return

label Jean_accepts_handjob_second_time:

    return

label Jean_accepts_handjob:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "I'm getting better at it, right?" 
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1)

        ch_Jean "Fine, but you're not cumming until I say so." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 2) 

        ch_Jean "That clear, [Jean.Player_petname]?"
        ch_Player "Yes. . ." 

    return

label Jean_accepts_handjob_love:

    return

label Jean_rejects_fondle_balls:
    $ Jean.change_face("confused1", eyes = "down", blush = 1) 

    ch_Jean "Let me figure your dick out first. . ."
    
    return

label Jean_accepts_fondle_balls_first_time:
    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean "Just hold them? Like this?"
    "She takes a hold of your balls, a bit too forcefully, causing you to wince."
    ch_Jean "Sorry. . . gently, got it."

    return

label Jean_accepts_fondle_balls_second_time:

    return

label Jean_accepts_fondle_balls:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

        ch_Jean "Sure."
        "She gently grabs them."
    elif dice_roll == 2:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Jean "You like when I'm in control, huh?"
        "She takes a hold of your balls, giving them a squeeze."

    return

label Jean_accepts_fondle_balls_love:

    return