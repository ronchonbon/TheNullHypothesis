init python:

    def Rogue_gifts_acoustic_panels():
        label = "Rogue_gifts_acoustic_panels"

        conditions = [
            "'camera' in Rogue.inventory.keys()",
            "day - Rogue.History.check_when('given_camera') >= 3",
            "'electric_guitar' in Player.inventory.keys()",
            "Player.location in public_locations",
            "Rogue.location != Player.location"]

        waiting = True
        traveling = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling)

label Rogue_gifts_acoustic_panels:
    $ ongoing_Event = True

    call send_Characters(Rogue, Player.location, behavior = False) from _call_send_Characters_298

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah have somethin' to give ya. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    "She hands you a big box. It's surprisingly light."
    ch_Player "What's this?"
    ch_Player "You didn't have to get me anything. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah just figured. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Rogue "The guitar ah gave ya can be pretty loud."
    ch_Rogue "Now ya don't have to worry so much. . ."

    call remove_Characters(Rogue) from _call_remove_Characters_318

    "She runs off before you can say anything."
    "You look inside the box and see a bunch of acoustic panels."

    $ Player.inventory["acoustic_panels"] = [acoustic_panels(Player)]

    $ ongoing_Event = False

    return