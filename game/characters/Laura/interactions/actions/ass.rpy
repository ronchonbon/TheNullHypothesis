label Laura_rejects_grab_ass_over_clothes:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "My ass?" 

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "Weird. . . No."

    return

label Laura_accepts_grab_ass_over_clothes_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "My ass?" 

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "You are always staring at it. . ." 
    ch_Laura "Sure."

    return

label Laura_accepts_grab_ass_over_clothes_second_time:

    return

label Laura_accepts_grab_ass_over_clothes:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Grab it."
    "She takes yours in hand as well."

    return

label Laura_accepts_grab_ass_over_clothes_love:

    return

label Laura_rejects_grab_ass:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "My ass?" 

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "Weird. . . No."

    return

label Laura_accepts_grab_ass_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "My ass?" 

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "You are always staring at it. . ." 
    ch_Laura "Sure."

    return

label Laura_accepts_grab_ass_second_time:

    return

label Laura_accepts_grab_ass:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Grab it."
    "She takes yours in hand as well."

    return

label Laura_accepts_grab_ass_love:

    return
    
label Laura_rejects_finger_ass:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "You want to put your finger in there?" 

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "No. . ."

    return

label Laura_accepts_finger_ass_first_time:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "You want to put your finger in there?" 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2) 

    ch_Laura "Could be interesting. . ."

    return

label Laura_accepts_finger_ass_second_time:

    return

label Laura_accepts_finger_ass:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Yes. . ."

    return

label Laura_accepts_finger_ass_love:

    return

label Laura_rejects_eat_ass:
    $ Laura.change_face("confused3", blush = 1)

    ch_Laura "You want to lick my ass?" 

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Not now. . ."

    if not Laura.History.check("eat_ass"):
        ch_Laura "People do that?"

    return

label Laura_accepts_eat_ass_first_time:
    $ Laura.change_face("surprised3", blush = 1)

    ch_Laura "You want to lick my ass?" 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2) 

    ch_Laura "Screw it. . ."

    return

label Laura_accepts_eat_ass_second_time:

    return

label Laura_accepts_eat_ass:
    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Laura "You really enjoy it, [Laura.Player_petname]. . . ?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Laura "Do it. . . I didn't expect it to feel so good."
    
    return

label Laura_accepts_eat_ass_love:

    return