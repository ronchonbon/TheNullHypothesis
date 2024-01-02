init -1:

    default Kurt = create_Kurt()
    
    define Kurt_color = "#183b82"
    define ch_Kurt = Character("[Kurt.tag]")

init -2 python:

    def create_Kurt():
        Kurt = NPCClass("Kurt", voice = ch_Kurt)

        Kurt.full_name = "Kurt Wagner"
        Kurt.call_sign = "Nightcrawler"

        Kurt.database_type = "ally"

        Kurt.chat_options.append("Can you tell me anything about. . . ?")
        Kurt.chat_options.append("Any tips regarding. . . ?")
        Kurt.text_options.append("what the heck is a 'BAMF taxi'?")
        Kurt.text_options.append("got any tips about this damn phone?")

        Kurt.hair = "quiff"
        Kurt.outfit = "casual"

        Cast.append(Kurt.tag)
        Sprites.append(Kurt)

        all_Characters.append(Kurt)
        all_NPCs.append(Kurt)
        Students.append(Kurt)

        bedrooms.append(Kurt.home)

        return Kurt

    def Kurt_faces(face):
        blush = 0

        if face == "neutral":
            brows = "neutral"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry1":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry2":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "happy"
        elif face == "appalled1":
            brows = "furrowed"
            eyes = "wide"
            mouth = "neutral"
        elif face == "appalled2":
            brows = "furrowed"
            eyes = "wide"
            mouth = "open"
        elif face == "appalled3":
            brows = "furrowed"
            eyes = "wide"
            mouth = "agape"
        elif face == "confused1":
            brows = "cocked"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "confused2":
            brows = "cocked"
            eyes = "wide"
            mouth = "neutral"
        elif face == "confused3":
            brows = "cocked"
            eyes = "wide"
            mouth = "agape"
        elif face == "devious":
            brows = "neutral"
            eyes = "squint"
            mouth = "smile"
        elif face == "furious":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "frown"
        elif face == "grimace":
            brows = "furrowed"
            eyes = "closed"
            mouth = "lipbite"
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
        elif face == "kiss1":
            brows = "worried"
            eyes = "closed"
            mouth = "kiss"
        elif face == "kiss2":
            brows = "neutral"
            eyes = "closed"
            mouth = "kiss"
        elif face == "manic":
            brows = "worried"
            eyes = "wide"
            mouth = "smile"
            blush = 1
        elif face == "perplexed":
            brows = "cocked"
            eyes = "wide"
            mouth = "open"
        elif face == "pleased1":
            brows = "raised"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "pleased2":
            brows = "raised"
            eyes = "wide"
            mouth = "smirk"
        elif face == "sad":
            brows = "worried"
            eyes = "neutral"
            mouth = "frown"
        elif face == "sexy":
            brows = "neutral"
            eyes = "sexy"
            mouth = "lipbite"
        elif face == "sly":
            brows = "neutral"
            eyes = "squint"
            mouth = "smirk"
        elif face == "smirk1":
            brows = "neutral"
            eyes = "neutral"
            mouth = "happy"
        elif face == "smirk2":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "surprised1":
            brows = "raised"
            eyes = "neutral"
            mouth = "open"
        elif face == "surprised2":
            brows = "raised"
            eyes = "wide"
            mouth = "open"
        elif face == "surprised3":
            brows = "raised"
            eyes = "wide"
            mouth = "agape"
        elif face == "suspicious1":
            brows = "furrowed"
            eyes = "squint"
            mouth = "neutral"
        elif face == "suspicious2":
            brows = "furrowed"
            eyes = "squint"
            mouth = "frown"
        elif face == "wink":
            brows = "wink"
            eyes = "wink"
            mouth = "kiss"
        elif face == "worried1":
            brows = "worried"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "worried2":
            brows = "worried"
            eyes = "wide"
            mouth = "neutral"
        elif face == "worried3":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
        elif face == "worried4":
            brows = "worried"
            eyes = "wide"
            mouth = "agape"
        else:
            return "wrong", "wrong", "wrong", 0

        return brows, eyes, mouth, blush

    def Kurt_arms(pose):
        if pose == "neutral":
            left_arm = "neutral"
            right_arm = "neutral"
        elif pose == "angry":
            left_arm = "fist"
            right_arm = "fist"
        elif pose == "crossed":
            left_arm = "crossed"
            right_arm = "crossed"
        elif pose == "fight":
            left_arm = "fight"
            right_arm = "fight"
        elif pose == "shrug":
            left_arm = "extended"
            right_arm = "extended"
        elif pose == "sheepish":
            left_arm = "rub_neck"
            right_arm = "question"
        else:
            return "wrong", "wrong"

        return left_arm, right_arm

    def Kurt_locations():
        possible_locations = []

        possible_locations.append(Kurt.home)

        if time_index < 2 and weekday < 5:
            possible_locations.append("bg_classroom")
            possible_locations.append("bg_classroom")
                
        if time_index < 3 and weather != "rain":
            possible_locations.append("bg_campus")

        if time_index < 3:
            possible_locations.append("bg_danger")

        if time_index < 3:
            if time_index == 2:
                if temperature[time_index] > 22 and not weather and snow_left == 0:
                    possible_locations.append("bg_pool")

                possible_locations.append("bg_mall")
            elif weekday > 4:
                if temperature[time_index] > 22 and not weather and snow_left == 0:
                    possible_locations.append("bg_pool")

                possible_locations.append("bg_mall")

        return possible_locations

