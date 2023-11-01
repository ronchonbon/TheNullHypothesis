label Laura_rejects_masturbation:
    $ Laura.change_face("angry1")

    ch_Laura "I want to stay like this."

    return

label Laura_accepts_masturbation_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Like. . . this?"

    return

label Laura_accepts_masturbation_second_time:

    return

label Laura_accepts_masturbation:
    $ Laura.change_face("sexy", blush = 1)

    return

label Laura_accepts_masturbation_love:

    return

label Laura_rejects_hands_and_knees:
    $ Laura.change_face("angry1")

    ch_Laura "I want to stay like this."

    return

label Laura_accepts_hands_and_knees_first_time:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "You want me in front of you like this?"

    return

label Laura_accepts_hands_and_knees_second_time:

    return

label Laura_accepts_hands_and_knees:
    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "You like this?"

    return

label Laura_accepts_hands_and_knees_love:

    return
    
label Laura_rejects_missionary:
    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "That sounds very vulnerable."

    return

label Laura_accepts_missionary_first_time:
    $ Laura.change_face("confused1", blush = 2)

    ch_Laura "I. . . suppose. okay."

    $ Laura.change_face("neutral", blush = 2)

    return

label Laura_accepts_missionary_second_time:

    return

label Laura_accepts_missionary:
    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Come here. . ."

    return

label Laura_accepts_missionary_love:

    return

label Laura_rejects_cowgirl:

    return

label Laura_accepts_cowgirl_first_time:

    return

label Laura_accepts_cowgirl_second_time:

    return

label Laura_accepts_cowgirl:

    return

label Laura_accepts_cowgirl_love:

    return

label Laura_rejects_doggy:
    $ Laura.change_face("angry1", blush = 2)

    ch_Laura "No, I want you in front of me."

    return

label Laura_accepts_doggy_first_time:
    $ Laura.change_face("confused1", blush = 2)

    pause 1.0

    $ Laura.change_face("angry1", blush = 3)

    ch_Laura "I. . . okay."

    $ Laura.change_face("neutral", blush = 2)

    ch_Laura "I trust you."

    return

label Laura_accepts_doggy_second_time:

    return

label Laura_accepts_doggy:
    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "You want me like this?"

    return

label Laura_accepts_doggy_love:

    return