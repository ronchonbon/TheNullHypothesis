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
    if "pubic" in Jean.desired_body_hair.keys() and Jean.body_hair["pubic"] != Jean.desired_body_hair["pubic"]:
        if (Jean.body_hair["pubic"] == "hairy") or (Jean.body_hair["pubic"] == "bush" and (not Jean.desired_body_hair["pubic"] or Jean.desired_body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (Jean.body_hair["pubic"] == "triangle" and (not Jean.desired_body_hair["pubic"] or Jean.desired_body_hair["pubic"] in ["growing", "null", "strip"])) or (Jean.body_hair["pubic"] in ["growing", "null", "strip"] and not Jean.desired_body_hair["pubic"]):
            if Jean.body_hair_growing["pubic"] or day - EventScheduler.Events["Jean_seen_pussy"].completed_when >= 4:
                if Jean.check_traits("quirk"):
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
                        $ Jean.body_hair_to_shave["pubic"] = Jean.desired_body_hair["pubic"]

    return

init python:

    def Jean_seen_anus():
        label = "Jean_seen_anus"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_seen_anus:

    return