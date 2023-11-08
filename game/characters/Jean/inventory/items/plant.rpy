label Jean_plant_shopping_accept:
    $ Jean.change_face("worried1", eyes = "down", mouth = "smirk")

    if "plant1" in Jean.inventory.keys() or "plant2" in Jean.inventory.keys() or "plant3" in Jean.inventory.keys():
        ch_Jean "Aw, you got me some more plants?"

        call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1307
        call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1308

        $ Jean.change_face("worried1", mouth = "smirk")
    else:
        ch_Jean "Aw, you got me some plants?"

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Before she left, Ororo said I should 'liven up' my room."
        ch_Player "Now if I'm not around, you won't be alone while studying."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "That was {i}super{/i} cheesy. . ."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "But I appreciate the thought."

        call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1309
        call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1310

    return True

label Jean_plant_shopping_reject:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "Hmm, that's. . . sweet of you. . ."

    $ Jean.change_face("worried1")

    ch_Jean "I can't really take care of these right now, though."

    return

label Jean_plant_gift_accept:
    $ Jean.change_face("worried1", eyes = "down", mouth = "smirk")

    if "plant1" in Jean.inventory.keys() or "plant2" in Jean.inventory.keys() or "plant3" in Jean.inventory.keys():
        ch_Jean "Aw, you got me some more plants?"

        call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1311
        call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1312

        $ Jean.change_face("worried1", mouth = "smirk")
    else:
        ch_Jean "Aw, you got me some plants?"

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Before she left, Ororo said I should 'liven up' my room."
        ch_Player "Now, if I'm not around, you won't be alone while studying."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "That was {i}super{/i} cheesy. . ."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "But I appreciate the thought."

        call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1313
        call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1314

    return True

label Jean_plant_gift_reject:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "Hmm, that's. . . sweet of you. . ."

    $ Jean.change_face("worried1")
    
    ch_Jean "I can't really take care of these right now, though."

    return