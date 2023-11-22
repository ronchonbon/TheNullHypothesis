init python:

    def Rogue_chapter_one_season_two_study_sessions():
        label = "Rogue_chapter_one_season_two_study_sessions"

        conditions = [
            "chapter == 1 and season == 2",
            
            "Rogue.History.check('studied_with_Player', tracker = 'season') >= 1",

            "Player.behavior == 'studying' and Rogue in Player.behavior_Partners and Rogue.behavior == 'studying'"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_two_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "So, what did ya wanna work on today?"
        ch_Player "How about that mutant physiology assignment?"

        $ Rogue.change_face("smirk2")

        ch_Rogue "Sure thing, [Rogue.Player_petname]."

        $ Rogue.change_face("smirk2", eyes = "down")

        "She helps you organize all the materials, and it takes a bit longer than usual, as you both exchange some small talk."

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        "She playfully falls onto the bed, beckoning you to lay down beside her."
        "Once you take your spot, she leans into your shoulder."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You start to work on the assignment, with [Rogue.name] guiding you towards the correct answer and where to find them."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        "You notice her staring at your hands, so you put one out for her to touch, while you continue working on the assignment."

        $ Rogue.change_face("smirk2", eyes = "closed", mouth = "lipbite", blush = 1)

        call take_off(Rogue, "gloves") from _call_take_off_17

        "She takes her gloves off and distracts herself by touching and playing with your hand."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Player "Hey, where can I find the answer to this question?"
        ch_Player "I don't remember the info from class."
        "You point to that particular question."

        $ Rogue.change_face("smirk2", blush = 1)

        "Without letting go of your other hand, she explains where to find it."
        ch_Rogue "So, the answer should be choice A."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_49

        "It doesn't take much longer to finish the assignment, and when you're done, she puts her gloves back on before helping you clean everything up."

        $ Rogue.change_face("smirk2", blush = 1)
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Want my help settin' up?"

        $ Rogue.change_face("smirk2")

        ch_Player "Sure do."
        "You have a good time chatting, as she helps you organize everything."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You plop down onto the bed, and [Rogue.name] follows suit, scooting right up next to you."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 2)
        
        "As she has you work on some of the more difficult course material, you absentmindedly put your hand out for her to touch."

        call take_off(Rogue, "gloves") from _call_take_off_18

        "She doesn't skip a beat, as she continues explaining one of the questions, while also removing her gloves and playing with your hand."

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Rogue "Ah think ya might have a bit of trouble with this one."
        "She points to one of the more difficult questions."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Think ya can do it?"
        ch_Player "Hmm. . ." 
        ch_Player "I think it's choice B, right?"

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Sorry, that ain't the right one." 

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "She goes over where you went wrong, continuing to touch your hands the whole time."

        $ Rogue.change_face("smirk2", blush = 1)

        call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_50

        "Once she's sure you understand everything, she puts her gloves back on and helps you clean up." 
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Want some help settin' everything up?"
        ch_Player "That would be nice."

        $ Rogue.change_face("smirk2")

        "She tells you about her day so far, as you help get everything organized."

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        "[Rogue.name] playfully drags you onto the bed and positions herself next to you. . ."
        "Making sure she's close enough to brush shoulders."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "As the session starts, you immediately put your hand out for her to touch."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        call take_off(Rogue, "gloves") from _call_take_off_19

        "You've made a lot of progress, so today is much more mutually beneficial, as you even help [Rogue.name] with some things she was having trouble with."
        "She absentmindedly plays with your hand, as the hours go by."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Player "So. . . what about this one, think you know the answer?"
        "You point to a particularly difficult question."

        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "Oh, sugar, ya can't trick me that easily."

        $ Rogue.change_face("sly")

        ch_Rogue "Ah remember this one, the answer is choice A."

        $ Rogue.change_face("smirk2")

        ch_Player "Damn, that's right."
        "The rest of the session goes by quickly, and [Rogue.name] continues to enjoy the physical connection."

        call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_51
        
        "Finally, she reluctantly puts her gloves back on and helps you clean everything up."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Thanks, [Rogue.Player_petname], for the session. . . and for everythin' else."
        ch_Player "Of course."

    $ ongoing_Event = False

    return