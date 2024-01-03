init python:

    def Rogue_texting_ask_to_masturbate():
        label = "Rogue_texting_ask_to_masturbate"

        conditions = [
            "renpy.random.random() > 0.5",

            "Rogue.check_traits('quirk')",

            "Rogue.behavior == 'masturbating'",

            "not Rogue.timed_text_options",

            "Player.location not in ['hold', Rogue.location, Rogue.destination]",
            "Player.destination not in [Rogue.location, Rogue.destination]",
                        
            "Rogue.History.check('self_touch_pussy')",

            "Rogue.is_in_normal_mood()",   
            "Rogue.status['horny'] or Rogue.status['nympho']"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_texting_ask_to_masturbate:
    $ temp = Rogue.Player_petname.capitalize()

    call receive_text(Rogue, f"{temp}", buzz = False) from _call_receive_text_478
    call receive_text(Rogue, "Im. . .", buzz = False) from _call_receive_text_479
    call receive_text(Rogue, "All pent up", buzz = False) from _call_receive_text_480
    call receive_text(Rogue, "Am I allowed to", buzz = False) from _call_receive_text_481
    call receive_text(Rogue, "Touch myself?", buzz = False) from _call_receive_text_482

    $ Rogue.timed_text_options.update({"Rogue_texting_ask_to_masturbate": ["not allowed. maybe I'll come take care of you later", "yes, you're allowed. but only if you say please", "you're not allowed, because I'm about to head over and take care of you myself"]})

    $ Rogue.behavior = None

    return

label Rogue_texting_ask_to_masturbate_response:
    $ temp = Rogue.timed_text_options["Rogue_texting_ask_to_masturbate"][:]

    $ del Rogue.timed_text_options["Rogue_texting_ask_to_masturbate"]

    if Rogue.text_history[-1][1] == temp[0]:
        call receive_text(Rogue, "Alright, [Rogue.Player_petname]") from _call_receive_text_483
        call receive_text(Rogue, "Please don't make me wait too long") from _call_receive_text_484
    elif Rogue.text_history[-1][1] == temp[1]:
        call receive_text(Rogue, "Please, [Rogue.Player_petname]") from _call_receive_text_485
        call send_text(Rogue, "good, go ahead") from _call_send_text_35
                    
        if Rogue.location in [Rogue.home, Player.home]:
            $ Rogue.behavior = "masturbating"
    elif Rogue.text_history[-1][1] == temp[2]:
        call receive_text(Rogue, "Lord, please do") from _call_receive_text_486
        
        hide screen phone_screen

        call remove_everyone_but(Rogue, location = Rogue.location, fade = False) from _call_remove_everyone_but_12
        call set_the_scene(location = Rogue.location) from _call_set_the_scene_199

        $ Rogue.change_face("manic", blush = 2)
        
        $ choice_disabled = False
        
    return