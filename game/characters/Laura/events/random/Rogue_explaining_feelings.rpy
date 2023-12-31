init python:

    def Laura_Rogue_explaining_feelings():
        label = "Laura_Rogue_explaining_feelings"

        conditions = [
            "Player.destination == Laura.home",
            "Laura.location == Laura.home and Rogue.location == Laura.home",
            "EventScheduler.Events['Laura_first_friend_part_two'].completed and not EventScheduler.Events['Laura_first_friend_part_three'].completed"]

        traveling = True

        return EventClass(label, conditions, traveling = traveling)

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
    ch_Rogue "X-23 and ah were havin' a chat. . ."

    $ ongoing_Event = False

    $ Laura.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_16

    return