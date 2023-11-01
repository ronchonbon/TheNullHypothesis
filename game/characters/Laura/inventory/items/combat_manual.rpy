label Laura_combat_manual_shopping_accept:
    $ Laura.change_face("suspicious1")

    pause 0.5

    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Is this another effort to have me read more?"
    "She looks over the cover."
    ch_Laura "'Combat Manual'?"

    $ Laura.change_face("confused1")

    ch_Player "I know you're already an amazing fighter."
    ch_Player "But I figured you might find this interesting."

    $ Laura.change_face("confused1", mouth = "smirk", eyes = "down")

    "She flips through the pages."
    ch_Laura "There are some interesting techniques in here."

    $ Laura.change_face("sly")

    ch_Laura "I'll have to test them on you."

    call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1455
    call change_Girl_stat(Laura, "trust", 20) from _call_change_Girl_stat_1456

    return True

label Laura_combat_manual_shopping_reject:
    $ Laura.change_face("suspicious1")

    ch_Laura "I think I know what I'm doing."

    return

label Laura_combat_manual_gift_accept:
    $ Laura.change_face("suspicious1")

    pause 0.5

    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "Is this another effort to have me read more?"
    "She looks over the cover."
    ch_Laura "'Combat Manual'?"

    $ Laura.change_face("confused1")

    ch_Player "I know you're already an amazing fighter."
    ch_Player "But I figured you might find this interesting."

    $ Laura.change_face("confused1", mouth = "smirk", eyes = "down")

    "She flips through the pages."
    ch_Laura "There are some interesting techniques in here."

    $ Laura.change_face("sly")

    ch_Laura "I'll have to test them on you."

    call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1457
    call change_Girl_stat(Laura, "trust", 20) from _call_change_Girl_stat_1458

    return True

label Laura_combat_manual_gift_reject:
    $ Laura.change_face("suspicious1")

    ch_Laura "I think I know what I'm doing."

    return