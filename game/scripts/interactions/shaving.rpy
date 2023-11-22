label ask_Girl_to_shave(Girl, hair_style):
    if hair_style != Girl.desired_pubes:
        call expression f"{Girl.tag}_pubes_{hair_style}_accept" from _call_expression_267
    else:
        $ changed_pubes = False

    if hair_style == "shaven":
        $ Girl.desired_pubes = None
    else:
        $ Girl.desired_pubes = hair_style

    return

label Girls_will_shave(shaving_Companions):
    if shaving_Companions in all_Characters:
        $ shaving_Companions = [shaving_Companions]

    while shaving_Companions:
        if (shaving_Companions[0].desired_pubes == "hairy") or (shaving_Companions[0].desired_pubes == "bush" and (not shaving_Companions[0].pubes or shaving_Companions[0].pubes in ["growing", "null", "strip", "triangle"])) or (shaving_Companions[0].desired_pubes == "triangle" and (not shaving_Companions[0].pubes or shaving_Companions[0].pubes in ["growing", "null", "strip"])) or (shaving_Companions[0].desired_pubes in ["growing", "null", "strip"] and not shaving_Companions[0].pubes):
            call expression f"{shaving_Companions[0].tag}_pubes_need_to_grow" from _call_expression_268
        else:
            call expression f"{shaving_Companions[0].tag}_pubes_need_to_shave" from _call_expression_269

        $ shaving_Companions.remove(shaving_Companions[0])

    return