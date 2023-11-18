init python:

    def Laura_chapter_one_season_two_first_study_session():
        label = "Laura_chapter_one_season_two_first_study_session"

        conditions = [
            "chapter == 1 and season == 2",
            "not Laura.History.check('studied_with_Player', tracker = 'season')",
            "Player.studying == Laura and Laura.studying"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_two_first_study_session:
    $ ongoing_Event = True

    $ Laura.change_face("neutral")

    ch_Laura "Do you. . ."

    $ Laura.change_face("suspicious1")

    ch_Laura "Want me to help set things up?"
    ch_Player "Uh, sure."
    ch_Player "But why are you looking at me like that?"

    $ Laura.change_face("angry1", eyes = "squint")

    ch_Laura "Because you're picky about it."

    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Player "I'm not. . ."
    ch_Player "Never mind."
    ch_Player "It would be great if you helped." 

    $ Laura.change_face("confused1", eyes = "down")

    "She does help you set things up, but you notice something odd."
    ch_Player "Why do you keep putting the psychology stuff next to the calculus papers?"

    $ Laura.change_face("angry1")

    ch_Laura ". . ."
    ch_Laura "This is what I mean by 'picky'."
    ch_Player "That's not being picky. . ."

    $ Laura.change_face("confused2")

    ch_Player "They're completely different subjects."
    ch_Laura "Subjects?"

    $ Laura.change_face("confused1")

    ch_Laura "It's all for 'class,' why does it matter which papers go where?"
    "After a bit of prying, you realize [Laura.name] has no concept for how courses are usually organized."
    "Or how school works in general. . ."

    menu:
        extend ""
        "I know your situation before coming here was different, but you must have had some kind of prior schooling, no?":
            $ Laura.change_face("angry1", eyes = "right")

            ch_Laura "I was taught many things. . ." 
            
            $ Laura.change_face("angry1") 
            
            ch_Laura "The vast majority of which were focused on how to most effectively kill someone." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_398 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_399
        "Did you really never have any experience with school before this? They must've taught you some stuff. . . before coming here.":
            $ Laura.change_face("angry1")

            ch_Laura "'School'?" 
            ch_Laura "No."
            ch_Laura "How to kill effectively?" 
            ch_Laura "Yes." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_400
        "Oh come on, there's no way you've never heard of this school stuff. You're pretty smart, all things considered. . .":
            ch_Player "Somebody must've taught you at some point." 
            
            $ Laura.change_face("appalled1")

            ch_Laura "Why would someone like me need to learn anything but how to most effectively kill a human being?" 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_401 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_402

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "I was taught very basic things. . ."
    ch_Laura "Concepts that were deemed necessary to understand."
    ch_Laura "Also, how to efficiently absorb and process information."

    $ Laura.change_face("neutral")

    ch_Laura "Mostly as a way to expedite my training process."

    $ Laura.change_face("confused1")

    ch_Player "Well. . . the vast majority of people go through a much different process when growing up."

    $ Laura.change_face("angry1", eyes = "squint")

    ch_Laura "Explain."
    "You describe how school usually works, explaining all the different grade levels and age groups."
    "Also how the Institute functions much like a college education."
    ch_Laura "I'm {i}almost{/i} glad I didn't have to suffer through all of that. . ."

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Player "For most nor-"

    $ Laura.change_face("neutral")

    ch_Player "I mean non-mutants, the idea of fighting and killing is a foreign concept."

    $ Laura.change_face("confused1")

    ch_Player "Parents usually want to shield their kids from things like that."
    ch_Player "Instead, the focus is on how to become a functioning member of society. . . despite all the system's flaws."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "I see."
    ch_Player "So that's why most people are 'weak' compared to you."

    $ Laura.change_face("neutral", eyes = "right")

    ch_Laura "I'd. . . like to change the subject. . ."

    $ Laura.change_face("neutral")

    ch_Player "Sure, let's just get into the tutoring then."

    $ Laura.change_face("neutral", eyes = "down")
    
    "Despite [Laura.name]'s lack of prior education, you've begun to notice just how effectively she's able to learn."
    "Her grades were pitiful before you arrived, despite [Ororo.name]'s attempts at tutoring."
    "On the other hand, under your tutelage, she's become a completely different student."

    $ Laura.change_face("smirk2")

    "Her recent exam results speak for themselves."
    "As today's session begins in earnest, you also notice the change in her demeanor as well."

    $ Laura.change_face("smirk2", eyes = "down", blush = 1)

    "Instead of acting like a skittish stray cat ready to claw you at the slightest touch, she seems much more relaxed."
    ch_Player "Here, try this question. . ."

    $ Laura.change_face("confused1")

    ch_Laura "The answer is choice A."
    ch_Player "Yep, that's right."

    menu:
        extend ""
        "I know you don't enjoy this stuff, but you've been doing really well lately.":
            $ Laura.change_face("smirk2", eyes = "right")

            ch_Laura "It's been. . . easier to digest lately. . ."
        "You've been crushing the exams recently, great job.":
            $ Laura.change_face("smirk2", eyes = "right")

            ch_Laura "I. . . thanks. . ."
        "Maybe whatever training you went through as a kid was a good thing. Can't deny the results, you've been crushing the recent exams.":
            $ Laura.change_face("angry1", eyes = "right")

            ch_Laura "Thanks. . . I guess. . ."

    $ Laura.change_face("angry1")

    ch_Laura "It's mostly your fault."

    if Player.scholarship == "academic":
        ch_Laura "You're clearly very intelligent." 
        ch_Laura "I can see why you'd be good at teaching."
    elif Player.scholarship == "athletic":
        ch_Laura "Despite your focus on athletics, you're clearly smart." 
        ch_Laura "It makes sense why you'd be a decent tutor."
    elif Player.scholarship == "artistic": 
        ch_Laura "Despite your focus on. . ." 
        
        $ Laura.change_face("suspicious1") 
        
        ch_Laura "The {i}arts{/i}." 
        ch_Laura "You're clearly smart." 
        ch_Laura "It makes sense why you're a decent tutor."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Player "That's nice of you to say."
    ch_Laura "Shut up. . ."

    $ Laura.change_face("angry1", eyes = "squint")

    ch_Laura "It's just an observation."

    $ Laura.change_face("neutral")

    ch_Laura "Doesn't mean I want to keep studying right now."
    ch_Laura "I'm going to train."
    ch_Laura "Bye."

    call remove_Characters(Laura) from _call_remove_Characters_124

    if Player.location == Laura.home and Laura not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_352
    
    $ ongoing_Event = False

    return