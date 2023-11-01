label Jean_vibrator_shopping_accept:
    $ Jean.change_face("worried2", eyes = "down")

    ch_Jean "That's uh. . ."
    
    $ Jean.change_face("worried2", mouth = "smirk")

    ch_Jean "Heh, sure, I guess."

    return True

label Jean_vibrator_shopping_reject:
    $ Jean.change_face("appalled2")

    ch_Jean "The fuck?!"
    ch_Jean "Why would you even bring me into a store like this?"

    return

label Jean_vibrator_gift_accept:
    $ Jean.change_face("worried2", eyes = "down")

    ch_Jean "That's uh. . ."
    
    $ Jean.change_face("worried2", mouth = "smirk")

    ch_Jean "Heh, sure, I guess."

    return True

label Jean_vibrator_gift_reject:
    $ Jean.change_face("appalled2")

    ch_Jean "The fuck?!"

    return