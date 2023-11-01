label Jean_rejects_striptease:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "Trying to see me naked?"
    
    $ Jean.change_face("neutral", eyes = "squint", blush = 1)

    ch_Jean "You wish."

    return

label Jean_accepts_striptease_first_time:
    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Trying to see me naked?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Today's your lucky day, [Jean.Player_petname]."
    
    return

label Jean_accepts_striptease_second_time:

    return

label Jean_accepts_striptease:
    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Fine, but I better not be the only one taking my clothes off. . ." 
    
    return

label Jean_accepts_striptease_love:

    return