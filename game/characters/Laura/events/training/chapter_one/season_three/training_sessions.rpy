init python:

    def Laura_chapter_one_season_three_training_sessions():
        label = "Laura_chapter_one_season_three_training_sessions"

        conditions = [
            "season == 3",
            "Laura.History.check('trained_with_Player', tracker = 'season') >= 2",
            "Player.training == Laura and Laura.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_three_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        "After a brief warm up. . ."
        ch_Laura "Today we start with sparring." 
        ch_Player "You don't mean. . . with my power, right?"

        $ Laura.change_face("confused1")

        ch_Laura "Why wouldn't I mean that?"
        ch_Player "Because I'll be dead for the rest of the session. . ."

        $ Laura.change_face("smirk2")

        ch_Laura "That's the point." 

        $ fade_to_black(0.4)

        $ Player.power = 25

        "Arguing is futile, so you dive right into it."

        $ Player.power = 50

        "Your perception of time while the power is active can't be accurate, because it feels like you only manage to fight for a minute at most."
        "Of course, [Laura.name] barely breaks a sweat."

        $ Player.power = 25

        "As the power dwindles, she doesn't let up and pushes you until you can barely stand."

        $ fade_in_from_black(0.4)

        $ Player.power = 0

        $ Laura.change_face("neutral")

        ch_Player "*huff* Fuck. . . *huff*"
        ch_Player "*huff* How long was that? *huff*"
        ch_Laura "More than last time."
        ch_Laura "But still not even ten minutes."

        $ Laura.change_face("angry1")

        "She gives you a couple minutes to catch your breath, before pushing you through more techniques and weapons training." 
        "The after effects of your power cause you to be a bit sloppy, making [Laura.name] even angrier."
        "You try your best and eventually make it to the end."

        $ Laura.change_face("furious")

        ch_Laura "You're done." 
        ch_Laura "Just moving backwards at this point." 

        call remove_Characters(Laura) from _call_remove_Characters_139
        
        "She goes to finish training on her own."
    elif dice_roll == 2:
        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "We're trying something different today."
        ch_Player "We are?"
        ch_Laura "Activate your power, but use it to do the exercises, instead of sparring." 
        ch_Laura "I'll be at a reasonable distance." 

        $ fade_to_black(0.4)

        $ Player.power = 25

        "[Laura.name] moves away and, as you activate your power, you feel the difference immediately."
        
        $ Player.power = 50

        "The boost is much less potent, but you can still tell how much better it makes you."
        "You blow right through the warm up."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("angry1")

        $ Laura.left_arm_pose = 2

        "[Laura.name] indicates for you to keep going and has you shadow her while she demonstrates various techniques and physical feats."
        "You have no idea how much time passes like this, just parroting whatever she shows you."
        
        $ Player.power = 25

        "Eventually the weakness starts creeping in, and you stop being able to copy everything."
        
        $ Laura.change_face("angry2")

        "You stumble after a particularly difficult move and end up on your ass."

        pause 1.0

        with small_screenshake

        $ Player.power = 0

        $ Laura.change_face("neutral")
        $ Laura.left_arm_pose = 1

        ch_Player "*huff* How long was that? *huff*"
        ch_Laura "Substantially longer than when we spar." 

        $ Laura.change_face("confused1", mouth = "smirk")

        ch_Laura "I imagine the aftereffects are less potent as well?"
        ch_Player "*huff* Hard to tell. . . *huff*"

        call remove_Characters(Laura) from _call_remove_Characters_140

        "[Laura.name] just leaves to go do her own thing."
        "The weakness does feel less suffocating, if only slightly."
    elif dice_roll == 3:
        $ Laura.change_face("confused1", eyes = "down")

        "[Laura.name] looks you up and down."

        $ Laura.change_face("confused1")

        ch_Laura "You look too comfortable." 
        ch_Player "Too comfortable. . . ?" 

        $ Laura.change_face("neutral")

        ch_Laura "Not pushing yourself hard enough lately."

        $ Laura.change_face("angry1")

        ch_Laura "Warm up, now."

        "The warm up is quick, but she pushes you harder than normal."
        "Afterwards she runs you through endless techniques and exercises, beating you thoroughly."

        call Laura_unsheathes_claws from _call_Laura_unsheathes_claws_1

        "She even makes you defend yourself with weapons against her claws."
        "The weapons get torn to shreds, and you don't come out of it unscathed either."

        call Laura_sheathes_claws from _call_Laura_sheathes_claws_1

        ch_Laura "Power on, now."

        $ Player.power = 25

        $ fade_to_black(0.4)

        $ count = 7

        while count > 0:
            $ dice_roll = renpy.random.randint(1, 3)

            $ x = renpy.random.random()*0.7 + 0.15
            $ y = renpy.random.random()*0.7 + 0.15

            if dice_roll == 1:
                show expression "images/effects/green_smack.webp" as smack onlayer effects:
                    anchor (0.5, 0.5) pos (x, y)

                    zoom 0.0
                    alpha 0.0
                    ease 0.1 zoom 1.0 alpha 1.0
                    ease 1.0 alpha 0.0
            elif dice_roll == 2:
                show expression "images/effects/crack.webp" as crack onlayer effects:
                    anchor (0.5, 0.5) pos (x, y)

                    zoom 0.0
                    alpha 0.0
                    ease 0.1 zoom 1.0 alpha 1.0
                    ease 1.0 alpha 0.0
            elif dice_roll == 3:
                show expression "images/effects/pow.webp" as pow onlayer effects:
                    anchor (0.5, 0.5) pos (x, y)

                    zoom 0.0
                    alpha 0.0
                    ease 0.1 zoom 1.0 alpha 1.0
                    ease 1.0 alpha 0.0

            $ renpy.pause(renpy.random.random(), hard = True)

            $ count -= 1
            
        "She doesn't miss a beat and throws herself at you, purposefully targeting what you now recognize as weak spots."
        
        $ Player.power = 50

        "You do an admirable job for your pitiful level of experience, but it's still not even a contest."
        "Strikes constantly slip past your defenses, hitting you where it hurts."
        "You're surprised, however, when a solid hit to your liver hurts like hell, but doesn't make you crumple like before."
        
        $ Player.power = 25

        "The exchange continues for a short while, before you run out of steam."

        $ fade_in_from_black(0.4)
        
        $ Laura.change_face("angry1", mouth = "smirk")

        $ Player.power = 0

        ch_Laura "So it's not just strength and stamina, but durability too."
        ch_Player "*huff* Still. . . *huff* hurts like hell. . . *huff*"

        "She gives you a minute to recover, before making you finish the session."

        $ Laura.change_face("neutral")

        ch_Laura "Stop."
        ch_Laura "You're more durable while the power is active, but even weaker than normal afterwards."
        ch_Laura "We have a lot of work to do."

        call remove_Characters(Laura) from _call_remove_Characters_141

        "You look down at yourself and notice the cuts from before are already closed."

    $ ongoing_Event = False

    return