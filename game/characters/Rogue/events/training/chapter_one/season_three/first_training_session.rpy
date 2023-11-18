init python:

    def Rogue_chapter_one_season_three_first_training_session():
        label = "Rogue_chapter_one_season_three_first_training_session"

        conditions = [
            "chapter == 1 and season == 3",
            "Laura.History.check('trained_with_Player', tracker = 'season') or Jean.History.check('trained_with_Player', tracker = 'season')",
            "not Rogue.History.check('trained_with_Player', tracker = 'season')",
            "Player.training == Rogue and Rogue.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_three_first_training_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1")

    ch_Player "What's wrong?"
    ch_Rogue "Nothin'."
    ch_Rogue "Everythin's fine. . ."
    ch_Rogue "Yer able to turn your powers off at will, right?"
    ch_Player "I am now, yeah."
    ch_Player "Why?"
    ch_Rogue "And your nullification, it's on right now?"
    ch_Player "It is. . . pretty much always is, unless I'm training."
    ch_Player "Hey, even if you touched me while it was off, it's not like it would kill me or anything."

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Just keep 'em on while we train, okay. . . ?"

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "{i}Please{/i}."

    $ Rogue.change_face("worried1")

    menu:
        extend ""
        "What's this all about? I don't know what you're so afraid of.":
            $ Rogue.change_face("worried2") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_661 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_662
        "What are you so scared of?! You're freaking me out. . .":
            $ Rogue.change_face("worried1", eyes = "down") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_663
        "Either tell me what you're so afraid of or cut it out.":
            $ Rogue.change_face("appalled1") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_664 

    ch_Rogue "Ah ain't budgin' on this one, [Player.first_name]."

    $ Rogue.change_face("angry1")

    ch_Rogue "Ah'm not messin' around neither. . ."
    ch_Rogue "Everything's fine, so just stop pushin' it."
    ch_Player "Okay, okay."

    $ Rogue.change_face("worried1")

    ch_Player "Let's just get into the training, alright?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Alright."

    $ fade_to_black(0.4)

    "You go through the warm up together, but instead of being laid back as usual, things are tense."
    "[Rogue.name] seems to be stuck in her own head, constantly glancing at you with worried looks."
    "Or is that look one of guilt. . ."

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("worried1", eyes = "right")

    "You try to engage in at least a bit of small talk, but she only gives terse replies."
    "What's gotten into her all of a sudden?"

    menu:
        extend ""
        "If you could just show her she doesn't have anything to be afraid of. . .":
            pass
        "You know what it's like to be scared, but maybe you can show her she doesn't have to be. . .":
            pass
        "She's not being rational, and you should just show her why. . .":
            pass

    "This will be good for her. . . at least that's what you tell yourself."
    "It seems like your sense of curiosity is doing a great job of clouding your judgment."

    $ Rogue.change_face("neutral")

    "[Rogue.name] doesn't seem as distracted once you start actually sparring."
    "Especially after she knows for sure her ability isn't hurting you when you start exchanging blows."

    $ fade_to_black(0.4)

    "Your focus shifts to the powers inside you."
    "They feel similar, yet distinct at the same time."
    "One is kept at bay by your subconscious, the other remains unrestricted."
    "Before you can think too hard about what you're about to do, with some significant mental effort, something changes."
    "You feel the nullification aspect get forced down, now firmly restr-"

    show expression "images/effects/zing.webp" as zing onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.5)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("confused1")

    "While you were focused internally, the sparring session was continuing on as normal, your body mostly on autopilot."
    "The moment you restrained your nullification, your hand brushed against [Rogue.name]'s bare skin as she barely managed to dodge a punch of yours."
    "During that infinitely brief moment of skin-to-skin contact, your instincts, your power, every fiber of your being screams danger."

    with small_screenshake

    "Something you've never felt before, something you didn't even know was a possibility, happens, as your nullification forces it way out."
    "Deep down, you feel like if it hadn't, you would be dead."
    ". . ."
    "Maybe her fears were justified. . ."
    "Outwardly you maintain control of yourself, despite a cold sweat breaking out on your neck."
    "To [Rogue.name] it just looks like you tripped up during sparring."
    ch_Rogue "You alright?"
    ch_Player "Yeah, I'm fine. . ."
    ch_Player "Think I might've pulled something. No biggie."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Maybe we should call it there, [Rogue.Player_petname]."
    ch_Player "That's probably a good idea, but, [Rogue.name]. . ."

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "Ah told you not to push it. . ."
    ch_Player "I wasn't going to."

    $ Rogue.change_face("worried1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("worried1")

    menu:
        extend ""
        "I completely understand if you're not ready to talk about it, and I just want you to know I'll be here if you ever are.":
            $ Rogue.change_face("worried2") 
            
            pause 1.0 
            
            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Thanks. . . ah really do appreciate yer understanding." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_665 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_666
        "Whatever you went through, I can tell it wasn't easy for you. I know what that's like now, and if you ever do want to talk. . .":
            $ Rogue.change_face("worried1", eyes = "down")

            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Ah don't know if ya really do. . . but ah still appreciate it." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_667
        "I don't know what you've been through, but I've been through some shit myself after all of this. Just don't lie to me and pretend like everything's fine.":
            ch_Player "When you do want to talk, I'll be here." 
            
            $ Rogue.change_face("confused2") 
            
            pause 1.0 
            
            $ Rogue.change_face("worried1", eyes = "right")

            ch_Rogue "Ah'm. . . sorry." 
            ch_Rogue "It's hard for me." 
            
            $ Rogue.change_face("worried1") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_668 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_669

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm just not ready to talk about it."

    $ Rogue.change_face("worried2")

    ch_Rogue "And it's not that ah don't trust you or nothin'!"

    $ Rogue.change_face("worried1", eyes = "down") 

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right") 

    ch_Rogue "Ah just can't. . . yet. . ."
    ch_Player "You don't have to justify yourself to me."

    $ Rogue.change_face("worried1") 

    ch_Player "But don't try and hide things from me or pretend like everything's fine."
    ch_Player "Okay?"

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("angry1")

    ch_Rogue "Ah am hidin' things. . . from everyone, not just you."

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "Ah have to."

    $ Rogue.change_face("confused1")

    ch_Rogue "That a problem?"
    ch_Player "Not as long as you're up front about it."

    $ Rogue.change_face("worried2") 

    ch_Player "I don't care if you have things you're not ready to talk about."
    ch_Player "I do care if you lie about it to my face."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm. . . sorry, [Rogue.Player_petname]."
    ch_Player "It's okay, [Rogue.petname]."
    ch_Player "Like I said, when you're ready. . . I'll be here."

    $ Rogue.change_face("worried1", mouth = "smirk") 

    ch_Rogue "Thanks. . . one day, ah promise."
    ch_Player "I'll see you later, okay?"

    $ Rogue.change_face("smirk1") 

    ch_Rogue "Alright, bye hon'."

    call remove_Characters(Rogue) from _call_remove_Characters_202

    $ ongoing_Event = False

    return