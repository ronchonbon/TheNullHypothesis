label Jean_chatting(line):
    if "girlfriend" in line:
        $ EventScheduler.Events["Jean_boyfriend_trigger_part_two"].start()

    if "decorated" in line:
        $ EventScheduler.Events["Jean_gifts"].start()

    return

label Jean_busy:
    if Jean.behavior == "in_class":
        $ Jean.change_face(eyes = "down") 

        pause 1.0

        $ Jean.change_face("surprised2") 

        ch_Jean  "Oh! It's you."

        $ Jean.change_face("smirk2") 

        ch_Jean "Sorry, busy with class work right now." 
    elif Jean.behavior == "training":
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Jean.change_face("worried1")  

            ch_Jean "I'm okay. . ."

            $ Jean.change_face("angry1") 

            ch_Jean "Ugh, it's so frustrating not being able to train with my powers properly."
            ch_Jean "I need to finish up this session already."
        elif dice_roll == 2:
            $ Jean.change_face("pleased2") 

            ch_Jean "Oh! Great, you're here." 

            $ Jean.change_face("smirk2") 

            ch_Jean "I was about to start training." 
            ch_Jean "You should join me."

            menu:
                extend ""
                "Count me in.":
                    $ Jean.change_face("happy")

                    call actually_train(Jean) from _call_actually_train_2
                "Not right now.":
                    $ Jean.change_face("confused1")

                    $ Jean.History.update("Player_rejected_training")
    elif Jean.behavior == "studying":
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Jean.change_face("smirk1")  

            ch_Jean "I'm pretty good." 
            ch_Jean "Just about to study some stuff."
        elif dice_roll == 2:
            $ Jean.change_face("worried1")  

            ch_Jean "Worried I didn't study enough for this next quiz." 

            $ Jean.change_face("surprised1") 

            ch_Jean "Oh!" 

            $ Jean.change_face("smirk2") 

            ch_Jean "Let's just study together, I'm feeling generous."

            menu:
                extend ""
                "Sure, thanks.":
                    $ Jean.change_face("happy")

                    call actually_study(Jean) from _call_actually_study_5
                "I don't really want to study right now.":
                    $ Jean.change_face("confused1") 
                    
                    ch_Jean "Ugh, fine."

                    $ Jean.History.update("Player_rejected_studying")
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("happy")

            ch_Jean "I'm great!" 

            $ Jean.change_face("smirk2")

            ch_Jean "Aced another exam, as usual."
        elif dice_roll == 2:
            $ Jean.change_face("smirk1") 

            ch_Jean "I'm okay." 

            $ Jean.change_face("smirk2")

            ch_Jean  "Thanks for caring."
        elif dice_roll == 3:
            $ Jean.change_face("worried1")

            ch_Jean "Hope I studied enough. . ."
        elif dice_roll == 4:
            $ Jean.change_face("smirk2") 

            ch_Jean "Pretty great." 
            ch_Jean "What about you?"

            menu:
                extend ""
                "I'm also great now that you're here.":
                    $ Jean.change_face("pleased2", blush = 1)  

                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_217 
                "Could be worse.":
                    $ Jean.change_face("confused1")
                "That's it? Whatever, never mind. . .":
                    $ Jean.change_face("worried1") 

                    $ Jean.change_face("confused1") 

                    ch_Jean "Okay. . ."

                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_218

    return

label Jean_busy_love:
    $ Jean.change_face("smirk2") 

    pause 1.0

    $ Jean.change_face("kiss2") 

    "She pulls you into a brief kiss." 

    $ Jean.History.update("kiss")

    $ Jean.change_face("smirk2") 

    ch_Jean "Much better now." 

    $ Jean.change_face("worried1") 

    ch_Jean "Just wish I had time to hang with you."

    return

label Jean_busy_relationship:
    $ Jean.change_face("worried1")  

    ch_Jean "Busy." 
    ch_Jean "So much stuff to do." 

    $ Jean.change_face("smirk1") 

    ch_Jean "Thanks for asking, though." 
    ch_Jean "Wish we could hang out."

    return

label Jean_busy_asked_once:
    $ Jean.change_face("confused1") 

    ch_Jean "Uhm, hello. . . you just asked me?"

    return

