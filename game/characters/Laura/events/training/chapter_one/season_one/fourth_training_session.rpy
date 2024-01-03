init python:

    def Laura_chapter_one_season_one_fourth_training_session():
        label = "Laura_chapter_one_season_one_fourth_training_session"

        conditions = [
            "chapter == 1 and season == 1",

            "Laura.History.check('trained_with_Player', tracker = 'season') == 3",
            
            "Player.behavior == 'training' and Laura in Player.behavior_Partners and Laura.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_one_fourth_training_session:
    $ ongoing_Event = True
        
    ch_Player "Ready to warm up?" 

    $ Laura.change_face("neutral", eyes = "squint") 
    $ Laura.change_arms("crossed")

    pause 1.0

    ch_Player "Right. . . don't know why I asked. . ."

    $ Laura.change_face("neutral")

    $ fade_to_black(0.4)

    "You get into the warm up and actually feel pretty good at the start."
    "Is she taking it easy on you today?"
    ". . ."
    "[Laura.name] very quickly crushes that idea, as the intensity keeps rising, until it far eclipses last session."
    "By the end, you're left gasping for air, as usual. . ."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("pleased1")
    $ Laura.change_arms("hips")

    ch_Laura "That was better than last time." 

    $ Laura.change_face("smirk2")

    ch_Player "*huff* Feels worse than last time. . . *huff*"

    $ Laura.change_arms("hips", left_arm = "extended")

    ch_Laura "You get another minute, then we continue." 

    $ Laura.change_face("neutral")
    $ Laura.change_arms("hips")

    "Shortest minute of your life. . ."

    $ Laura.change_arms("fight")

    "Today she puts you through a mixture of offensive and defensive exercises."
    "Combining what you've learned so far proves to be difficult, and most of the time you just make things worse." 

    $ Laura.change_face("angry1")

    "[Laura.name] mercilessly capitalizes on your openings, getting angrier every time you get hit."

    $ Laura.change_face("furious")

    "You're used to the beatings by now, and you even manage to use the right technique and simultaneously defend yourself while countering."

    $ Laura.change_face("surprised2")
    $ Laura.change_arms("claws")

    "[Laura.name] wasn't expecting any real competency from you, and you almost manage to tag her."
    "Still, she effortlessly dodges out of the way."

    $ Laura.change_face("neutral", eyes = "squint")
    $ Laura.change_arms("crossed")

    ch_Laura "That was sloppy. . . but you had the right idea." 
    "You take a moment to catch your breath."

    menu:
        extend ""
        "You're probably the best fighter on campus. . . I had to learn something eventually.":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_1070
            call change_Character_stat(Laura, "trust", medium_stat) from _call_change_Character_stat_1071
            
            $ Laura.change_face("surprised1")

            pause 1.0

            $ Laura.change_face("smirk2")

            ch_Laura "Took you long enough." 
        "I guess my brain decided it didn't like getting hit so much. . .":
            call change_Character_stat(Laura, "love", -small_stat) from _call_change_Character_stat_1074
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_1076

            $ Laura.change_face("confused1")
            
            pause 1.0
            
            $ Laura.change_face("smirk2")

            ch_Laura "Took your brain long enough." 
        "Maybe things would go faster if you just went easier on me. . .":
            call change_Character_stat(Laura, "love", -medium_stat) from _call_change_Character_stat_1078
            call change_Character_stat(Laura, "trust", -small_stat) from _call_change_Character_stat_1079

            $ Laura.change_face("angry1")

            pause 1.0

            $ Laura.change_face("furious")

            ch_Laura "You think someone will go easy when they're actually trying to kill you?"

    $ Laura.change_face("neutral")
    $ Laura.change_arms("hips")

    ch_Laura "You know what's next." 

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Player "Let's get this over with. . ." 
    "You've been doing well today, and that clearly means you aren't being pushed hard enough. . ."
    "If nothing else, [Laura.name] is thorough." 
    "She makes you go through countless exercises, exhausting muscle groups you didn't even know you had."

    $ Laura.change_face("angry1")
    $ Laura.change_arms("crossed")

    "It feels like it goes on forever. . ."
    "Your legs give out, but you manage to catch yourself on the way down."

    $ Laura.change_face("neutral")

    ch_Laura "That was satisfactory. . . for your level at least."
    ch_Player "*huff* Fucking hell. . . *huff*"
    ch_Player "Maybe one day it won't hurt so much." 

    $ Laura.change_face("confused1")
    $ Laura.change_arms("angry")

    ch_Laura "If it doesn't. . . "

    $ Laura.change_arms("neutral")

    ch_Player "Yeah, yeah. 'I'm not training hard enough.'" 

    $ Laura.change_face("smirk2")
    $ Laura.change_arms("neutral", left_arm = "extended")

    "She actually offers her hand to help you up."
    "You take it."

    $ Laura.change_face("appalled1", blush = 1) 
    $ Laura.change_arms("crossed")

    "And as soon as you're up, she jerks it back." 

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "Goodbye."

    call remove_Characters(Laura) from _call_remove_Characters_130
    
    "With that, she leaves to go train on her own."

    $ ongoing_Event = False

    return