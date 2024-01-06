label Laura_seen_bra(proper_subject = True):

    return

label Laura_seen_breasts(proper_subject = True):

    return

label Laura_seen_underwear(proper_subject = True):

    return

label Laura_seen_ass(proper_subject = True):

    return

label Laura_seen_pussy(proper_subject = True):
    if "pubic" in Laura.desired_body_hair.keys() and Laura.body_hair["pubic"] != Laura.desired_body_hair["pubic"]:
        if (Laura.body_hair["pubic"] == "hairy") or (Laura.body_hair["pubic"] == "bush" and (not Laura.desired_body_hair["pubic"] or Laura.desired_body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (Laura.body_hair["pubic"] == "triangle" and (not Laura.desired_body_hair["pubic"] or Laura.desired_body_hair["pubic"] in ["growing", "null", "strip"])) or (Laura.body_hair["pubic"] in ["growing", "null", "strip"] and not Laura.desired_body_hair["pubic"]):
            if Laura.body_hair_growing["pubic"] or day - Laura.History.check_when("seen_pussy") >= 4:
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

label Laura_seen_anus(proper_subject = True):

    return