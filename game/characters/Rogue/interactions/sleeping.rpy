label Rogue_getting_late:
    $ Rogue.change_face("worried1")

    ch_Rogue "It's gettin' pretty late, [Rogue.Player_petname]. . ."

    return

label Rogue_getting_late_relationship:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "It's gettin' real late. . ."

    return

label Rogue_getting_late_love:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if Player.location != Rogue.home:
        ch_Rogue "Ah really don't wanna go."
        ch_Rogue "But it's so late already. . ."
    else:
        ch_Rogue "It's so late already. . ."

    return

label Rogue_getting_late_mad:
    $ Rogue.change_face("angry1")

    ch_Rogue "Ah'm tired."

    return

label Rogue_getting_late_heartbroken:
    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "It's real late. . ."
    
    if Player.location != Rogue.home:
        ch_Rogue "Ah reckon you'll just want me to leave. . ."
    else:
        ch_Rogue "Ah reckon you want to leave. . ."

    return

label Rogue_getting_late_horny:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "If only it weren't so late."
    ch_Rogue "Ah'd like to spend some quality time with ya. . ."

    return

label Rogue_getting_late_nympho:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "Oh lord, it's already so late."
    ch_Rogue "Not enough time to do anythin'. . ." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    return

label Rogue_asked_to_sleepover(sleeping_Characters):
    $ Rogue.change_face("worried2")

    if Player.location != Rogue.home:
        if len(sleeping_Characters) > 0:
            ch_Rogue "Ya also want me to sleep over. . . ?"
        else:
            ch_Rogue "Ya want me to sleep over. . . ?"
    else:
        ch_Rogue "Ya want to sleep over?"

    $ Rogue.change_face("worried1", mouth = "lipbite")

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("pleased1", mouth = "lipbite")

        if Player.location != Rogue.home:
            ch_Rogue "Sure. . . ah guess ah could stay."
        else:
            ch_Rogue "Sure. . . ah guess you could stay."

        return True
    else:
        $ Rogue.change_face("confused2")

        ch_Rogue "Sorry. . ."

        $ Rogue.change_face("confused1", mouth = "lipbite")

        ch_Rogue "Ah'd rather not." 

    return False

label Rogue_asked_to_sleepover_relationship(sleeping_Characters):
    $ Rogue.change_face("surprised2", mouth = "lipbite")

    if Player.location != Rogue.home:
        if len(sleeping_Characters) > 0:
            ch_Rogue "Ya also want me to?"
        else:
            ch_Rogue "Ya want me to?"
    else:
        ch_Rogue "Ya want to?"

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Rogue "Gladly. . ."

        return True
    else:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry, [Rogue.Player_petname]. . ." 
        ch_Rogue "Maybe some other night."

    return False

label Rogue_asked_to_sleepover_love(sleeping_Characters):
    $ Rogue.change_face("pleased2")

    if Player.location != Rogue.home:
        if len(sleeping_Characters) > 0:
            ch_Rogue "You want me to also share yer bed?"
        else:
            ch_Rogue "You want me to share yer bed?"
    else:
        ch_Rogue "You want to share my bed?"

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Rogue "You know ah sleep better when you're 'round. . ."
        ch_Rogue "How could ah say no?"

        return True
    else:
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry, not tonight, [Rogue.Player_petname]. . ." 

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah love you."
        ch_Rogue "See ya tomorrow."

    return False

label Rogue_asked_to_sleepover_mad(sleeping_Characters):
    $ Rogue.change_face("appalled2")

    ch_Rogue "That's what yer worried 'bout right now?"

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("angry1", eyes = "right") 

        ch_Rogue "Not like ah'd say no, though. . ."

        return True
    else:
        $ Rogue.change_face("angry1")

        ch_Rogue "Yeah, not happenin' tonight. . ."

        if len(sleeping_Characters) > 0:
            ch_Rogue "Ah'll just see y'all tomorrow."
        else:
            ch_Rogue "Ah'll just see you tomorrow."

    return False

label Rogue_asked_to_sleepover_heartbroken(sleeping_Characters):
    $ Rogue.change_face("worried2")

    if Player.location != Rogue.home:
        ch_Rogue "Ya really want me to?"
    else:
        ch_Rogue "Ya really want to?"

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("worried1", eyes = "down") 

        ch_Rogue "Ah was hopin'. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Ah'd really like to."

        return True
    else:
        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Ah don't. . ."

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah should just go. . . goodnight."

    return False

