label Jean_ring_labia_piercings_accept:
    if "ring_labia_piercings" in Jean.inventory.keys():
        $ Jean.change_face("smirk2")

        ch_Jean "It's grown on me."
    else:
        $ Jean.change_face("worried2")

        ch_Jean "You really think it'd look good?"
        ch_Jean "Okay. . ."

    return

label Jean_ring_labia_piercings_reject:
    $ Jean.change_face("appalled3")

    ch_Jean "What the fuck?"

    $ Jean.change_face("angry1")

    ch_Jean "You really think I'd go for something like that?"

    return