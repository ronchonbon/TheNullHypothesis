label Laura_belly_piercing_accept:
    if "belly_piercing" in Laura.inventory.keys():
        $ Laura.change_face("neutral")

        ch_Laura "You like it?"
    else:
        $ Laura.change_face("confused1")

        ch_Laura "Eh, fine."
        ch_Laura "Can always take it out."

    return

label Laura_belly_piercing_reject:
    $ Laura.change_face("confused1")

    ch_Laura "Why?"

    $ Laura.change_face("neutral")

    ch_Laura "No."

    return