init python:

    def Rogue_Laura_asks_about_Player():
        label = "Rogue_Laura_asks_about_Player"

        conditions = [
            "Player.destination == Rogue.home",
            "Rogue.location == Rogue.home and Laura.location == Rogue.home",
            "EventScheduler.Events['Laura_first_friend_part_two'].completed",
            "not Rogue in Partners and not Laura in Partners"]

        traveling = True

        return EventClass(label, conditions, traveling = traveling)

label Rogue_Laura_asks_about_Player:
    $ ongoing_Event = True

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_185

    "You can hear a conversation through the door."
    ch_Laura "You're closer with [Player.first_name]."
    ch_Laura "Tell me more about him."
    ch_Rogue "Why do ya want to know?"
    ch_Rogue "He seems like a real nice guy. . ."
    ch_Laura "Would you consider him attractive?"
    ch_Rogue "Yeah. . ."
    ch_Rogue "C'mon, tell me why yer askin'."
    ch_Laura "Because. . . I feel things I've never felt before around him. . ."
        
    call knock_on_door(times = 2) from _call_knock_on_door_14

    $ Rogue.name = Rogue.temp

    $ Laura.name = Laura.temp

    "You knock on the door."
    ch_Laura "Who is it?"
    ch_Player "[Laura.name]?"
    ch_Rogue "Sorry, hon'."
    ch_Rogue "Could ya come back later?"
    ch_Rogue "X-23 and ah were havin' a chat. . ."

    $ ongoing_Event = False

    $ Rogue.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_26

    return