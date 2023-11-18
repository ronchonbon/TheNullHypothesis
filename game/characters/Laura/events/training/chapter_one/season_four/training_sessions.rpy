init python:

    def Laura_chapter_one_season_four_training_sessions():
        label = "Laura_chapter_one_season_four_training_sessions"

        conditions = [
            "chapter == 1 and season == 4",
            "Laura.History.check('trained_with_Player', tracker = 'season') >= 1",
            "Player.training == Laura and Laura.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_four_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Laura "Today we'll properly warm up before sparring."  

        $ Laura.change_face("sly")

        ch_Laura "Need to save your power so I can get a good workout in."
        "The warm up still isn't particularly light, but you're used to that by now."

        $ Laura.left_arm_pose = 2

        "She seems eager to get to the fighting, so you don't waste any time."

        $ fade_to_black(0.4)

        $ Player.power = 25

        "After spending a minute wrangling your power under control, the fight's on."

        $ Player.power = 50

        "These sparring sessions have only been getting longer as of late, thanks to your continued improvement."
        
        $ Player.power = 75
        
        "Of course, [Laura.name] eclipses you in terms of skill, and you're more focused on survival as per usual."
        
        $ Player.power = 100

        "She pushes you to the breaking point and has to stop herself mid-kick to prevent taking your head off."

        $ Player.power = 0

        $ fade_in_from_black(0.4)

        $ Laura.change_face("smirk2")
        $ Laura.left_arm_pose = 1

        ch_Player "*huff* That was better. . . *huff* right?" 
        ch_Laura "Than last time? Yes."
        ch_Laura "But still not good enough."

        $ Laura.change_face("angry1")

        ch_Laura "I'm not even winded."
        "She graciously allows you a couple minutes rest, before making you finish the training session properly." 
        "The after effects aren't as acute this time, but you're still dead tired by the end."

        $ Laura.change_face("neutral")

        ch_Laura "Okay, enough." 
        ch_Laura "You can barely stand." 
        ch_Laura "I'll keep going on my own."

        call remove_Characters(Laura) from _call_remove_Characters_127

        "She goes to finish her own training."
    elif dice_roll == 2:
        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "Today you won't use your power until the very end."
        ch_Player "I won't?"
        ch_Laura "No, you need to practice using it while already fatigued." 
        ch_Player "That's. . . reasonable."

        $ fade_to_black(0.4)

        "[Laura.name] makes every aspect of the following session as painful as possible."
        "The warm up is drawn out, and she makes you demonstrate techniques and weapon handling until your arms nearly fall off."
        "It takes quite a while."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("angry1") 

        ch_Laura "Now, we spar."
        ch_Player "*huff* But. . . *huff*"

        $ Laura.change_face("suspicious1")
        $ Laura.left_arm_pose = 2

        "[Laura.name] doesn't leave you much choice, as she pounces before you're even able to activate the power."
        "She doesn't slow down for you at all, and you take a few solid hits just trying to react."

        $ Player.power = 25

        "Eventually you get things going and, as the power takes effect, your weakness and fatigue wash away."

        $ fade_to_black(0.4)

        $ Player.power = 50

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

        "The sparring session goes mostly as expected, with you getting your ass beat for the majority of it."

        $ Player.power = 25

        "You notice the power start to dwindle a bit earlier than usual and much more rapidly than you're used to."
        "[Laura.name] throws a punch which you manage to block, but your legs give out anyway, and your ass meets the floor."

        pause 1.0

        with small_screenshake

        $ fade_in_from_black(0.4)

        $ Laura.change_face("confused1")
        $ Laura.left_arm_pose = 1

        "The after effects seem to be particularly potent today."
        ch_Player "*huff* That felt quick. . . *huff*"

        $ Laura.change_face("neutral") 
        
        ch_Laura "It was quicker than normal." 

        $ Laura.change_face("confused1", mouth = "smirk")

        ch_Laura "So already being fatigued does have a substantial effect."
        ch_Player "*huff* Seems so. . . *huff*"

        call remove_Characters(Laura) from _call_remove_Characters_128

        "[Laura.name] leaves to go do her own thing."
        "It takes you several minutes to catch your breath and get back to your feet."
    elif dice_roll == 3:
        $ Laura.change_face("confused1", eyes = "down")

        "[Laura.name] looks you up and down."

        $ Laura.change_face("confused1")

        ch_Laura "We need to work on your power control." 
        ch_Player "Don't we always. . . ?" 

        $ Laura.change_face("neutral")

        ch_Laura "I can tell it takes a lot of effort to limit yourself."

        $ Laura.change_face("angry1")

        ch_Laura "Enough talking, get to work."

        "She throws you into a quick warm up, one not much harder than normal." 
        "Afterwards, she takes a few steps back."
        ch_Laura "Power on, all the way."
        ch_Laura "Limit it only when I come in to attack."

        $ fade_to_black(0.4)

        "She has you perform various exercises and practice countless techniques."
        "Occasionally, without warning, she'll swoop in to exchange blows, before pulling back again."
        "It's as much a strain on your mind as it is on your body, constantly modulating your power like that."
        "You manage to hold out for longer than you thought, before everything falls apart, and you're left thoroughly wrung out."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("neutral")

        ch_Laura "Better. . ."
        ch_Player "*huff* But not good enough. . . *huff* I know. . . *huff*"

        $ Laura.change_face("angry1", mouth = "smirk")

        ch_Laura "Just for that, you lose 30 seconds of rest."
        "She gives you less than a minute to recover, before making you finish the session."
        "You have a hard time focusing and perform worse than normal."

        $ Laura.change_face("neutral")

        ch_Laura "That's enough."
        ch_Laura "You just missed the last three directions I gave you."
        ch_Laura "Go recover."

        call remove_Characters(Laura) from _call_remove_Characters_129

        "You couldn't argue even if you wanted to."

    $ ongoing_Event = False

    return