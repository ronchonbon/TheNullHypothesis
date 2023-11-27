init python:

    def Jean_chapter_one_season_one_exam_freakout_setup():
        label = "Jean_chapter_one_season_one_exam_freakout_setup"

        conditions = [
            "Jean.location not in ['hold', Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Jean_chapter_one_season_one_exam_freakout'].completed",

            "time_index not in Jean.schedule.keys()",

            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",
            "weather != 'rain'",    
            "clock == Player.max_stamina",

            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_chapter_one_season_one_exam_freakout_setup:
    call send_Characters(Jean, "bg_classroom", behavior = "in_class") from _call_send_Characters_329
    
    return

init python:

    def Jean_chapter_one_season_one_exam_freakout():
        label = "Jean_chapter_one_season_one_exam_freakout"

        conditions = [
            "Player.destination == 'bg_classroom'",
            
            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",
            "weather != 'rain'",    
            "clock == Player.max_stamina",
            
            "Jean.location == 'bg_classroom'",
            "Jean.behavior == 'in_class'",

            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_classroom": [
                "Player.location != 'bg_classroom'",
                
                "chapter == 1 and season == 1",

                "weekday < 5 and time_index < 2",
                "weather != 'rain'",    
                "clock == Player.max_stamina",
                
                "Jean.location == 'bg_classroom'",
                "Jean.behavior == 'in_class'",

                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Jean_chapter_one_season_one_exam_freakout:
    $ ongoing_Event = True

    $ Present = get_Present(location = "bg_classroom")

    python:
        for C in Present:
            if C != Jean:
                C.location = "nearby"

    call set_the_scene(location = "bg_classroom", show_Characters = False) from _call_set_the_scene_54

    "You walk through the class room doors to see many more people than you were expecting."
    "Some seem to have just arrived, like you, but others are packing their things and hastily heading for the door."
    
    call set_the_scene(location = "bg_classroom", fade = False) from _call_set_the_scene_55

    "You spot [Jean.name] sitting at a desk with her head in her hands before getting up to leave herself."

    menu:
        extend ""
        "Check on [Jean.name]":
            pass
        "Leave her to her thoughts":
            "You keep your distance."

            call remove_Characters(Jean) from _call_remove_Characters_320

            $ EventScheduler.Events["Jean_chapter_one_season_one_exam_freakout"].completed = False
            $ EventScheduler.Events["Jean_chapter_one_season_one_exam_freakout"].completed_when = 1e8

            $ EventScheduler.Events["Jean_chapter_one_season_one_exam_freakout"].counter = 0

            $ ongoing_Event = False

            return

    $ Jean.change_face("angry1", eyes = "down")

    ch_Player "[Jean.name]?"

    $ Jean.change_face("perplexed")

    ch_Jean "YOU!"
    ch_Player "Wha-"

    $ Jean.change_face("worried3")

    pause 0.5

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite")

    ch_Jean "Sorry, I mean, hey. . ."

    $ Jean.change_face("worried1")

    ch_Jean "Didn't mean to snap at you, just stressed about that exam."
    ch_Player "Ah, so that's why there's so many people here."

    menu:
        extend ""
        "But why are you stressed? The exam's over - knowing you, you probably aced it.":
            call change_Girl_stat(Jean, "love", medium_stat) from _call_change_Girl_stat_107
            call change_Girl_stat(Jean, "trust", small_stat) from _call_change_Girl_stat_108

            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "UGH! Not this time I didn't. . ."
        "Don't worry, no hard feelings. I'm sure you aced the exam anyway.":
            call change_Girl_stat(Jean, "love", large_stat) from _call_change_Girl_stat_109
            
            $ Jean.change_face("angry1", mouth = "smirk", eyes = "right")

            ch_Jean "Ha, yeah right. This time was different. . ."
        "It's fine I guess, not like it's my fault. You probably aced the exam anyway.":
            call change_Girl_stat(Jean, "love", -small_stat) from _call_change_Girl_stat_110
            call change_Girl_stat(Jean, "trust", small_stat) from _call_change_Girl_stat_111
            
            $ Jean.change_face("confused1", mouth = "smirk")

            ch_Jean "Pfft, if only." 
            
            $ Jean.change_face("angry1", eyes = "right") 
            
            ch_Jean "And, yeah. . . not like you really did anything wrong. . ."

    $ Jean.change_face("worried3")

    ch_Jean "I did all my normal pre-exam traditions, but no matter what I tried. . ."

    $ Jean.change_face("furious", eyes = "right")

    ch_Jean "UGH!"
    ch_Jean "My mind kept wandering and I couldn't focus."

    $ Jean.change_face("angry1")

    ch_Jean "I knew how to do everything, studied it all to death. . ."

    $ Jean.change_face("angry1", eyes = "squint")

    ch_Jean "I just couldn't help getting distracted by thoughts of yo-"

    $ Jean.change_face("worried3")

    pause 0.5

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite")

    ch_Jean "{i}Ahem{/i}. . ."

    $ Jean.change_face("worried1", eyes = "left", mouth = "lipbite")

    "She quickly glances around the room before composing herself."

    $ Jean.change_face("smirk1")

    ch_Jean "Never mind. Don't mind me, I'm sure it'll be fine. . ."
    "You can tell [Jean.name] is just putting on a brave face and is still freaking out on the inside."

    $ Jean.change_face("confused2")

    ch_Player "You don't have to pretend."
    ch_Jean "Wha-"

    $ Jean.change_face("worried2")

    ch_Player "C'mon, let's get out of here."
    ch_Jean "Don't you have class?!"
    ch_Player "It's fine, I won't be missing anything important."

    menu:
        extend ""
        "I care much more about taking your mind off things than some lecture.":
            call change_Girl_stat(Jean, "love", medium_stat) from _call_change_Girl_stat_112
            call change_Girl_stat(Jean, "trust", medium_stat) from _call_change_Girl_stat_113
            
            $ Jean.change_face("worried3")

            ch_Jean "You. . . do?"
        "Really, it's okay. I just wanna hang out with you for a bit.":
            call change_Girl_stat(Jean, "love", medium_stat) from _call_change_Girl_stat_114
            call change_Girl_stat(Jean, "trust", small_stat) from _call_change_Girl_stat_115
            
            $ Jean.change_face("worried3")

            ch_Jean "Are you sure?" 
            ch_Player "Yep."
        "I mean look at you, you're holding on by a thread. You need a distraction.":
            call change_Girl_stat(Jean, "love", -small_stat) from _call_change_Girl_stat_116
            call change_Girl_stat(Jean, "trust", medium_stat) from _call_change_Girl_stat_131
            
            $ Jean.change_face("worried3") 
            
            pause 0.5 
            
            $ Jean.change_face("worried1", eyes = "right")

            ch_Jean "I. . . guess you're right. . ."
            
    $ Jean.change_face("worried1")

    ch_Jean "People usually just find it annoying and try not to be around me when I'm like this. . ."

    $ Jean.change_face("worried2")

    ch_Player "Sounds like these 'people' are assholes."

    $ Jean.change_face("confused1", eyes = "right")

    "A thoughtful expression crosses over [Jean.name]'s face, and she doesn't respond. Instead, she follows you out of the classroom."

    $ fade_to_black(0.4)

    pause 1.0

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_323
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_395
    call send_Characters(Jean, "bg_campus", behavior = False) from _call_send_Characters_57

    $ Jean.change_face("neutral", eyes = "right")

    "[Jean.name] is uncharacteristically quiet as you lead her across the campus grounds."
    "You lead the conversation, exchanging small talk, trying to draw her mind away from her exam."

    $ fade_to_black(0.4)

    pause 1.0

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_333
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_396
    call send_Characters(Jean, "bg_mall", behavior = False) from _call_send_Characters_58

    $ Jean.change_face("happy")

    "By the time you finally arrive at the mall, [Jean.name] is talking much more animatedly with you, not even realizing where you both ended up."
    ch_Jean "I know, right?! That's what I've been sa-"

    $ Jean.change_face("confused2")

    pause 0.5

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "right")

    ch_Jean "Oh, when did we get here?"
    ch_Player "Heh, we just arrived."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "Let's walk around for a bit, then we can head back."
    ch_Jean "Okay, sure. . ."

    $ fade_to_black(0.4)

    "You spend a while just walking and talking with [Jean.name]. She seems much less stressed - almost like she's enjoying herself - by the time you make it back to campus."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_334
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_397
    call send_Characters(Jean, "bg_campus", behavior = False) from _call_send_Characters_59

    $ Jean.change_face("smirk2")

    ch_Jean "Thanks for all this."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "right")

    ch_Jean "I know how I get with this stuff, and it's usually much more. . . 'explosive.'"

    $ Jean.change_face("worried1")

    ch_Jean "When you put {i}so much{/i} effort into something and then screw it up anyway, it feels like it was all for nothing, ya'know?"

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "Of course."
    ch_Player "If you're ever on the verge of 'exploding' again, just let me know, and we can take another walk."

    $ Jean.change_face("smirk2")

    ch_Jean "Thanks, I {i}really{/i} appreciate it."
    ch_Jean "I'm gonna go read a book or something now, see you later!"

    call remove_Characters(Jean) from _call_remove_Characters_335

    $ clock = 0

    $ ongoing_Event = False

    return