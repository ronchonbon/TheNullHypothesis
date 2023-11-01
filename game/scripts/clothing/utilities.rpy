init python:

    import copy

    def set_default_Outfits(Girl, change = False):
        Outfits = eval(f"default_{Girl.tag}_Outfits()")

        temp = list(Girl.Wardrobe.Outfits.keys())[:]

        for O_name in temp:
            if Girl.Wardrobe.Outfits[O_name].Outfit_type == "default":
                if Girl.Wardrobe.Outfits[O_name].disabled:
                    for O in Outfits:
                        if O.name == O_name:
                            O.disabled = True

                del Girl.Wardrobe.Outfits[O_name]

        for O in Outfits:
            Girl.Wardrobe.Outfits.update({O.name: O})

        for O in Girl.Wardrobe.Outfits.values():
            for Clothing in O.Clothes.values():
                if Clothing.name:
                    Girl.give(Clothing)

        exec(f"Girl.give({Girl.tag}_towel())")

        if change:
            Girl.choose_Outfits()

        return

    def check_if_Clothes_in_Wardrobe(Girl, Clothes):
        for C in Clothes.values():
            if C.name not in Girl.Wardrobe.Clothes.keys():
                return False

        return True

label save_new_Outfit(Girl, name, color, flags):
    $ new_Outfit = OutfitClass(name)

    python:
        for C in Girl.Clothes.keys():
            new_Outfit.Clothes[C] = copy.copy(Girl.Clothes[C])

    python:
        for Clothing_type in all_Clothing_types:
            new_Outfit.Clothes[Clothing_type].selected_state = new_Outfit.Clothes[Clothing_type].state

    call set_Outfit_flags(Girl, new_Outfit, hypothetical = True) from _call_set_Outfit_flags_21
    
    if flags["wear_in_public"]:
        $ new_Outfit.wear_in_public = True

    if flags["wear_in_private"]:
        $ new_Outfit.wear_in_private = True

    if flags["activewear"]:
        $ new_Outfit.activewear = True
        
    if flags["swimwear"]:
        $ new_Outfit.swimwear = True

    if flags["datewear"]:
        $ new_Outfit.datewear = True

    if flags["sexwear"]:
        $ new_Outfit.sexwear = True

    if flags["sleepwear"]:
        $ new_Outfit.sleepwear = True

    if flags["winterwear"]:
        $ new_Outfit.winterwear = True

    $ new_Outfit.Outfit_type = "custom"
    $ new_Outfit.color = color

    if new_Outfit.wear_in_public or new_Outfit.activewear or new_Outfit.swimwear:
        if (not new_Outfit.wear_in_public and (new_Outfit.activewear or new_Outfit.swimwear) and approval_check(Girl, threshold = 2.5*new_Outfit.shame, extra_condition = "new_Outfit")) or approval_check(Girl, threshold = 4.0*new_Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Girl.tag}_accept_public_Outfit" pass (Outfit = new_Outfit) from _call_expression_103

            if name in Girl.Wardrobe.Outfits.keys():
                $ Girl.Wardrobe.Outfits[name] = copy.deepcopy(new_Outfit)

                $ del new_Outfit
            else:
                $ Girl.Wardrobe.Outfits.update({name: new_Outfit})

            $ Outfit_list = []

            python:
                for O in Girl.Wardrobe.Outfits.values():
                    if O.Outfit_type == Wardrobe_tab:
                        Outfit_list.append(O)
                        
            if len(Outfit_list) > 0:
                $ current_Wardrobe_Outfit_page = current_Wardrobe_Outfit_page % math.ceil(len(Outfit_list)/3)
            else:
                $ current_Wardrobe_Outfit_page = 0
        else:
            call expression f"{Girl.tag}_reject_public_Outfit" pass (Outfit = new_Outfit) from _call_expression_104

            $ del new_Outfit
    else:
        if approval_check(Girl, threshold = 0.4*new_Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Girl.tag}_accept_private_Outfit" pass (Outfit = new_Outfit) from _call_expression_105

            if name in Girl.Wardrobe.Outfits.keys():
                $ Girl.Wardrobe.Outfits[name] = copy.deepcopy(new_Outfit)

                $ del new_Outfit
            else:
                $ Girl.Wardrobe.Outfits.update({name: new_Outfit})

            $ Outfit_list = []

            python:
                for O in Girl.Wardrobe.Outfits.values():
                    if O.Outfit_type == Wardrobe_tab:
                        Outfit_list.append(O)

            if len(Outfit_list) > 0:
                $ current_Wardrobe_Outfit_page = current_Wardrobe_Outfit_page % math.ceil(len(Outfit_list)/3)
            else:
                $ current_Wardrobe_Outfit_page = 0
        else:
            call expression f"{Girl.tag}_reject_private_Outfit" pass (Outfit = new_Outfit) from _call_expression_106

            $ del new_Outfit

    return

