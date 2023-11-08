init python:

    def Jean_back_from_mission():
        label = "Jean_back_from_mission"

        conditions = [
            "EventScheduler.Events['Jean_leaving_for_mission'].completed",
            "day - EventScheduler.Events['Jean_leaving_for_mission'].completed > 2",
            "Player.location in ['bg_girls_hallway', 'bg_hallway'] or Player.location in bedrooms",
            "Player.destination not in ['bg_girls_hallway', 'bg_hallway'] and Player.destination not in bedrooms and 'bg_shower' not in Player.destination",
            "not Party"]

        traveling = True

        priority = 1

        return EventClass(label, conditions, traveling = traveling, priority = priority)

label Jean_back_from_mission:
    $ ongoing_Event = True
    
    $ temp_destination = Player.destination

    "As you exit the dorms, a voice pops into your head."

    $ Charles.telepathic = True

    ch_Charles "[Player.first_name], could you please meet come to my study."

    $ Charles.telepathic = False

    "You turn around and head back."

    call send_Characters([Jean, Charles], "bg_study") from _call_send_Characters_51
    
    call change_Outfit(Jean, Jean.Wardrobe.Outfits["Hero (Chapter I)"], instant = True) from _call_change_Outfit_3
    
    call set_the_scene(location = "bg_study") from _call_set_the_scene_49

    $ Jean.change_face("happy")

    "As you approach, [Jean.name] notices you. Her face lights up."
    ch_Jean "Hi, [Player.first_name]!"
    ch_Player "Hey, [Jean.name], [Charles.name]. What's going on?"

    $ Jean.change_face("neutral")

    ch_Charles "Good morning, [Player.first_name]. It seems you two are already acquainted."
    ch_Charles "While on mission, Jean and her team were ambushed. The incident bore striking similarities to the events that led to your arrival here."
    
    $ Jean.change_face("worried1")
    
    ch_Charles "Jean has had. . . difficulties controlling her powers since then."
    ch_Charles ". . . As a result, I am assigning you as her training partner."
    ch_Charles "With your nullification ability, even if she loses control during training, you will be there to prevent any harm."
    ch_Charles "I also believe this will be a good opportunity to test the limits of your own powers."

    menu:
        extend ""
        "That sounds great! I'm happy to help [Jean.name], and I've been eager to learn how to use my powers.":
            ch_Player "Everyone around here is so capable, I want to be able to help out as well."

            $ Jean.change_face("smirk2", blush = 1)

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_107
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_108

            $ Jean.History.update("Player_happy_to_help")
        "An excuse to spend more time with [Jean.name]? Count me in.":
            $ Jean.change_face("confused1")

            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_109

            $ Jean.History.update("Player_wants_excuse_to_spend_time_together")
        "To be honest, I still don't know how I feel about having powers. But if it helps [Jean.name], then I'll do it.":
            $ Jean.change_face("sad")

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_110

            $ Jean.History.update("Player_is_worried_about_being_a_mutant")

    ch_Charles "Very good. Now, I must be off. Please excuse me."

    $ Jean.change_face("neutral")

    call remove_Characters(Charles) from _call_remove_Characters_44

    ch_Jean "So, hey."

    if Jean.History.check("Player_happy_to_help") or Jean.History.check("Player_wants_excuse_to_spend_time_together"):
        ch_Jean "I'm glad you have that nullification ability, otherwise I don't know how I'd be able to get confidence in my powers again."
        ch_Player "I'm just glad you're okay."

        if Jean.History.check("Player_happy_to_help"):
            $ Jean.change_face("smirk1", blush = 1)

            ch_Jean "Thanks. . ."
            ch_Player "Hopefully both of us will come out of this understanding our abilities better. I really want to start getting stronger."

            $ Jean.change_face("smirk2")

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_111

            ch_Jean "I'm glad you feel the same way."

            $ Jean.change_face("happy")

            ch_Jean "Plus we get to spend more time together!"
            ch_Jean "I'll take good care of you, don't worry."
        elif Jean.History.check("Player_wants_excuse_to_spend_time_together"):
            $ Jean.change_face("smirk1")

            ch_Jean "Thanks. . ."

            $ Jean.change_face("smirk2")

            ch_Jean ". . . and excited to be working with you."
            ch_Jean "We'll be spending plenty of time trying to figure out our powers together."
            ch_Jean "Don't worry, I'll take good care of you."
    else:
        $ Jean.change_face("worried1")

        ch_Jean "I know you're not too happy about being a mutant and all. . ."
        ch_Jean "But without that nullification ability, I don't know how I'd be able to get confidence in my powers again."
        ch_Player "I'm glad I can help. It's just that everything has been so sudden. I was in a norm- er, I was in college like a week ago!"
        
        $ Jean.change_face("sad")
        
        ch_Player "I'm just worried about my family. . ."
        ch_Jean "Yeah. . . I get it. Trust me, we've all been there."

        $ Jean.change_face("smirk1")

        ch_Jean "But don't worry, I'll take good care of you."
        
    ch_Jean "I'll be like, your campus big sib!"

    menu:
        extend ""
        "So. . . I'll be your 'little bro''?":
            $ Jean.change_face("surprised2", blush = 1)

            ch_Jean "Haha, yeah. I guess so. . ."

            $ Jean.change_face("surprised1", blush = 2)

            pause 1.0

            $ Jean.blush = 1

            pause 1.0

            $ Jean.blush = 0

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_112
        "Heh, I guess so.":
            pass

    $ Jean.change_face("smirk2")

    ch_Jean "Oh! By the way, if you want any extra help with classes or training, just let me know."

    menu:
        extend ""
        "Yes, please.":
            ch_Player "That would be great, I'll need all the help I can get to catch up."

            $ Jean.blush = 1
            
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_113
            call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_114

            ch_Jean "Can you. . . say that again. . ."
            ch_Player "Uh. . . that would be great. . ."
            ch_Jean "No, the first part."
            ch_Player "Yes, please?"

            $ Jean.change_face("surprised2", blush = 2)
            
            call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_115

            "[Jean.name] stares at you for a second before snapping out of it."
        "That would be great.":
            ch_Player "I'll take all the help I can get in order to catch up."

            $ Jean.change_face("happy")

            ch_Jean "Happy to help!."

            $ Jean.change_face("surprised2", blush = 1)

            ch_Jean ". . ."
            "She seems surprised by her own enthusiasm."

    $ Jean.change_face("neutral")

    ch_Jean "{i}Ahem{/i}. . . well I'm usually pretty busy with studying and exams."

    $ Jean.change_face("smirk1")

    ch_Jean "But I'll make time just for you."

    menu:
        extend ""
        "I really appreciate that.":
            $ Jean.blush = 1

            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_116

            ch_Player "Thanks, [Jean.name]."
            ch_Jean "Of course!"
        "You don't have to go out of your way. . .":
            ch_Player "But, thanks, [Jean.name]."

    ch_Jean "Just let me know when you wanna start working on our powers. Take my number so you can shoot me a text."
    "You give [Jean.name] your phone and she adds herself as a contact."
    ch_Jean "Alright, I gotta head out. I'll see you later!"
    ch_Player "See ya."

    call remove_Characters(Jean) from _call_remove_Characters_45

    "You continue along your way."

    $ Contacts.append(Jean)

    $ Jean.chat_options.insert(0, "Ready for that training session?")
    $ Jean.text_options.insert(0, "I'm ready for that training session")

    $ ongoing_Event = False

    if Player.location != temp_destination:
        call travel(temp_destination) from _call_travel
    
    return