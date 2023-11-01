init python:

    def Rogue_confession_text():
        label = "Rogue_confession_text"

        conditions = [
            "QuestPool.Quests['Rogue: Friendship'].completed",
            "Rogue not in Present",
            "weekday < 5"]

        sleeping = True

        priority = 1

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Rogue_confession_text:
    $ ongoing_Event = True

    call start_new_day from _call_start_new_day

    call phone_buzz(times = 3, intensity = 0.25) from _call_phone_buzz_1

    "You hear a distant buzzing."

    call phone_buzz(times = 3, intensity = 0.5) from _call_phone_buzz_2
        
    "It's getting louder."

    call phone_buzz(times = 3) from _call_phone_buzz_3

    $ fade_in_from_black(0.4)

    "You rub the sleep from your eyes as your phone buzzes once more."

    call receive_text(Rogue, "Mornin!", buzz = False) from _call_receive_text_488
    call receive_text(Rogue, ":))", buzz = False) from _call_receive_text_489
    call receive_text(Rogue, "You up yet hon'?", buzz = False) from _call_receive_text_490
    call open_texts(Rogue) from _call_open_texts_8
    call send_text(Rogue, "good morning!") from _call_send_text_38
    call send_text(Rogue, "just got up") from _call_send_text_39
    call receive_text(Rogue, "Got class this morning, can I come over after?") from _call_receive_text_491
    call receive_text(Rogue, "I wanna talk about something") from _call_receive_text_492
    call send_text(Rogue, "sure") from _call_send_text_40
    call send_text(Rogue, "see ya later") from _call_send_text_41
    call receive_text(Rogue, ":)))") from _call_receive_text_493

    $ phone_interactable = True

    $ ongoing_Event = False

    return

init python:

    def Rogue_confession_afternoon():
        label = "Rogue_confession_afternoon"

        conditions = [
            "EventScheduler.Events['Rogue_confession_text'].completed",
            "day - EventScheduler.Events['Rogue_confession_text'].completed == 1",
            "Player.destination not in [Player.home, 'bg_shower_Player'] or time_index == 2"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, priority = priority, waiting = waiting, traveling = traveling)

label Rogue_confession_afternoon:
    $ ongoing_Event = True

    if Player.destination != Player.home and time_index < 2:
        if Player.destination == "bg_classroom":
            call remove_Characters(location = "bg_classroom", fade = False) from _call_remove_Characters_189
            call set_the_scene(location = "bg_classroom") from _call_set_the_scene_205

            "You get to class and see [Rogue.name] sitting near the back."

            menu:
                extend ""
                "Sit next to [Rogue.name]":
                    call Rogue_confession_afternoon_class_sat_next_to from _call_Rogue_confession_afternoon_class_sat_next_to
                "Pick a random seat":
                    call Rogue_confession_afternoon_class_sat_random from _call_Rogue_confession_afternoon_class_sat_random
                    
            $ Player.History.update("attended_class")
        else:
            call Rogue_confession_afternoon_wander from _call_Rogue_confession_afternoon_wander

        ch_Kurt "Mhm."

        $ Kurt.change_face("happy")

        ch_Kurt "Vell, I don't sink you do it on purpose at least."

        call remove_Characters(Kurt) from _call_remove_Characters_190

        ch_Player "Do what. . . ?"

    if Player.destination == "bg_classroom":
        "You head back to your room to wait for [Rogue.name]."
    else:
        $ fade_to_black(0.4)

        if Player.location == Player.home:
            "The day flies by, and soon you're waiting in your room for [Rogue.name]."
        else:
            "The day flies by, and you soon head back to your room to wait for [Rogue.name]."

    $ time_index = 2
    
    $ clock = Player.max_stamina

    call set_the_scene(location = Player.home) from _call_set_the_scene_206

    $ EventScheduler.Events["Rogue_confession"].start()

    $ ongoing_Event = False

    return

