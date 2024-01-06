init python:

    def get_changed_Items(Character, Outfit):
        Items_to_remove = []
        Items_to_add = []

        for C_type in reversed(removable_Clothing_types):
            if Character.Clothes[C_type].string and not Outfit.Clothes[C_type].string:
                Items_to_remove.append(Character.Clothes[C_type])

        for C_type in removable_Clothing_types:
            if Outfit.Clothes[C_type].string and Character.Clothes[C_type].string != Outfit.Clothes[C_type].string:
                Items_to_add.append(Outfit.Clothes[C_type])

        return Items_to_remove, Items_to_add

    def create_hypothetical_Outfit(Character, added_Items = None, removed_Items = None, undressed_Items = None, undressed_states = None, only_final = True):
        if not added_Items:
            added_Items = []
        
        if not removed_Items:
            removed_Items = []

        if not undressed_Items:
            undressed_Items = []
        else:
            if not undressed_states:
                undressed_states = []

        hypothetical_Outfit = OutfitClass("Hypothetical")

        for C in Character.Clothes.keys():
            hypothetical_Outfit.Clothes[C] = copy.copy(Character.Clothes[C])

        for i, I in enumerate(undressed_Items):
            hypothetical_Outfit.Clothes[I.Clothing_type] = copy.copy(I)

            if undressed_states:
                hypothetical_Outfit.Clothes[I.Clothing_type].state = undressed_states[i]
            else:
                hypothetical_Outfit.Clothes[I.Clothing_type].state = hypothetical_Outfit.Clothes[I.Clothing_type].undressed_states[Character.position]

            if not only_final:
                for C_type in removable_Clothing_types:
                    if hypothetical_Outfit.Clothes[C_type].string:
                        if hypothetical_Outfit.Clothes[C_type].string in I.covered_by.keys() and hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position] in I.covered_by[hypothetical_Outfit.Clothes[C_type].string]:
                            hypothetical_Outfit.Clothes[C_type] = null_Clothing
                        elif hypothetical_Outfit.Clothes[C_type].string in I.covered_by.keys():
                            hypothetical_Outfit.Clothes[C_type].state = hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position]

        for I in removed_Items:
            hypothetical_Outfit.Clothes[I.Clothing_type] = null_Clothing

            if not only_final:
                for C_type in removable_Clothing_types:
                    if hypothetical_Outfit.Clothes[C_type].string:
                        if hypothetical_Outfit.Clothes[C_type].string in I.blocked_by.keys() and hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position] in I.blocked_by[hypothetical_Outfit.Clothes[C_type].string]:
                            hypothetical_Outfit.Clothes[C_type] = null_Clothing
                        elif hypothetical_Outfit.Clothes[C_type].string in I.blocked_by.keys():
                            if hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position]:
                                hypothetical_Outfit.Clothes[C_type].state = hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position]
                            else:
                                hypothetical_Outfit.Clothes[C_type] = null_Clothing

        for I in added_Items:
            for C_type in removable_Clothing_types:
                if hypothetical_Outfit.Clothes[C_type].string:
                    if I.string in hypothetical_Outfit.Clothes[C_type].incompatibilities or hypothetical_Outfit.Clothes[C_type].string in I.incompatibilities:
                        hypothetical_Outfit.Clothes[C_type] = null_Clothing

                    if not only_final:
                        if hypothetical_Outfit.Clothes[C_type].string in I.blocked_by.keys() and hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position] in I.blocked_by[hypothetical_Outfit.Clothes[C_type].string]:
                            hypothetical_Outfit.Clothes[C_type] = null_Clothing
                        elif hypothetical_Outfit.Clothes[C_type].string in I.blocked_by.keys():
                            if hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position]:
                                hypothetical_Outfit.Clothes[C_type].state = hypothetical_Outfit.Clothes[C_type].undressed_states[Character.position]
                            else:
                                hypothetical_Outfit.Clothes[C_type] = null_Clothing

            if only_final:
                hypothetical_Outfit.Clothes[I.Clothing_type] = copy.copy(I)
                hypothetical_Outfit.Clothes[I.Clothing_type].state = hypothetical_Outfit.Clothes[I.Clothing_type].selected_state
            elif I.undressed_states[Character.position]:
                hypothetical_Outfit.Clothes[I.Clothing_type] = copy.copy(I)
                hypothetical_Outfit.Clothes[I.Clothing_type].state = hypothetical_Outfit.Clothes[I.Clothing_type].undressed_states[Character.position]

        return hypothetical_Outfit

