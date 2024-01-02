label Rogue_chatting(line):
    if "girlfriend" in line:
        $ EventScheduler.Events["Rogue_boyfriend_trigger_part_two"].start()

    if "decorated" in line:
        $ EventScheduler.Events["Rogue_gifts"].start()

    return

label Rogue_busy:
    if Rogue.behavior == "in_class":
        $ Rogue.change_face("worried1")

        ch_Rogue "Ah shoulda studied more. . ." 
        ch_Rogue "Wish ah could chat with ya."
    elif Rogue.behavior == "training":
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah'm. . . okay."

            $ Rogue.change_face("neutral")

            ch_Rogue "Gotta finish this trainin' session."
        elif dice_roll == 2:
            $ Rogue.change_face("worried2")

            ch_Rogue "Sorry, ah can't really chat. . ."

            $ Rogue.change_face("worried1")

            ch_Rogue "In the middle of trainin'."
            ch_Rogue "Unless. . . want to join?"

            menu:
                extend ""
                "Sure.":
                    $ Rogue.change_face("smirk2")

                    call actually_train(Rogue) from _call_actually_train_8
                "Nah, I'm good.":
                    $ Rogue.History.update("Player_rejected_training")
    elif Rogue.location == Rogue.home:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("pleased1")

            ch_Rogue "Good, thanks for askin' sugar."

            $ Rogue.change_face("worried1")

            ch_Rogue "Ah'm just a bit busy."
        elif dice_roll == 2:
            $ Rogue.change_face("worried2")

            ch_Rogue "Ah'm a bit worried about the upcoming quiz. . ."

            $ Rogue.change_face("worried1", blush = 1)

            ch_Rogue "Did ya maybe. . ."
            ch_Rogue "Wanna study with me?"

            menu:
                extend ""
                "Sure.":
                    $ Rogue.change_face("smirk2")

                    call actually_study(Rogue) from _call_actually_study_11
                "Nah, I'm good.":
                    $ Rogue.History.update("Player_rejected_studying")
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            ch_Rogue "Ah'm alright, thanks for askin'." 

            $ Rogue.change_face("smirk2")
        elif dice_roll == 2:
            ch_Rogue "Ah could be worse." 

            $ Rogue.change_face("smirk2")
        elif dice_roll == 3:
            ch_Rogue "Better now that yer here." 

            $ Rogue.change_face("smirk2", blush = 1)
        elif dice_roll == 4:
            ch_Rogue "Ah'm good."
            ch_Rogue "How 'bout you?" 

            $ Rogue.change_face("smirk2")

            menu:
                extend ""
                "Great, now that I'm with you.":
                    $ Rogue.change_face("pleased1", blush = 1) 
                    
                    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_686
                "I'm okay.":
                    $ Rogue.change_face("neutral")
                "Really? Never mind. . .":
                    $ Rogue.change_face("worried1") 
                    
                    ch_Rogue "Sorry. . ." 
                    
                    call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_687

    return

label Rogue_busy_love:
    ch_Rogue "Ah'm doin' a whole lot better now that yer here, [Rogue.Player_petname]." 

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "If only ah had more time for ya."

    return

label Rogue_busy_relationship:
    ch_Rogue "Not too bad, ah'm real glad yer here."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Wish ah wasn't so busy."

    return

label Rogue_busy_asked_once:
    $ Rogue.change_face("confused1")

    ch_Rogue "You alright?"
    ch_Rogue "Just asked me that. . ."

    return

label Rogue_busy_asked_twice:
    $ Rogue.change_face("angry1")

    ch_Rogue "Ah told ya ah'm busy."

    if Player.location == Rogue.location:
        if Player.location == Rogue.home:
            ch_Rogue "Get out."
        else:
            ch_Rogue "Ah'm out of here."
            
        call getting_kicked_out(Rogue) from _call_getting_kicked_out_51

    return

label Rogue_busy_late:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm okay, but can't really chat. . ."
    ch_Rogue "Was 'bout to go to bed, sorry hon'."

    return

label Rogue_busy_late_asked_once:
    $ Rogue.change_face("confused1")

    ch_Rogue "Ah said ah'm 'bout to go to bed. . ."

    return

label Rogue_busy_late_asked_twice:
    $ Rogue.change_face("angry1")
    
    if Player.location == Rogue.location:
        if Player.location == Rogue.home:
            ch_Rogue "Ah think you should leave."
        else:
            ch_Rogue "Ah'm out of here."
            
        call getting_kicked_out(Rogue) from _call_getting_kicked_out_52

    return

