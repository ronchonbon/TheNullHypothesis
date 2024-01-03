init python:

    def Laura_texting_save_cum():
        label = "Laura_texting_save_cum"

        conditions = [
            "renpy.random.random() > 0.5",

            "Laura.check_traits('quirk')",

            "not Laura.timed_text_options",

            "time_index < 2",
            "not Player.History.check('orgasmed', tracker = 'daily')",
            
            "not Player.History.check('received_invite', tracker = 'daily')",

            "Player.location not in ['hold', Laura.location, Laura.destination]",
            "Player.destination not in [Laura.location, Laura.destination]",

            "Laura.History.check('creampie') or Laura.History.check('swallow_cum') or Laura.History.check('anal_creampie')",

            "Laura.is_in_normal_mood()",    
            "Laura.status['horny'] or Laura.status['nympho']"]

        waiting = True

        repeatable = True

        return EventClass(label, conditions, waiting = waiting, repeatable = repeatable)

label Laura_texting_save_cum:
    $ temp = Laura.Player_petname.capitalize()

    call receive_text(Laura, f"{temp}", buzz = False) from _call_receive_text_256    
    call receive_text(Laura, "You better come to my room tonight", buzz = False) from _call_receive_text_257
    call receive_text(Laura, "I need to use you", buzz = False) from _call_receive_text_258
    call receive_text(Laura, "Thoroughly", buzz = False) from _call_receive_text_259
    call receive_text(Laura, "So you're not allowed to cum until then", buzz = False) from _call_receive_text_260
    call receive_text(Laura, "I'll be able to tell", buzz = False) from _call_receive_text_261

    $ Laura.timed_text_options.update({"Laura_texting_save_cum": ["but I had. . . other plans today", "okay, I'll be there. and I'll save everything for you", "I'll come over tonight, but no promises about the other thing. . ."]})

    $ Player.History.update("received_invite")

    return

label Laura_texting_save_cum_response:
    $ temp = Laura.timed_text_options["Laura_texting_save_cum"][:]

    $ del Laura.timed_text_options["Laura_texting_save_cum"]

    if Laura.text_history[-1][1] == temp[0]:
        call receive_text(Laura, "Fine") from _call_receive_text_263
        call receive_text(Laura, "I'll just get off by myself") from _call_receive_text_264
    elif Laura.text_history[-1][1] == temp[1]:
        call receive_text(Laura, "Good") from _call_receive_text_265
        
        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_348

        $ Player.schedule[3] = [["True", "EventScheduler.Events['Laura_saving_cum'].start()"]]
    elif Laura.text_history[-1][1] == temp[2]:
        call receive_text(Laura, "Fine, just be here") from _call_receive_text_266

        hide screen phone_screen

        call set_the_scene(Laura, location = Laura.location) from _call_set_the_scene_118

        call change_Character_stat(Laura, "love", 0) from _call_change_Character_stat_349

    return

init python:

    def Laura_saving_cum():
        label = "Laura_saving_cum"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_saving_cum:
    $ ongoing_Event = True

    if Player.location != Laura.home:
        "You remember you promised to come over to [Laura.name]'s tonight."

        if Player.History.check("orgasmed", tracker = "daily"):
            "You hope she was lying about being able to tell if you. . ."

        call remove_Characters(location = Laura.home) from _call_remove_Characters_322
        call send_Characters(Laura, Laura.home) from _call_send_Characters_102
        call set_the_scene(location = Laura.home) from _call_set_the_scene_119

        $ Laura.change_face("suspicious1", mouth = "lipbite", blush = 2)
        
        "As you enter, [Laura.name] stares at you intently."
        "Her nostrils flare as you get closer."
    else:
        call remove_everyone_but(Laura) from _call_remove_everyone_but_10

        "[Laura.name] stares at you intently."
        "Her nostrils flare."

    if Player.check_traits("grool") or Player.check_traits("dirty_cock"):
        $ Laura.change_face("angry1", blush = 2)

        ch_Laura "You didn't do as I said."
        ch_Laura "{i}Grrrrrr{/i}"
    else:
        $ Laura.change_face("sexy", blush = 2)

        ch_Laura "Good, so you did as I said."
    
    $ choice_disabled = False

    $ ongoing_Event = False

    return