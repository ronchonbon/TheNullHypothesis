init python:

    def Jean_chapter_one_season_one_third_training_session():
        label = "Jean_chapter_one_season_one_third_training_session"

        conditions = [
            "chapter == 1 and season == 1",
            
            "Jean.History.check('trained_with_Player', tracker = 'season') == 2",

            "Player.behavior == 'training' and Jean in Player.behavior_Partners and Jean.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_one_third_training_session:
    $ ongoing_Event = True

    $ Jean.change_face("happy")

    ch_Player "Ready to warm up?" 

    $ Jean.change_face("smirk2")

    ch_Jean "Yep!" 
    ch_Jean "Today's gonna be good, I can feel it."

    $ fade_to_black(0.4)

    "You both do some light cardio and stretching before the session starts."

    $ fade_in_from_black(0.4)

    ch_Jean "I have an idea, let's do things a bit differently today." 

    call Jean_activate_psychic from _call_Jean_activate_psychic_11

    "This time, she floats a tennis ball directly above your head."
    ch_Jean "Try touching me."
    ch_Jean "Let's see how those instincts react now."
    ch_Player "Huh. . . so if my nullification works, it'll actually cause me to get hit." 

    $ Jean.change_face("happy")

    ch_Jean "Yep! Maybe this will incentivize your power not to turn on."
    ch_Jean "I'm basically a genius." 

    $ Jean.change_face("smirk2")

    "Unfortunately, things aren't quite so simple."
    "You touch Jean. . ."

    $ Jean.change_face("surprised2")

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_11

    "The tennis ball falls and hits you on the head."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "Damnit."
    ch_Player "It was a good idea."
    ch_Jean "Let's keep trying, see if anything changes."

    call Jean_activate_psychic from _call_Jean_activate_psychic_12

    $ fade_to_black(0.4)

    "You try again and again, but the tennis ball just keeps falling."
    "No matter how hard you focus, you just can't get a hold of your power."
    "After a few more attempts, something finally changes."

    $ fade_in_from_black(0.4)

    $ Jean.change_face("surprised2")

    "You make contact with [Jean.name]. . ."
    "This time, the ball stays in the air while you're touching her."

    $ Jean.change_face("happy")

    ch_Player "It's working!"

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_12

    "Right as you open your mouth, the ball falls and bonks you on the head."

    $ Jean.change_face("confused1", mouth = "smirk") 

    ch_Jean "Heh, well it worked for a second there." 

    $ Jean.change_face("smirk2")

    ch_Player "Barely. . ." 
    ch_Player "As soon as I lost focus, it fell."
    ch_Player "Seems like having a 'Sword of Damocles' looming over my head helped somewhat." 

    $ Jean.change_face("happy")

    ch_Jean "You're welcome." 

    $ Jean.change_face("smirk2")

    ch_Jean "And don't worry, control always takes a while." 
    ch_Jean "But it's like riding a bike. Once you get it in the first place, it becomes easier."

    $ Jean.change_face("smirk1")

    ch_Jean "Let's go again, and maybe I'll give the ball a little downward push this time."

    call Jean_activate_psychic from _call_Jean_activate_psychic_13

    $ fade_to_black(0.4)

    "She must've meant to say a 'very hard downward push'. . ."
    "You try for another hour and manage to succeed a few more times."
    "It's very inconsistent and seems to get more difficult as time goes on."

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_13

    "By the end, you can barely think straight, and she suggests switching things up."
    "You both do some sparring practice before Jean goes through control exercises with her own power."

    call Jean_activate_psychic from _call_Jean_activate_psychic_14

    "Her control is leagues better than yours, and you can even tell her raw output is better than last time. . ."

    $ Jean.change_face("happy")

    "That is until she takes it too far."

    $ Jean.change_face("worried4")

    ch_Jean "Oh shit!"
    "You rush over and grab her hand."

    $ Jean.change_face("surprised2") 

    pause 1.0

    $ Jean.change_face("worried1")

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_14

    ch_Jean "Thanks."
    ch_Jean "I think that's enough for today. . ." 
    ch_Jean "I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_55

    $ ongoing_Event = False

    return