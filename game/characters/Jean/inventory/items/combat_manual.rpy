label Jean_combat_manual_shopping_accept:
    $ Jean.change_face("confused1", eyes = "down")

    "She reads the cover."

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "A book about fighting?"

    $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

    ch_Jean "You sure this is for me, and not. . . what's-her-name?"
    ch_Player "[Laura.name]?"

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "Yeah, her."

    $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Jean "It's the thought that counts. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean ". . . but I try to avoid close combat."
    ch_Jean "Save it for [Laura.name] or something."

    return False

label Jean_combat_manual_shopping_reject:
    $ Jean.change_face("confused1", eyes = "down")

    ch_Jean "How. . . random."
    ch_Jean "Not really my thing, [Player.first_name]."

    $ Jean.change_face("confused1")

    return

label Jean_combat_manual_gift_accept:
    $ Jean.change_face("confused1", eyes = "down")

    "She reads the cover."

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "A book about fighting?"

    $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

    ch_Jean "You sure this is for me, and not. . . what's-her-name?"
    ch_Player "[Laura.name]?"

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "Yeah, her."

    $ Jean.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Jean "It's the thought that counts. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean ". . . but I try to avoid close combat."
    ch_Jean "Save it for [Laura.name] or something."

    return False

label Jean_combat_manual_gift_reject:
    $ Jean.change_face("confused1", eyes = "down")

    ch_Jean "How. . . random."
    ch_Jean "Not really my thing, [Player.first_name]."

    $ Jean.change_face("confused1")

    return