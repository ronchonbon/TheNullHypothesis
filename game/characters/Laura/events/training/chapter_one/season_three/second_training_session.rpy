init python:

    def Laura_chapter_one_season_three_second_training_session():
        label = "Laura_chapter_one_season_three_second_training_session"

        conditions = [
            "season == 3",
            "Laura.History.check('trained_with_Player', tracker = 'season') == 1",
            "Player.training == Laura and Laura.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Laura_chapter_one_season_three_second_training_session:
    $ ongoing_Event = True

    $ Laura.change_face("neutral", eyes = "squint")

    "She walks right up to you, a bit too close for comfort."
    ch_Laura "How was your recovery from our last session?"

    menu:
        extend ""
        "Were you worried about me? That's sweet.":
            $ Laura.change_face("suspicious1")

            ch_Laura "Shut up." 
            ch_Laura "Answer the question." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_443
        "Not bad at all.":
            $ Laura.change_face("neutral") 

            ch_Laura "Explain."
        "I'm fine now, but what about you?":
            $ Laura.change_face("confused1")

            ch_Laura "Answer my question first." 
            
            $ Laura.change_face("angry1") 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_444

    ch_Player "Okay, well, I was pretty exhausted for a while afterwards."

    $ Laura.change_face("neutral")

    ch_Player "My power seemed like it went dormant or something."
    ch_Player "Only the new part, not my nullification."
    ch_Player "By the next day, I felt back to normal and had to actively keep it down again."
    ch_Laura "Today we will see if that refractory period can be improved."

    $ Laura.change_face("confused1")

    ch_Player "And what about you?"
    ch_Laura "I felt normal only minutes later."
    ch_Player "Oh. . ."

    $ Laura.change_face("neutral")

    ch_Laura "Time for the warm up."

    $ fade_to_black(0.4)

    "Today's warm up isn't light at all, and she pushes you pretty hard, but you manage to keep up."

    if Player.scholarship == "athletic":
        "It's a bit disconcerting, as you know from firsthand experience, normal athletes don't improve this quickly."

    "Despite how much the previous training session exhausted you, things start off well."
    "Not having to deal with any muscle soreness from prior workouts is pretty nice. . ."

    $ fade_in_from_black(0.4)

    "After the warm up, you work on more hand-to-hand techniques, including some grappling this time."
    "She also introduces you to a couple new weapons, both bladed and otherwise."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "Time to move on."
    ch_Laura "Use your power again."
    ch_Laura "We will spar."

    $ Laura.left_arm_pose = 2

    "The look in her eye doesn't give any room for negotiation."
    "You just brace yourself and let it out."

    $ fade_to_black(0.4)

    $ Player.power = 25

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

    "It was easier to start this time, but you still have basically zero control over how strongly your power expresses itself."
    
    $ Player.power = 50
    
    "It's all or nothing."
    "[Laura.name] doesn't seem to mind and completely dominates you once again."
    "The exhilarating feeling you get from the power is tempered by how easily she seems to overcome it."
    "Whether it was her intention for you to learn this or not, the lesson sinks in. . ."
    "All the power in the world is worthless if you don't know how to use it."

    $ Laura.left_arm_pose = 1

    $ fade_in_from_black(0.4)

    $ Laura.change_face("angry1")

    $ Player.power = 25

    "After several minutes, your power peeters out, and you're left thoroughly exhausted."
    
    $ Player.power = 0
    
    ch_Laura "Slightly better than last time, but not enough."

    $ Laura.change_face("neutral")

    ch_Laura "You get two minutes, then we finish up."
    "You take your two minutes and then struggle through the final work out."
    "When it's finally over, you can barely walk straight."

    $ Laura.change_face("angry1")

    ch_Laura "We have a long way to go."

    call remove_Characters(Laura) from _call_remove_Characters_138

    "With that, she leaves."
    "Training with you is still not enough of a workout apparently."

    $ ongoing_Event = False

    return