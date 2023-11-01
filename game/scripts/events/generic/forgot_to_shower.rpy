init python:

    def Player_forgot_to_shower():
        label = "Player_forgot_to_shower"

        conditions = [
            "day > 3 and day - Player.History.check_when('showered') >= 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Player_forgot_to_shower:
    $ Player.sweaty = True

    return