label does_Character_want_privacy(Character, Items_to_add = None, Items_to_remove = None):
    $ Present = get_Present(location = Character.location)[0]

    if len(Present) > 1 and not are_Characters_in_Partners(Present):
        return True

    $ hypothetical_Outfit = create_hypothetical_Outfit(Character, added_Items = Items_to_add, removed_Items = Items_to_remove)

    call set_Outfit_flags(Character, hypothetical_Outfit, hypothetical = True) from _call_set_Outfit_flags

    if not approval_check(Character, threshold = "exhibitionism") or not Character.check_traits("exhibitionist"):
        if Character.location in public_locations:
            return True
        else:
            $ renpy.dynamic(temp_body_parts = ["bra", "underwear", "breasts", "pussy"])

            while temp_body_parts:
                if Character.check_traits(f"{temp_body_parts[0]}_hidden") and not hypothetical_Outfit.check_traits("f{temp_body_parts[0]}_hidden"):
                    if not Character.History.check(f"seen_{temp_body_parts[0]}") or not approval_check(Character, threshold = f"see_{temp_body_parts[0]}"):
                        return True

                $ temp_body_parts.remove(temp_body_parts[0])

    return False

label set_Outfit_flags(Character, Outfit = None, hypothetical = False):
    if not Outfit:
        $ Character.give_trait("naked")

        python:
            for C_type in removable_Clothing_types:
                if Character.Clothes[C_type].string:
                    Character.remove_trait("naked")

                    break

        $ Character.remove_trait("breasts_supported")

        python:
            for C_type in all_Clothing_types:
                if Character.Clothes[C_type].string:
                    if Character.Clothes[C_type].supports_breasts and Character.Clothes[C_type].state == 0:
                        Character.give_trait("breasts_supported")

                        break

        $ Character.Outfit.shame = 0

        python:
            for C_type in all_Clothing_types:
                Character.Clothes[C_type].covered = False
                Character.Clothes[C_type].blocked = False

                if Character.Clothes[C_type].name:
                    for candidate_type in all_Clothing_types:
                        if Character.Clothes[candidate_type].string:
                            if Character.Clothes[candidate_type].string in Character.Clothes[C_type].covered_by.keys() and Character.Clothes[candidate_type].state in Character.Clothes[C_type].covered_by[Character.Clothes[candidate_type].string]:
                                Character.Clothes[C_type].covered = True

                            if Character.Clothes[candidate_type].string in Character.Clothes[C_type].blocked_by.keys() and Character.Clothes[candidate_type].state in Character.Clothes[C_type].blocked_by[Character.Clothes[candidate_type].string]:
                                Character.Clothes[C_type].blocked = True

                    if Character.Clothes[C_type].covered or (("swimsuit" in Character.Clothes[C_type].name or "bikini" in Character.Clothes[C_type].name) and Character.location == "bg_pool"):
                        Character.Outfit.shame += Character.Clothes[C_type].shame[0]
                    else:
                        Character.Outfit.shame += Character.Clothes[C_type].shame[1]

        $ proper_subject = True

        $ renpy.dynamic(temp_body_parts = ["bra", "breasts", "back", "belly", "thighs", "underwear", "ass", "pussy", "anus", "feet"])

        while temp_body_parts:
            if temp_body_parts[0] not in ["bra", "underwear"] or Character.Clothes[temp_body_parts[0]].string:
                $ Character.remove_trait(f"{temp_body_parts[0]}_covered")
                $ Character.remove_trait(f"{temp_body_parts[0]}_hidden")

                $ covered = False
                $ hidden = False

                python:
                    for C_type in all_Clothing_types:
                        if Character.Clothes[C_type].string:
                            if Character.position in Character.Clothes[C_type].covers.keys():
                                if temp_body_parts[0] in Character.Clothes[C_type].covers[Character.position].keys() and Character.Clothes[C_type].state in Character.Clothes[C_type].covers[Character.position][temp_body_parts[0]]:
                                    Character.give_trait(f"{temp_body_parts[0]}_covered")

                                    covered = True

                            if Character.position in Character.Clothes[C_type].hides.keys():
                                if temp_body_parts[0] in Character.Clothes[C_type].hides[Character.position].keys() and Character.Clothes[C_type].state in Character.Clothes[C_type].hides[Character.position][temp_body_parts[0]]:
                                    Character.give_trait(f"{temp_body_parts[0]}_hidden")

                                    hidden = True
                
                if not covered:
                    $ Character.Outfit.shame += eval(f"{Character.tag}_Outfit_shame['{temp_body_parts[0]}_exposed']")
                elif not hidden:
                    $ Character.Outfit.shame += eval(f"{Character.tag}_Outfit_shame['{temp_body_parts[0]}_visible']")

                if not hypothetical and not black_screen and renpy.showing(f"{Character.tag}_sprite"):
                    if not hidden and Character.location != "hold" and Character.location == Player.location:
                        if temp_body_parts[0] in ["bra", "breasts", "underwear", "ass", "pussy", "anus"]:
                            if not Character.History.check(f"seen_{temp_body_parts[0]}", tracker = "recent"):
                                call expression f"{Character.tag}_seen_{temp_body_parts[0]}" pass (proper_subject = proper_subject)
                                
                                $ proper_subject = False

                        $ Character.History.update(f"seen_{temp_body_parts[0]}")

            $ temp_body_parts.remove(temp_body_parts[0])
    else:
        $ Outfit.shame = 0

        python:
            for C_type in all_Clothing_types:
                Outfit.Clothes[C_type].covered = False
                Outfit.Clothes[C_type].blocked = False

                if Outfit.Clothes[C_type].name:
                    for candidate_type in all_Clothing_types:
                        if Outfit.Clothes[candidate_type].string:
                            if Outfit.Clothes[candidate_type].string in Outfit.Clothes[C_type].covered_by.keys() and Outfit.Clothes[candidate_type].state in Outfit.Clothes[C_type].covered_by[Outfit.Clothes[candidate_type].string]:
                                Outfit.Clothes[C_type].covered = True

                            if Outfit.Clothes[candidate_type].string in Outfit.Clothes[C_type].blocked_by.keys() and Outfit.Clothes[candidate_type].state in Outfit.Clothes[C_type].blocked_by[Outfit.Clothes[candidate_type].string]:
                                Outfit.Clothes[C_type].blocked = True

                    if Outfit.Clothes[C_type].covered or (("swimsuit" in Outfit.Clothes[C_type].name or "bikini" in Outfit.Clothes[C_type].name) and Character.location == "bg_pool"):
                        Outfit.shame += Outfit.Clothes[C_type].shame[0]
                    else:
                        Outfit.shame += Outfit.Clothes[C_type].shame[1]
    
        $ renpy.dynamic(temp_body_parts = ["bra", "breasts", "back", "belly", "thighs", "underwear", "ass", "pussy", "anus", "feet"])

        while temp_body_parts:
            if temp_body_parts[0] not in ["bra", "underwear"] or Outfit.Clothes[temp_body_parts[0]].string:
                $ Outfit.remove_trait(f"{temp_body_parts[0]}_covered")
                $ Outfit.remove_trait(f"{temp_body_parts[0]}_hidden")

                $ covered = False
                $ hidden = False

                python:
                    for C_type in all_Clothing_types:
                        if Outfit.Clothes[C_type].string:
                            if Character.position in Outfit.Clothes[C_type].covers.keys():
                                if temp_body_parts[0] in Outfit.Clothes[C_type].covers[Character.position].keys() and Outfit.Clothes[C_type].state in Outfit.Clothes[C_type].covers[Character.position][temp_body_parts[0]]:
                                    Outfit.give_trait(f"{temp_body_parts[0]}_covered")

                                    covered = True

                            if Character.position in Outfit.Clothes[C_type].hides.keys():
                                if temp_body_parts[0] in Outfit.Clothes[C_type].hides[Character.position].keys() and Outfit.Clothes[C_type].state in Outfit.Clothes[C_type].hides[Character.position][temp_body_parts[0]]:
                                    Outfit.give_trait(f"{temp_body_parts[0]}_hidden")

                                    hidden = True
                
                if not covered:
                    $ Outfit.shame += eval(f"{Character.tag}_Outfit_shame['{temp_body_parts[0]}_exposed']")
                elif not hidden:
                    $ Outfit.shame += eval(f"{Character.tag}_Outfit_shame['{temp_body_parts[0]}_visible']")

            $ temp_body_parts.remove(temp_body_parts[0])
                
    return

