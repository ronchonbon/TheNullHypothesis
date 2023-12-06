label Laura_plant_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    if "plant1" in Laura.inventory.keys() or "plant2" in Laura.inventory.keys() or "plant3" in Laura.inventory.keys():
        ch_Laura "Another plant?"

        $ Laura.change_face("confused1")

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1473
    else:
        ch_Laura "A plant?"

        $ Laura.change_face("confused1")

        ch_Laura "Why?"
        ch_Player "I just thought it would look nice in your room. . ."

        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "Maybe. . ."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Laura "Thank you."

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1474

    return True

label Laura_plant_shopping_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "I'm not really sure what I'd do with it. . ."

    $ Laura.change_face("confused1")

    return

label Laura_plant_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    if "plant1" in Laura.inventory.keys() or "plant2" in Laura.inventory.keys() or "plant3" in Laura.inventory.keys():
        ch_Laura "Another plant?"

        $ Laura.change_face("confused1")

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1475
    else:
        ch_Laura "A plant?"

        $ Laura.change_face("confused1")

        ch_Laura "Why?"
        ch_Player "I just thought it would look nice in your room. . ."

        $ Laura.change_face("confused1", eyes = "down")

        ch_Laura "Maybe. . ."

        $ Laura.change_face("neutral", eyes = "right", blush = 1)

        ch_Laura "Thank you."

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1476

    return True

label Laura_plant_gift_reject:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "I'm not really sure what I'd do with it. . ."

    $ Laura.change_face("confused1")

    return