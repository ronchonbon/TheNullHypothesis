label give_Character_piercing(Companion, Piercing, mall = False, discounted = False, instant = False):
    if mall:
        hide screen piercings_screen
        hide screen shop_screen

        $ Character_picker_disabled = True
        $ belt_disabled = True

    if Companion.status["miffed"] or Companion.status["mad"]:
        call expression f"{Companion.tag}_{Piercing.string}_reject" from _call_expression_261

        $ Companion.History.update(f"said_no_to_{Piercing.string}")
    elif approval_check(Companion, threshold = Piercing.threshold, extra_condition = "piercing"):
        call expression f"{Companion.tag}_{Piercing.string}_accept" from _call_expression_262

        if mall and discounted:
            $ Player.cash -= int(0.5*Piercing.price)
        elif mall:
            $ Player.cash -= Piercing.price

        if "belly" in Piercing.string:
            $ Companion.piercings["belly"] = True
        elif "nipple" in Piercing.string:
            if approval_check(Companion, threshold = "see_breasts") and (renpy.get_screen("Wardrobe_screen") or approval_check(Companion, threshold = "exhibitionism")):
                call expose(Companion, "breasts", instant = instant) from _call_expose_14

                if not instant:
                    pause 1.0
            else:
                $ fade_to_black(0.4)

                "You give [Companion.name] some privacy."

            if "barbell" in Piercing.string:
                if Companion.piercings["nipple"] == "ring":
                    $ Companion.piercings["nipple"] = "both"
                else:
                    $ Companion.piercings["nipple"] = "barbell"
            elif "ring" in Piercing.string:
                if Companion.piercings["nipple"] == "barbell":
                    $ Companion.piercings["nipple"] = "both"
                else:
                    $ Companion.piercings["nipple"] = "ring"
                    
            if approval_check(Companion, threshold = "see_breasts") and (renpy.get_screen("Wardrobe_screen") or approval_check(Companion, threshold = "exhibitionism")):
                pause 2.0

                call change_Outfit(Companion, Companion.Wardrobe.Outfits[Companion.Outfit.name], instant = instant) from _call_change_Outfit_40
            else:
                $ fade_in_from_black(0.4)
        elif "labia" in Piercing.string:
            if approval_check(Companion, threshold = "see_pussy") and (renpy.get_screen("Wardrobe_screen") or approval_check(Companion, threshold = "exhibitionism")):
                call expose(Companion, "pussy", instant = instant) from _call_expose_15

                if not instant:
                    pause 1.0
            else:
                $ fade_to_black(0.4)

                "You give [Companion.name] some privacy."

            if "barbell" in Piercing.string:
                if Companion.piercings["labia"] == "ring":
                    $ Companion.piercings["labia"] = "both"
                else:
                    $ Companion.piercings["labia"] = "barbell"
            elif "ring" in Piercing.string:
                if Companion.piercings["labia"] == "barbell":
                    $ Companion.piercings["labia"] = "both"
                else:
                    $ Companion.piercings["labia"] = "ring"
                    
            if approval_check(Companion, threshold = "see_pussy") and (renpy.get_screen("Wardrobe_screen") or approval_check(Companion, threshold = "exhibitionism")):
                pause 2.0

                call change_Outfit(Companion, Companion.Wardrobe.Outfits[Companion.Outfit.name], instant = instant) from _call_change_Outfit_41
            else:
                $ fade_in_from_black(0.4)

        if Piercing.string not in Companion.inventory.keys():
            $ Companion.inventory[Piercing.string] = Piercing

        $ Companion.History.update(f"put_in_{Piercing.string}")
    else:
        if Companion.History.check(f"said_no_to_{Piercing.string}", tracker = "recent") >= 1:
            call change_Companion_stat(Companion, "love", -5) from _call_change_Companion_stat_990
            call change_Companion_stat(Companion, "trust", -5) from _call_change_Companion_stat_991

            call expression f"{Companion.tag}_rejected_piercing_twice" from _call_expression_264
        elif Companion.History.check(f"said_no_to_{Piercing.string}", tracker = "recent") == 1:
            call change_Companion_stat(Companion, "love", -2) from _call_change_Companion_stat_992

            call expression f"{Companion.tag}_rejected_piercing_once" from _call_expression_265
        else:
            call expression f"{Companion.tag}_{Piercing.string}_reject" from _call_expression_266

        $ Companion.History.update(f"said_no_to_{Piercing.string}")

    if mall:
        $ Character_picker_disabled = False
        $ belt_disabled = False

        show screen shop_screen("sex")

    return