init python:

    def Rogue_bedroom_masturbating():
        label = "Rogue_bedroom_masturbating"

        conditions = [
            "Player.destination == Rogue.home and Rogue.location == Rogue.home",

            "Rogue.behavior == 'masturbating'",

            "day - EventScheduler.Events['Rogue_bedroom_masturbating'].completed_when > 1",
            
            "Rogue.is_in_normal_mood()"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Rogue_bedroom_masturbating:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_193

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear {i}interesting{/i} noises coming from inside."
        ch_Rogue "Mmm, oh god, please [Player.first_name]."
        ch_Rogue "*gasp* [Player.first_name]. . . ah. . ."
        ch_Player "[Rogue.name]?"
    elif dice_roll == 2:
        "As you get closer, you hear some {i}interesting{/i} noises coming from inside."
        ch_Rogue "[Player.first_name], please. . . *gasp*"
        ch_Rogue "Ah need you. . . oh lord, [Player.first_name]. . ."
        
        call knock_on_door(times = 2) from _call_knock_on_door_19

        "You knock on the door."
        ch_Player "Everything okay in there, [Rogue.name]?"

    if approval_check(Rogue, threshold = "hookup"):
        ch_Rogue "[Player.first_name]?!"
        "You hear some shuffling before [Rogue.name] opens the door."

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_194

        $ Rogue.change_face("manic", blush = 2)

        ch_Rogue "Ah'm alright. . . was just. . ."
        ch_Rogue "You didn't hear all that, did you?"
    else:
        ch_Rogue "[Player.first_name]?!"
        ch_Rogue "{size=-5}Oh lord{/size}. . . you didn't hear nothin', right?"
        ch_Rogue "Ah mean, sorry, ah'm busy. . . could ya come by later?"

        $ Rogue.wants_alone_time = 1
        
        call move_location("bg_girls_hallway") from _call_move_location_29

    $ ongoing_Event = False
    
    return