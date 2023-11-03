init python:

    def Rogue_chapter_one_season_four_first_study_session():
        label = "Rogue_chapter_one_season_four_first_study_session"

        conditions = [
            "season == 4",
            "not Rogue.History.check('studied_with_Player', tracker = 'season')",
            "Player.studying == Rogue and Rogue.studying"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_four_first_study_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("angry1", eyes = "right")

    pause 1.0

    $ Rogue.change_face("neutral")

    ch_Rogue "Before we start. . ."

    $ Rogue.change_face("confused1")

    ch_Rogue "Can ah ask you a question, [Rogue.Player_petname]?"
    ch_Player "Of course."
    ch_Player "What's up?"

    $ Rogue.change_face("angry1", eyes = "right")

    pause 1.0

    $ Rogue.change_face("worried1")

    ch_Rogue "These classes. . . and all this studyin'. . ."

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "Ah'm really startin' to think it's a waste of time."

    $ Rogue.change_face("worried2")

    ch_Rogue "And not because ah don't like spendin' the time with ya or nothin'!"
    ch_Player "Don't worry, I know what you mean."

    $ Rogue.change_face("worried1")

    ch_Rogue "Well, do ya agree?"

    menu:
        extend ""
        "I. . . don't know. But, you can't think of it that way, [Rogue.name]. What brought this on?":
            $ Rogue.change_face("angry1", eyes = "right")

            ch_Rogue "It's hard not to. . ." 
            
            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_1066
        "I'm. . . not sure anymore. But you're making me worried, is something going on?":
            $ Rogue.change_face("worried1", eyes = "right")

            ch_Rogue "Don't worry, nothin' new. . ." 
            
            call change_Girl_stat(Rogue, "love", 10) from _call_change_Girl_stat_1067
        "Yeah, I think I do. . . but where's this coming from?":
            $ Rogue.change_face("worried2")

            ch_Rogue "You do?" 
            
            call change_Girl_stat(Rogue, "trust", 20) from _call_change_Girl_stat_1068

    $ Rogue.change_face("worried1")

    ch_Rogue "[Player.first_name], it's just. . . with everythin' that's been happenin' lately. . ."

    $ Rogue.change_face("appalled2")

    ch_Rogue "How can anyone justify studyin' so much, instead of trainin', when it nearly gets ya killed?!"

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "And ah'm not talkin' about what happened to me."
    ch_Rogue "Ah mean all the terrible stuff you've had to go through." 
    ch_Rogue "Prof. X thinks it's all so important, but maybe X-23 had the right idea. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "What's it all worth, if ya can't keep the ones you care about safe?"

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Player "I see what you're saying, but no matter how much training either of us did, nothing would've changed."
    ch_Player "Not counting what just happened out in town. . ."

    menu:
        extend ""
        "But, I can tell you for a fact, all this studying hasn't been a waste.":
            $ Rogue.change_face("worried1")
        "But all the studying we've done together hasn't been a waste at all.":
            $ Rogue.change_face("worried1")
        "But, seriously, all the studying hasn't been a waste. I know you don't actually believe that.":
            $ Rogue.change_face("angry1", eyes = "right") 
            
            call change_Girl_stat(Rogue, "love", -5) from _call_change_Girl_stat_1069

    $ Rogue.change_face("confused1")

    ch_Rogue "How do ya mean?"

    $ Rogue.change_face("worried2")

    ch_Player "I mean, even if the time wasn't spent training, it was still spent with you."
    ch_Rogue "Oh. . . ah'm sorry, ah didn't mean it that way."

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "You know ah appreciate every single second ya spend with me."
    ch_Player "I do, and I also appreciate the distraction studying gives me."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "So. . . how about it?"
    ch_Player "I could really use a distraction right about now."
    ch_Rogue "Whatever ya want, [Rogue.Player_petname]."

    $ Rogue.change_face("worried1", eyes = "down")

    "The mood is still a bit tense, as she reluctantly helps you set things up for the session."

    $ Rogue.change_face("worried1", mouth = "smirk")

    "It quickly lightens up, as you tell her about your day, making her laugh a couple times."

    $ Rogue.change_face("smirk2")

    "Today, you take control of the session, even though it's more laid back than usual."
    "Most of the time is just spent chatting, or hanging out, rather than actually studying."
    "There is one question you've been having trouble with, and she's more than happy to help."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "Yeah, this one."
    ch_Player "Just can't seem to figure it out."
    "You point to the question giving you trouble."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah had trouble with that one too."
    ch_Rogue "Here. . ."
    ch_Rogue "This is how ya do it. . . so the answer is choice D."

    "After that, the session deviates away from the studying even more, as [Rogue.name] throws some music on, and you spend the rest of the time hanging out."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "If we're just gonna chill, let's at least clean all this stuff up."
    ch_Rogue "Sure." 

    $ ongoing_Event = False

    return