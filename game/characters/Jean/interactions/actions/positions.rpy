label Jean_rejects_masturbation:
    $ Jean.change_face("confused1", blush = 1)

    ch_Jean "Let's just stay like this, okay?"

    return

label Jean_accepts_masturbation_first_time:
    $ Jean.change_face("confused1", blush = 1)

    ch_Jean "Like this?"

    return

label Jean_accepts_masturbation_second_time:

    return

label Jean_accepts_masturbation:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Yeah. . .?"

    return

label Jean_accepts_masturbation_love:

    return

label Jean_rejects_hands_and_knees:
    $ Jean.change_face("confused1", blush = 1)

    ch_Jean "Let's just stay like this, okay?"

    return

label Jean_accepts_hands_and_knees_first_time:
    $ Jean.change_face("worried1", blush = 2)

    ch_Jean "How's this?"

    return

label Jean_accepts_hands_and_knees_second_time:

    return

label Jean_accepts_hands_and_knees:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Yeah. . .?"

    return

label Jean_accepts_hands_and_knees_love:

    return
    
label Jean_rejects_missionary:
    $ Jean.change_face("worried1", blush = 2)

    ch_Jean "I'm not ready for that yet. . ."

    return

label Jean_accepts_missionary_first_time:
    $ Jean.change_face("worried1", blush = 2)

    ch_Jean "Mmm, like this?"

    return

label Jean_accepts_missionary_second_time:

    return

label Jean_accepts_missionary:
    $ Jean.change_face("sexy", blush = 2)

    ch_Jean "I love you on top. . ."

    return

label Jean_accepts_missionary_love:

    return

label Jean_rejects_cowgirl:

    return

label Jean_accepts_cowgirl_first_time:

    return

label Jean_accepts_cowgirl_second_time:

    return

label Jean_accepts_cowgirl:

    return

label Jean_accepts_cowgirl_love:

    return

label Jean_rejects_doggy:
    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "Heh, you'll have to {i}earn{/i} that, [Jean.Player_petname]. . ."

    return

label Jean_accepts_doggy_first_time:
    $ Jean.change_face("worried1", blush = 2)

    ch_Jean "You really like this?"

    return

label Jean_accepts_doggy_second_time:

    return

label Jean_accepts_doggy:
    $ Jean.change_face("sexy", blush = 2)

    ch_Jean "Come here, you. . ."

    return

label Jean_accepts_doggy_love:

    return