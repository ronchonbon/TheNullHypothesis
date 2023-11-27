init python:

    def Laura_Rogue_explaining_feelings_setup():
        label = "Laura_Rogue_explaining_feelings_setup"

        conditions = [
            "Laura.location not in ['hold', Player.location, Player.destination]",
            "Rogue.location not in ['hold', Player.location, Player.destination]",
            
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_Rogue_explaining_feelings'].completed",

            "time_index not in Laura.schedule.keys()",
            "time_index not in Rogue.schedule.keys()",

            "EventScheduler.Events['Laura_first_friend_part_two'].completed and not EventScheduler.Events['Laura_first_friend_part_three'].completed",

            "Laura.is_in_normal_mood()",
            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_Rogue_explaining_feelings_setup:
    call send_Characters(Laura, Laura.home, behavior = False) from _call_send_Characters_307
    call send_Characters(Rogue, Laura.home, behavior = False) from _call_send_Characters_308

    return

init python:

    def Laura_Rogue_explaining_feelings():
        label = "Laura_Rogue_explaining_feelings"

        conditions = [
            "Player.destination == Laura.home",
            
            "Laura.location == Laura.home and Rogue.location == Laura.home",

            "EventScheduler.Events['Laura_first_friend_part_two'].completed and not EventScheduler.Events['Laura_first_friend_part_three'].completed",

            "Laura.is_in_normal_mood()",
            "Rogue.is_in_normal_mood()"]

        traveling = True

        markers = {
            Laura.home: [
                "Player.location != Laura.home",
                
                "Laura.location == Laura.home and Rogue.location == Laura.home",

                "EventScheduler.Events['Laura_first_friend_part_two'].completed and not EventScheduler.Events['Laura_first_friend_part_three'].completed",

                "Laura.is_in_normal_mood()",
                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_Rogue_explaining_feelings:
    $ ongoing_Event = True

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_109
    
    "You can hear a conversation through the door."
    ch_Laura "And you think I have a 'crush' on [Player.first_name]?"
    ch_Rogue "Well ain't it obvious?"
    ch_Rogue "It's clear ya got plenty of feelin's for him."
    ch_Laura "Those feelings are normal?"
    ch_Laura "They just feel like a handicap."
    ch_Rogue "Aw, cmon darlin'. . ."
    ch_Rogue "They're not a handicap."

    call knock_on_door(times = 2) from _call_knock_on_door_4

    "You knock on the door."

    $ Rogue.name = Rogue.temp

    $ Laura.name = Laura.temp

    ch_Laura "Who is it?"
    ch_Player "[Laura.name]? It's me."
    ch_Rogue "Sorry, [Player.first_name]."
    ch_Rogue "Could ya come back later?"
    ch_Rogue "[Laura.public_name] and ah were havin' a chat. . ."

    $ Laura.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_16

    $ ongoing_Event = False

    return