label update_Kurt:
    $ Kurt.full_name = "Kurt Wagner"
    $ Kurt.call_sign = "Nightcrawler"

    $ Kurt.database_type = "ally"
    
    $ Kurt.sprite_anchor = Kurt_standing_anchor
    $ Kurt.sprite_position[1] = Kurt_standing_height
    $ Kurt.sprite_zoom = Kurt_standing_zoom

    return

label Kurt_teleports_in(dialogue = None, x = None, y = None, add = True):
    $ temp_dialogue_hidden = dialogue_hidden
    $ temp_phone_interactable = phone_interactable
    $ temp_choice_disabled = choice_disabled
    $ temp_Character_picker_disabled = Character_picker_disabled
    $ temp_belt_disabled = belt_disabled

    $ dialogue_hidden = False
    $ phone_interactable = False
    $ choice_disabled = False
    $ Character_picker_disabled = True
    $ belt_disabled = True

    $ Kurt.give_trait("smoke")
    $ Kurt.give_trait("teleporting_in")

    show expression "images/effects/bamf.webp" as bamf onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    if not x:
        $ x = stage_center

    if not y:
        $ y = Kurt_standing_height

    call show_Character(Kurt, x = x, y = y, fade = False) from _call_show_Character

    $ Kurt.remove_trait("smoke")

    if dialogue:
        ch_Kurt "[dialogue]" with small_screenshake
    else:
        $ renpy.pause(3.0, hard = True)
    
    $ Kurt.remove_trait("teleporting_in")

    hide bamf onlayer effects

    if add:
        call add_Characters(Kurt, fade = False) from _call_add_Characters_14

    $ Kurt.History.update("teleported_in")

    $ dialogue_hidden = temp_dialogue_hidden
    $ phone_interactable = temp_phone_interactable
    $ choice_disabled = temp_choice_disabled
    $ Character_picker_disabled = temp_Character_picker_disabled
    $ belt_disabled = temp_belt_disabled

    return

label Kurt_teleports_out:
    $ temp_dialogue_hidden = dialogue_hidden
    $ temp_phone_interactable = phone_interactable
    $ temp_choice_disabled = choice_disabled
    $ temp_Character_picker_disabled = Character_picker_disabled
    $ temp_belt_disabled = belt_disabled

    $ dialogue_hidden = False
    $ phone_interactable = False
    $ choice_disabled = False
    $ Character_picker_disabled = True
    $ belt_disabled = True
    
    $ Kurt.give_trait("teleporting_out")

    show expression "images/effects/bamf.webp" as bamf onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    $ Kurt.give_trait("smoke")

    $ renpy.pause(0.1, hard = True)
    
    $ Kurt.remove_trait("smoke")

    $ renpy.pause(3.0, hard = True)

    hide bamf onlayer effects

    call remove_Characters(Kurt, fade = False) from _call_remove_Characters_65

    $ Kurt.remove_trait("teleporting_out")

    $ dialogue_hidden = temp_dialogue_hidden
    $ phone_interactable = temp_phone_interactable
    $ choice_disabled = temp_choice_disabled
    $ Character_picker_disabled = temp_Character_picker_disabled
    $ belt_disabled = temp_belt_disabled

    return