init python:

    def Laura_chapter_one_season_three_first_training_session():
        label = "Laura_chapter_one_season_three_first_training_session"

        conditions = [
            "chapter == 1 and season == 3",

            "not Laura.History.check('trained_with_Player', tracker = 'season')",
            
            "Player.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_three_first_training_session:
    $ ongoing_Event = True

    $ Laura.change_face("furious")
    
    if Player.training != Laura:
        if Player.training in all_Girls:
            "You're about to start training with [Player.training.name] when a shiver crawls up your spine."
        else:
            "You're about to start training when a shiver crawls up your spine."
        
        if Laura.History.check("said_no_to_training", tracker = "recent"):
            "The thought of getting caught training without [Laura.name] causes you to break out into a cold sweat."
            "Your better judgment wins out, and you hold off. . . just as she appears, looking quite unhappy."
        else:
            "The thought of getting caught by [Laura.name], without consulting her first, causes you to break out into a cold sweat."
            "Your better judgment wins out, and you hold off. . . just as she appears, looking quite unhappy."
        
        call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_116

        $ Laura.change_face("suspicious1") 
        
        if Laura.History.check("said_no_to_training", tracker = "recent"):
            ch_Laura "I didn't mean for you to train without me."
            ch_Laura "Fine, I'm here now."
        else:
            ch_Laura "I know you weren't about to try training without me. . ." 
        
        $ Laura.change_face("furious")

        $ Player.training = Laura

        call remove_everyone_but(Laura) from _call_remove_everyone_but_3

    ch_Laura "With all the changes you seem to undergo after your near-death experiences, an evaluation is necessary. . ."

    $ Laura.change_face("suspicious1")

    ch_Laura "Especially considering how traumatic this most recent one was."
    ch_Player "Yeah. . ."
    ch_Player "Still not entirely sure how I wasn't killed instantly."

    $ Laura.change_face("furious")

    ch_Laura "Stupidity and luck."
    ch_Player "Probably not far from the truth."

    $ Laura.change_face("angry1")

    ch_Laura "At least you were able to deactivate your powers."

    $ Laura.change_face("confused1")

    ch_Laura "Have you tried reactivating them since the incident?"

    menu:
        extend ""
        "Absolutely not, it's terrifying.":
            ch_Player "How it makes me feel. . . it scares me. . ." 
            
            $ Laura.change_face("furious")

            ch_Laura "Get over it." 
            ch_Laura "You have to get stronger." 
            ch_Laura "You will learn how to use it properly." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_432 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_433
        "No, but I sure as hell want to try them out.":
            ch_Player "It feels exhilarating." 
            
            $ Laura.change_face("suspicious1")

            ch_Laura "Do not let it cloud your judgment." 
            ch_Laura "You're not well trained enough to trust your instincts yet." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_434 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_435
        "Not yet, but I am kinda eager to figure them out.":
            $ Laura.change_face("angry1")

            ch_Laura "If you do what I say, you will." 
            ch_Laura "I won't let you stay this weak forever." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_436 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_437

    if Jean.History.check("trained_with_Player", tracker = "season"):
        ch_Laura "You didn't try while training with [Jean.name]?" 
        ch_Player "How did you know I. . . never mind." 
        ch_Player "No, she thought I should wait until seeing you first." 
        ch_Player "There's some kind of separation between my nullification and this new thing, where I can use one without the other if I want." 
        ch_Player "It's not at all easy to do that, though." 
        
        $ Laura.change_face("suspicious1") 

        ch_Laura "Hmmm. . ."

        $ Laura.change_face("neutral")

        ch_Laura "It doesn't matter."

    ch_Laura "Today, you will turn it on."
    ch_Player "Today?!"

    $ Laura.change_face("angry1")

    ch_Laura "Yes."
    ch_Laura "Learning how to use it properly might actually make you dangerous."

    $ Laura.change_face("neutral", eyes = "squint")

    menu:
        extend ""
        "Dangerous. . . to you in particular? I do appreciate how much you're trusting me.":
            $ Laura.change_face("neutral", eyes = "left")

            ch_Laura "Yes. . ." 
            
            $ Laura.change_face("angry1") 
            
            ch_Laura "You should be grateful." 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_438
        "You think so? Sweet.":
            $ Laura.change_face("suspicious1")

            ch_Laura ". . ." 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_439

    $ Laura.change_face("angry1")

    ch_Laura "We will do a light warm up before anything else."
    ch_Player "Light?"
    ch_Laura "Yes."
    ch_Laura "Your evaluation will be especially taxing today."

    $ fade_to_black(0.4)

    "A 'light' warm up now would've been a death sentence to you just mere months ago."
    "It goes by quickly, although your sense of time during these things isn't the best."
    "The focus seems to be more on preparing for a fight than for a workout."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "I am ready."

    $ Laura.left_arm_pose = 2

    ch_Laura "When you activate it, the fight will start."
    ch_Laura "Just focus on survival."

    menu:
        extend ""
        "Are you sure about this?":
            $ Laura.change_face("angry1")

            ch_Laura "I am." 
            ch_Laura "Stop stalling." 

            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_440
        "Brace yourself.":
            pass
        "I'm the one who should be focused on survival?":
            $ Laura.change_face("furious")

            "She just glares at you." 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_441

    "As you try releasing your power, you realize how much of a death grip you've had on it."
    "Whether out of fear or ineptitude, your will has been clamping down on it with full force."
    "It takes an immense mental effort to try and release your hold."
    
    $ Player.power = 25

    "You stagger as the power rips free of its shackles." with small_screenshake

    $ Laura.change_face("appalled2")

    $ Player.power = 50

    "It feels like an adrenaline rush, only ten times more potent."

    $ Laura.change_face("furious")

    "[Laura.name] doesn't miss a beat, as she immediately strikes out at you."
    "The first few strikes don't feel too much different, but that quickly changes."
    
    $ Player.power = 75

    "The change is exponential."
    "You've never felt so fast, and she's never felt so slow."
    "However, exchanging blows with such a boost only exposes more of your weaknesses."
    "You don't have the skill or experience to properly utilize this new power."

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    $ Laura.change_face("surprised2")

    "A leg connects with your arm as you block, but it doesn't rattle your bones like normal."

    $ Laura.change_face("angry1")

    "Completely unperturbed, [Laura.name] demonstrates why she's the best."
    "You can tell she's getting slower and weaker by the second, yet you're completely incapable of taking advantage."
    "She smacks you around as if this was just any other sparring session."
    
    $ Player.power = 25

    "You can't tell how long it's been, as a wave of exhaustion hits you like a truck."

    $ Laura.change_face("surprised2")

    $ Player.power = 0

    "[Laura.name] stops herself mid-punch, as you nearly fall down, your power suddenly no longer active."

    $ Laura.left_arm_pose = 1

    $ Laura.change_face("confused1")

    ch_Laura "Did you turn it back off?"
    ch_Player "*huff* No. . . *huff* It turned itself off. . . *huff*"

    $ Laura.change_face("neutral")

    ch_Laura "Interesting."
    "After a moment, you manage to catch your breath."
    ch_Player "What about you?"
    ch_Player "How did that feel?"
    ch_Laura "Like my strength and stamina were being stolen. . ."

    $ Laura.change_face("suspicious1")

    ch_Laura "Not painful, just very unpleasant."
    ch_Player "Sorry. . . I was kinda just along for the ride."
    ch_Player "Once I let go, it was all the way on."
    ch_Player "Didn't know how or even if I could tone it down."

    $ Laura.change_face("neutral")

    ch_Laura "And now?"
    ch_Player "I'm completely spent."

    $ Laura.change_face("smirk2")

    ch_Laura "You have enough in you for one final workout, I can tell."
    ch_Player "But. . ."
    "She doesn't take no for an answer and, after only a few minutes rest, she makes you finish things properly."
    "At least she has mercy on you, and it's a relatively light workout."
    "Your body doesn't agree, and you feel weaker than ever."
    "She seems barely phased by it all, as usual."

    $ Laura.change_face("angry1")

    ch_Laura "Enough."
    ch_Laura "I think you should see now why it's so important for you to practice with this power."
    ch_Laura "Being so vulnerable after a fight is unacceptable."
    ch_Laura "You need to get over it."

    call remove_Characters(Laura) from _call_remove_Characters_137

    "With that, she marches off."
    "Leaving you gasping for air."

    $ ongoing_Event = False

    return