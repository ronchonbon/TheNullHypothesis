init python:

    def Jean_seen_bra():
        label = "Jean_seen_bra"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_bra:

    return

init python:

    def Jean_seen_breasts():
        label = "Jean_seen_breasts"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_breasts:

    return

init python:

    def Jean_seen_underwear():
        label = "Jean_seen_underwear"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_underwear:

    return

init python:

    def Jean_seen_ass():
        label = "Jean_seen_ass"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_ass:

    return

init python:

    def Jean_seen_pussy():
        label = "Jean_seen_pussy"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_pussy:
    if Jean.desired_pubes and Jean.pubes != Jean.desired_pubes:
        if (Jean.pubes == "hairy") or (Jean.pubes == "bush" and (not Jean.desired_pubes or Jean.desired_pubes in ["growing", "null", "strip", "triangle"])) or (Jean.pubes == "triangle" and (not Jean.desired_pubes or Jean.desired_pubes in ["growing", "null", "strip"])) or (Jean.pubes in ["growing", "null", "strip"] and not Jean.desired_pubes):
            if Jean.pubes_growing or day - EventScheduler.Events["Jean_seen_pussy"].completed_when >= 4:
                if Jean.quirk:
                    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

                    ch_Jean "You should be thankful. . ."
                    ch_Jean "I've been keeping it just the way you like, [Jean.Player_petname]."

                    $ Jean.change_face("sexy", blush = 1) 
                else:
                    $ Jean.change_face("confused1", eyes = "down", blush = 1)

                    ch_Jean "Oh, whoops. . ."

                    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

                    ch_Jean "Been busy. . . kinda forgot to keep shaving it."
                    ch_Jean "I'll fix it later."

                    $ Jean.change_face("suspicious1", blush = 1)

                    ch_Jean "Plus, you haven't wanted to look at it in a while."
                    ch_Jean "What's up with that?"

                    if Player.location in bedrooms:
                        call Jean_pubes_need_to_shave from _call_Jean_pubes_need_to_shave
                    else:
                        $ Jean.pubes_to_shave = Jean.desired_pubes

    return

init python:

    def Jean_seen_anus():
        label = "Jean_seen_anus"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_anus:

    return