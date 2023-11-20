init python:

    def Rogue_Laura_asks_about_body_setup():
        label = "Rogue_Laura_asks_about_body_setup"

        conditions = [
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Rogue_Laura_asks_about_body'].completed",

            "time_index not in Rogue.schedule.keys()",
            "time_index not in Laura.schedule.keys()",

            "EventScheduler.Events['Laura_first_friend_part_two'].completed",

            "Rogue.is_in_normal_mood()",
            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_Laura_asks_about_body_setup:
    call send_Characters(Rogue, Rogue.home, behavior = False) from _call_send_Characters_322
    call send_Characters(Laura, Rogue.home, behavior = False) from _call_send_Characters_323

    return

init python:

    def Rogue_Laura_asks_about_body():
        label = "Rogue_Laura_asks_about_body"

        conditions = [
            "Player.destination == Rogue.home",
            
            "Rogue.location == Rogue.home and Laura.location == Rogue.home",
            
            "EventScheduler.Events['Laura_first_friend_part_two'].completed",

            "Rogue.is_in_normal_mood()",
            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            Rogue.home: [
                "Rogue.location == Rogue.home and Laura.location == Rogue.home",
                
                "EventScheduler.Events['Laura_first_friend_part_two'].completed",

                "Rogue.is_in_normal_mood()",
                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Rogue_Laura_asks_about_body:
    $ ongoing_Event = True

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_186

    "You hear talking inside the room."
    ch_Laura "But why does my body do shit like this?"
    ch_Laura "Why does it. . . whenever I see [Player.first_name]. . ."
    ch_Laura "{i}Grrrrr{/i}"
    ch_Rogue "Aw, don't get mad at yerself."
    ch_Rogue "It's normal to have feelin's."
    ch_Rogue "Not to mention. . . [Player.first_name] is very. . . attractive. . . and nice. . . and. . ."
    
    call knock_on_door(times = 2) from _call_knock_on_door_15

    "You knock on the door."
    ch_Player "It's me! Can I come in?"
    ch_Rogue "[Player.first_name]?!"

    $ Rogue.name = Rogue.temp

    $ Laura.name = Laura.temp

    call set_the_scene(location = Rogue.home) from _call_set_the_scene_187

    $ Rogue.change_face("surprised2", blush = 1)
    $ Laura.change_face("perplexed")

    ch_Rogue "Ah was just havin' a chat with X-23."
    
    $ Laura.change_face("neutral")

    pause 1.0

    $ Laura.change_face("angry1")
    
    ch_Laura "About you."

    $ Rogue.change_face("worried2")

    if Laura.sprite_position[0] > Rogue.sprite_position[0]:
        $ Rogue.eyes = "right"
    else:
        $ Rogue.eyes = "left"

    ch_Player "Didn't mean to interrupt. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "We were only sayin' good things 'bout ya. . ."
    ch_Laura "I'm leaving."

    call remove_Characters(Laura) from _call_remove_Characters_180

    $ ongoing_Event = False

    return