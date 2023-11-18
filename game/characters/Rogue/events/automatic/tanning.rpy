init python:

    def Rogue_tan_wore_off():
        label = "Rogue_tan_wore_off"

        conditions = [
            "(Rogue.tan_lines['full'] and day - Rogue.History.check_when('tan_lines_full') >= 5) or (Rogue.tan_lines['top'] and day - Rogue.History.check_when('tan_lines_top') >= 5) or (Rogue.tan_lines['bottom'] and day - Rogue.History.check_when('tan_lines_bottom') >= 5)"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_tan_wore_off:
    if Rogue.tan_lines["full"] and day - Rogue.History.check_when("tan_lines_full") >= 5:
        $ Rogue.tan_lines["full"] = False

    if Rogue.tan_lines["top"] and day - Rogue.History.check_when("tan_lines_top") >= 5:
        $ Rogue.tan_lines["top"] = False
    
    if Rogue.tan_lines["bottom"] and day - Rogue.History.check_when("tan_lines_bottom") >= 5:
        $ Rogue.tan_lines["bottom"] = False

    return