label Rogue_busy_mad:
    $ Rogue.change_face("angry1")

    ch_Rogue "Ya really can't tell?" 

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Rogue "Ah'm busy anyway. . . can't talk." 

    return

label Rogue_busy_heartbroken:
    $ Rogue.change_face("worried1")

    ch_Rogue "Ah'm. . ." 

    $ Rogue.change_face("worried1", eyes = "down") 

    ch_Rogue "Busy, don't really wanna chat. . ." 

    $ Rogue.change_face("worried1", eyes = "right")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "down") 

    return

label Rogue_busy_horny:
    $ Rogue.change_face(mouth = "lipbite", blush = 1)

    ch_Rogue "Ah could be better. . ." 

    $ Rogue.change_face(mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face(mouth = "lipbite", eyes = "neutral", blush = 2)

    ch_Rogue "If only ah wasn't so busy."

    return

label Rogue_busy_nympho:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "Ah'm. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 2) 

    pause 1.0

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 3) 

    ch_Rogue "Ah {i}need{/i} you. . ." 
    ch_Rogue "But ah'm too busy right now." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 3) 

    return

label Rogue_talk_later:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Rogue "Sure hon', later." 

        $ Rogue.change_face("smirk2")
    elif dice_roll == 2:
        ch_Rogue "{size=-5}Please do{/size}. . ."
    elif dice_roll == 3:
        ch_Rogue "Ah'll be here." 

        $ Rogue.change_face("smirk2")

    return

label Rogue_talk_later_love:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("worried1")  

        ch_Rogue "Ah hope you mean it." 
        ch_Rogue "Love you."
    elif dice_roll == 2:
        $ Rogue.change_face("smirk2") 

        ch_Rogue "Bye, [Rogue.Player_petname]." 
        ch_Rogue "Ah love you."

    return

label Rogue_talk_later_relationship:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("smirk2")

        ch_Rogue "Ah'll be here for ya."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1")  

        ch_Rogue "Ah hope we can hang later. . ."

    return

label Rogue_talk_later_mad:
    $ Rogue.change_face("angry1") 

    ch_Rogue "Fine, ah guess ah'll be seein' you." 

    return

label Rogue_talk_later_heartbroken:
    $ Rogue.change_face("worried2") 

    ch_Rogue "But. . . ah. . ." 

    $ Rogue.change_face("worried1", eyes = "down") 

    ch_Rogue "Bye. . ."

    return

label Rogue_talk_later_horny:
    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Alright. . . ah hope ah do see you later."

    return

label Rogue_talk_later_nympho:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

    ch_Rogue "Please don't make me wait too long. . ." 
    ch_Rogue "Ah {i}need{/i} you." 

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

    return

