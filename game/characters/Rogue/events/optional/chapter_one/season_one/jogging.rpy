init python:

    def Rogue_chapter_one_season_one_jogging():
        label = "Rogue_chapter_one_season_one_jogging"

        conditions = [
            "chapter == 1 and season == 1",

            "time_index == 2",

            "Player.History.check('trained', tracker = 'last')",
            "not Rogue.History.check('trained_with_Player', tracker = 'last')",

            "time_index not in Rogue.schedule.keys()",

            "Rogue.location not in ['hold', 'bg_lockers']",
            "Rogue.original_location != Player.location",

            "Rogue.is_in_normal_mood()"]

        waiting = True

        return EventClass(label, conditions, waiting = waiting)

label Rogue_chapter_one_season_one_jogging:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_lockers")
    call set_the_scene(location = "bg_lockers")

    "You head to the locker rooms after your session in the Danger Room."

    $ Rogue.change_face("neutral", eyes = "down")

    call send_Characters(Rogue, "bg_lockers", behavior = "training")

    "On the way in, you notice [Rogue.name] exiting the room looking dejected."

    menu:
        extend ""
        "Approach [Rogue.name]":
            pass
        "Don't get involved":
            call remove_Characters(Rogue)

            $ ongoing_Event = False

            return

    "She heads outside before you can get her attention - you follow her."

    call remove_Characters(location = "bg_campus")
    call set_the_scene(location = "bg_campus")
    
    $ Rogue.change_face("neutral", eyes = "down")

    call send_Characters(Rogue, "bg_campus", behavior = "training")

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
            call change_Girl_stat(Rogue, "love", small_stat)
            call change_Girl_stat(Rogue, "trust", medium_stat)

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

            ch_Rogue "Ah mean, if you're sure, it'd be nice to have some company for once." 
        "Of course. It's not fair you always have to work out alone.":
            call change_Girl_stat(Rogue, "love", medium_stat)
            call change_Girl_stat(Rogue, "trust", medium_stat)

            $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 1)

            ch_Rogue "That's really kind of you. . . Ah dunno what to say." 
        "Absolutely! And you can't say you don't want to know which of us is faster, right?":
            call change_Girl_stat(Rogue, "trust", medium_stat)

            $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

            ch_Rogue "Oh really? Sounds like a challenge - hope y'all can deliver!" 

    $ Rogue.change_face("smirk2")

    "You talk to Rogue for a little longer and make more formal plans to go running."
    "With that done, [Rogue.name] heads off, looking a little more upbeat than she did before."

    call remove_Characters(Rogue)

    $ ongoing_Event = False

    return