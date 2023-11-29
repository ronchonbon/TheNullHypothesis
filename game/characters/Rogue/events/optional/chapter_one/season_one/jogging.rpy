init python:

    def Rogue_chapter_one_season_one_jogging_setup():
        label = "Rogue_chapter_one_season_one_jogging_setup"

        conditions = [
            "Rogue.location not in ['hold', Player.location, Player.destination]",
            "'bg_lockers' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Rogue_chapter_one_season_one_jogging'].completed",

            "time_index not in Rogue.schedule.keys()",

            "chapter == 1 and season == 1",

            "time_index == 2",
            "weather != 'rain'",    

            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_chapter_one_season_one_jogging_setup:
    call send_Characters(Rogue, "bg_lockers", behavior = "changing") from _call_send_Characters_328

    return

init python:

    def Rogue_chapter_one_season_one_jogging():
        label = "Rogue_chapter_one_season_one_jogging"

        conditions = [
            "Player.destination == 'bg_lockers'",

            "chapter == 1 and season == 1",

            "time_index == 2",
            "weather != 'rain'",    
            
            "Rogue.location == 'bg_lockers'",
            "Rogue.behavior == 'changing'",

            "Rogue.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_lockers": [
                "Player.location != 'bg_lockers'",

                "chapter == 1 and season == 1",

                "time_index == 2",
                "weather != 'rain'",    
                
                "Rogue.location == 'bg_lockers'",
                "Rogue.behavior == 'changing'",

                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Rogue_chapter_one_season_one_jogging:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_lockers") from _call_remove_Characters_341
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_387

    $ Rogue.change_face("sad", eyes = "down")

    call send_Characters(Rogue, "bg_lockers", behavior = "training") from _call_send_Characters_313

    "On the way into the locker rooms, you notice [Rogue.name] exiting with a dejected look on her face."

    menu:
        extend ""
        "Ask [Rogue.name] where she's headed":
            pass
        "Let her do her thing":
            call remove_Characters(Rogue) from _call_remove_Characters_324

            $ EventScheduler.Events["Rogue_chapter_one_season_one_jogging"].completed = False
            $ EventScheduler.Events["Rogue_chapter_one_season_one_jogging"].completed_when = 1e8

            $ EventScheduler.Events["Rogue_chapter_one_season_one_jogging"].counter = 0

            $ ongoing_Event = False

            return

    "She heads outside before you can get her attention - you follow her."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_325
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_388
    
    $ Rogue.change_face("neutral", eyes = "down")

    call send_Characters(Rogue, "bg_campus", behavior = "training") from _call_send_Characters_314

    "You catch up with her as she starts doing some warmup exercises on the front lawn."

    $ Rogue.change_face("surprised2")

    ch_Player "Hey, [Rogue.name]. Everything okay?"

    $ Rogue.change_face("worried1")

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "*sigh* Yeah, everythin's fine, ah guess."
    ch_Rogue "Just had a crappy trainin' session there. Well, tried to at least."

    $ Rogue.change_face("worried1")

    ch_Player "Tried to?"
    ch_Rogue "Yeah. It's these darn powers again."

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "We don't have the facilities for anyone else to train safely with me, so if ah want to get a proper session in, ah have to do it alone." 

    $ Rogue.change_face("angry1")

    ch_Rogue "Ah have to sit on the sidelines 'n watch everyone else spar together, do team activities. . ."

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "So yeah, most of the time, it's just easier to come out here 'n go for a run."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "You do that a lot?"
    ch_Rogue "Let's just say ah'm probably one of the better distance runners at the school for a reason."

    $ Rogue.change_face("worried2")

    ch_Player "Well, I just finished a training session myself, but if you want a running buddy, I wouldn't mind helping out. "

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Really? Ah don't mind runnin' alone. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Rogue "But ah'll admit, the company would be nice."

    menu: 
        extend ""
        "Really. Besides, I can always use the extra cardio!":
            call change_Girl_stat(Rogue, "love", small_stat) from _call_change_Girl_stat_127
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_128

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

            ch_Rogue "Ah mean, if you're sure, it'd be nice to have some company for once." 
        "Of course. It's not fair you always have to work out alone.":
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_135
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_136

            $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 1)

            ch_Rogue "That's really kind of you. . . Ah dunno what to say." 
        "Absolutely! And you can't say you don't want to know which of us is faster, right?":
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_137

            $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

            ch_Rogue "Oh really? Sounds like a challenge - hope y'all can deliver!" 

    $ Rogue.change_face("smirk2")

    "You talk to [Rogue.name] for a little longer and make more formal plans to go running."
    "With that done, [Rogue.name] heads off, looking a little more upbeat than she did before."

    call remove_Characters(Rogue) from _call_remove_Characters_326

    $ ongoing_Event = False

    return