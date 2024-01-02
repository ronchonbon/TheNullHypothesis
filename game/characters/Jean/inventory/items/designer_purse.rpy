label Jean_designer_purse_shopping_accept:
    $ Jean.change_face("perplexed")

    ch_Jean "What the. . ."

    $ Jean.change_face("confused1", eyes = "down")

    ch_Jean "Is this a real. . . ?"

    $ Jean.change_face("worried2", blush = 1)

    ch_Jean "How much did this cost?!"
    ch_Player "Uhh. . ."

    $ Jean.change_face("confused2", blush = 1)

    ch_Player "It really wasn't {i}that{/i} expensive."

    $ Jean.change_face("suspicious1", blush = 1)

    ch_Jean "You didn't steal it, right?"
    ch_Player "What?! Of course not."

    $ Jean.change_face("worried1", eyes = "down", blush = 1)

    ch_Jean "And you're giving it to me. . . ?"

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "Thank you." 

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "I'll put it to good use."

    return True

label Jean_designer_purse_shopping_reject:
    $ Jean.change_face("perplexed")

    ch_Jean "What the. . ."
    ch_Jean "I. . . I can't accept something like this. . ."

    return

label Jean_designer_purse_gift_accept:
    $ Jean.change_face("perplexed")

    ch_Jean "What the. . ."

    $ Jean.change_face("confused1", eyes = "down")

    ch_Jean "Is this a real. . . ?"

    $ Jean.change_face("worried2", blush = 1)

    ch_Jean "How much did this cost?!"
    ch_Player "Uhh. . ."

    $ Jean.change_face("confused2", blush = 1)

    ch_Player "It really wasn't {i}that{/i} expensive."

    $ Jean.change_face("suspicious1", blush = 1)

    ch_Jean "You didn't steal it, right?"
    ch_Player "What?! Of course not."

    $ Jean.change_face("worried1", eyes = "down", blush = 1)

    ch_Jean "And you're giving it to me. . . ?"

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "Thank you." 

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "I'll put it to good use."

    return True

label Jean_designer_purse_gift_reject:
    $ Jean.change_face("perplexed")

    ch_Jean "What the. . ."
    ch_Jean "I. . . I can't accept something like this. . ."

    return