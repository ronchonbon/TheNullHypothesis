init python:

    def Kurt_Sunday_morning_text():
        label = "Kurt_Sunday_morning_text"

        conditions = [
            "Kurt.History.check('texted_Sunday_morning', tracker = 'daily')",
            
            "day - EventScheduler.Events['Kurt_Sunday_morning_text'].completed_when != 0",
            
            "time_index == 2"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Kurt_Sunday_morning_text:
    $ fade_in_from_black(0.4)
    
    call receive_text(Kurt, "Sorry mein Bruder") from _call_receive_text_220
    call receive_text(Kurt, "Was at church") from _call_receive_text_221
    
    return