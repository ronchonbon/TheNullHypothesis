init python:

    def Laura_Jean_wants_to_go_on_date_setup():
        label = "Laura_Jean_wants_to_go_on_date_setup"

        conditions = [
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_Jean_wants_to_go_on_date'].completed",

            "time_index not in Laura.schedule.keys()",
            "time_index not in Jean.schedule.keys()",

            "Laura in Partners and Jean in Partners",

            "not Player.date_planned",

            "Laura.is_in_normal_mood()",
            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_Jean_wants_to_go_on_date_setup:
    call send_Characters(Laura, Laura.home, behavior = False)
    call send_Characters(Jean, Laura.home, behavior = False)

    return

init python:

    def Laura_Jean_wants_to_go_on_date():
        label = "Laura_Jean_wants_to_go_on_date"

        conditions = [
            "Player.destination == Laura.home",

            "Laura in Partners and Jean in Partners",

            "Laura.location == Laura.home and Jean.location == Laura.home",

            "not Player.date_planned",

            "Laura.is_in_normal_mood()",
            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            Laura.home: [
                "Laura in Partners and Jean in Partners",

                "Laura.location == Laura.home and Jean.location == Laura.home",

                "not Player.date_planned",

                "Laura.is_in_normal_mood()",
                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_Jean_wants_to_go_on_date:
    $ ongoing_Event = True

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    $ Jean.temp = Jean.name
    $ Jean.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_106

    "You hear a heated argument going on inside the room."
    ch_Laura "{i}Grrrrrr{/i}. . ."
    ch_Laura "Why are you here?"
    ch_Jean "Because I know you were planning on stealing my time with [Player.first_name] tonight."
    ch_Laura "Steal? Time with {i}you{/i}?"
    ch_Laura "He's {i}mine{/i}."
    ch_Jean "He's {i}ours{/i}!"
    ch_Jean "And more {i}mine{/i} than yours."
    ch_Jean "So I get to decide what he's doing tonight."
    ch_Laura "You fu. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_2

    "You knock on the door."
    ch_Player "It's me!"
    ch_Player "Everything okay in there?"
    "The door suddenly swings open, and you're yanked inside."

    $ Laura.name = Laura.temp
    
    $ Jean.name = Jean.temp

    call set_the_scene(location = Laura.home) from _call_set_the_scene_107

    $ Laura.change_face("furious", eyes = "right")
    $ Jean.change_face("angry1", eyes = "left")

    pause 1.0

    $ Jean.change_face("suspicious1")

    ch_Jean "You're going on a date with {i}me{/i} tonight."
    ch_Player "Wha. . ."

    $ Laura.change_face("suspicious2")

    ch_Laura "No, you're coming with {i}me{/i}."

    menu:
        extend ""
        "Pick [Jean.name]":
            $ Laura.change_face("furious", eyes = "right") 
            $ Jean.change_face("sly") 
            
            ch_Jean "Good. . ."
            ch_Jean "Then I'll see you later, [Jean.Player_petname]."
            
            $ Jean.change_face("happy") 

            ch_Jean "Bye!"

            call remove_Characters(Jean) from _call_remove_Characters_95

            ch_Player "Sorry. . ."
            
            $ Laura.change_face("suspicious2") 
            
            ch_Laura "Fine, but you're all mine another day."

            $ Player.date_planned[Jean] = "Girl_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Jean_date"].start()
        "Pick [Laura.name]":
            $ Jean.change_face("furious", eyes = "left") 
            $ Laura.change_face("sly") 
            
            ch_Laura "See."

            $ Jean.change_face("suspicious1") 
            
            ch_Jean "Fine. . . I'll just get him all to myself another day."
            
            call remove_Characters(Jean) from _call_remove_Characters_96

            $ Player.date_planned[Laura] = "Girl_initiated_primary"

            if time_index == 2:
                $ EventScheduler.Events["Laura_date"].start()
        "Neither":
            $ Jean.change_face("confused1") 
            $ Laura.change_face("suspicious2") 

            ch_Jean "Wait. . . what?"
            ch_Laura ". . ."

            $ Jean.change_face("suspicious1")

            ch_Jean "I guess I'll just. . . see you later, then."

            call remove_Characters(Jean) from _call_remove_Characters_97

    $ ongoing_Event = False

    return