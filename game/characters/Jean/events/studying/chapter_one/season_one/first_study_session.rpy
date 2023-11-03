init python:

    def Jean_chapter_one_season_one_first_study_session():
        label = "Jean_chapter_one_season_one_first_study_session"

        conditions = [
            "season == 1",
            "not Jean.History.check('studied_with_Player', tracker = 'season')",
            "Player.studying == Jean and Jean.studying"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_one_first_study_session:
    $ ongoing_Event = True

    $ Jean.change_face("happy")

    ch_Jean "Alright, you gonna help me set all this stuff up?" 
    ch_Player "Sure." 

    $ Jean.change_face("smirk2")

    "You spend the next several minutes organizing the papers and books for the session."

    $ Jean.change_face("smirk2", eyes = "down")

    "[Jean.name] is very particular about where she wants things to go, so it takes a fair bit of time."
    "She also not so subtly checks you out while you help."

    $ Jean.change_face("smirk1", eyes = "right")

    pause 1.0

    $ Jean.change_face("smirk2", eyes = "down", blush = 1) 

    pause 1.0

    $ Jean.change_face("smirk2", blush = 1) 

    ch_Jean "Good, now scoot over."
    "You both hop on the bed, and she scoots right up next to you."
    "Apparently disregarding your personal space. . ."

    $ Jean.change_face("smirk2", eyes = "down", blush = 1) 

    "As you go over the course material, you begin to realize [Jean.name] must either have a photographic memory or has studied these topics to death."
    "Although, unlike [Rogue.name] who seems to be a natural teacher, [Jean.name] isn't quite so effortlessly helpful." 

    $ Jean.change_face("confused1")

    "Sure, she knows the answer to everything, but it's like she assumes you should as well."
    ch_Jean "Really, [Jean.Player_petname]?"
    ch_Jean "You didn't know how to do that one?"

    $ Jean.change_face("smirk2")

    ch_Jean "Here. . ."
    "She flips directly to the exact page in the textbook as she explains the correct answer."
    "In case you thought it was a fluke, she proceeds to cite the relevant information perfectly from memory, without even glancing down."
    "And then she does it for the next three questions as well."

    menu:
        extend ""
        "You know exactly where to look. . . amazing.":
            $ Jean.change_face("pleased2") 
            
            pause 1.0 
            
            $ Jean.change_face("smirk2", eyes = "right")

            ch_Jean "You think so?" 
            
            call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_131 
            call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_132
        "Holy shit. . . are you a genius or something?":
            $ Jean.change_face("smirk2", eyes = "right") 
            
            pause 1.0 
            
            $ Jean.change_face("sly") 

            ch_Jean "Well. . . a few people have told me my IQ is pretty high. . ." 
            
            call change_Girl_stat(Jean, "love", 10) from _call_change_Girl_stat_133
        "What the hell. . . is your entire life just spent studying and memorizing. . . ?":
            $ Jean.change_face("appalled1") 
            
            pause 1.0 
            
            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "No!" 
            ch_Jean "Of course not. . ." 
            ch_Jean "I. . . do other things. . ." 
            
            call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_134

    $ Jean.change_face("worried1")

    ch_Jean "I just. . . take my studies really seriously. . . ya'know?"
    ch_Player "It is impressive, to say the least."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "I know, right?"

    $ Jean.change_face("sly")

    ch_Jean "Now, [Jean.Player_petname], enough stalling."

    $ Jean.change_face("smirk2")

    ch_Jean "Okay, so this one. . ."
    ch_Player "Is the answer not choice B?"
    ch_Jean "Nope, it's A."
    "The rest of the session mainly consists of [Jean.name] systematically exposing all your academic inadequacies and proceeding to lowkey flaunt her knowledge as she does her best to fix them."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "I think we should stop here."
    ch_Jean "I can tell your brain is getting a bit burnt out."
    ch_Player "Yeah. . . you're not wrong."

    $ Jean.change_face("smirk2", mouth = "lipbite")

    pause 1.0

    $ Jean.change_face("worried1", mouth = "smirk")

    if Player.location == Jean.home:
        ch_Jean "You can hang out for a bit if you want. . ."

    $ ongoing_Event = False

    return