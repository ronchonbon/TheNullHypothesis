init python:

    def Laura_chapter_one_season_two_second_training_session():
        label = "Laura_chapter_one_season_two_second_training_session"

        conditions = [
            "chapter == 1 and season == 2",

            "Laura.History.check('trained_with_Player', tracker = 'season') == 1",
            
            "Player.behavior == 'training' and Laura in Player.behavior_Partners and Laura.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_two_second_training_session:
    $ ongoing_Event = True

    $ Laura.change_face("neutral")

    "[Laura.name] walks right up to you, completely disregarding your personal space."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "How do you feel?"

    $ Laura.change_face("neutral")

    menu:
        extend ""
        "I feel great, thanks.":
            ch_Player "How are you?" 
            
            $ Laura.change_face("surprised2")

            pause 1.0

            $ Laura.change_face("confused1") 
            
            ch_Laura "I feel. . . fine." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_451 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_452
        "Uh. . . am I dreaming?":
            ch_Player "So you do actually care."

            $ Laura.change_face("neutral", eyes = "squint") 
            
            ch_Laura "Shut up. . ." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_453
        "Like shit, because I know how much this is gonna suck.":
            $ Laura.change_face("furious") 
            
            ch_Laura "Suck it up." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_454

    $ Laura.change_face("suspicious1")

    "She takes a step back."
    ch_Laura "The {i}only{/i} reason I asked. . ."
    ch_Laura "Is because you don't seem to comprehend your new situation."
    ch_Player "I don't?"
    ch_Player "Sure, the previous session was harder than normal, and I was able t-"

    $ Laura.change_face("furious")

    ch_Laura "No."
    ch_Laura "As I just said, you do not understand."

    $ Laura.change_face("angry1")

    ch_Laura "You fail to grasp just how much further I pushed you in our previous session."

    $ Laura.change_face("confused1")

    ch_Laura "Do you even feel any lingering soreness or muscle aches?"
    ch_Player "No. . ."

    $ Laura.change_face("angry1")

    ch_Laura "Exactly."
    ch_Laura "You should not be capable of the things I pushed you to do."

    if Player.scholarship == "athletic":
        ch_Laura "Even considering your natural athleticism."
    else:
        ch_Laura "Even considering your natural lack of athleticism."
    
    $ Laura.change_face("furious")

    ch_Laura "But regardless of how, or why. . ."

    $ Laura.change_face("angry1", eyes = "left")

    ch_Laura "This might mean you won't be so vulnerable and need people to protect you forever."
    ch_Laura "{size=-5}Then I won't have to worry so much{/size}. . ."

    $ Laura.change_face("furious", eyes = "right", blush = 1)

    pause 1.0

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "I thoroughly dislike how much anxiety you cause me on a daily basis."
    ch_Player "Anxiety?"

    $ Laura.change_face("confused1", blush = 1)

    menu:
        extend ""
        "I'm sorry, I really don't mean to stress you out.":
            ch_Player "But I trust you to help me learn how to fend for myself."
        
            $ Laura.change_face("angry1") 
            
            ch_Laura "Good." 
            ch_Laura "Then you will trust that the amount of pain I'm going to put you through is justified." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_455
        "I hate being a burden to you too. I refuse to be one for much longer.":
            $ Laura.change_face("surprised1") 
            
            ch_Player "You know my own limitations better than me. . . help me break through them."

            $ Laura.change_face("neutral") 
            
            ch_Laura "Trust in the fact that I will." 
            ch_Laura "And it will be {i}very{/i} painful." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_456 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_457
        "How much anxiety do you think {i}I{/i} feel, having so many near-death experiences?!":
            $ Laura.change_face("furious") 
            
            ch_Player "You know I need your help to stop being so goddamn vulnerable."
            ch_Laura "Then don't complain when I put you through more pain than you've ever felt in your life." 
            ch_Laura "Trust that it's for your own good." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_458 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_459

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Now. . ."
    ch_Laura "Shut up."
    ch_Laura "You will begin the warmup as directed."

    $ fade_to_black(0.4)

    "This time, instead of going through the normal routine, [Laura.name] directs you through more advanced exercises."
    "She manages to thoroughly exhaust you, despite your newfound stamina."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral")

    ch_Laura "You get 3 minutes before we move on."
    ch_Player "*huff* Thanks. . . *huff*"
    "After the first minute, you feel ready to go."

    $ Laura.change_face("neutral", eyes = "squint")

    "[Laura.name] seems to notice, but before she can say anything, you ask a question to delay her."
    ch_Player "By the way, why haven't you made me train with all those lasers and robot arms since our very first session?"

    $ Laura.change_face("confused1")

    ch_Laura "What use would it be, when you're barely capable of handling a normal human attacker?"
    ch_Player "Fair point. . ."

    $ Laura.change_face("neutral")

    ch_Laura "With your new situation, you might be good enough. . . one day."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "I can tell you're trying to stall."
    ch_Laura "Too bad, rest is over."

    $ fade_to_black(0.4)

    "[Laura.name] once again demonstrates how well she can control her own body, as she puts you through your paces."
    "Making herself just fast enough to outspeed you, but not so fast that it overwhelms you, is probably way harder than she makes it seem."
    "Time flies by as she painfully imparts her knowledge of hand-to-hand combat to you."
    "You're surprised when she even introduces you to fighting with knives and small blades."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral")

    ch_Laura "That's enough for today."
    ch_Laura "Now we move on to the final workout."
    ch_Player "Wait, that was it?"

    $ Laura.change_face("confused1")

    ch_Laura "Do you not realize how long it's been?"
    "You check your watch. . . it's already been several hours."
    ch_Player "Didn't feel like that long. . ."

    $ Laura.change_face("angry1")

    ch_Laura "You know what's left."
    ch_Laura "Get started."

    "You do as she says and go through all the normal exercises, albeit with many more repetitions than usual."
    "It takes longer than it ever has, but the accumulation of fatigue from all the training finally catches up with you."
    "You're in the middle of a burpee when you fail to slow yourself on the way down. . ."

    show expression "images/effects/green_smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.4)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    $ Laura.change_face("smirk2") 

    ch_Laura "Good, now we're done."
    "You struggle back up to your feet."
    ch_Player "Is it really necessary for me to wipe out every single time. . ."

    $ Laura.change_face("sly") 

    ch_Laura "Yes."

    call remove_Characters(Laura) from _call_remove_Characters_143

    "She just leaves, refusing to elaborate."

    $ ongoing_Event = False

    return