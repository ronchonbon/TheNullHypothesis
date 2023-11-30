init python:

    def Rogue_chapter_one_season_one_first_training_session():
        label = "Rogue_chapter_one_season_one_first_training_session"

        conditions = [
            "chapter == 1 and season == 1",

            "not Rogue.History.check('trained_with_Player', tracker = 'season')",
            
            "Player.behavior == 'training' and Rogue in Player.behavior_Partners and Rogue.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_one_first_training_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1")

    ch_Rogue "Did ya really wanna train together?" 

    $ Rogue.change_face("worried1", mouth = "smirk")

    menu:
        extend ""
        "Of course, I wouldn't ask if I weren't serious.":
            call change_Companion_stat(Rogue, "love", medium_stat) from _call_change_Companion_stat_1617
            call change_Companion_stat(Rogue, "trust", medium_stat) from _call_change_Companion_stat_1618

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Ah know. . ."
        "It couldn't be any worse than training with [Laura.name], that's for sure.":
            call change_Companion_stat(Rogue, "love", small_stat) from _call_change_Companion_stat_1619
            call change_Companion_stat(Rogue, "trust", small_stat) from _call_change_Companion_stat_1620

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Ah reckon yer not wrong. . ."
        "Why, is there something about all this that you're not telling me?":
            call change_Companion_stat(Rogue, "love", -small_stat) from _call_change_Companion_stat_1621

            $ Rogue.change_face("worried2")

            ch_Rogue "No, ah swear there's nothin'!"

    $ Rogue.change_face("worried1")

    ch_Rogue "It's just. . ."

    $ Rogue.change_face("sad", eyes = "right")

    ch_Rogue "Ah've never really been able to spar with anyone cuz of my power."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Player "You know that's not a problem for me." 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Yeah, but. . . ah just wanted to make sure." 
    ch_Player "I appreciate it, but seriously, don't worry."

    $ Rogue.change_face("smirk1")

    ch_Player "Come on, let's warm up."

    $ fade_to_black(0.4)

    "You both spend some time stretching and getting ready for the session."

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("neutral")

    ch_Player "So, [Laura.name]'s been teaching me some techniques."

    if Laura.History.check("trained_with_Player", tracker = "season") >= 3:
        ch_Player "After getting beaten up by her so many times, I think I might be getting the hang of it."
    else:
        ch_Player "To be honest, I still kinda suck and should probably train with her more, but I might've learned a thing or two."

    ch_Player "Wanna work through some of it together?"

    $ Rogue.change_face("pleased1")

    ch_Rogue "Sure! Ah'll do anythin' ya want." 

    if Rogue in Partners:
        $ Rogue.change_face("worried2") 
        
        ch_Rogue "Well. . . not anythin'. . ." 
        
        $ Rogue.change_face("smirk2", eyes = "right", mouth = "lipbite") 
        
        ch_Rogue "At least not 'round here. . ."
    else:
        $ Rogue.change_face("worried2") 
        
        ch_Rogue "Ah didn't. . . mean it like that. . ." 
        
        $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

    $ Rogue.change_face("smirk2")

    "You spend the next couple hours practicing with Rogue."
    "Despite being relegated to training alone, you can tell she's put some serious work in."
    "She's way better than you."
    "You try to pass on some of the knowledge [Laura.name] has been drilling into you, but in the end, [Rogue.name] ends up doing most of the teaching."
    "She just seems overjoyed by the fact that she can finally spar with another person."

    $ Rogue.change_face("happy")

    "She also seems to find any excuse to touch you and correct your form. . ."

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Rogue "Thanks, [Rogue.Player_petname]. . . for lettin' me train with you." 
    ch_Rogue "You don't know how much ah've been wantin' to."
    ch_Player "Of course!"
    ch_Player "Heh, you ended up doing most of the teaching anyway."
    ch_Player "It was substantially less painful than doing it with [Laura.name] too. . ." 

    $ Rogue.change_face("sly")

    ch_Rogue "Ah can imagine."

    $ Rogue.change_face("smirk2")

    ch_Player "I would offer to try and help you figure out your powers. . ." 

    $ Rogue.change_face("worried1")

    ch_Player "But I still can't even figure out my own ability yet."
    ch_Rogue "It's alright, [Rogue.Player_petname]."  

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "You just focus on figurin' out your own stuff for now." 
    ch_Rogue "Ah wouldn't want to make things even more confusin' for ya." 

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Player "One day, though. . . I want to help."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Yeah. . . one day."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "See ya later, [Rogue.Player_petname]."

    call remove_Characters(Rogue) from _call_remove_Characters_200

    $ ongoing_Event = False

    return