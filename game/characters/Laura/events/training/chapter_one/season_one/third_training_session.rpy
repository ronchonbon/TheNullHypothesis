init python:

    def Laura_chapter_one_season_one_third_training_session():
        label = "Laura_chapter_one_season_one_third_training_session"

        conditions = [
            "chapter == 1 and season == 1",

            "Laura.History.check('trained_with_Player', tracker = 'season') == 2",
            
            "Player.behavior == 'training' and Laura in Player.behavior_Partners and Laura.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_one_third_training_session:
    $ ongoing_Event = True

    $ Laura.change_face("neutral")
    $ Laura.change_arms("hips")

    ch_Laura "Let's go, time to start."
    ch_Player "Are we doing another one of your 'warm ups'?" 

    $ Laura.change_face("confused1")

    ch_Laura "Why wouldn't we?"
    ch_Player "Don't know what I expected. . ."

    $ Laura.change_face("neutral")
    $ Laura.change_arms("crossed")

    $ fade_to_black(0.4)

    "Today's 'warm up' seems even harder than last time."
    "You're not sure if it actually is, or that's just your imagination. . ."
    "Regardless, you're left gasping for breath by the time it's over."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("confused2")
    $ Laura.change_arms("hips", left_arm = "extended")

    ch_Laura "Is this really that hard for you?"

    $ Laura.change_arms("hips")

    ch_Player "*huff* Yes. . . *huff*" 

    $ Laura.change_face("confused1")
    $ Laura.change_arms("crossed")

    "You finally catch your breath."

    if Player.scholarship == "athletic":
        ch_Player "I was in very good shape before coming here." 
        ch_Player "Played D1. . ." 
    else:
        ch_Player "I kept myself in pretty good shape before coming here." 
        ch_Player "Not a big athlete or anything. . ." 

    $ Laura.change_face("neutral")

    ch_Player "But, you're just on another level." 

    $ Laura.change_face("angry1")
    $ Laura.change_arms("angry")

    ch_Laura "Am I? Or is everyone else just not training hard enough?" 

    $ Laura.change_arms("fight")

    "She goes right into the lesson and seems hellbent on making sure you do train hard enough from now on."
    "You're an order of magnitude slower than her, but you've always been a quick learner."
    "You even manage to successfully defend yourself like she taught you."

    $ Laura.change_face("sly")

    "Your success just encourages her to go faster. . ."
    "After a while, she suddenly stops."

    $ Laura.change_face("neutral", eyes = "squint")
    $ Laura.change_arms("crossed")

    ch_Laura "So you are capable of improving." 

    $ Laura.change_face("neutral")

    ch_Laura "Now we can move on to offensive techniques."

    $ Laura.change_arms("fight")

    "She coaches you on how to look for weaknesses and openings before going into practical demonstrations."
    "That just means she finds another excuse to beat you up."
    "At least she puts on a pair of ratty MMA gloves before hitting you."

    $ Laura.change_face("surprised2")

    "Everytime she connects or touches you to correct your form, she shudders and redoubles her efforts to exhaust you."

    $ Laura.change_face("angry1")

    "She doesn't have to try very hard, before you're hardly able to lift your arms up, let alone throw a punch."

    $ Laura.change_arms("hips")

    ch_Player "*huff* I know, I know. . . we're not done yet. *huff*" 

    $ Laura.change_face("angry1", mouth = "smirk")

    ch_Laura "Not nearly."
    "With that, she pushes you through the final hour of pain and torture."
    "She's very thorough, making sure to evenly distribute the pain and suffering throughout every last muscle group."

    $ Laura.change_face("angry1")
    $ Laura.change_arms("crossed")

    "You're in the middle of a pushup when your arms give out on you. . ."
    
    pause 1.0

    with small_screenshake

    "You smack the floor with your face."

    $ Laura.change_face("smirk1")

    ch_Player "Fuuuuuck. . ."
    ch_Laura "That's it, you're done." 

    $ Laura.change_face("neutral")

    ch_Laura "That was even worse than last time." 

    $ Laura.change_face("confused1")
    $ Laura.change_arms("hips")

    ch_Laura "I guess you do take substantially longer to recover. . ."
    ch_Player "And I'm sure all of that was like a light jog to you." 

    $ Laura.change_face("sly")

    ch_Laura "More of a slow walk. . ."
    ch_Player "Was that an actual joke?"

    call remove_Characters(Laura) from _call_remove_Characters_132

    "She just leaves to continue training on her own."

    $ ongoing_Event = False

    return