label Rogue_ask_about_Laura:
    if approval_check(Laura, threshold = "love"):
        if Rogue in Partners and Laura in Partners:
            $ Rogue.change_face("worried1")  

            ch_Rogue "Well ah love ya both. . ." 
            ch_Rogue "But do ya really like her tellin' ya what to do so much?"
            
            menu:
                extend ""
                "Yeah. . . I kinda do.":
                    $ Rogue.change_face("worried1", blush = 1) 

                    ch_Rogue "Oh. . . ah. . . know what ya mean. . ." 

                    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)
                "I mean, she knows what she's doing. It would be pretty stupid not to listen to her during training.":
                    $ Rogue.change_face("confused1") 

                    $ Rogue.change_face("worried1") 

                    ch_Rogue "That's. . . not really what ah meant. . ."
                "She doesn't when we're in private.": 
                    $ Rogue.change_face("worried2", blush = 1) 

                    ch_Rogue "Oh. . ."
        else:
            $ Rogue.change_face("smirk2")

            ch_Rogue "About [Laura.public_name]?" 
            ch_Rogue "Ah know you two are gettin' super close." 

            $ Rogue.change_face("worried1")    

            ch_Rogue "Isn't she a bit demandin' sometimes?"
    elif Laura in Partners:
        if Rogue in Partners:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Ah like her, and ah'd say she cares about both of us more than she lets on." 

            $ Rogue.change_face("sly") 

            ch_Rogue "She's constantly talkin' to me 'bout ya."
        else:
            $ Rogue.change_face("worried1")  

            ch_Rogue "Ah'm quite fond of her." 
            ch_Rogue "You two. . . make a nice couple." 
            ch_Rogue "Bein' with you is good for her."
    elif EventScheduler.Events["Laura_first_friend_part_three"].completed:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Rogue.change_face("confused1", mouth = "smirk") 

            ch_Rogue "Well it's yer fault ah'm friends with her now." 

            $ Rogue.change_face("smirk2") 

            ch_Rogue "Not like ah mind, deep down she's real sweet." 

            $ Rogue.change_face("worried1") 

            ch_Rogue "Just don't tell her ah said that. . ."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1")  

            ch_Rogue "Ah just feel bad for her." 
            ch_Rogue "But, she doesn't take kindly to pity. . ."
        elif dice_roll == 3:
            $ Rogue.change_face("smirk2")

            ch_Rogue "Well ah quite like her." 

            $ Rogue.change_face("sly") 

            ch_Rogue "And ah think she quite likes {i}you{/i}."
            ch_Rogue "Constantly askin' me. . . things."
    else:
        $ dice_roll = renpy.random.randint(1, 3)
        
        if dice_roll == 1:
            $ Rogue.change_face("confused1")  

            ch_Rogue "Well ah don't know too much 'bout her." 

            $ Rogue.change_face("worried1") 

            ch_Rogue "She doesn't let anyone get close."
        elif dice_roll == 2:
            $ Rogue.change_face("worried1") 

            ch_Rogue "Ah don't think the poor thing even has any friends."
        elif dice_roll == 3:
            $ Rogue.change_face("confused1")  

            ch_Rogue "About [Laura.public_name]?" 

            $ Rogue.change_face("worried1") 

            ch_Rogue "Ah heard quite a few people were none too happy 'bout her startin' school here. . ." 

            $ Rogue.change_face("worried1", eyes = "right")

            pause 1.0

            $ Rogue.change_face("worried1", eyes = "down") 

            pause 1.0

            $ Rogue.change_face("worried1", eyes = "neutral")

            pause 1.0  

            ch_Rogue "Don't ask how ah know, but. . ." 
            ch_Rogue "{size=-5}Apparently she almost killed one of the X-Men{/size}."

    return

