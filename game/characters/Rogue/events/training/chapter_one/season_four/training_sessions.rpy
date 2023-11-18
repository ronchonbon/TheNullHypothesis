init python:

    def Rogue_chapter_one_season_four_training_sessions():
        label = "Rogue_chapter_one_season_four_training_sessions"

        conditions = [
            "chapter == 1 and season == 4",
            "Rogue.History.check('trained_with_Player', tracker = 'season') >= 1",
            "Player.training == Rogue and Rogue.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_four_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah've been needin' a good workout."
        ch_Player "Same."
        ch_Player "C'mon, I'll help you stretch."

        $ Rogue.change_face("surprised1", mouth = "smile")

        $ fade_to_black(0.4)

        "[Rogue.name] seems pretty eager, as you both go through some light exercises and help each other stretch."
        "She vents a lot of the day's woes to you, and you do the same back."
        "The warm up is as much of a way to destress, as it is to prepare for the upcoming training session."

        $ fade_in_from_black(0.4)

        $ Rogue.change_face("smirk2")

        "Your growing awareness and control over the powers inside you bring some new insights. . ."

        $ Rogue.change_face("worried1")

        "But unfortunately not ones that have much benefit to [Rogue.name]."

        $ Rogue.change_face("worried1", mouth = "smirk")

        "Despite her own lack of progress, she seems happy that you've been doing so well."
        "After a good sparring session, her spirits are right back up."
        ch_Rogue "Ah'm gettin' real good, right?"

        $ Rogue.change_face("smirk2")

        ch_Player "You really are."
        ch_Player "If I didn't have such an advantage, you'd be able to beat me up with ease."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Flattery will get ya places, [Rogue.Player_petname]. . ."
        ch_Rogue "But we both know it ain't just yer 'advantages'."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah think that's enough for today."
        ch_Rogue "See ya later, hon'."
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Ah'm ready to go!"
        ch_Player "You seem awfully enthusiastic today."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Sorry. . . just excited. . ."

        $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

        ch_Rogue "Ah really enjoy trainin' with ya."
        ch_Player "I enjoy it too."

        $ Rogue.change_face("smirk2")

        ch_Player "Let's get to it."

        $ fade_to_black(0.4)

        "The warm up is a bit more intense than usual, as [Rogue.name]'s competitive spirit shows itself."
        "She makes a game out of it, and you handicap yourself to keep things fair."
        "Despite all your advantages, [Rogue.name] manages to beat you." 

        $ fade_in_from_black(0.4)

        $ Rogue.change_face("sly")

        "After giving her a minute to catch her breath. . ."
        ch_Rogue "Yer gettin' slow."
        ch_Player "Or you're getting pretty fast."

        $ Rogue.change_face("smirk2")

        ch_Player "{size=-5}That handicap was pretty unfair, though{/size}. . ."

        $ Rogue.change_face("sly")

        ch_Rogue "Mhm, sure, hon'."
        ch_Rogue "Let's get into the sparrin'."
        ch_Rogue "Maybe that'll help with the bruised ego."

        $ Rogue.change_face("smirk2")

        "You can tell she pushed herself pretty hard earlier, so the sparring is a bit quicker than usual."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah'm pretty tuckered out, can we call it there?"
        ch_Player "Sure, as long as you agree the handicap earlier was unfair."

        $ Rogue.change_face("sly")

        ch_Rogue "Nope."
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", eyes = "right")

        ch_Player "Hey, everything alright?"

        $ Rogue.change_face("worried1")

        ch_Rogue "Just got a lot on my mind. . ."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Can we just get into the trainin'?"
        ch_Rogue "Ah need a distraction."
        ch_Player "Sure thing."

        $ fade_to_black(0.4)

        "[Rogue.name] doesn't seem to want to vent, so you just go through a relatively quiet warm up."
        "Afterwards, you try helping her through some power control exercises, but she seems even more distracted than usual."
        "At the very least, you manage to give yourself a proper headache and make decent progress with your own powers."

        $ fade_in_from_black(0.4)

        $ Rogue.change_face("worried1", eyes = "right")

        ch_Player "Wanna spar for a bit before we finish?"

        $ Rogue.change_face("worried2")

        pause 1.0

        $ Rogue.change_face("worried1")

        ch_Rogue "Yeah. . . sorry."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "We could also. . . just talk about what's bothering you."

        $ Rogue.change_face("worried1", eyes = "down")

        ch_Rogue "Ah can't. . ."

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm sorry."
        ch_Player "Don't worry about it."

        $ Rogue.change_face("worried1", mouth = "smirk")

        "You go through a quick sparring session, and it seems to provide a good distraction for [Rogue.name]."

        $ Rogue.change_face("smirk1")

        "But she ends up cutting the session short."

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm real sorry, [Rogue.Player_petname]."
        ch_Rogue "Feel like ah'm wastin' yer time."

        $ Rogue.change_face("worried1", eyes = "right")

        ch_Rogue "Let's just call it here."

        $ Rogue.change_face("worried1")

        ch_Rogue "Ah'm no good to anybody like this."
        ch_Rogue "Ah'm just gonna go spend some time alone."
        ch_Rogue "See ya later. . ."

    call remove_Characters(Rogue) from _call_remove_Characters_199

    if dice_roll == 3:
        call send_Characters(Rogue, Rogue.home) from _call_send_Characters_165

    $ ongoing_Event = False

    return