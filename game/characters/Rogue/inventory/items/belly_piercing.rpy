label Rogue_belly_piercing_accept:
    if "belly_piercing" in Rogue.inventory.keys():
        $ Rogue.change_face("pleased1")

        ch_Rogue "Like it pierced?"
    else:
        $ Rogue.change_face("pleased1")

        ch_Rogue "Ah was thinkin' about gettin' one. . ."

    return

label Rogue_belly_piercing_reject:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah. . . don't really wanna get pierced right now. . ."

    return