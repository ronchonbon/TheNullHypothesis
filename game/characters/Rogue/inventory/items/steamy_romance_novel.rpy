label Rogue_steamy_romance_novel_shopping_accept:
    $ Rogue.change_face("confused1", mouth = "smirk", eyes = "down")

    "[Rogue.name] takes the book, and reads the cover."
    ch_Rogue "This author sounds familiar. . ."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Oh. . . lord. . . it's {i}that{/i} author. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Player "You've read some of their books before?"
    ch_Rogue "Ah. . . have. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "Really enjoyed 'em too. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Rogue "Thank you."

    call change_Girl_stat(Rogue, "desire", 25) from _call_change_Girl_stat_1573

    ch_Rogue "Ah'm just gonna. . ."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Rogue "Uhm. . ."
    ch_Rogue "Go to my room. . ."

    call send_Characters(Rogue, Rogue.home, behavior = "masturbating") from _call_send_Characters_300

    call change_Girl_stat(Rogue, "love", 35) from _call_change_Girl_stat_1574
    call change_Girl_stat(Rogue, "trust", 15) from _call_change_Girl_stat_1575

    return True

label Rogue_steamy_romance_novel_shopping_reject:
    $ Rogue.change_face("confused1", eyes = "down")
    
    pause 1.0

    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "Uhm. . ."
    ch_Rogue "No thanks, [Player.first_name]."

    return

label Rogue_steamy_romance_novel_gift_accept:
    $ Rogue.change_face("confused1", mouth = "smirk", eyes = "down")

    "[Rogue.name] takes the book, and reads the cover."
    ch_Rogue "This author sounds familiar. . ."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Oh. . . lord. . . it's {i}that{/i} author. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Player "You've read some of their books before?"
    ch_Rogue "Ah. . . have. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "Really enjoyed 'em too. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Rogue "Thank you."

    call change_Girl_stat(Rogue, "desire", 25) from _call_change_Girl_stat_1576

    ch_Rogue "Ah'm just gonna. . ."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Rogue "Uhm. . ."
    ch_Rogue "Go to my room. . ."

    call send_Characters(Rogue, Rogue.home, behavior = "masturbating") from _call_send_Characters_301

    call change_Girl_stat(Rogue, "love", 35) from _call_change_Girl_stat_1577
    call change_Girl_stat(Rogue, "trust", 15) from _call_change_Girl_stat_1578

    return True

label Rogue_steamy_romance_novel_gift_reject:
    $ Rogue.change_face("confused1", eyes = "down")
    
    pause 1.0

    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "Uhm. . ."
    ch_Rogue "No thanks, [Player.first_name]."

    return