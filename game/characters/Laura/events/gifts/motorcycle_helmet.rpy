init python:

    def Laura_gifts_motorcycle_helmet():
        label = "Laura_gifts_motorcycle_helmet"

        conditions = [
            "'motorcycle_helmet' in Laura.inventory.keys()",
            "day - Laura.History.check_when('given_motorcycle_helmet') >= 3",
            "Player.location in public_locations",
            "Laura.location != Player.location"]

        waiting = True
        traveling = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling)

label Laura_gifts_motorcycle_helmet:
    $ ongoing_Event = True

    $ Laura.change_face("neutral", blush = 1)

    call send_Characters(Laura, Player.location, behavior = False) from _call_send_Characters_297

    "[Laura.name] seems to appear out of nowhere."
    ch_Player "Where th-"
    ch_Laura "Here."

    $ Laura.change_face("worried1", eyes = "down", blush = 1)

    ch_Laura "Now we can both do it together."
    ch_Laura ". . . once we get a bike."
    "She shoves something into your hands, before running away."

    call remove_Characters(Laura) from _call_remove_Characters_317

    "You look down at what she gave you."
    "It's a brand new motorcycle helmet."

    if "motorcycle_helmet" in Player.inventory.keys():
        $ Player.inventory["motorcycle_helmet"].insert(0, motorcycle_helmet(Player))
    else:
        $ Player.inventory["motorcycle_helmet"] = [motorcycle_helmet(Player)]

    $ ongoing_Event = False

    return