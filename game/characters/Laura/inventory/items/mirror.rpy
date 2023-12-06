label Laura_mirror_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A mirror?"

    $ Laura.change_face("confused1") 

    ch_Laura "Why do I need to look at myself?"

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Player "I know you're very 'utilitarian', but you're also allowed to want to look good."
    ch_Player "This'll help you try on new outfits and stuff."

    $ Laura.change_face("angry1", eyes = "right", blush = 1) 

    ch_Laura "[Rogue.name] has been urging me to 'expand my wardrobe'. . ."
    ch_Laura "Thank you."

    call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1461
    call change_Character_stat(Laura, "trust", 0) from _call_change_Character_stat_1462

    return True

label Laura_mirror_shopping_reject:

    return

label Laura_mirror_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "A mirror?"

    $ Laura.change_face("confused1") 

    ch_Laura "Why do I need to look at myself?"

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Player "I know you're very 'utilitarian', but you're also allowed to want to look good."
    ch_Player "This'll help you try on new outfits and stuff."

    $ Laura.change_face("angry1", eyes = "right", blush = 1) 

    ch_Laura "[Rogue.name] has been urging me to 'expand my wardrobe'. . ."
    ch_Laura "Thank you."

    call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_1463
    call change_Character_stat(Laura, "trust", 0) from _call_change_Character_stat_1464

    return True

label Laura_mirror_gift_reject:

    return