label Laura_chatting(line):
    if "girlfriend" in line:
        $ EventScheduler.Events["Laura_boyfriend_trigger_part_two"].start()
    
    return

label Laura_busy:
    if Laura.in_class:
        $ Laura.change_face("angry1") 

        ch_Laura "Bored out of my mind." 
        ch_Laura "I'm busy trying not to pay attention, just find me in the Danger Room later if you have something to say." 

        $ Laura.change_face("angry1", eyes = "right")
    elif Laura.training:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Laura.change_face("angry1") 

            ch_Laura "I'm in the middle of training." 
            ch_Laura "I'll be done in. . ." 

            $ Laura.change_face("angry1", eyes = "down") 

            ch_Laura "Five hours." 

            $ Laura.change_face("neutral")
        elif dice_roll == 2:
            $ Laura.change_face("confused1") 

            ch_Laura "How am I?" 
            ch_Laura "I'm about to start training, and you're going to join me." 

            $ Laura.change_face("confused1", eyes = "down") 

            $ Laura.change_face("confused1") 

            ch_Laura "You look like you need it."

            menu:
                extend ""
                "Yeah. . . I kinda do.":
                    $ Laura.change_face("smirk2")

                    call actually_train(Laura) from _call_actually_train_5
                "I probably do, but not right now.":
                    $ Laura.change_face("confused1", eyes = "squint")

                    $ Laura.History.update("Player_rejected_studying")
    elif Laura.studying:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Laura.change_face("confused1") 

            ch_Laura "I'm fine." 

            $ Laura.change_face("neutral") 

            ch_Laura "Busy."
        elif dice_roll == 2:
            $ Laura.change_face("angry1")

            ch_Laura "I'm not fine." 
            ch_Laura "Have to waste my time studying so I don't fail." 

            $ Laura.change_face("confused1", eyes = "squint") 

            ch_Laura "Actually. . ." 
            ch_Laura "You're just going to teach it to me."

            menu:
                extend ""
                "Want me to tutor you? Sure.":
                    $ Laura.change_face("smirk2")

                    ch_Laura "Good."

                    call actually_study(Laura) from _call_actually_study_8
                "Sorry, not right now.":
                    $ Laura.change_face("angry1")

                    ch_Laura "{i}Grrrrrr{/i}."

                    $ Laura.History.update("Player_rejected_studying")
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("confused1")

            ch_Laura "What?" 
            ch_Laura "Why?" 

            $ Laura.change_face("confused1", eyes = "down") 

            ch_Laura "Is there blood on my clothes or something?" 

            $ Laura.change_face("confused1") 
        elif dice_roll == 2:
            $ Laura.change_face("confused1")

            ch_Laura "Why wouldn't I be fine?"
        elif dice_roll == 3:
            $ Laura.change_face("angry1")

            ch_Laura "Pissed off that I have to waste so much time in class."
        elif dice_roll == 4:
            ch_Laura "Fine." 

            $ Laura.change_face("confused1")

            ch_Laura "Why do you care?" 

            $ Laura.change_face("confused1", eyes = "squint")

            menu:
                extend ""
                "Is it really so bizarre to you that someone might actually care about your well-being?":
                    $ Laura.change_face("suspicious1", blush = 1) 
                    
                    ch_Laura "Yes, it is." 
                    
                    call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_463
                "Just wondering. . . you didn't look very happy.":
                    $ Laura.change_face("angry1") 
                    
                    ch_Laura "My face always looks like that. . ." 
                    
                    $ Laura.change_face("angry1", eyes = "squint")
                "Whatever, I guess I'll stop caring then.":
                    
                    $ Laura.change_face("furious") 

                    pause 1.0

                    $ Laura.change_face("angry1") 
                    
                    ch_Laura "I never asked you to start." 

                    call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_464

    return

label Laura_busy_love:
    $ Laura.change_face("smirk2") 

    ch_Laura "Good." 

    $ Laura.change_face("kiss2") 

    "She pulls you into a brief kiss." 

    $ Laura.History.update("kiss")

    $ Laura.change_face("smirk2", mouth = "lipbite") 

    ch_Laura "Now I'm great."

    return

