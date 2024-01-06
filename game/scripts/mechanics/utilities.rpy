init python:
     
    def get_Present(location = None, selected_Character = None, traveling = False, include_Party = True):
        temp_Present = Party[:] if Party and include_Party else []
        temp_left_Slot = left_Slot if left_Slot else None
        temp_middle_Slot = middle_Slot if middle_Slot else None
        temp_right_Slot = right_Slot if right_Slot else None
        temp_Offscreen = Offscreen[:] + Background[:] if (Offscreen or Background) else []

        location = Player.location if not location else location

        for C in all_Characters:
            if C not in Party:
                if C not in temp_Present and C.location == location:
                    temp_Present.append(C)

        temp_Characters = temp_Present[:]
        
        # if location == Player.location:
        #     for C in temp_Offscreen:
        #         if C in temp_Characters:
        #             temp_Characters.remove(C)

        for C in temp_Present:
            if C in temp_Characters:
                if C.behavior == "teaching" and C.location == "bg_classroom":
                    temp_Characters.remove(C)
        
        if temp_left_Slot not in temp_Characters:
            temp_left_Slot = None

        if temp_middle_Slot not in temp_Characters:
            temp_middle_Slot = None

        if temp_right_Slot not in temp_Characters:
            temp_right_Slot = None

        sorted_Characters = sort_Characters_by_approval(temp_Characters[:])

        for C in temp_Offscreen:
            if C in sorted_Characters:
                sorted_Characters.remove(C)

        if traveling:
            if sorted_Characters:
                temp_middle_Slot = sorted_Characters[0]

            if len(sorted_Characters) >= 2:
                temp_left_Slot = sorted_Characters[1]

            if len(sorted_Characters) >= 3:
                temp_right_Slot = sorted_Characters[2]
        elif selected_Character:
            if temp_left_Slot == selected_Character:
                temp_left_Slot, temp_middle_Slot = temp_middle_Slot, selected_Character
            elif temp_middle_Slot == selected_Character:
                pass
            elif temp_right_Slot == selected_Character:
                temp_middle_Slot, temp_right_Slot = selected_Character, temp_middle_Slot
            else:
                if temp_left_Slot and temp_middle_Slot and temp_right_Slot:
                    temp_left_Slot, temp_middle_Slot = temp_middle_Slot, selected_Character
                elif not temp_middle_Slot:
                    temp_middle_Slot = selected_Character
                elif not temp_left_Slot:
                    temp_left_Slot, temp_middle_Slot = temp_middle_Slot, selected_Character
                elif not temp_right_Slot:
                    temp_middle_Slot, temp_right_Slot = selected_Character, temp_middle_Slot

        if not ongoing_Event and sandbox:
            if not temp_middle_Slot:
                if temp_left_Slot:
                    temp_left_Slot, temp_middle_Slot = None, temp_left_Slot
                elif right_Slot:
                    temp_middle_Slot, temp_right_Slot = temp_right_Slot, None

        if location == Player.location:            
            for C in all_Characters:
                if C in temp_Offscreen and C.location != location:
                    temp_Offscreen.remove(C)
                        
            for C in temp_Present:
                if C not in temp_Offscreen:
                    if C not in [temp_left_Slot, temp_middle_Slot, temp_right_Slot]:
                        temp_Offscreen.append(C)
                elif C in temp_Offscreen:
                    if C in [temp_left_Slot, temp_middle_Slot, temp_right_Slot]:
                        temp_Offscreen.remove(C)

            if location in location_Slots.keys():
                for S in location_Slots[location].values():
                    already_somewhere = False
                    occupied = False

                    temp_Characters = temp_Offscreen[:]

                    for C in temp_Characters:
                        if C in Background:
                            for S_alt in location_Slots[location].values():
                                if S != S_alt and S_alt["position"] == C.sprite_position:
                                    already_somewhere = True

                                    temp_Offscreen.remove(C)

                                    break

                        for C_alt in temp_Present:
                            if C != C_alt and S["position"] == C_alt.sprite_position:
                                occupied = True

                                break

                        if not already_somewhere and not occupied:
                            if not S["behavior"] or C.behavior == S["behavior"]:
                                C.sprite_position = S["position"]

                                temp_Offscreen.remove(C)
                
        return temp_Present, temp_left_Slot, temp_middle_Slot, temp_right_Slot, temp_Offscreen

label approach_Characters:
    $ renpy.dynamic(temp_Characters = sort_Characters_by_approval(Background + Offscreen))

    menu:
        "Approach. . ."
        "[temp_Characters[0].name]" if temp_Characters and temp_Characters[0].behavior != "teaching":
            $ new_Characters = [temp_Characters[0]]
        "[temp_Characters[1].name]" if len(temp_Characters) >= 2 and temp_Characters[1].behavior != "teaching":
            $ new_Characters = [temp_Characters[1]]
        "[temp_Characters[2].name]" if len(temp_Characters) >= 3 and temp_Characters[2].behavior != "teaching":
            $ new_Characters = [temp_Characters[2]]
        "[temp_Characters[3].name]" if len(temp_Characters) >= 4 and temp_Characters[3].behavior != "teaching":
            $ new_Characters = [temp_Characters[3]]
        "[temp_Characters[4].name]" if len(temp_Characters) >= 5 and temp_Characters[4].behavior != "teaching":
            $ new_Characters = [temp_Characters[4]]
        "[temp_Characters[5].name]" if len(temp_Characters) >= 6 and temp_Characters[5].behavior != "teaching":
            $ new_Characters = [temp_Characters[5]]
        "[temp_Characters[6].name]" if len(temp_Characters) >= 7 and temp_Characters[6].behavior != "teaching":
            $ new_Characters = [temp_Characters[6]]
        "[temp_Characters[7].name]" if len(temp_Characters) >= 8 and temp_Characters[7].behavior != "teaching":
            $ new_Characters = [temp_Characters[7]]
        "Back":
            return

    call set_the_scene(greetings = True, fade = False, selected_Character = new_Characters[0]) from _call_set_the_scene_404

    return

label reset_all_interfaces:
    call stop_all_Actions(automatic = True) from _call_stop_all_Actions_6
    call closing_Action_interface from _call_closing_Action_interface_6

    hide screen Wardrobe_screen
    hide screen phone_screen
    hide screen interactions_screen
    show screen belt_screen()

    $ current_phone_screen = "home"

    if current_phone_Character:
        $ current_phone_Character.remove_trait("electronic")

        $ current_phone_Character = None

    $ ongoing_Event = False
    $ phone_interactable = True
    $ choice_disabled = False
    $ Character_picker_active = True
    $ Character_picker_disabled = False
    $ belt_hidden = False
    $ belt_disabled = False

    return