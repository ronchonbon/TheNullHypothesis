label Laura_getting_late:
    $ Laura.change_face("neutral")

    ch_Laura "It's late."

    return

label Laura_getting_late_relationship:
    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "It's getting late."
    ch_Laura "You're probably going to bed soon. . ."

    return

label Laura_getting_late_love:
    $ Laura.change_face("neutral", eyes = "down", blush = 1)

    ch_Laura "Fuck. . . it's already late."

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "I don't know why you need so much sleep. . ."

    return

label Laura_getting_late_mad:
    $ Laura.change_face("angry1")

    ch_Laura "You're probably tired already or some shit."

    $ Laura.change_face("angry1", eyes = "left")

    ch_Laura "Just fuck off. . ."

    return

label Laura_getting_late_heartbroken:
    $ Laura.change_face("worried1", eyes = "left")

    ch_Laura "It's late. . ."

    $ Laura.change_face("angry1")

    ch_Laura "Aren't you tired or something?"

    return

label Laura_getting_late_horny:
    $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Laura "Why do you have to go to bed so early?" 

    return

label Laura_getting_late_nympho:
    $ Laura.change_face("suspicious1", mouth = "lipbite", blush = 1)

    ch_Laura "Why the fuck is it so late already. . ."
    ch_Laura "I had plans for you." 

    $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

    return

label Laura_asked_to_sleepover(sleeping_Characters):
    $ Laura.change_face("confused1")

    if Player.location != Laura.home:
        ch_Laura "You want to share your bed with me. . . ?" 
    else:
        ch_Laura "You want me to share my bed with you. . . ?" 
    
    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("smirk2", mouth = "lipbite")

        ch_Laura "I'm glad you asked."

        return True
    else:
        $ Laura.change_face("confused1", eyes = "squint")

        ch_Laura "Not tonight. . ." 

    return False

label Laura_asked_to_sleepover_relationship(sleeping_Characters):
    $ Laura.change_face("confused1", mouth = "lipbite")

    if Player.location != Laura.home:
        if len(sleeping_Characters) > 0:
            ch_Laura "You also want me to sleep over?"
        else:
            ch_Laura "You want me to sleep over?"
    else:
        ch_Laura "You want to sleep over?"

    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("smirk2", mouth = "lipbite")

        if Player.location != Laura.home:
            ch_Laura "Fine, I will. . ."
        else:
            ch_Laura "Fine."

        return True
    else:
        $ Laura.change_face("neutral")

        ch_Laura "Not tonight, [Laura.Player_petname]. . ." 
        ch_Laura "You'll see me tomorrow."

    return False

label Laura_asked_to_sleepover_love(sleeping_Characters):
    $ Laura.change_face("pleased1", mouth = "lipbite")

    if Player.location != Laura.home:
        if len(sleeping_Characters) > 0:
            ch_Laura "Want me to sleep over also?"
        else:
            ch_Laura "Want me to sleep over?"
    else:
        ch_Laura "You want to sleep over?"

    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("sly", mouth = "lipbite")

        ch_Laura "Good, I like that. . ."
        ch_Laura "You're sleeping naked, right?"

        return True
    else:
        $ Laura.change_face("smirk2")

        ch_Laura "Can't tonight, [Laura.Player_petname]. . ."
        ch_Laura "But you will see me tomorrow."

    return False

label Laura_asked_to_sleepover_mad(sleeping_Characters):
    $ Laura.change_face("appalled2")

    ch_Laura "{i}Grrrrrr{/i}"

    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("angry1", eyes = "squint") 

        ch_Laura "Fine."
        ch_Laura "Just because I'm angry doesn't mean I don't want to. . ."

        return True
    else:
        $ Laura.change_face("angry1")

        ch_Laura "I'm leaving. . ." 

    return False

label Laura_asked_to_sleepover_heartbroken(sleeping_Characters):
    $ Laura.change_face("worried1", eyes = "right") 

    pause 1.0

    $ Laura.change_face("confused1")

    ch_Laura "You're serious?"

    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("neutral", eyes = "right") 

        if Player.location != Laura.home:
            ch_Laura "Fine. . . I'll stay." 
        else:
            ch_Laura "Fine. . ."

        return True
    else:
        $ Laura.change_face("neutral")

        ch_Laura "No. . ."

        if Player.location != Laura.home:
            ch_Laura "I'll just go. . . goodnight."
        else:
            ch_Laura ". . . goodnight."

    return False

label Laura_asked_to_sleepover_horny(sleeping_Characters):
    $ Laura.change_face("sly", mouth = "lipbite")

    ch_Laura "Do I?"

    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "You know I do. . ."

        $ Laura.change_face("sly", mouth = "lipbite", eyes = "down")

        return True
    else:
        $ Laura.change_face("smirk2", mouth = "lipbite")

        ch_Laura "Normally. . ."

        $ Laura.change_face("smirk2") 

        ch_Laura "But not tonight."

    return False

