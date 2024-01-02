label Laura_rejects_creampie:
    # if Laura.check_trait("birth_control"):
    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Not inside, no."
    # else:
    #     $ Laura.change_face("suspicious1", blush = 1)

    #     ch_Laura "Did you take those anti-fertility pills. . . ?"

    #     $ Laura.change_face("angry1", blush = 1)

    #     ch_Laura "Then no." 
    #     ch_Laura "You know what my power does to my fertility."

    return

label Laura_accepts_creampie_first_time:
    # if Laura.check_trait("birth_control"):
    #     $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    #     ch_Laura "Did you take those pills?" 

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    # if Laura.check_trait("birth_control"):
    #     ch_Laura "Then fine, I've been wondering what it feels like. . ."
    # else:
    ch_Laura "Fine, I've been wondering what it feels like. . ." 

    return

label Laura_accepts_creampie_second_time:

    return

label Laura_accepts_creampie:
    if Laura.check_traits("quirk"):
        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "Inside?" 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "Do it all the way."
    else:
        $ Laura.change_face("sexy", blush = 1) 

        "She just gives you a small nod."

    return

label Laura_accepts_creampie_love:

    return

label Laura_rejects_anal_creampie:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "I'm not in the mood to clean that stuff out of my ass."

    return

label Laura_accepts_anal_creampie_first_time:
    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Laura "Inside my ass?" 

    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Do it." 

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "Deep."

    return

label Laura_accepts_anal_creampie_second_time:

    return

label Laura_accepts_anal_creampie:
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Laura "Do it." 
    ch_Laura "Deep. . ."

    return

label Laura_accepts_anal_creampie_love:

    return

label Laura_rejects_cum_in_mouth:
    $ Laura.change_face("confused2", blush = 1)

    if not Laura.History.check("cum_in_mouth") and not Laura.History.check("swallow_cum"):
        ch_Laura "I'm not gonna try tasting that stuff right now. . ."
    else:
        ch_Laura "No."

    return

label Laura_accepts_cum_in_mouth_first_time:
    $ Laura.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Laura "It doesn't smell as bad as I imagined. . ." 

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 2)

    ch_Laura ". . . actually pretty good." 
    "She opens wide."

    return

label Laura_accepts_cum_in_mouth_second_time:

    return

label Laura_accepts_cum_in_mouth:
    $ Laura.change_face("sexy", blush = 1)

    "She wraps her lips around you as you blow."

    return

label Laura_accepts_cum_in_mouth_love:

    return
    
label Laura_rejects_cum_down_throat:
    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    if not Laura.History.check("cum_down_throat"):
        ch_Laura "Can't even fit you that deep yet. . ."
    else:
        ch_Laura "No thanks."

    return

label Laura_accepts_cum_down_throat_first_time:
    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Laura "All the way inside?" 

    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Let's try it."

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "I want to feel it deep."

    return

label Laura_accepts_cum_down_throat_second_time:

    return

label Laura_accepts_cum_down_throat:
    $ Laura.change_face("surprised2", blush = 1) 

    pause 1.0

    $ Laura.change_face("sly", blush = 1) 

    "She grabs your balls and pulls you in as deep as possible."

    return

label Laura_accepts_cum_down_throat_love:

    return