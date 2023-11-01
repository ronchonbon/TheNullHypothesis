default current_customization_tab = "body"

image Player_customization_selector:
    "images/interface/Player_customization/selector.webp" 
    
    anchor (0.5, 0.5)
    pos (0.5, 0.4)

layeredimage Player_portrait:
    always:
        "images/interface/Player_portrait/background_[Player.background_color].webp"

    always:
        "images/interface/Player_portrait/body_[Player.skin_color].webp"

    if Player.Outfit:
        "images/interface/Player_portrait/clothes_[Player.Outfit.string].webp"

    always:
        "images/interface/Player_portrait/head_[Player.skin_color].webp"

    if Player.hair:
        "images/interface/Player_portrait/hair_[Player.hair]_[Player.hair_color].webp"

    always:
        "images/interface/Player_portrait/ears_[Player.ears]_[Player.skin_color].webp"

    if Player.beard:
        "images/interface/Player_portrait/beard_[Player.beard]_[Player.hair_color].webp"

    anchor (0.5, 0.5)

style Player_customization is default

style Player_customization_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

style Player_customization_image_button:
    # hover_sound "sounds/interface/hover.ogg"
    activate_sound "sounds/interface/press.ogg"

screen Player_customization_screen(scholarship = False):
    layer "interface"

    style_prefix "Player_customization"
    
    on "show" action [
        SetVariable("choice_disabled", True),
        SetVariable("say_obscured", True),
        SetVariable("Character_picker_disabled", True)]
    on "hide" action [
        SetVariable("choice_disabled", False),
        SetVariable("say_obscured", False),
        SetVariable("Character_picker_disabled", False)]

    if not black_screen:
        add "images/interface/Player_customization/background.webp" align (0.5, 0.5)

        add "images/interface/Player_customization/athletics.webp" align (0.5, 0.5)
        add "images/interface/Player_customization/academics.webp" align (0.5, 0.5)
        add "images/interface/Player_customization/art.webp" align (0.5, 0.5)

        if scholarship:
            imagebutton:
                idle At("images/interface/Player_customization/athletics.webp", almost_invisible) hover "images/interface/Player_customization/athletics_selected.webp"

                action SetVariable("Player.scholarship", "athletic")

                focus_mask True

            imagebutton:
                idle At("images/interface/Player_customization/academics.webp", almost_invisible) hover "images/interface/Player_customization/academics_selected.webp"

                action SetVariable("Player.scholarship", "academic")

                focus_mask True

            imagebutton:
                idle At("images/interface/Player_customization/art.webp", almost_invisible) hover "images/interface/Player_customization/art_selected.webp"

                action SetVariable("Player.scholarship", "artistic")

                focus_mask True

            text "You attended college on a scholarship: what was it for?" anchor (0.5, 0.5) pos (0.139, 0.325) xmaximum 400:
                size 36

                color "#512908"

        text "Character Portrait" anchor (0.5, 0.5) pos (0.425, 0.309):
            size 40

            color "#000000"

        add At("Player_portrait", customization_portrait) pos (0.425, 0.522)
            
        if Player.scholarship == "athletic":
            add "images/interface/Player_customization/athletics_selected.webp" align (0.5, 0.5)
            add "images/interface/Player_customization/baseball.webp" align (0.5, 0.5)
        elif Player.scholarship == "academic":
            add "images/interface/Player_customization/academics_selected.webp" align (0.5, 0.5)
            add "images/interface/Player_customization/book.webp" align (0.5, 0.5)     
        elif Player.scholarship == "artistic":
            add "images/interface/Player_customization/art_selected.webp" align (0.5, 0.5)
            add "images/interface/Player_customization/brush.webp" align (0.5, 0.5)

        text "ATHLETICS" anchor (0.5, 0.5) pos (0.139, 0.423):
            size 40

            color "#ffffff"

        text "ACADEMICS" anchor (0.5, 0.5) pos (0.139, 0.53):
            size 40

            color "#ffffff"

        text "ART" anchor (0.5, 0.5) pos (0.139, 0.637):
            size 40

            color "#ffffff"

        vbox anchor (0.5, 0.5) pos (0.664, 0.486):
            spacing 50
                
            if current_customization_tab == "body":
                fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                    add "images/interface/Player_customization/title.webp" align (0.5, 0.5)
                    
                    text "Skin Color" align (0.5, 0.5) size 36

                hbox ysize int(64*2*interface_sampling) align (0.5, 0.5):
                    spacing 15

                    for color in ["black", "blue", "green", "red", "white"]:
                        imagebutton:
                            selected_background "Player_customization_selector"

                            selected Player.skin_color == color

                            idle f"images/interface/Player_customization/skin_{color}.webp" hover f"images/interface/Player_customization/skin_{color}.webp"

                            action SetVariable("Player.skin_color", color)

                fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                    add "images/interface/Player_customization/title.webp" align (0.5, 0.5)

                    text "Ears" align (0.5, 0.5) size 36

                fixed xalign 0.5 xysize (int(375*2*interface_sampling), int(64*2*interface_sampling)):
                    imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                        idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                        if Player.ears == "human":
                            action SetVariable("Player.ears", "fin")
                        elif Player.ears == "fin":
                            action SetVariable("Player.ears", "elf")
                        elif Player.ears == "elf":
                            action SetVariable("Player.ears", "human")

                    text Player.ears.upper() align (0.5, 0.5):
                        size 32

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                        idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                        if Player.ears == "human":
                            action SetVariable("Player.ears", "elf")
                        elif Player.ears == "elf":
                            action SetVariable("Player.ears", "fin")
                        elif Player.ears == "fin":
                            action SetVariable("Player.ears", "human")
            elif current_customization_tab == "hair":
                fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                    add "images/interface/Player_customization/title.webp" align (0.5, 0.5)

                    text "Hair" align (0.5, 0.5) size 36

                fixed xalign 0.5 xysize (int(375*2*interface_sampling), int(64*2*interface_sampling)):
                    imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                        idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                        action SetVariable("Player.hair", (Player.hair - 1) % 7)

                    text f"TYPE {Player.hair}" align (0.5, 0.5):
                        size 32

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                        idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                        action SetVariable("Player.hair", (Player.hair + 1) % 7)
                
                if Player.beards_unlocked:
                    fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                        add "images/interface/Player_customization/title.webp" align (0.5, 0.5)

                        text "Beard" align (0.5, 0.5) size 36

                    fixed xalign 0.5 xysize (int(375*2*interface_sampling), int(64*2*interface_sampling)):
                        imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                            idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                            action SetVariable("Player.beard", (Player.beard - 1) % 3)

                        text f"TYPE {Player.beard}" align (0.5, 0.5):
                            size 32

                        imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                            idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                            action SetVariable("Player.beard", (Player.beard + 1) % 3)

                fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                    add "images/interface/Player_customization/title.webp" align (0.5, 0.5)
                    
                    text "Hair Color" align (0.5, 0.5) size 36

                hbox ysize int(64*2*interface_sampling) align (0.5, 0.5):
                    spacing 15

                    for color in ["black", "blond", "blue", "brown", "green", "red"]:
                        imagebutton:
                            selected_background "Player_customization_selector"

                            selected Player.hair_color == color

                            idle f"images/interface/Player_customization/hair_{color}.webp" hover f"images/interface/Player_customization/hair_{color}.webp"

                            action SetVariable("Player.hair_color", color)
            elif current_customization_tab == "clothing":
                fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                    add "images/interface/Player_customization/title.webp" align (0.5, 0.5)

                    text "Clothing" align (0.5, 0.5) size 36

                if len(Player.Outfits) > 0:
                    $ list_size = len(Player.Outfits)
                else:
                    $ list_size = 1

                fixed xalign 0.5 xysize (int(375*2*interface_sampling), int(64*2*interface_sampling)):
                    imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                        idle "images/interface/Player_customization/left_idle.webp" hover "images/interface/Player_customization/left.webp"

                        action [
                            SetVariable("Player.Outfit_index", (Player.Outfit_index - 1) % list_size),
                            SetVariable("Player.Outfit", Player.Outfits[(Player.Outfit_index - 1) % list_size])]

                    text Player.Outfits[Player.Outfit_index].name.upper() align (0.5, 0.5) xmaximum int(180*2*interface_sampling):
                        size 32

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                        idle "images/interface/Player_customization/right_idle.webp" hover "images/interface/Player_customization/right.webp"

                        action [
                            SetVariable("Player.Outfit_index", (Player.Outfit_index + 1) % list_size),
                            SetVariable("Player.Outfit", Player.Outfits[(Player.Outfit_index + 1) % list_size])]
                
                fixed xysize (int(375*2*interface_sampling), int(57*2*interface_sampling)) xalign 0.5:
                    add "images/interface/Player_customization/title.webp" align (0.5, 0.5)

                    text "Background Color" align (0.5, 0.5) size 36

                hbox ysize int(64*2*interface_sampling) align (0.5, 0.5):
                    spacing 15

                    for background_color in ["purple", "blue", "green", "grey", "orange", "red"]:
                        imagebutton:
                            selected_background "Player_customization_selector"

                            selected Player.background_color == background_color

                            idle f"images/interface/Player_customization/background_{background_color}.webp" hover f"images/interface/Player_customization/background_{background_color}.webp"

                            action SetVariable("Player.background_color", background_color)

        if scholarship:
            text "Scholarships yield different dialogue options. NPCs may comment on your appearance. Save after customization to continue." anchor (0.0, 0.5) pos (0.05, 0.95):
                size 28

                color "#b3b3b3"
                
        imagebutton:
            idle "images/interface/Player_customization/body_idle.webp" hover "images/interface/Player_customization/body.webp" selected_idle "images/interface/Player_customization/body_selected.webp" selected_hover "images/interface/Player_customization/body_selected.webp"

            selected current_customization_tab == "body"

            action SetVariable("current_customization_tab", "body")

            focus_mask True
                
        imagebutton:
            idle "images/interface/Player_customization/hair_idle.webp" hover "images/interface/Player_customization/hair.webp" selected_idle "images/interface/Player_customization/hair_selected.webp" selected_hover "images/interface/Player_customization/hair_selected.webp"

            selected current_customization_tab == "hair"

            action SetVariable("current_customization_tab", "hair")

            focus_mask True
                
        imagebutton:
            idle "images/interface/Player_customization/clothing_idle.webp" hover "images/interface/Player_customization/clothing.webp" selected_idle "images/interface/Player_customization/clothing_selected.webp" selected_hover "images/interface/Player_customization/clothing_selected.webp"

            selected current_customization_tab == "clothing"

            action SetVariable("current_customization_tab", "clothing")

            focus_mask True
                
        imagebutton:
            idle "images/interface/Player_customization/save_idle.webp" hover "images/interface/Player_customization/save.webp"

            if Player.scholarship:
                action Return()
            else:
                action None

            focus_mask True