label Laura_busy_relationship:
    ch_Laura "Can't talk." 

    $ Laura.change_face("neutral")

    ch_Laura "I'm busy right now. . ." 

    $ Laura.change_face("angry1")

    ch_Laura "Wish I wasn't so we could hang out."

    return

label Laura_busy_asked_once:
    $ Laura.change_face("confused1")

    ch_Laura "What did I just say?"

    return

label Laura_busy_asked_twice:
    $ Laura.change_face("appalled2") 

    ch_Laura "You're pissing me off."

    $ Laura.change_face("angry1")

    if Player.location == Laura.location:
        if Player.location == Laura.home:
            ch_Laura "Go away." 
            "She pushes you out of the room, locking the door behind you."
        else:
            "She storms out of the room."
            
        call getting_kicked_out(Laura) from _call_getting_kicked_out_29

    return

label Laura_busy_late:
    ch_Laura "Not now." 
    ch_Laura "I'm going to bed."

    return

label Laura_busy_late_asked_once:
    $ Laura.change_face("confused1")

    ch_Laura "You deaf?"

    return

label Laura_busy_late_asked_twice:
    $ Laura.change_face("angry1")
    
    if Player.location == Laura.location:
        if Player.location == Laura.home:
            ch_Laura "Get out, now."
        else:
            ch_Laura "Fuck this."
            
        call getting_kicked_out(Laura) from _call_getting_kicked_out_30
    else:
        ch_Laura "Fuck this."
    
    return

label Laura_busy_mad:
    $ Laura.change_face("angry1") 

    ch_Laura "You don't want to be near me right now." 
    ch_Laura "I'm pissed. . . and busy." 

    $ Laura.change_face("angry1", eyes = "right")

    return

label Laura_busy_heartbroken:
    $ Laura.change_face("surprised2") 

    pause 1.0

    $ Laura.change_face("worried1", eyes = "right")

    ch_Laura "Why. . ." 

    $ Laura.change_face("angry1") 

    ch_Laura "Go away. . ." 

    $ Laura.change_face("angry2")

    ch_Laura "I'm busy."

    return

label Laura_busy_horny:
    $ Laura.change_face(mouth = "lipbite", blush = 1)

    ch_Laura "I'm busy. . . for now. . ." 

    $ Laura.change_face(mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    return

label Laura_busy_nympho:
    $ Laura.change_face("sexy", blush = 1) 

    ch_Laura "If I wasn't busy. . ." 

    $ Laura.change_face("sexy", eyes = "down", blush = 1) 

    pause 1.0

    $ Laura.change_face("sexy", blush = 2) 

    ch_Laura "We'd be in my room right now." 

    return

label Laura_talk_later:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Laura "Okay."
    elif dice_roll == 2:
        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "I will hold you to that."
    elif dice_roll == 3:
        $ Laura.change_face("confused1")

        ch_Laura ". . . why?"

    return

label Laura_talk_later_love:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("angry1")

        ch_Laura "If you don't, I will come find you." 

        $ Laura.change_face("neutral")

        pause 1.0

        $ Laura.change_face("worried1") 

        ch_Laura ". . . love you." 

        $ Laura.change_face("angry1", eyes = "right")
    elif dice_roll == 2:
        $ Laura.change_face("smirk2") 

        ch_Laura "Good." 
        ch_Laura "Bye, [Laura.Player_petname]." 
        ch_Laura "I. . . love you."

    return

label Laura_talk_later_relationship:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "You know where to find me." 
        ch_Laura "If not, I'll just find you."
    elif dice_roll == 2:
        $ Laura.change_face("angry1")

        ch_Laura "I want to hang out later."

    return

label Laura_talk_later_mad:
    $ Laura.change_face("appalled2") 

    ch_Laura "Where do you think you're going?" 

    $ Laura.change_face("angry1", eyes = "right") 

    ch_Laura "{i}Grrrrrr{/i}." 
    ch_Laura "Go away." 

    return

label Laura_talk_later_heartbroken:
    $ Laura.change_face("surprised2")

    pause 1.0

    $ Laura.change_face("worried1")

    ch_Laura "Where are you going?" 

    $ Laura.change_face("worried1", eyes = "right") 

    ch_Laura "Why. . ." 

    $ Laura.change_face("angry1")

    ch_Laura "Never mind, go away."

    return

label Laura_talk_later_horny:
    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Laura "You're leaving?" 

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1) 

    pause 1.0

    $ Laura.change_face("sexy", blush = 1) 

    ch_Laura "I may come find you later."

    return