label Rogue_confession_afternoon_class_sat_next_to:
    $ Rogue.change_face("pleased2")

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits["Casual 1"], instant = True) from _call_change_Outfit_18
    call add_Characters(Rogue) from _call_add_Characters

    ch_Rogue "Howdy, [Player.first_name]!"

    $ Rogue.change_face("pleased1")

    ch_Rogue "Wasn't sure if ya also had lecture today."
    ch_Player "Yeah my schedule's a bit. . . free form."

    $ Rogue.change_face("confused1")

    pause 1.0

    $ Rogue.change_face("neutral")

    ch_Player "By the way, what did you wanna talk about?"

    $ Rogue.change_face("surprised2", eyes = "right", blush = 1)

    pause 1.0

    $ Rogue.eyes = "wide"

    ch_Rogue "Ah told you after class, hon'."

    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "In private."

    $ Rogue.change_face("neutral", eyes = "down")

    "A few more people trickle in - you notice [Kurt.name] sitting across the room."

    $ Rogue.eyes = "right"

    "The lecture begins - even superpowered mutants learn calculus."

    $ Rogue.eyes = "neutral"

    "You notice [Rogue.name] sneaking glances at you."

    $ Rogue.blush = 1

    "She seems a bit nervous."

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2

    $ Rogue.blush = 2

    $ fade_in_from_black(0.4)

    ch_Rogue "Ah gotta go. . . freshen up."

    $ Rogue.eyes = "wide"
    $ Rogue.blush = 3

    ch_Rogue "Wait for me in yer room?"

    call remove_Characters(Rogue) from _call_remove_Characters_191

    "She rushes off."

    $ Kurt.change_face("confused")
    $ Kurt.outfit = "casual"

    call Kurt_teleports_in("Vat did you do zis time?") from _call_Kurt_teleports_in_3

    ch_Player "Gah!"

    $ Kurt.change_face("happy")

    ch_Player "Dude, when did you get here."
    ch_Kurt ". . . "

    $ Kurt.change_face("neutral")

    ch_Player "She just wanted to chat later! She's been acting extra nervous today."

    return

label Rogue_confession_afternoon_class_sat_random:
    "You sit down in a random seat."
    "A few people trickle in - you notice [Kurt.name] sitting across the room."
    "The lecture begins - even superpowered mutants learn calculus."
    "You look over and notice [Rogue.name] a bit distracted during the lecture."

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2

    $ fade_in_from_black(0.4)

    "At the end of class, [Rogue.name] packs up and rushes towards the door."
    "She doesn't see you and almost bumps right into you."

    $ Rogue.change_face("surprised1", blush = 1)

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits["Casual 1"], instant = True) from _call_change_Outfit_17
    call add_Characters(Rogue) from _call_add_Characters_34

    ch_Rogue "Oh! Hey hon'. . ."
    ch_Rogue "Didn't expect to see you here. . ."

    $ Rogue.change_face("worried1")

    ch_Player "Is everything okay?"

    $ Rogue.change_face("pleased2", blush = 2)

    ch_Rogue "Yeah, ah'm fine, everythin's fine."
    ch_Rogue "Ah gotta go. . . freshen up."

    $ Rogue.blush = 3

    ch_Rogue "Wait for me in yer room?"

    call remove_Characters(Rogue) from _call_remove_Characters_192

    "She rushes off."

    $ Kurt.change_face("confused")
    $ Kurt.outfit = "casual"

    call Kurt_teleports_in("Vat is up viz zat one?") from _call_Kurt_teleports_in_4

    ch_Player "Gah!"

    $ Kurt.change_face("happy")

    ch_Player "Dude, when did you get here."
    ch_Kurt ". . . "

    $ Kurt.change_face("neutral")

    ch_Player "I'm not sure what's up with her. She did want to chat with me later. . ."

    return

label Rogue_confession_afternoon_wander:
    call remove_Characters(location = "bg_hallway", fade = False) from _call_remove_Characters_193
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_207

    "As you leave your room, you see [Rogue.name] walking down the hall."
    ch_Player "[Rogue.name]!"

    $ Rogue.change_face("surprised1")

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits["Casual 1"], instant = True) from _call_change_Outfit_21
    call add_Characters(Rogue) from _call_add_Characters_1

    ch_Rogue "Howdy, [Player.first_name]!"

    $ Rogue.change_face("pleased1")

    ch_Rogue "You comin' to class?"
    ch_Player "Not right now, but what did you wanna talk about?"

    $ Rogue.change_face("surprised2", eyes = "right", blush = 1)

    pause 1.0

    $ Rogue.eyes = "wide"
    $ Rogue.blush = 2

    "She glances around anxiously as people walk by."
    ch_Rogue "Not now, hon'."
    
    $ Rogue.change_face("worried1", blush = 2)

    ch_Rogue "Later, in private."

    $ Rogue.eyes = "wide"
    $ Rogue.blush = 3

    ch_Rogue "Ah gotta. . . freshen up after class. Wait for me in yer room?"
    ch_Player "Uh, okay, sure."
    ch_Player "I'll see you later."

    call remove_Characters(Rogue) from _call_remove_Characters_194

    "She hurries off."

    $ Kurt.change_face("confused")
    $ Kurt.outfit = "casual"

    call Kurt_teleports_in("Vat did you do zis time?") from _call_Kurt_teleports_in_5

    ch_Player "Gah!"

    $ Kurt.change_face("happy")

    if Kurt.History.check("teleported_in") == 1:
        ch_Player "Jesus, do you just appear out of thin air???"
        ch_Kurt "Ja."
        ch_Player "Okay. . ."

    $ Kurt.change_face("neutral")

    ch_Player "Well, I swear I didn't do anything."
    ch_Player "She just wanted to chat later. . ."
    ch_Player "She seems extra nervous."

    return

