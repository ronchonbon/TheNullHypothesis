label Jean_seen_bra(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Jean.name
        $ object = Jean.name
        $ owner = Jean.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_bra_narrations(Jean, proper_subject = proper_subject, undressing = undressing)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Jean_seen_breasts(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Jean.name
        $ object = Jean.name
        $ owner = Jean.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_breasts_narrations(Jean, proper_subject = proper_subject, undressing = undressing)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Jean_seen_underwear(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Jean.name
        $ object = Jean.name
        $ owner = Jean.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_underwear_narrations(Jean, proper_subject = proper_subject, undressing = undressing)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Jean_seen_ass(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Jean.name
        $ object = Jean.name
        $ owner = Jean.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_ass_narrations(Jean, proper_subject = proper_subject, undressing = undressing)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Jean_seen_pussy(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Jean.name
        $ object = Jean.name
        $ owner = Jean.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_pussy_narrations(Jean, proper_subject = proper_subject, undressing = undressing)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    if "pubic" in Jean.desired_body_hair.keys() and Jean.body_hair["pubic"] != Jean.desired_body_hair["pubic"]:
        if (Jean.body_hair["pubic"] == "hairy") or (Jean.body_hair["pubic"] == "bush" and (not Jean.desired_body_hair["pubic"] or Jean.desired_body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (Jean.body_hair["pubic"] == "triangle" and (not Jean.desired_body_hair["pubic"] or Jean.desired_body_hair["pubic"] in ["growing", "null", "strip"])) or (Jean.body_hair["pubic"] in ["growing", "null", "strip"] and not Jean.desired_body_hair["pubic"]):
            if Jean.body_hair_growing["pubic"] or day - Jean.History.check_when("seen_pussy") >= 4:
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

label Jean_seen_anus(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Jean.name
        $ object = Jean.name
        $ owner = Jean.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"
        
    $ pool = seen_anus_narrations(Jean, proper_subject = proper_subject, undressing = undressing)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return