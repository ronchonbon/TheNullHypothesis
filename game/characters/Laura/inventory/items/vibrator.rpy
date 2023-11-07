label Laura_vibrator_shopping_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "You want me to use this?"
    
    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Laura "Okay."

    return True

label Laura_vibrator_shopping_reject:
    $ Laura.change_face("appalled1")

    ch_Laura "What the hell?"

    return

label Laura_vibrator_gift_accept:
    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura "You want me to use this?"
    
    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Laura "Okay."

    return True

label Laura_vibrator_gift_reject:
    $ Laura.change_face("appalled1")

    ch_Laura "What the hell?"

    return