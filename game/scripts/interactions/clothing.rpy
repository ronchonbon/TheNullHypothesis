label give_Character_Clothing(Character, Clothing):
    hide screen Player_menu

    if (Clothing.shop_type in ["sex", "lingerie"] and approval_check(Character, threshold = Clothing.thresholds["accept"], extra_condition = "sexy_gifts")) or approval_check(Character, threshold = Clothing.thresholds["accept"]):
        call expression f"{Character.tag}_{Clothing.string}_gift_accept" from _call_expression_154

        $ Clothing.gift = True

        $ Character.give(Clothing)
            
        $ set_default_Outfits(Character, change = False)

        $ del Player.inventory[Clothing.string]
    else:
        if Character.History.check(f"said_no_to_{Clothing.string}", tracker = "recent") > 1:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_946
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_947

            call expression f"{Character.tag}_rejected_Clothing_twice" from _call_expression_156
        elif Character.History.check(f"said_no_to_{Clothing.string}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_948

            call expression f"{Character.tag}_rejected_Clothing_once" from _call_expression_157
        else:
            call expression f"{Character.tag}_{Clothing.string}_gift_reject" from _call_expression_158

        $ Character.History.update(f"said_no_to_{Clothing.string}")

    if Character.location == Player.location:
        show screen interactions_screen(Character)

    return

label ask_Character_to_change_Outfit(Character, Outfit_name, instant = False):
    call set_Outfit_flags(Character, Character.Wardrobe.Outfits[Outfit_name], hypothetical = True) from _call_set_Outfit_flags_24

    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_change_Outfit_reject_mad" from _call_expression_159

        $ Character.History.update("refused_to_change_Outfit")
    elif approval_check(Character, threshold = "change_Outfit") and approval_check(Character, threshold = 0.5*Character.Wardrobe.Outfits[Outfit_name].shame):
        $ Items_to_remove, Items_to_add = get_changed_Items(Character, Character.Wardrobe.Outfits[Outfit_name])

        call does_Character_want_privacy(Character, Items_to_add = Items_to_add, Items_to_remove = Items_to_remove) from _call_does_Character_want_privacy_1

        if (Items_to_add or Items_to_remove) and _return:
            call expression f"{Character.tag}_change_Outfit_accept_with_privacy_before" pass (Outfit_name = Outfit_name) from _call_expression_166

            call change_Outfit(Character, Character.Wardrobe.Outfits[Outfit_name], instant = instant) from _call_change_Outfit_38

            call expression f"{Character.tag}_change_Outfit_accept_with_privacy_after" pass (Outfit_name = Outfit_name) from _call_expression_167
        else:
            call expression f"{Character.tag}_change_Outfit_accept_before" pass (Outfit_name = Outfit_name) from _call_expression_160

            call change_Outfit(Character, Character.Wardrobe.Outfits[Outfit_name], instant = instant) from _call_change_Outfit_37

            call expression f"{Character.tag}_change_Outfit_accept_after" pass (Outfit_name = Outfit_name) from _call_expression_161
    else:
        if Character.History.check("refused_to_change_Outfit", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_952
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_953
            
            call expression f"{Character.tag}_change_Outfit_reject_asked_twice" from _call_expression_169
        elif Character.History.check("refused_to_change_Outfit", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_954
            
            call expression f"{Character.tag}_change_Outfit_reject_asked_once" from _call_expression_170
        else:
            call expression f"{Character.tag}_change_Outfit_reject" from _call_expression_171

        $ Character.History.update("refused_to_change_Outfit")

    return

label ask_Character_to_try_on(Clothing, instant = False):
    $ Character = Clothing.Owner

    $ renpy.dynamic(temp_Clothes = removable_Clothing_types[:])

    $ temp_Clothes = list(reversed(temp_Clothes))

    while temp_Clothes:
        if Clothing.string in Character.Clothes[temp_Clothes[0]].incompatibilities or Character.Clothes[temp_Clothes[0]].string in Clothing.incompatibilities:
            $ Clothing_name = Character.Clothes[temp_Clothes[0]].name
            
            "She'll have to take off her [Clothing_name] first."

            return

        $ temp_Clothes.remove(temp_Clothes[0])

    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_change_Outfit_reject_mad" from _call_expression_172

        $ Character.History.update(f"said_no_to_{Clothing.string}")
    elif renpy.get_screen("shop_screen") and approval_check(Character, threshold = Clothing.thresholds["wear_in_private"]) and len(Present) == 1:
        if not Character.History.check(f"wore_{Clothing.string}", tracker = "recent"):
            if Clothing.Clothing_type == "hair" and Clothing.string not in ["bun", "ponytail", "mohawk", "wet_mohawk"]:
                call expression f"{Character.tag}_{Clothing.string}_hair_change_private_before" from _call_expression_173
            else:
                call expression f"{Character.tag}_{Clothing.string}_change_private_before" from _call_expression_174
            
        call does_Character_agree_to_change_Clothes(Character, added_Items = [Clothing], instant = instant) from _call_does_Character_agree_to_change_Clothes_3

        if _return and not Character.History.check(f"wore_{Clothing.string}", tracker = "recent"):
            if Clothing.Clothing_type == "hair" and Clothing.string not in ["bun", "ponytail", "mohawk", "wet_mohawk"]:
                call expression f"{Character.tag}_{Clothing.string}_hair_change_private_after" from _call_expression_175
            else:
                call expression f"{Character.tag}_{Clothing.string}_change_private_after" from _call_expression_176

            $ Character.History.update(f"wore_{Clothing.string}")

            return True
    elif approval_check(Character, threshold = Clothing.thresholds["wear_in_public"]):
        if not Character.History.check(f"wore_{Clothing.string}", tracker = "recent"):
            if Clothing.Clothing_type == "hair" and Clothing.string not in ["bun", "ponytail", "mohawk", "wet_mohawk"]:
                call expression f"{Character.tag}_{Clothing.string}_hair_change_public_before" from _call_expression_177
            else:
                call expression f"{Character.tag}_{Clothing.string}_change_public_before" from _call_expression_178
                
        call does_Character_agree_to_change_Clothes(Character, added_Items = [Clothing], instant = instant) from _call_does_Character_agree_to_change_Clothes_4

        if _return and not Character.History.check(f"wore_{Clothing.string}", tracker = "recent"):
            if Clothing.Clothing_type == "hair" and Clothing.string not in ["bun", "ponytail", "mohawk", "wet_mohawk"]:
                call expression f"{Character.tag}_{Clothing.string}_hair_change_public_after" from _call_expression_179
            else:
                call expression f"{Character.tag}_{Clothing.string}_change_public_after" from _call_expression_180

            $ Character.History.update(f"wore_{Clothing.string}")

            return True
    else:
        if Character.History.check(f"said_no_to_{Clothing.string}", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_955
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_956
            
            call expression f"{Character.tag}_rejected_Clothing_twice" from _call_expression_182
        elif Character.History.check(f"said_no_to_{Clothing.string}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_957

            call expression f"{Character.tag}_rejected_Clothing_once" from _call_expression_183
        else:
            call expression f"{Character.tag}_change_Outfit_reject" from _call_expression_184

        $ Character.History.update(f"said_no_to_{Clothing.string}")

    return False

label ask_Character_to_take_off(Clothing, instant = False):
    $ Character = Clothing.Owner

    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_change_Outfit_reject_mad" from _call_expression_185

        $ Character.History.update("refused_to_change_Outfit")
    elif approval_check(Character, threshold = "change_Outfit"):
        if not Character.Clothes[Clothing.Clothing_type].string:
            call expression f"{Character.tag}_not_wearing_Clothing_type" pass (Clothing_type = Clothing.Clothing_type) from _call_expression_186

            return

        call does_Character_agree_to_change_Clothes(Character, removed_Items = [Clothing], instant = instant) from _call_does_Character_agree_to_change_Clothes_5

        if _return:
            return True
    else:
        if Character.History.check("refused_to_change_Outfit", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_958
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_959
            
            call expression f"{Character.tag}_change_Outfit_reject_asked_twice" from _call_expression_188
        elif Character.History.check("refused_to_change_Outfit", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_960
            
            call expression f"{Character.tag}_change_Outfit_reject_asked_once" from _call_expression_189
        else:
            call expression f"{Character.tag}_change_Outfit_reject" from _call_expression_190

        $ Character.History.update("refused_to_change_Outfit")

    return False

label ask_Character_to_undress(Clothing, state = None, instant = False):
    $ Character = Clothing.Owner

    if state is None:
        $ state = Character.Clothes[Clothing.Clothing_type].undressed_states[Character.position]

    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_change_Outfit_reject_mad" from _call_expression_191

        $ Character.History.update("refused_to_change_Outfit")
    elif approval_check(Character, threshold = "change_Outfit"):
        call does_Character_agree_to_change_Clothes(Character, undressed_Items = [Clothing], undressed_states = [state], instant = instant) from _call_does_Character_agree_to_change_Clothes_6

        if _return:
            return True
    else:
        if Character.History.check("refused_to_change_Outfit", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_961
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_962

            call expression f"{Character.tag}_change_Outfit_reject_asked_twice" from _call_expression_193
        elif Character.History.check("refused_to_change_Outfit", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_963

            call expression f"{Character.tag}_change_Outfit_reject_asked_once" from _call_expression_194
        else:
            call expression f"{Character.tag}_change_Outfit_reject" from _call_expression_195

        $ Character.History.update("refused_to_change_Outfit")

    return False

label ask_Character_to_redress(Clothing, state = 0, instant = False):
    $ Character = Clothing.Owner

    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_change_Outfit_reject_mad" from _call_expression_196

        $ Character.History.update("refused_to_change_Outfit")
    elif approval_check(Character, threshold = "change_Outfit"):
        $ renpy.dynamic(temp_Clothing_types = removable_Clothing_types[:])

        while temp_Clothing_types:
            if Character.Clothes[temp_Clothing_types[0]].string:
                if Clothing.string in Character.Clothes[temp_Clothing_types[0]].covered_by.keys() and state in Character.Clothes[temp_Clothing_types[0]].covered_by[Clothing.string]:
                    if Character.Clothes[temp_Clothing_types[0]].state > 0:
                        call fix(Character, temp_Clothing_types[0], state = 0, instant = instant) from _call_fix

            $ temp_Clothing_types.remove(temp_Clothing_types[0])
        
        call fix(Character, Clothing.Clothing_type, state = state, instant = instant) from _call_fix_1

        return True
    else:
        if Character.History.check("refused_to_change_Outfit", tracker = "recent") >= 2:
            call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_964
            call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_965

            call expression f"{Character.tag}_change_Outfit_reject_asked_twice" from _call_expression_198
        elif Character.History.check("refused_to_change_Outfit", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_966

            call expression f"{Character.tag}_change_Outfit_reject_asked_once" from _call_expression_199
        else:
            call expression f"{Character.tag}_change_Outfit_reject" from _call_expression_200

        $ Character.History.update("refused_to_change_Outfit")

    return False

label does_Character_agree_to_change_Clothes(Character, added_Items = None, removed_Items = None, undressed_Items = None, undressed_states = None, automatic = False, instant = False):
    if not added_Items:
        $ added_Items = []
    
    if not removed_Items:
        $ removed_Items = []

    if not undressed_Items:
        $ undressed_Items = []
    else:
        if not undressed_states:
            $ undressed_states = []
        
    $ hypothetical_Outfit = create_hypothetical_Outfit(Character, added_Items = added_Items, removed_Items = removed_Items, undressed_Items = undressed_Items, undressed_states = undressed_states, only_final = instant)

    call set_Outfit_flags(Character, hypothetical_Outfit, hypothetical = True) from _call_set_Outfit_flags_25

    $ shown_body_parts = []

    python:
        for body_part in ["pussy", "breasts", "underwear", "bra"]:
            if body_part in ["underwear", "bra"] and not hypothetical_Outfit.Clothes[body_part].string:
                continue

            if Character.check_traits(f"{body_part}_hidden") and not hypothetical_Outfit.check_traits(f"{body_part}_hidden"):
                shown_body_parts.append(body_part)

    $ agrees_to_remove = True

    if shown_body_parts:
        $ renpy.dynamic(temp_body_parts = shown_body_parts[:])
        
        while temp_body_parts and agrees_to_remove:
            if not Character.History.check(f"seen_{temp_body_parts[0]}", tracker = "recent"):
                if approval_check(Character, threshold = f"see_{temp_body_parts[0]}"):
                    if not automatic:
                        if Character.History.check(f"seen_{temp_body_parts[0]}") == 1:
                            call expression f"{Character.tag}_accepts_show_{temp_body_parts[0]}_before_first_time" from _call_expression_201
                        elif Character.History.check(f"seen_{temp_body_parts[0]}") == 2:
                            call expression f"{Character.tag}_accepts_show_{temp_body_parts[0]}_before_second_time" from _call_expression_202
                        elif approval_check(Character, threshold = "love"):
                            call expression f"{Character.tag}_accepts_show_{temp_body_parts[0]}_before_love" from _call_expression_203
                        else:
                            call expression f"{Character.tag}_accepts_show_{temp_body_parts[0]}_before" from _call_expression_204

                        $ temp_body_parts = []
                else:
                    if Character.History.check(f"refused_to_show_{temp_body_parts[0]}", tracker = "recent") >= 2:
                        call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_967
                        call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_968

                        call expression f"{Character.tag}_rejects_show_{temp_body_parts[0]}_asked_twice" from _call_expression_206
                    elif Character.History.check(f"refused_to_show_{temp_body_parts[0]}", tracker = "recent") == 1:
                        call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_969

                        call expression f"{Character.tag}_rejects_show_{temp_body_parts[0]}_asked_once" from _call_expression_207
                    else:
                        call expression f"{Character.tag}_rejects_show_{temp_body_parts[0]}" from _call_expression_208

                    $ Character.History.update(f"refused_to_show_{temp_body_parts[0]}")

                    $ agrees_to_remove = False

            if temp_body_parts:
                $ temp_body_parts.remove(temp_body_parts[0])

    $ del hypothetical_Outfit

    if agrees_to_remove:
        $ actual_Outfit = create_hypothetical_Outfit(Character, added_Items = added_Items, removed_Items = removed_Items, undressed_Items = undressed_Items, undressed_states = undressed_states, only_final = True)
        $ actual_Outfit.name = Character.Outfit.name

        call change_Outfit(Character, actual_Outfit, instant = instant) from _call_change_Outfit_39
            
        if not automatic:
            while shown_body_parts:
                if not Character.History.check(f"seen_{shown_body_parts[0]}", tracker = "recent"):
                    if Character.History.check(f"seen_{shown_body_parts[0]}") == 1:
                        call expression f"{Character.tag}_accepts_show_{shown_body_parts[0]}_after_first_time" from _call_expression_209
                    elif Character.History.check(f"seen_{shown_body_parts[0]}") == 2:
                        call expression f"{Character.tag}_accepts_show_{shown_body_parts[0]}_after_second_time" from _call_expression_210
                    elif approval_check(Character, threshold = "love"):
                        call expression f"{Character.tag}_accepts_show_{shown_body_parts[0]}_after_love" from _call_expression_211
                    else:
                        call expression f"{Character.tag}_accepts_show_{shown_body_parts[0]}_after" from _call_expression_212

                $ shown_body_parts.remove(shown_body_parts[0])
    else:
        return False

    return True