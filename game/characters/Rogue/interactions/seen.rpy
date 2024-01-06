label Rogue_seen_bra(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Rogue.name
        $ object = Rogue.name
        $ owner = Rogue.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_bra_narrations(Rogue, proper_subject = proper_subject)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Rogue_seen_breasts(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Rogue.name
        $ object = Rogue.name
        $ owner = Rogue.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_breasts_narrations(Rogue, proper_subject = proper_subject)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Rogue_seen_underwear(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Rogue.name
        $ object = Rogue.name
        $ owner = Rogue.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_underwear_narrations(Rogue, proper_subject = proper_subject)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Rogue_seen_ass(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Rogue.name
        $ object = Rogue.name
        $ owner = Rogue.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_ass_narrations(Rogue, proper_subject = proper_subject)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return

label Rogue_seen_pussy(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Rogue.name
        $ object = Rogue.name
        $ owner = Rogue.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ pool = seen_pussy_narrations(Rogue, proper_subject = proper_subject)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    if "pubic" in Rogue.desired_body_hair.keys() and Rogue.body_hair["pubic"] != Rogue.desired_body_hair["pubic"]:
        if (Rogue.body_hair["pubic"] == "hairy") or (Rogue.body_hair["pubic"] == "bush" and (not Rogue.desired_body_hair["pubic"] or Rogue.desired_body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (Rogue.body_hair["pubic"] == "triangle" and (not Rogue.desired_body_hair["pubic"] or Rogue.desired_body_hair["pubic"] in ["growing", "null", "strip"])) or (Rogue.body_hair["pubic"] in ["growing", "null", "strip"] and not Rogue.desired_body_hair["pubic"]):
            if Rogue.body_hair_growing["pubic"] or day - Rogue.History.check_when("seen_pussy") >= 4:
                if Rogue.check_traits("quirk"):
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

label Rogue_seen_anus(proper_subject = True, undressing = True):
    if proper_subject:
        $ subject = Rogue.name
        $ object = Rogue.name
        $ owner = Rogue.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"
        
    $ pool = seen_anus_narrations(Rogue, proper_subject = proper_subject)

    $ dialogue = renpy.random.choice(pool)

    "[dialogue]"

    return