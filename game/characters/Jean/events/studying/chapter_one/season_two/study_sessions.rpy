init python:

    def Jean_chapter_one_season_two_study_sessions():
        label = "Jean_chapter_one_season_two_study_sessions"

        conditions = [
            "chapter == 1 and season == 2",
            
            "Player.behavior == 'studying' and Jean in Player.behavior_Partners and Jean.behavior == 'studying'"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_two_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if not Jean.History.check("studied_with_Player", tracker = "season") or dice_roll == 1:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "So. . ." 

        if Player.History.check("studied", tracker = "weekly") >= 2:
            $ Jean.change_face("smirk2") 
            $ Jean.change_arms("hips")
            
            ch_Jean "You've been doing pretty well in class lately."
        else:
            $ Jean.change_face("worried1", mouth = "smirk") 
            $ Jean.change_arms("crossed")
            
            ch_Jean "Seems like you've been struggling in class a bit."

        $ Jean.change_face("sly")
        $ Jean.change_arms("sass")

        ch_Player "H-"
        ch_Jean "Don't ask how I know."

        $ Jean.change_face("smirk2")

        ch_Jean "Let's just get started."

        $ Jean.change_arms("crossed")

        if Player.History.check("studied", tracker = "season") >= 5: 
            ch_Jean "Gotta work on keeping those grades up for you."
        else:
            ch_Jean "Gotta work on getting those grades up for you."

        "It only takes a few minutes to set everything up."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "She takes her usual spot on the bed, brushing up against you."
        "[Jean.name] takes charge more than usual, going through all your weakest subjects."

        $ Jean.change_face("confused1", mouth = "smirk")

        "It is a bit suspicious. . . how she knows exactly where your grades are the weakest, despite never actually telling her."
        "You just chalk it up to her knowing after all the studying you've done together."
        "Surely that's the only reason why she knows so much."

        $ Jean.change_face("smirk2")

        ch_Player "Yeah, I was having trouble with this question as well."
        "You point to one of the more difficult practice questions."

        $ Jean.change_face("confused1", mouth = "smirk")
        $ Jean.change_arms("hips")

        ch_Jean "That?"
        ch_Jean "C'mon, [Jean.Player_petname], that one's easy."

        $ Jean.change_face("worried1", mouth = "smirk")
        $ Jean.change_arms("sass")

        ch_Player "Heh, uhm. . ." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Really, [Jean.Player_petname]?"

        $ Jean.change_face("smirk2")

        ch_Jean "Okay, okay, it's choice C." 
        "[Jean.name]'s high expectations for herself, also bleed over into her expectations for you."

        if Player.scholarship == "academic":
            "Despite all your prior academic experience, you still struggle to live up to them."
        else:
            "You might not have been the worst student in the past, but living up to her expectations is nigh impossible for anyone."

        $ Jean.change_face("sly")
        $ Jean.change_arms("crossed")

        ch_Jean "Let's call it there."

        $ Jean.change_face("smirk2")

        ch_Jean "Don't wanna push you {i}too{/i} hard."

        $ Jean.change_face("sly")

        ch_Player "Not sure I believe you. . ."
    elif dice_roll == 2:
        $ Jean.change_face("happy")
        $ Jean.change_arms("sass")

        ch_Jean "You gonna set it all up for me today, [Jean.Player_petname]?" 
        ch_Player "You're not gonna help?"

        $ Jean.change_face("confused1", mouth = "smirk")
        $ Jean.change_arms("crossed")

        ch_Jean "Well, I guess I could. . ."
        ch_Player "Please. . . ?"

        $ Jean.change_face("sly")
        $ Jean.change_arms("hips")

        ch_Jean "How can I say no to that?"
        
        if Jean in Partners:
            "She gives your ass a light smack before moving to help."
        else:
            "She moves to help you." 

        $ Jean.change_face("smirk2")

        "It takes a couple minutes to set up, before you jump onto the bed next to her."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)
        $ Jean.change_arms("crossed")

        "As the session starts, you realize how much better [Jean.name]'s gotten at this whole teaching thing."
        "Instead of bombarding you with way too much information at once or having sky high expectations, she's actually quite reasonable." 

        $ Jean.change_face("confused1", mouth = "smirk")

        "She still struggles a bit with making things easy to understand, but not for lack of trying." 

        $ Jean.change_face("smirk2")
        $ Jean.change_arms("hips", left_arm = "extended")

        ch_Jean "Okay, [Jean.Player_petname], I think you should be able to do this one." 
        "She points to a particular question."

        $ Jean.change_arms("hips")

        ch_Player "Hmm. . ." 

        $ Jean.change_face("confused1", mouth = "smirk") 

        ch_Player "It's choice D." 

        $ Jean.change_face("happy")
        $ Jean.change_arms("sass")

        ch_Jean "Right!"

        $ Jean.change_face("smirk2")

        ch_Jean "Good job."
        "The session ended up being quite productive."
    elif dice_roll == 3:
        $ Jean.change_face("happy")
        $ Jean.change_arms("sass")

        ch_Jean "I'll help setup." 

        $ Jean.change_face("smirk2")

        ch_Jean "You're welcome, [Jean.Player_petname]."
        "You've done this enough to know how [Jean.name] likes to organize things."
        "With the two of you together, it barely takes a few minutes."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)
        $ Jean.change_arms("crossed")

        "She gently pushes you onto the bed, before jumping down right next to you."
        "[Jean.name] lets you take the lead at the start, and you point out subjects you've been struggling with or questions you couldn't figure out."

        $ Jean.change_face("confused1", mouth = "smirk", eyes = "down") 

        "Under her direction, you're able to get nearly all the answers you've been looking for." 

        $ Jean.change_face("sly")
        $ Jean.change_arms("hips", left_arm = "extended")

        ch_Jean "Here. . . why don't you try this one." 
        "She points to a particular question." 

        $ Jean.change_face("surprised1")
        $ Jean.change_arms("sass")

        ch_Player "Oh, that one's easy." 
        ch_Player "It's choice B." 

        $ Jean.change_face("confused1", mouth = "smirk")
        $ Jean.change_arms("crossed")

        "Seems like she wasn't expecting you to know that answer."
        "Feels good to surprise her with your knowledge for once. . ."

        $ Jean.change_face("sly")

        ch_Jean "Have you been studying ahead?"
        ch_Player "No. . . I just remember that one from class."

        $ Jean.change_face("worried1")

        ch_Jean "Am I the only one who studies ahead?"
        ch_Player "Probably not. . ." 

        $ Jean.change_face("worried1", mouth = "smirk")
    
    $ ongoing_Event = False

    return