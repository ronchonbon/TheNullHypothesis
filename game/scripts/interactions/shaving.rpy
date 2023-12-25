label ask_Character_to_shave(Character, hair_style):
    if hair_style != Character.desired_body_hair["pubic"]:
        call expression f"{Character.tag}_pubes_{hair_style}_accept" from _call_expression_267
    else:
        $ changed_body_hair = False

    if hair_style == "shaven":
        $ Character.desired_body_hair["pubic"] = None
    else:
        $ Character.desired_body_hair["pubic"] = hair_style

    return

label Characters_will_shave(shaving_Characters):
    if shaving_Characters in all_Companions:
        $ shaving_Characters = [shaving_Characters]

    while shaving_Characters:
        if (shaving_Characters[0].desired_body_hair["pubic"] == "hairy") or (shaving_Characters[0].desired_body_hair["pubic"] == "bush" and (not shaving_Characters[0].body_hair["pubic"] or shaving_Characters[0].body_hair["pubic"] in ["growing", "null", "strip", "triangle"])) or (shaving_Characters[0].desired_body_hair["pubic"] == "triangle" and (not shaving_Characters[0].body_hair["pubic"] or shaving_Characters[0].body_hair["pubic"] in ["growing", "null", "strip"])) or (shaving_Characters[0].desired_body_hair["pubic"] in ["growing", "null", "strip"] and not shaving_Characters[0].body_hair):
            call expression f"{shaving_Characters[0].tag}_pubes_need_to_grow" from _call_expression_268
        else:
            call expression f"{shaving_Characters[0].tag}_pubes_need_to_shave" from _call_expression_269

        $ shaving_Characters.remove(shaving_Characters[0])

    return