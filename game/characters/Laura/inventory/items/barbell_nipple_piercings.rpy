label Laura_barbell_nipple_piercings_accept:
    if "barbell_nipple_piercings" in Laura.inventory.keys():
        $ Laura.change_face("smirk2")

        ch_Laura "I kinda get why people like these now."
    else:
        $ Laura.change_face("confused2")

        ch_Laura "You think it would look good?"

        $ Laura.change_face("neutral")

        ch_Laura "Eh, why not."

    return

label Laura_barbell_nipple_piercings_reject:
    $ Laura.change_face("angry1")

    ch_Laura "Why the fuck would I do that?"

    return