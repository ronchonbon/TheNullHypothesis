init python:

    def Rogue_chapter_one_season_four_study_sessions():
        label = "Rogue_chapter_one_season_four_study_sessions"

        conditions = [
            "season == 4",
            "Rogue.History.check('studied_with_Player', tracker = 'season') >= 1",
            "Player.studying == Rogue and Rogue.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_four_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Gonna help me set up?"
        ch_Rogue "'Course, [Rogue.Player_petname]"
        ch_Player "Don't worry, I don't wanna try too hard today either."

        $ Rogue.change_face("smirk2")

        "You put some good music on and have a good time talking with [Rogue.name], as she helps you organize all the study materials."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "She falls down onto the bed beside you and doesn't waste any time reaching out for your hand to touch."
        "You oblige her, and it takes a while to actually start studying, as you just enjoy the music and each other's company." 
        "You finally get to work, and [Rogue.name] helps with a difficult assignment."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Rogue "Alright, why don't ya try this question on yer own."
        ch_Rogue "Ah'll explain if ya get anythin' wrong."
        "She points to a particular question."

        $ Rogue.change_face("smirk2", blush = 1)

        "You go through the question, double checking your work before committing to an answer."
        ch_Player "Okay, I'm pretty sure it's choice B."

        $ Rogue.change_face("happy", blush = 1)

        ch_Rogue "Great job."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah think that's enough for today, let's clean up."
        "You're both quite lazy about it, as you just jam out to the music, slowly putting all the materials away."

        $ Rogue.change_face("smirk2", blush = 1)
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Let's try a bit harder today."
        ch_Player "That last test was pretty difficult. . ."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Whatever ya want, [Rogue.Player_petname]."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah also struggled with it a bit."
        "You exchange a bit of small talk, but setup is pretty quick today all things considered."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You give [Rogue.name] a playful shove, and she falls onto the bed, dragging you down with her."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)
        
        "You both work together to go through the study guide, as she absentmindedly touches your hand."
        "She helps you with one topic, and you help her with another."
        "Today's session is very mutually beneficial."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Player "I don't know how to do this one, can I just watch you go through it?."
        "You point to that particular question."

        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "Alright, [Rogue.Player_petname], watch 'n learn."
        "She goes through the work, explaining her reasoning for each part."

        $ Rogue.change_face("sly")

        ch_Rogue "Ain't no way it's anythin' other than choice B>"
        "You check the answer key."
        ch_Player "Great job, [Rogue.petname], that's the right answer." 

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "It doesn't take much longer to go through the rest of the study guide, and she helps you clean everything up in the end."

        $ Rogue.change_face("smirk2")
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah feel bad. . . but. . ."
        ch_Player "Don't worry, [Rogue.petname], we can take it easy today."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Thanks, [Rogue.Player_petname]."
        "She puts some good music on, and you both take your time setting everything up."

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        "Finally, you both take your positions on the bed, leaning into each other's shoulders."
        "Despite everything being set up, you just chill for a while, chatting about nothing."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "When the session finally starts, you mostly work on one of the assignments that's due relatively soon."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        "Although, that mostly just means [Rogue.name] helps you get to the answers as quickly as possible so she can get back to jamming out."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Player "What about this one?"
        "You point to a particularly difficult question."

        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "Here, [Rogue.Player_petname], let me show ya."
        "She basically does all the work for you."
        ch_Rogue "So that means the answer is choice C."

        $ Rogue.change_face("smirk2")

        ch_Player "Awesome, thanks."
        "After that, not much 'studying' actually gets done, as you both spend the rest of the time just enjoying each other's company."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "We should probably clean up."
        ch_Rogue "Ah agree."

    call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_1071

    $ ongoing_Event = False

    return