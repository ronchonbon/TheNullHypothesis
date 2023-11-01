label Jean_rejects_blowjob:
    $ Jean.change_face("surprised2", blush = 1)

    ch_Jean "You wanna put your. . ." 

    $ Jean.change_face("surprised1", eyes = "down", blush = 1) 

    ch_Jean "In my mouth?" 

    $ Jean.change_face("confused1", blush = 1)

    ch_Jean "Not gonna happen right now. . ."
    
    return

label Jean_accepts_blowjob_first_time:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 1)

    ch_Jean "You want me to suck your. . ." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean "Well, I've never done it before." 
    
    $ Jean.change_face("sexy", blush = 2)

    ch_Jean "But it's you, so I'll give it a try."
    
    return

label Jean_accepts_blowjob_second_time:

    return

label Jean_accepts_blowjob:
    if Jean.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Yeah. . . sure." 

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "I am getting better at it." 
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1)

        ch_Jean "You like using your big sister's mouth, huh?" 

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Fine, better only cum when I say so." 
    
    return

label Jean_accepts_blowjob_love:

    return

label Jean_rejects_suck_balls:
    $ Jean.change_face("worried1", eyes = "down", blush = 1)

    ch_Jean "Sorry [Jean.Player_petname], one thing at a time."
    
    return

label Jean_accepts_suck_balls_first_time:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Jean "Suck on your balls?" 

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 2)

    ch_Jean "I guess. . ."

    return

label Jean_accepts_suck_balls_second_time:

    return

label Jean_accepts_suck_balls:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Fine. . ." 

    return

label Jean_accepts_suck_balls_love:

    return

label Jean_rejects_deepthroat:
    $ Jean.change_face("confused1", eyes = "down", blush = 1) 

    ch_Jean "I'm still not even used to the taste of your thing yet."
    
    return

label Jean_accepts_deepthroat_first_time:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    ch_Jean "You want to go even deeper?"

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Jean "Just go slow. . ."
    ch_Jean "I'm not gonna be able to take you all at once yet. . . it'll take a while to build up to that."
    
    return

label Jean_accepts_deepthroat_second_time:

    return

label Jean_accepts_deepthroat:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Sure."

    $ Jean.change_face("sexy", blush = 2) 

    ch_Jean "I've been making pretty good progress."
    
    return

label Jean_accepts_deepthroat_love:

    return