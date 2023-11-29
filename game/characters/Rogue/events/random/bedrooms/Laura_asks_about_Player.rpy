init python:

    def Rogue_Laura_asks_about_Player_setup():
        label = "Rogue_Laura_asks_about_Player_setup"

        conditions = [
            "Rogue.location not in ['hold', Player.location, Player.destination]",
            "Laura.location not in ['hold', Player.location, Player.destination]",
            "Rogue.home not in [Player.location, Player.destination]",
            
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Rogue_Laura_asks_about_Player'].completed",

            "time_index not in Rogue.schedule.keys()",
            "time_index not in Laura.schedule.keys()",

            "EventScheduler.Events['Laura_first_friend_part_two'].completed",
            
            "not Rogue in Partners and not Laura in Partners",

            "Rogue.is_in_normal_mood()",
            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_Laura_asks_about_Player_setup:
    call send_Characters(Rogue, Rogue.home, behavior = False) from _call_send_Characters_320
    call send_Characters(Laura, Rogue.home, behavior = False) from _call_send_Characters_321

    return

init python:

    def Rogue_Laura_asks_about_Player():
        label = "Rogue_Laura_asks_about_Player"

        conditions = [
            "Player.destination == Rogue.home",

            "Rogue.location == Rogue.home and Laura.location == Rogue.home",
            
            "EventScheduler.Events['Laura_first_friend_part_two'].completed",
            
            "not Rogue in Partners and not Laura in Partners",

            "Rogue.is_in_normal_mood()",
            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            Rogue.home: [         
                "Player.location != Rogue.home",
                     
                "Rogue.location == Rogue.home and Laura.location == Rogue.home",
                
                "EventScheduler.Events['Laura_first_friend_part_two'].completed",
                
                "not Rogue in Partners and not Laura in Partners",

                "Rogue.is_in_normal_mood()",
                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

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
    ch_Rogue "[Laura.public_name] and ah were havin' a chat. . ."

    $ Rogue.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_26

    $ ongoing_Event = False

    return