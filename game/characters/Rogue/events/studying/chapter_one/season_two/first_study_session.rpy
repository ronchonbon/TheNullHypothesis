init python:

    def Rogue_chapter_one_season_two_first_study_session():
        label = "Rogue_chapter_one_season_two_first_study_session"

        conditions = [
            "season == 2",
            "not Rogue.History.check('studied_with_Player', tracker = 'season')",
            "Player.studying == Rogue and Rogue.studying"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_two_first_study_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "down")

    "Without even saying anything, [Rogue.name] just starts setting up all the textbooks and study guides."
    "You move to help, but. . ."

    $ Rogue.change_face("worried2")

    ch_Rogue "Don't bother yerself, darlin', ah got it."

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "Just let me take care of it. . ."

    if Rogue.petname not in ["Anna Marie"]:
        $ temp = Rogue.petname.capitalize()
    else:
        $ temp = Rogue.petname

    ch_Player "[temp], what's going on?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Nothin', ah just wanna do somethin' for ya for once."

    $ Rogue.change_face("worried1")

    ch_Player "For once?"
    ch_Player "You do stuff for me all the time."
    ch_Rogue "Please, darlin', just relax while ah set this up. . ."
    ch_Player "Alright. . ."

    $ Rogue.change_face("worried1", eyes = "down")

    "You sit down on the bed and chat with [Rogue.name] a bit as she gets things organized."
    "She's acting very deferential. . . even more so than usual."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "That oughta do it."
    ch_Rogue "Ya ready to get started?"

    if Rogue.petname not in ["Anna Marie"]:
        $ temp = Rogue.petname.capitalize()
    else:
        $ temp = Rogue.petname

    menu:
        extend ""
        "Hey, I can tell something's off. Talk to me.":
            $ Rogue.change_face("worried2") 
            
            pause 1.0 
            
            $ Rogue.change_face("worried1", eyes = "right")

            ch_Rogue "Ah'm sorry for bein' like this, [Rogue.Player_petname]." 
            
            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_1081 
            call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_1082
        "[temp], are you really okay? If something's going on, you can tell me.":
            $ Rogue.change_face("worried1", eyes = "right")

            ch_Rogue "Ah'm fine, really."
            
            $ Rogue.change_face("worried1") 
            
            ch_Rogue "And ah'm sorry, but. . ." 
            
            call change_Girl_stat(Rogue, "love", 10) from _call_change_Girl_stat_1083
        "Okay, seriously, what the hell is going on with you?":
            $ Rogue.change_face("worried2") 
            
            pause 1.0 
            
            $ Rogue.change_face("confused1", eyes = "right")

            ch_Rogue "Nothin's goin' on!" 
            ch_Rogue "It ain't about me." 
            
            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_1084
            call change_Girl_stat(Rogue, "trust", -5) from _call_change_Girl_stat_1085

    $ Rogue.change_face("worried2")

    ch_Rogue "It's about you. . ."

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Player "About me?"
    ch_Rogue "Ah've just been real worried about ya lately."
    ch_Rogue "After everythin' that happened, ya haven't really been reactin' the way ah'd expect. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "If ah didn't know ya, ah would never have thought ya nearly got killed twice in the past few months."
    ch_Rogue "Ah know ya must be hurtin' on the inside, even if ya don't show it."
    ch_Player "I. . ."
    ch_Rogue "Ya shouldn't bottle everythin' up, [Rogue.Player_petname]."
    ch_Rogue "And. . . ah just wanted to try 'n make things a bit easier for ya. . ."

    menu:
        extend ""
        "I appreciate the thought, but that's not what I want from you.":
            $ Rogue.change_face("worried1", eyes = "down")
        "That's really sweet. . . but please don't worry so much about me.":
            $ Rogue.change_face("worried1")
        "I don't know why you thought that's what I want from you.":
            $ Rogue.change_face("confused1")

    $ Rogue.change_face("worried2")

    ch_Player "I don't want special treatment."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Just spending time with you and our friends. . . that's what I want."
    ch_Player "The way I cope with things. . ."

    $ Rogue.change_face("worried1")

    ch_Player "I need the distraction, and I just want things to feel normal."
    ch_Player "Anything else just reminds me about all the bad stuff."
    ch_Rogue "Ah'm sorry for assumin'."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "And ah think ah know how ya feel."
    ch_Rogue "Ah'll spend as much time with you as ya need, studyin' or otherwise."
    ch_Player "Thank you, I really appreciate it."
    ch_Rogue "And, if ya ever do wanna talk about yer feelin's, ah'll be here."
    ch_Rogue "But, for now, ah think we should get to that distraction."

    $ Rogue.change_face("smirk2")

    ch_Player "I'd like that."

    $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

    "[Rogue.name] plops down onto the bed next to you and leans into your shoulder comfortingly."
    "With the dour mood of the previous conversation, you can tell she does her best to bring it back up."
    "It doesn't take long, and spirits are lifted as you go through some tricky calculus homework, exchanging the occasional small talk."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Player "Okay I'm pretty sure I did the work right on this one."

    $ Rogue.change_face("confused1", mouth = "smirk", eyes = "down")

    "You point to the last homework question."
    "[Rogue.name] reads it over, but doesn't say anything, as you consider the answer."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "Okay, I'm pretty sure the answer is 47."

    if Player.scholarship == "academic":
        $ Rogue.change_face("happy") 
        
        ch_Rogue "Great job, [Rogue.Player_petname]!"
    else:
        $ Rogue.change_face("worried1", mouth = "smirk") 
        
        ch_Rogue "Oh, so close, [Rogue.Player_petname]. . ." 
        ch_Rogue "The answer is 49."

    $ Rogue.change_face("smirk2", eyes = "down")

    "As things finish up, you help her put everything away."

    $ Rogue.change_face("smirk2")

    ch_Rogue "That was productive."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm sorry about the beginnin'. . ."
    ch_Player "It's okay, [Rogue.petname]."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Really."

    call change_Girl_stat(Rogue, "love", 10) from _call_change_Girl_stat_1086

    $ ongoing_Event = False

    return