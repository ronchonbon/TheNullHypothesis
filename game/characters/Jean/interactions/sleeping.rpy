label Jean_getting_late:
    $ Jean.change_face("worried1")

    ch_Jean "It's pretty late, [Jean.Player_petname]. . ."

    return

label Jean_getting_late_relationship:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "It's kinda late already, [Jean.Player_petname]." 

    return

label Jean_getting_late_love:
    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "I really wish it wasn't so late."

    if Player.location != Jean.home:
        ch_Jean "Wanted to hang around for a while longer. . ."
    else:
        ch_Jean "Wanted you to hang around for a while longer. . ."

    return

label Jean_getting_late_mad:
    $ Jean.change_face("angry1")

    ch_Jean "I am not in the mood to lose sleep right now. . ."

    $ Jean.change_face("angry1", eyes = "left")

    return

label Jean_getting_late_heartbroken:
    $ Jean.change_face("angry1", eyes = "right")

    ch_Jean "It's late. . ."

    $ Jean.change_face("worried1", eyes = "left")

    if Player.location != Jean.home:
        ch_Jean "I guess I should just leave or whatever. . ."
    else:
        ch_Jean "I guess you have to leave. . ."

    return

label Jean_getting_late_horny:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "If it wasn't so late. . ."
    ch_Jean ". . . guess it'll just have to wait."

    return

label Jean_getting_late_nympho:
    $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Jean "Ugh, it's way too late to do anything. . ." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    return

label Jean_asked_to_sleepover(sleeping_Characters):
    $ Jean.change_face("confused1", mouth = "smirk")

    if Player.location != Jean.home:
        if len(sleeping_Characters) > 0:
            ch_Jean "Want me to sleep over also, huh?"
        else:
            ch_Jean "Want me to sleep over, huh?"
    else:
        ch_Jean "Want to sleep over, huh?"

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("smirk2", mouth = "lipbite")

        ch_Jean "Of course I want to."

        return True
    else:
        $ Jean.change_face("confused1")

        ch_Jean "Sorry, [Jean.Player_petname]. . ."
        ch_Jean "Not gonna happen tonight." 

    return False

label Jean_asked_to_sleepover_relationship(sleeping_Characters):
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    if Player.location != Jean.home:
        if len(sleeping_Characters) > 0:
            ch_Jean "Also want me to?"
        else:
            ch_Jean "Want me to?"
    else:
        ch_Jean "Want to sleepover?"

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("smirk2", mouth = "lipbite")

        ch_Jean "I guess I could. . ."
        ch_Jean "Make room."

        return True
    else:
        $ Jean.change_face("worried1", mouth = "lipbite")

        ch_Jean "Sorry, [Jean.Player_petname]. Not a good night for that." 
        ch_Jean "Maybe tomorrow."

    return False

label Jean_asked_to_sleepover_love(sleeping_Characters):
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    if Player.location != Jean.home:
        if len(sleeping_Characters) > 0:
            ch_Jean "You want me to stay too, huh?"
        else:
            ch_Jean "You want me to stay, huh?"
    else:
        ch_Jean "You want to stay, huh?"

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "How could I say no to you. . ."
        ch_Jean "Better be thankful, [Jean.Player_petname]."

        return True
    else:
        $ Jean.change_face("worried1", mouth = "lipbite")

        ch_Jean "Sorry, [Jean.Player_petname]. . ." 

        $ Jean.change_face("smirk2")

        ch_Jean "I really want to, but I can't."
        ch_Jean "Maybe tomorrow."

    return False

label Jean_asked_to_sleepover_mad(sleeping_Characters):
    $ Jean.change_face("appalled2")

    ch_Jean "Think that'll just make everything all better?"

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("angry1", eyes = "squint") 

        ch_Jean "Doesn't mean I'm gonna say no. . ."

        return True
    else:
        $ Jean.change_face("angry1")

        ch_Jean "No. . . you're not getting off the hook that easily."
        ch_Jean "Just find me tomorrow or something."

    return False

