label Laura_horror_novel_shopping_accept:
    if EventScheduler.Events["Laura_boyfriend"].completed:
        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "A book?"
        ch_Laura "I do like the cover art. . ."

        $ Laura.change_face("confused1", eyes = "squint")

        ch_Laura "Are you attempting to make me read more?"
        ch_Player "I picked it mostly because of the cover."

        $ Laura.change_face("confused1", blush = 1)

        ch_Player "Thought it would look nice around your room."
        ch_Player "You don't have to read it if you don't want to."

        $ Laura.change_face("confused1", eyes = "down", blush = 1)

        ch_Laura "I see. . ."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Laura "Thank you. . ."

        call change_Companion_stat(Laura, "love", 0) from _call_change_Companion_stat_1459

        return True
    else:
        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "A book?"

        $ Laura.change_face("suspicious1")

        ch_Laura "I don't want it."

    return False

label Laura_horror_novel_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A book?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't want it."

    return

label Laura_horror_novel_gift_accept:
    if EventScheduler.Events["Laura_boyfriend"].completed:
        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "A book?"
        ch_Laura "I do like the cover art. . ."

        $ Laura.change_face("confused1", eyes = "squint")

        ch_Laura "Are you attempting to make me read more?"
        ch_Player "I picked it mostly because of the cover."

        $ Laura.change_face("confused1", blush = 1)

        ch_Player "Thought it would look nice around your room."
        ch_Player "You don't have to read it if you don't want to."

        $ Laura.change_face("confused1", eyes = "down", blush = 1)

        ch_Laura "I see. . ."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Laura "Thank you. . ."

        call change_Companion_stat(Laura, "love", 0) from _call_change_Companion_stat_1460

        return True
    else:
        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "A book?"

        $ Laura.change_face("suspicious1")

        ch_Laura "I don't want it."

    return False

label Laura_horror_novel_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A book?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't want it."

    return