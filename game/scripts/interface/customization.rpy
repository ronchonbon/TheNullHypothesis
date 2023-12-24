default current_customization_tab = "body"

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

    timer 0.5 repeat True action ToggleVariable("blinking")

    if not black_screen:
        add "images/interface/Player_customization/background.webp" zoom interface_new_adjustment

        add At(At("images/interface/preferences/spin.webp", interface), spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502)

        if scholarship:
            imagebutton:
                idle At("images/interface/Player_customization/athletics_idle.webp", interface) 
                hover At("images/interface/Player_customization/athletics.webp", interface)

                action SetVariable("Player.scholarship", "athletic")

            imagebutton:
                idle At("images/interface/Player_customization/academics_idle.webp", interface) 
                hover At("images/interface/Player_customization/academics.webp", interface) 

                action SetVariable("Player.scholarship", "academic")

            imagebutton:
                idle At("images/interface/Player_customization/arts_idle.webp", interface) 
                hover At("images/interface/Player_customization/arts.webp", interface) 

                action SetVariable("Player.scholarship", "artistic")

            text "You are attending college on a scholarship: what is it for?" anchor (0.5, 0.5) pos (0.198, 0.375) xmaximum 400:
                font "agency_fb.ttf"

                size 40

        if blinking:
            text "PREVIEW" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.367, 0.337):
                size 35
        else:
            text "PREVIEW" + "_" anchor (0.0, 0.5) pos (0.367, 0.337):
                size 35

        add At("Player_portrait", customization_portrait) pos (0.431, 0.635)
            
        if Player.scholarship == "athletic":
            add "images/interface/Player_customization/athletics_selected.webp" zoom interface_new_adjustment
            add "images/interface/Player_customization/athletics_icon.webp" zoom interface_new_adjustment

            text "ATHLETICS" anchor (0.5, 0.5) pos (0.455, 0.432):
                font "agency_fb.ttf"

                size 35
        elif Player.scholarship == "academic":
            add "images/interface/Player_customization/academics_selected.webp" zoom interface_new_adjustment
            add "images/interface/Player_customization/academics_icon.webp" zoom interface_new_adjustment

            text "ACADEMICS" anchor (0.5, 0.5) pos (0.455, 0.432):
                font "agency_fb.ttf"

                size 35
        elif Player.scholarship == "artistic":
            add "images/interface/Player_customization/arts_selected.webp" zoom interface_new_adjustment
            add "images/interface/Player_customization/arts_icon.webp" zoom interface_new_adjustment

            text "ARTS" anchor (0.5, 0.5) pos (0.455, 0.432):
                font "agency_fb.ttf"

                size 35

        text "ATHLETICS" anchor (0.5, 0.5) pos (0.198, 0.517):
            size 40

        text "ACADEMICS" anchor (0.5, 0.5) pos (0.198, 0.623):
            size 40

        text "ARTS" anchor (0.5, 0.5) pos (0.198, 0.728):
            size 40

        vbox anchor (0.5, 0.5) pos (0.73, 0.59):
            spacing 50
                
            if current_customization_tab == "body":
                fixed xysize (0.195, 0.01):
                    text "SKIN COLOR":
                        size 35

                hbox ysize 0.06:
                    spacing 15

                    for color in ["black", "blue", "green", "red", "white"]:
                        imagebutton:
                            idle At(f"images/interface/Player_customization/skin_{color}.webp", interface)
                            hover At(f"images/interface/Player_customization/skin_{color}.webp", interface)

                            selected_foreground At("images/interface/Player_customization/selector.webp", interface)

                            selected Player.skin_color == color

                            action SetVariable("Player.skin_color", color)

                null height 0.1

                fixed xysize (0.195, 0.01):
                    text "EARS":
                        size 35

                fixed xysize (0.195, 0.06):
                    imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                        idle At("images/interface/Player_customization/left_idle.webp", interface)
                        hover At("images/interface/Player_customization/left.webp", interface)

                        if Player.ears == "human":
                            action SetVariable("Player.ears", "fin")
                        elif Player.ears == "fin":
                            action SetVariable("Player.ears", "elf")
                        elif Player.ears == "elf":
                            action SetVariable("Player.ears", "human")

                    text Player.ears.upper():
                        size 32

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                        idle At("images/interface/Player_customization/right_idle.webp", interface)
                        hover At("images/interface/Player_customization/right.webp", interface)

                        if Player.ears == "human":
                            action SetVariable("Player.ears", "elf")
                        elif Player.ears == "elf":
                            action SetVariable("Player.ears", "fin")
                        elif Player.ears == "fin":
                            action SetVariable("Player.ears", "human")
            elif current_customization_tab == "hair":
                fixed xysize (0.195, 0.01):
                    text "HAIR":
                        size 35

                fixed xysize (0.195, 0.06):
                    imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                        idle At("images/interface/Player_customization/left_idle.webp", interface)
                        hover At("images/interface/Player_customization/left.webp", interface)

                        action SetVariable("Player.hair", (Player.hair - 1) % 7)

                    text f"TYPE {Player.hair}":
                        size 32

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                        idle At("images/interface/Player_customization/right_idle.webp", interface) 
                        hover At("images/interface/Player_customization/right.webp", interface)

                        action SetVariable("Player.hair", (Player.hair + 1) % 7)
                
                if Player.beards_unlocked:
                    null height 0.0333

                    fixed xysize (0.195, 0.01):
                        text "BEARD":
                            size 35

                    fixed xysize (0.195, 0.06):
                        imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                            idle At("images/interface/Player_customization/left_idle.webp", interface)
                            hover At("images/interface/Player_customization/left.webp", interface)

                            action SetVariable("Player.beard", (Player.beard - 1) % 3)

                        text f"TYPE {Player.beard}":
                            size 32

                        imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                            idle At("images/interface/Player_customization/right_idle.webp", interface) 
                            hover At("images/interface/Player_customization/right.webp", interface)

                            action SetVariable("Player.beard", (Player.beard + 1) % 3)

                    null height 0.0333
                else:
                    null height 0.1

                fixed xysize (0.195, 0.01):
                    text "HAIR COLOR":
                        size 35

                hbox ysize 0.6:
                    spacing 15

                    for color in ["black", "blond", "blue", "brown", "green", "red"]:
                        imagebutton:
                            idle At(f"images/interface/Player_customization/hair_{color}.webp", interface)
                            hover At(f"images/interface/Player_customization/hair_{color}.webp", interface)

                            selected_foreground At("images/interface/Player_customization/selector.webp", interface)

                            selected Player.hair_color == color

                            action SetVariable("Player.hair_color", color)
            elif current_customization_tab == "outfit":
                fixed xysize (0.195, 0.01):
                    text "CLOTHING":
                        size 35

                if len(Player.Outfits) > 0:
                    $ list_size = len(Player.Outfits)
                else:
                    $ list_size = 1

                fixed xysize (0.195, 0.06):
                    imagebutton anchor (0.0, 0.5) pos (0.0, 0.5):
                        idle At("images/interface/Player_customization/left_idle.webp", interface)
                        hover At("images/interface/Player_customization/left.webp", interface)

                        action [
                            SetVariable("Player.Outfit_index", (Player.Outfit_index - 1) % list_size),
                            SetVariable("Player.Outfit", Player.Outfits[(Player.Outfit_index - 1) % list_size])]

                    text Player.Outfits[Player.Outfit_index].name.upper() xmaximum int(180*interface_new_sampling):
                        size 32

                    imagebutton anchor (1.0, 0.5) pos (1.0, 0.5):
                        idle At("images/interface/Player_customization/right_idle.webp", interface) 
                        hover At("images/interface/Player_customization/right.webp", interface)

                        action [
                            SetVariable("Player.Outfit_index", (Player.Outfit_index + 1) % list_size),
                            SetVariable("Player.Outfit", Player.Outfits[(Player.Outfit_index + 1) % list_size])]

                null height 0.1
                
                fixed xysize (0.195, 0.01):
                    text "BACKGROUND COLOR":
                        size 35

                hbox ysize 0.06:
                    spacing 15

                    for background_color in ["purple", "blue", "green", "grey", "orange", "red"]:
                        imagebutton:
                            idle At(f"images/interface/Player_customization/background_{background_color}.webp", interface)
                            hover At(f"images/interface/Player_customization/background_{background_color}.webp", interface)

                            selected_foreground At("images/interface/Player_customization/selector.webp", interface)

                            selected Player.background_color == background_color

                            action SetVariable("Player.background_color", background_color)

        if scholarship:
            text "Scholarships yield different dialogue options. NPCs may comment on your appearance. Save after customization to continue." anchor (0.0, 0.5) pos (0.065, 0.859):
                font "agency_fb.ttf"

                size 28
                
        imagebutton:
            idle At("images/interface/Player_customization/body_idle.webp", interface)
            hover At("images/interface/Player_customization/body.webp", interface)
            selected_idle At("images/interface/Player_customization/body.webp", interface)
            selected_hover At("images/interface/Player_customization/body.webp", interface)

            selected current_customization_tab == "body"

            action SetVariable("current_customization_tab", "body")
                
        imagebutton:
            idle At("images/interface/Player_customization/hair_idle.webp", interface)
            hover At("images/interface/Player_customization/hair.webp", interface)
            selected_idle At("images/interface/Player_customization/hair.webp", interface)
            selected_hover At("images/interface/Player_customization/hair.webp", interface)

            selected current_customization_tab == "hair"

            action SetVariable("current_customization_tab", "hair")
                
        imagebutton:
            idle At("images/interface/Player_customization/outfit_idle.webp", interface)
            hover At("images/interface/Player_customization/outfit.webp", interface)
            selected_idle At("images/interface/Player_customization/outfit.webp", interface)
            selected_hover At("images/interface/Player_customization/outfit.webp", interface)

            selected current_customization_tab == "outfit"

            action SetVariable("current_customization_tab", "outfit")

        text "BODY" anchor (0.5, 0.5) pos (0.729, 0.3395):
            size 40

        text "HAIR" anchor (0.5, 0.5) pos (0.813, 0.3395):
            size 40

        text "OUTFIT" anchor (0.5, 0.5) pos (0.896, 0.3395):
            size 40
                
        imagebutton:
            idle At("images/interface/Player_customization/save_idle.webp", interface)
            hover At("images/interface/Player_customization/save.webp", interface)

            if Player.scholarship:
                action Return()
            else:
                action None

        text "SAVE AND CONTINUE" anchor (0.5, 0.5) pos (0.821, 0.857):
            size 40
            
    use quick_menu