label fix(Character, Clothing_type_to_fix, state = None, instant = False, final = True):
    if state is None:
        $ state = Character.Clothes[Clothing_type_to_fix].selected_state

    if Character.Clothes[Clothing_type_to_fix].state != state:
        $ Character.Clothes[Clothing_type_to_fix].state = state

        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_1

            $ renpy.pause(0.15, hard = True)
    else:
        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_2

    if not Character.Clothes[Clothing_type_to_fix].soiled:
        python:
            for part in ["breasts", "back", "belly", "ass", "feet"]:
                if part in Character.Clothes[Clothing_type_to_fix].covers[Character.position].keys() and Character.Clothes[Clothing_type_to_fix].state in Character.Clothes[Clothing_type_to_fix].covers[Character.position][part]:
                    Character.spunk[part] = False
                elif Character.persistent_spunk[part]:
                    Character.spunk[part] = 1
                else:
                    Character.spunk[part] = False

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_27

    return

label undress(Character, Clothing_type_to_undress, state = None, instant = False, final = True):
    if state is None:
        $ state = Character.Clothes[Clothing_type_to_undress].undressed_states[Character.position]

    if Character.Clothes[Clothing_type_to_undress].state != state:
        $ Character.Clothes[Clothing_type_to_undress].state = state

        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_3

            $ renpy.pause(0.15, hard = True)
    else:
        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_4

    if Character.Clothes[Clothing_type_to_undress].soiled:
        python:
            for part in ["breasts", "back", "belly", "ass", "feet"]:
                if (part not in Character.Clothes[Clothing_type_to_undress].covers[Character.position].keys() or Character.Clothes[Clothing_type_to_undress].state not in Character.Clothes[Clothing_type_to_undress].covers[Character.position][part]) or not Character.persistent_spunk[part]:
                    Character.spunk[part] = False

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_28

    return

