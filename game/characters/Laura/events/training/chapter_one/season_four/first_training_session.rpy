init python:

    def Laura_chapter_one_season_four_first_training_session():
        label = "Laura_chapter_one_season_four_first_training_session"

        conditions = [
            "chapter == 1 and season == 4",

            "Jean.History.check('trained_with_Player', tracker = 'season')",

            "not Laura.History.check('trained_with_Player', tracker = 'season')",
            
            "Player.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_four_first_training_session:
    $ ongoing_Event = True
    
    if Player.training != Laura:
        "You're still not ready to train on your own."
        "[Laura.name] will want to hear about the progress you've been making with [Jean.name]."
        "As if summoned by your thoughts, you hear footsteps approaching from behind."
        
        call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_115
        
        if Laura.History.check("said_no_to_training", tracker = "recent"):
            $ Laura.change_face("suspicious1") 

            ch_Laura "I didn't mean for you to start anyways."
            ch_Laura "Fine, I'm here."

        $ Player.training = Laura

        call remove_everyone_but(Laura) from _call_remove_everyone_but_2

    $ Laura.change_face("neutral", eyes = "squint") 

    ch_Laura "What's with that look?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I don't care about what happened."
    ch_Laura "They tried to kill you."
    ch_Laura "You would've been entirely justified in returning the favor." 

    menu:
        extend ""
        "No, [Laura.name]. We have to be better than that.":
            ch_Player "That's the easy way out." 
            
            $ Laura.change_face("furious")
            
            if Player.History.check("told_Laura_protesters_got_what_they_deserved_during_mutant_hate"):
                ch_Laura "So now you're suddenly all self righteous?" 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_405 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_406
            else:
                ch_Laura "So people who kill are lesser, in your opinion?" 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_407 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_408
        "I can't just kill people! The fact that it would've been so easy terrifies me.":
            $ Laura.change_face("angry1")
            
            if Player.History.check("told_Laura_protesters_got_what_they_deserved_during_mutant_hate"):
                ch_Laura "Where'd your spine go?" 
                ch_Laura "Killing is necessary at times." 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_409
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_410
            else:
                ch_Laura "This is reality, you need to get over it." 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_411 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_412
        "I know. You're right, maybe they didn't deserve mercy.":
            $ Laura.change_face("angry1", eyes = "left")

            if Player.History.check("told_Laura_protesters_got_what_they_deserved_during_mutant_hate"):
                ch_Laura "Everyone at this goddamn school thinks otherwise. . ." 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_413 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_414
            else:
                ch_Laura "Changed your mind so easily?" 
                ch_Laura "Everyone at this goddamn school thinks otherwise. . ." 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_415 
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_416

    ch_Player "I just-"

    $ Laura.change_face("furious", eyes = "left")

    "She interrupts you."
    ch_Laura "I've killed people before."

    $ Laura.change_face("angry1")

    ch_Laura "A lot. . . of people." 
    ch_Laura "Probably hundreds, by my tenth birthday."
    ch_Laura "Many of whom certainly did not deserve it."
    ch_Player ". . ."

    menu:
        extend ""
        "You were just a child, that's on the people who controlled you.":
            $ Laura.change_face("furious", eyes = "left")

            ch_Laura "I was still the one who did the killing." 
            ch_Laura "But apparently, now I can make my own decisions on who to kill." 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_418
        "Fuck. . . I'm sorry you had to go through that.":
            $ Laura.change_face("angry1", eyes = "left")

            ch_Laura "Now that I'm in control. . ." 
            ch_Laura "Anyone who tries to harm you will. . ." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_417
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_419
        ". . .":
            $ Laura.change_face("furious")

            "She punches you in the shoulder, hard." with small_screenshake
            ch_Player "Ow! The hell was that for?" 
            ch_Laura "Aren't you going to say anything?" 
            ch_Laura "Call me a monster like everyone else?" 
            
            $ Laura.change_face("confused1") 
            
            ch_Player "Of course not." 
            ch_Player "How are you to blame, when you were a child?"
            ch_Player "You didn't want any of that." 
            
            $ Laura.change_face("angry1", eyes = "left") 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_420

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "Let's talk about something else."
    ch_Player "Well. . ."

    $ Laura.change_face("angry1")

    ch_Laura "Yes?"
    ch_Player "I was working with [Jean.name] earlier and managed to figure something out."
    ch_Player "It's not easy, but I can somewhat control how strongly my power asserts itself now."
    ch_Player "Doesn't have to be all or nothing anymore."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "Then we will put it to the test."
    ch_Laura "I need to punch something right now. . ."

    # $ Laura.left_arm_pose = 2

    ch_Player "Exactly what I had in mind." 

    $ Player.power = 25
    
    "With a mental effort, you let the power loose, but you keep it on a tight leash."
    "The boost is barely noticeable, as you focus on using the smallest amount possible."
    "Your control is tenuous at best, and half your concentration is focused on keeping it down."
    "[Laura.name] hesitates and doesn't attack right away."

    $ Laura.change_face("angry1")

    ch_Laura "More."
    ch_Player "Wha-"
    ch_Laura "My regeneration is still keeping up, I'll tell you when to stop." 

    $ fade_to_black(0.4)

    $ Player.power = 50

    "With much difficulty, you manage to match your absorption with her regeneration."
    "Some quick tests show that now neither of you has an advantage in strength or speed."
    "[Laura.name] grins like you've never seen before and attacks."

    $ count = 7

    while count > 0:
        $ dice_roll = renpy.random.randint(1, 3)

        $ x = renpy.random.random()*0.7 + 0.15
        $ y = renpy.random.random()*0.7 + 0.15

        if dice_roll == 1:
            show expression "images/effects/green_smack.webp" as smack onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0
        elif dice_roll == 2:
            show expression "images/effects/crack.webp" as crack onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0
        elif dice_roll == 3:
            show expression "images/effects/pow.webp" as pow onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0

        $ renpy.pause(renpy.random.random(), hard = True)

        $ count -= 1

    $ fade_in_from_black(0.4)

    $ Laura.change_face("angry1", mouth = "smile")
    # $ Laura.left_arm_pose = 1

    $ Player.power = 25

    "She still absolutely demolishes you based on skill and experience alone, but her grin remains."
    
    $ Player.power = 0

    "You, on the other hand, are thoroughly drained from the drawn out sparring session."
    ch_Laura "That is the first time I've ever fought someone on a level playing field."

    $ Laura.change_face("smirk2")

    ch_Player "*huff* I thought. . . *huff* you fought Logan once. . . *huff*"
    ch_Laura "He's old and slow."
    ch_Laura "Doesn't count."
    ch_Laura "As a reward, you get two minutes to rest."
    ch_Player "*huff* But that's the normal amount. . . *huff*"

    $ Laura.change_face("sly")

    "After you catch your breath, you notice a bead of sweat on [Laura.name]'s forehead."
    "That sparring session must've lasted longer than you thought. . ."
    "She still shows no mercy and pushes you through the remaining workouts, but the rest of the session goes by quickly."

    $ Laura.change_face("smirk2")

    ch_Laura "That was a decent warm up. . . for once."
    ch_Laura "I expect you to be available whenever I need one."

    call remove_Characters(Laura) from _call_remove_Characters_126

    "She leaves you gasping for breath."
    "Your new power - and control over it - only seem to bring more pain and suffering to your life. . ."

    $ ongoing_Event = False

    return