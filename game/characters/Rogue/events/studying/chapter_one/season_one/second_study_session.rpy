init python:

    def Rogue_chapter_one_season_one_second_study_session():
        label = "Rogue_chapter_one_season_one_second_study_session"

        conditions = [
            "chapter == 1 and season == 1",
            "Rogue.History.check('studied_with_Player', tracker = 'season') == 1",
            "Player.studying == Rogue and Rogue.studying"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_one_second_study_session:
    $ ongoing_Event = True

    $ Rogue.change_face("happy")

    ch_Rogue "Ah'll help ya get everythin' set up."

    $ Rogue.change_face("smirk2")

    ch_Player "Thanks, [Rogue.name]."
    "She helps you organize all the notes and study materials you'll need for the session."

    $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

    "You exchange some small talk, but notice [Rogue.name] is quite picky with how things are organized."
    "Nevertheless, it only takes a couple minutes."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "That oughta do it." 
    "As you get on the bed with your papers spread out in front of you, you notice [Rogue.name] lies down directly next to you, close enough for your shoulders to touch."

    $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

    "You spend the next couple hours reviewing the material you learned in class and revisiting specific topics on the study guide."

    $ Rogue.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1)

    "Throughout the session, you notice her continuously sneaking glances at your hands."

    menu:
        extend ""
        "Ya'know, you can touch my hands again if you want. . .":
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_1072
            call change_Girl_stat(Rogue, "trust", medium_stat)

            ch_Player "I don't mind." 
            
            $ Rogue.change_face("worried3", blush = 2) 
            
            pause 1.0 
            
            $ Rogue.change_face("worried1", eyes = "right", blush = 1)

            ch_Rogue "Ah'm. . . sorry, hon'." 
            ch_Player "Nothing to be sorry about." 
            
            $ Rogue.change_face("worried1", blush = 1) 
            
            ch_Rogue "But, did ya really mean it?" 
            
            ch_Rogue "Ya don't mind?" 
        "Did you want to touch my hands again? Heh, they are nice right?":
            call change_Girl_stat(Rogue, "love", medium_stat)
            
            $ Rogue.change_face("worried3", blush = 2) 
            
            ch_Player "I should totally be a hand model." 
            
            $ Rogue.change_face("worried1", mouth = "smirk", eyes = "right", blush = 1)

            ch_Rogue "Yeah, they are nice. . ." 
            
            $ Rogue.change_face("worried1", blush = 1) 
            
            ch_Rogue "Ah'm sorry for starin'. . ." 
            ch_Rogue "But you don't mind if ah touch?" 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1073
        "Really? You're staring at my hands again?":
            call change_Girl_stat(Rogue, "love", -medium_stat)
            call change_Girl_stat(Rogue, "trust", -small_stat)

            $ Rogue.change_face("worried3", blush = 2) 
            
            ch_Player "You want to touch them that badly?" 
            
            $ Rogue.change_face("worried1", eyes = "down", blush = 2)

            ch_Rogue "Ah'm sorry, [Player.first_name]."
            ch_Rogue "Ah'll stop if it bothers you. . ." 
            
            $ Rogue.change_face("sad", eyes = "right", blush = 1) 
            
    menu:
        extend ""
        "I don't mind at all.":
            call change_Girl_stat(Rogue, "love", small_stat) from _call_change_Girl_stat_1075
        "I guess it's fine.":
            ch_Player "You can touch them."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    "You put your hand out for her to touch."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1) 

    ch_Rogue "Thank you. . ."
    
    call take_off(Rogue, "gloves") from _call_take_off_7
    
    "[Rogue.name] takes her glove off and tentatively reaches out."

    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 2)

    "As your hands touch, she shudders slightly."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    "She holds on for a few moments, before pulling away." 

    $ Rogue.change_face("pleased2", blush = 2)

    ch_Player "Your hands are really soft."

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue ". . . thanks." 

    $ Rogue.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Player "Okay, back to studying." 

    $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

    "You finish going through some practice questions, but get to one you can't figure out."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "Hey, [Rogue.name], how do you do this one?"
    "You point to a particular question."

    $ Rogue.change_face("smirk2")

    ch_Rogue "That one's a bit confusin'."
    "She briefly explains the process to arrive at the correct answer."
    ch_Rogue "That's why the answer is choice A."
    "You finish up the session shortly after, and [Rogue.name] helps you put away all the study materials."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thanks again."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 2)

    ch_Rogue "For lettin' me. . . touch you." 
    ch_Player "No problem, but feel free to ask next time." 

    $ Rogue.change_face("worried2", blush = 3)

    ch_Rogue "Maybe. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah'll be seein' ya."
    ch_Player "Bye."
        
    call remove_Characters(Rogue) from _call_remove_Characters_261

    if Player.location == Rogue.home and Rogue not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_357

    $ ongoing_Event = False

    return