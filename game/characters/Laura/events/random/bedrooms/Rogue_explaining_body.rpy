init python:

    def Laura_Rogue_explaining_body_setup():
        label = "Laura_Rogue_explaining_body_setup"

        conditions = [
            "Laura.location != Player.location",
            "Rogue.location != Player.location",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_Rogue_explaining_body'].completed",

            "time_index not in Laura.schedule.keys()",
            "time_index not in Rogue.schedule.keys()",

            "EventScheduler.Events['Laura_first_friend_part_two'].completed",

            "Laura.is_in_normal_mood()",
            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_Rogue_explaining_body_setup:
    call send_Characters(Laura, Laura.home, behavior = False) from _call_send_Characters_305
    call send_Characters(Rogue, Laura.home, behavior = False) from _call_send_Characters_306

    return

init python:

    def Laura_Rogue_explaining_body():
        label = "Laura_Rogue_explaining_body"

        conditions = [
            "Player.destination == Laura.home",

            "Laura.location == Laura.home and Rogue.location == Laura.home",

            "EventScheduler.Events['Laura_first_friend_part_two'].completed",

            "Laura.is_in_normal_mood()",
            "Rogue.is_in_normal_mood()"]
            
        traveling = True

        markers = {
            Laura.home: [
                "Laura.location == Laura.home and Rogue.location == Laura.home",

                "EventScheduler.Events['Laura_first_friend_part_two'].completed",

                "Laura.is_in_normal_mood()",
                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_Rogue_explaining_body:
    $ ongoing_Event = True

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_108

    "You hear a heated conversation behind the door."
    ch_Rogue "Are you alright darlin'?"
    ch_Rogue "Why did ya drag me here in such a rush?"
    ch_Laura "I am {i}not{/i} alright."
    ch_Laura "My body is betraying me."
    ch_Laura "Whenever I even look at [Player.first_name], I. . ."

    show expression "images/effects/crash.webp" as crash onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 0.5 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    ch_Laura "GAH!"
    ch_Rogue "Oh sweetie. . ."
    ch_Rogue "Ah know this is all new to you."
    ch_Rogue "Don't be so hard on yerself."
    ch_Laura "{i}Grrrrrr{/i}. . ." 

    call knock_on_door(times = 2) from _call_knock_on_door_3

    "You knock on the door."
    ch_Laura "GO AWAY!"
    ch_Player "I should probably come back later. . ."
    ch_Rogue "[Player.first_name]? Sorry, ah'm helpin' X-23 work through some. . . issues. . ."

    $ Laura.name = Laura.temp

    $ Rogue.name = Rogue.temp

    $ ongoing_Event = False

    $ Laura.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_15

    return