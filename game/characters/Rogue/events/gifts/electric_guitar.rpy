init python:

    def Rogue_gifts_electric_guitar():
        label = "Rogue_gifts_electric_guitar"

        conditions = [
            "'acoustic_guitar' in Rogue.inventory.keys()",
            "day - Rogue.History.check_when('given_acoustic_guitar') >= 3",
            "Player.location in public_locations",
            "Rogue.location != Player.location"]

        waiting = True
        traveling = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling)

label Rogue_gifts_electric_guitar:
    $ ongoing_Event = True

    call send_Characters(Rogue, Player.location, behavior = False) from _call_send_Characters_299

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "There ya are. . ."
    ch_Player "Oh, hey [Rogue.petname]."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah really appreciated that guitar ya got me."

    if Player.scholarship == "artistic":
        ch_Rogue "And ah know yer the creative type. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah had something sent to your room. . ."
    ch_Rogue ". . . ah wanted to give you somethin' for once. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    call remove_Characters(Rogue) from _call_remove_Characters_319

    "She runs off before you can say anything."
    "You head over to your room."

    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_133

    "In front of your door are multiple massive boxes."

    call set_the_scene(location = Player.home) from _call_set_the_scene_156

    "You bring them in and open the oblong box, instantly recognizing its contents."
    "It's a red Fender Stratocaster. . ."
    "In one of the other boxes is a guitar amp, and another contains a full-blown sound system with tower speakers and everything."
    "[Rogue.name] really went all out for you."

    $ Player.inventory["electric_guitar"] = [electric_guitar(Player)]
    $ Player.inventory["sound_system"] = [sound_system(Player)]

    $ ongoing_Event = False

    return