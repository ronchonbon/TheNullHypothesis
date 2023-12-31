init python:

    def Rogue_chapter_one_season_two_first_training_session():
        label = "Rogue_chapter_one_season_two_first_training_session"

        conditions = [
            "season == 2",
            "Laura.History.check('trained_with_Player', tracker = 'season')",
            "not Rogue.History.check('trained_with_Player', tracker = 'season')",
            "Player.training == Rogue and Rogue.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_two_first_training_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "How ya been feelin', [Rogue.Player_petname]?"
    ch_Player "Better than ever, actually."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "Ah thought ya broke a few ribs or somethin'?"
    ch_Player "I did."
    ch_Player "Hit my head pretty hard too. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "And yer already healed?"
    ch_Rogue "Don't ribs usually take a real long time to heal?"
    ch_Player "Usually."
    ch_Player "Sure surprised the hell out of the doctor too."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "[Charles.name] thinks I have a 'robust constitution' as a by-product of my power."
    ch_Player "Which would explain the healing."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm glad, but. . ."
    ch_Rogue "What about how yer doin'. . . mentally. . . ?"

    menu:
        extend ""
        "Mentally, I've been better, but that doesn't mean I regret what I did.": 
            $ Rogue.change_face("worried2")

            ch_Rogue "Ah'm just sorry. . . ya had to get hurt for me. . ." 
            
            $ Rogue.change_face("worried1", eyes = "down") 
            
            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_678 
            call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_679
        "Not. . . great. It honestly shook me up pretty bad. Just trying not to think about it.": 
            $ Rogue.change_face("worried1", eyes = "down")

            ch_Rogue "Ah'm sorry. . . it's all my fault. . ." 
            
            $ Rogue.change_face("worried1", eyes = "right") 
            
            ch_Rogue "Ah was useless." 
            
            call change_Girl_stat(Rogue, "love", 10) from _call_change_Girl_stat_680
        "I'm fine. Angry, if anything, that I was so useless.":
            $ Rogue.change_face("worried2")

            ch_Rogue "Ya weren't useless!" 
            
            $ Rogue.change_face("worried1", eyes = "down") 
            
            ch_Rogue "Ah might be dead. . . if not for you." 
            
            call change_Girl_stat(Rogue, "trust", 20) from _call_change_Girl_stat_681

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah hate needin' to be rescued."

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "Wish ah could actually do somethin' with my power."
    ch_Player "It's not your fault."
    ch_Player "You were knocked out before you even knew what happened."

    $ Rogue.change_face("worried1")

    ch_Player "I don't blame you."
    ch_Player "So don't blame yourself either."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks, [Rogue.Player_petname]. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "And thanks for comin' to train with me. . ."
    ch_Rogue "Even if ya can't help me with my powers."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah appreciate the company."
    ch_Player "Of course, [Rogue.petname]."
    ch_Player "Wanna get into it?"
    ch_Player "I could really use the distraction."

    $ Rogue.change_face("smirk1")

    ch_Rogue "Yeah, me too."

    $ fade_to_black(0.4)

    "You spend as much time chatting, as you do actually warming up."
    "She makes you chuckle here and there, and you do the same."
    "After just a few minutes, your minds have wandered far away from the event that nearly killed you both."

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("smirk2")

    "Her fighting skills have sharpened since last you trained together, mirroring her determination to not be useless in the future."

    if Laura.History.check("trained_with_Player") >= 5:
        $ Rogue.change_face("surprised2") 
        
        "You haven't been slacking off either, and the combination of your improving skills - and improved physique - puts [Rogue.name] on the back foot for most of the session."
    else:
        "Your newly improved physique gives you an edge during training, but her technique is still far superior." 
        
        $ Rogue.change_face("sly") 
        
        "She manages to keep you on the back foot for most of the session."

    $ Rogue.change_face("smirk2")

    "Hours pass, and the session is over before you know it." 
    "It wasn't a physical beatdown like with [Laura.name], nor was it the mental gymnastics you have to endure with [Jean.name]."
    "It was just. . ."
    ch_Player "That was pretty relaxing."

    $ Rogue.change_face("worried1", mouth = "open")

    ch_Player "Feels nice to not be in some kind of agony after training."

    $ Rogue.change_face("confused1", mouth = "open")

    ch_Rogue "*Huff* What in the hell are those girls makin' you do? *huff*"
    ch_Player "They must like seeing me in pain or something. . ."
    "She takes a moment to catch her breath."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah'm glad yer feelin' relaxed."
    ch_Rogue "That was a pretty good workout for me."

    $ Rogue.change_face("smirk2", eyes = "down")

    ch_Rogue "That new 'constitution' of yers. . ."

    $ Rogue.change_face("smirk2", mouth = "lipbite")

    ch_Rogue "It's quite somethin'."
    ch_Player "Heh, thanks. . ."
    ch_Player "Wanna call it there for now?"

    $ Rogue.change_face("smirk2")

    ch_Rogue "Sure, [Rogue.Player_petname]."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Maybe you could come find me later?"

    call remove_Characters(Rogue) from _call_remove_Characters_205

    call change_Girl_stat(Rogue, "trust", 20) from _call_change_Girl_stat_682

    $ ongoing_Event = False

    return