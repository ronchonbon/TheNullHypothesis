init python:

    def Jean_locker_room_showering():
        label = "Jean_locker_room_showering"

        conditions = [
            "renpy.random.random() > 0.75",

            "Player.location == 'bg_lockers' and Player.behavior == 'showering'",

            "not Present",

            "day - EventScheduler.Events['Jean_locker_room_showering'].completed_when > 1",

            "time_index not in Jean.schedule.keys()",

            "Jean.location not in ['hold', 'bg_lockers']",
            "Jean.original_location != Player.location",

            "Jean.is_in_normal_mood()"]

        repeatable = True

        return EventClass(label, conditions, repeatable = repeatable)

label Jean_locker_room_showering:
    $ ongoing_Event = True

    call send_Characters(Jean, "bg_lockers", behavior = "showering") from _call_send_Characters_44
    
    if Jean in Partners:
        $ Jean.change_face("smirk2", eyes = "left")

        "As you're finishing up, [Jean.name] walks in."

        $ Jean.change_face("pleased2", blush = 1)

        call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_69

        "You're topless in nothing but a bathing suit, and she seems to take notice."
        ch_Jean "Jesus, you look. . . {i}hot{/i}. . ."

        $ Jean.change_face("sly", eyes = "down", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Jean.change_face("sexy", blush = 2)

        ch_Jean "Don't mind me, just taking in the view."
        ch_Player "Be my guest."
        "You grab a towel and start to dry off."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)
    else:
        $ Jean.change_face("smirk2", eyes = "left")

        "As you're finishing up, [Jean.name] walks in."

        $ Jean.change_face("surprised2", blush = 1)

        call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_70

        ch_Jean "*gasp*"

        $ Jean.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2)

        "You're topless in nothing but a bathing suit, and she seems to take notice."
        ch_Jean "Well, {size=-5}goddamn{/size}. . ."

        $ Jean.change_face("confused1", mouth = "lipbite", blush = 2)

        ch_Jean "I'm. . . {size=-5}a little bit{/size}. . . sorry about barging in like that. . ."
        ch_Player "Don't worry about it."
        "You grab a towel and start to dry off."

        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    $ ongoing_Event = False

    return