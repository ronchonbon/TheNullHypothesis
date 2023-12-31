init python:

    def Kurt_pool_tutorial():
        label = "Kurt_pool_tutorial"

        conditions = [
            "Player.destination == 'bg_pool'",
            "time_index < 3",
            "not weather",
            "Kurt.location != Player.location",
            "not get_Present(location = 'bg_pool')"]

        traveling = True

        priority = 98

        return EventClass(label, conditions, traveling = traveling, priority = priority)

label Kurt_pool_tutorial:
    $ belt_disabled = True

    call set_the_scene(location = Player.destination) from _call_set_the_scene_72

    pause 1.0

    $ ongoing_Event = True

    $ Kurt.outfit = "casual"

    call Kurt_teleports_in from _call_Kurt_teleports_in_2

    ch_Player "Gah!"
    ch_Player "Where the hell-"
    ch_Kurt "Hallo, brüder."
    ch_Kurt "Vant to go swimming, ja?"

    $ Kurt.change_face("confused")

    ch_Player "I was just. . ."
    ch_Kurt "The pool here is quite nice."

    $ Kurt.change_face("neutral")

    ch_Kurt "Good place for some low impact exercise."

    $ Kurt.change_face("neutral", eyes = "squint", mouth = "smile")

    ch_Kurt "And, I think you must be aware of zee effect you have on women here, no?"
    ch_Player "'Effect'?"

    $ Kurt.change_face("neutral")

    ch_Kurt "Valking around in a bathing suit is a sure vay to attract zeir attention."

    $ Kurt.change_face("confused")

    ch_Kurt "Also, if two of zee frauleins don't seem to like each other very much. . ."
    ch_Kurt ". . . bringing zem to hang out at zee pool with you is a good way to help better zeir relationship viz each other." 
    ch_Player "It is?"

    $ Kurt.change_face("happy")

    ch_Kurt "Ja."
    ch_Kurt "And I'm sure zee fair skinned might tan quite quickly while out here, keep zat in mind."
    ch_Kurt "Auf Wiedersehen!"

    call Kurt_teleports_out from _call_Kurt_teleports_out_2

    $ belt_disabled = False

    $ ongoing_Event = False
    
    return