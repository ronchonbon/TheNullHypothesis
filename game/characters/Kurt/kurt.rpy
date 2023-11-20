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