label Jean_horror_novel_shopping_accept:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "This one sounds scary. . . {i}too{/i} scary. . ."

    $ Jean.change_face("worried1")

    return False

label Jean_horror_novel_shopping_reject:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "This one sounds scary. . . {i}too{/i} scary. . ."

    $ Jean.change_face("worried1")

    return

label Jean_horror_novel_gift_accept:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "This one sounds scary. . . {i}too{/i} scary. . ."

    $ Jean.change_face("worried1")

    return False

label Jean_horror_novel_gift_reject:
    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "This one sounds scary. . . {i}too{/i} scary. . ."

    $ Jean.change_face("worried1")

    return