label Rogue_asked_to_sleepover_horny(sleeping_Characters):
    $ Rogue.change_face("surprised2", mouth = "lipbite")

    if Player.location != Rogue.home:
        ch_Rogue "You want me to?"
    else:
        ch_Rogue "You want to?"

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("smirk2", mouth = "lipbite") 

        if Player.location != Rogue.home:
            ch_Rogue "Ah'd love too. . ."
        else:
            ch_Rogue "Ah'd love that. . ."

        $ Rogue.change_face("smirk2", mouth = "lipbite", eyes = "down")

        return True
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Ah wish. . ."

        $ Rogue.change_face("worried1") 

        ch_Rogue "Ah'll see ya tomorrow."

    return False

label Rogue_asked_to_sleepover_nympho(sleeping_Characters):
    $ Rogue.change_face("manic", blush = 1)

    ch_Rogue "Yer not jokin'. . . right?"

    $ accepted = False

    if approval_check(Rogue, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Rogue.change_face("sexy", blush = 1) 

        if Player.location != Rogue.home:
            ch_Rogue "Lord. . . ah was really hopin' you'd let me. . ."
        else:
            ch_Rogue "Lord. . . ah was really hopin' you'd ask. . ."

        $ Rogue.change_face("sexy", eyes = "down", blush = 1)

        ch_Rogue "Ah've been fixin' to spend some more time with ya. . ."

        return True
    else:
        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

        if Player.location != Rogue.home:
            ch_Rogue "You don't even know how bad ah wanna. . ."
        else:
            ch_Rogue "You don't even know how bad ah want ya to. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "But not tonight."
        ch_Rogue "Could ya. . . at least come see me tomorrow?"

    return False
    
label Rogue_request_sleepover(sleeping_Characters):
    $ Rogue.change_face("worried1")

    if len(sleeping_Characters) > 0:
        ch_Rogue "Ah was wonderin'. . . if maybe ah could also sleep over tonight?"
    else:
        if Player.location == Rogue.home:
            ch_Rogue "Ah was wonderin'. . . if maybe you wanted to sleep over tonight?"
        else:
            ch_Rogue "Ah was wonderin'. . . if maybe ah could sleep over tonight?"

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("pleased2")

            if Player.location == Rogue.home:
                ch_Rogue "Yeah?!"
            else:
                ch_Rogue "Ah can?!"

            $ Rogue.change_face("smirk2")

            ch_Rogue "Ah promise ah won't hog the blanket."

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("worried1")

            ch_Rogue "Alright. . . ah'll see ya tomorrow then. . ."

    return False

label Rogue_request_sleepover_relationship(sleeping_Characters):
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if len(sleeping_Characters) > 0:
        ch_Rogue "Ah was hopin'. . . you'd also want me to sleep over tonight."
    else:
        if Player.location == Rogue.home:
            ch_Rogue "Ah was hopin'. . . you'd want to sleep over tonight."
        else:
            ch_Rogue "Ah was hopin'. . . you'd want me to sleep over tonight."

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("pleased2", blush = 1)

            if Player.location == Rogue.home:
                ch_Rogue "Yeah?!"
            else:
                ch_Rogue "Ah can?!"

            $ Rogue.change_face("smirk2", mouth = "lipbite")

            ch_Rogue "Ah always feel better when ah'm close to you. . ." 

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("worried1")

            ch_Rogue "It's alright. . . ah don't mind. . ."
            ch_Rogue "See ya tomorrow." 

    return False

label Rogue_request_sleepover_love(sleeping_Characters):
    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    if len(sleeping_Characters) > 0:
        ch_Rogue "If it's okay with you. . . ah'd really love to also sleep over."
    else:
        if Player.location == Rogue.home:
            ch_Rogue "If it's okay with you. . . ah'd really love you to sleep over."
        else:
            ch_Rogue "If it's okay with you. . . ah'd really love to sleep over."

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("pleased2", blush = 1)

            pause 1.0

            $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

            ch_Rogue "Thanks. . ."

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("worried1")

            ch_Rogue "Alright. . . ah'll just see ya tomorrow then."

            $ Rogue.change_face("smirk2")

            ch_Rogue "Sleep well, ah love you." 

    return False

label Rogue_request_sleepover_mad(sleeping_Characters):
    $ Rogue.change_face("angry1", eyes = "right") 

    ch_Rogue "Ah'm not in a great mood. . ."
    ch_Rogue "But you should still sleep over."

    if len(sleeping_Characters) > 0:
        ch_Rogue "But I'd still like to sleep over too."
    else:
        if Player.location == Rogue.home:
            ch_Rogue "But you should still sleep over."
        else:
            ch_Rogue "But I'd still like to sleep over."

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("worried1")

            ch_Rogue "Thanks. . ."

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("appalled2")

            ch_Rogue "Ah get it. . . don't mind me then. . ."

            $ Rogue.change_face("angry1")

            ch_Rogue "Goodnight." 

    return False

label Rogue_request_sleepover_heartbroken(sleeping_Characters):
    $ Rogue.change_face("worried1", eyes = "down") 

    if len(sleeping_Characters) > 0:
        ch_Rogue "Ah know ya probably don't want me to. . ."
        ch_Rogue "But can I sleep over tonight too?"
    else:
        if Player.location == Rogue.home:
            ch_Rogue "Ah know ya probably don't wanna. . ."
            ch_Rogue "But would you sleep over tonight?"
        else:
            ch_Rogue "Ah know ya probably don't want me to. . ."
            ch_Rogue "But can I sleep over tonight?"

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("worried2")

            ch_Rogue "Really?"

            $ Rogue.change_face("worried1")

            ch_Rogue "Thanks. . ."

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("worried2")

            ch_Rogue "Ah. . . understand."

            $ Rogue.change_face("worried1", eyes = "down") 

            ch_Rogue "'Night." 

    return False

label Rogue_request_sleepover_horny(sleeping_Characters):
    $ Rogue.change_face("worried1", mouth = "lipbite") 

    ch_Rogue "Ah was wonderin'. . ."

    if len(sleeping_Characters) > 0:
        ch_Rogue "Maybe I could sleep over tonight too?"
    else:
        if Player.location == Rogue.home:
            ch_Rogue "Maybe you'd wanna sleep over tonight?"
        else:
            ch_Rogue "Maybe I could sleep over tonight?"

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("pleased2", mouth = "lipbite")

            ch_Rogue "Really?"

            $ Rogue.change_face("smirk2", mouth = "lipbite")

            ch_Rogue "Thanks. . ."

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("worried2")

            ch_Rogue "It's alright. . ."

            $ Rogue.change_face("worried1") 

            ch_Rogue "Maybe tomorrow." 

    return False

label Rogue_request_sleepover_nympho(sleeping_Characters):
    $ Rogue.change_face("manic", blush = 1) 

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]. . ."

    if len(sleeping_Characters) > 0:
        ch_Rogue "Could ah please sleep over tonight too?"
    else:
        if Player.location == Rogue.home:
            ch_Rogue "Could you please sleep over tonight?"
        else:
            ch_Rogue "Could ah please sleep over tonight?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    menu:
        extend ""
        "Sure!":
            $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1)

            ch_Rogue "Really?!"

            $ Rogue.change_face("sexy", blush = 1)

            if len(sleeping_Characters) > 0:
                ch_Rogue "Thanks. . . ah could really use the extra time with you. . ."
            else:
                ch_Rogue "Thanks. . . ah could really use the extra alone time with you. . ."

            return True
        "Not tonight, [Rogue.name].":
            $ Rogue.change_face("manic", blush = 1) 

            ch_Rogue "Don't worry none. . ."

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

            ch_Rogue "Ah'll be fine. . ."
            ch_Rogue "Maybe you could come see me tomorrow?" 

    return False
    
