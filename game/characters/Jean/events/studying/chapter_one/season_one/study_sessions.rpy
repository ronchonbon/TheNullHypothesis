init python:

    def Jean_chapter_one_season_one_study_sessions():
        label = "Jean_chapter_one_season_one_study_sessions"

        conditions = [
            "season == 1",
            "Jean.History.check('trained_with_Player', tracker = 'season') >= 1",
            "Player.studying == Jean and Jean.studying"]

        priority = 99
        repeatable = True

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Jean_chapter_one_season_one_study_sessions:
    $ ongoing_Event = True

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "You gonna help me set this stuff up, [Jean.Player_petname]?" 
        ch_Player "Sure."

        $ Jean.change_face("smirk2")

        ch_Jean "Good."
        "Despite [Jean.name]'s obsessiveness about where things should go, it only takes a few minutes to set everything up."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "She plops down on the bed, 'accidentally' bumping into you, as she gets comfortable."
        "[Jean.name] takes charge, running you through the topics she thinks are most important."

        $ Jean.change_face("confused1", mouth = "smirk")

        "The thing is. . . she keeps going past what you were expected to learn, touching on more advanced topics, as if she imagined you would go ahead in the material like she does."

        ch_Player "We didn't go over this in class yet. . ."

        $ Jean.change_face("smirk2")

        ch_Jean "Okay, this one should actually be relevant."
        "She points to one of the more difficult practice questions."
        ch_Player "Uhhh. . ." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Really, [Jean.Player_petname]?"

        $ Jean.change_face("smirk1")

        ch_Jean "It's obviously choice C." 
        "For the rest of the session, she does her best to not go too far ahead in the material."
        "After only a couple hours, your brain feels like mashed potatoes."

        $ Jean.change_face("sly")

        ch_Jean "I think we should stop there."
        ch_Jean "You look like you could use a break."
        ch_Player "Thanks. . ."
    elif dice_roll == 2:
        $ Jean.change_face("happy")

        ch_Jean "You excited, [Jean.Player_petname]?" 
        ch_Player "Excited. . . ?"

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Well, yeah. . ."

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "You never get excited to study?"

        if Player.scholarship == "athletic" or Player.History.check("studied") >= 3:
            ch_Player "I don't know about excited. . . but it's not completely unenjoyable."
        else:
            ch_Player "I wouldn't say that. . ."

        $ Jean.change_face("sly")

        ch_Jean "Well, help me set this stuff up already."
        "As you both organize everything, she 'accidentally' brushes against you a couple times."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "She gets onto the bed next to you, inching closer."
        "Once the session starts, you ask some questions, and [Jean.name] basically starts teaching an entire course to you as she goes over the answers."
        "As usual, she could probably be a professor with how much she knows about the current topic." 

        $ Jean.change_face("confused1")

        "Maybe not the greatest professor, though. . ."
        "She tries quite hard to help you, but struggles with making things easily digestible."

        $ Jean.change_face("smirk2")

        ch_Jean "Okay you should definitely know this already, and it'll be the quiz question this week for sure." 
        "She points to a particular question."
        ch_Player "Hehe, uhm. . ." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Aw, c'mon, it's easyyy."
        ch_Jean "The answer is obviously choice D." 
        "By the end of the session, you have learned a lot, but [Jean.name] also managed to make some things even more confusing. . ."
    elif dice_roll == 3:
        $ Jean.change_face("happy")

        ch_Player "Want some help?" 

        $ Jean.change_face("smirk2")

        ch_Jean "Sure do, [Jean.Player_petname]."
        "You 'helping' mostly means you end up doing most of the organizing, under [Jean.name]'s instruction."

        $ Jean.change_face("smirk2", eyes = "down", blush = 1)

        "She not so subtly checks you out several times, before teasingly shoving you onto the bed and plopping down next to you."
        "As the session starts, [Jean.name] tries her best to go over the subjects you've been struggling with, but she has trouble dumbing things down."

        $ Jean.change_face("worried1", eyes = "down") 

        "She's used to her higher level courses, and you have to point out concepts you haven't learned yet."

        $ Jean.change_face("confused1")

        ch_Player "Yeah. . . don't think I learned this yet." 
        "You point to a particular question." 

        $ Jean.change_face("happy")

        ch_Jean "Great, then you'll get a head start on everyone else!"

        $ Jean.change_face("smirk2")

        ch_Jean "The answer is choice C." 

        $ Jean.change_face("confused1")

        "[Jean.name] was getting a bit fed up, so by the end of the session, she just started teaching you the higher level concepts."
        "They do clarify some questions you had, but most of the info won't be relevant for a while. . ."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "I think you've had enough. . ."
        ch_Jean "Don't wanna push you too hard."
        ch_Jean "Just chill while I put everything away."
        ch_Player "Thanks, [Jean.petname]. . ." 

        $ Jean.change_face("smirk2")

        ch_Jean "Of course."

    $ ongoing_Event = False

    return