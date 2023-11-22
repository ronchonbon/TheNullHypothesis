label ask_to_undress(Character):
    $ finished = False

    while not finished:
        $ choice_disabled = False

        $ verb = None
        $ Item_type = None
        $ state = None

        $ Clothes = Character.Clothes
        $ Outfit = Character.Wardrobe.Outfits[Character.Outfit.name].Clothes

        menu:
            "Can you. . . ?"
            "Use your remote vibrator?" if not Character.remote_vibrator and "remote_vibrator" in Character.inventory.keys() and not Character.vagina_Actions:
                call ask_Girl_to_use_Toy(Character, Character.inventory["remote_vibrator"][0]) from _call_ask_Girl_to_use_Toy
            "Remove your remote vibrator?" if Character.remote_vibrator:
                call expose(Character, "pussy") from _call_expose_12

                pause 1.0

                $ Character.remote_vibrator = False

                pause 1.0

                call fix_clothing(Character) from _call_fix_clothing_2
            "Put in a buttplug?" if not Character.buttplug and ("heart_anal_plug" in Character.inventory.keys() or "round_anal_plug" in Character.inventory.keys()) and not Character.anus_Actions:
                $ plug_type = None
                $ plug_size = None
                
                menu:
                    "Put in a buttplug"
                    "[Character.inventory[heart_anal_plug][0].name] XS" if "heart_anal_plug" in Character.inventory.keys():
                        $ plug_type = "heart_anal_plug"
                        $ plug_size = "XS"
                    "[Character.inventory[heart_anal_plug][0].name] S" if "heart_anal_plug" in Character.inventory.keys():
                        $ plug_type = "heart_anal_plug"
                        $ plug_size = "S"
                    "[Character.inventory[heart_anal_plug][0].name] M" if "heart_anal_plug" in Character.inventory.keys():
                        $ plug_type = "heart_anal_plug"
                        $ plug_size = "M"
                    "[Character.inventory[heart_anal_plug][0].name] L" if "heart_anal_plug" in Character.inventory.keys():
                        $ plug_type = "heart_anal_plug"
                        $ plug_size = "L"
                    "[Character.inventory[round_anal_plug][0].name] XS" if "round_anal_plug" in Character.inventory.keys():
                        $ plug_type = "round_anal_plug"
                        $ plug_size = "XS"
                    "[Character.inventory[round_anal_plug][0].name] S" if "round_anal_plug" in Character.inventory.keys():
                        $ plug_type = "round_anal_plug"
                        $ plug_size = "S"
                    "[Character.inventory[round_anal_plug][0].name] M" if "round_anal_plug" in Character.inventory.keys():
                        $ plug_type = "round_anal_plug"
                        $ plug_size = "M"
                    "[Character.inventory[round_anal_plug][0].name] L" if "round_anal_plug" in Character.inventory.keys():
                        $ plug_type = "round_anal_plug"
                        $ plug_size = "L"
                    "Back":
                        pass

                if plug_type and plug_size:
                    if plug_size == "XS":
                        call ask_Girl_to_use_Toy(Character, Character.inventory[plug_type][0], 0) from _call_ask_Girl_to_use_Toy_1
                    elif plug_size == "S":
                        call ask_Girl_to_use_Toy(Character, Character.inventory[plug_type][0], 1) from _call_ask_Girl_to_use_Toy_2
                    elif plug_size == "M":
                        call ask_Girl_to_use_Toy(Character, Character.inventory[plug_type][0], 2) from _call_ask_Girl_to_use_Toy_3
                    elif plug_size == "L":
                        call ask_Girl_to_use_Toy(Character, Character.inventory[plug_type][0], 3) from _call_ask_Girl_to_use_Toy_4
            "Take out your buttplug?" if Character.buttplug:
                call expose(Character, "anus") from _call_expose_13

                $ Character.buttplug = None
                $ Character.buttplug_size = None

                pause 1.0

                call fix_clothing(Character) from _call_fix_clothing_3
            "Open your [Clothes[cloak].short_name]?" if Clothes["cloak"].string and len(Clothes["cloak"].available_states[Character.position]) > 1 and not Clothes["cloak"].covered and Clothes["cloak"].state == 0:
                $ verb = "undress"
                $ Item_type = "cloak"
            "Close your [Clothes[cloak].short_name]?" if Clothes["cloak"].string and len(Clothes["cloak"].available_states[Character.position]) > 1 and not Clothes["cloak"].covered and Clothes["cloak"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "cloak"
            "Take off your [Clothes[cloak].short_name]?" if Clothes["cloak"].string:
                $ verb = "take_off"
                $ Item_type = "cloak"
            "Put on your [Outfit[cloak].short_name]?" if not Clothes["cloak"].string and Outfit["cloak"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["top"].poses:
                $ verb = "try_on"
                $ Item_type = "cloak"
            "Open your [Clothes[towel].short_name]?" if Clothes["towel"].string and len(Clothes["towel"].available_states[Character.position]) > 1 and not Clothes["towel"].covered and Clothes["towel"].state == 0:
                $ verb = "undress"
                $ Item_type = "towel"
            "Close your [Clothes[towel].short_name]?" if Clothes["towel"].string and len(Clothes["towel"].available_states[Character.position]) > 1 and not Clothes["towel"].covered and Clothes["towel"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "towel"
            "Take off your [Clothes[towel].short_name]?" if Clothes["towel"].string:
                $ verb = "take_off"
                $ Item_type = "towel"
            "Put on your [Outfit[towel].short_name]?" if not Clothes["towel"].string and Outfit["towel"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["top"].poses:
                $ verb = "try_on"
                $ Item_type = "towel"
            "Open your [Clothes[jacket].short_name]?" if Clothes["jacket"].string and len(Clothes["jacket"].available_states[Character.position]) > 1 and not Clothes["jacket"].covered and Clothes["jacket"].state == 0:
                $ verb = "undress"
                $ Item_type = "jacket"
            "Close your [Clothes[jacket].short_name]?" if Clothes["jacket"].string and len(Clothes["jacket"].available_states[Character.position]) > 1 and not Clothes["jacket"].covered and Clothes["jacket"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "jacket"
            "Take off your [Clothes[jacket].short_name]?" if Clothes["jacket"].string:
                $ verb = "take_off"
                $ Item_type = "jacket"
            "Put on your [Outfit[jacket].short_name]?" if not Clothes["jacket"].string and Outfit["jacket"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["top"].poses:
                $ verb = "try_on"
                $ Item_type = "jacket"
            "Shift your [Clothes[suspenders].short_name]?" if Clothes["suspenders"].string and len(Clothes["suspenders"].available_states[Character.position]) > 1 and not Clothes["suspenders"].covered and Clothes["suspenders"].state == 0:
                $ verb = "undress"
                $ Item_type = "suspenders"
            "Fix your [Clothes[suspenders].short_name]?" if Clothes["suspenders"].string and len(Clothes["suspenders"].available_states[Character.position]) > 1 and not Clothes["suspenders"].covered and Clothes["suspenders"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "suspenders"
            "Take off your [Clothes[suspenders].short_name]?" if Clothes["suspenders"].string:
                $ verb = "take_off"
                $ Item_type = "suspenders"
            "Put on your [Outfit[suspenders].short_name]?" if not Clothes["suspenders"].string and Outfit["suspenders"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["top"].poses:
                $ verb = "try_on"
                $ Item_type = "suspenders"
            "Lift your [Clothes[top].short_name]?" if Clothes["top"].string and len(Clothes["top"].available_states[Character.position]) > 1 and not Clothes["top"].covered and Clothes["top"].state == 0:
                $ verb = "undress"
                $ Item_type = "top"
            "Lower your [Clothes[top].short_name]?" if Clothes["top"].string and len(Clothes["top"].available_states[Character.position]) > 1 and not Clothes["top"].covered and Clothes["top"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "top"
            "Take off your [Clothes[top].short_name]?" if Clothes["top"].string:
                $ verb = "take_off"
                $ Item_type = "top"
            "Put on your [Outfit[top].short_name]?" if not Clothes["top"].string and Outfit["top"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["top"].poses:
                $ verb = "try_on"
                $ Item_type = "top"
            "Open your [Clothes[dress].short_name]?" if Clothes["dress"].string and len(Clothes["dress"].available_states[Character.position]) > 1 and not Clothes["dress"].covered and Clothes["dress"].state in [0, 2] and ((Clothes["dress"].state == 0 and 1 in Clothes["dress"].available_states[Character.position]) or (Clothes["dress"].state == 2 and 3 in Clothes["dress"].available_states[Character.position])):
                $ verb = "undress"
                $ Item_type = "dress"

                if state == 2:
                    $ state = 3
                else:
                    $ state = 1
            "Pull up your [Clothes[dress].short_name]?" if Clothes["dress"].string and len(Clothes["dress"].available_states[Character.position]) > 1 and not Clothes["dress"].covered and Clothes["dress"].state in [0, 1] and ((Clothes["dress"].state == 0 and 2 in Clothes["dress"].available_states[Character.position]) or (Clothes["dress"].state == 1 and 3 in Clothes["dress"].available_states[Character.position])):
                $ verb = "undress"
                $ Item_type = "dress"

                if state == 1:
                    $ state = 3
                else:
                    $ state = 2
            "Fix your [Clothes[dress].short_name]?" if Clothes["dress"].string and len(Clothes["dress"].available_states[Character.position]) > 1 and not Clothes["dress"].covered and Clothes["dress"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions and not Character.vagina_Actions and not Character.anus_Actions:
                $ verb = "redress"
                $ Item_type = "dress"
            "Take off your [Clothes[dress].short_name]?" if Clothes["dress"].string:
                $ verb = "take_off"
                $ Item_type = "dress"
            "Put on your [Outfit[dress].short_name]?" if not Clothes["dress"].string and Outfit["dress"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and not Character.vagina_Actions and not Character.anus_Actions and Character.position in Outfit["dress"].poses:
                $ verb = "try_on"
                $ Item_type = "dress"
            "Take off your [Clothes[belt].short_name]?" if Clothes["belt"].string:
                $ verb = "take_off"
                $ Item_type = "belt"
            "Put on your [Outfit[belt].short_name]?" if not Clothes["belt"].string and Outfit["belt"].string and Character.position in Outfit["belt"].poses:
                $ verb = "try_on"
                $ Item_type = "belt"
            "Lift your [Clothes[skirt].short_name]?" if Clothes["skirt"].string and len(Clothes["skirt"].available_states[Character.position]) > 1 and not Clothes["skirt"].covered and Clothes["skirt"].state == 0:
                $ verb = "undress"
                $ Item_type = "skirt"
            "Lower your [Clothes[skirt].short_name]?" if Clothes["skirt"].string and len(Clothes["skirt"].available_states[Character.position]) > 1 and not Clothes["skirt"].covered and Clothes["skirt"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "skirt"
            "Take off your [Clothes[skirt].short_name]?" if Clothes["skirt"].string:
                $ verb = "take_off"
                $ Item_type = "skirt"
            "Put on your [Outfit[skirt].short_name]?" if not Clothes["skirt"].string and Outfit["skirt"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["skirt"].poses:
                $ verb = "try_on"
                $ Item_type = "skirt"
            "Unzip your [Clothes[pants].short_name]?" if Clothes["pants"].string and len(Clothes["pants"].available_states[Character.position]) > 2 and not Clothes["pants"].covered and Clothes["pants"].state == 0:
                $ verb = "undress"
                $ Item_type = "pants"

                $ state = 1
            "Lower your [Clothes[pants].short_name]?" if Clothes["pants"].string and len(Clothes["pants"].available_states[Character.position]) > 1 and not Clothes["pants"].covered and Clothes["pants"].state != Clothes["pants"].undressed_states[Character.position]:
                $ verb = "undress"
                $ Item_type = "pants"
            "Fix your [Clothes[pants].short_name]?" if Clothes["pants"].string and len(Clothes["pants"].available_states[Character.position]) > 1 and not Clothes["pants"].covered and Clothes["pants"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "pants"
            "Take off your [Clothes[pants].short_name]?" if Clothes["pants"].string:
                $ verb = "take_off"
                $ Item_type = "pants"
            "Put on your [Outfit[pants].short_name]?" if not Clothes["pants"].string and Outfit["pants"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["pants"].poses:
                $ verb = "try_on"
                $ Item_type = "pants"
            "Open your [Clothes[bodysuit].short_name]?" if Clothes["bodysuit"].string and len(Clothes["bodysuit"].available_states[Character.position]) > 1 and not Clothes["bodysuit"].covered and Clothes["bodysuit"].state in [0, 2] and ((Clothes["bodysuit"].state == 0 and 1 in Clothes["bodysuit"].available_states[Character.position]) or (Clothes["bodysuit"].state == 2 and 3 in Clothes["bodysuit"].available_states[Character.position])):
                $ verb = "undress"
                $ Item_type = "bodysuit"

                if state == 2:
                    $ state = 3
                else:
                    $ state = 1
            "Pull your [Clothes[bodysuit].short_name] aside?" if Clothes["bodysuit"].string and len(Clothes["bodysuit"].available_states[Character.position]) > 1 and not Clothes["bodysuit"].covered and Clothes["bodysuit"].state in [0, 1] and ((Clothes["bodysuit"].state == 0 and 2 in Clothes["bodysuit"].available_states[Character.position]) or (Clothes["bodysuit"].state == 1 and 3 in Clothes["bodysuit"].available_states[Character.position])):
                $ verb = "undress"
                $ Item_type = "bodysuit"

                if state == 1:
                    $ state = 3
                else:
                    $ state = 2
            "Fix your [Clothes[bodysuit].short_name]?" if Clothes["bodysuit"].string and len(Clothes["bodysuit"].available_states[Character.position]) > 1 and not Clothes["bodysuit"].covered and Clothes["bodysuit"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions and not Character.vagina_Actions and not Character.anus_Actions:
                $ verb = "redress"
                $ Item_type = "bodysuit"
            "Take off your [Clothes[bodysuit].short_name]?" if Clothes["bodysuit"].string:
                $ verb = "take_off"
                $ Item_type = "bodysuit"
            "Put on your [Outfit[bodysuit].short_name]?" if not Clothes["bodysuit"].string and Outfit["bodysuit"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and not Character.vagina_Actions and not Character.anus_Actions and Character.position in Outfit["bodysuit"].poses:
                $ verb = "try_on"
                $ Item_type = "bodysuit"
            "Lift your [Clothes[bra].short_name]?" if Clothes["bra"].string and len(Clothes["bra"].available_states[Character.position]) > 1 and not Clothes["bra"].covered and Clothes["bra"].state == 0:
                $ verb = "undress"
                $ Item_type = "bra"
            "Fix your [Clothes[bra].short_name]?" if Clothes["bra"].string and len(Clothes["bra"].available_states[Character.position]) > 1 and not Clothes["bra"].covered and Clothes["bra"].state != 0 and not Character.left_nipple_Actions and not Character.right_nipple_Actions:
                $ verb = "redress"
                $ Item_type = "bra"
            "Take off your [Clothes[bra].short_name]?" if Clothes["bra"].string:
                $ verb = "take_off"
                $ Item_type = "bra"
            "Put on your [Outfit[bra].short_name]?" if not Clothes["bra"].string and Outfit["bra"].string and not Character.left_nipple_Actions and not Character.right_nipple_Actions and Character.position in Outfit["bra"].poses:
                $ verb = "try_on"
                $ Item_type = "bra"
            "Lower your [Clothes[hose].short_name]?" if Clothes["hose"].string and len(Clothes["hose"].available_states[Character.position]) > 1 and not Clothes["hose"].covered and Clothes["hose"].state == 0:
                $ verb = "undress"
                $ Item_type = "hose"
            "Fix your [Clothes[hose].short_name]?" if Clothes["hose"].string and len(Clothes["hose"].available_states[Character.position]) > 1 and not Clothes["hose"].covered and Clothes["hose"].state != 0 and not Character.vagina_Actions and not Character.anus_Actions:
                $ verb = "redress"
                $ Item_type = "hose"
            "Take off your [Clothes[hose].short_name]?" if Clothes["hose"].string:
                $ verb = "take_off"
                $ Item_type = "hose"
            "Put on your [Outfit[hose].short_name]?" if not Clothes["hose"].string and Outfit["hose"].string and not Character.vagina_Actions and not Character.anus_Actions and Character.position in Outfit["hose"].poses:
                $ verb = "try_on"
                $ Item_type = "hose"
            "Lower your [Clothes[underwear].short_name]?" if Clothes["underwear"].string and len(Clothes["underwear"].available_states[Character.position]) > 1 and not Clothes["underwear"].covered and Clothes["underwear"].state == 0:
                $ verb = "undress"
                $ Item_type = "underwear"
            "Fix your [Clothes[underwear].short_name]?" if Clothes["underwear"].string and len(Clothes["underwear"].available_states[Character.position]) > 1 and not Clothes["underwear"].covered and Clothes["underwear"].state != 0 and not Character.vagina_Actions and not Character.anus_Actions:
                $ verb = "redress"
                $ Item_type = "underwear"
            "Take off your [Clothes[underwear].short_name]?" if Clothes["underwear"].string:
                $ verb = "take_off"
                $ Item_type = "underwear"
            "Put on your [Outfit[underwear].short_name]?" if not Clothes["underwear"].string and Outfit["underwear"].string and not Character.vagina_Actions and not Character.anus_Actions and Character.position in Outfit["underwear"].poses:
                $ verb = "try_on"
                $ Item_type = "underwear"
            "Take off your [Clothes[nipple_accessories].short_name]?" if Clothes["nipple_accessories"].string:
                $ verb = "take_off"
                $ Item_type = "nipple_accessories"
            "Put on your [Outfit[nipple_accessories].short_name]?" if not Clothes["nipple_accessories"].string and Outfit["nipple_accessories"].string and Character.position in Outfit["nipple_accessories"].poses:
                $ verb = "try_on"
                $ Item_type = "nipple_accessories"
            "Take off your [Clothes[gloves].short_name]?" if Clothes["gloves"].string:
                $ verb = "take_off"
                $ Item_type = "gloves"
            "Put on your [Outfit[gloves].short_name]?" if not Clothes["gloves"].string and Outfit["gloves"].string and Character.position in Outfit["gloves"].poses:
                $ verb = "try_on"
                $ Item_type = "gloves"
            "Take off your [Clothes[sleeves].short_name]?" if Clothes["sleeves"].string:
                $ verb = "take_off"
                $ Item_type = "sleeves"
            "Put on your [Outfit[sleeves].short_name]?" if not Clothes["sleeves"].string and Outfit["sleeves"].string and Character.position in Outfit["sleeves"].poses:
                $ verb = "try_on"
                $ Item_type = "sleeves"
            "Take off your [Clothes[boots].short_name]?" if Clothes["boots"].string:
                $ verb = "take_off"
                $ Item_type = "boots"
            "Put on your [Outfit[boots].short_name]?" if not Clothes["boots"].string and Outfit["boots"].string and Character.position in Outfit["boots"].poses:
                $ verb = "try_on"
                $ Item_type = "boots"
            "Take off your [Clothes[socks].short_name]?" if Clothes["socks"].string:
                $ verb = "take_off"
                $ Item_type = "socks"
            "Put on your [Outfit[socks].short_name]?" if not Clothes["socks"].string and Outfit["socks"].string and Character.position in Outfit["socks"].poses:
                $ verb = "try_on"
                $ Item_type = "socks"
            "Take off everything?" if not Character.naked:
                $ removed_Items = []

                python:
                    for C_type in removable_Clothing_types:
                        if Clothes[C_type].string:
                            removed_Items.append(Clothes[C_type])

                call does_Girl_agree_to_change_Clothes(Character, removed_Items = removed_Items, instant = False) from _call_does_Girl_agree_to_change_Clothes_7

                if _return:
                    call get_naked(Character) from _call_get_naked_1
            "Back":
                $ finished = True

        $ choice_disabled = True

        if verb == "undress":
            if state is None:
                $ state = Clothes[Item_type].undressed_states[Character.position]

            call expression f"ask_Girl_to_{verb}" pass (Clothing = Clothes[Item_type], state = state) from _call_expression_98
        elif verb in ["redress", "take_off"]:
            call expression f"ask_Girl_to_{verb}" pass (Clothing = Clothes[Item_type]) from _call_expression_99
        elif verb == "try_on":
            call expression f"ask_Girl_to_{verb}" pass (Clothing = Outfit[Item_type]) from _call_expression_100

        if _return and verb == "take_off":
            if Player.location == Player.home:
                $ Player.clothes_on_floor = True
            elif Player.location in bedrooms:
                python:
                    for C in active_Companions:
                        if Player.location == C.home:
                            C.clothes_on_floor = True

        python:
            for A in Character.all_Actions:
                if A.Action_type in ["touch_thighs_over_clothes", "touch_thighs_higher_over_clothes"] and not Character.thighs_covered:
                    stop_Action(A)
                elif A.Action_type == "touch_breasts_over_clothes" and not Character.breasts_covered:
                    stop_Action(A)
                elif A.Action_type == "touch_pussy_over_clothes" and not Character.pussy_covered:
                    stop_Action(A)
                elif A.Action_type == "grab_ass_over_clothes" and not Character.ass_covered:
                    stop_Action(A)
                elif A.Action_type in ["touch_thighs", "touch_thighs_higher"] and Character.thighs_covered:
                    stop_Action(A)
                elif A.Action_type in ["touch_breasts", "pinch_nipples", "suck_nipples"] and Character.breasts_covered:
                    stop_Action(A)
                elif A.Action_type in ["touch_pussy", "finger_pussy", "eat_pussy", "self_touch_pussy", "self_vibrator", "self_dildo_pussy", "sex", "vibrator", "dildo_pussy"] and Character.pussy_covered:
                    stop_Action(A)
                elif A.Action_type in ["finger_ass", "eat_ass", "self_finger_ass", "self_dildo_ass", "anal", "dildo_ass"] and Character.anus_covered:
                    stop_Action(A)

    return