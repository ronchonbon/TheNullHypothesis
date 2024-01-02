label give_Character_piercing(Character, Piercing, mall = False, discounted = False, instant = False):
    if mall:
        hide screen piercings_screen
        hide screen shop_screen

        $ Character_picker_disabled = True
        $ belt_disabled = True

    if Character.status["miffed"] or Character.status["mad"]:
        call expression f"{Character.tag}_{Piercing.string}_reject" from _call_expression_261

        $ Character.History.update(f"said_no_to_{Piercing.string}")
    elif approval_check(Character, threshold = eval(f"{Character.tag}_gift_thresholds[Piercing.string]"), extra_condition = "piercing"):
        call expression f"{Character.tag}_{Piercing.string}_accept" from _call_expression_262

        if mall and discounted:
            $ Player.cash -= int(0.5*Piercing.price)
        elif mall:
            $ Player.cash -= Piercing.price

        if "belly" in Piercing.string:
            $ Character.piercings["belly"] = True
        elif "nipple" in Piercing.string:
            if approval_check(Character, threshold = "see_breasts") and (renpy.get_screen("Wardrobe_screen") or approval_check(Character, threshold = "exhibitionism")):
                call expose(Character, "breasts", instant = instant) from _call_expose_14

                if not instant:
                    pause 1.0
            else:
                $ fade_to_black(0.4)

                "You give [Character.name] some privacy."

            if "barbell" in Piercing.string:
                if Character.piercings["nipple"] == "ring":
                    $ Character.piercings["nipple"] = "both"
                else:
                    $ Character.piercings["nipple"] = "barbell"
            elif "ring" in Piercing.string:
                if Character.piercings["nipple"] == "barbell":
                    $ Character.piercings["nipple"] = "both"
                else:
                    $ Character.piercings["nipple"] = "ring"
                    
            if approval_check(Character, threshold = "see_breasts") and (renpy.get_screen("Wardrobe_screen") or approval_check(Character, threshold = "exhibitionism")):
                pause 2.0

                call change_Outfit(Character, Character.Wardrobe.Outfits[Character.Outfit.name], instant = instant) from _call_change_Outfit_40
            else:
                $ fade_in_from_black(0.4)
        elif "labia" in Piercing.string:
            if approval_check(Character, threshold = "see_pussy") and (renpy.get_screen("Wardrobe_screen") or approval_check(Character, threshold = "exhibitionism")):
                call expose(Character, "pussy", instant = instant) from _call_expose_15

                if not instant:
                    pause 1.0
            else:
                $ fade_to_black(0.4)

                "You give [Character.name] some privacy."

            if "barbell" in Piercing.string:
                if Character.piercings["labia"] == "ring":
                    $ Character.piercings["labia"] = "both"
                else:
                    $ Character.piercings["labia"] = "barbell"
            elif "ring" in Piercing.string:
                if Character.piercings["labia"] == "barbell":
                    $ Character.piercings["labia"] = "both"
                else:
                    $ Character.piercings["labia"] = "ring"
                    
            if approval_check(Character, threshold = "see_pussy") and (renpy.get_screen("Wardrobe_screen") or approval_check(Character, threshold = "exhibitionism")):
                pause 2.0

                call change_Outfit(Character, Character.Wardrobe.Outfits[Character.Outfit.name], instant = instant) from _call_change_Outfit_41
            else:
                $ fade_in_from_black(0.4)

        if Piercing.string not in Character.inventory.keys():
            $ Character.inventory[Piercing.string] = Piercing

            if len(Player.inventory[Piercing.string]) > 1:
                $ Player.inventory[Piercing.string].remove(Piercing)
            else:
                $ del Player.inventory[Piercing.string]

        $ Character.History.update(f"put_in_{Piercing.string}")
    else:
        if Character.History.check(f"said_no_to_{Piercing.string}", tracker = "recent") >= 1:
            call change_Character_stat(Character, "love", -5) from _call_change_Character_stat_990
            call change_Character_stat(Character, "trust", -5) from _call_change_Character_stat_991

            call expression f"{Character.tag}_rejected_piercing_twice" from _call_expression_264
        elif Character.History.check(f"said_no_to_{Piercing.string}", tracker = "recent") == 1:
            call change_Character_stat(Character, "love", -2) from _call_change_Character_stat_992

            call expression f"{Character.tag}_rejected_piercing_once" from _call_expression_265
        else:
            call expression f"{Character.tag}_{Piercing.string}_reject" from _call_expression_266

        $ Character.History.update(f"said_no_to_{Piercing.string}")

    if mall:
        $ Character_picker_disabled = False
        $ belt_disabled = False

        call screen shop_screen("sex")

    return