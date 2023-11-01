init python:

    def Laura_locker_room_changing():
        label = "Laura_locker_room_changing"

        conditions = [
            "day - EventScheduler.Events['Laura_locker_room_changing'].completed > 0",
            "Player.destination == 'bg_lockers'",
            "Laura.location == 'bg_lockers'",
            "Laura.changing"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Laura_locker_room_changing:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_lockers") from _call_remove_Characters_311
    call send_Characters(Laura, "bg_lockers", behavior = "changing") from _call_send_Characters_288
    call change_Outfit(Laura, Laura.Wardrobe.gym_Outfit, instant = True) from _call_change_Outfit_9
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_117

    if Laura in Partners:
        if Laura.History.check("seen_breasts") and Laura.History.check("seen_pussy"):
            $ Laura.change_face("neutral", eyes = "down")

            "You walk in and see [Laura.name]. . ."

            $ Laura.change_face("sly", blush = 1)

            "As soon as you're through the door, she glances up at you."

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You can watch. . ."

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "There is nobody else here . . ." 

            $ Laura.change_face("sexy", eyes = "left", blush = 2)

            pause 1.0

            $ Laura.change_face("sexy", eyes = "right", blush = 2)

            pause 1.0

            $ Laura.change_face("sexy", eyes = "down", blush = 2)

            "After making sure nobody is coming, [Laura.name] gets right back to changing."

            call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_341

            call take_off_everything_but(Laura, ["bra", "underwear"]) from _call_take_off_everything_but_5

            pause 2.0

            $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

            call take_off(Laura, "bra", redress = False) from _call_take_off_3
            call take_off(Laura, "underwear", redress = False) from _call_take_off_4

            "She just stands there for a few seconds, giving you a good look."

            pause 2.0

            $ Laura.changing = False
            $ Laura.showering = True

            call set_Character_Outfits(Laura, instant = False) from _call_set_Character_Outfits_2

            $ Laura.change_face("sexy", eyes = "down", blush = 2)

            ch_Laura "It was as much for me as it was for you. . ."
        else:
            $ Laura.change_face("neutral", eyes = "down")

            "You walk in and see [Laura.name]. . ."

            $ Laura.change_face("sly", blush = 1)

            "As soon as you're through the door, she glances up at you."

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You can watch. . ."

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "There is nobody else here . . ." 

            $ Laura.change_face("sexy", eyes = "left", blush = 2)

            pause 1.0

            $ Laura.change_face("sexy", eyes = "right", blush = 2)

            pause 1.0

            $ Laura.change_face("sexy", eyes = "down", blush = 2)

            "After making sure nobody is coming, [Laura.name] gets right back to changing."

            call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_342
            call take_off_everything_but(Laura, ["bra", "underwear"]) from _call_take_off_everything_but_6

            pause 1.0

            $ Laura.change_face("confused1", eyes = "right", mouth = "lipbite", blush = 3)

            pause 1.0

            ch_Laura "Hmmm. . ."

            call hide_Character(Laura) from _call_hide_Character_16
            
            $ Laura.location = "nearby"

            "She walks off behind a locker, keeping her eyes on you."
            "You notice it's almost as if she looks satisfied that you watch, as she walks out of sight."

            call send_Characters(Laura, "bg_lockers", behavior = "showering") from _call_send_Characters_98

            $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Laura "You are welcome. . ." 
    elif approval_check(Laura, threshold = "relationship"):
        $ Laura.change_face("neutral", eyes = "down")

        "You walk in and see [Laura.name]. . ."
        "But, as soon as you're through the door. . ."

        $ Laura.change_face("suspicious1", blush = 1)

        ch_Laura "So it is you. . ."

        $ Laura.change_face("angry1", eyes = "left", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Laura.change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2)

        "After making sure nobody else is around, [Laura.name] gets right back to changing."

        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_343
        call take_off_everything_but(Laura, ["bra", "underwear"]) from _call_take_off_everything_but_7

        pause 1.0

        $ Laura.change_face("suspicious1", mouth = "lipbite", blush = 3)

        pause 1.0

        ch_Laura "Hmmm. . ."

        call hide_Character(Laura) from _call_hide_Character_17
            
        $ Laura.location = "nearby"

        "She walks off behind a locker, keeping her eyes on you."
        "You notice it's almost as if she looks satisfied that you watch, as she walks out of sight."

        call send_Characters(Laura, "bg_lockers", behavior = "showering") from _call_send_Characters_99

        $ Laura.change_face("neutral", eyes = "squint", blush = 1) 
    else:
        $ Laura.change_face("neutral", eyes = "down")

        call undress(Laura, "bodysuit", state = 1) from _call_undress_16

        "You walk in and see [Laura.name]. . ."
        "But, as soon as you're through the door. . ."

        call fix(Laura, "bodysuit") from _call_fix_4

        $ Laura.change_face("suspicious1", blush = 1)

        ch_Player "Sorry, I assume you heard me coming?"
        ch_Laura "Yes."

        $ Laura.change_face("angry1", blush = 2)

        ch_Laura "You are. . ."

        $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 3)

        ch_Laura "Hard to miss. . ."

        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_344
        call hide_Character(Laura) from _call_hide_Character_18
            
        $ Laura.location = "nearby"

        pause 1.0

        call send_Characters(Laura, "bg_lockers", behavior = "showering") from _call_send_Characters_100

        $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    $ Laura.schedule[time_index] = ["bg_lockers", "showering"]

    $ ongoing_Event = False
    
    return