init python:

    def Rogue_confession():
        label = "Rogue_confession"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_confession:
    $ ongoing_Event = True

    call remove_Characters(location = Player.home, fade = False) from _call_remove_Characters_195

    pause 1.0

    "After about 15 minutes, you hear a knock on the door."

    call set_the_scene(location = Player.home) from _call_set_the_scene_208

    "You get up and let [Rogue.name] in."

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits["Casual 2"], instant = True) from _call_change_Outfit_19

    call add_Characters(Rogue) from _call_add_Characters_36

    "The scent of perfume follows her into the room."

    $ Rogue.blush = 1

    "She seems pretty anxious."
    ch_Player "Hey, [Rogue.name]."
    ch_Player "So, what did you wanna talk about?"

    $ Rogue.blush = 2

    "She blushes even more."

    $ Rogue.change_face("manic", blush = 2)

    ch_Rogue "You have a good day so far. . . ?"
    ch_Player "Uh, yeah, thanks."
    ch_Player "Bu. . ."

    $ Rogue.blush = 3

    ch_Rogue "Did ya try some of that cornbread at breakfast this mornin'?"
    ch_Rogue "Almost as good as back home. . ."

    $ Rogue.blush = 2

    ch_Player "Yeah, it was actually really good."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Player "The food here is always great."

    menu:
        extend ""
        "Better than. . . back home.":
            ch_Player "I hope my family's doing alright. . ."

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_618
        "Sure beats the food I got back home.":
            ch_Player "At least there's a plus side to all of this. . ."
        "Still not as good as. . . back home.":
            ch_Player "I still miss my mom's cooking sometimes."

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_619
    
    $ Rogue.change_face("sad", blush = 0)

    "She seems to regain a bit of her composure."
    ch_Rogue ". . ."

    $ Rogue.change_face("worried2")

    ch_Rogue "Are ya doin' alright?"
    ch_Rogue "You've been a real great student to tutor."
    ch_Rogue "Ah can tell you've been tryin' real hard."

    $ Rogue.blush = 1

    ch_Rogue "But if ya want someone to talk about. . . other stuff."
    ch_Player "Thanks, [Rogue.name]."

    $ Rogue.change_face("worried1")

    ch_Player "I'm not gonna lie, it's been a struggle."

    menu:
        extend ""
        "I'm. . . angry.":
            call Rogue_confession_1A from _call_Rogue_confession_1A
        "I've been. . . out of my depth.":
            call Rogue_confession_1B from _call_Rogue_confession_1B
        "But, I'm. . . determined.":
            call Rogue_confession_1C from _call_Rogue_confession_1C

    $ Rogue.change_face("worried1")

    ch_Player "At first I thought I'd be on my own around here."

    $ Rogue.change_face("neutral")

    ch_Player "Was feeling pretty sorry for myself. . ."

    if Laura.History.check("trained_with_Player") >= 2 and Jean.History.check("trained_with_Player") >= 2:
        $ Rogue.change_face("smirk1")
        
        ch_Player "But you, [Laura.name], and [Jean.name] have really helped me out. . ."
        ch_Player "More than was expected from any of you all."
        ch_Player "And just like that, I have people I care about."
        ch_Player "It's not just about me anymore."

        $ Rogue.change_face("smirk2")
    elif Laura.History.check("trained_with_Player") >= 2:
        $ Rogue.change_face("smirk2")
        
        ch_Player "But you and [Laura.name] have really helped me out. . ."
        ch_Player "More than was expected from either of you."
        ch_Player "And just like that, I have people I care about."
        ch_Player "It's not just about me anymore."

        $ Rogue.change_face("happy")
    elif Jean.History.check("trained_with_Player") >= 2:
        $ Rogue.change_face("smirk1")
        
        ch_Player "But you and [Jean.name] have really helped me out. . ."
        ch_Player "More than was expected from either of you."
        ch_Player "And just like that, I have people I care about."
        ch_Player "It's not just about me anymore."

        $ Rogue.change_face("happy")
    else:
        $ Rogue.change_face("smirk1")
        
        ch_Player "But you've really helped me out. . ."
        ch_Player "More than was expected of you."
        ch_Player "And just like that, I have someone I care about."
        ch_Player "It's not just about me anymore."

        $ Rogue.change_face("smirk2")
        
    ch_Player "So, either way, I'm gonna catch my ass up."
    "She stares at you for a moment, smiling."
    ch_Player "What?"

    $ Rogue.blush = 1

    ch_Rogue "Oh, nothin'."

    $ Rogue.blush = 2

    ch_Rogue "Ah can just tell ah'd still like you even if we weren't mutants."

    $ Rogue.change_face("pleased2", blush = 3)

    "She realizes what she just said and blushes."
    ch_Player "{i}Ahem{/i}. . ."

    menu:
        extend ""
        "Okay [Rogue.name], c'mon, what did you {i}actually{/i} come here to talk about?":
            $ Rogue.change_face("worried1")

            call change_Girl_stat(Rogue, "trust", -5) from _call_change_Girl_stat_620

            ch_Rogue "Alright, fine."
            ch_Rogue "Well. . ."
        "Sorry for bringing down the mood, but what did you actually want to talk about?":
            $ Rogue.change_face("worried1")

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_621

            ch_Rogue "Don't worry hon', ah appreciate the honesty."
            ch_Rogue "Well. . ."
        "Now I kinda want more cornbread. Wanna grab some food?":
            $ Rogue.change_face("pleased1")

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_622
            call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_623

            ch_Rogue "Heh, maybe after ah've said my peace."
            ch_Rogue "Speaking of. . ."

    $ Rogue.change_face("neutral")

    ch_Rogue "With all the time we've spent together. . ."

    $ Rogue.change_face("smirk1", blush = 1)

    ch_Rogue ". . . Ah think we've gotten to know each other pretty well."

    $ Rogue.change_face("worried1")

    ch_Rogue "We're friends, right?"

    menu:
        extend ""
        "For sure.":
            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_624

            $ Rogue.change_face("pleased1", blush = 1)
        "Yeah, I'd like to think so.":
            pass

    ch_Rogue "Well, ah was thinkin'. . ."

    $ Rogue.blush = 2

    ch_Rogue "Maybe you'd wanna be. . . {size=-5}more than friends{/size}."

    $ chatting = True
    $ asked_more_than_friends = False
    $ asked_dating = False
    $ asked_what_had_in_mind = False
    $ said_sure = False
    $ said_would_like_it = False

    while chatting:
        menu:
            extend ""
            "More than friends?" if not asked_more_than_friends and not asked_dating and not asked_what_had_in_mind:
                call Rogue_confession_2A from _call_Rogue_confession_2A

                $ asked_more_than_friends = True
            "As in, 'dating'?" if not asked_dating:
                call Rogue_confession_2B from _call_Rogue_confession_2B

                $ asked_dating = True
            "What exactly did you have in mind?" if not asked_what_had_in_mind:
                call Rogue_confession_2C from _call_Rogue_confession_2C

                $ asked_what_had_in_mind = True
            "Uh, sure. . . we can be more than friends." if asked_more_than_friends or asked_dating:
                $ Rogue.change_face("confused1")

                call change_Girl_stat(Rogue, "love", -5) from _call_change_Girl_stat_625

                $ chatting = False
            "I'd really like that." if asked_more_than_friends or asked_dating:
                ch_Player "To be {i}more{/i} than friends."

                $ Rogue.change_face("happy", blush = 1)

                call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_626

                $ chatting = False

    $ Rogue.change_face("neutral")

    ch_Player "So, how about a proper date then?"

    $ Rogue.change_face("happy", blush = 1)

    pause 1.0

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'd like that."
    ch_Rogue "Just text me whenever you're ready to head out."
    ch_Rogue "Ah'll see ya later, hon'."
    ch_Player "See ya."

    call remove_Characters(Rogue) from _call_remove_Characters_196

    "You spot a bit more confidence in her step than usual."

    pause 1.0
    
    call wait_around(silent = True) from _call_wait_around_1

    $ Rogue.text_options.insert(0, "want to go on that date tonight?")

    $ ongoing_Event = False

    # call move_location(Player.home) from _call_move_location_33

    return

