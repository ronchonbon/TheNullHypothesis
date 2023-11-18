init python:

    def Laura_chapter_one_season_two_training_sessions():
        label = "Laura_chapter_one_season_two_training_sessions"

        conditions = [
            "chapter == 1 and season == 2",
            "Laura.History.check('trained_with_Player', tracker = 'season') >= 2",
            "Player.training == Laura and Laura.training"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Laura_chapter_one_season_two_training_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("neutral")

        ch_Laura "You don't have plans for any strenuous physical activity after this session, correct?" 

        $ Laura.change_face("confused1")

        ch_Player "I don't know. . . why?" 

        $ Laura.change_face("neutral")

        ch_Laura "Just focus on surviving."
        ch_Player "Surviving?!"

        $ fade_to_black(0.4)

        "Without elaborating, [Laura.name] puts you through a living hell."
        "The warm up is quicker than usual, but you don't get a moment's rest for the entire session afterwards."
        "There doesn't seem to be any specific focus. . . other than making you feel as much pain as possible."
        "You just do what she says and focus on making it through the training intact."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("angry1")

        "You've made substantial progress in general, but [Laura.name] shows you just how little that means when compared to her." 
        "The session ends as usual, with your face hitting the ground."

        $ Laura.change_face("smirk2")

        "You pick yourself back up, struggling for breath."
        ch_Laura "Good, we're done." 
        ch_Player "*huff* Ow. . . *huff*"

        call remove_Characters(Laura) from _call_remove_Characters_144
        
        "She goes to finish training on her own."
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        ch_Laura "You're not limping?"
        ch_Player "Why would I be. . . ?" 
        ch_Laura "No residual aches and pains?"
        ch_Player "Not really. . ."

        $ Laura.change_face("neutral")

        ch_Laura "After the last session, I was expecting. . . never mind."

        $ Laura.change_face("neutral", eyes = "squint")

        $ fade_to_black(0.4)

        "[Laura.name] almost seems offended that you don't have any lingering pain from the previous session."
        "She does her utmost to rectify the situation."
        "The warm up is quick, but painful, and she allows you only seconds of rest before continuing."

        $ fade_in_from_black(0.4)

        $ Laura.change_face("angry1")

        "You have a decent grasp of the hand-to-hand techniques [Laura.name]'s taught you so far, but she makes you practice with short blades again today."
        "Apparently she 'doesn't believe in dull practice weapons'. . ."
        "And thinks letting you accidentally cut yourself a bunch of times is the quickest way to learn how to properly respect a blade."
        
        $ Laura.change_face("angry2")

        "At least the workout to end the session goes by quickly. . . albeit painfully, as you wipe out."

        pause 1.0

        with small_screenshake

        $ Laura.change_face("smirk2")

        ch_Laura "Good, that's enough for today."
        ch_Player "*huff* Why did that. . . *huff* hurt more than all the cuts. . . *huff*" 

        $ Laura.change_face("confused1", mouth = "smirk")

        call remove_Characters(Laura) from _call_remove_Characters_145

        "[Laura.name] just leaves to go do her own thing."
        "You look down at yourself, seeing patches of blood staining your clothes."
        "The oldest of the cuts almost looks like it started closing already. . ."
    elif dice_roll == 3:
        $ Laura.change_face("confused1", eyes = "down")

        "[Laura.name] looks you up and down."

        $ Laura.change_face("confused1")

        ch_Laura "Why is your heart rate already elevated?" 
        ch_Player "It's just anticipation. . . for all the pain you're about to put me through." 

        $ Laura.change_face("neutral")

        ch_Laura "You're still too sensitive to pain."

        $ Laura.change_face("sly")

        ch_Laura "You'll get used to it."

        "The warm up sucks slightly less than usual."
        "Maybe you are getting used to it."

        $ fade_to_black(0.4)

        "That idea is quickly quashed, as apparently today's training focus is on how to take hits."
        "Thanks to your new situation, she feels comfortable hitting you hard in sensitive places, so you can 'acclimate yourself to the pain'."

        $ fade_in_from_black(0.4)

        show expression "images/effects/green_smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.4)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake

        $ Laura.change_face("angry1", mouth = "smirk")

        "A sharp jab to your liver causes you to instantly crumple."
        "It wasn't particularly forceful, but hurt even more in that moment than breaking your ribs."

        $ Laura.change_face("smirk2")

        ch_Laura "A simple strike to the liver can be especially effective."

        "She actually gives you a minute to recover, before finishing the session with a lighter than usual workout."

        $ Laura.change_face("neutral")

        ch_Laura "That's enough."
        ch_Laura "You don't seem to be bleeding internally, but you're still weak. . ."
        ch_Laura "Best not to push things too far."

        call remove_Characters(Laura) from _call_remove_Characters_146

        "Phantom pains still linger around your midsection, so you don't argue."

    $ ongoing_Event = False

    return