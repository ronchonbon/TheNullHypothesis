init python:

    def Jean_chapter_one_season_two_second_training_session():
        label = "Jean_chapter_one_season_two_second_training_session"

        conditions = [
            "season == 2",
            "Jean.History.check('trained_with_Player', tracker = 'season') == 1",
            "Player.training == Jean and Jean.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_two_second_training_session:
    $ ongoing_Event = True
    
    $ Jean.change_face("smirk2")

    ch_Jean "So, I've been thinking about your powers since last time."
    ch_Jean "The whole suddenly being super strong and fast thing has been bothering me."
    ch_Jean "Let's start from the beginning."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "What exactly happened when you were attacked that first time?"

    $ Jean.change_face("worried1")

    ch_Jean "That is, if you're okay to talk about it. . ."

    $ choice = None

    menu:
        extend ""
        "I don't mind at all. If anything, it'd be good to tell someone about the details.":
            $ Jean.change_face("smirk1") 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_210 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_211

            $ choice = "A"
        "I. . . I'll try. Not like I can ever forget how it felt. . .":
            $ Jean.change_face("worried2") 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_212

            $ choice = "B"
        "I guess I can. . . really didn't want to relive those memories, but fine.":
            $ Jean.change_face("worried1", eyes = "left") 
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_213 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_214

            $ choice = "C"

    "You tell her about that day, mentioning all the details you can remember."

    $ Jean.change_face("confused1")

    ch_Jean "So you suddenly felt sick and left class?"
    ch_Jean "And he attacked you in the bathroom?"
    ch_Player "Yeah, is that something he could've done to me himself?"
    ch_Player "Maybe so I was all alone?"
    ch_Jean "Maybe. . ."

    $ Jean.change_face("confused1", eyes = "squint")

    ch_Jean "But why would he do it in the middle of a big lecture and not call you into his office hours or something?"
    ch_Player "That's true."

    if choice == "A":
        ch_Player "Wait a minute. . . I think I remember now." 

        $ Jean.change_face("confused1") 

        ch_Player "I was watching a news report about some recent attacks the moment I felt sick." 
        ch_Player "Could my powers appearing have been the result of an emotional reaction?" 

        $ Jean.change_face("surprised1") 

        ch_Jean "Could be!"
    else:
        ch_Player "I. . . can't really remember the exact moment I felt sick. . ." 
        ch_Player "I kinda suppressed that whole day. . ." 

        $ Jean.change_face("worried1")

        ch_Player "It was definitely very stressful, could that have something to do with it?"

        $ Jean.change_face("worried1")

        ch_Jean "Definitely." 

    if Player.visible_mutation:
        ch_Player "But, I do know my appearance didn't change until I was in the bathroom."

    $ Jean.change_face("worried1")

    ch_Jean "And what about this new thing?"
    ch_Jean "With Juggernaut and all. . ."
    ch_Player "I mean that was also super stressful. . ."
    ch_Player ". . . seeing [Rogue.name] injured like that."

    $ Jean.change_face("worried2")

    ch_Jean "I think that's enough for now."
    ch_Jean "I don't like seeing you all sad like this. . ."

    $ Jean.change_face("worried1")

    ch_Jean "Just, if you can, try and think about the details, they could be important."
    ch_Player "I will, thanks [Jean.petname]."

    $ Jean.change_face("smirk1")

    ch_Jean "Alright, now into the real training."

    call Jean_activate_psychic from _call_Jean_activate_psychic_29

    $ fade_to_black(0.4)

    "Instead of haphazardly flinging tennis balls in your direction, she has you focus on one ball at a time."
    "After nearly an hour of trying, you get extremely close."
    "Maybe it had something to do with all the emotions stirred up by your previous conversation, but you feel like you're on the cusp of succeeding." 

    $ fade_in_from_black(0.4)

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_29

    $ Jean.change_face("worried1")

    ch_Player "Wait, why'd you stop?"
    ch_Player "I almost had it that time!"

    $ Jean.change_face("worried2")

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp], you've been saying that for an hour."

    $ Jean.change_face("neutral")

    ch_Jean "Trying to force it isn't a good idea."
    ch_Jean "Let's just do some sparring, okay?"
    ch_Player "Yeah. . . okay."

    $ Jean.change_face("smirk2")

    ch_Jean "Good."
    "While [Jean.name] has clearly been practicing, your new advantages make it a less than even fight."
    "She doesn't seem too bothered, mostly happy that you can actually defend yourself now."

    $ Jean.change_face("sly")

    call Jean_activate_psychic from _call_Jean_activate_psychic_30

    "That doesn't mean she won't try to overshadow you, as she cheats with her powers a bit."
    "Tennis balls dropping on your head are a constant distraction, and even as you finish the sparring, she continues to flaunt her abilities."

    $ Jean.change_face("worried1")

    "It seems like she's getting better at determining just how much she can do without losing control."

    $ Jean.change_face("worried2")

    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_30

    "You feel a slight vibration in the air, and [Jean.name] immediately shut her powers off."

    $ Jean.change_face("worried1", mouth = "lipbite")

    ch_Jean "That was a bit close. . ."
    ch_Player "But also better than last time, I could tell."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Thanks, [Jean.Player_petname]."
    ch_Jean "Let's call it there."
    ch_Jean "Seems like we could both use a rest."
    ch_Jean "I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_61

    $ ongoing_Event = False

    return