label put_on(Character, Clothing_type_to_put_on, instant = False, final = True):
    if Character.Clothes[Clothing_type_to_put_on].state != Character.Clothes[Clothing_type_to_put_on].selected_state:
        $ Character.Clothes[Clothing_type_to_put_on].state = Character.Clothes[Clothing_type_to_put_on].selected_state

        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_5

            $ renpy.pause(0.15, hard = True)
    else:
        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_6

    if not Character.Clothes[Clothing_type_to_put_on].soiled:
        python:
            for part in ["breasts", "back", "belly", "ass", "feet"]:
                if part in Character.Clothes[Clothing_type_to_put_on].covers[Character.position].keys() and Character.Clothes[Clothing_type_to_put_on].state in Character.Clothes[Clothing_type_to_put_on].covers[Character.position][part]:
                    Character.spunk[part] = False
                elif Character.persistent_spunk[part]:
                    for Clothing_type in reversed(removable_Clothing_types):
                        Character.spunk[part] = 1

                        if part in Character.Clothes[Clothing_type].covers[Character.position].keys() and Character.Clothes[Clothing_type].state in Character.Clothes[Clothing_type].covers[Character.position][part]:
                            if Character.Clothes[Clothing_type].string and not Character.Clothes[Clothing_type].soiled:
                                Character.spunk[part] = False

                                break
                else:
                    Character.spunk[part] = False

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_29

    return

