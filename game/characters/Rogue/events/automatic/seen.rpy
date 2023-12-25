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
    if "pubic" in Rogue.desired_body_hair.keys() and Rogue.body_hair["pubic"] != Rogue.desired_body_hair["pubic"]:
        if (Rogue.body_hair["pubic"] == "hairy") or (Rogue.body_hair["pubic"] == "bush" and (not Rogue.desired_body_hair["pubic"] or Rogue.desired_body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (Rogue.body_hair["pubic"] == "triangle" and (not Rogue.desired_body_hair["pubic"] or Rogue.desired_body_hair["pubic"] in ["growing", "null", "strip"])) or (Rogue.body_hair["pubic"] in ["growing", "null", "strip"] and not Rogue.desired_body_hair["pubic"]):
            if Rogue.body_hair_growing["pubic"] or day - EventScheduler.Events["Rogue_seen_pussy"].completed_when >= 4:
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
                        $ Rogue.body_hair_to_shave["pubic"] = Rogue.desired_body_hair["pubic"]

    return

init python:

    def Rogue_seen_anus():
        label = "Rogue_seen_anus"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_seen_anus:

    return