init python:

    def Rogue_Laura_asks_about_masturbation():
        label = "Rogue_Laura_asks_about_masturbation"

        conditions = [
            "Player.destination == Rogue.home",

            "Rogue.location == Rogue.home and Laura.location == Rogue.home",
            
            "EventScheduler.Events['Laura_first_friend_part_two'].completed",

            "Rogue.in_normal_mood()"]

        traveling = True

        markers = {
            Rogue.home: [
                "Rogue.location == Rogue.home and Laura.location == Rogue.home",
                
                "EventScheduler.Events['Laura_first_friend_part_two'].completed",

                "Rogue.in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Rogue_Laura_asks_about_masturbation:
    $ ongoing_Event = True

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_188

    "You hear talking behind the door."
    ch_Laura "'Masturbation'?"
    ch_Laura "What is that?"
    ch_Rogue "Well, if ya ever feel. . . somethin' down there. . ."
    ch_Rogue "It can help relieve some stress. . . if ya know what ah mean."
    ch_Laura "I don't understand."
    ch_Laura "Can't you just demonstrate?"
    ch_Rogue "You want me to. . ."
    ch_Rogue "Ah guess ah could show ya. . ."
        
    call knock_on_door(times = 2) from _call_knock_on_door_16

    "You knock on the door."
    "*thud*"
    ch_Laura "Why did you just fall off the bed?"
    ch_Rogue "Who is it?!"
    ch_Player "It's me. . ."
    ch_Player "I think I should probably try again later."
    ch_Rogue "Yeah, sorry sugar."
    ch_Rogue "We're a bit busy. . ."
    ch_Laura "Why does he have to leave?"
    ch_Laura "He probably also knows what it is."
    ch_Laura "Can't he help demonstrate?"
    ch_Rogue "No!"

    $ Rogue.name = Rogue.temp

    $ Laura.name = Laura.temp

    $ ongoing_Event = False

    $ Rogue.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_27

    return