init python:

    def Laura_Rogue_talking_about_masturbation():
        label = "Laura_Rogue_talking_about_masturbation"

        conditions = [
            "Player.destination == Laura.home",
            "Laura.location == Laura.home and Rogue.location == Laura.home",
            "EventScheduler.Events['Laura_first_friend_part_two'].completed",
            "EventScheduler.Events['Rogue_Laura_asks_about_masturbation'].completed"]

        traveling = True

        return EventClass(label, conditions, traveling = traveling)

label Laura_Rogue_talking_about_masturbation:
    $ ongoing_Event = True

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_112

    "You hear a hushed conversation behind the door."
    ch_Laura "I tried that thing you showed me. . ."
    ch_Rogue "Ah'm not sure what you. . ."
    ch_Rogue "OH!"
    ch_Laura "You were right."
    ch_Laura "It did help relieve stress. . ."
    ch_Laura ". . . after the tenth time."
    ch_Rogue "Tenth?!"
    ch_Rogue "Lord, how can ya walk straight?"
    ch_Laura "But it only worked when I thought about. . . [Player.first_name]. . ."
    ch_Rogue "Oh darlin'. . ."
    ch_Rogue "Ah think yer fallin' hard for him."

    call knock_on_door(times = 2) from _call_knock_on_door_6

    "You knock on the door."
    ch_Player "Uhm. . . it's [Player.first_name]."
    ch_Player "Can I come in?"
    ch_Laura "NO!"
    ch_Rogue "Sorry, [Player.first_name]."
    ch_Rogue "We're a bit busy. . ."

    $ Laura.name = Laura.temp

    $ Rogue.name = Rogue.temp

    $ ongoing_Event = False

    $ Laura.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_17

    return