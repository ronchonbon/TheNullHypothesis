label Rogue_pubic_hair_discussion:
    ch_Player "Hey, can I ask you something?"

    $ Rogue.change_face("worried2")

    if Player.location in public_locations:
        ch_Player "Actually. . . never mind, we should probably do this in private."

        $ Rogue.change_face("confused1")

        ch_Rogue "Alright, [Rogue.Player_petname]."
    else:
        ch_Rogue "Sure, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1")

        ch_Rogue "Is everythin' alright?"
        ch_Player "It's nothing bad, I was just wondering. . ."
        ch_Player ". . . if you would be willing to change up your pubic hair."

        $ Rogue.change_face("worried3", blush = 1)

        if approval_check(Rogue, threshold = [425, 425]):
            ch_Rogue "My. . ."

            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

            ch_Rogue "Well. . . ah guess ah could try. . . if ya wanted."
            ch_Rogue "Just let me know what ya want."

            $ Rogue.customizable_pubes = True
        else:
            ch_Rogue "Ah don't. . ."
            ch_Rogue "Uhm, ah. . ."
            
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

            ch_Rogue "Sorry. . . ah'd rather not. . ."

    return

label Rogue_pubes_bush_accept:
    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Sure thing, [Rogue.Player_petname]."
    ch_Rogue "Ah usually keep it like that."

    return

label Rogue_pubes_growing_accept:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Rogue "Just want me to let it grow in a little bit. . . ?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah can do that, [Rogue.Player_petname]."

    return

label Rogue_pubes_hairy_accept:
    $ Rogue.change_face("confused2", mouth = "lipbite", blush = 1)

    ch_Rogue "Ya want me to let it grow all the way out. . . ?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Alright, ah will [Rogue.Player_petname]."

    return

label Rogue_pubes_null_accept:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "A null symbol. . . ?"

    $ Rogue.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Rogue "Well. . . it is all yours and only yours."
    ch_Rogue "Ah'll get right on it, [Rogue.Player_petname]."

    return

label Rogue_pubes_shaven_accept:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Rogue "Want it all off?"

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah'll make it nice 'n smooth, just for you [Rogue.Player_petname]."

    return

label Rogue_pubes_strip_accept:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Want it like a strip?"

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Sure, [Rogue.Player_petname]."

    return

label Rogue_pubes_triangle_accept:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Shave it like a triangle?"

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Alright, ah'll try [Rogue.Player_petname]."

    return

label Rogue_pubes_need_to_grow:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah'm sorry, [Rogue.Player_petname]."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Gonna have to let the hair down there grow out. . ."
    ch_Rogue ". . . before ah can make it the way ya want."

    $ Rogue.pubes_to_grow = Rogue.desired_pubes

    $ EventScheduler.Events["Rogue_growing_back"].start()

    return

label Rogue_pubes_need_to_shave:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if Player.location in bedrooms:
        ch_Rogue "Ah'll just go shave it real quick. . ."

        call hide_Character(Rogue) from _call_hide_Character_29

        "[Rogue.name] heads into the bathroom."

        $ fade_to_black(0.4)

        $ Rogue.pubes_growing = False
        $ Rogue.pubes = Rogue.desired_pubes

        pause 2.0

        $ fade_in_from_black(0.4)

        call add_Characters(Rogue) from _call_add_Characters_46

        $ Rogue.change_face("sexy", eyes = "down", blush = 1) 

        ch_Rogue "Here. . ."

        call expose(Rogue, "pussy") from _call_expose_11

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Happy?" 
        ch_Player "Very."

        call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_20
    else:
        ch_Rogue "Ah'll do that when ah get a chance."

        $ Rogue.pubes_to_shave = Rogue.desired_pubes

    $ Rogue.pubes_to_grow = False
    
    $ EventScheduler.Events["Rogue_growing_back"].completed_when = 1e8

    return