init python:

    def Rogue_bedroom_changing():
        label = "Rogue_bedroom_changing"

        conditions = [
            "day - EventScheduler.Events['Rogue_bedroom_changing'].completed > 0",
            "Player.destination == Rogue.home",
            "Rogue.location == Rogue.home",
            "Rogue.changing"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Rogue_bedroom_changing:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_191
    call knock_on_door(times = 2) from _call_knock_on_door_18

    if Rogue.History.check("seen_underwear"):
        ch_Player "Can I come in?"
        ch_Rogue "[Player.first_name]?"
        ch_Rogue "Sure, ah'll get the door."

        call take_off_everything_but(Rogue, ["top", "bra", "underwear"]) from _call_take_off_everything_but_8

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_192

        $ Rogue.change_face("worried1", mouth = "lipbite")

        "As you walk in, you realize [Rogue.name] was in the middle of changing. . ."
        ch_Rogue "Ah just gotta finish changin'. . ."

        $ Rogue.blush = 1

        call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_14
    else:
        ch_Player "[Rogue.name], you there?"
        "You hear the shower turn off behind the door."
        ch_Rogue "Sorry, sugar."
        ch_Rogue "Ah'm not. . . decent right now."
        ch_Rogue "Could ya come back later?"

        $ ongoing_Event = False

        $ Rogue.wants_alone_time = 1
        
        call move_location("bg_girls_hallway") from _call_move_location_28

    $ ongoing_Event = False
    
    return