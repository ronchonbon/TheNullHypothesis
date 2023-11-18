init python:

    def Laura_chapter_one_season_one_training_sessions():
        label = "Laura_chapter_one_season_one_training_sessions"

        conditions = [
            "chapter == 1 and season == 1",

            "Laura.History.check('trained_with_Player', tracker = 'season') >= 4",
            
            "Player.training == Laura and Laura.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_one_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Player "I'm ready to start." 

        $ Laura.change_face("confused1")

        ch_Laura "You say that frequently. . . but you're still always surprised by the intensity." 

        $ Laura.change_face("neutral")

        $ fade_to_black(0.4)

        "She has a point and, after today's warmup beats the crap out of you, maybe it wasn't the best choice of words."
        "Today the focus is on defense."
        "Well, it's more like you don't have a choice but to defend yourself if you don't want to get the crap kicked out of you."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("smirk1")

        "You're making pretty good progress with the techniques and maybe get hit less than last time."
        "It's hard to tell when it happens so often."
        "The session ends as usual, with an abundance of pain and suffering."

        $ Laura.change_face("neutral")

        "You endure it, and it's as if you can almost see [Laura.name] make a mental note for next time to be even harder."
        ch_Laura "Enough, you are done for today." 
        ch_Player "*huff* Won't argue with that. . . *huff*"

        call remove_Characters(Laura) from _call_remove_Characters_133
        
        "She goes to finish training on her own."
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "Why are you limping?" 
        ch_Player "Definitely not because I'm still sore from last time. . ." 

        $ Laura.change_face("neutral", eyes = "squint")

        $ fade_to_black(0.4)

        "[Laura.name] doesn't seem too worried, and the warm up is just as torturous as ever."
        "She was right not to be worried, and you actually feel less stiff afterwards."
        "Today you work on a combination of techniques."
        "Your awareness of your own body is getting better, but still pretty crappy."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("angry1")

        "You get beat down pretty hard, but only because [Laura.name] is picking up the pace now that you're actually improving."

        $ Laura.change_face("angry2")

        "The workout to end the session doesn't seem quite so bad this time, but your entire body still feels like jelly in the end."

        $ Laura.change_face("neutral")

        ch_Laura "Fine, we're done."
        ch_Player "Have a good workout." 

        $ Laura.change_face("confused1")

        ch_Laura "Thanks. . ."

        call remove_Characters(Laura) from _call_remove_Characters_134

        "[Laura.name] leaves to go do her own thing."
    elif dice_roll == 3:
        "You're a bit fidgety."

        $ Laura.change_face("confused1")

        ch_Laura "What are you doing?" 
        ch_Player "Just psyching myself up for the pain." 
        ch_Laura "Okay. . ." 

        $ Laura.change_face("neutral")

        "Psyching yourself up didn't help, and the warm up sucks as usual."

        $ fade_to_black(0.4)

        "Today's focus is offense, and you try your best not to make a fool of yourself."
        "You're actually starting to get somewhat competent, and you notice [Laura.name] has to go faster than usual in order to not get hit."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("angry1")

        "Of course this just means things will only get more difficult as you continue to improve."
        "You thought the workout at the end wouldn't be so bad today. . ." 
        ". . . until you fall on your face." with small_screenshake

        $ Laura.change_face("confused1")

        "You should really just start assuming it's always going to be worse than last time."

        ch_Laura "You should really stop falling like that. . ."
        ch_Player "*huff* I wish. . . *huff*"

        call remove_Characters(Laura) from _call_remove_Characters_135

        "You manage to get back up, and [Laura.name] leaves to go workout on her own."
    elif dice_roll == 4:
        ch_Laura "Time to start."

        $ fade_to_black(0.4)

        "You're feeling pretty good today and, despite the warm up intensity, it goes more smoothly than usual."
        "[Laura.name] makes you focus on defense again, and you're doing noticeably better than normal."
        "She picks up the pace, and you struggle, yet still manage to hold out."
        "Things are looking up, until you start to feel yourself crashing."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("neutral", eyes = "squint")

        "The final workout isn't substantially harder than last time, but you feel way more fatigued than normal."
        "You barely crawl through the exercises."

        ch_Player "*huff* And I was doing so well at the start. . . *huff." 

        $ Laura.change_face("angry1")

        ch_Laura "You need to learn how to pace yourself."
            
        call remove_Characters(Laura) from _call_remove_Characters_136
        
        "She leaves to finish working out on her own."

    $ ongoing_Event = False

    return