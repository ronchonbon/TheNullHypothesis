label Jean_follow_in_love:
    "She grabs your hand." 

    $ Jean.change_face("smirk2")

    ch_Jean "I'm in as always, silly."

    return

label Jean_follow_in_relationship:
    $ Jean.change_face("smirk2")

    ch_Jean "Lead the way. . ." 

    $ Jean.change_face("sly", eyes = "down") 

    ch_Jean "So I can get a good look."

    $ Jean.change_face("smirk2") 

    return

label Jean_follow_love_and_trust:
    $ Jean.change_face("smirk2")

    ch_Jean "Count me in, [Jean.Player_petname]."

    return

label Jean_follow_love:
    ch_Jean "Well c'mon then, let's go."

    $ Jean.change_face("smirk2")

    return

label Jean_follow_trust:
    $ Jean.change_face("confused1") 

    ch_Jean "Mayyybe if you tell me where first."

    $ Jean.change_face("smirk2")

    return

label Jean_follow_temporary:
    ch_Jean "Fiiine." 
    ch_Jean "But, only for a bit."

    return

label Jean_follow_busy:
    if Jean.behavior == "training":
        $ Jean.change_face("confused1")

        ch_Jean "Kinda in the middle of training. . ."
    elif Jean.behavior == "studying":
        $ Jean.change_face("confused1")

        ch_Jean "No, sorry. . . I was planning on studying."

        $ Jean.change_face("neutral")

        ch_Jean "You're welcome to join though. . ."
    elif Jean.behavior == "in_class":
        $ Jean.change_face("perplexed")

        ch_Jean "Like I would skip class. . ."

        $ Jean.change_face("confused1")

        ch_Jean "You shouldn't either."
    else:
        ch_Jean "Sorry, kind of busy right now."

    return

label Jean_follow_reject:
    $ Jean.change_face("worried1")

    ch_Jean "Can't, [Jean.Player_petname]." 
    ch_Jean "Haven't studied enough today."

    return

label Jean_follow_reject_asked_once:
    $ Jean.change_face("confused1")

    ch_Jean "Really. . ."
    ch_Jean "Are you ignoring me?"

    return

label Jean_follow_reject_asked_twice:
    $ Jean.change_face("angry1")

    ch_Jean "Okay, quit it."
        
    call getting_kicked_out(Jean) from _call_getting_kicked_out_11

    return

label Jean_follow_reject_mad:
    $ Jean.change_face("appalled1") 

    ch_Jean "Ugh, no."

    $ Jean.change_face("angry1")

    ch_Jean "Not in the mood to go running around."

    return

label Jean_stop_follow_love:
    ch_Jean "Don't miss me too much."

    return

label Jean_stop_follow_love_stay:
    ch_Jean "Kay, but I'll hang around for a bit."

    return

label Jean_stop_follow:
    ch_Jean "See ya later."

    return

label Jean_stop_follow_mad:
    $ Jean.change_face("appalled1") 

    ch_Jean "Trying to ditch me?" 

    $ Jean.change_face("angry1") 

    ch_Jean "Ugh, bye."

    return

label Jean_stop_follow_heartbroken:
    $ Jean.change_face("worried1")  

    ch_Jean "But. . . why?" 

    $ Jean.change_face("sad", eyes = "down")

    pause 1.0

    $ Jean.change_face("neutral")

    "Whatever, bye." 

    return

label Jean_stop_follow_horny:
    $ Jean.mouth = "lipbite"

    ch_Jean "I can stop for now. . ." 

    $ Jean.change_face(eyes = "down", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Jean.change_face(eyes = "sexy", mouth = "lipbite", blush = 1) 

    ch_Jean "But you'll be on my mind."

    return

label Jean_stop_follow_nympho:
    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    ch_Jean "But I. . ." 

    $ Jean.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 2)

    pause 1.0

    $ Jean.change_face("worried2", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Jean "Just don't be surprised when I come looking for you later. . ."

    return