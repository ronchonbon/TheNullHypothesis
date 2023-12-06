init python:

    def Laura_locker_room_showering():
        label = "Laura_locker_room_showering"

        conditions = [
            "renpy.random.random() > 0.75",

            "Player.location == 'bg_lockers' and Player.behavior == 'showering'",

            "not Present",

            "day - EventScheduler.Events['Laura_locker_room_showering'].completed_when > 1",

            "time_index not in Laura.schedule.keys()",

            "Laura.location not in ['hold', 'bg_lockers']",
            "Laura.original_location != Player.location",

            "Laura.is_in_normal_mood()"]

        repeatable = True

        return EventClass(label, conditions, repeatable = repeatable)

label Laura_locker_room_showering:
    $ ongoing_Event = True

    call send_Characters(Laura, "bg_lockers", behavior = "showering") from _call_send_Characters_101
    
    if Laura in Partners:
        $ Laura.change_face("suspicious1", blush = 1)

        "As you're finishing up, [Laura.name] walks in."

        $ Laura.change_face("sexy", blush = 1)

        call change_Character_stat(Laura, "desire", 0) from _call_change_Character_stat_345

        "Based on her lust filled gaze, it almost seems like she was seeking you out."

        $ Laura.change_face("sexy", eyes = "down", blush = 1)

        "You're topless, in nothing but a bathing suit, and she seems to take notice."
        ch_Laura "It is pleasing to. . . look at you without a shirt. . ." 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

        ch_Laura "I don't intend to stop looking."
        ch_Player "Fine by me."
        "You grab a towel and start to dry off."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)
    else:
        $ Laura.change_face("neutral")

        "As you're finishing up, [Laura.name] walks in."

        $ Laura.change_face("suspicious1", blush = 1)

        call change_Character_stat(Laura, "desire", 0) from _call_change_Character_stat_346

        "She doesn't look the least bit surprised to see you."

        $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2)

        "You're topless, in nothing but a bathing suit, and she seems to take notice."
        ch_Laura "{size=-5}Hmmm{/size}. . ."

        $ Laura.change_face("suspicious1", blush = 2)

        "She just stares at you."
        ch_Player "Everything okay?"
        "You grab a towel and start to dry off."
        ch_Laura "Yes."

        $ Laura.change_face("suspicious1", mouth = "lipbite", blush = 1)

    $ ongoing_Event = False

    return