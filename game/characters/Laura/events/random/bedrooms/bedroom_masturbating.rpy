init python:

    def Laura_bedroom_masturbating():
        label = "Laura_bedroom_masturbating"

        conditions = [
            "Player.destination == Laura.home and Laura.location == Laura.home",

            "EventScheduler.Events['Rogue_Laura_asks_about_masturbation'].completed",
            "Laura.masturbating",

            "day - EventScheduler.Events['Laura_bedroom_masturbating'].completed_when > 1",
            
            "Laura.is_in_normal_mood()"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Laura_bedroom_masturbating:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_115

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "As you get closer, you hear. . . growling. . . and other {i}interesting{/i} noises."
        ch_Laura "*gasp* Asshole. . ."
        ch_Laura "[Player.first_name]. . . making me feel. . ."
        ch_Laura ". . . *gasp*"

        call knock_on_door(times = 2) from _call_knock_on_door_8

        "You knock on the door."
        ch_Player "[Laura.name]?"
    elif dice_roll == 2:
        "As you get closer, you hear. . . growling. . . and other {i}interesting{/i} noises."
        ch_Laura "{i}Grrrrr{/i}. . . this is your fault, [Player.first_name]."
        ch_Laura "Mmm. . ."
        ch_Laura "*gasp* Goddamnit. . . [Player.first_name]. . ."
        
        call knock_on_door(times = 2) from _call_knock_on_door_9

        "You knock on the door."
        ch_Player "[Laura.name]? You okay?"

    if approval_check(Laura, threshold = "hookup"):
        ch_Laura "[Player.first_name]?!"
        "You hear frantic shuffling before [Laura.name] swings the door open."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_116

        $ Laura.change_face("appalled1", blush = 2)

        ch_Laura "{i}Grrrrr{/i}"
        ch_Player "Uh. . ."

        $ Laura.change_face("furious")

        "She looks {i}pissed{/i}."
        ch_Laura "Come in already. . ."
    else:
        ch_Laura "Go away!"
        ch_Laura "You didn't hear anything."
        ch_Laura "I'm busy."
        ch_Laura "Go away."

        $ ongoing_Event = False

        $ Laura.wants_alone_time = 1
        
        call move_location("bg_girls_hallway") from _call_move_location_19

    $ ongoing_Event = False
    
    return