init python:

    def Rogue_locker_room_showering():
        label = "Rogue_locker_room_showering"

        conditions = [
            "renpy.random.random() > 0.75",

            "Player.location == 'bg_lockers' and Player.behavior == 'showering'",

            "not Present",

            "day - EventScheduler.Events['Rogue_locker_room_showering'].completed_when > 1",

            "time_index not in Rogue.schedule.keys()",

            "Rogue.location not in ['hold', 'bg_lockers']",
            "Rogue.original_location != Player.location",

            "Rogue.is_in_normal_mood()"]

        repeatable = True

        return EventClass(label, conditions, repeatable = repeatable)

label Rogue_locker_room_showering:
    $ ongoing_Event = True

    call send_Characters(Rogue, "bg_lockers", behavior = "showering") from _call_send_Characters_158
    
    if Rogue in Partners:
        $ Rogue.change_face("smirk2", eyes = "left")

        "As you're finishing up, [Rogue.name] walks in."

        $ Rogue.change_face("surprised2", blush = 1)

        call change_Character_stat(Rogue, "desire", 0) from _call_change_Character_stat_602

        "You're topless in nothing but a bathing suit, and she seems to take notice."
        ch_Rogue "Well ain't that a sight. . ."

        $ Rogue.change_face("sly", eyes = "down", mouth = "lipbite", blush = 2)

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "Ah hope ya don't mind me enjoyin' the view."
        ch_Player "Not at all."
        "You grab a towel and start to dry off."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)
    else:
        $ Rogue.change_face("smirk2", eyes = "left")

        "As you're finishing up, [Rogue.name] walks in."

        $ Rogue.change_face("surprised2", blush = 1)

        call change_Character_stat(Rogue, "desire", 0) from _call_change_Character_stat_603

        ch_Rogue "*gasp*"

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

        "You're topless in nothing but a bathing suit, and she seems to take notice."
        ch_Rogue "{size=-5}My lord{/size}. . ."

        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

        ch_Rogue "Ah'm so sorry for bargin' in on ya. . ."
        ch_Player "Don't worry about it."
        "You grab a towel and start to dry off."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    $ ongoing_Event = False

    return