init python:

    def Laura_chapter_one_season_two_first_training_session():
        label = "Laura_chapter_one_season_two_first_training_session"

        conditions = [
            "season == 2",
            "not Laura.History.check('trained_with_Player', tracker = 'season')",
            "Player.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_two_first_training_session:
    $ ongoing_Event = True
    
    if Player.training != Laura:
        call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_117
        
        $ Laura.change_face("angry1")

        if Laura.History.check("said_no_to_training", tracker = "recent"):
            ch_Laura "So you were just going to train without me?"
        else:
            if Player.training in all_Girls:
                ch_Laura "Were you about to train without me?"
            else:
                ch_Laura "Were you about to train on your own?"

        ch_Player "Yes. . ."

        $ Laura.change_face("furious")

        ch_Laura "Absolutely not."

        $ Player.training = Laura

        call remove_everyone_but(Laura) from _call_remove_everyone_but_4

    $ Laura.change_face("angry1")

    ch_Laura "Are you fully healed?"
    ch_Player "Yeah."
    ch_Player "Not sure how, but I feel perfectly fine."
    ch_Laura "Good."
    ch_Laura "Because we haven't been taking this training seriously enough."
    ch_Player "We haven't?!"
    ch_Laura "No, w-"
    "She seems to interrupt herself, as she gets a good look at you."

    $ Laura.change_face("neutral", eyes = "squint")

    pause 1.0

    $ Laura.change_face("neutral", eyes = "down")

    pause 1.0

    $ Laura.change_face("neutral", eyes = "squint")

    "[Laura.name] doesn't say anything and just stands there. . ."
    "Judging you. . ."
    "Silently. . ."

    ch_Player "Uh. . . what's wrong?"

    $ Laura.change_face("neutral", eyes = "down")

    ch_Laura "Something's different. . ."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "You're different. . ."
    ch_Player "Different?"
    ch_Laura "Your heartbeat, muscle tone, weight distribution. . ."
    "She continues muttering to herself."
    ch_Player "I don-"

    $ Laura.change_face("angry1")

    ch_Laura "Quiet."
    ch_Laura "You're being evaluated."
    ch_Laura "Warm up. Now."

    $ fade_to_black(0.4)

    "[Laura.name] looks deadly serious, so you just do as she says."
    "You start with the standard warm up exercises, mulling over the situation."
    "After Juggernaut. . . you were forced to rest and recover from your injuries."
    "Maybe she wants to see if you've gotten worse?"
    "You continue the warm up, too preoccupied with your own thoughts, barely paying attention to the workout."
    "What could possibly have bothered her so much. . ."
    "You finish the warm up."
    "Did you do something wrong?"
    "Then, it clicks."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("furious")

    ch_Player "What the fuck. . ."
    ch_Laura "Yes. {i}What{/i} the fuck?"

    $ Laura.change_face("suspicious1")

    "While you were so preoccupied with trying to figure out why [Laura.name] was upset, you breezed right through the normally excruciating warm up."
    "It wasn't easy, per se."
    "It just actually felt like. . . a warm up. . ."
    "Instead of a torturous workout."

    ch_Laura "I'm not done evaluating you."
    ch_Player "What do you w-"

    call Laura_unsheathes_claws from _call_Laura_unsheathes_claws_2

    $ Laura.change_face("furious")

    "Without warning, her claws come out, and you instinctively duck."
    "You're given a haircut as they nearly take your head off." 
    "She fluidly transitions into a kick, but you manage to put your arms up in time to block."

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "As it connects with your forearm, no bones are broken, but your hand briefly goes numb."
    "That kick was substantially more powerful than anything she's thrown at you before while sparring."

    call Laura_sheathes_claws from _call_Laura_sheathes_claws_2

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "Hmm. . . faster too."

    menu:
        extend ""
        "Holy shit. . . that was exhilarating.":
            $ Laura.change_face("confused2") 
            
            call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_447
        "Maybe a fucking warning next time ?!":
            $ Laura.change_face("appalled1") 
            
            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_448
        "What if I didn't duck in time. . . ?":
            $ Laura.change_face("angry1") 
            
            call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_449

    pause 1.0

    $ Laura.change_face("neutral")

    $ Laura.left_arm_pose = 2

    "Again, she's silent, but you recognize her fighting stance when you see it."

    $ fade_to_black(0.4)

    "Just in case you thought you might actually be able to keep up with her, she beats you worse than ever before."
    "This is less of a training session and more a trial by fire."
    "She pushes your meager skills to the limit and, by now, the fatigue is starting to build up."

    $ Laura.left_arm_pose = 1

    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral")

    "Her claws never came out again, but her deadliness is more evident than ever."
    "Matching your newfound speed still didn't even cause her to break a sweat."
    ch_Laura "Better, but still not nearly good enough."
    ch_Player "*huff* Holy shit. . . *huff*"

    $ Laura.change_face("angry1")

    ch_Laura "That's enough rest."
    ch_Laura "You know what's next."
    "Unfortunately, you do."
    "Despite whatever's changed, the next hour is just as torturous as ever."

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    "Your arms give out during a pushup, and you smack your face on the ground."

    $ Laura.change_face("confused1")

    ch_Laura "Maybe not better. . ."
    "She gives you a minute to catch your breath."
    ch_Player "Okay. . . what the hell is going on?"
    ch_Player "You've been 'evaluating' me, right?"

    $ Laura.change_face("suspicious1")

    ch_Laura "I have been."
    ch_Laura "Compared to several weeks ago. . ."

    $ Laura.change_face("confused1")

    ch_Laura "You're stronger, faster, more coordinated, indefatigable. . ."
    ch_Player "I felt pretty fatigable by the end there."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "I said, 'compared to several weeks ago.'"
    ch_Laura "Compared to me, you're still an infant."
    ch_Player "Thanks. . ."

    $ Laura.change_face("confused1")

    ch_Laura "You're. . . welcome?"

    $ Laura.change_face("sly", mouth = "smirk")

    ch_Laura "Regardless, this just means I get to push you even harder from now on."
    ch_Laura "And you're allowed to train on your own, as long as you follow this, to the letter."

    "She hands you a very extensive list of workouts."

    ch_Player "Wai-"

    call remove_Characters(Laura) from _call_remove_Characters_142

    "Without another word - and seemingly minimal interest in what actually caused these changes - she goes to finish her own training."
    
    "Leaving you to wallow in your own self pity."

    call change_Girl_stat(Laura, "trust", 20) from _call_change_Girl_stat_450

    $ ongoing_Event = False

    return