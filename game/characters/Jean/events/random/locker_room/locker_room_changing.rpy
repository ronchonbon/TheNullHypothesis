init python:

    def Jean_locker_room_changing():
        label = "Jean_locker_room_changing"

        conditions = [
            "Player.destination == 'bg_lockers' and Jean.location == 'bg_lockers'",
            "Jean.behavior == 'changing'",

            "day - EventScheduler.Events['Jean_locker_room_changing'].completed_when > 1",

            "Jean.is_in_normal_mood()"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Jean_locker_room_changing:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_lockers") from _call_remove_Characters_310
    call send_Characters(Jean, "bg_lockers", behavior = "changing") from _call_send_Characters_287
    call change_Outfit(Jean, Jean.Wardrobe.superhero_Outfit, instant = True) from _call_change_Outfit_2
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_38

    if Jean in Partners:
        if Jean.History.check("seen_breasts") and Jean.History.check("seen_pussy"):
            $ Jean.change_face("neutral", eyes = "down")

            "You walk in and see [Jean.name]. . ."

            $ Jean.change_face("surprised2", blush = 1)

            "Your footfalls prompt her to look up."

            $ Jean.change_face("pleased2", blush = 1)

            $ temp = Jean.Player_petname.capitalize()

            ch_Jean "[temp]!"

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "Since it's just the two of us in here. . ."

            $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Jean.change_face("sly", eyes = "down", mouth = "lipbite", blush = 2)

            "After making sure nobody else is around, [Jean.name] gets right back to changing."

            call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_65
        
            call take_off_everything_but(Jean, ["bra", "underwear"]) from _call_take_off_everything_but

            pause 2.0

            $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

            call take_off(Jean, "bra") from _call_take_off
            call take_off(Jean, "underwear") from _call_take_off_1

            "She just stands there for a few seconds, giving you a good look."

            pause 2.0

            $ Jean.behavior = "showering"

            call set_Character_Outfits(Jean, instant = False) from _call_set_Character_Outfits

            ch_Jean "You're lucky I'm so generous. . ." 
        else:
            $ Jean.change_face("neutral", eyes = "down")

            "You walk in and see [Jean.name]. . ."

            $ Jean.change_face("surprised2", blush = 1)

            "Your footfalls prompt her to look up."

            $ Jean.change_face("pleased2", blush = 1)

            $ temp = Jean.Player_petname.capitalize()

            ch_Jean "[temp]?"

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "Since it's just us. . ."

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "I'll let you watch."

            $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

            "After making sure nobody else is around, [Jean.name] gets right back to changing."

            call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_66
        
            call take_off_everything_but(Jean, ["bra", "underwear"]) from _call_take_off_everything_but_1

            pause 1.0

            $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

            pause 1.0

            ch_Jean "I'm just gonna. . . go over here. . ."

            call hide_Character(Jean) from _call_hide_Character_6

            "She saunters off, undoubtedly hoping your eyes follow her."

            call send_Characters(Jean, "bg_lockers", behavior = "showering") from _call_send_Characters_41

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

            ch_Jean "You better have enjoyed that. . ." 
    elif approval_check(Jean, threshold = "relationship"):
        $ Jean.change_face("neutral", eyes = "down")

        "You walk in and see [Jean.name]. . ."

        $ Jean.change_face("surprised2", blush = 1)

        "Your footfalls prompt her to look up."

        $ Jean.change_face("pleased2", blush = 1)

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]?!"

        $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

        "After making sure nobody else is around, [Jean.name] gets right back to changing."

        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_67
        
        call take_off_everything_but(Jean, ["bra", "underwear"]) from _call_take_off_everything_but_2

        pause 1.0

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

        pause 1.0

        ch_Jean "I'm just gonna. . . go over here. . ."

        call hide_Character(Jean) from _call_hide_Character_7

        "She saunters off, undoubtedly hoping your eyes follow her."

        call send_Characters(Jean, "bg_lockers", behavior = "showering") from _call_send_Characters_42

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)
    else:
        $ Jean.change_face("neutral", eyes = "down")

        "You walk in and see [Jean.name]. . ."
        
        call take_off_everything_but(Jean, ["bra", "underwear"]) from _call_take_off_everything_but_3

        "Your footfalls prompt her to look up."

        $ Jean.change_face("perplexed", blush = 1)

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]?!"

        # call try_on(Jean, Jean.Wardrobe.Clothes["towel"]) from _call_try_on_2

        $ Jean.change_face("worried1", mouth = "smirk", blush = 2)

        "She throws a towel over herself with lightning speed."
        ch_Jean "Heh, woops. . ."
        ch_Jean "I'm just gonna. . ."

        call change_Companion_stat(Jean, "desire", 0) from _call_change_Companion_stat_68

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

        call hide_Character(Jean) from _call_hide_Character_8

        pause 1.0

        call send_Characters(Jean, "bg_lockers", behavior = "showering") from _call_send_Characters_43

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Sorry, I wasn't paying attention. . ."

    $ Jean.schedule[time_index] = ["bg_lockers", "showering"]

    $ ongoing_Event = False
    
    return