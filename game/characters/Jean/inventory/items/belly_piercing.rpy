label Jean_belly_piercing_accept:
    if "belly_piercing" in Jean.inventory.keys():
        $ Jean.change_face("smirk2")

        ch_Jean "It is a cute look."
    else:
        $ Jean.change_face("worried1")

        ch_Jean "Yeah, I was thinking about getting one. . ."
        ch_Jean "I hope it doesn't hurt too badly."

    return

label Jean_belly_piercing_reject:
    $ Jean.change_face("worried1")

    ch_Jean "I don't really want to get a piercing right now. . ."

    return