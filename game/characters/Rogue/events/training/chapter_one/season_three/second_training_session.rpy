init python:

    def Rogue_chapter_one_season_three_second_training_session():
        label = "Rogue_chapter_one_season_three_second_training_session"

        conditions = [
            "chapter == 1 and season == 3",

            "Rogue.History.check('trained_with_Player', tracker = 'season') == 1",
            
            "Player.training == Rogue and Rogue.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_three_second_training_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk") 

    ch_Player "You don't look very happy to see me. . ."

    $ Rogue.change_face("worried2")

    ch_Rogue "Ah just. . ."
    ch_Rogue "Last time we trained was all tense and everythin'."

    $ Rogue.change_face("worried1")

    ch_Player "Don't worry, [Rogue.petname]."
    ch_Player "That was important. . . I think, for both of us."

    $ Rogue.change_face("worried1", mouth = "smirk") 

    ch_Rogue "So yer not mad?"

    menu:
        extend ""
        "Of course I'm not mad.":
            $ Rogue.change_face("worried2") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_671 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_672
        "Definitely not mad. Worried about you, if anything.": 
            $ Rogue.change_face("worried1", eyes = "down") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_673
        "Just don't lie again and I'll be fine.":
            $ Rogue.change_face("worried1", eyes = "right")

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_674 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_675

    $ Rogue.change_face("worried1")

    ch_Player "And, why would I be mad at you for having completely justifiable concerns?"

    $ Rogue.change_face("confused1", mouth = "smirk") 

    ch_Rogue "Justifiable?"
    ch_Player "Well. . . if it bothered you that much. . . I'm sure they were justifiable. . ."
    ch_Player "{i}Ahem{/i}. . ."

    $ Rogue.change_face("worried1", mouth = "smirk") 

    ch_Rogue "Thanks for bein' so understanding."
    ch_Player "On a better note, since I was able to figure out how to get some control over my powers, maybe I could try helping you do the same?"

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "My. . . difficulties aren't so simple. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah appreciate the thought, but it's probably a waste of time."

    $ Rogue.change_face("worried3")

    ch_Rogue "Not because yer useless or nothin'!"
    ch_Rogue "Just don't think anybody could help."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah have this mental block. . ."
    ch_Rogue "Ah doubt even [Charles.name] or [Jean.name] could fix it, if they tried rummagin' around in my head."
    ch_Player "Hey, I suggested it just as much to help myself, as I did to help you."

    $ Rogue.change_face("confused1")

    ch_Player "It'll be good practice for me, plus, who knows, it might help you too."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Alright, [Rogue.Player_petname]."
    ch_Rogue "Might as well."

    $ fade_to_black(0.4)

    "You spend a while trying to form your thoughts and feelings into words, as you attempt to explain how you control your power."
    "Unfortunately, you barely have a grasp of the concept yourself, and [Rogue.name] doesn't get too much out of it."
    "She doesn't go into detail, but mentions how her issue isn't just lack of knowledge or practice, but instead stems from some kind of trauma."
    "She's been dealing with it for years, with no progress to show for it."
    "At least the whole process helped you understand your own power a bit more."

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah'm sorry, doesn't seem like that did much for me. . ."
    ch_Player "Don't apologize."
    ch_Player "We knew it was a long shot."
    ch_Player "I think I got a bit out of it."
    ch_Player "So it wasn't a complete waste of time."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "It's a bit interestin', though."
    ch_Rogue "The way you described how yer own power feels. . ."

    $ Rogue.change_face("confused1")

    ch_Rogue "Mine doesn't feel nothin' like that at all." 

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "I am pretty special, glad you agree."

    $ Rogue.change_face("sly")

    ch_Rogue "Very funny, darlin'."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "But ah guess that means ya might not be able to help me much. . ."
    ch_Player "No harm in trying, right?"
    ch_Rogue "Right."
    ch_Rogue "Wanna get into some sparrin' to finish things up?"
    ch_Player "Sure thing."

    $ Rogue.change_face("smirk1")

    "You make sure your nullification is on before getting into the sparring."
    "That feeling from last time. . . you're not keen on experiencing whatever that was again."
    "The mood is much less tense than last time as well, and things feel like they're back to normal, as you both have a good time with the training."

    $ Rogue.change_face("sly")

    ch_Rogue "Ah can tell yer still holdin' back on my account."
    ch_Player "Sorry. . . if I don't. . ."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Don't you worry none."
    ch_Rogue "One day you won't have too."
    ch_Player "I'm looking forward to it."

    $ Rogue.change_face("happy")

    ch_Rogue "Ya better be ready when the time comes."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'll see you later, alright?"
    ch_Player "Definitely." 

    call remove_Characters(Rogue) from _call_remove_Characters_203

    $ ongoing_Event = False

    return