label try_on(Character, Clothing, redress = True, instant = False, final = True):
    if Character.Clothes[Clothing.Clothing_type].string:
        if Clothing.name == Character.Clothes[Clothing.Clothing_type].name:
            return

    call fix_clothing(Character, instant = instant, final = False) from _call_fix_clothing_1

    $ temp_trying_on_Clothes = {}

    python:
        for C in Character.Clothes.keys():
            temp_trying_on_Clothes[C] = copy.copy(Character.Clothes[C])

    $ renpy.dynamic(temp_Clothing_types = removable_Clothing_types[:])

    while temp_Clothing_types:
        if Character.Clothes[temp_Clothing_types[0]].string:
            if Clothing.string in Character.Clothes[temp_Clothing_types[0]].blocked_by.keys():
                if Character.Clothes[temp_Clothing_types[0]].state != Character.Clothes[temp_Clothing_types[0]].selected_state:
                    $ Character.Clothes[temp_Clothing_types[0]].state = Character.Clothes[temp_Clothing_types[0]].selected_state

                    if not instant:
                        call set_Outfit_flags(Character) from _call_set_Outfit_flags_7

                        $ renpy.pause(0.15, hard = True)

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    $ renpy.dynamic(temp_Clothing_types = list(reversed(removable_Clothing_types))[:])

    while temp_Clothing_types:
        if Character.Clothes[temp_Clothing_types[0]].string:
            if Character.Clothes[temp_Clothing_types[0]].string in Clothing.blocked_by.keys():
                if Character.Clothes[temp_Clothing_types[0]].undressed_states[Character.position] in Clothing.blocked_by[Character.Clothes[temp_Clothing_types[0]].string]:
                    call undress(Character, Character.Clothes[temp_Clothing_types[0]].Clothing_type, instant = instant, final = False) from _call_undress

                    $ Character.Clothes[temp_Clothing_types[0]] = null_Clothing
        
                    if not instant:
                        call set_Outfit_flags(Character) from _call_set_Outfit_flags_8

                        $ renpy.pause(0.15, hard = True)
                else:
                    call undress(Character, Character.Clothes[temp_Clothing_types[0]].Clothing_type, instant = instant, final = False) from _call_undress_1

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    $ renpy.dynamic(temp_Clothes = list(temp_trying_on_Clothes.values())[:])

    while temp_Clothes:
        if Clothing.string in temp_Clothes[0].incompatibilities or temp_Clothes[0].string in Clothing.incompatibilities:
            if Character.Clothes[temp_Clothes[0].Clothing_type].string:
                call undress(Character, temp_Clothes[0].Clothing_type, instant = instant, final = False) from _call_undress_2

                $ Character.Clothes[temp_Clothes[0].Clothing_type] = null_Clothing

                if not instant:
                    call set_Outfit_flags(Character) from _call_set_Outfit_flags_9

                    $ renpy.pause(0.15, hard = True)

            $ temp_trying_on_Clothes[temp_Clothes[0].Clothing_type] = null_Clothing

        $ temp_Clothes.remove(temp_Clothes[0])

    if Character.Clothes[Clothing.Clothing_type].name and Clothing.Clothing_type in removable_Clothing_types:
        call undress(Character, Clothing.Clothing_type, instant = instant, final = False) from _call_undress_3

        $ Character.Clothes[Clothing.Clothing_type] = null_Clothing

        if not instant:
            call set_Outfit_flags(Character) from _call_set_Outfit_flags_10

            $ renpy.pause(0.15, hard = True)

    $ Clothing.state = Clothing.undressed_states[Character.position]
    $ Character.Clothes[Clothing.Clothing_type] = Clothing
                    
    if not instant:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_11

        $ renpy.pause(0.15, hard = True)

    call put_on(Character, Clothing.Clothing_type, instant = instant, final = False) from _call_put_on

    if redress:
        $ temp_Clothing_types = removable_Clothing_types[:]

        while temp_Clothing_types:
            if temp_trying_on_Clothes[temp_Clothing_types[0]].string:
                if temp_trying_on_Clothes[temp_Clothing_types[0]].string in Character.Clothes[Clothing.Clothing_type].blocked_by.keys():
                    $ temp_trying_on_Clothes[temp_Clothing_types[0]].state = temp_trying_on_Clothes[temp_Clothing_types[0]].undressed_states[Character.position]
                    $ Character.Clothes[temp_Clothing_types[0]] = temp_trying_on_Clothes[temp_Clothing_types[0]]
                    
                    if not instant:
                        call set_Outfit_flags(Character) from _call_set_Outfit_flags_12

                        $ renpy.pause(0.15, hard = True)

                    call put_on(Character, temp_Clothing_types[0], instant = instant, final = False) from _call_put_on_1

            $ temp_Clothing_types.remove(temp_Clothing_types[0])

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_30

    return

