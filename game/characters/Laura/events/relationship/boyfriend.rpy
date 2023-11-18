init python:

    def Laura_boyfriend_trigger_part_one():
        label = "Laura_boyfriend_trigger_part_one"

        conditions = [
            "QuestPool.Quests['Laura_dating_Quest'].completed"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Laura_boyfriend_trigger_part_one:
    $ Laura.chat_options.insert(0, f"Ask her to be your girlfriend")

    python:
        for C in Partners:
            if C != Laura:
                if not C.History.check("told_wants_multiple_partners") or Laura not in C.knows_about:
                    C.History.update("cheated_on_relationship")

                    if not Player.History.check(f"cheated_on_{C.tag}_with_Laura_relationship", tracker = "recent"):
                        Player.History.update(f"cheated_on_{C.tag}_with_Laura_relationship")

    return

init python:

    def Laura_boyfriend_trigger_part_two():
        label = "Laura_boyfriend_trigger_part_two"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_boyfriend_trigger_part_two:
    $ ongoing_Event = True

    if Laura.location == Player.location and Player.location != Player.home:
        $ Laura.change_face("confused1") 
        
        ch_Player "Hey, [Laura.name]. Can we talk in my room?" 
        ch_Laura "Fine." 

        if Player.location != "bg_hallway":
            call remove_Characters(location = "bg_hallway") from _call_remove_Characters_99
            call set_the_scene(location = "bg_hallway") from _call_set_the_scene_122
            call send_Characters(Laura, "bg_hallway", behavior = False) from _call_send_Characters_105

        "You open your door, and [Laura.name] follows you inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_100
        call set_the_scene(location = Player.home) from _call_set_the_scene_123
    elif Laura.location != Player.location:
        if current_phone_screen == "text":
            call send_text(Laura, "can you meet me in my room?") from _call_send_text_24
            call send_text(Laura, "I want to talk about something") from _call_send_text_25
            call receive_text(Laura, "Fine") from _call_receive_text_291
            call receive_text(Laura, "On my way") from _call_receive_text_292
        elif current_phone_screen == "call":
            ch_Player "Hey, [Laura.name]. Can we talk in my room?" 
            ch_Laura "Fine."
            ch_Laura "On my way."

        pause

        hide screen phone_screen

        call remove_Characters(location = Player.home) from _call_remove_Characters_101
        call set_the_scene(location = Player.home) from _call_set_the_scene_124

        "You wait less than a minute before you hear a knock on the door."
        "You open it, and [Laura.name] pushes her way in."

    call send_Characters(Laura, location = Player.home, behavior = False) from _call_send_Characters_255

    $ Laura.change_face("angry1", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Before you speak, there is also something I need to talk to you about." 

    $ Laura.change_face("suspicious1", blush = 2)

    $ EventScheduler.Events["Laura_boyfriend"].start()

    $ ongoing_Event = False

    return

init python:

    def Laura_boyfriend_alternate_trigger():
        label = "Laura_boyfriend_alternate_trigger"

        conditions = [
            "not EventScheduler.Events['Laura_boyfriend'].completed",

            "day - EventScheduler.Events['Laura_boyfriend_trigger_part_one'].completed >= 4",
            
            "Player.location in public_locations and Laura.location != Player.location",

            "Laura.is_in_normal_mood()"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Laura_boyfriend_alternate_trigger:
    $ ongoing_Event = True

    call send_Characters(Laura, Player.location, behavior = False) from _call_send_Characters_107

    $ Laura.change_face("angry1", blush = 1)

    "[Laura.name] appears out of nowhere."
    ch_Laura "We are going to talk."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "In private."
    ch_Player "Wha-"

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "{i}Now{/i}." 

    if Player.location != "bg_hallway":
        "She grabs your arm, dragging you to your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_102
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_125
        call send_Characters(Laura, location = "bg_hallway", behavior = False) from _call_send_Characters_256

    $ Laura.change_face("neutral")

    ch_Laura "Open your door."
    "You unlock it, and she pushes you inside the room."

    call remove_Characters(location = Player.home) from _call_remove_Characters_103
    call set_the_scene(location = Player.home) from _call_set_the_scene_126
    call send_Characters(Laura, location = Player.home, behavior = False) from _call_send_Characters_257

    $ Laura.change_face("angry1", blush = 1)

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "There is something I need to talk to you about." 

    $ Laura.change_face("suspicious1", blush = 2)

    menu:
        extend ""
        "Progress your relationship with [Laura.name]":
            pass
        "Postpone relationship talk":
            $ Laura.change_face("suspicious2", blush = 3)

            ch_Player "Uh. . . this is actually a pretty bad time, [Laura.name]."

            $ Laura.change_face("angry1", blush = 1)

            pause 1.0

            $ Laura.change_face("angry1", eyes = "right", blush = 1)

            pause 1.0

            ch_Laura ". . . Fine."

            call remove_Characters(Laura) from _call_remove_Characters_104

            "She walks out of your room before you can react."

            $ Laura.wants_alone_time = 2

            return

    $ EventScheduler.Events["Laura_boyfriend"].start()

    $ ongoing_Event = False

    return

init python:

    def Laura_boyfriend():
        label = "Laura_boyfriend"

        conditions = [
            "False"]

        priority = 1

        return EventClass(label, conditions, priority = priority)

label Laura_boyfriend:
    $ ongoing_Event = True

    $ Laura.change_face("suspicious1", blush = 1)

    $ temp = Laura.petname

    ch_Player "[temp], what is it?" 

    $ Laura.change_face("angry1", blush = 1)

    ch_Player "Is everything okay?" 

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Yes. . ."
    ch_Laura "I'm fine, for the most part."

    $ Laura.change_face("suspicious1")

    ch_Laura "Except for one thing."
    ch_Laura "There is a problem, and it's your fault."

    $ Laura.change_face("angry1")

    ch_Player "My fault?"
    ch_Laura "Yes."
    ch_Laura "All the time we are spending together. . ."

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "Rogue believes it has led me to develop an. . . 'emotional connection'. . . to you."

    $ Laura.change_face("furious", blush = 2)

    ch_Player "Oh. . ."
    ch_Laura "And I tend to agree with her. . ."

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Player "OH!"

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "We have gone on a number of dates." 

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "And. . . kissed each other."

    $ Laura.change_face("furious", blush = 2)

    ch_Laura "I want you to be my 'boyfriend.'"

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Have we not met the criteria at this point?" 
    "You feel a mix of excitement, but also. . . worry."

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "Why are you making that face?" 
    ch_Player "It's not that I don't want to be your boyfriend."
    ch_Player "I just. . ."

    $ Laura.change_face("confused2")

    ch_Player "I'm worried I might be unintentionally taking advantage of you." 

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Player "I'm the only person you trust to get close enough to touch. . . without killing."
    ch_Player "I'm your first friend, first kiss." 

    $ Laura.change_face("furious", blush = 1)

    ch_Player "First. . . everything."
    ch_Player "I'm worried that since it's your first time exploring these feelings, you're quicker to jump into things." 

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    ch_Laura "Are you an idiot?" 

    menu:
        extend ""
        "I'm being serious. I care about you too much not to worry about these things.": 
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_355 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_356
        ". . . probably? But, c'mon, it's not that far-fetched. I really care about you, and I'm worried. . .":
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_357
        "That's rude, and don't tell me you can't see where I'm coming from. I'm not so sure I can trust your judgment. . .": 
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_358 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_359

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "Just because I lack certain. . . social skills, doesn't mean I'm helpless and can't think for myself."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "It's true, you're the only person who has ever touched me in that way, and vice versa."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I've probably tried to kill anyone else I've ever touched at one point. . ."

    $ Laura.change_face("neutral")

    ch_Player "Even Storm, or Logan?"
    ch_Laura "Yes. . . fought them the first time we met. . ." 

    $ Laura.change_face("angry1")

    ch_Laura "But I am not 'jumping' into things, and you are not manipulating me into doing anything."
    ch_Laura "I was at this school for weeks before you arrived. More than enough time for me to become friends with anyone else."

    $ Laura.change_face("neutral")

    ch_Laura "But they're all. . . sub-standard. . . not including Rogue."
    ch_Laura "And you're the only person I've ever had these feelings for."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Not to mention, I was the one who initiated the dating process. . ." 

    $ Laura.change_face("angry1")

    ch_Player "Okay, okay, you have a point." 

    $ Laura.change_face("neutral")

    ch_Player "I just wanted to make sure we're both comfortable with where things are going." 

    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Player "Because I definitely do want to progress things."

    $ Laura.change_face("sly", blush = 1)

    ch_Player "But. . ."

    if len(Partners) > 0:
        $ Laura.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        if len(Partners) == 1:
            ch_Laura "Obviously I realize you are already in a relationship with [Partners[0].public_name]."
        elif len(Partners) == 2:
            ch_Laura "Obviously I realize you are already in a relationship with [Partners[0].public_name] and [Partners[1].public_name]."
        else:
            ch_Laura "Obviously I realize you are already in. . . a number of other relationships."

        $ Laura.change_face("neutral", blush = 1)

        ch_Laura "I do not care."
        ch_Laura "I want you to be my boyfriend regardless."

        $ Laura.change_face("confused1", blush = 1)

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "Good, then there is no issue."

        $ Laura.change_face("confused1", blush = 1)

        ch_Player "You're really okay with me having multiple girlfriends?"
        ch_Laura "Why wouldn't I be?"
        ch_Laura "It is clear to everyone that you are the most attractive male at the Institute."
        ch_Laura "Is it not expected for a man like you to have many women pursue him at once?"
        ch_Player "No, I. . . wait, 'the most attractive'?"

        $ Laura.change_face("neutral") 

        ch_Laura "Yes, it's obvious."
        ch_Laura "Regardless, you know I don't care."

        $ Laura.change_face("smirk2")

        ch_Laura "I only care that you're {i}mine{/i}." 

        $ Laura.change_face("confused1", mouth = "smirk")

        ch_Laura "As long as you're here when I want and {i}tell me about any additional women you plan on dating{/i}." 
        ch_Player "I can do that."

        python:
            for C in Partners:
                Laura.knows_about.append(C)

        $ Laura.History.update("told_wants_multiple_partners")
    else:
        menu:
            extend ""
            "Tell her you're interested in multiple partners":
                $ Laura.change_face("confused1")

                ch_Player "If we are going to be in a relationship, you should know. . ." 
                ch_Player "I'm interested in having multiple girlfriends. . ." 

                $ Laura.change_face("confused3")

                ch_Laura "Is this a common thing?" 
                ch_Player "Not really. . ." 

                $ Laura.change_face("confused1") 

                ch_Laura "Is this because you're the most attractive male at the Institute and are expecting other women to also want a relationship with you?"
                ch_Player "No, I. . . wait, 'the most attractive'?"

                $ Laura.change_face("neutral") 

                ch_Laura "Yes, it's obvious."
                ch_Player "Wh-"
                ch_Laura "Regardless, I don't care."
                ch_Player "You don't?"
                ch_Laura "No." 

                $ Laura.change_face("smirk2")

                ch_Laura "I only care that you're {i}mine{/i}." 

                $ Laura.change_face("confused1", mouth = "smirk")

                ch_Laura "As long as you're here when I want and {i}tell me who you plan on dating{/i}." 
                ch_Player "I can do that."

                $ Laura.History.update("told_wants_multiple_partners")
            "Never mind.":
                if Rogue.History.check("went_on_date_with_Player") or Jean.History.check("went_on_date_with_Player"):
                    $ Laura.change_face("confused1", blush = 1)

                    ch_Laura "Also, is a man having multiple 'girlfriends' common?"
                    ch_Player "Not really. . . wh-"

                    $ Laura.change_face("neutral")

                    ch_Laura "It must be the fact that you're the most attractive male at the Institute, you are expecting other women to also want a relationship with you."
                    ch_Laura "I have seen you go on dates with other women already." 
                    
                    $ Laura.change_face("confused2")

                    ch_Player "No, I. . ."
                    ch_Player "What?!"
                    ch_Player "How did you know that?"
                    ch_Laura "That you are the most attractive male at the Institute?"

                    $ Laura.change_face("confused1", blush = 1)

                    ch_Laura "It is obvious. . ."
                    ch_Player "No. . . I meant about the other dates." 

                    $ Laura.change_face("confused1", mouth = "smirk", eyes = "squint", blush = 1)

                    ch_Laura "You are {i}very{/i} easy to keep track of."

                    $ Laura.change_face("confused1")

                    ch_Player "Well, to be honest, I am interested in having multiple girlfriends. . ."
                    ch_Player "I-"

                    $ Laura.change_face("neutral")

                    ch_Laura "Fine."
                    ch_Player "Fine?"
                    ch_Laura "Yes, I don't care."

                    $ Laura.change_face("smirk2")

                    ch_Laura "I only care that you're {i}mine{/i}." 

                    $ Laura.change_face("confused1", mouth = "smirk")

                    ch_Laura "As long as you're here when I want and {i}tell me who you plan on dating{/i}." 
                    ch_Player "I can do that."

                    $ Laura.History.update("told_wants_multiple_partners")
                else:
                    pass
    
    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "You are now my 'boyfriend,' right?" 
    ch_Player "Yes, I am." 

    $ Laura.change_face("sexy", eyes = "down", blush = 1)

    ch_Laura ". . ." 

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Take your pants off."

    $ Laura.change_face("confused1", blush = 1)

    ch_Player "What?!"
    ch_Laura "Now that we're boyfriend and girlfriend, I'm allowed to see you naked, no?"

    $ Laura.change_face("sexy", eyes = "down", blush = 1)

    ch_Laura "I've never seen one before. . ."

    $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Laura "Rogue informed me that when you are in a relationship with someone, there are certain things you are. . . allowed to do with them."
    ch_Player "I mean. . . she's not exactly wrong. . ."

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Well, now we are in a relationship. . . and I want to see it. . ." 

    if EventScheduler.Events["ch1_Sentinel_attack"].completed:
        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 
        
        ch_Player "Didn't you see. . . {i}everything{/i}. . . while I was in that coma after the Sentinel attack?" 
        
        $ Laura.change_face("confused3", blush = 1) 
        
        ch_Laura "No. . ." 
        
        $ Laura.change_face("confused1", blush = 1) 
        
        ch_Laura "Like I said previously, I respected your modesty." 
        
        $ Laura.change_face("smirk2", blush = 1) 
        
        ch_Player "Thanks. . ."

    menu:
        extend ""
        "Take your pants off":
            "You remove your pants, exposing yourself to her."

            $ Laura.change_face("surprised1", eyes = "down", mouth = "lipbite", blush = 1)

            ch_Laura "Interesting. . ." 

            $ Laura.change_face("surprised1", eyes = "down", mouth = "lipbite", blush = 2)

            "Her nostrils flare slightly." 
            ch_Laura "Hmmm. . ." 

            $ Laura.change_face("confused1", eyes = "down", mouth = "lipbite", blush = 1)

            ch_Laura "Are they all. . . this large. . . ?"

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "Looking at it makes me feel. . . interesting."
            ch_Laura "Keep your pants off." 

            $ Laura.change_face("kiss2", blush = 2)

            "[Laura.name] proceeds to roughly pull you into a kiss." 
            "Her hand drifts down your torso towards your crotch. . ." 

            $ Laura.change_face("kiss2", blush = 3)

            "She stops herself before going all the way." 
            "[Laura.name] holds the kiss for a few moments, before letting go." 

            $ Laura.change_face("sexy", eyes = "down", blush = 2)

            "She reaches down and picks your underwear off of the floor." 

            $ Laura.change_face("sexy", eyes = "closed", blush = 1)

            "Holding it up to her face, she inhales deeply."

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "This is mine now." 

            $ Laura.change_face("sexy", eyes = "squint", blush = 1)

            ch_Laura ". . . and so are you." 

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "I need to go. . . I'll see you later." 

            $ Laura.change_face("sexy", eyes = "right", blush = 1)

            "She puts your underwear in her pocket and leaves." 

            $ Laura.History.update("seen_Player_naked")
        "Tell her to wait":
            $ Laura.change_face("confused1", blush = 1)

            ch_Player "I think we should wait. . . before stuff like that." 

            $ Laura.change_face("neutral", blush = 1)

            ch_Laura "Fine. Then I'm kissing you." 

            $ Laura.change_face("kiss2", blush = 1)

            "She proceeds to roughly pull you into a kiss." 
            "Holding it for a few moments, before letting go." 

            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "I need to go. . . I'll see you later." 

    $ Laura.History.update("kiss")

    call remove_Characters(Laura) from _call_remove_Characters_105

    $ fade_to_black(0.4)

    "As your relationship develops with [Laura.name], you're finally starting to understand more about her."
    "Her room is currently pretty spartan - if she won't decorate it herself, maybe receiving things from you would change her mind."

    $ fade_in_from_black(0.4)

    $ Partners.append(Laura)

    $ temp = Laura.chat_options[:]

    python:
        for chat_option in temp:
            if "girlfriend" in chat_option:
                Laura.chat_options.remove(chat_option)
                
    $ ongoing_Event = False

    call move_location(Player.location) from _call_move_location_39

    return