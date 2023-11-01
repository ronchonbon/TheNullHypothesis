init python:

    def Jean_asked_on_date():
        label = "Jean_asked_on_date"

        conditions = [
            "QuestPool.Quests['Jean Grey: Friendship'].completed",
            "not get_Present(location = Player.destination)",
            "time_index >= 3"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Jean_asked_on_date:
    $ ongoing_Event = True

    call receive_text(Jean, "Meet me outside your room. I gotta ask you something <3") from _call_receive_text_43
    call receive_text(Jean, "You there???") from _call_receive_text_44
    call open_texts(Jean) from _call_open_texts_2
    call receive_text(Jean, "Helloooo") from _call_receive_text_45
    call receive_text(Jean, "This is important") from _call_receive_text_46

    pause

    if Player.location in ["bg_hallway", Player.home]:
        call send_text(Jean, "sorry! I'm here already") from _call_send_text_2
    else:
        call send_text(Jean, "sorry! omw") from _call_send_text_3

    pause 2.0

    hide screen phone_screen

    call send_Characters(Jean, "bg_hallway", behavior = False) from _call_send_Characters_47
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_42
    
    $ Jean.change_face("smirk1", blush = 1)

    ch_Jean "Thanks for coming. . ."
    ch_Jean "Let's go inside, I wanna talk."

    call set_the_scene(location = Player.home) from _call_set_the_scene_43
    call send_Characters(Jean, location = Player.home, behavior = False) from _call_send_Characters_106
    
    "[Jean.name] looks like she's struggling with something."

    $ Jean.change_face("worried1", eyes = "down")

    pause 1.0

    $ Jean.eyes = "left"
    $ Jean.blush = 2

    "She finally gathers up her courage."

    $ Jean.change_face("neutral", blush = 1)

    if Jean.History.check("Player_is_worried_about_being_a_mutant"):
        ch_Jean "I just wanted to say thanks. . ."

        $ Jean.blush = 0

        ch_Player "About what?"
        ch_Jean "Well. . ."

        $ Jean.change_face("worried1")

        ch_Jean "I know you weren't thrilled about getting your powers."
        ch_Jean "But I can tell you've really been trying during our lessons."

        $ Jean.change_face("smirk1")

        call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_78

        ch_Jean ". . . just for my sake."
        ch_Player "You're welcome."

        $ Jean.change_face("smirk2")

        ch_Player "I might not be crazy about having my own powers, but I'm still glad I can help you."

        $ Jean.change_face("worried1")

        ch_Jean "I'm the big sib here, I'm supposed to be the one helping you out. . ."

        $ Jean.change_face("smirk1", blush = 1)

        ch_Jean "But I really appreciate it."

        call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_79
    else:
        ch_Jean "I just wanted to say thanks. . ."
        ch_Player "About what?"

        $ Jean.blush = 2
        
        ch_Jean "Wellll. . ."

        $ Jean.change_face("smirk1")

        ch_Jean "I know you were obviously excited to learn more about your own powers. . ."

        $ Jean.blush = 1

        ch_Jean ". . . and work with me."
        ch_Jean "I like the ambition, I've always been that way too. . ."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "But I can tell you've also been working really hard to help me figure out my problem."

        call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_80

        ch_Player "Of course, you're welcome."
        ch_Player "I was eager to learn about my own abilities. . ."

        $ Jean.change_face("pleased1", blush = 1)
        
        call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_81
        call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_82

        ch_Player ". . . but there's no way I'd give up a chance to help you."

    $ Jean.change_face("happy")

    ch_Jean "Well, as a reward for helping your big sibling out so much. . ."

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "I'm taking you out on a date!"

    $ Jean.change_face("neutral")

    "You stare at her, a bit confused."

    $ Jean.change_face("perplexed")

    ch_Jean "Where's my thank you???"

    $ Jean.change_face("confused1")

    pause 1.0

    $ Jean.change_face("angry1")

    ch_Jean "Why are you looking at me like that?"

    $ chatting = True
    $ asked_single = False
    $ asked_date = False
    $ asked_big_sis = False

    while chatting:
        menu:
            extend ""
            "You're single?" if not asked_single:
                call Jean_asked_on_date_1A from _call_Jean_asked_on_date_1A

                $ asked_single = True
            "You want to date me??" if not asked_date:
                $ Jean.change_face("worried1", blush = 1)

                ch_Jean "Well, yeah. . ."
                
                $ Jean.change_face("neutral", blush = 0)
                
                ch_Jean "When I first started here, I had to shoot down plenty of annoying attempts at flirting."
                ch_Jean "But you. . ."

                $ Jean.change_face("smirk1")

                ch_Jean "You've been helping me without expecting anything."

                call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_83

                $ asked_date = True
            "Date? But you're my 'big sib.'" if not asked_big_sis and Jean.petname == "big sis'":
                call Jean_asked_on_date_1B from _call_Jean_asked_on_date_1B

                $ asked_big_sis = True
            "I'd love to go on a date with you." if asked_single:
                call Jean_asked_on_date_1C from _call_Jean_asked_on_date_1C

                $ chatting = False
            "Sure, let's go on a date." if asked_single:
                call Jean_asked_on_date_1D from _call_Jean_asked_on_date_1D

                $ chatting = False

    $ Jean.change_face("smirk1", blush = 1)

    ch_Jean "Well. . . just send me a text whenever you're free, and I'll take you out."
    ch_Player "Where are we going?"

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "You just let me worry about that."

    $ Jean.blush = 0

    ch_Jean "Now I gotta go to bed. Goodnight, [Player.first_name]."

    $ Jean.change_face("happy")

    ch_Jean "Text me soon!"
    ch_Player "Goodnight, [Jean.petname]."

    call remove_Characters(Jean) from _call_remove_Characters_36

    $ Jean.text_options.insert(0, "free tonight for that date?")

    $ ongoing_Event = False

    # call move_location(Player.location) from _call_move_location_3

    return

label Jean_asked_on_date_1A:
    $ Jean.change_face("furious", blush = 2)

    ch_Jean "What's that supposed to mean?!"
    "Seems like you struck a nerve."
    ch_Player "No wait, I didn't mean it like. . ."
    "She interrupts you."

    $ Jean.change_face("angry1", blush = 1)

    ch_Jean "I've had a boyfriend before. . . kinda. . ."

    $ Jean.change_face("worried1")

    ch_Jean "I dated Scott for a few months. . . several years ago."

    $ Jean.change_face("angry1")

    ch_Jean "But his tiny little ego couldn't handle my teasing, he was a real jerk about it."

    $ Jean.change_face("neutral")

    ch_Jean "I never even let him kiss me. . ."

    return

label Jean_asked_on_date_1B:
    $ Jean.brows = "worried"
    $ Jean.eyes = "wide"
    $ Jean.mouth = "lipbite"
    $ Jean.blush = 3

    ch_Jean "I don't see a problem."

    $ Jean.change_face("worried1")

    ch_Jean "{size=-5}If anything that makes it better{/size}. . ."

    menu:
        extend ""
        "I agree. . .":
            $ Jean.change_face("smirk2", blush = 2)

            call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_84
            call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_85
            call change_Girl_stat(Jean, "desire", 5) from _call_change_Girl_stat_86

            ch_Jean "Good."
        "Isn't that a bit weird. . .":
            $ Jean.change_face("angry1")

            call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_87

            ch_Jean "No. . ."

    return

label Jean_asked_on_date_1C:
    $ Jean.change_face("neutral", eyes = "left", blush = 1)

    ch_Jean "Hmph, well now I'm not so sure."
    "Is she really pouting?"

    menu:
        extend ""
        "Please? I really want to go on that date.":
            $ Jean.change_face("smirk2", blush = 2)

            call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_88

            ch_Jean "How can I say no to that. . ."
        "Come on, you know I didn't mean it like that. I'd really like to go on that date.":
            $ Jean.change_face("smirk2")

            ch_Jean "Fiiine."

    return

label Jean_asked_on_date_1D:
    $ Jean.change_face("angry1")

    ch_Jean "You don't sound very thankful."
    ch_Jean "Hmph, now I'm not so sure."

    menu:
        extend ""
        "I am thankful!":
            $ Jean.change_face("smirk2", blush = 1)

            ch_Player "Please?"
            ch_Jean "Okay, fiiine."
        "I really am flattered, [Jean.name].":
            $ Jean.change_face("neutral")

            ch_Player "I swear."
            ch_Jean "Okay, okay. . ."

    return