label Jean_rejects_spank:
    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "*gasp*" 

    $ Jean.change_face("appalled1", blush = 1) 

    ch_Jean "Who said you could do that?"

    return

label Jean_accepts_spank_first_time:
    $ Jean.change_face("surprised3", blush = 1) 

    ch_Jean "*gasp*" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Bad boy. . ." 
    ch_Jean ". . . do it again."

    return

label Jean_accepts_spank_second_time:

    return

label Jean_accepts_spank:
    $ Jean.change_face("surprised3", blush = 1) 

    ch_Jean "*gasp*" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Harder."

    return

label Jean_accepts_spank_love:

    return