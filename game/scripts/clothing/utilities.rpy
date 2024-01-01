init python:

    import copy

    def set_default_Outfits(Character, change = False):
        Outfits = eval(f"default_{Character.tag}_Outfits()")

        temp = list(Character.Wardrobe.Outfits.keys())[:]

        for O_name in temp:
            if Character.Wardrobe.Outfits[O_name].Outfit_type == "default":
                if Character.Wardrobe.Outfits[O_name].disabled:
                    for O in Outfits:
                        if O.name == O_name:
                            O.disabled = True

                del Character.Wardrobe.Outfits[O_name]

        for O in Outfits:
            Character.Wardrobe.Outfits.update({O.name: O})

        for O in Character.Wardrobe.Outfits.values():
            for Clothing in O.Clothes.values():
                if Clothing.name:
                    Character.give(Clothing)

        # exec(f"Character.give({Character.tag}_towel())")

        if change:
            Character.choose_Outfits()

        return

    def check_if_Clothes_in_Wardrobe(Character, Clothes):
        for C in Clothes.values():
            if C.name not in Character.Wardrobe.Clothes.keys():
                return False

        return True

label save_new_Outfit(Character, name, color, flags):
    $ new_Outfit = OutfitClass(name)

    python:
        for C in Character.Clothes.keys():
            new_Outfit.Clothes[C] = copy.copy(Character.Clothes[C])

    python:
        for Clothing_type in all_Clothing_types:
            new_Outfit.Clothes[Clothing_type].selected_state = new_Outfit.Clothes[Clothing_type].state

    call set_Outfit_flags(Character, new_Outfit, hypothetical = True) from _call_set_Outfit_flags_21

    python:
        for flag in flags:
            new_Outfit.flags.append(flag)

    $ new_Outfit.Outfit_type = "custom"
    $ new_Outfit.color = color

    if "public" in new_Outfit.flags or "exercise" in new_Outfit.flags or "hero" in new_Outfit.flags or "swim" in new_Outfit.flags:
        if ("public" not in new_Outfit.flags and ("exercise" in new_Outfit.flags or "hero" in new_Outfit.flags or "swim" in new_Outfit.flags) and approval_check(Character, threshold = 2.5*new_Outfit.shame, extra_condition = "new_Outfit")) or approval_check(Character, threshold = 4.0*new_Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Character.tag}_accept_public_Outfit" pass (Outfit = new_Outfit) from _call_expression_103

            if name in Character.Wardrobe.Outfits.keys():
                $ Character.Wardrobe.Outfits[name] = copy.deepcopy(new_Outfit)

                $ del new_Outfit
            else:
                $ Character.Wardrobe.Outfits.update({name: new_Outfit})

            $ Outfit_list = []

            python:
                for O in Character.Wardrobe.Outfits.values():
                    if O.Outfit_type == Wardrobe_tab:
                        Outfit_list.append(O)
                        
            if len(Outfit_list) > 0:
                $ current_Wardrobe_Outfit_page = current_Wardrobe_Outfit_page % math.ceil(len(Outfit_list)/3)
            else:
                $ current_Wardrobe_Outfit_page = 0
        else:
            call expression f"{Character.tag}_reject_public_Outfit" pass (Outfit = new_Outfit) from _call_expression_104

            $ del new_Outfit
    else:
        if approval_check(Character, threshold = 0.4*new_Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Character.tag}_accept_private_Outfit" pass (Outfit = new_Outfit) from _call_expression_105

            if name in Character.Wardrobe.Outfits.keys():
                $ Character.Wardrobe.Outfits[name] = copy.deepcopy(new_Outfit)

                $ del new_Outfit
            else:
                $ Character.Wardrobe.Outfits.update({name: new_Outfit})

            $ Outfit_list = []

            python:
                for O in Character.Wardrobe.Outfits.values():
                    if O.Outfit_type == Wardrobe_tab:
                        Outfit_list.append(O)

            if len(Outfit_list) > 0:
                $ current_Wardrobe_Outfit_page = current_Wardrobe_Outfit_page % math.ceil(len(Outfit_list)/3)
            else:
                $ current_Wardrobe_Outfit_page = 0
        else:
            call expression f"{Character.tag}_reject_private_Outfit" pass (Outfit = new_Outfit) from _call_expression_106

            $ del new_Outfit

    return