label Rogue_ask_about_Jean:
    if approval_check(Jean, threshold = "love"):
        if Rogue in Partners and Jean in Partners:
            $ Rogue.change_face("worried2")

            ch_Rogue "Yer askin' what ah think?" 

            $ Rogue.change_face("worried1") 

            ch_Rogue "Ah think you shouldn't let her boss you 'round so much. . ."
            
            menu:
                extend ""
                "I wouldn't call it 'boss around', but. . . I like it.":
                    $ Rogue.change_face("surprised2", blush = 1) 

                    ch_Rogue "Ah. . ." 

                    $ Rogue.change_face("worried1", blush = 2) 

                    ch_Rogue "Know what ya mean. . ."
                "She doesn't 'boss me around'. . .":
                    $ Rogue.change_face("worried1") 

                    ch_Rogue "Sorry. . ."
                "If I wanted your advice, I'd ask for it.":
                    if Rogue.check_traits("quirk"):
                        $ Rogue.change_face("worried2", blush = 1) 

                        ch_Rogue "Ah'm sorry, [Rogue.Player_petname]." 

                        $ Rogue.change_face("worried1")
                    else:
                        $ Rogue.change_face("confused1") 

                        ch_Rogue "Ah'm just lookin' out for ya. . ." 

                        call change_Character_stat(Rogue, "love", 0) from _call_change_Character_stat_688
        else:
            $ Rogue.change_face("confused2")  

            ch_Rogue "What ah think 'bout her?" 

            $ Rogue.change_face("worried1")

            ch_Rogue "Well. . . ah know you two are. . ." 
            ch_Rogue "Ah don't really think ah should say nothin'. . ." 

            $ Rogue.change_face("worried1", eyes = "down")
    elif Jean in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1")  

            ch_Rogue "Ya want to know what ah think?" 

            $ Rogue.change_face("worried1") 

            ch_Rogue "She's nice. . ." 
            ch_Rogue "A bit much sometimes. . ." 
        elif dice_roll == 2:
            ch_Rogue "Ah heard she dated Scott a while back." 
            ch_Rogue "And it didn't end too well. . ." 

            $ Rogue.change_face("worried1") 

            ch_Rogue "Maybe you should. . ." 

            $ Rogue.change_face("worried1", eyes = "right") 

            ch_Rogue "Never mind."
    elif approval_check(Jean, threshold = "friendship"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1") 

            ch_Rogue "Well aren't ya friends with her?" 

            $ Rogue.change_face("smirk1")  

            ch_Rogue "Ah'm not too close with her." 

            $ Rogue.change_face("worried1") 

            ch_Rogue "Not that ah don't like her or nothin'." 
        elif dice_roll == 2:
            $ Rogue.change_face("confused1") 

            ch_Rogue "Ah'm not really that close with her. . ." 
            ch_Rogue "But you're friends, right?" 

            $ Rogue.change_face("worried1")

            ch_Rogue "Haven't her powers been actin' up?"
    else:
        $ dice_roll = renpy.random.randint(1, 2)
        
        if dice_roll == 1:
            $ Rogue.change_face("confused1")

            ch_Rogue "Jean?" 

            $ Rogue.change_face("smirk1") 

            ch_Rogue "Ah go to her for help studyin' sometimes." 
            ch_Rogue "She's super smart, but. . ." 

            $ Rogue.change_face("worried1") 

            ch_Rogue "Well, we're not that close." 

            $ Rogue.change_face("worried1", eyes = "right")
        elif dice_roll == 2:
            $ Rogue.change_face("confused1") 

            ch_Rogue "What do ah think about her?" 
            ch_Rogue "She's nice." 

            $ Rogue.change_face("smirk1") 
            
    return

label Rogue_ask_on_date:
    ch_Player "Hey, [Rogue.name], wanna go on a date tonight?"
    
    if Rogue.status["mad"] or Rogue.status["heartbroken"]:
        $ Rogue.change_face("confused2") 
        
        pause 1.0 
        
        $ Rogue.change_face("worried1", eyes = "right") 
        
        ch_Rogue "Ah. . . can't." 
        
        $ Rogue.change_face("worried1") 
        
        ch_Rogue "Maybe some other day." 
        
        $ Rogue.change_face("worried1", eyes = "right")
        
        $ Rogue.History.update("said_no_to_date")
    elif Rogue.status["horny"] or Rogue.status["nympho"]:
        $ Rogue.change_face("worried2", mouth = "lipbite") 
        
        ch_Rogue "Yes please. . ." 
        
        $ Rogue.change_face("sexy", blush = 1)
        
        ch_Rogue "Ain't nothin' better than a date with you." 
        
        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1) 
        
        ch_Rogue "Ah just hope you have some {i}special plans{/i} for me tonight." 
        
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        $ Player.date_planned[Rogue] = "Player_initiated_primary"
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Rogue.change_face("happy") 
            
            ch_Rogue "You know ah do." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Ah'm lookin' forward to it."

            $ Player.date_planned[Rogue] = "Player_initiated_primary"
        elif dice_roll == 2:
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Ah was hopin' you'd ask." 
            
            $ Rogue.change_face("smirk2") 
            
            ch_Rogue "See ya tonight."

            $ Player.date_planned[Rogue] = "Player_initiated_primary"
        elif dice_roll == 3:
            $ Rogue.schedule[2] = [Rogue.home, "studying"]
            
            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Ah'm sorry, [Rogue.Player_petname], ah really want to." 
            ch_Rogue "Tonight just ain't good for me." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Please ask me again tomorrow."

            $ Rogue.History.update("said_no_to_date")
        elif dice_roll == 4:
            $ Rogue.schedule[2] = [Rogue.home, "studying"]

            $ Rogue.change_face("worried1") 
            
            ch_Rogue "Ah sure want to." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "But we got a test comin' up."
            ch_Rogue "Maybe we could study together instead?" 
            ch_Player "We do?" 
            
            $ Rogue.change_face("confused1", mouth = "smirk") 

            if Rogue.location == Player.location:
                "She just stares at you." 

            menu:
                extend ""
                "Sure, we can study tonight.":
                    $ Player.schedule[2] = [
                        ["Player.location != Rogue.home", "renpy.say(None, 'You rush over to study for that test with [Rogue.name].')"],
                        ["Rogue.location != Rogue.home", "renpy.call('send_Characters', Rogue, Rogue.home, behavior = 'studying')"],
                        ["Player.location != Rogue.home", "renpy.call('set_the_scene', location = Rogue.home)"],
                        ["True", "renpy.call('actually_study', Rogue)"]]
                "Sorry, I. . . can't tonight.":
                    $ Rogue.change_face("worried1") 

                    $ Rogue.History.update("Player_rejected_studying")
            
            $ Rogue.History.update("said_no_to_date")

    return

label Rogue_answering_phone:
    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "Hello? [temp]?"

    return