label take_off(Character, Clothing_type_to_take_off, redress = True, instant = False, final = True):
    if not Character.Clothes[Clothing_type_to_take_off].string:
        return
    elif Clothing_type_to_take_off == "hair":
        return

    $ temp_taking_off_Clothes = {}

    python:
        for C in Character.Clothes.keys():
            temp_taking_off_Clothes[C] = copy.copy(Character.Clothes[C])

    $ renpy.dynamic(temp_Clothing_types = list(reversed(removable_Clothing_types))[:])

    while temp_Clothing_types:
        if Character.Clothes[temp_Clothing_types[0]].string:
            if Character.Clothes[temp_Clothing_types[0]].string in Character.Clothes[Clothing_type_to_take_off].blocked_by.keys():
                if Character.Clothes[temp_Clothing_types[0]].undressed_states[Character.position] in Character.Clothes[Clothing_type_to_take_off].blocked_by[Character.Clothes[temp_Clothing_types[0]].string]:
                    call undress(Character, Character.Clothes[temp_Clothing_types[0]].Clothing_type, instant = instant, final = False) from _call_undress_4

                    $ Character.Clothes[temp_Clothing_types[0]] = null_Clothing
        
                    if not instant:
                        call set_Outfit_flags(Character) from _call_set_Outfit_flags_13

                        $ renpy.pause(0.15, hard = True)
                else:
                    call undress(Character, Character.Clothes[temp_Clothing_types[0]].Clothing_type, instant = instant, final = False) from _call_undress_5

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    call undress(Character, Clothing_type_to_take_off, instant = instant, final = False) from _call_undress_6

    $ Character.Clothes[Clothing_type_to_take_off] = null_Clothing
    
    if not instant:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_14

        $ renpy.pause(0.15, hard = True)

    if redress:
        $ renpy.dynamic(temp_Clothing_types = removable_Clothing_types[:])

        while temp_Clothing_types:
            if temp_Clothing_types[0] != Clothing_type_to_take_off:
                if temp_taking_off_Clothes[temp_Clothing_types[0]].string:
                    if not Character.Clothes[temp_Clothing_types[0]].string:
                        $ temp_taking_off_Clothes[temp_Clothing_types[0]].state = temp_taking_off_Clothes[temp_Clothing_types[0]].undressed_states[Character.position]
                        $ Character.Clothes[temp_Clothing_types[0]] = temp_taking_off_Clothes[temp_Clothing_types[0]]
                        
                        if not instant:
                            call set_Outfit_flags(Character) from _call_set_Outfit_flags_15

                            $ renpy.pause(0.15, hard = True)

                        call put_on(Character, temp_Clothing_types[0], instant = instant, final = False) from _call_put_on_2

            $ temp_Clothing_types.remove(temp_Clothing_types[0])

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_31

    return

label take_off_everything_but(Character, Clothing_types, instant = False, final = True):
    if Clothing_types in all_Clothing_types:
        $ Clothing_types = [Clothing_types]

    $ temp_take_off_everything_but_Clothes = {}

    python:
        for C in Character.Clothes.keys():
            temp_take_off_everything_but_Clothes[C] = copy.copy(Character.Clothes[C])

    $ renpy.dynamic(temp_Clothing_types = list(reversed(removable_Clothing_types))[:])

    while temp_Clothing_types:
        if temp_Clothing_types[0] not in Clothing_types:
            call take_off(Character, temp_Clothing_types[0], redress = False, instant = instant, final = False) from _call_take_off_8

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    $ renpy.dynamic(temp_Clothing_types = removable_Clothing_types[:])

    while temp_Clothing_types:
        if temp_Clothing_types[0] in Clothing_types:
            if temp_take_off_everything_but_Clothes[temp_Clothing_types[0]].string:
                if not Character.Clothes[temp_Clothing_types[0]].string:
                    $ temp_take_off_everything_but_Clothes[temp_Clothing_types[0]].state = temp_take_off_everything_but_Clothes[temp_Clothing_types[0]].undressed_states[Character.position]
                    $ Character.Clothes[temp_Clothing_types[0]] = temp_take_off_everything_but_Clothes[temp_Clothing_types[0]]
        
                    if not instant:
                        call set_Outfit_flags(Character) from _call_set_Outfit_flags_16

                        $ renpy.pause(0.15, hard = True)

                    call put_on(Character, temp_Clothing_types[0], instant = instant, final = False) from _call_put_on_3

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_32

    return

