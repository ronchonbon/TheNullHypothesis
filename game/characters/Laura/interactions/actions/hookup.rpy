label Laura_rejects_hookup:
    $ Laura.change_face("angry1", blush = 1) 

    ch_Laura "No."

    return

label Laura_rejects_hookup_mad:
    $ Laura.change_face("appalled3")

    pause 1.0

    $ Laura.change_face("furious")

    ch_Laura "What the hell makes you think I want to do that right now?"

    $ Laura.change_face("suspicious1")

    ch_Laura "{i}Grrrrrr{/i}"
    ch_Laura "Fuck off."

    return

label Laura_rejects_hookup_public:
    $ Laura.change_face("confused3", blush = 1)

    pause 1.0

    $ Laura.change_face("confused1", eyes = "right", blush = 1)

    ch_Laura "We're not alone."

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "Why the hell would we do that with other people around?"

    return

label Laura_rejects_hookup_threesome:
    $ Laura.change_face("appalled2", eyes = "right", blush = 1)

    python:
        for G in Present:
            if G in all_Girls and G != Laura:
                G.change_face("suspicious1", blush = 1)

    pause 1.0

    $ Laura.change_face("furious", blush = 1)

    call change_Girl_stat(Laura, "trust", -6) from _call_change_Girl_stat_462

    if len(Present) > 2:
        ch_Laura "{i}If{/i} they leave."
    elif len(Present) == 2:
        ch_Laura "{i}If{/i} she leaves."

    $ Laura.change_face("suspicious1")

    ch_Laura "I should make {i}you{/i} leave."

    return

label Laura_accepts_hookup_first_time:
    $ Laura.change_face("surprised1", blush = 1)

    ch_Laura "You want to.  . . fool around?" 

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "Fine, I trust you enough." 
    ch_Laura "But only for a little bit."

    return

label Laura_accepts_hookup_second_time:

    return

label Laura_accepts_hookup:
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "I am in the mood. . ."
    elif dice_roll == 2:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "Want to mess around?"
        ch_Laura "Good, I was just getting in the mood. . ."
    
    return

label Laura_accepts_hookup_love:

    return

label Laura_rejects_Action_asked_once:
    $ Laura.change_face("angry1") 

    ch_Laura "Don't make me repeat myself."

    return

label Laura_rejects_Action_asked_twice:
    $ Laura.change_face("furious") 

    ch_Laura "{i}Grrrrrr{/i}"

    call stop_all_Actions(close_interface = True) from _call_stop_all_Actions

    if Player.location == Laura.home:
        "She forcefully shoves you out of the room, slamming the door shut behind you."
    else:
        "She storms out of the room, slamming the door behind her."
        
    call getting_kicked_out(Laura) from _call_getting_kicked_out_22

    return

label Laura_accepts_Action_again:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Laura "You can keep going. . . ?"

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Good."
    elif dice_roll == 2:
        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "Again. . . ?"

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "I could go all day. . ."
    elif dice_roll == 3:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "You're not worn out yet?"

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "Good. . ."

    return