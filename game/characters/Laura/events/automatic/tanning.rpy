init python:

    def Laura_tan_wore_off():
        label = "Laura_tan_wore_off"

        conditions = [
            "(Laura.tan_lines['full'] and day - Laura.History.check_when('tan_lines_full') >= 5) or (Laura.tan_lines['top'] and day - Laura.History.check_when('tan_lines_top') >= 5) or (Laura.tan_lines['bottom'] and day - Laura.History.check_when('tan_lines_bottom') >= 5)"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_tan_wore_off:
    if Laura.tan_lines["full"] and day - Laura.History.check_when("tan_lines_full") >= 5:
        $ Laura.tan_lines["full"] = False

    if Laura.tan_lines["top"] and day - Laura.History.check_when("tan_lines_top") >= 5:
        $ Laura.tan_lines["top"] = False
    
    if Laura.tan_lines["bottom"] and day - Laura.History.check_when("tan_lines_bottom") >= 5:
        $ Laura.tan_lines["bottom"] = False

    return