label expose(Character, part, instant = False, final = True):
    $ renpy.dynamic(temp_Clothing_types = eval(f"{part}_hiding_Clothing_types")[:])

    while temp_Clothing_types:
        if Character.Clothes[temp_Clothing_types[0]].string and part in Character.Clothes[temp_Clothing_types[0]].covers[Character.position].keys() and Character.Clothes[temp_Clothing_types[0]].state in Character.Clothes[temp_Clothing_types[0]].covers[Character.position][part]:
            call undress(Character, temp_Clothing_types[0], instant = instant, final = False) from _call_undress_7

            if Character.Clothes[temp_Clothing_types[0]].state < 1:
                $ Character.Clothes[temp_Clothing_types[0]] = null_Clothing
        
                if not instant:
                    call set_Outfit_flags(Character) from _call_set_Outfit_flags_17
        
        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_33

    return

label get_naked(Character, under_towel = False, instant = False, final = True):
    $ renpy.dynamic(temp_Clothing_types = list(reversed(removable_Clothing_types))[:])

    while temp_Clothing_types:
        if not under_towel or temp_Clothing_types[0] != "towel":
            if Character.Clothes[temp_Clothing_types[0]].name:
                call undress(Character, temp_Clothing_types[0], instant = instant, final = False) from _call_undress_8
                
                $ Character.Clothes[temp_Clothing_types[0]] = null_Clothing
        
                if not instant:
                    call set_Outfit_flags(Character) from _call_set_Outfit_flags_18

                    $ renpy.pause(0.15, hard = True)

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_34

    return

label fix_clothing(Character, instant = False, final = True):
    $ renpy.dynamic(temp_Clothing_types = removable_Clothing_types[:])

    while temp_Clothing_types:
        if Character.Clothes[temp_Clothing_types[0]].string and Character.Clothes[temp_Clothing_types[0]].state > 0:
            call put_on(Character, temp_Clothing_types[0], instant = instant, final = False) from _call_put_on_4

        $ temp_Clothing_types.remove(temp_Clothing_types[0])

    if final:
        call set_Outfit_flags(Character) from _call_set_Outfit_flags_35

    return

label change_Outfit(Character, Outfit, instant = False):
    $ Character.Outfit = Outfit

    $ Items_to_remove, Items_to_add = get_changed_Items(Character, Character.Outfit)

    $ renpy.dynamic(temp_Clothes = Items_to_remove[:])

    while temp_Clothes:
        call take_off(Character, temp_Clothes[0].Clothing_type, redress = False, instant = instant, final = False) from _call_take_off_9

        $ temp_Clothes.remove(temp_Clothes[0])

    $ renpy.dynamic(temp_Clothes = Items_to_add[:])

    while temp_Clothes:
        call try_on(Character, temp_Clothes[0], redress = False, instant = instant, final = False) from _call_try_on_11

        $ temp_Clothes.remove(temp_Clothes[0])

    if not instant:
        $ renpy.dynamic(temp_Clothes = removable_Clothing_types[:])

        while temp_Clothes:
            if Character.Outfit.Clothes[temp_Clothes[0]].string:
                if not Character.Clothes[temp_Clothes[0]].string:
                    $ temp = Character.Outfit.Clothes[temp_Clothes[0]].selected_state
                    $ Character.Outfit.Clothes[temp_Clothes[0]].state = Character.Outfit.Clothes[temp_Clothes[0]].undressed_states[Character.position]
                    $ Character.Clothes[temp_Clothes[0]] = copy.copy(Character.Outfit.Clothes[temp_Clothes[0]])
                    $ Character.Outfit.Clothes[temp_Clothes[0]].state = temp
        
                    call set_Outfit_flags(Character) from _call_set_Outfit_flags_19
                    
                    $ renpy.pause(0.15, hard = True)

                    call put_on(Character, temp_Clothes[0], instant = False, final = False) from _call_put_on_5

            $ temp_Clothes.remove(temp_Clothes[0])
                    
    python:
        for C in Character.Outfit.Clothes.keys():
            Character.Clothes[C] = copy.copy(Character.Outfit.Clothes[C])

    call set_Outfit_flags(Character) from _call_set_Outfit_flags_20

    return