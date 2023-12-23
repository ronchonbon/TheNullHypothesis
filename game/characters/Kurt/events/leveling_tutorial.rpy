init python:

    def Kurt_leveling_tutorial():
        label = "Kurt_leveling_tutorial"

        conditions = [
            "Player.level >= 2",

            "Player.location in public_locations",

            "Player.location not in [Kurt.location, Kurt.destination]",

            "not get_Present(location = Player.destination)[0]"]

        waiting = True
        traveling = True

        priority = 98

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Kurt_leveling_tutorial:
    $ belt_disabled = True

    pause 1.0

    $ ongoing_Event = True

    $ Kurt.outfit = "casual"
    
    call Kurt_teleports_in from _call_Kurt_teleports_in_1

    $ Kurt.change_face("happy")

    ch_Player "Gah!"
    ch_Kurt "Hallo!"

    $ Kurt.change_face("confused1")

    ch_Player "Bro, where the hel-"
    ch_Kurt "It seems mein Bruder has recently leveled up."
    ch_Player "'Leveled up'?"

    $ Kurt.change_face("neutral")

    ch_Kurt "Zee professor takes pride in his students and knows ven you've made good personal progress."

    $ Kurt.change_face("confused1")

    ch_Player "He does???"

    $ Kurt.change_face("neutral")

    ch_Kurt "Improving yourself is a benefit to everyone, afterall."
    ch_Kurt "Not only do you become more capable, gaining increased stamina to perform more activities per period. . ."

    $ Kurt.change_face("confused1", eyes = "squint", mouth = "smile")

    ch_Kurt "But zee monetary incentive is quite generous as well."

    $ Kurt.change_face("happy")

    ch_Kurt "You vill gain a boost to zee allowance by leveling."
    ch_Player "Well, that is nice. . ."

    $ Kurt.change_face("neutral")

    ch_Kurt "I don't think it is too complicated."
    ch_Kurt "Level up by attending class, studying, or training. Is simple."
    ch_Kurt "I have faith zat you can figure it out."

    $ Kurt.change_face("happy")

    ch_Kurt "Tschüss!"

    call Kurt_teleports_out from _call_Kurt_teleports_out_1

    $ belt_disabled = False

    $ ongoing_Event = False
    
    return