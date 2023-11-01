label Jean_rejects_footjob:
    $ Jean.change_face("surprised2", blush = 1)

    ch_Jean "You're into feet?"

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "That's cute, but I'm not touching your thing with them."

    return

label Jean_accepts_footjob_first_time:
    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "With my feet?" 

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "You like them that much?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "I did just get a pedicure."
    ch_Jean "Fine, let's try it."
    
    return

label Jean_accepts_footjob_second_time:

    return

label Jean_accepts_footjob:
    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "My feet again?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Alright, but you owe me a foot massage afterwards." 

    return

label Jean_accepts_footjob_love:

    return