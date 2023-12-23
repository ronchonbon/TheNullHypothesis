label Jean_rejects_grab_ass_over_clothes:
    $ Jean.change_face("surprised2", blush = 2)

    ch_Jean "My butt?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "I know it's nice, but no. . ."

    return

label Jean_accepts_grab_ass_over_clothes_first_time:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "My butt?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

    ch_Jean "You do like staring at it. . ." 
    ch_Jean "Okay, sure."

    return

label Jean_accepts_grab_ass_over_clothes_second_time:

    return

label Jean_accepts_grab_ass_over_clothes:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "It's all yours." 

    return

label Jean_accepts_grab_ass_over_clothes_love:

    return

label Jean_rejects_grab_ass:
    $ Jean.change_face("surprised2", blush = 2)

    ch_Jean "My butt?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "I know it's nice, but no. . ."

    return

label Jean_accepts_grab_ass_first_time:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "My butt?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

    ch_Jean "You do like staring at it. . ." 
    ch_Jean "Okay, sure."

    return

label Jean_accepts_grab_ass_second_time:

    return

label Jean_accepts_grab_ass:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "It's all yours." 

    return

label Jean_accepts_grab_ass_love:

    return
    
label Jean_rejects_finger_ass:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 2)

    ch_Jean "You want to finger my. . ." 

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "Not in there, [Jean.Player_petname]."

    return

label Jean_accepts_finger_ass_first_time:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Jean "You want to finger my. . ." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2) 

    ch_Jean "Be gentle, [Jean.Player_petname]."

    return

label Jean_accepts_finger_ass_second_time:

    return

label Jean_accepts_finger_ass:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Get in there. . ."
    
    return

label Jean_accepts_finger_ass_love:

    return

label Jean_rejects_eat_ass:
    $ Jean.change_face("worried3", mouth = "lipbite", blush = 2) 

    ch_Jean "You want to lick. . . back there?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "I don't really wanna try that right now. . ."
    
    return

label Jean_accepts_eat_ass_first_time:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Jean "You want to lick. . . my butthole?" 

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "I don't know. . ." 
    ch_Jean "I guess it's worth trying if you really want to."
    
    return

label Jean_accepts_eat_ass_second_time:

    return

label Jean_accepts_eat_ass:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "You're into some really weird stuff, [Jean.Player_petname]. . ." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "But it did feel really good last time. . ." 
    
    return

label Jean_accepts_eat_ass_love:

    return