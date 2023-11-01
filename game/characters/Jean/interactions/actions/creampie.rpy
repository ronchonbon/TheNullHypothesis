label Jean_rejects_creampie:
    if Jean.birth_control:
        $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Jean "I don't want you to finish inside. . ."
    else:
        $ Jean.change_face("perplexed", blush = 2)

        ch_Jean "Trying to get me pregnant or something?!" 

        $ Jean.change_face("confused1", eyes = "squint", blush = 1)

        ch_Jean "You're not allowed to cum inside until I start on birth control."

    return

label Jean_accepts_creampie_first_time:
    if Jean.birth_control:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Jean "I am on the pill. . ." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Okay, you can do it inside."

    return

label Jean_accepts_creampie_second_time:

    return

label Jean_accepts_creampie:
    if Jean.quirk:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "Wanna cum inside your big sister?" 

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "You better."
    else:
        $ Jean.change_face("sexy", blush = 1) 

        "She just gives you a small nod."

    return

label Jean_accepts_creampie_love:

    return

label Jean_rejects_anal_creampie:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Jean "Not inside, I don't wanna clean it out. . ."

    return

label Jean_accepts_anal_creampie_first_time:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Jean "Inside my ass?" 

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Could be interesting. . ."

    return

label Jean_accepts_anal_creampie_second_time:

    return

label Jean_accepts_anal_creampie:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Jean "Inside my ass?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Do it. . ."

    return

label Jean_accepts_anal_creampie_love:

    return

label Jean_rejects_cum_in_mouth:
    $ Jean.change_face("worried1", blush = 1)

    if not Jean.History.check("cum_in_mouth") and not Jean.History.check("swallow_cum"):
        ch_Jean "I don't really wanna try tasting that stuff. . ."
    else:
        ch_Jean "No. . ."

    return

label Jean_accepts_cum_in_mouth_first_time:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    if not Jean.History.check("cum_in_mouth") and not Jean.History.check("swallow_cum"):
        ch_Jean "I have been wondering what it tastes like. . ."
    else:
        ch_Jean "Hmm. . . okay. . ."

    return

label Jean_accepts_cum_in_mouth_second_time:

    return

label Jean_accepts_cum_in_mouth:
    $ Jean.change_face("sly", blush = 1)

    "She wraps her lips around you as you blow."

    return

label Jean_accepts_cum_in_mouth_love:

    return
    
label Jean_rejects_cum_down_throat:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    if not Jean.History.check("cum_down_throat"):
        ch_Jean "I'm not even able to fit you that deep. . ."
    else:
        ch_Jean "I don't think so. . ."

    return

label Jean_accepts_cum_down_throat_first_time:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 1) 

    ch_Jean "In my throat?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "I'll try keeping it down. . ."

    return

label Jean_accepts_cum_down_throat_second_time:

    return

label Jean_accepts_cum_down_throat:
    $ Jean.change_face("surprised2", blush = 1) 

    pause 1.0

    $ Jean.change_face("sly", blush = 1) 

    "She helps pull you down as deep as possible."
    "She gags slightly, but manages to keep it down."

    return

label Jean_accepts_cum_down_throat_love:

    return