label Jean_busy_asked_twice:
    $ Jean.change_face("angry1")  

    ch_Jean "The hell?"

    $ Jean.change_face("appalled1") 

    ch_Jean "Are you ignoring me?!"

    if Player.location == Jean.location:
        if Player.location == Jean.home:
            ch_Jean "Get out."
        else:
            ch_Jean "I'm out of here."
            
        call getting_kicked_out(Jean) from _call_getting_kicked_out_7

    return

label Jean_busy_late:
    $ Jean.change_face("smirk2") 

    ch_Jean "I'm good."
    ch_Jean "Just about to go to bed." 

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "I'll see you tomorrow, right?" 

    return

label Jean_busy_late_asked_once:
    $ Jean.change_face("confused1")  

    ch_Jean "Uhm. . . Weren't you listening?" 
    ch_Jean "I'm about to go to bed."

    return

label Jean_busy_late_asked_twice:
    $ Jean.change_face("appalled1") 

    if Player.location == Jean.location:
        if Player.location == Jean.home:
            ch_Jean "Stop ignoring me and get out."
        else:
            ch_Jean "Are you ignoring me?"
            ch_Jean "I'm out of here."

        call getting_kicked_out(Jean) from _call_getting_kicked_out_8
    else:
        ch_Jean "Stop ignoring me!"

    return

label Jean_busy_mad:
    $ Jean.change_face("angry1")  

    ch_Jean "I am NOT okay." 

    $ Jean.change_face("angry1", eyes = "left")

    ch_Jean "I'm busy, don't talk to me."

    return

label Jean_busy_heartbroken:
    $ Jean.change_face("worried1") 

    ch_Jean "I'm. . ." 

    $ Jean.change_face("worried1", eyes = "down")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "left")

    ch_Jean "Okay." 

    $ Jean.change_face("worried1")

    ch_Jean "Why did. . . never mind." 
    ch_Jean "I'm busy right now."

    $ Jean.change_face("neutral", eyes = "left")

    return

label Jean_busy_horny:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 1)

    ch_Jean "I'm. . ."

    $ Jean.change_face("sexy") 

    ch_Jean "Great. . ."

    $ Jean.change_face("sexy", eyes = "down")

    pause 1.0

    $ Jean.change_face("sexy")

    ch_Jean "Wish I wasn't busy so we could hang out."

    return

label Jean_busy_nympho:
    $ Jean.change_face("manic", blush = 1)

    ch_Jean "I'm fine, everything's fine." 
    ch_Jean "If only I wasn't so busy, then I could have. . ."

    $ Jean.change_face("sexy", eyes = "down", blush = 1)

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "{i}Ahem{/i}. . ."

    return

label Jean_talk_later:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Jean.change_face("happy") 

        ch_Jean "Yep! Later." 

        $ Jean.change_face("smirk2")
    elif dice_roll == 2:
        $ Jean.change_face("smirk2") 

        ch_Jean "I hope you do. . ."
    elif dice_roll == 3:
        $ Jean.change_face("smirk2")

        ch_Jean "You better. . ."
        ch_Jean "I'm not going anywhere. . ."

    return

label Jean_talk_later_love:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("sly") 

        ch_Jean "You better." 

        $ Jean.change_face("smirk2")

        ch_Jean "Love you!" 
        ch_Jean "Bye."
    elif dice_roll == 2:
        $ Jean.change_face("smirk2") 

        ch_Jean "Bye, [Jean.Player_petname]!" 
        ch_Jean "Love you."

    return

label Jean_talk_later_relationship:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Jean.change_face("worried1") 

        ch_Jean  "Not gonna stick around?" 

        $ Jean.change_face("smirk1") 

        ch_Jean "Well maybe we can hang later."
    elif dice_roll == 2:
        $ Jean.change_face("smirk2") 

        ch_Jean "You better."

    return

label Jean_talk_later_mad:
    $ Jean.change_face("appalled1")

    ch_Jean "What? Now you're leaving." 

    $ Jean.change_face("appalled1", eyes = "left") 

    ch_Jean "Whatever, bye."

    return

label Jean_talk_later_heartbroken:
    $ Jean.change_face("worried1") 

    ch_Jean "You're. . . leaving?" 

    $ Jean.change_face("worried1", eyes = "left") 

    ch_Jean "I. . ." 

    $ Jean.change_face("worried1", eyes = "down") 

    ch_Jean "Bye."

    return