label Jean_asked_to_sleepover_heartbroken(sleeping_Characters):
    $ Jean.change_face("worried2")

    ch_Jean "Really?"

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("worried1", eyes = "right") 

        ch_Jean "I guess I could. . ."

        $ Jean.change_face("worried1", mouth = "lipbite") 

        return True
    else:
        $ Jean.change_face("worried1", eyes = "right") 

        ch_Jean "I'd rather be alone tonight. . ."

        $ Jean.change_face("worried1") 

    return False

label Jean_asked_to_sleepover_horny(sleeping_Characters):
    $ Jean.change_face("pleased1", mouth = "lipbite")

    ch_Jean "Yeah?"

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Jean "Of course I will. . ."

        $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

        return True
    else:
        $ Jean.change_face("worried1", mouth = "lipbite")

        ch_Jean "I really want to. . ."

        $ Jean.change_face("worried1") 

        ch_Jean "Sorry, [Jean.Player_petname]. Maybe tomorrow."

    return False

label Jean_asked_to_sleepover_nympho(sleeping_Characters):
    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "You better not be joking around. . ."

    $ accepted = False

    if approval_check(Jean, threshold = "sleepover"):
        if len(sleeping_Characters) > 0:
            if are_Characters_in_Partners(sleeping_Characters):
                $ accepted = True
        else:
            $ accepted = True

    if accepted:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "You don't even know how much I need to. . ."

        $ Jean.change_face("sexy", eyes = "down", blush = 1) 

        return True
    else:
        $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Jean "Shit. . . I really can't afford to be up late tonight. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "You don't even know how badly I need to. . ."
        ch_Jean "Just. . . find me tomorrow, okay?"

    return False
    
label Jean_request_sleepover(sleeping_Characters):
    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "I was wondering. . ."

    if len(sleeping_Characters) > 0:
        ch_Jean "I should totally sleep over tonight too, right?"
    else:
        if Player.location == Jean.home:
            ch_Jean "You should totally sleep over tonight, right?"
        else:
            ch_Jean "I should totally sleep over tonight, right?"

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("pleased2")

            ch_Jean "You want me to?"

            $ Jean.change_face("smirk2", mouth = "lipbite")

            ch_Jean "I mean. . . of course you do."

            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("worried1")

            ch_Jean "It's fine. . ."

            $ Jean.change_face("smirk2")

            ch_Jean "See you tomorrow!"

    return False

label Jean_request_sleepover_relationship(sleeping_Characters):
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    if len(sleeping_Characters) > 0:
        ch_Jean "You want me to sleep over tonight too, right [Jean.Player_petname]?"
    else:
        if Player.location == Jean.home:
            ch_Jean "You want to sleep over tonight, right [Jean.Player_petname]?"
        else:
            ch_Jean "You want me to sleep over tonight, right [Jean.Player_petname]?"

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

            ch_Jean "Good."

            $ Jean.change_face("worried1", mouth = "lipbite")

            ch_Jean "Being near you helps me turn my brain off. . ."
            
            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("worried1", mouth = "lipbite")

            ch_Jean "Oh. . . okay."
            ch_Jean "I'll see you tomorrow, then." 

    return False

label Jean_request_sleepover_love(sleeping_Characters):
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    if len(sleeping_Characters) > 0:
        ch_Jean "I'm also sleeping over tonight. . . make some room."
    else:
        if Player.location == Jean.home:
            ch_Jean "You're sleeping over tonight. . ."
        else:
            ch_Jean "I'm sleeping over tonight. . . make some room."

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("sexy", blush = 1)
        
            if Player.location == Jean.home:
                ch_Jean "I knew you wanted to. . ."
            else:
                ch_Jean "I knew you wanted me to. . ."

            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("confused1")

            ch_Jean "Whatever. . . I guess I'll just see you tomorrow."

            $ Jean.change_face("smirk2")

            ch_Jean "Don't miss me too much." 

    return False