label edit_Outfit(Character, Outfit, name, color, flags):
    python:
        for Clothing_type in all_Clothing_types:
            Outfit.Clothes[Clothing_type].selected_state = Outfit.Clothes[Clothing_type].state

    call set_Outfit_flags(Character, Outfit, hypothetical = True) from _call_set_Outfit_flags_22

    if "public" in flags or "exercise" in flags or "swim" in flags:
        if ("public" not in flags and ("exercise" in flags or "swim" in flags) and approval_check(Character, threshold = 2.5*Character.Outfit.shame, extra_condition = "new_Outfit")) or approval_check(Character, threshold = 4.0*Character.Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Character.tag}_accept_public_Outfit" pass (Outfit = Outfit) from _call_expression_107
        else:
            call expression f"{Character.tag}_reject_public_Outfit" pass (Outfit = Outfit) from _call_expression_108

            return
    else:
        if approval_check(Character, threshold = 0.4*Character.Outfit.shame, extra_condition = "new_Outfit"):
            call expression f"{Character.tag}_accept_private_Outfit" pass (Outfit = Outfit) from _call_expression_109
        else:
            call expression f"{Character.tag}_reject_private_Outfit" pass (Outfit = Outfit) from _call_expression_110

            return

    $ Outfit.flags  = []

    python:
        for flag in flags:
            Outfit.flags.append(flag)

    $ Outfit.color = color
    
    $ old_name = Outfit.name
    $ Outfit.name = name

    $ Character.Wardrobe.Outfits[Outfit.name] = copy.deepcopy(Outfit)

    if old_name != Outfit.name:
        $ del Character.Wardrobe.Outfits[old_name]

    call change_Outfit(Character, Outfit, instant = True) from _call_change_Outfit_25

    $ Outfit_list = []

    $ del Outfit

    python:
        for O in Character.Wardrobe.Outfits.values():
            if O.Outfit_type == Wardrobe_tab:
                Outfit_list.append(O)

    if len(Outfit_list) > 0:
        $ current_Wardrobe_Outfit_page = current_Wardrobe_Outfit_page % math.ceil(len(Outfit_list)/3)
    else:
        $ current_Wardrobe_Outfit_page = 0

    return

label review_Outfit(Character):
    call debrief_Outfit_change(Character, instant = True) from _call_debrief_Outfit_change
    
    $ Outfit_changed = False

    python:
        for Clothing_type in all_Clothing_types:
            if Character.previous_Outfit not in Character.Wardrobe.Outfits.keys() or Character.Outfit.Clothes[Clothing_type].string != Character.Wardrobe.Outfits[Character.previous_Outfit].Clothes[Clothing_type].string:
                Outfit_changed = True

                break

    if not Outfit_changed:
        call change_Outfit(Character, Character.Wardrobe.Outfits[Character.previous_Outfit], instant = True) from _call_change_Outfit_26

    if Outfit_changed:
        $ say_obscured = True

        $ flag = are_Characters_in_Partners(Present)

        if "public" in Character.Outfit.flags or (("exercise" in Character.Outfit.flags or "hero" in Character.Outfit.flags) and Player.location == "bg_danger") or ("swim" in Character.Outfit.flags and Player.location == "bg_pool") or ("sleep" in Character.Outfit.flags and Player.location in bedrooms and flag):
            pass
        elif approval_check(Character, threshold = 4.0*Character.Outfit.shame):
            call expression f"{Character.tag}_accept_public_Outfit" pass (Outfit = Character.Outfit) from _call_expression_112
        elif Player.location not in public_locations and flag and approval_check(Character, threshold = 0.4*Character.Outfit.shame):
            call expression f"{Character.tag}_accept_private_Outfit" pass (Outfit = Character.Outfit) from _call_expression_113
        elif Player.location in public_locations or not flag:
            call expression f"{Character.tag}_reject_public_Outfit" pass (Outfit = Character.Outfit) from _call_expression_129

            call set_Character_Outfits(Character) from _call_set_Character_Outfits_28
        elif (("exercise" in Character.Outfit.flags or "hero" in Character.Outfit.flags) and Player.location != "bg_danger") or ("swim" in Character.Outfit.flags and Player.location != "bg_pool") or ("sleep" in Character.Outfit.flags and Player.location not in bedrooms):
            call expression f"{Character.tag}_reject_contextual_Outfit" pass (Outfit = Character.Outfit) from _call_expression_111

            call set_Character_Outfits(Character) from _call_set_Character_Outfits_5
        else:
            call expression f"{Character.tag}_reject_private_Outfit" pass (Outfit = Character.Outfit) from _call_expression_114

            call set_Character_Outfits(Character) from _call_set_Character_Outfits_6

        $ say_obscured = False

    $ Character.Wardrobe.replace_disabled_Outfits()

    hide screen Wardrobe_screen
    
    if Character.location == Player.location:
        show screen interactions_screen(Character)

    return

label debrief_Outfit_change(Characters, instant = False):
    call set_music from _call_set_music
    
    if Characters in all_Companions:
        $ Characters = [Characters]

    if renpy.get_screen("shop_screen"):
        call set_Character_Outfits(Characters, instant = instant) from _call_set_Character_Outfits_7

    if not renpy.get_screen("shop_screen") and changed_body_hair:
        $ renpy.dynamic(temp_Characters = [])

        python:
            for G in Characters:
                if G.body_hair["pubic"] != G.desired_body_hair["pubic"]:
                    temp_Characters.append(G)

        call Characters_will_shave(temp_Characters) from _call_Characters_will_shave

        $ changed_body_hair = False

    hide screen shop_screen

    $ belt_hidden = False
    $ say_obscured = False
    $ choice_disabled = False
    $ Character_picker_disabled = False

    return