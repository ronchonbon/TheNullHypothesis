init python:

    def Jean_chapter_one_season_one_training_sessions():
        label = "Jean_chapter_one_season_one_training_sessions"

        conditions = [
            "chapter == 1 and season == 1",
            
            "Jean.History.check('trained_with_Player', tracker = 'season') >= 4",

            "Player.training == Jean and Jean.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_one_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Jean.change_face("happy")

        ch_Jean "Ready to start?"

        $ Jean.change_face("smirk2")

        ch_Player "Yep!"

        call Jean_activate_psychic from _call_Jean_activate_psychic_15

        "After warming up, you spend the next couple hours with Jean going through increasingly elaborate control exercises."
        "It's daunting, how slow your progress is, but she assures you it's normal."

        if Laura.History.check("trained_with_Player", tracker = "season") >= 2:
            $ Jean.change_face("surprised1") 
            
            "You can at least be proud of your physical progress, as your training with [Laura.name] really shows during sparring." 
        else:
            $ Jean.change_face("worried1") 
            
            "Not only that, but she still stomps you during sparring."

        $ Jean.change_face("smirk2")

        "[Jean.name] finishes the session by flexing her power."
        "She almost overdoes it a couple times and barely manages to keep things under control."

        $ Jean.change_face("worried1")

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_15
 
        "Her progress since last time might be even slower than yours, but of course you don't say that."
        ch_Jean "Aight, let's call it for today."
    elif dice_roll == 2:
        $ Jean.change_face("smirk1")

        ch_Player "You ready?"

        $ Jean.change_face("smirk2")

        ch_Jean "Yep, follow my lead."
        "You briefly warm up, helping each other stretch out, before diving into more control exercises." 

        call Jean_activate_psychic from _call_Jean_activate_psychic_16

        "She tries teaching you all the various tricks she's picked up over the years."
        "Some of them aren't really applicable, but there are a few that actually have an effect."
        "After some more sparring, Jean practices with her own powers."

        $ Jean.change_face("worried1")

        "She goes too far this time and you have to step in more than once after she refuses to quit."

        $ Jean.change_face("angry1")

        "You both made some progress today. . . better than nothing. . ."

        $ Jean.change_face("appalled1")

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_16

        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], that's like the third time I've had to step in."

        $ Jean.change_face("worried2")

        ch_Player "I think we should call it here." 

        $ Jean.change_face("angry1", eyes = "right")

        ch_Jean "Goddamnit. . . I know."

        $ Jean.change_face("worried1")

        ch_Jean "Sorry, you're right."
        ch_Jean "Let's call it here."
    elif dice_roll == 3:
        $ Jean.change_face("worried1")

        ch_Player "You okay? Ready to start?"

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "Yeah, I'm alright."
        ch_Jean "I hope things go better today." 

        $ Jean.change_face("neutral")

        ch_Jean "Let's start."

        call Jean_activate_psychic from _call_Jean_activate_psychic_17

        "A few dynamic stretches later, and Jean has you doing some really confusing mental exercises that will supposedly help with power control."
        "Some of them don't seem to do anything, but others actually show some promise."

        $ Jean.change_face("smirk1")

        "You both do a bit of sparring before [Jean.name] starts working on her power."

        $ Jean.change_face("angry1")

        "She seems a bit off today, and things get out of control faster than usual."

        $ Jean.change_face("worried1") 

        with small_screenshake

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_17

        ch_Jean "Fuck, I'm really off my game today."
        ch_Player "I think we should call it there."
        ch_Player "Some rest would do us both good." 

        $ Jean.change_face("smirk1")

        ch_Jean "Got that right. . ."

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "If only I didn't have an exam coming up."

        $ Jean.change_face("worried1")

        ch_Jean "I gotta go study, I'll see you later."
    elif dice_roll == 4:
        $ Jean.change_face("smirk2")

        ch_Jean "Today's gonna be good."
        ch_Jean "C'mon, let's start."
        "She runs you through a warmup that's more energetic than usual, casually 'helping you stretch out.'"

        $ Jean.change_face("smirk2", blush = 1)

        call Jean_activate_psychic from _call_Jean_activate_psychic_18

        "Then, [Jean.name] goes right into pelting you with tennis balls."
        "You practice your reaction time and use your power to sense the projectiles before they can hit you."
        "This aspect of your power seems to come more naturally than when you try taking more direct control over it."

        $ Jean.change_face("happy")

        "She seems to be having a great time, watching you get hit by the occasional tennis ball."
        "The smile looks good on her."

        $ Jean.change_face("smirk1")

        "After that you both get into some sparring practice."

        $ Jean.change_face("smirk2")

        "At the end, [Jean.name] starts working on her own power, and it seems like her bright mood is also translating into her power control." 
        "Although, in the end, you still have to step in when she goes too far."

        $ Jean.change_face("worried2")

        pause 1.0

        with small_screenshake

        call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_18

        $ Jean.change_face("worried1")

        ch_Jean "Damn, I was having fun." 

        $ Jean.change_face("smirk1")

        ch_Player "You were doing better than usual too, seems like your mood has a lot to do with it." 

        $ Jean.change_face("smirk2", mouth = "lipbite")

        ch_Jean "I think you're right." 
        ch_Jean "I guess that means you'll have to be around more often to keep me in a good one. . ."
        ch_Player "I guess so. . ."
        ch_Jean "I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_56

    $ ongoing_Event = False

    return