label Rogue_confession_1A:
    ch_Player "At first I was just pissed about the whole situation."
    ch_Player "Getting attacked out of nowhere."

    $ Rogue.change_face("worried2")

    ch_Player "Ripped away from my friends and family."
    ch_Player "But now I see how fucked the world is for mutants in general. . ."

    $ Rogue.change_face("worried3")

    ch_Player "Makes my blood boil."

    call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_627

    ch_Rogue "It really ain't fair. . ."
    ch_Rogue "For any of us."
    ch_Rogue "Nobody chooses to get powers."

    $ Rogue.change_face("sad")

    ch_Rogue "Not to mention what your powers do to people. . .{p} when you can't control 'em yet. . ."

    return

label Rogue_confession_1B:
    ch_Player "I was really overwhelmed at first."
    ch_Player "Attacked by my goddamn college professor of all people."
    ch_Player "Then I find out I'm a mutant. . ."

    $ Rogue.change_face("worried2")

    ch_Player "And people want to kidnap or kill me because of it?!"
    ch_Player "This all felt so surreal."

    $ Rogue.change_face("worried1")

    ch_Player "It's been taking a while to really process everything. . ."

    call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_628

    ch_Rogue "Ah know how you feel."
    ch_Rogue "It's a lot to go through."

    $ Rogue.change_face("sad")

    ch_Rogue "Most of the time, discovering your powers. . . it ain't a great experience."

    return

