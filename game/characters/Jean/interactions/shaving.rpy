label Jean_pubic_hair_discussion:
    ch_Player "Hey, can I ask you something?" 

    $ Jean.change_face("happy")

    ch_Jean "Of course!"

    if Player.location in public_locations:
        $ Jean.change_face("confused1")

        ch_Player "Actually. . . never mind, we should probably do this in private."
        ch_Jean "Uhm. . . okay?" 
    else:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "You need help with something?"
        ch_Player "Not exactly." 
        ch_Player "I was wondering if you'd be willing to. . ."
        ch_Player ". . . change up your pubic hair."

        $ Jean.change_face("surprised3", blush = 1)

        if approval_check(Jean, threshold = [400, 375]):
            ch_Jean "You. . ." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Naughty little. . ." 
            ch_Jean "Fine, maybe I could."

            $ Jean.customizable_body_hair = True
        else:
            ch_Jean "Why would I. . ."

            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "Yeah, uh. . . no."

    return

label Jean_pubes_bush_accept:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "So. . . just what I normally do?"
    ch_Jean "Fine, [Jean.Player_petname]."

    return

label Jean_pubes_growing_accept:
    $ Jean.change_face("confused1", blush = 1)

    ch_Jean "I guess I could. . ."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "A bit weird, [Jean.Player_petname]."

    return

label Jean_pubes_hairy_accept:
    $ Jean.change_face("confused1", blush = 1)

    ch_Jean "Just let it grow out?"

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "Kinda weird, [Jean.Player_petname]."
    ch_Jean "But fine, less work for me."

    return

label Jean_pubes_null_accept:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 1)

    ch_Jean "Really? You're not serious. . ."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Oh screw it. You're the only one who'll ever see it anyway."

    return

label Jean_pubes_shaven_accept:
    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "You like it smooth?"

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Fine, [Jean.Player_petname]. I'll clean it up just for you"
    
    return

label Jean_pubes_strip_accept:
    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "A strip?"

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "Okay, [Jean.Player_petname]."

    return

label Jean_pubes_triangle_accept:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "Heh, yeah, I can do that."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    return

label Jean_pubes_need_to_grow:
    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "What?"

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "You're gonna have to be patient, [Jean.Player_petname]."
    ch_Jean "Gotta wait until the hair grows in."

    $ Jean.body_hair_to_grow["pubic"] = Jean.desired_body_hair["pubic"]

    $ EventScheduler.Events["Jean_growing_back"].start()

    return

label Jean_pubes_need_to_shave:
    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    if Player.location in bedrooms:
        ch_Jean "Wait right there. . ."

        call hide_Character(Jean) from _call_hide_Character_9

        "[Jean.name] heads into the bathroom."

        $ fade_to_black(0.4)

        $ Jean.body_hair_growing["pubic"] = False
        $ Jean.body_hair["pubic"] = Jean.desired_body_hair["pubic"]

        pause 2.0

        $ fade_in_from_black(0.4)

        call add_Characters(Jean) from _call_add_Characters_13

        $ Jean.change_face("sexy", eyes = "down", blush = 1) 

        ch_Jean "There you go. . ."

        call expose(Jean, "pussy") from _call_expose_2

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "You're welcome." 

        call change_Outfit(Jean, Jean.Wardrobe.Outfits[Jean.Outfit.name]) from _call_change_Outfit_5
    else:
        ch_Jean "I'll get on that!"

        $ Jean.body_hair_to_shave["pubic"] = Jean.desired_body_hair["pubic"]

    $ Jean.body_hair_to_grow["pubic"] = False
    
    $ EventScheduler.Events["Jean_growing_back"].completed_when = 1e8

    return