label edit_Outfit(Girl, Outfit, name, color, flags):
    python:
        for Clothing_type in all_Clothing_types:
            Outfit.Clothes[Clothing_type].selected_state = Outfit.Clothes[Clothing_type].state

    call set_Outfit_flags(Girl, Outfit, hypothetical = True) from _call_set_Outfit_flags_22

    if flags["wear_in_public"] or flags["activewear"] or flags["swimwear"]:
        if (not flags["wear_in_public"] and (flags["activewear"] or flags["swimwear"]) and approval_check(Girl, threshold = 2.5*Girl.Outfit.shame, extra_condition = "new_Outfit")) or approval_check(Girl, threshold = 4.0*Girl.Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Girl.tag}_accept_public_Outfit" pass (Outfit = Outfit) from _call_expression_107
        else:
            call expression f"{Girl.tag}_reject_public_Outfit" pass (Outfit = Outfit) from _call_expression_108

            return
    else:
        if approval_check(Girl, threshold = 0.4*Girl.Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Girl.tag}_accept_private_Outfit" pass (Outfit = Outfit) from _call_expression_109
        else:
            call expression f"{Girl.tag}_reject_private_Outfit" pass (Outfit = Outfit) from _call_expression_110

            return

    if flags["wear_in_public"]:
        $ Outfit.wear_in_public = True
    else:
        $ Outfit.wear_in_public = False

    if flags["wear_in_private"]:
        $ Outfit.wear_in_private = True
    else:
        $ Outfit.wear_in_private = False

    if flags["activewear"]:
        $ Outfit.activewear = True
    else:
        $ Outfit.activewear = False
        
    if flags["swimwear"]:
        $ Outfit.swimwear = True
    else:
        $ Outfit.swimwear = False

    if flags["datewear"]:
        $ Outfit.datewear = True
    else:
        $ Outfit.datewear = False

    if flags["sexwear"]:
        $ Outfit.sexwear = True
    else:
        $ Outfit.sexwear = False

    if flags["sleepwear"]:
        $ Outfit.sleepwear = True
    else:
        $ Outfit.sleepwear = False
        
    if flags["winterwear"]:
        $ Outfit.winterwear = True
    else:
        $ Outfit.winterwear = False

    $ Outfit.color = color
    
    $ old_name = Outfit.name
    $ Outfit.name = name

    $ Girl.Wardrobe.Outfits[Outfit.name] = copy.deepcopy(Outfit)

    if old_name != Outfit.name:
        $ del Girl.Wardrobe.Outfits[old_name]

    call change_Outfit(Girl, Outfit, instant = True) from _call_change_Outfit_25

    $ Outfit_list = []

    $ del Outfit

    python:
        for O in Girl.Wardrobe.Outfits.values():
            if O.Outfit_type == Wardrobe_tab:
                Outfit_list.append(O)

    if len(Outfit_list) > 0:
        $ current_Wardrobe_Outfit_page = current_Wardrobe_Outfit_page % math.ceil(len(Outfit_list)/3)
    else:
        $ current_Wardrobe_Outfit_page = 0

    return

label review_Outfit(Girl):
    call debrief_Outfit_change(Girl, instant = True) from _call_debrief_Outfit_change
    
    $ Outfit_changed = False

    python:
        for Clothing_type in all_Clothing_types:
            if Girl.previous_Outfit not in Girl.Wardrobe.Outfits.keys() or Girl.Outfit.Clothes[Clothing_type].string != Girl.Wardrobe.Outfits[Girl.previous_Outfit].Clothes[Clothing_type].string:
                Outfit_changed = True

                break

    if not Outfit_changed:
        call change_Outfit(Girl, Girl.Wardrobe.Outfits[Girl.previous_Outfit], instant = True) from _call_change_Outfit_26

    if Outfit_changed:
        $ say_obscured = True

        $ flag = are_Characters_in_Partners(Present)

        if Girl.Outfit.wear_in_public or (Girl.Outfit.activewear and Player.location == "bg_danger") or (Girl.Outfit.swimwear and Player.location == "bg_pool") or (Girl.Outfit.sleepwear and Player.location in bedrooms and flag):
            pass
        elif approval_check(Girl, threshold = 4.0*Girl.Outfit.shame):
            call expression f"{Girl.tag}_accept_public_Outfit" pass (Outfit = Girl.Outfit) from _call_expression_112
        elif Player.location not in public_locations and flag and approval_check(Girl, threshold = 0.4*Girl.Outfit.shame):
            call expression f"{Girl.tag}_accept_private_Outfit" pass (Outfit = Girl.Outfit) from _call_expression_113
        elif Player.location in public_locations or not flag:
            call expression f"{Girl.tag}_reject_public_Outfit" pass (Outfit = Girl.Outfit) from _call_expression_129

            call set_Character_Outfits(Girl) from _call_set_Character_Outfits_28
        elif (Girl.Outfit.activewear and Player.location != "bg_danger") or (Girl.Outfit.swimwear and Player.location != "bg_pool") or (Girl.Outfit.sleepwear and Player.location not in bedrooms):
            call expression f"{Girl.tag}_reject_contextual_Outfit" pass (Outfit = Girl.Outfit) from _call_expression_111

            call set_Character_Outfits(Girl) from _call_set_Character_Outfits_5
        else:
            call expression f"{Girl.tag}_reject_private_Outfit" pass (Outfit = Girl.Outfit) from _call_expression_114

            call set_Character_Outfits(Girl) from _call_set_Character_Outfits_6

        $ say_obscured = False

    $ Girl.Wardrobe.replace_disabled_Outfits()

    hide screen Wardrobe_screen
    
    if Girl.location == Player.location:
        show screen interactions_screen(Girl)

    return

label debrief_Outfit_change(Girls, instant = False):
    call set_music from _call_set_music
    
    if Girls in all_Girls:
        $ Girls = [Girls]

    if renpy.get_screen("shop_screen"):
        call set_Character_Outfits(Girls, instant = instant) from _call_set_Character_Outfits_7

    if not renpy.get_screen("shop_screen") and changed_pubes:
        $ temp_shaving_Girls = []

        python:
            for G in Girls:
                if G.pubes != G.desired_pubes:
                    temp_shaving_Girls.append(G)

        call Girls_will_shave(temp_shaving_Girls) from _call_Girls_will_shave

        $ changed_pubes = False

    hide screen shop_screen

    $ belt_hidden = False
    $ say_obscured = False
    $ choice_disabled = False
    $ Character_picker_disabled = False

    return