label Rogue_confession_1C:
    ch_Player "I haven't really been dealing with my situation in the healthiest of ways."
    ch_Player "I dove headfirst into studying and training. . ."
    ch_Player "But it's just a coping mechanism."
    ch_Player "If I lose this momentum, reality will catch up. . ."

    $ Rogue.change_face("worried2")

    ch_Player ". . . and crush me."
    ch_Player "So, I guess I won't lose the momentum."
    ch_Player "I'll sprint to the point where I can protect myself and the people I care about."

    $ Rogue.change_face("worried1")

    ch_Player "Then it won't matter what catches up to me."

    call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_629
    call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_630

    ch_Rogue "Reality sure ain't kind to people like us."
    ch_Rogue "I reckon that's not. . . the worst way to deal with the stress."

    $ Rogue.change_face("sad")

    ch_Rogue "Better than what ah did when my powers first emerged. . ."

    return

label Rogue_confession_2A:
    ch_Rogue "Well. . . we're pretty close already."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "Heh, ah mean, we've even held hands already."

    if Rogue.History.check("Player_faked_injury"):
        $ Rogue.change_face("worried1")

        ch_Rogue "At first you were a bit of a jerk."

        $ Rogue.change_face("neutral")

        ch_Player "Yeah. . . sorry. I still feel bad about that."
        ch_Rogue "Don't worry none."
        ch_Rogue "You apologized first thing the next day."
        ch_Rogue "Ah appreciate you not pullin' anythin' like that once you knew it was a big deal."

        $ Rogue.change_face("smirk2")

        call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_631
        call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_632

        ch_Rogue "And not once did ya take advantage of me bein' a bit desperate about finally bein' able to touch someone. . ."
    else:
        $ Rogue.change_face("pleased1", blush = 2)

        ch_Rogue "Ya did flirt a bit at the start."

        $ Rogue.change_face("smirk1")

        ch_Rogue "But you even came to apologize when you thought it made me uncomfortable."
        ch_Rogue "Ah really appreciated that."
        ch_Rogue "And not once did ya take advantage of me bein' a bit desperate about finally bein' able to touch someone. . ."
        
        $ Rogue.change_face("smirk2")

        call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_633
        call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_634

        ch_Rogue "You've been a right gentleman about it."
    
    if EventScheduler.Events["Laura_first_friend_part_two"].completed:
        ch_Rogue "Also what ya did for [Laura.name]."
        ch_Rogue "Tryin' to help her out and all."
        ch_Rogue "That was real sweet of you."

        call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_635
        call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_636

    return

label Rogue_confession_2B:
    ch_Rogue "Ah. . . really, {i}really{/i} like you. . ."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "So, yeah. . . datin'."

    menu:
        extend ""
        "I really, {i}really{/i} like you too.":
            ch_Player "I'm glad you feel the same way."
            ch_Player "To be honest, I was working up the courage to ask you out too."

            $ Rogue.change_face("pleased2", blush = 2)

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_637
        "Oh. . . uh, yeah, that could be cool.":
            $ Rogue.change_face("perplexed")

            call change_Girl_stat(Rogue, "love", -5) from _call_change_Girl_stat_638

            ch_Player "I like you too."

    return

label Rogue_confession_2C:
    ch_Rogue "Ah'm a bit of a sucker for traditional romance. . ."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Was kinda hopin' we could start off slow."

    menu:
        extend ""
        "So you're saying I can't kiss you right now?":
            $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 2)

            ch_Rogue "Let's at least go on a date 'fore any of that. . ."

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_639
            call change_Girl_stat(Rogue, "desire", 5) from _call_change_Girl_stat_640
        "That's fine by me, no rush to jump into anything.":
            $ Rogue.change_face("smirk2")

            call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_641

    return