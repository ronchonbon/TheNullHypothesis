label Jean_rejects_titjob:
    $ Jean.change_face("confused2", blush = 1)

    ch_Jean "You wanna. . ." 

    $ Jean.change_face("confused1", eyes = "down", blush = 1) 

    ch_Jean "Between my boobs??"
    ch_Jean "Not right now. . ."

    return

label Jean_accepts_titjob_first_time:
    $ Jean.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Jean "You wanna. . ." 

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "Between my boobs?"

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "We can try that." 
    ch_Jean "What, touching them with your hands wasn't enough?"

    return

label Jean_accepts_titjob_second_time:

    return

label Jean_accepts_titjob:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Sure." 
        ch_Jean "It is kinda fun."   
    elif dice_roll == 2:
        $ Jean.change_face("sly", blush = 1)

        ch_Jean "I'm feeling generous. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "C'mere, [Jean.Player_petname]." 

    return

label Jean_accepts_titjob_love:

    return