label Laura_talk_later_nympho:
    $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Laura "If you don't do something about. . ." 

    $ Laura.change_face("angry1", mouth = "lipbite", eyes = "down", blush = 1) 

    pause 1.0

    $ Laura.change_face("sexy", blush = 2) 

    ch_Laura "I {i}will{/i} track you down."

    return

label Laura_ask_about_Rogue:
    if approval_check(Rogue, threshold = "love"):
        if Laura in Partners and Rogue in Partners:
            $ Laura.change_face("confused1")

            ch_Laura "I care about her very much."

            $ Laura.change_face("smirk1") 

            ch_Laura "She has been a good 'friend'. . . and more. . . to both of us." 

            $ Laura.change_face("angry1") 

            ch_Laura "But I don't understand why she's so submissive to you."

            menu:
                extend ""
                "Well. . . I like it when you boss me around. . . she likes it when I do it to her.":
                    $ Laura.change_face("confused2", blush = 1) 
                    
                    ch_Laura "I see. . ."
                    
                    $ Laura.change_face("sexy", blush = 1) 
                    
                    call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_465
                "She is, but I don't capitalize on it like you're thinking.":
                    $ Laura.change_face("confused1") 
                    
                    ch_Laura "It's still confusing why that's her nature. . ."
                "I like telling her what to do. . . not so much when you try doing it to me. . .":
                    $ Laura.change_face("confused2") 
                    
                    ch_Laura "Really?"
                    
                    $ Laura.change_face("angry1", eyes = "right") 
                "Yeah, but I'm not a weirdo who likes bossing people around. . .":
                    $ Laura.change_face("appalled2") 
                    
                    ch_Laura "Trying to piss me off?"
                    
                    $ Laura.change_face("angry1") 
                    
                    call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_466
        else:
            $ Laura.change_face("confused1")

            ch_Laura "She talks about you even more now. . ."

            $ Laura.change_face("angry1")

            ch_Laura "Is this what 'love' is?"
            ch_Laura "An obsession?"

            $ Laura.change_face("confused1")

            ch_Laura "She has also seemed. . . different lately."

            $ Laura.change_face("neutral") 

            ch_Laura "More {i}attached{/i} since you arrived."

            $ Laura.change_face("neutral", eyes = "squint")
    elif Rogue in Partners:
        if Laura in Partners:
            $ Laura.change_face("confused1", mouth = "smirk") 

            ch_Laura "I think I. . . care about her. . . a lot."

            $ Laura.change_face("smirk2") 

            ch_Laura "She's helped me figure all this shit out. . . like you."
        else:
            $ Laura.change_face("confused1") 

            ch_Laura "She is your 'girlfriend', no?"

            $ Laura.change_face("neutral") 

            ch_Laura "Her obsession with you was obvious."

            $ Laura.change_face("neutral", eyes = "squint") 

            ch_Laura "She always had a {i}lot{/i} to say about you."

            $ Laura.change_face("suspicious1", eyes = "right") 

            ch_Laura "She seems to know a lot about everyone. . ."
    elif EventScheduler.Events["Laura_first_friend_part_three"].completed:
        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ Laura.change_face("smirk2") 

            ch_Laura "I understand now, why she won't touch anyone."

            $ Laura.change_face("neutral", eyes = "squint") 

            ch_Laura "Except you, apparently."
            ch_Laura "She seems overly excited about that."

            $ Laura.change_face("suspicious1")
        elif dice_roll == 2:
            $ Laura.change_face("confused1") 

            ch_Laura "She's nice, but unfortunately lacking in combat prowess."
            ch_Laura "I might have to make her train with me as well."
        elif dice_roll == 3:
            $ Laura.change_face("smirk2")  

            ch_Laura "I think she is a good. . ."

            $ Laura.change_face("confused1")  

            ch_Laura "'Friend'."
            ch_Laura "She seems to care about me despite my. . ."

            $ Laura.change_face("angry1") 

            ch_Laura "Lack of social skills. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 3)
        
        if dice_roll == 1:
            $ Laura.change_face("confused1") 

            ch_Laura "Her?"

            $ Laura.change_face("confused1", eyes ="squint") 

            ch_Laura "She's suspiciously nice to me."
            ch_Laura "It's impossible she's being genuine."
        elif dice_roll == 2:
            $ Laura.change_face("confused1") 

            ch_Laura "I've followed her around several times."
            ch_Laura "She always avoids touching anyone."

            $ Laura.change_face("confused1", eyes = "squint") 

            ch_Laura "Bizarre."
        elif dice_roll == 3:
            ch_Laura "Her accent is interesting."

            $ Laura.change_face("confused1") 

            ch_Laura "Her vocabulary is also bizarre."
            ch_Laura "'Howdy', 'Y'all', 'Reckon'."

            $ Laura.change_face("confused1", eyes = "squint") 

            ch_Laura "What language is that?"
            
    return

