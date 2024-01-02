init python:

    def Laura_chapter_one_season_one_first_study_session():
        label = "Laura_chapter_one_season_one_first_study_session"

        conditions = [
            "chapter == 1 and season == 1",

            "not Laura.History.check('studied_with_Player', tracker = 'season')",
            
            "Player.behavior == 'studying' and Laura in Player.behavior_Partners and Laura.behavior == 'studying'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_one_first_study_session:
    $ ongoing_Event = True

    $ Laura.change_face("neutral")
    $ Laura.change_arms("hips")

    "[Laura.name] haphazardly tosses her books and papers onto the bed before laying down."

    ch_Player "Uhm. . ." 

    $ Laura.change_face("confused2")
    $ Laura.change_arms("crossed")

    ch_Laura "What?" 
    ch_Player "Just. . . here let me organize things first."

    $ Laura.change_face("confused1")

    ch_Laura "Why. . . ?"
    "She just watches you, a bit perplexed, as you try to organize all the books and papers."

    $ Laura.change_face("neutral")

    "As the session starts, it becomes clear that [Laura.name] does not put nearly as much effort into studying as she does into training."
    "The 'study session' ends up being more of a tutoring session as you basically have to teach everything to her yourself."

    if Player.scholarship == "academic":
        "All that studying you did for your prior college courses comes in handy." 
        "You also realize some of the current coursework is relatively advanced compared to what you learned in college."
    else:
        "You've never been the best student, but it's not like you were ever at risk of failing in your prior college courses." 
        "Some of the stuff you've been learning at the Institute is more advanced in comparison, but easy enough to wrap your head around, let alone tutor [Laura.name]."

    $ Laura.change_face("angry1")
    $ Laura.change_arms("angry")

    "As you try explaining the concepts to [Laura.name], you realize it also helps deepen your own understanding of the material."
    "The thing is. . ."
    "You have to explain just about everything."
    ch_Player "Have you. . . studied any of this before?"

    $ Laura.change_face("confused1")
    $ Laura.change_arms("neutral", left_arm = "rub_neck")

    ch_Laura "Once."
    ch_Player "Once so far this week?" 

    $ Laura.change_face("confused2")
    $ Laura.change_arms("crossed")

    ch_Laura "No, {i}once{/i}."

    menu:
        extend ""
        "I know you think class is a waste of time, but it's important in its own way.":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_912
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_913

            $ Laura.change_face("angry1")
            $ Laura.change_arms("angry")

            ch_Laura "Everyone keeps telling me that." 
            
            $ Laura.change_face("angry1", eyes = "right") 
            
            ch_Laura "Especially [Ororo.public_name]. . ." 
            ch_Laura "How is it not obvious that focusing on 'studying' is why everyone's so weak. . ." 
            
            $ Laura.change_face("suspicious1") 
        "C'mon, [Laura.name], do you really think class is such a waste of time?":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_914
            
            $ Laura.change_face("angry1", eyes = "right")
            $ Laura.change_arms("angry")

            ch_Laura "It is." 
            
            $ Laura.change_face("angry1") 
            
            ch_Laura "Everyone wastes their time worrying about these 'grades.'" 
            
            $ Laura.change_face("furious") 
            
            ch_Laura "That's why they're all so weak." 
        "Seriously, [Laura.name], are you trying to fail?":
            call change_Character_stat(Laura, "love", -medium_stat) from _call_change_Character_stat_916

            $ Laura.change_face("appalled1")
            $ Laura.change_arms("angry")

            ch_Laura "{i}Grrrrrr{/i}. . . no." 
            
            $ Laura.change_face("angry1", eyes = "right") 
            
            ch_Laura "I just don't understand. . ." 
            ch_Laura "Worrying so much about 'grades'. . ." 
            
            $ Laura.change_face("furious") 
            
            ch_Laura "That's why everyone's so weak." 
            
    $ Laura.change_face("angry1", eyes = "right")
    $ Laura.change_arms("crossed")

    ch_Laura "Still. . . [Ororo.public_name] would be disappointed if I fail." 

    $ Laura.change_face("angry1")

    ch_Laura "But you seem to be good enough at this 'class' thing." 

    $ Laura.change_face("neutral")
    $ Laura.change_arms("hips", left_arm = "extended")

    ch_Laura "I'll just have you teach me everything." 

    $ Laura.change_arms("hips")

    menu:
        extend ""
        "I'll try my best.":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_917
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_993

            $ Laura.change_face("surprised1") 
            
            ch_Player "It does actually help me understand things better when teaching someone else." 
            
            $ Laura.change_face("smirk1")
        
            ch_Laura "Good. . ." 
            
            $ Laura.change_face("neutral") 
            
            ch_Laura "Now keep going, I didn't get that last part." 
        "I guess I can. . .":            
            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_994
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_1016

            ch_Player "But I don't know if I'll be any good at teaching."
        
            ch_Laura "You've already proven competent enough." 
            ch_Laura "Now, continue." 
            ch_Laura "None of this makes sense." 
        "Can't you just pay more attention during lecture?":
            call change_Character_stat(Laura, "trust", -small_stat) from _call_change_Character_stat_1017
            
            $ Laura.change_face("confused1") 
            
            ch_Player "I don't really want to have to learn everything, while also teaching it to you. . ." 
            
            $ Laura.change_face("suspicious1") 

            ch_Laura "No, I can't." 
            
            $ Laura.change_face("neutral") 
            
            ch_Laura "Now continue, I zoned out." 
            
    $ Laura.change_face("neutral")
    $ Laura.change_arms("crossed")

    "You spend the next few hours going through each lecture, trying your best to teach every topic covered in class so far."
    "[Laura.name] actually seems to be paying attention, even taking notes at times."

    $ Laura.change_face("angry1", eyes = "down")

    "She does occasionally get distracted, discreetly shifting a few inches away from you at times."

    $ Laura.change_face("angry1", eyes = "down", blush = 1)

    "You also notice her nostrils occasionally flairing, as if she smells something."

    $ Laura.change_face("neutral", blush = 1)

    ch_Player "Also, this one will probably be on the weekly quiz."

    $ Laura.blush = 0

    "You show her a specific question from your notes."

    $ Laura.change_face("confused1", eyes = "down")

    ch_Laura ". . . what's the answer?" 

    $ Laura.change_face("confused1")

    ch_Player "Not even going to try and solve it?" 

    $ Laura.change_face("neutral", eyes = "squint")
    $ Laura.change_arms("hips")

    ". . ."
    ch_Player "Okay, okay, the answer is choice A." 

    $ Laura.change_face("neutral")
    $ Laura.change_arms("crossed")

    ch_Player "Alright, I think that's about everything."
    ch_Laura "That was substantially more tolerable than a normal lecture."

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "You also smell. . ."

    $ Laura.change_face("angry1", blush = 1)
    $ Laura.change_arms("angry")

    ch_Laura ". . . pleasant."
    ch_Player "Uh. . . thanks?"

    $ Laura.change_face("suspicious1")

    ch_Laura "Why do you smell so good?"
    ch_Laura "Better than. . . everyone else." 

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Player "It's not like I use special shampoo or anything." 
    ch_Laura "Hmm. . ."

    $ Laura.change_face("neutral", blush = 1)
    $ Laura.change_arms("crossed")

    ch_Laura "I have decided."
    ch_Laura "You will just be my teacher from now on." 

    $ Laura.change_face("smirk2")

    ch_Laura "So now, I won't have to waste my time in class."

    $ Laura.change_face("confused1")
    $ Laura.change_arms("neutral")

    ch_Player "You know they take attendance right?" 
    ch_Laura "'Attendance'. . . ?"
    ch_Player "You still have to be present during lecture in order to get a good grade." 

    $ Laura.change_face("angry1")
    $ Laura.change_arms("angry")

    pause 1.0

    $ Laura.change_face("furious")

    ch_Laura "Fine, but that doesn't mean I have to pay attention." 

    $ Laura.change_face("angry1")
    $ Laura.change_arms("crossed")

    ch_Laura "That's enough for today, I need to go train." 

    call remove_Characters(Laura) from _call_remove_Characters_121

    if Player.location == Laura.home and Laura not in Keys:
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_349
    
    $ ongoing_Event = False

    return