label Laura_pubic_hair_discussion:
    ch_Player "Hey, can I ask you something?" 

    $ Laura.change_face("confused1")

    ch_Laura "Why wouldn't you just ask your actual question in the first place?"

    if Player.location in public_locations:
        ch_Player "Actually. . . never mind, we should probably do this in private."

        $ Laura.change_face("confused1")

        ch_Laura "What was the point of this conversation?" 

        $ Laura.change_face("suspicious1")

        ch_Laura "Did you hit your head again?"
    else:
        ch_Player "Well, I was just wondering. . ." 
        ch_Player ". . . if you would be willing to change up your pubic hair."

        $ Laura.change_face("confused2", blush = 1)

        if approval_check(Laura, threshold = [325, 375]):
            ch_Laura "'Change up'?" 

            $ Laura.change_face("confused1", eyes = "down", blush = 1)

            ch_Player "Yeah, you know. . . shave it in certain ways. . ."

            $ Laura.change_face("confused1", blush = 1)

            ch_Laura "People do that?" 

            $ Laura.change_face("smirk1", blush = 1)

            ch_Laura "Might as well try it out. . ."
            ch_Laura "I'll just ask [Rogue.public_name] how to do it."

            $ Laura.customizable_body_hair = True
        else:
            ch_Laura "My pubic hair?"

            $ Laura.change_face("confused1", eyes = "down", blush = 1)

            ch_Laura "Weird. . ."

            $ Laura.change_face("confused1")

            ch_Laura "Yeah, not happening."

    return

label Laura_pubes_bush_accept:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Fine, I can do that."

    return

label Laura_pubes_growing_accept:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Let it grow in. . . but only a little bit?"

    $ Laura.change_face("confused1", eyes = "down", blush = 1)

    ch_Laura "Weird, but fine."

    return

label Laura_pubes_hairy_accept:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Just leave it alone?"

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "That's what I normally do."

    return

label Laura_pubes_null_accept:
    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "Marking your territory?"
    ch_Laura "I approve."

    return

label Laura_pubes_shaven_accept:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Just shave it all off?"

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Laura "Easy enough."
    
    return

label Laura_pubes_strip_accept:
    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Just a strip?"
    ch_Laura "Who came up with this?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Whatever."

    return

label Laura_pubes_triangle_accept:
    $ Laura.change_face("confused2", blush = 1)

    ch_Laura "You're not joking?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Fine, I'll do it."

    return

label Laura_pubes_need_to_grow:
    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I might be able to regenerate, but it's not like I can re-grow hair at will."

    $ Laura.change_face("smirk2", blush = 1)

    ch_Laura "You will just wait until it grows back."

    $ Laura.body_hair_to_grow["pubic"] = Laura.desired_body_hair["pubic"]

    $ EventScheduler.Events["Laura_growing_back"].start()

    return

label Laura_pubes_need_to_shave:
    $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

    if Player.location in bedrooms:
        ch_Laura "Be right back. . ."

        call hide_Character(Laura) from _call_hide_Character_19

        "[Laura.name] heads into the bathroom."

        $ fade_to_black(0.4)

        $ Laura.body_hair_growing["pubic"] = False
        $ Laura.body_hair["pubic"] = Laura.desired_body_hair["pubic"]

        pause 2.0

        $ fade_in_from_black(0.4)

        call add_Characters(Laura) from _call_add_Characters_30

        $ Laura.change_face("sly", eyes = "down", blush = 1) 

        ch_Laura "There. . ."

        call expose(Laura, "pussy") from _call_expose_5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Satisfied?" 
        ch_Player "Very."

        call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_10
    else:
        ch_Laura "I'll get on that."

        $ Laura.body_hair_to_shave["pubic"] = Laura.desired_body_hair["pubic"]

    $ Laura.body_hair_to_grow["pubic"] = False

    $ EventScheduler.Events["Laura_growing_back"].completed_when = 1e8

    return