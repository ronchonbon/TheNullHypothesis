init python:

    def Ororo_tan_wore_off():
        label = "Ororo_tan_wore_off"

        conditions = [
            "(Ororo.tan_lines['full'] and day - Ororo.History.check_when('tan_lines_full') >= 5) or (Ororo.tan_lines['top'] and day - Ororo.History.check_when('tan_lines_top') >= 5) or (Ororo.tan_lines['bottom'] and day - Ororo.History.check_when('tan_lines_bottom') >= 5)"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Ororo_tan_wore_off:
    if Ororo.tan_lines["full"] and day - Ororo.History.check_when("tan_lines_full") >= 5:
        $ Ororo.tan_lines["full"] = False

    if Ororo.tan_lines["top"] and day - Ororo.History.check_when("tan_lines_top") >= 5:
        $ Ororo.tan_lines["top"] = False
    
    if Ororo.tan_lines["bottom"] and day - Ororo.History.check_when("tan_lines_bottom") >= 5:
        $ Ororo.tan_lines["bottom"] = False

    return