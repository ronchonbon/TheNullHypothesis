init python:

    def Jean_chapter_one_season_four_study_sessions():
        label = "Jean_chapter_one_season_four_study_sessions"

        conditions = [
            "chapter == 1 and season == 4",

            "Jean.History.check('trained_with_Player', tracker = 'season') >= 1",
            
            "Player.behavior == 'studying' and Jean in Player.behavior_Partners and Jean.behavior == 'studying'"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_four_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("smirk2")

        ch_Jean "Alright, [Jean.Player_petname], let's get set up." 
        ch_Player "What's the rush?"

        $ Jean.change_face("confused1")

        "You know how [Jean.name] is, how slowing things down makes her anxious."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "With the music on, you try and get her to relax, exchanging some small talk as you both leisurely organize all the materials."
        "By the time the session actually starts, it's already been quite a while."
        "Although it's relatively unproductive, you treat it more like a hang out than anything else."

        $ Jean.change_face("worried1", mouth = "smirk")

        "She has a hard time neglecting the course materials, but you manage to show her how it's done."
        ch_Player "Oh, by the way."
        ch_Player "Did you know how to do this one?"
        "You point to a particular question."

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Hmm?"
        ch_Jean "Oh, that one?"
        ch_Jean "It's choice D." 

        $ Jean.change_face("smirk2")

        "You actually try to focus a bit near the end of the session, but in the end not much studying actually happened."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "It feels weird. . . not actually trying too hard."
        ch_Jean "It was nice, though."
    elif dice_roll == 2:
        $ Jean.change_face("happy")

        ch_Jean "Gonna turn some music on, [Jean.Player_petname]?" 
        ch_Player "Now you're getting the right idea."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Slowly but surely. . ."
        "You both listen to some good music and exchange small talk, while setting everything up."

        $ Jean.change_face("worried1", eyes = "down", mouth = "smirk")

        "She still can't help but fuss over how things are organized, but at least it's not as bad as it used to be."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "After plenty of procrastination, you hop on the bed next to each other, and she leans into your shoulder."
        "Once the session finally starts, [Jean.name] has you do some easy practice questions."
        "You both try a bit harder during today's session, but it's still fairly laid back compared to how it used to be." 

        $ Jean.change_face("confused1")

        "She's also much better at this whole tutoring thing in general."

        $ Jean.change_face("smirk2")

        ch_Jean "Try this question next."
        ch_Jean "I think it should be pretty easy." 
        "She points to a particular question."
        ch_Player "A bit too easy. . ." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Player "The answer is obviously choice A." 
        "The session ends before either of you know it, as you both end up neglecting the studying and spend a long while chatting."
    elif dice_roll == 3:
        $ Jean.change_face("happy")

        ch_Player "Excited?" 

        $ Jean.change_face("smirk2")

        ch_Jean "Sure am, [Jean.Player_petname]."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Feels weird to be excited about neglecting my studies. . ."
        "Despite her reservations, she procrastinates just as much as you."

        $ Jean.change_face("smirk2")

        "After a long while just listening to music and hanging out, everything's finally set up."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "She gets onto the bed next to you, leaning into your shoulder."
        "As the session finally starts, [Jean.name] keeps getting distracted every time a new song comes on in the background."
        "You're no help, as you encourage it all."

        $ Jean.change_face("confused1", mouth = "smirk")

        "She finally forces things back on track."

        $ Jean.change_face("confused1")

        ch_Jean "Okay, c'mon, why don't you try another question." 
        "She points to a particular question." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Player "Wait, that one?"
        ch_Player "Shit. . ."
        "After taking too long to answer. . ."

        $ Jean.change_face("smirk2")

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp], answer is choice B." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Okay, I think we should actually work on this stuff for you."
        "[Jean.name] makes you go through a bunch of review, as she jams out next to you, occasionally correcting your mistakes." 

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Okay, I think that should be enough."
        ch_Jean "We're not supposed to try too hard, right?" 
        ch_Player "Heh, good point." 

        $ Jean.change_face("sly")

        ch_Jean "I'm learning."
    
    $ ongoing_Event = False

    return