label Jean_talk_later_horny:
    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Don't mind me as I watch you leave. . ." 

    $ Jean.change_face("sly", eyes = "down", blush = 1) 

    pause 1.0

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    return

label Jean_talk_later_nympho:
    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "You better do more than just {i}talk{/i} to me later. . ." 

    $ Jean.change_face("sexy", eyes = "down", blush = 1)

    $ Jean.change_face("sexy", blush = 2)

    return

label Jean_ask_about_Rogue:
    if approval_check(Rogue, threshold = "love"):
        if Jean in Partners:
            $ Jean.change_face("smirk2") 

            ch_Jean "She's the sweetest thing." 

            $ Jean.change_face("smirk2", eyes = "squint") 

            ch_Jean "She'd probably do just about anything for you." 
            ch_Jean "I bet you like that."

            menu:
                extend ""
                "I like telling her what to do. . . and you telling {i}me{/i} what to do. . .":
                    $ Jean.change_face("sexy") 
                    
                    ch_Jean "Good." 
                    
                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_219
                "I like telling her what to do. . . but I'm not a huge fan of you doing it to me. . .":
                    $ Jean.change_face("worried1") 
                    
                    ch_Jean "Really?"
                "Not really. I know you enjoy telling me what to do, but I'm not like that.":
                    $ Jean.change_face("smirk2", mouth = "lipbite") 
                    
                    ch_Jean "I do enjoy it. . ."
                "I'm not a weirdo like you. . .":
                    $ Jean.change_face("angry1") 
                    
                    ch_Jean "The hell?" 
                    
                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_220
        else:
            $ Jean.change_face("confused1") 

            ch_Jean "Well, she's nice. . ." 

            $ Jean.change_face("confused1", eyes = "squint") 

            ch_Jean "Maybe {i}too{/i} nice, to you in particular." 

            $ Jean.change_face("worried1") 

            ch_Jean "There's also something about her. . ." 
            ch_Jean "I dunno, maybe you should just steer clear. . ."
    elif Jean in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Jean.change_face("confused1") 

            ch_Jean "Why do you wanna know about her?" 

            $ Jean.change_face("confused1", eyes = "squint")

            ch_Jean "I know she's like, obsessed with you or something." 

            $ Jean.change_face("suspicious1") 

            ch_Jean "Maybe you should stay away from her. . ."
        elif dice_roll == 2:
            $ Jean.change_face("confused1")  

            ch_Jean "Rogue?" 

            $ Jean.change_face("smirk2") 

            ch_Jean "She's sweet on the outside. . ." 
            ch_Jean "At least when you're around. . ."

            $ Jean.change_face("worried1")  

            ch_Jean "But I always feel kinda uneasy whenever I get a sense of her emotions." 

            $ Jean.change_face("worried1", eyes = "left")

            ch_Jean "She used to be. . . never mind."
    elif approval_check(Jean, threshold = "friendship"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Jean.change_face("worried1") 

            ch_Jean "I dunno, I mean she's nice." 
            ch_Jean "There's just something about her. . ."
            ch_Jean "Like she always knows more than she lets on." 
        elif dice_roll == 2:
            $ Jean.change_face("confused1") 

            ch_Jean "That one?" 
            ch_Jean "Isn't she your tutor?" 

            $ Jean.change_face("confused1", eyes = "squint") 

            ch_Jean "Are you two a thing?" 

            $ Jean.change_face("worried1")  

            ch_Jean "Everyone knows she. . ." 

            $ Jean.change_face("worried1", eyes = "left")

            pause 1.0

            $ Jean.change_face("worried1") 

            ch_Jean "Has a huge crush on you."
    else:
        $ dice_roll = renpy.random.randint(1, 2)
        
        if dice_roll == 1:
            $ Jean.change_face("confused1", mouth = "smirk") 

            ch_Jean "What do I think?" 

            $ Jean.change_face("smirk2") 

            ch_Jean "Well she's sweet, but. . ."

            $ Jean.change_face("worried1")

            ch_Jean "Used to be pretty standoffish if I'm honest."

            $ Jean.change_face("smirk2")

            ch_Jean "She's warmer now. Really smart too!"
            ch_Jean "Not as smart as me, of course."
            ch_Jean "I help her out sometimes." 
        elif dice_roll == 2:
            $ Jean.change_face("confused1") 

            ch_Jean "Do you think it's all a show, or is she actually that much of a Southern belle?" 

            ch_Jean "Wasn't always like that."

            $ Jean.change_face("confused1", mouth = "smirk") 

            ch_Jean "Different now that you're around."

            $ Jean.change_face("confused1", mouth = "smirk", eyes = "squint") 

            ch_Jean "I swear. . . I mean who actually says 'howdy'?"

    return

label Jean_ask_about_Laura:
    if approval_check(Laura, threshold = "love"):
        if Jean in Partners:
            $ Jean.change_face("confused1")

            ch_Jean "She would be fine if she wasn't constantly trying to hijack {i}my{/i} time with you." 

            $ Jean.change_face("angry1")

            ch_Jean "She's so pushy about it." 

            $ Jean.change_face("confused1")

            ch_Jean "Doesn't she get I'm your main girlfriend?" 
            ch_Jean "And, what, you like her bossing you around?"

            menu:
                extend ""
                "I mean. . . I like when you boss me around. . . I like when she does it too.":
                    $ Jean.change_face("pleased2") 

                    $ Jean.change_face("neutral", mouth = "lipbite", blush = 1) 

                    ch_Jean "I'm glad you like it. . ." 

                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_221
                "I like when {i}you{/i} boss me around. . . but I'm trying to help her be. . . more normal.":
                    $ Jean.change_face("worried1") 

                    ch_Jean "Yeah. . . maybe I should cut her some slack."
                "I don't like {i}either{/i} of you trying to boss me around.":
                    $ Jean.change_face("angry1") 

                    ch_Jean "Whatever." 

                    $ Jean.change_face("angry1", eyes = "left") 

                    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_222
        else:
            $ Jean.change_face("confused1") 

            ch_Jean "About [Laura.public_name]?" 

            $ Jean.change_face("confused1", eyes = "left") 

            ch_Jean ". . ." 

            $ Jean.change_face("confused1") 

            ch_Jean "Well, I know you two are. . ." 

            $ Jean.change_face("worried1") 

            ch_Jean "Do you really. . ."
            ch_Jean "I mean, isn't she mean?"
    elif Laura in Partners:
        if Jean in Partners:
            $ Jean.change_face("angry1")  

            ch_Jean "She's. . . frustrating. . ." 

            $ Jean.change_face("worried1") 

            ch_Jean "But I know she's trying." 

            $ Jean.change_face("sly") 

            ch_Jean "And basically obsessed with you. . ."
        else:
            $ Jean.change_face("worried1")

            ch_Jean "You're. . . {i}with{/i} her, right?" 

            $ Jean.change_face("worried1", eyes = "left") 

            ch_Jean "She's kinda mean. . ." 

            $ Jean.change_face("worried1") 

            ch_Jean "Why do you. . ." 

            $ Jean.change_face("angry1") 

            ch_Jean "Whatever, never mind."
    elif EventScheduler.Events["Laura_first_friend_part_three"].completed:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Jean.change_face("confused1") 

            ch_Jean "What do I think?"

            $ Jean.change_face("smirk2") 

            ch_Jean "Heh, aren't you her only friend or something?" 
            ch_Jean "You tell me."
        elif dice_roll == 2:
            $ Jean.change_face("confused1") 

            ch_Jean "Aren't you friends with her?" 
            ch_Jean "She's been hanging around you a lot lately." 

            $ Jean.change_face("confused1", eyes = "squint")

            pause 1.0

            ch_Jean "You know she follows you around, right?"
        elif dice_roll == 3:
            $ Jean.change_face("confused1") 

            ch_Jean "Aren't you friends with her?"
            ch_Jean "She actually came to me for help with some assignment the other day." 

            $ Jean.change_face("neutral") 

            ch_Jean "She's kinda. . . blunt. . ." 

            $ Jean.change_face("worried1")
    else:
        $ dice_roll = renpy.random.randint(1, 3)
        
        if dice_roll == 1:
            $ Jean.change_face("confused1") 

            ch_Jean "[Laura.public_name]?" 
            ch_Jean "She's. . ." 

            $ Jean.change_face("worried1")

            ch_Jean "Kinda scary, to be honest." 

            $ Jean.change_face("worried1", eyes = "left") 

            pause 1.0

            $ Jean.change_face("worried1") 

            ch_Jean "I heard she's killed people before. . ."
        elif dice_roll == 2:
            $ Jean.change_face("confused1") 

            ch_Jean "Does anyone even know anything about her?" 

            $ Jean.change_face("worried1")

            ch_Jean "I don't really know anything about her. . ." 
            ch_Jean "Other than how good she is at fighting."
        elif dice_roll == 3:
            $ Jean.change_face("confused1")  

            ch_Jean "That one?" 
            ch_Jean "Does she even have any friends?" 

            $ Jean.change_face("worried1") 

            ch_Jean "Can't help but feel a bit bad for her."

    return

label Jean_ask_on_date:
    ch_Player "Hey, [Jean.name], wanna go on a date tonight?"
    
    if Jean.status["mad"] or Jean.status["heartbroken"]:
        $ Jean.change_face("worried1") 
        
        pause 1.0 
        
        $ Jean.change_face("angry1", eyes = "right") 
        
        ch_Jean "Can't." 
        
        $ Jean.change_face("neutral") 
        
        ch_Jean "I. . . have to study." 
        
        $ Jean.change_face("worried1", eyes = "right")
        
        $ Jean.History.update("said_no_to_date")
    elif Jean.status["horny"] or Jean.status["nympho"]:
        $ Jean.change_face("confused1", mouth = "lipbite") 
        
        ch_Jean "I had other plans for you tonight. . ." 
        
        $ Jean.change_face("sexy", blush = 1) 
        
        ch_Jean "But, you know I love going on dates with you." 
        ch_Jean "We just need to get back early so there's enough time for. . ." 
        
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
        
        ch_Jean "You know. . ."

        $ Player.date_planned[Jean] = "Player_initiated_primary"
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Jean.change_face("happy") 
            
            ch_Jean "Of course I do." 
            
            $ Jean.change_face("smirk2") 
            
            ch_Jean "I'll see you tonight." 

            $ Player.date_planned[Jean] = "Player_initiated_primary"
        elif dice_roll == 2:
            $ Jean.change_face("confused1", mouth = "smirk", eyes = "squint") 
            
            ch_Jean "I was just about to ask you the same thing." 
            
            $ Jean.change_face("smirk2", eyes = "squint") 
            
            ch_Jean "I'll see you tonight, [Jean.Player_petname]."

            $ Player.date_planned[Jean] = "Player_initiated_primary"
        elif dice_roll == 3:
            $ Jean.schedule[2] = [Jean.home, "studying"]
            
            $ Jean.change_face("worried1") 
            
            ch_Jean "I'm sorry, [Jean.Player_petname], I can't." 
            
            ch_Jean "I really have to study tonight." 
            
            $ Jean.change_face("worried1", eyes = "right") 
            
            ch_Jean "You're gonna ask me again tomorrow, right?"

            $ Jean.History.update("said_no_to_date")
        elif dice_roll == 4:
            $ Jean.schedule[2] = [Jean.home, "studying"]

            $ Jean.change_face("confused1", mouth = "smirk") 
            
            ch_Jean "We can't go out tonight." 
            
            $ Jean.change_face("confused1", mouth = "smirk", eyes = "squint") 
            
            ch_Jean "We're gonna study together." 
            ch_Player "We are?" 

            if Jean.location == Player.location:
                "She just stares at you." 

            menu:
                extend ""
                "I mean, of course we are. . .":
                    $ Player.schedule[2] = [
                        ["Player.location != Jean.home", "renpy.say(None, 'You head to your study session with [Jean.name].')"],
                        ["Jean.location != Jean.home", "renpy.call('send_Characters', Jean, Jean.home, behavior = 'studying')"],
                        ["Player.location != Jean.home", "renpy.call('set_the_scene', location = Jean.home)"],
                        ["True", "renpy.call('actually_study', Jean)"]]
                "I. . . can't tonight.":
                    $ Jean.change_face("suspicious1") 

                    $ Jean.History.update("Player_rejected_studying")
            
            $ Jean.History.update("said_no_to_date")

    return

label Jean_answering_phone:
    ch_Jean "Hey [Jean.Player_petname]!"

    return