label give_Girl_piercing(Girl, Piercing, mall = False, discounted = False, instant = False):
    if mall:
        hide screen piercings_screen
        hide screen shop_screen

        $ Character_picker_disabled = True
        $ belt_disabled = True

    if Girl.status["miffed"] or Girl.status["mad"]:
        call expression f"{Girl.tag}_{Piercing.string}_reject" from _call_expression_261

        $ Girl.History.update(f"said_no_to_{Piercing.string}")
    elif approval_check(Girl, threshold = Piercing.threshold, extra_condition = "piercing"):
        call expression f"{Girl.tag}_{Piercing.string}_accept" from _call_expression_262

        if mall and discounted:
            $ Player.cash -= int(0.5*Piercing.price)
        elif mall:
            $ Player.cash -= Piercing.price

        if "belly" in Piercing.string:
            $ Girl.piercings["belly"] = True
        elif "nipple" in Piercing.string:
            if approval_check(Girl, threshold = "see_breasts") and (renpy.get_screen("Wardrobe_screen") or approval_check(Girl, threshold = "exhibitionism")):
                call expose(Girl, "breasts", instant = instant) from _call_expose_14

                if not instant:
                    pause 1.0
            else:
                $ fade_to_black(0.4)

                "You give [Girl.name] some privacy."

            if "barbell" in Piercing.string:
                if Girl.piercings["nipple"] == "ring":
                    $ Girl.piercings["nipple"] = "both"
                else:
                    $ Girl.piercings["nipple"] = "barbell"
            elif "ring" in Piercing.string:
                if Girl.piercings["nipple"] == "barbell":
                    $ Girl.piercings["nipple"] = "both"
                else:
                    $ Girl.piercings["nipple"] = "ring"
                    
            if approval_check(Girl, threshold = "see_breasts") and (renpy.get_screen("Wardrobe_screen") or approval_check(Girl, threshold = "exhibitionism")):
                pause 2.0

                call change_Outfit(Girl, Girl.Wardrobe.Outfits[Girl.Outfit.name], instant = instant) from _call_change_Outfit_40
            else:
                $ fade_in_from_black(0.4)
        elif "labia" in Piercing.string:
            if approval_check(Girl, threshold = "see_pussy") and (renpy.get_screen("Wardrobe_screen") or approval_check(Girl, threshold = "exhibitionism")):
                call expose(Girl, "pussy", instant = instant) from _call_expose_15

                if not instant:
                    pause 1.0
            else:
                $ fade_to_black(0.4)

                "You give [Girl.name] some privacy."

            if "barbell" in Piercing.string:
                if Girl.piercings["labia"] == "ring":
                    $ Girl.piercings["labia"] = "both"
                else:
                    $ Girl.piercings["labia"] = "barbell"
            elif "ring" in Piercing.string:
                if Girl.piercings["labia"] == "barbell":
                    $ Girl.piercings["labia"] = "both"
                else:
                    $ Girl.piercings["labia"] = "ring"
                    
            if approval_check(Girl, threshold = "see_pussy") and (renpy.get_screen("Wardrobe_screen") or approval_check(Girl, threshold = "exhibitionism")):
                pause 2.0

                call change_Outfit(Girl, Girl.Wardrobe.Outfits[Girl.Outfit.name], instant = instant) from _call_change_Outfit_41
            else:
                $ fade_in_from_black(0.4)

        if Piercing.string not in Girl.inventory.keys():
            $ Girl.inventory[Piercing.string] = Piercing

        $ Girl.History.update(f"put_in_{Piercing.string}")
    else:
        if Girl.History.check(f"said_no_to_{Piercing.string}", tracker = "recent") >= 1:
            call change_Girl_stat(Girl, "love", -5) from _call_change_Girl_stat_990
            call change_Girl_stat(Girl, "trust", -5) from _call_change_Girl_stat_991

            call expression f"{Girl.tag}_rejected_piercing_twice" from _call_expression_264
        elif Girl.History.check(f"said_no_to_{Piercing.string}", tracker = "recent") == 1:
            call change_Girl_stat(Girl, "love", -2) from _call_change_Girl_stat_992

            call expression f"{Girl.tag}_rejected_piercing_once" from _call_expression_265
        else:
            call expression f"{Girl.tag}_{Piercing.string}_reject" from _call_expression_266

        $ Girl.History.update(f"said_no_to_{Piercing.string}")

    if mall:
        $ Character_picker_disabled = False
        $ belt_disabled = False

        show screen shop_screen("sex")

    return