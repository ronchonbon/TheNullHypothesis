label Jean_rejects_sex:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 2)

    ch_Jean "You. . . want to take my virginity?!" 

    $ Jean.change_face("worried3", mouth = "lipbite", blush = 1) 

    ch_Jean "I'm definitely not ready to give that to you yet. . ."
    
    return

label Jean_accepts_sex_first_time:
    $ EventScheduler.Events["Jean_first_sex_part_two"].start()

    return

label Jean_accepts_sex_second_time:

    return

label Jean_accepts_sex:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Sex again?"

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Let's do it."
    elif dice_roll == 2:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Jean "You wanna have sex with your big sister?"

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Fine, but only if you cum deep inside me. . ."

    return

label Jean_accepts_sex_love:

    return
    
label Jean_rejects_anal:
    $ Jean.change_face("surprised3", blush = 2)

    ch_Jean "You want to put your thing in my butt?!" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean ". . . I don't think it would fit." 

    $ Jean.change_face("perplexed", blush = 2)

    if not Jean.History.check("sex"):
        ch_Jean "And we haven't even had sex yet!" 

    return

label Jean_accepts_anal_first_time:
    $ Jean.change_face("surprised3", blush = 1)

    ch_Jean "You want to put it in my butt?!" 

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Jean ". . . I don't really think it'll fit." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "We can at least try it I guess. . ." 

    $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Jean "You better be gentle." 

    return

label Jean_accepts_anal_second_time:

    return

label Jean_accepts_anal:
    if Jean.check_traits("quirk"):
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Now that I'm used to it. . ." 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 2) 

        ch_Jean ". . . it does feel pretty good. . ." 
    elif dice_roll == 2:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Wanna fuck your big sister in the ass?" 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 2) 

        ch_Jean "Fine. . . I can't help but spoil you." 

    return

label Jean_accepts_anal_love:

    return