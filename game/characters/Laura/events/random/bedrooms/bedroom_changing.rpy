init python:

    def Laura_bedroom_changing():
        label = "Laura_bedroom_changing"

        conditions = [
            "Player.destination == Laura.home and Laura.location == Laura.home",

            "Laura.behavior == 'changing'",

            "day - EventScheduler.Events['Laura_bedroom_changing'].completed_when > 1",
            
            "Laura.is_in_normal_mood()"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Laura_bedroom_changing:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_113
    call knock_on_door(times = 2) from _call_knock_on_door_7

    if Laura.History.check("seen_underwear"):
        ch_Player "Can I come in?"
        ch_Laura "Fine."
        ch_Laura "I'll unlock the door."
        
        call take_off_everything_but(Laura, ["top", "bra", "underwear"]) from _call_take_off_everything_but_4

        call set_the_scene(location = Laura.home) from _call_set_the_scene_114

        $ Laura.change_face("neutral")

        "As you walk in, you realize [Laura.name] was in the middle of changing. . ."
        ch_Laura "What?"

        $ Laura.change_face("confused1")

        ch_Laura "You can watch."

        $ Laura.change_face("neutral")

        call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_8
    else:
        ch_Player "[Laura.name], you there?"
        "You hear the shower turn off behind the door."
        ch_Laura "I'm busy."
        ch_Laura "Go away."

        $ Laura.wants_alone_time = 1
        
        call move_location("bg_girls_hallway") from _call_move_location_18

    $ ongoing_Event = False
    
    return