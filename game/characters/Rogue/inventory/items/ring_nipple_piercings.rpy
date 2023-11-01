label Rogue_ring_nipple_piercings_accept:
    if "ring_nipple_piercings" in Rogue.inventory.keys():
        $ Rogue.change_face("sexy")

        ch_Rogue "You like 'em pierced?"
    else:
        $ Rogue.change_face("surprised2")

        ch_Rogue "Ya think ah'd look good with 'em?"
        ch_Rogue "Ah have been curious. . ."

    return

label Rogue_ring_nipple_piercings_reject:
    $ Rogue.change_face("confused3")

    ch_Rogue "Ya want me to get my. . . pierced?!"

    $ Rogue.change_face("angry1")

    ch_Rogue "Not happenin'."

    return