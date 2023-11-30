label Jean_mystery_novel_shopping_accept:
    if EventScheduler.Events["Jean_gifts"].completed:
        $ Jean.change_face("confused1", eyes = "down", mouth = "smirk")

        "She looks over the cover."
        ch_Jean "I haven't read stuff from this author before. . ."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "It looks really interesting though."
        ch_Player "I've heard good things."
        ch_Player "Let me know what you think."
        ch_Player "I know you could use a break, so just relax, and take some time to read it."

        $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

        ch_Jean "I'll try. . ."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "That upcoming exam can wait anyway."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1303
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1304

        return True
    else:
        $ Jean.change_face("surprised2")

        "She just pushes the book back into your hands."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I'm sorry. . ."
        ch_Jean "I just know that if I even look at an interesting book right now, I won't be able to stop myself from reading it."

        $ Jean.change_face("worried1", eyes = "down", blush = 1)

        ch_Jean "With all the exams coming up. . . I can't afford the distraction."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I appreciate the thought, though."

    return False

label Jean_mystery_novel_shopping_reject:
    $ Jean.change_face("surprised2")

    "She just pushes the book back into your hands."
    ch_Jean "Sorry, no time to read."

    return

label Jean_mystery_novel_gift_accept:
    if EventScheduler.Events["Jean_gifts"].completed:
        $ Jean.change_face("confused1", eyes = "down", mouth = "smirk")

        "She looks over the cover."
        ch_Jean "I haven't read stuff from this author before. . ."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "It looks really interesting though."
        ch_Player "I've heard good things."
        ch_Player "Let me know what you think."
        ch_Player "I know you could use a break, so just relax, and take some time to read it."

        $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

        ch_Jean "I'll try. . ."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "That upcoming exam can wait anyway."

        call change_Companion_stat(Jean, "love", 0) from _call_change_Companion_stat_1305
        call change_Companion_stat(Jean, "trust", 0) from _call_change_Companion_stat_1306

        return True
    else:
        $ Jean.change_face("surprised2")

        "She just pushes the book back into your hands."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I'm sorry. . ."
        ch_Jean "I just know that if I even look at an interesting book right now, I won't be able to stop myself from reading it."

        $ Jean.change_face("worried1", eyes = "down", blush = 1)

        ch_Jean "With all the exams coming up. . . I can't afford the distraction."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I appreciate the thought, though."

    return False

label Jean_mystery_novel_gift_reject:
    $ Jean.change_face("surprised2")

    "She just pushes the book back into your hands."
    ch_Jean "Sorry, no time to read."

    return