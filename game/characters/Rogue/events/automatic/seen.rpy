init python:

    def Rogue_seen_bra():
        label = "Rogue_seen_bra"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_bra:

    return

init python:

    def Rogue_seen_breasts():
        label = "Rogue_seen_breasts"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_breasts:

    return

init python:

    def Rogue_seen_underwear():
        label = "Rogue_seen_underwear"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_underwear:

    return

init python:

    def Rogue_seen_ass():
        label = "Rogue_seen_ass"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_ass:

    return

init python:

    def Rogue_seen_pussy():
        label = "Rogue_seen_pussy"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_pussy:
    if Rogue.desired_pubes and Rogue.pubes != Rogue.desired_pubes:
        if (Rogue.pubes == "hairy") or (Rogue.pubes == "bush" and (not Rogue.desired_pubes or Rogue.desired_pubes in ["growing", "null", "strip", "triangle"])) or (Rogue.pubes == "triangle" and (not Rogue.desired_pubes or Rogue.desired_pubes in ["growing", "null", "strip"])) or (Rogue.pubes in ["growing", "null", "strip"] and not Rogue.desired_pubes):
            if Rogue.pubes_growing or day - EventScheduler.Events["Rogue_seen_pussy"].completed_when >= 4:
                if Rogue.quirk:
                    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

                    ch_Rogue "Ah've been a good girl, right [Rogue.Player_petname]?"

                    $ Rogue.change_face("sexy", blush = 1)

                    ch_Rogue "Ah kept the hair down there just the way you wanted it. . ."
                    ch_Rogue "Ready for the next time ya wanted to see it."
                else:
                    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

                    ch_Rogue "Ah'm sorry, [Rogue.Player_petname]."

                    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

                    ch_Rogue "Ah let it grow out a bit."
                    ch_Rogue "Been a while since ya last wanted to see it. . ."

                    if Player.location in bedrooms:
                        call Rogue_pubes_need_to_shave from _call_Rogue_pubes_need_to_shave
                    else:
                        $ Rogue.pubes_to_shave = Rogue.desired_pubes

    return

init python:

    def Rogue_seen_anus():
        label = "Rogue_seen_anus"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_anus:

    return