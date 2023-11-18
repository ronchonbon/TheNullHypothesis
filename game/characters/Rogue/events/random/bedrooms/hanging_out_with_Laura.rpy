init python:

    def Rogue_hanging_out_with_Laura():
        label = "Rogue_hanging_out_with_Laura"

        conditions = [
            "renpy.random.random() > 0.5",

            "Player.destination == Rogue.home",

            "Rogue.location == Rogue.home and Laura.location == Rogue.home",

            "Rogue.in_normal_mood()"]

        traveling = True

        repeatable = True

        return EventClass(label, conditions, traveling = traveling, repeatable = repeatable)

label Rogue_hanging_out_with_Laura:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_195
    call knock_on_door(times = 2) from _call_knock_on_door_20

    ch_Player "[Rogue.name]?"
    ch_Player "It's me, can I come in?"
    ch_Rogue "Sorry, [Player.first_name]."
    ch_Rogue "Ah'm helpin' X-23 with somethin'."
    ch_Laura "Yeah, go away."
    ch_Rogue "That wasn't very nice darlin'."
    ch_Laura ". . . please."

    $ ongoing_Event = False

    $ Rogue.wants_alone_time = 1
        
    call move_location("bg_girls_hallway") from _call_move_location_30

    return