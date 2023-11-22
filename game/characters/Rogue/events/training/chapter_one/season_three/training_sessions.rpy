init python:

    def Rogue_chapter_one_season_three_training_sessions():
        label = "Rogue_chapter_one_season_three_training_sessions"

        conditions = [
            "chapter == 1 and season == 3",

            "Rogue.History.check('trained_with_Player', tracker = 'season') >= 2",
            
            "Player.behavior == 'training' and Rogue in Player.behavior_Partners and Rogue.behavior == 'training'"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_three_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("smirk1")

        ch_Rogue "Ah'm excited."
        ch_Rogue "It's always a good time, trainin' with ya."
        ch_Player "You got that right."
        ch_Player "C'mon, let's start."

        $ Rogue.change_face("smirk2")

        "The warm up today is a bit longer than usual, as you both take your time and just have a good time chatting."

        $ Rogue.change_face("worried1")

        "Afterwards, you do your best to help [Rogue.name] make progress with her mental block."
        "Despite both of your powers being relatively similar in theory, nothing you've learned so far really transfers over."
        "At the very least, the understanding of your own powers deepens a bit."

        $ Rogue.change_face("worried1", mouth = "smirk")

        "Once you get into the sparring, her mood seems to brighten."

        $ Rogue.change_face("smirk2")

        "You've been making a lot of progress in terms of combat prowess and end up giving [Rogue.name] a few pointers."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Wish we could keep goin', but ah got some studyin' to do."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'll see ya later."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2")

        ch_Player "C'mon, [Rogue.petname]."
        ch_Player "Let's warm up."

        $ Rogue.change_face("smirk2", eyes = "right", mouth = "lipbite")

        ch_Rogue "Ah've had this cramp. . ."

        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Rogue "Could use some help stretchin' it out."

        $ fade_to_black(0.4)

        "After helping [Rogue.name] with her 'cramp', you go through a standard warm up."
        "You spend just as much time chatting as you do getting ready for the training session."

        $ fade_in_from_black(0.4)

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Ah was thinkin'. . ."
        ch_Rogue "You mentioned somethin' last time ya tried tellin' me 'bout yer powers."
        "Instead of you trying to help her, she brings up a few good points and actually helps you make a bit of progress with your power control."

        $ Rogue.change_face("smirk2")

        "After you've developed a proper headache, you switch to sparring and show off how much progress you've been making."

        $ Rogue.change_face("confused1", mouth = "smirk")
        ch_Rogue "Yer gettin' real good, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ya'know. . . people don't normally get so good, so darn fast."
        ch_Player "I'm just that much better than everyone else, I know."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Well, if yer that much better, ah expect ya to not get so banged up next time yer in a real fight."
        ch_Player "Just you wait."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Thanks for the session today."
        ch_Rogue "Ah'll see ya later."
    elif dice_roll == 3:
        $ Rogue.change_face("smirk2")

        ch_Player "Feelin' good today?"
        ch_Rogue "Ah sure am."
        ch_Rogue "C'mon, [Rogue.Player_petname]."

        $ Rogue.change_face("sly")

        ch_Rogue "Ah could use some help stretchin' again."

        $ fade_to_black(0.4)

        "You help [Rogue.name] work through any kinks she hasn't been able to stretch out on her own."
        "The warm up takes a while, as usual, she certainly doesn't seem to mind."

        $ fade_in_from_black(0.4)

        $ Rogue.change_face("smirk2")

        "You try to run [Rogue.name] through some of the power control exercises [Jean.name] has been teaching you."

        $ Rogue.change_face("worried1")

        "While you notice yourself making some progress, [Rogue.name] can't say the same."

        $ Rogue.change_face("smirk2")

        "Her dour mood brightens, as you get into sparring, and you both have a good deal of fun pushing yourselves."
        "With all the progress you've been making, you can tell just how much better [Rogue.name]'s also gotten."
        "Maybe training together has been more than just a good time and ends up being actually productive."
        ch_Player "You're getting a lot better."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Player "And I'm not just saying that."
        ch_Rogue "Well. . . thanks."
        ch_Rogue "When ah see ya improvin' so quickly, gives me some motivation."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "But ah think ah'm all tuckered out."
        ch_Rogue "Can we call if for today?"
        ch_Player "Sure, I'll see you later."

    call remove_Characters(Rogue) from _call_remove_Characters_204

    $ ongoing_Event = False

    return