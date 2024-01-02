label Laura_rejects_touch_pussy_over_clothes:
    $ Laura.change_face("surprised3", blush = 1) 

    pause 1.0

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "My crotch?"  

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "Off limits. . ."

    return

label Laura_accepts_touch_pussy_over_clothes_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "Down there?"  

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "Screw it. . ."

    return

label Laura_accepts_touch_pussy_over_clothes_second_time:

    return

label Laura_accepts_touch_pussy_over_clothes:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "I was about to make you touch me. . ."
    
    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Go for it. . ."

    return

label Laura_accepts_touch_pussy_over_clothes_love:

    return
    
label Laura_rejects_touch_pussy:
    $ Laura.change_face("surprised3", blush = 1) 

    pause 1.0

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "My crotch?"  

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "Off limits. . ."

    return

label Laura_accepts_touch_pussy_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "Down there?"  

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "Screw it. . ."

    return

label Laura_accepts_touch_pussy_second_time:

    return

label Laura_accepts_touch_pussy:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "I was about to make you touch it. . ."
    
    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Go for it. . ."

    return

label Laura_accepts_touch_pussy_love:

    return
    
label Laura_rejects_finger_pussy:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    if not Laura.History.check("finger_pussy"):
        ch_Laura "Nothing has ever been up there. I'm not starting like this." 
    else:
        ch_Laura "Not happening."

    return

label Laura_accepts_finger_pussy_first_time:
    $ Laura.change_face("surprised2", blush = 1)

    if Laura.check_traits("virgin"):
        ch_Laura "Nothings ever been up there. . ."
    else:
        pause 1.0

    $ Laura.change_face("neutral", eyes = "squint", blush = 2)

    ch_Laura "Not too rough. . ." 

    return

label Laura_accepts_finger_pussy_second_time:

    return

label Laura_accepts_finger_pussy:
    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Yes. . . use more than one."

    return

label Laura_accepts_finger_pussy_love:

    return

label Laura_rejects_eat_pussy:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "You cannot."

    if not Laura.History.check("eat_pussy"):
        ch_Laura "Whatever that is. . ."

    return

label Laura_accepts_eat_pussy_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "You want to lick it?" 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2)

    ch_Laura "Eh, why not."

    return

label Laura_accepts_eat_pussy_second_time:

    return

label Laura_accepts_eat_pussy:
    if Laura.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "Yeah. . ."
        ch_Laura "You really should."
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        "She just grabs your head, and shoves it in between her legs."

        $ Laura.change_face("sexy", blush = 2)

    return

label Laura_accepts_eat_pussy_love:

    return