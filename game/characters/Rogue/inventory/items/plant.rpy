label Rogue_plant_shopping_accept:
    $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

    if "plant1" in Rogue.inventory.keys() or "plant2" in Rogue.inventory.keys() or "plant3" in Rogue.inventory.keys():
        ch_Rogue "Aw, more plants for my room?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1569
    else:
        ch_Rogue "Are these for my room?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah was thinkin' about gettin' some greenery to liven the place up."
        ch_Rogue "This is a real sweet gift, thank you. . ."

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1570

    return True

label Rogue_plant_shopping_reject:
    $ Rogue.change_face("confused1", eyes = "down")

    ch_Rogue "Ah'm not really sure what I'd do with it. . ."

    $ Rogue.change_face("confused1")

    return

label Rogue_plant_gift_accept:
    $ Rogue.change_face("confused1", eyes = "down", mouth = "smirk")

    if "plant1" in Rogue.inventory.keys() or "plant2" in Rogue.inventory.keys() or "plant3" in Rogue.inventory.keys():
        ch_Rogue "Aw, more plants for my room?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1571
    else:
        ch_Rogue "Are these for my room?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah was thinkin' about gettin' some greenery to liven the place up."
        ch_Rogue "This is a real sweet gift, thank you. . ."

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1572

    return True

label Rogue_plant_gift_reject:
    $ Rogue.change_face("confused1", eyes = "down")

    ch_Rogue "Ah'm not really sure what I'd do with it. . ."

    $ Rogue.change_face("confused1")

    return