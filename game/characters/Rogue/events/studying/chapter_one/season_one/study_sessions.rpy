init python:

    def Rogue_chapter_one_season_one_study_sessions():
        label = "Rogue_chapter_one_season_one_study_sessions"

        conditions = [
            "chapter == 1 and season == 1",

            "Rogue.History.check('studied_with_Player', tracker = 'season') >= 2",
            
            "Player.behavior == 'studying' and Rogue in Player.behavior_Partners and Rogue.behavior == 'studying'"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Rogue_chapter_one_season_one_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Rogue.change_face("happy")

        ch_Player "Just gotta set things up before we start."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'll help!"
        ch_Player "Thanks."
        "After taking a few minutes to set up all the course materials, you get right into the tutoring session."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        "Once you hop onto the bed, as usual, she scoots close enough for your shoulders to touch."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You go through the material you've learned in psychology so far, and she helps you work on some of the upcoming assignments."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        "While you're writing something down, you notice she's looking at your hands."

        $ Rogue.change_face("worried2", blush = 2)

        ch_Player "Did you want to touch my hands again?" 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Yes. . ." 

        menu:
            extend ""
            "Say please.":
                $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 
                
                pause 1.0
                
                $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1) 
                
                ch_Rogue ". . . Please." 
                
                call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_1077
            "Be my guest.":
                $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1)

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)
        
        call take_off(Rogue, "gloves") from _call_take_off_11

        "[Rogue.name] removes her glove and takes your hand, shuddering slightly."

        $ Rogue.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 2)

        "After a few moments she lets go."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Thanks, sugar."
        ch_Rogue "Ah really appreciate it. . ."

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Player "You're welcome."
        "The rest of the session goes by quickly, but there's one question you're still not sure about."
        ch_Player "What about this one? I can't figure it out."
        "You point to a particular question."

        ch_Rogue "Ah had a bit of trouble with that one too."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'm pretty sure it's choice B."
        "After that, the session doesn't last much longer, and [Rogue.name] helps you clean up at the end."
    elif dice_roll == 2:
        $ Rogue.change_face("happy")

        ch_Rogue "Here, darlin'."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Let's get everythin' set up."
        "You both take a few minutes to lay out all the textbooks and study guides."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "[Rogue.name] takes her usual position on the bed, scooting close enough to brush shoulders with you." 
        "With an exam coming up, you decide to mostly review stuff for mutant physiology."
        "You don't have much difficulty grasping the majority of the material, mostly thanks to [Rogue.name]'s help, but there is one question giving you trouble."

        $ Rogue.change_face("smirk2")

        ch_Rogue ". . . good job, hon'."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Rogue "Was there anythin' else given' ya trouble?" 
        ch_Player "Yeah, this one."
        "You point to a particular practice question."

        $ Rogue.change_face("confused1")

        ch_Rogue "Hmm, ah don't remember seein' this one."

        $ Rogue.change_face("confused1", eyes = "down")

        "She quickly checks her notes."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Now ah remember, the answer is choice D."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Thanks."

        $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah was wonderin'. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue ". . . If you wouldn't mind lettin' me touch yer hands again?"
        ch_Player "You can."

        $ Rogue.change_face("happy", eyes = "wide", blush = 2)

        call take_off(Rogue, "gloves") from _call_take_off_12

        "She eagerly takes her gloves off and gently grabs your hand."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        "She seems fascinated by them, as she gingerly touches your skin."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        "After a moment she takes her hands back."
        ch_Rogue "Thanks. . . ah really appreciate it." 

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah think that's enough for today."
        "You help [Rogue.name] put away all the books."
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Could ya help me set everythin' up?"
        ch_Player "Sure."

        $ Rogue.change_face("smirk2")

        "With your help, setting up only takes a few minutes."

        $ Rogue.change_face("smirk2", eyes = "down")

        "You hop onto the bed, with [Rogue.name] taking her usual spot next to you."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "She leans into your shoulder a bit."
        "The session starts, and she starts going over a few things you were struggling to understand."
        "With her there to tutor you, everything is very easy to understand."

        $ Rogue.change_face("smirk2", eyes = "down")

        "After a couple hours, you have most of the material down pat."
        "There's just one question that's giving you trouble."

        $ Rogue.change_face("confused1", mouth = "smirk")

        ch_Player ". . . Yeah this one. Do you know the answer?"
        "You point to a particularly difficult question."

        $ Rogue.change_face("smirk2", eyes = "down")

        ch_Rogue "Here, sugar, the answer is choice C."

        ch_Player "Awesome, thanks."
        "The session doesn't last much longer, and you both start putting everything away."

        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Rogue ". . ." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Could ah maybe. . ."

        $ Rogue.change_face("surprised2", blush = 1)

        "Before she can even finish, you put your hand out for her to touch." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Player "I knew what you were gonna ask."
        ch_Rogue "Thanks, sugar." 

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        call take_off(Rogue, "gloves") from _call_take_off_13

        "She takes her glove off and grasps your hand."

        $ Rogue.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 2)

        "Her fingers gently caress your hands, and she seems lost in the feeling for a while before pulling away." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Player "Well. . . that was a productive session."
    elif dice_roll == 4:
        $ Rogue.change_face("happy")

        ch_Player "Gonna help me set everything up?" 

        $ Rogue.change_face("smirk2")

        ch_Rogue "'Course ah will, sugar."
        "You spend the next few minutes organizing all the notes and study guides."
        "[Rogue.name] also 'accidentally' brushes against you a few times."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "You hop onto the bed next to her, and she makes sure to scoot very close to you, with her shoulder touching your."

        $ Rogue.change_face("confused1", mouth = "smirk", eyes = "down")

        "As the session starts, [Rogue.name] moves to focus on calculus, despite your grumbling."
        "She makes sure to go over what you'll need to know for the upcoming exams."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah think you might get a question like this one on yer test. . ."
        "She points to a particular question."

        $ Rogue.change_face("confused1", mouth = "smirk")

        "After doing the work, you think you've found the answer."
        ch_Player "Okay. . . is it choice A?"
        
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Sorry, sugar, it's choice B."
        "She points out where you went wrong and makes sure you understand how to do it properly."

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        "The rest of the lesson goes by quickly, you were already pretty familiar with the material."

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        "[Rogue.name] helps you clean everything up, but she seems a bit anxious. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "So. . . sugar, ah was wonderin'. . ."
        ch_Player "If you could touch my hands again?"

        $ Rogue.change_face("worried2", blush = 2)

        ch_Rogue "Yes. . ." 

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

        call take_off(Rogue, "gloves") from _call_take_off_14

        "You put your hand out, and she eagerly takes her glove off." 

        $ Rogue.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 2) 

        "After a long moment, she pulls away."

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "Thanks. . ."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Don't be afraid to ask."

    $ ongoing_Event = False

    return