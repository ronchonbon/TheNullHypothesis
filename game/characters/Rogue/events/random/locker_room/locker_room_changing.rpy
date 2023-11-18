init python:

    def Rogue_locker_room_changing():
        label = "Rogue_locker_room_changing"

        conditions = [
            "day - EventScheduler.Events['Rogue_locker_room_changing'].completed > 0",
            "Player.destination == 'bg_lockers'",
            "Rogue.location == 'bg_lockers'",
            "Rogue.changing"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Rogue_locker_room_changing:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_lockers") from _call_remove_Characters_312
    call send_Characters(Rogue, "bg_lockers", behavior = "changing") from _call_send_Characters_289
    call change_Outfit(Rogue, Rogue.Wardrobe.gym_Outfit, instant = True) from _call_change_Outfit_15
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_196

    if Rogue in Partners:
        if Rogue.History.check("seen_breasts") and Rogue.History.check("seen_pussy"):
            $ Rogue.change_face("neutral", eyes = "down")

            "You walk in and see [Rogue.name]. . ."

            $ Rogue.change_face("surprised2", blush = 1)

            "Your footfalls prompt her to look up."

            $ Rogue.change_face("pleased1", blush = 1)

            ch_Rogue "Howdy!"

            $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Rogue "If yer the only one around. . ."

            $ Rogue.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Rogue.change_face("sly", eyes = "down", mouth = "lipbite", blush = 2)

            "After making sure nobody else is around, [Rogue.name] gets right back to changing."

            call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_598

            call take_off_everything_but(Rogue, ["bra", "underwear"]) from _call_take_off_everything_but_9

            pause 2.0

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

            call take_off(Rogue, "bra", redress = False) from _call_take_off_5
            call take_off(Rogue, "underwear", redress = False) from _call_take_off_6

            "She just stands there for a few seconds, giving you a good look."

            pause 2.0

            $ Rogue.changing = False
            $ Rogue.showering = True

            call set_Character_Outfits(Rogue, instant = False) from _call_set_Character_Outfits_4

            ch_Rogue "Yer welcome. . ." 
        else:
            $ Rogue.change_face("neutral", eyes = "down")

            "You walk in and see [Rogue.name]. . ."

            $ Rogue.change_face("surprised2", blush = 1)

            "Your footfalls prompt her to look up."

            $ Rogue.change_face("pleased1", blush = 1)

            ch_Rogue "Oh. . ."

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "If it's only you, ah don't mind lettin' ya watch. . ."

            $ Rogue.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

            "After making sure nobody else is around, [Rogue.name] gets right back to changing."

            call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_599

            call take_off_everything_but(Rogue, ["bra", "underwear"]) from _call_take_off_everything_but_10

            pause 1.0

            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

            pause 1.0

            ch_Rogue "Ah'll. . . be right back. . ."

            call hide_Character(Rogue) from _call_hide_Character_26

            $ Rogue.location = "nearby"

            "She saunters off, undoubtedly hoping your eyes follow her."

            call send_Characters(Rogue, "bg_lockers", behavior = "showering") from _call_send_Characters_155

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Yer welcome. . ." 
    elif approval_check(Rogue, threshold = "relationship"):
        $ Rogue.change_face("neutral", eyes = "down")

        "You walk in and see [Rogue.name]. . ."

        $ Rogue.change_face("surprised2", blush = 1)

        "Your footfalls prompt her to look up."

        $ Rogue.change_face("pleased1", blush = 1)

        ch_Rogue "Oh, it's only you. . ."

        $ Rogue.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

        "After making sure nobody else is around, [Rogue.name] gets right back to changing."

        call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_600

        call take_off_everything_but(Rogue, ["bra", "underwear"]) from _call_take_off_everything_but_11

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

        pause 1.0

        ch_Rogue "Ah'll. . . be right back. . ."

        call hide_Character(Rogue) from _call_hide_Character_27
            
        $ Rogue.location = "nearby"

        "She saunters off, undoubtedly hoping your eyes follow her."

        call send_Characters(Rogue, "bg_lockers", behavior = "showering") from _call_send_Characters_156

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)
    else:
        $ Rogue.change_face("neutral", eyes = "down")

        "You walk in and see [Rogue.name]. . ."

        call take_off_everything_but(Rogue, ["bra", "underwear"]) from _call_take_off_everything_but_12

        "Your footfalls prompt her to look up."

        $ Rogue.change_face("surprised2", blush = 1)

        ch_Rogue "*gasp*"

        call try_on(Rogue, Rogue.Wardrobe.Clothes["towel"]) from _call_try_on_10

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        "She throws a towel over herself with lightning speed."
        ch_Rogue "Ah'm so sorry [Player.first_name]."
        ch_Rogue "Ah didn't mean to. . ."

        call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_601

        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

        call hide_Character(Rogue) from _call_hide_Character_28
            
        $ Rogue.location = "nearby"

        pause 1.0

        call send_Characters(Rogue, "bg_lockers", behavior = "showering") from _call_send_Characters_157

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Sorry 'bout that. . ."

    $ Rogue.schedule[time_index] = ["bg_lockers", "showering"]

    $ ongoing_Event = False
    
    return