label Laura_ask_about_Jean:
    if approval_check(Jean, threshold = "love"):
        if Laura in Partners and Jean in Partners:
            $ Laura.change_face("angry1") 

            ch_Laura "She's even more irritating now."
            ch_Laura "Thinks you're all hers. . ."
            ch_Laura "Treating you like a child."
            ch_Laura "{i}Grrrrrr{/i}."

            menu:
                extend ""
                "You also act like you own me. . . which I like. . . and I also like the way she treats me. . .":
                    $ Laura.change_face("surprised2") 

                    pause 1.0
                    
                    $ Laura.change_face("pleased2") 
                    
                    ch_Laura "I. . . see. . ."
                    
                    $ Laura.change_face("smirk2", blush = 1) 
                    
                    call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_467
                "That's just how she is, she likes to take care of me. That's as far as it goes.":
                    $ Laura.change_face("suspicious1") 
                    
                    ch_Laura "Hmmm."
                "I'm not {i}all{/i} hers, nor am I {i}all{/i} yours either.":
                    $ Laura.change_face("angry1") 
                    
                    ch_Laura "{i}Grrrrrr{/i}."
                    
                    call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_468

        else:
            $ Laura.change_face("confused1") 

            ch_Laura "You probably don't want to know what I think. . ."

            $ Laura.change_face("confused1", eyes = "squint") 

            ch_Laura "Seeing as how you two have been spending significantly more time together recently."
    elif Jean in Partners:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Laura.change_face("confused1") 

            ch_Laura "Why are you asking me?"

            $ Laura.change_face("confused1", eyes = "right") 

            ch_Laura "It's obvious she's your 'girlfriend'."

            $ Laura.change_face("angry1")

            ch_Laura "I know you two have been spending more time together."

            $ Laura.change_face("confused1") 

            ch_Laura "Does she not annoy you?"
        elif dice_roll == 2:
            $ Laura.change_face("confused1") 

            ch_Laura "You want to know what I think?"

            $ Laura.change_face("angry1")

            ch_Laura "I find her annoying."
            ch_Laura "Always worried about classes and studying, when she can't even control her own power."

            $ Laura.change_face("angry1", eyes = "right") 

            ch_Laura "Don't know why you spend so much time with her. . ."
    elif approval_check(Jean, threshold = "friendship"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Laura.change_face("confused1") 

            ch_Laura "You're asking me?"

            $ Laura.change_face("neutral") 

            ch_Laura "Is she not {i}your{/i} 'friend'?"
            ch_Laura "Don't understand how she doesn't irritate you."
        elif dice_roll == 2:
            $ Laura.change_face("angry1")

            ch_Laura "I. . . tolerate her. . ."

            $ Laura.change_face("neutral") 

            ch_Laura "She has helped me not fail all my classes so far."
    else:
        $ dice_roll = renpy.random.randint(1, 2)
        
        if dice_roll == 1:
            $ Laura.change_face("confused1") 

            ch_Laura "Who?"

            $ Laura.change_face("neutral") 

            ch_Laura "Oh, the annoying one with red hair."
            ch_Laura "I hear she's powerful."

            $ Laura.change_face("neutral", eyes = "squint") 

            ch_Laura "Wouldn't mind sparring to test that out."
        elif dice_roll == 2:
            $ Laura.change_face("confused1")  

            ch_Laura "What, why?"

            $ Laura.change_face("neutral")

            ch_Laura "She must actually enjoy studying, which makes absolutely no sense."
            ch_Laura "Always worried about grades."

            $ Laura.change_face("angry1") 

            ch_Laura "It annoys me."
            
    return

label Laura_ask_on_date:
    ch_Player "Hey, [Laura.name], wanna go on a date tonight?"
    
    if Laura.status["mad"] or Laura.status["heartbroken"]:
        $ Laura.change_face("angry1", eyes = "right") 
        
        ch_Laura "I. . . not tonight."
        
        $ Laura.change_face("neutral") 
        
        ch_Laura "Just ask me again some other day."
        
        $ Laura.History.update("said_no_to_date")
    elif Laura.status["horny"] or Laura.status["nympho"]:
        $ Laura.change_face("sly", mouth = "lipbite") 
        
        ch_Laura "Yes. . ."
        
        $ Laura.change_face("sexy", blush = 1) 
        
        ch_Laura "As long as we don't waste too much time."
        ch_Laura "I need you back in my room early, so we have enough time for. . . activities. . ."

        $ Player.date_planned[Laura] = "Player_initiated_primary"
    else:
        $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ Laura.change_face("smirk2") 
            
            ch_Laura "I do."
            ch_Laura "Be ready in the evening."

            $ Player.date_planned[Laura] = "Player_initiated_primary"
        elif dice_roll == 2:
            $ Laura.change_face("smirk2") 
            
            ch_Laura "Yes."
            
            $ Laura.change_face("smirk2", eyes = "squint") 
            
            ch_Laura "I will find you in the evening."

            $ Player.date_planned[Laura] = "Player_initiated_primary"
        elif dice_roll == 3:
            $ Laura.schedule[2] = ["bg_danger", "training"]
            
            $ Laura.change_face("neutral") 
            
            ch_Laura "Not tonight."
            ch_Laura "I have to train."
            
            $ Laura.change_face("neutral", eyes = "right") 
            
            ch_Laura "But. . . you better ask me again tomorrow."
            
            $ Laura.History.update("said_no_to_date")
        elif dice_roll == 4:
            $ Laura.schedule[2] = ["bg_danger", "training"]

            $ Laura.change_face("neutral") 
            
            ch_Laura "Can't, we're training tonight."
            
            $ Laura.change_face("neutral", eyes = "squint") 
            ch_Player "We are?"

            if Laura.location == Player.location:
                "She just stares at you." 

            menu:
                extend ""
                "I mean, of course we are. . .":
                    $ Player.schedule[2] = [
                        ["Player.location != 'bg_danger'", "renpy.say(None, 'You head to the Danger Room to train with [Laura.name].')"],
                        ["Laura.location != 'bg_danger'", "renpy.call('send_Characters', Laura, 'bg_danger', behavior = 'training')"],
                        ["Player.location != 'bg_danger'", "renpy.call('set_the_scene', location = 'bg_danger')"],
                        ["True", "renpy.call('actually_train', Laura)"]]
                "I. . . can't tonight.":
                    $ Laura.change_face("suspicious1") 

                    $ Laura.History.update("Player_rejected_training")
            
            $ Laura.History.update("said_no_to_date")

    return

label Laura_answering_phone:
    ch_Laura "Yes?"

    return