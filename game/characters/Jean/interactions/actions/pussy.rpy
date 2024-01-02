label Jean_rejects_touch_pussy_over_clothes:
    $ Jean.change_face("confused2", blush = 2)

    ch_Jean "My crotch is off limits right now. . ."

    $ Jean.change_face("neutral", eyes = "squint", blush = 1)

    return

label Jean_accepts_touch_pussy_over_clothes_first_time:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2)

    ch_Jean "My crotch. . . ?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "Yeah, okay. . ."
    
    return

label Jean_accepts_touch_pussy_over_clothes_second_time:

    return

label Jean_accepts_touch_pussy_over_clothes:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "I'd very much like that. . ."
    elif dice_roll == 2:
        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "You'd better, [Jean.Pplayer_petname]. . ."
    
    return

label Jean_accepts_touch_pussy_over_clothes_love:

    return

label Jean_rejects_touch_pussy:
    $ Jean.change_face("confused2", blush = 2)

    ch_Jean "My pussy is off limits right now. . ."

    $ Jean.change_face("neutral", eyes = "squint", blush = 1)

    return

label Jean_accepts_touch_pussy_first_time:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2)

    ch_Jean "My. . . ?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "Yeah, okay. . ."

    return

label Jean_accepts_touch_pussy_second_time:

    return

label Jean_accepts_touch_pussy:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "I'd very much like that. . ."
    elif dice_roll == 2:
        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "You'd better, [Jean.Pplayer_petname]. . ."
    
    return

label Jean_accepts_touch_pussy_love:

    return
    
label Jean_rejects_finger_pussy:
    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Jean "Not right now."

    return

label Jean_accepts_finger_pussy_first_time:
    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Jean "Okay, but gently."

    return

label Jean_accepts_finger_pussy_second_time:

    return

label Jean_accepts_finger_pussy:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Jean "You can try using more than one finger too. . ." 
    
    return

label Jean_accepts_finger_pussy_love:

    return

label Jean_rejects_eat_pussy:
    $ Jean.change_face("surprised2", blush = 2)

    ch_Jean "You wanna lick it?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "Just use your hand for now. . ."

    return

label Jean_accepts_eat_pussy_first_time:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 2)

    ch_Jean "You wanna lick it?"  

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

    ch_Jean "Fine. . . I have been wondering what it might feel like."
    
    return

label Jean_accepts_eat_pussy_second_time:

    return

label Jean_accepts_eat_pussy:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

        ch_Jean "God, yes."  

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "I've been waiting for you to ask again. . ."
    elif dice_roll == 2:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Jean "You wanna eat your big sister out?"  

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Better get on it then. . ."
        ch_Jean "And you're not allowed to stop until I get at least a couple orgasms."
        
    return

label Jean_accepts_eat_pussy_love:

    return