label Jean_request_sleepover_mad(sleeping_Characters):
    $ Jean.change_face("angry1", eyes = "squint") 

    ch_Jean "I'm still mad at you, [Jean.Player_petname]. . ."

    if Player.location == Jean.home:
        ch_Jean "So you're sleeping over tonight, to make it up to me."
    else:
        ch_Jean "So you're having me over tonight, to make it up to me."

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("angry1")

            ch_Jean "Good. . ."

            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("appalled2")

            ch_Jean "Ugh, whatever. . ."

            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "Just go away." 

    return False

label Jean_request_sleepover_heartbroken(sleeping_Characters):
    $ Jean.change_face("worried1", eyes = "right") 

    ch_Jean "You're probably gonna say no, but. . ."
    
    if len(sleeping_Characters) > 0:
        ch_Jean "I want to sleep over tonight too."
    else:
        if Player.location == Jean.home:
            ch_Jean "I want you to sleep over tonight."
        else:
            ch_Jean "I want to sleep over tonight."

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("worried2")

            ch_Jean "You're being serious?"

            $ Jean.change_face("neutral")

            ch_Jean "Thanks. . ."

            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("worried2")

            pause 1.0

            $ Jean.change_face("angry1")

            ch_Jean "Whatever. . ."

            $ Jean.change_face("worried1", eyes = "right") 

            ch_Jean "Bye." 

    return False

label Jean_request_sleepover_horny(sleeping_Characters):
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1) 

    if Player.location == Jean.home:
        ch_Jean "You should really sleep over tonight. . ."
    else:
        ch_Jean "I should sleep over tonight. . ."

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Good. . ."
            ch_Jean "You're gonna sleep naked, right?"

            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "Aw, why not. . . ?"

            $ Jean.change_face("neutral") 

            ch_Jean "Whatever, maybe tomorrow." 

    return False

label Jean_request_sleepover_nympho(sleeping_Characters):
    $ Jean.change_face("manic", blush = 1) 

    if Player.location == Jean.home:
        ch_Jean "I really need you to sleep over tonight, [Jean.Player_petname]. . ." 
    else:
        ch_Jean "I really need to sleep over tonight, [Jean.Player_petname]. . ." 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    menu:
        extend ""
        "Sure!":
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

            ch_Jean "Good. . . don't know if I could've waited all the way until tomorrow. . ."

            $ Jean.change_face("sexy", blush = 1) 

            return True
        "Not tonight, [Jean.name].":
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

            ch_Jean "Why not?!"

            $ Jean.change_face("angry1", mouth = "lipbite", blush = 1) 

            ch_Jean "You better at least come see me tomorrow." 
    
    return False
    
label Jean_goodnight(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Jean "Yeah, I also gotta go to bed." 
    else:
        ch_Jean "I gotta go to bed."

    $ Jean.change_face("smirk2")

    ch_Jean "See you tomorrow!"

    return

label Jean_goodnight_relationship(sleeping_Characters, also_leaving = False):
    $ Jean.change_face("worried1", blush = 1)
    
    if also_leaving:
        ch_Jean "I also need to head out."
    else:
        ch_Jean "I need to head out."

    ch_Jean "Not like I can sleep in tomorrow. . ."

    return

label Jean_goodnight_love(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Jean "Yeah, and I'll find you tomorrow."
    else:
        ch_Jean "I'll find you tomorrow."

    ch_Jean "Goodnight, [Jean.Player_petname]."

    return

label Jean_goodnight_mad(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Jean "Yeah, I'm going to bed."
    else:
        ch_Jean "I'm going to bed."

    ch_Jean "I guess I'll see you tomorrow. . ."

    return

label Jean_goodnight_heartbroken(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Jean "Yeah, goodnight. . ."
    else:
        ch_Jean "Goodnight. . ."

    return

label Jean_goodnight_horny(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Jean "I also gotta go."

    ch_Jean "Goodnight, [Jean.Player_petname]. You better dream about me."

    return

label Jean_goodnight_nympho(sleeping_Characters, also_leaving = False):
    if also_leaving:
        ch_Jean "Yeah, I guess it's time for bed. . ."
    else:
        ch_Jean "I guess it's time for bed. . ."

    ch_Jean "You better come see me tomorrow, [Jean.Player_petname]." 

    return