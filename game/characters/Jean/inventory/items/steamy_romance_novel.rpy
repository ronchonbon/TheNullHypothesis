label Jean_steamy_romance_novel_shopping_accept:
    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Jean "I don't know if I have enough free time to read another. . ."
    "[Jean.name] looks at the cover."

    call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_1315

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 0.5

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Jean "Well. . ."

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Jean "Maybe I can make an exception this one time."
    ch_Player "Wait, but you sai-"

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    ch_Jean "Oh! I just realized. . ."
    ch_Jean "I have some free time {i}right now{/i} as a matter of fact."
    ch_Jean "I'll just be. . . in my room. . ."

    call send_Characters(Jean, Jean.home, behavior = "masturbating") from _call_send_Characters_295

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1316
    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1317 

    return True

label Jean_steamy_romance_novel_shopping_reject:
    $ Jean.change_face("appalled1", eyes = "down", blush = 1)

    ch_Jean "Uhm, hah, no thanks, [Player.first_name]. . ."

    $ Jean.change_face("worried1")

    return

label Jean_steamy_romance_novel_gift_accept:
    $ Jean.change_face("worried1", mouth = "smirk", eyes = "down")

    ch_Jean "I don't know if I have enough free time to read another. . ."
    "[Jean.name] looks at the cover."

    call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_1318

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 0.5

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Jean "Well. . ."

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Jean "Maybe I can make an exception this one time."
    ch_Player "Wait, but you sai-"

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    ch_Jean "Oh! I just realized. . ."
    ch_Jean "I have some free time {i}right now{/i} as a matter of fact."
    ch_Jean "I'll just be. . . in my room. . ."

    call send_Characters(Jean, Jean.home, behavior = "masturbating") from _call_send_Characters_296

    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1319
    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1320 

    return True

label Jean_steamy_romance_novel_gift_reject:
    $ Jean.change_face("appalled1", eyes = "down", blush = 1)

    ch_Jean "Uhm, hah, no thanks, [Player.first_name]. . ."

    $ Jean.change_face("worried1")

    return