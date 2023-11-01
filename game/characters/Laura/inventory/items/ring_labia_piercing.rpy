label Laura_ring_labia_piercings_accept:
    if "ring_labia_piercings" in Laura.inventory.keys():
        $ Laura.change_face("smirk2")

        ch_Laura "I actually don't mind it down there."
    else:
        $ Laura.change_face("perplexed")

        ch_Laura "You really want me to?"

        $ Laura.change_face("neutral")

        ch_Laura "Fine."

    return

label Laura_ring_labia_piercings_reject:
    $ Laura.change_face("appalled1")

    ch_Laura "Are you insane?"

    return