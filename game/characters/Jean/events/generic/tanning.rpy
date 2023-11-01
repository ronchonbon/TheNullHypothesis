init python:

    def Jean_tan_wore_off():
        label = "Jean_tan_wore_off"

        conditions = [
            "(Jean.tan_lines['full'] and day - Jean.History.check_when('tan_lines_full') >= 5) or (Jean.tan_lines['top'] and day - Jean.History.check_when('tan_lines_top') >= 5) or (Jean.tan_lines['bottom'] and day - Jean.History.check_when('tan_lines_bottom') >= 5)"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_tan_wore_off:
    if Jean.tan_lines["full"] and day - Jean.History.check_when("tan_lines_full") >= 5:
        $ Jean.tan_lines["full"] = False

    if Jean.tan_lines["top"] and day - Jean.History.check_when("tan_lines_top") >= 5:
        $ Jean.tan_lines["top"] = False
    
    if Jean.tan_lines["bottom"] and day - Jean.History.check_when("tan_lines_bottom") >= 5:
        $ Jean.tan_lines["bottom"] = False

    return