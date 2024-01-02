label Jean_wholesome_romance_novel_shopping_accept:
    if EventScheduler.Events["Jean_gifts"].completed:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("surprised1", eyes = "down", blush = 1)

        ch_Jean "I recognize this author!"

        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "I love their other books."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Thank you so much. . ."

        $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

        ch_Jean "Now I just gotta find time to read it."

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

label Jean_wholesome_romance_novel_shopping_reject:
    $ Jean.change_face("surprised2")

    "She just pushes the book back into your hands."
    ch_Jean "Sorry, no time to read."

    return

label Jean_wholesome_romance_novel_gift_accept:
    if EventScheduler.Events["Jean_gifts"].completed:
        $ Jean.change_face("surprised2")

        pause 1.0

        $ Jean.change_face("surprised1", eyes = "down", blush = 1)

        ch_Jean "I recognize this author!"

        $ Jean.change_face("pleased2", blush = 1)

        ch_Jean "I love their other books."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Thank you so much. . ."

        $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

        ch_Jean "Now I just gotta find time to read it."

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

label Jean_wholesome_romance_novel_gift_reject:
    $ Jean.change_face("surprised2")

    "She just pushes the book back into your hands."
    ch_Jean "Sorry, no time to read."

    return