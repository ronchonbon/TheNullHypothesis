init python:

    def Jean_gifts_record_player():
        label = "Jean_gifts_record_player"

        conditions = [
            "'wholesome_romance_novel' in Jean.inventory.keys()",
            "day - Jean.History.check_when('given_wholesome_romance_novel') >= 3",
            "Player.location in public_locations",
            "Jean.location != Player.location"]

        waiting = True
        traveling = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling)

label Jean_gifts_record_player:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location, behavior = False) from _call_send_Characters_291

    $ Jean.change_face("happy", blush = 1)

    ch_Jean "Hey!."

    $ petname = Jean.petname.capitalize()

    ch_Player "[petname]?"

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "I've been thinking about 'fun' stuff, and I really like music. . ."

    if Player.scholarship == "artistic":
        ch_Jean "I know you do too. . ."

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Jean "But I don't want it for my room."
    "She hands you a box."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "I spend enough time in there as it is."

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Put this in your room, then I'll have a good excuse to come over more often."

    call remove_Characters(Jean) from _call_remove_Characters_316

    "She runs off before you can say anything."
    "You open the box and find a very nice record player inside."

    if "record_player" in Player.inventory.keys():
        $ Player.inventory["record_player"].insert(0, record_player(Player))
    else:
        $ Player.inventory["record_player"] = [record_player(Player)]

    $ ongoing_Event = False

    return