label Laura_asked_to_sleepover_nympho(sleeping_Characters):
    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    if Player.location != Laura.home:
        ch_Laura "You want me to?"
    else:
        ch_Laura "You want to?"

    $ accepted = False

    if approval_check(Laura, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "Good thing you do. . ."

        $ Laura.change_face("sexy", eyes = "down", blush = 1) 

        return True
    else:
        $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

        ch_Laura "Not tonight." 

        $ Laura.change_face("sexy", eyes = "down", blush = 1)

        ch_Laura "I'll just have to come find you tomorrow." 

    return False
    
label Laura_request_sleepover(sleeping_Characters):
    $ Laura.change_face("neutral", eyes = "squint")

    if len(sleeping_Characters) > 0:
        ch_Laura "I want to sleep over too."
    else:
        if Player.location == Laura.home:
            ch_Laura "I want you to sleep over."
        else:
            ch_Laura "I want to sleep over."

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("smirk2") 

            ch_Laura "Don't hog the blanket."

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("neutral")

            ch_Laura "Fine. Goodnight."

    return False

label Laura_request_sleepover_relationship(sleeping_Characters):
    $ Laura.change_face("smirk2", mouth = "lipbite")

    if len(sleeping_Characters) > 0:
        ch_Laura "Make room. . . I also want to sleep over tonight."
    else:
        if Player.location == Laura.home:
            ch_Laura "I'll make room, I want you to sleep over tonight."
        else:
            ch_Laura "Make room. . . I want to sleep over tonight."

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("smirk2", blush = 1)

            ch_Laura "Good."

            $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

            ch_Laura "It's always better when you're around. . ."

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("confused1")

            ch_Laura "Why not?"

            $ Laura.change_face("neutral")

            ch_Laura "Fine, goodnight." 

    return False

label Laura_request_sleepover_love(sleeping_Characters):
    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

    if len(sleeping_Characters) > 0:
        ch_Laura "I'm also sleeping over tonight."
    else:
        if Player.location == Laura.home:
            ch_Laura "You're sleeping over tonight."
        else:
            ch_Laura "I'm sleeping over tonight."

    ch_Laura "And you're the little spoon."

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

            ch_Laura "You should sleep naked. . ."

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("neutral", eyes = "squint")

            ch_Laura "Fine. . . you'll just see me tomorrow then." 
            ch_Laura "Goodnight." 

    return False

label Laura_request_sleepover_mad(sleeping_Characters):
    $ Laura.change_face("angry1", eyes = "squint") 

    ch_Laura "I'm still pissed. . ."

    if Player.location == Laura.home:
        ch_Laura "But that doesn't mean I don't want you to sleep over."
    else:
        ch_Laura "But that doesn't mean I don't want to sleep over."

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("angry1") 

            ch_Laura "Good. . ."

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("appalled2")

            ch_Laura "{i}Grrrrrr{/i}"

            $ Laura.change_face("angry1")

            "She leaves without another word."

    return False

label Laura_request_sleepover_heartbroken(sleeping_Characters):
    $ Laura.change_face("worried1", eyes = "right") 

    if Player.location == Laura.home:
        ch_Laura "I want you to sleep over. . ."
    else:
        ch_Laura "I want to sleep over. . ."

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("confused1")

            ch_Laura "You're sure?"

            $ Laura.change_face("neutral")

            ch_Laura "Good. . ."

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("angry1")

            ch_Laura "Fine. . . I get it."
            ch_Laura "Bye." 

    return False

label Laura_request_sleepover_horny(sleeping_Characters):
    $ Laura.change_face("smirk2", mouth = "lipbite") 

    if Player.location == Laura.home:
        ch_Laura "You should stay. . ."
        ch_Laura "Sleep over."
    else:
        ch_Laura "I should stay. . ."

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

            ch_Laura "Good."

            $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("confused1")

            ch_Laura "Why not. . . ?"

            $ Laura.change_face("neutral") 

            ch_Laura "Fine, tomorrow." 

    return False

label Laura_request_sleepover_nympho(sleeping_Characters):
    $ Laura.change_face("suspicious1", mouth = "lipbite", blush = 1) 

    if Player.location == Laura.home:
        ch_Laura "You're sharing my bed tonight. . ."
    else:
        ch_Laura "I'm sharing your bed tonight. . ."

    ch_Laura "Right?" 

    menu:
        extend ""
        "Sure!":
            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "Good."

            $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1)

            ch_Laura "Now I won't have to come find you tomorrow. . ."

            return True
        "Not tonight, [Laura.name].":
            $ Laura.change_face("suspicious1", blush = 1) 

            ch_Laura "{i}Grrrrrr{/i}. . ."

            $ Laura.change_face("angry1", mouth = "lipbite", blush = 1) 

            ch_Laura "Fine, I'll just come find you tomorrow." 

    return False
    
label Laura_goodnight(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Laura "I'm also going to bed."
    else:
        ch_Laura "I'm going to bed."

    return

label Laura_goodnight_relationship(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Laura "I'm also leaving."
    else:
        ch_Laura "I'm leaving."

    ch_Laura "You'll see me tomorrow."

    return

label Laura_goodnight_love(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Laura "I'm also going to leave, but I'll be close by."
    else:
        ch_Laura "I'm going to leave, but I'll be close by."

    ch_Laura "Sleep well, or else."

    return

label Laura_goodnight_mad(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Laura "I'm going to bed too. . ."
    else:
        ch_Laura "I'm going to bed. . ."

    return

label Laura_goodnight_heartbroken(sleeping_Characters, also_leaving = False):
    $ Laura.change_face("worried1", eyes = "down")

    if also_leaving:
        ch_Laura "Yeah, I'm gone. . ."
    else:
        ch_Laura "I'm gone. . ."

    return

label Laura_goodnight_horny(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Laura "I'll also go. . . prepare yourself for tomorrow, [Laura.Player_petname]. . ." 
    else:
        ch_Laura "I'll go. . . prepare yourself for tomorrow, [Laura.Player_petname]. . ." 

    return

label Laura_goodnight_nympho(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Laura "Guess ah have to go too. . . maybe tomorrow, [Laura.Player_petname]. . ."
        ch_Laura "G'night."
    else:
        ch_Laura "Guess ah have to go. . . maybe tomorrow, [Laura.Player_petname]. . ."
        ch_Laura "G'night."

    return