label Rogue_goodnight(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Rogue "Ah'm also gonna head to bed, see ya tomorrow." 
    else:
        ch_Rogue "Ah'm gonna head to bed, see ya tomorrow."

    return

label Rogue_goodnight_relationship(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Rogue "Yeah, ah'm real tired as well. Ah'll see ya tomorrow." 
    else:
        ch_Rogue "Ah'm real tired. Ah'll see ya tomorrow."

    return

label Rogue_goodnight_love(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Rogue "Ah'm goin' too. . . sweet dreams, [Rogue.Player_petname]."
    else:
        ch_Rogue "Sweet dreams, [Rogue.Player_petname]."

    return

label Rogue_goodnight_mad(sleeping_Characters, also_leaving = False):
    $ Rogue.change_face("angry1", eyes = "right")

    if also_leaving:
        ch_Rogue "Ah'm leavin' too. Ah'll just see ya tomorrow or somethin'. . ."
    else:
        ch_Rogue "Ah'll just see ya tomorrow or somethin'. . ."

    return

label Rogue_goodnight_heartbroken(sleeping_Characters, also_leaving = False):
    $ Rogue.change_face("worried1", eyes = "down")

    if also_leaving:
        ch_Rogue "Yeah, bye. . ."
    else:
        ch_Rogue "Bye. . ."

    return

label Rogue_goodnight_horny(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Rogue "Ah guess ah'm leavin' too."
        ch_Rogue "'Night, [Rogue.Player_petname]. Ah'll be thinkin' about ya."
    else:
        ch_Rogue "'Night, [Rogue.Player_petname]. Ah'll be thinkin' about ya."

    return

label Rogue_goodnight_nympho(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Rogue "Guess ah have to go too. . . maybe tomorrow, [Rogue.Player_petname]. . ."
        ch_Rogue "G'night."
    else:
        ch_Rogue "Guess ah have to go. . . maybe tomorrow, [Rogue.Player_petname]. . ."
        ch_Rogue "G'night."

    return