init python:

    def Rogue_chapter_one_season_four_first_training_session():
        label = "Rogue_chapter_one_season_four_first_training_session"

        conditions = [
            "season == 4",
            "Jean.History.check('trained_with_Player', tracker = 'season')",
            "not Rogue.History.check('trained_with_Player', tracker = 'season')",
            "Player.training == Rogue and Rogue.training"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_four_first_training_session:
    $ ongoing_Event = True

    $ Rogue.change_face("neutral")

    ch_Rogue "So. . ."
    ch_Player "So?"

    $ Rogue.change_face("neutral", eyes = "right")

    ch_Rogue "Why are you trainin' with me?"
    ch_Player "[Rogue.name]. . . what are you talking about?"

    $ Rogue.change_face("appalled1")

    ch_Rogue "Why are ya wastin' yer time 'training' with me?!"

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "We both know ah can't teach ya anything the other girls can."
    ch_Rogue "Ah reckon you'd be better off just trainin' with one of them."

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "Lord knows ah ain't got nothin' worthwhile to pass on. . . can't even figure out my own shit."

    $ Rogue.change_face("angry1")

    ch_Rogue "And don't tell me yer here because ya feel sorry for me."
    ch_Rogue "That would only make it worse."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah'm sick of people feelin' sorry for me. . ."

    if Rogue.petname not in ["Anna Marie"]:
        $ temp = Rogue.petname.capitalize()
    else:
        $ temp = Rogue.petname

    menu:
        extend ""
        "[temp], spending time with you is worth so much to me. I'm not here out of pity.":
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_644 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_645
        "I'm not here because I pity you. Did you really think that was the only reason?":
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_646
        "Could you even imagine, for just one second, that maybe I actually have a good reason to be here? This isn't a pity party.":
            $ Rogue.change_face("angry1", eyes = "right") 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_647 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_648

    $ Rogue.change_face("worried1")

    ch_Player "You give me something none of the other girls can."

    $ Rogue.change_face("confused1")

    ch_Player "With them, learning about the weight of our powers and how to use them to good effect is {i}fucking stressful{/i}."
    ch_Player "Especially after. . . I nearly killed all those people. . ."
    ch_Player "It only made things worse."
    ch_Player "But you know what's just as important, maybe even more so?"

    $ Rogue.change_face("worried1")

    ch_Player "Learning how to relax and feel like a normal fucking person."

    $ Rogue.change_face("worried2")

    ch_Player "I'm not saying [Laura.name] or [Jean.name] are bad people, or that I can't relax around them. . ."

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Player "But with you. . . it's just so easy."
    ch_Player "I don't think you realize how much of a positive impact you've had on me ever since I got here."

    $ Rogue.change_face("worried1")

    if Rogue in Partners:
        ch_Player "Even if we weren't together, you've been a better friend than I probably deserve."
    else:
        ch_Player "You've been a better friend than I probably deserve."

    $ Rogue.change_face("worried2")

    ch_Player "That a good enough reason?"
    ch_Rogue "Yes. . . of course it is."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah just never expected. . ."
    ch_Rogue "Yer bein' honest with me?"
    ch_Player "One hundred percent."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks, [Rogue.Player_petname]. . ."
    ch_Rogue "Can we. . . get into the trainin' then?"
    ch_Rogue "Ah've got a lot on my mind and have been fixin' for a smackdown."
    ch_Player "You want me to spank you that badly?"

    $ Rogue.change_face("surprised2")

    ch_Player "Fine, if you {i}really{/i} want me to. . ."

    if Rogue in Partners and approval_check(Rogue, threshold = [600, 600]):
        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1) 
        
        ch_Rogue "Ah'd think it shouldn't be too much of a surprise. . ." 
        
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        ch_Rogue "If ya don't want me to resist. . . just say the word, [Rogue.Player_petname]. . ." 
        
        $ Rogue.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1)
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        ch_Rogue "Well. . . not that ah {i}want{/i} ya to or nothin'. . ." 
        ch_Rogue "Ah just. . . ah didn't. . ." 
        ch_Rogue "Ah didn't mean it like that. . ." 
        
        $ Rogue.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Player "Wait. . . no I didn't me-"
    "While you're momentarily taken off guard by whatever just happened, she takes the opportunity to strike."

    $ Rogue.change_face("sly")

    "You're able to react in time after your brain barely manages to stop thinking about. . . things. . ."
    "She played you like a fiddle."
    "Credit where credit is due, but that doesn't mean you let her have her way with you."
    "The sparring session is more intense than normal and also feels a lot more fun."

    $ Rogue.change_face("happy")

    "[Rogue.name] seems to have dropped the sullen demeanor from the start of the session and looks like she's having a great time as well."

    $ Rogue.change_face("smirk2")

    "Once she runs out of steam and sparring any longer would only provide diminishing returns, you both settle into an easy pace doing workouts for the rest of the session."
    "Sharing small talk and just generally enjoying each other's company, the time goes by fast."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks, [Player.first_name]."
    ch_Rogue "For everythin'. . ."
    ch_Rogue "For not feelin' so sorry for me like everyone else. . . for bein' a great friend to me too. . ."

    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah. . . wanna have a talk. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "But not here."
    ch_Rogue "Can ya meet me in my room in a few minutes?"
    ch_Rogue "Please?"
    ch_Rogue "This is important to me. . ."
    ch_Player "Of course."
    ch_Player "I'll change, take a quick shower, and be right over."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks, [Rogue.Player_petname]."
    ch_Rogue "See ya soon. . ."

    call remove_Characters(Rogue) from _call_remove_Characters_314

    "You head to the locker room."

    call remove_Characters(location = "bg_lockers", fade = False) from _call_remove_Characters_197
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_209

    "You quickly wash off and change out of your workout clothes."

    $ Player.showering = True
    $ shower_steam = True

    $ Player.sweat = 0
    $ Player.chlorine = 0
    $ Player.spunk = False
    $ Player.saliva = False
    $ Player.grool = False
    $ Player.dirty_cock = False
            
    pause 5.0

    $ fade_to_black(0.4)

    pause 2.0

    $ Player.showering = False

    $ fade_in_from_black(0.4)

    call remove_Characters(location = "bg_girls_hallway", fade = False) from _call_remove_Characters_198
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_210
    call knock_on_door(times = 2) from _call_knock_on_door_22

    ch_Player "[Rogue.name]?"
    ch_Player "It's me."
    "The door quickly opens, and you're dragged inside."

    call remove_Characters(location = Rogue.home, fade = False) from _call_remove_Characters_315
    call send_Characters(Rogue, Rogue.home) from _call_send_Characters_164
    call set_the_scene(location = Rogue.home) from _call_set_the_scene_211

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thanks for comin' so quick."

    if Rogue.petname not in ["Anna Marie"]:
        $ temp = Rogue.petname.capitalize()
    else:
        $ temp = Rogue.petname

    ch_Player "[temp], what's this about?"

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ya know how ah told ya ah was hidin' stuff from everyone. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "There are some things that ah still can't tell ya. . ."
    ch_Rogue "Ah'm sorry."
    ch_Rogue "But there is somethin' ah wanted to share with you."
    ch_Rogue "Somethin' only a couple of other people know."
    ch_Player "No pressure from me, [Rogue.name]."
    ch_Player "Whatever you're comfortable with."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Rogue "Thanks. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ya really make it so easy. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "But. . . the thing ah wanted to tell ya. . . was what happened the first time ah got my powers."
    ch_Rogue "And why ah've had so much trouble with 'em, even after all these years."
    ch_Rogue ". . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "When ah was in high school, ah had this friend."
    ch_Rogue ". . . {i}best{/i} friend."

    $ Rogue.change_face("worried1")

    ch_Rogue "We were real close. . . and eventually, became more than friends."
    ch_Rogue "Ah was his first girlfriend, he was my first boyfriend."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "We were together for a little while, and we held hands 'n all, but never more than that."
    ch_Rogue "Ah don't really remember why, but one day, we were hangin' out. . ."

    $ Rogue.change_face("worried1")

    ch_Rogue "And ah had my first kiss."

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "Only, that's exactly when my powers decided to kick in."

    $ Rogue.change_face("angry1")

    ch_Rogue "Of course it had to be right then."
    ch_Rogue "Ah couldn't stop it, ah was just as helpless as he was."

    $ Rogue.change_face("worried1")

    ch_Rogue "And it didn't just hurt him. . . it nearly killed him."
    ch_Rogue "Put him in a coma. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "One that he's still in to this day."
    ch_Rogue "And that's why ah'm all messed up in the head. . . can't control my powers or nothin'."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ah just. . . thought it might help ya. . . to know that it's not yer fault, what happened to those people that attacked you."
    ch_Rogue "You couldn't control what happened, just like ah couldn't."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "And yer not the only one whose power has almost killed someone."

    menu:
        extend ""
        "Thank you, [Rogue.name], It does help. I really appreciate you opening up to try and help me like this.":
            $ Rogue.change_face("worried1", mouth = "smirk")
            
            if Player.History.check("told_Rogue_did_what_had_to_do_during_mutant_hate"):
                ch_Rogue "Ah don't know how yer always so level-headed about it. . ." 
                ch_Rogue "Ah hope you don't feel sorry for those people that attacked you." 
                
                $ Rogue.change_face("angry1") 
                
                ch_Rogue "You gave 'em what they deserved." 
                
                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_649 
                call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_650
            else:
                ch_Rogue "That doesn't mean you should feel sorry for 'em, though." 
                
                $ Rogue.change_face("angry1") 
                
                ch_Rogue "In your situation, with them tryin' to kill you and all, they got what they deserved." 
                
                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_651 
                call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_652
        "I. . . thank you, it does help. It's just so scary how dangerous our powers can be when we don't know what we're doing. . .":
            $ Rogue.change_face("worried1", mouth = "smirk")
            
            if Player.History.check("told_Rogue_was_scared_during_mutant_hate"):
                ch_Rogue "You been alright, [Rogue.Player_petname]?" 
                ch_Rogue "And please don't feel bad for those people. . . they tried to kill you." 
                
                $ Rogue.change_face("angry1") 
                
                ch_Rogue "They got what they deserved."
                
                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_653
            else:
                ch_Rogue "I know, hon', trust me. . ." 
                
                $ Rogue.change_face("angry1") 
                
                ch_Rogue "But yer situation ain't the same as mine. . . those people got what they deserved." 
                
                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_654
        "I appreciate you trying to help, and I'm sorry you had to go through something like that, but I know it's not my fault. They made a choice, and I'm comfortable with how I responded.":
            $ Rogue.change_face("worried1")
            
            if Player.History.check("told_Rogue_protesters_had_it_coming_during_mutant_hate"):
                ch_Rogue "Good. . ." 
                ch_Rogue "Ah don't want you to feel sorry for them or nothin'." 
                
                $ Rogue.change_face("angry1") 
                
                ch_Rogue "They got what they deserved for hurtin' you." 
                
                call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_655
            else:
                ch_Rogue "Ah'm glad yer startin' to agree. . ." 
                ch_Rogue "You shouldn't feel sorry for those people." 
                
                $ Rogue.change_face("angry1") 
                
                ch_Rogue "They got what was comin' for tryin' to hurt you." 
                
                call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_656 

    $ Rogue.change_face("worried1")

    ch_Rogue "Also. . ."
    ch_Rogue "There's more to the story. . . after what ah did."
    ch_Rogue "But ah'm not ready to tell ya everything yet."
    ch_Player "It's okay, [Rogue.petname]."
    ch_Player "I just appreciate how much you've opened up so far."
    ch_Player "Take your time, there's no rush."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Thank you."

    $ Rogue.change_face("worried1")

    ch_Rogue "Now, if it's alright, ah'd like to just relax, have some alone time. . ."
    ch_Player "Sure thing."
    ch_Player "Maybe I'll see you later? If you're up to it?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Sure, later."
    
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_212

    $ Rogue.wants_alone_time = 1

    $ ongoing_Event = False

    return