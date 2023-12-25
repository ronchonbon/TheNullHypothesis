init python:

    def Laura_seen_bra():
        label = "Laura_seen_bra"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_bra:

    return

init python:

    def Laura_seen_breasts():
        label = "Laura_seen_breasts"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_breasts:

    return

init python:

    def Laura_seen_underwear():
        label = "Laura_seen_underwear"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_underwear:

    return

init python:

    def Laura_seen_ass():
        label = "Laura_seen_ass"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_ass:

    return

init python:

    def Laura_seen_pussy():
        label = "Laura_seen_pussy"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_pussy:
    if Laura.desired_body_hair["pubic"] and Laura.body_hair["pubic"] != Laura.desired_body_hair["pubic"]:
        if (Laura.body_hair["pubic"] == "hairy") or (Laura.body_hair["pubic"] == "bush" and (not Laura.desired_body_hair["pubic"] or Laura.desired_body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (Laura.body_hair["pubic"] == "triangle" and (not Laura.desired_body_hair["pubic"] or Laura.desired_body_hair["pubic"] in ["growing", "null", "strip"])) or (Laura.body_hair["pubic"] in ["growing", "null", "strip"] and not Laura.desired_body_hair["pubic"]):
            if Laura.body_hair_growing["pubic"] or day - EventScheduler.Events["Laura_seen_pussy"].completed_when >= 4:
                $ Laura.change_face("confused1", eyes = "down", blush = 1)

                ch_Laura "Oh."

                $ Laura.change_face("sly", blush = 1)

                ch_Laura "Forgot to keep shaving it."
                ch_Laura "I'll just do it later. . ."

                if Player.location in bedrooms:
                    call Laura_pubes_need_to_shave from _call_Laura_pubes_need_to_shave
                else:
                    $ Laura.body_hair_to_shave["pubic"] = Laura.desired_body_hair["pubic"]

    return

init python:

    def Laura_seen_anus():
        label = "Laura_seen_anus"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_anus:

    return