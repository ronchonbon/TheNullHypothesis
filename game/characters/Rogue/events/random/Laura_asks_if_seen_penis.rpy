init python:

    def Rogue_Laura_asks_if_seen_penis():
        label = "Rogue_Laura_asks_if_seen_penis"

        conditions = [
            "Player.destination == Rogue.home",
            "Rogue.location == Rogue.home and Laura.location == Rogue.home",
            "EventScheduler.Events['Laura_first_friend_part_two'].completed",
            "Laura.History.check('seen_Player_cock') and not Rogue.History.check('seen_Player_cock') and Laura in Partners and Rogue in Partners and Rogue in Laura.knows_about and Laura in Rogue.knows_about"]

        traveling = True

        return EventClass(label, conditions, traveling = traveling)

label Rogue_Laura_asks_if_seen_penis:
    $ ongoing_Event = True

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_189

    "You can hear a conversation through the door."
    ch_Laura "Have you not seen [Player.first_name]'s penis yet?"
    ch_Rogue "Huh?!"
    ch_Rogue "No. . ."
    ch_Rogue "Lord, where is that comin' from?"
    ch_Laura "I have seen his."
    ch_Laura "Was not expecting it to be so large."
    ch_Laura "Is every penis so big?"
    ch_Laura "First one I've seen."
    ch_Rogue "What?!"
    ch_Rogue "You've seen it?!"
    ch_Rogue "And hell, ah wouldn't know. . ."
    ch_Rogue "Never seen one up close. . ."
        
    call knock_on_door(times = 2) from _call_knock_on_door_17

    "You knock on the door."
    ch_Player "[Rogue.name]?"
    ch_Rogue "[Player.first_name]?!"

    $ Rogue.name = Rogue.temp

    $ Laura.name = Laura.temp

    call set_the_scene(location = Rogue.home) from _call_set_the_scene_190

    $ Rogue.change_face("surprised2", blush = 1)
    $ Laura.change_face("sly", blush = 1)
    
    ch_Laura "We were just talking about you."

    $ Laura.eyes = "down"

    $ Rogue.change_face("worried2", blush = 2)

    ch_Rogue "No we weren't. . ."

    $ Laura.change_face("smirk2", blush = 1)

    ch_Laura "I'm heading out, bye."

    call remove_Characters(Laura) from _call_remove_Characters_181

    $ ongoing_Event = False

    return