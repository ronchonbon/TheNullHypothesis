init -1:

    default Kurt = create_Kurt()
    
    define Kurt_color = "#183b82"
    define ch_Kurt = Character("[Kurt.tag]")

    define Kurt_standing_anchor = [int(1250*character_sampling), int(1250*character_sampling)]
    define Kurt_standing_height = 0.23
    define Kurt_standing_zoom = 0.35*character_adjustment

init -2 python:

    def create_Kurt():
        Kurt = NPCClass("Kurt", voice = ch_Kurt)

        Kurt.full_name = "Kurt Wagner"
        Kurt.call_sign = "Nightcrawler"

        Kurt.chat_options.append("Can you tell me anything about. . . ?")
        Kurt.chat_options.append("Any tips regarding. . . ?")
        Kurt.text_options.append("what the heck is a 'BAMF taxi'?")
        Kurt.text_options.append("got any tips about this damn phone?")

        Kurt.outfit = "casual"

        Kurt.shadow = False
        Kurt.smoke = False
        Kurt.teleporting_in = False
        Kurt.teleporting_out = False
        Kurt.tail_hidden = False

        Cast.append(Kurt.tag)
        Sprites.append(Kurt)

        all_Characters.append(Kurt)
        all_NPCs.append(Kurt)
        Students.append(Kurt)

        bedrooms.append(Kurt.home)

        return Kurt

    def Kurt_faces(face):
        if face == "neutral":
            mouth = "neutral"
            brows = "neutral"
            eyes = "neutral"
        elif face == "angry":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "frown"
        elif face == "confused":
            brows = "furrowed"
            eyes = "squint"
            mouth = "neutral"
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
        elif face == "sad":
            brows = "neutral"
            eyes = "neutral"
            mouth = "frown"
        elif face == "stunned":
            brows = "neutral"
            eyes = "up"
            mouth = "neutral"
        elif face == "surprised":
            brows = "raised"
            eyes = "wide"
            mouth = "neutral"
        else:
            renpy.say(None, "Something went wrong with a face here.")

            return "neutral", "neutral", "neutral"

        return brows, eyes, mouth

    def Kurt_arms(pose):
        return "neutral", "neutral"

    def Kurt_locations():
        global weekday
        global time_index

        global weather
        global snow_left
        
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

    $ Kurt.smoke = True
    $ Kurt.teleporting_in = True

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

    call show_Character(Kurt, x = x, y = y, sprite_layer = 6, fade = False) from _call_show_Character

    $ Kurt.smoke = False

    if dialogue:
        ch_Kurt "[dialogue]" with small_screenshake
    else:
        $ renpy.pause(3.0, hard = True)
    
    $ Kurt.teleporting_in = False

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
    
    $ Kurt.teleporting_out = True

    show expression "images/effects/bamf.webp" as bamf onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    $ Kurt.smoke = True

    $ renpy.pause(0.1, hard = True)
    
    $ Kurt.smoke = False

    $ renpy.pause(3.0, hard = True)

    hide bamf onlayer effects

    call remove_Characters(Kurt, fade = False) from _call_remove_Characters_65

    $ Kurt.teleporting_out = False

    $ dialogue_hidden = temp_dialogue_hidden
    $ phone_interactable = temp_phone_interactable
    $ choice_disabled = temp_choice_disabled
    $ Character_picker_disabled = temp_Character_picker_disabled
    $ belt_disabled = temp_belt_disabled

    return