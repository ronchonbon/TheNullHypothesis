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
    if Laura.desired_pubes and Laura.pubes != Laura.desired_pubes:
        if (Laura.pubes == "hairy") or (Laura.pubes == "bush" and (not Laura.desired_pubes or Laura.desired_pubes in ["growing", "null", "strip", "triangle"])) or (Laura.pubes == "triangle" and (not Laura.desired_pubes or Laura.desired_pubes in ["growing", "null", "strip"])) or (Laura.pubes in ["growing", "null", "strip"] and not Laura.desired_pubes):
            if Laura.pubes_growing or day - EventScheduler.Events["Laura_seen_pussy"].completed_when >= 4:
                $ Laura.change_face("confused1", eyes = "down", blush = 1)

                ch_Laura "Oh."

                $ Laura.change_face("sly", blush = 1)

                ch_Laura "Forgot to keep shaving it."
                ch_Laura "I'll just do it later. . ."

                if Player.location in bedrooms:
                    call Laura_pubes_need_to_shave from _call_Laura_pubes_need_to_shave
                else:
                    $ Laura.pubes_to_shave = Laura.desired_pubes

    return

init python:

    def Laura_seen_anus():
        label = "Laura_seen_anus"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_seen_anus:

    return