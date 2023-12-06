init python:

    def Jean_boyfriend_trigger_part_one():
        label = "Jean_boyfriend_trigger_part_one"

        conditions = [
            "QuestPool.Quests['Jean_dating_Quest'].completed"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Jean_boyfriend_trigger_part_one:
    $ Jean.chat_options.insert(0, f"Ask her to be your girlfriend")

    python:
        for C in Partners:
            if C != Jean:
                if not C.History.check("told_wants_multiple_partners") or Jean not in C.knows_about:
                    C.History.update("cheated_on_relationship")

                    if not Player.History.check(f"cheated_on_{C.tag}_with_Jean_relationship", tracker = "recent"):
                        Player.History.update(f"cheated_on_{C.tag}_with_Jean_relationship")

    return

init python:

    def Jean_boyfriend_trigger_part_two():
        label = "Jean_boyfriend_trigger_part_two"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_boyfriend_trigger_part_two:
    $ ongoing_Event = True

    if Jean.location == Player.location and Player.location != Player.home:
        $ Jean.change_face("confused1") 
        
        ch_Player "Hey, [Jean.petname]. Can we talk in my room?"
        ch_Jean "Okayyy."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_37
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_44
        call send_Characters(Jean, "bg_hallway", behavior = False) from _call_send_Characters_48

        "You open your door, and [Jean.name] follows you inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_38
        call set_the_scene(location = Player.home) from _call_set_the_scene_45
    elif Jean.location != Player.location:
        if current_phone_screen == "text":
            call send_text(Jean, "can you meet me in my room?") from _call_send_text_4
            call send_text(Jean, "I want to talk about something") from _call_send_text_5
            call receive_text(Jean, "Sure!") from _call_receive_text_47
            call receive_text(Jean, "Omw <3") from _call_receive_text_48
        elif current_phone_screen == "call":
            ch_Player "Hey, [Jean.petname]. Can we talk in my room?"
            ch_Jean "Sure!"
            ch_Jean "On my way."

        pause

        hide screen phone_screen

        call remove_Characters(location = Player.home) from _call_remove_Characters_39
        call set_the_scene(location = Player.home) from _call_set_the_scene_46

        pause 1.0

        call knock_on_door(times = 1) from _call_knock_on_door

        "You wait a couple minutes before there's a knock at the door."
        "You open it, and [Jean.name] steps in."

    call send_Characters(Jean, Player.home, behavior = False) from _call_send_Characters_49

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean "Before we get to your thing, there's something I want to talk about. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    $ EventScheduler.Events["Jean_boyfriend"].start()

    $ ongoing_Event = False

    return

init python:

    def Jean_boyfriend_alternate_trigger():
        label = "Jean_boyfriend_alternate_trigger"

        conditions = [
            "not EventScheduler.Events['Jean_boyfriend'].completed",

            "day - EventScheduler.Events['Jean_boyfriend_trigger_part_one'].completed_when >= 4",
            
            "Player.location in public_locations and Jean.location not in ['hold', Player.location]",

            "Jean.is_in_normal_mood()"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Jean_boyfriend_alternate_trigger:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location, behavior = False) from _call_send_Characters_50

    $ Jean.change_face("happy", blush = 1)

    ch_Jean "Heyy, [Jean.Player_petname]."

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "Come with me, we're gonna have a chat."

    $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "left", blush = 1)

    ch_Player "Whe. . ."

    if Player.location != "bg_hallway":
        "She doesn't let you respond and just grabs your hand, leading you to your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_40
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_47
        call send_Characters(Jean, location = "bg_hallway", behavior = False) from _call_send_Characters_229
        
        $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Gonna let me in, [Jean.Player_petname]?"
    "You unlock the door and hold it open for her to enter."

    call remove_Characters(location = Player.home) from _call_remove_Characters_41
    call set_the_scene(location = Player.home) from _call_set_the_scene_48
    call send_Characters(Jean, location = Player.home, behavior = False) from _call_send_Characters_230

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean "There's something we need to talk about. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    menu:
        extend ""
        "Progress your relationship with [Jean.name]":
            pass
        "Postpone relationship talk":
            $ Jean.change_face("surprised2", blush = 3)

            ch_Player "Uh. . . this is actually a pretty bad time, [Jean.name]."

            $ Jean.change_face("worried1", eyes = "right", blush = 1)

            pause 1.0

            $ Jean.change_face("worried1", blush = 2)

            pause 1.0

            ch_Jean "Yeah, okay! No problem."

            call remove_Characters(Jean) from _call_remove_Characters_42

            ch_Player "Oka-"
            "She's already out the door."

            $ Jean.wants_alone_time = 2

            return

    $ EventScheduler.Events["Jean_boyfriend"].start()

    $ ongoing_Event = False

    return

init python:

    def Jean_boyfriend():
        label = "Jean_boyfriend"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_boyfriend:
    $ ongoing_Event = True

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        $ Jean.change_face("neutral", mouth = "lipbite", blush = 1)

        ch_Player "What's th. . ."
        ch_Jean "Shush, let me say my peace first."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "You can speak when I'm done."
        ch_Jean ". . ."

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Jean "Now. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "We've been spending a lot more time together lately."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "And I've really enjoyed getting to know you. . . I think we get along pretty great."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "I'm sure you'd agree."

        menu:
            extend ""
            "Give her a small nod":
                $ Jean.change_face("sly", blush = 1)

                ch_Jean "Good. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_89 
                call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_90
            "I do. . .":
                $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

                ch_Jean "I didn't say you could talk yet. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_91
            "Yeah. . . but what are you getting at?":
                $ Jean.change_face("worried1", blush = 1)

                ch_Jean "You're not supposed to talk yet. . ."
                
        $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        ch_Jean "And I'm sure you think I'm pretty, right?"

        menu:
            extend ""
            "Nod in affirmation":
                $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

                ch_Jean "I can tell. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_92
                call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_93
            "You are drop dead gorgeous.":
                $ Jean.change_face("worried2", mouth = "smirk", blush = 2)

                pause 1.0

                $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 
                
                ch_Jean "Well. . . I, uh. . . thanks. . ."
                
                $ Jean.change_face("confused1", mouth = "smirk", blush = 1) 
                
                ch_Jean "But I didn't say you could speak yet. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_94
            "Yeah, not too bad. . .":
                $ Jean.change_face("confused2", blush = 2)
                
                pause 1.0
                
                $ Jean.change_face("worried1", eyes = "right", blush = 1) 
                
                ch_Jean "I still didn't say you could speak yet. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_95

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Jean "And, you're. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Jean "I mean you're handsome, fit. . ."

        $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        ch_Jean "Heh, {i}almost{/i} as smart as me."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "I made you my 'little sib' for a reason. . ."

        $ Jean.change_face("worried1", eyes = "right", blush = 1)

        ch_Jean "But I can tell you really do care about me, more than all that superficial stuff. . ."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "You've been trying super hard to help me figure out my issues."

        $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        ch_Player "Of c. . ."
        ch_Jean "Shhhh."

        $ Jean.change_face("neutral", blush = 1)

        pause 1.0

        $ Jean.change_face("worried1", eyes = "right", blush = 1)

        ch_Jean ". . . thanks."

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "I just {i}really{/i} appreciate it."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "Not to mention, you're the first person I've ever even considered skipping a study session to hang out with."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "And I want to spend even more time with you."

        $ Jean.change_face("worried1", eyes = "right", blush = 2)

        ch_Jean "That's why. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "I want you to be my boyfriend."

        if len(Partners) > 0:
            $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

            ch_Jean "And. . . I know you already have a girlfriend. . ."
    
            if len(Partners) > 2:
                ch_Jean ". . . or a few."
            elif len(Partners) == 2:
                ch_Jean ". . . or two."

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "So I get it's a stretch, but I just couldn't live with myself if I didn't put this all out there, and ask anyway."

        ". . ."
        ch_Jean "You can speak now. . ."
    else:
        $ Jean.change_face("neutral", mouth = "lipbite", blush = 1)

        ch_Player "What's that?"

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Jean "Wellll. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "You enjoy hanging out with me, right?"

        menu:
            extend ""
            "It's always a good time, yeah.":
                $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

                ch_Jean "I'm glad you agree."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_96
            "I do. I really, really do.":
                $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

                pause 1.0

                $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
                
                ch_Jean "Good. . . I enjoy it too. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_97 
                call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_98
            "It's not the worst time. . .":
                $ Jean.change_face("confused1", blush = 1) 

                pause 1.0

                $ Jean.change_face("worried1", eyes = "right", blush = 1) 
                
                ch_Jean "Well, I really enjoy it. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_99

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "I think you'd agree we get along pretty great. . . right?"

        menu:
            extend ""
            "I'd say so.":
                $ Jean.change_face("worried1", mouth = "smirk", blush = 1)
            "Of course. Hard not to with someone like you. . .":
                $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_100 
                call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_101
            "Pretty well. . . I guess. . .":
                $ Jean.change_face("worried1", eyes = "right", blush = 1) 
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_102

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "And you think I'm. . . pretty, right?"

        menu:
            extend ""
            "Absolutely.":
                $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

                ch_Jean "I can tell. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_103
            "You are drop dead gorgeous.":
                $ Jean.change_face("worried2", mouth = "smirk", blush = 2)

                pause 1.0

                $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 
                
                ch_Jean "Well. . . I, uh. . . thanks. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_104 
                call change_Character_stat(Jean, "desire", 0) from _call_change_Character_stat_105
            "Yeah, not too bad. . .":
                $ Jean.change_face("confused2", blush = 2)

                pause 1.0

                $ Jean.change_face("worried1", eyes = "right", blush = 1) 
                
                ch_Jean "Oh. . ."
                
                call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_106

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "Well, you're. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "Handsome, fit. . ."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "Just about as smart."

        $ Jean.change_face("smirk2", blush = 1)

        ch_Jean "But I know you don't care too much about the superficial stuff."

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "You helped me out so much with my power issues. . ."

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "I want you to know I {i}really{/i} appreciate it."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "And. . . I'll admit."
        ch_Jean "You're also the first guy I've ever even considered skipping a study session to hang out with."

        $ Jean.change_face("worried1", eyes = "right", blush = 1)

        ch_Jean "I'd. . ."

        $ Jean.change_face("worried1", blush = 1)

        ch_Jean "I want you to be my boyfriend."
        
        if len(Partners) > 0:
            $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

            ch_Jean "And. . . I know you already have a girlfriend. . ."
    
            if len(Partners) > 2:
                ch_Jean ". . . or a few."
            elif len(Partners) == 2:
                ch_Jean ". . . or two."

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "So I get it's a stretch, but I just couldn't live with myself if I didn't put this all out there, and ask anyway."

    $ Jean.change_face("happy", blush = 1)

    ch_Player "I really would like to be. . ."

    if len(Partners) > 0:
        $ Jean.change_face("happy")

        ch_Jean "You would?!"

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Player "Definitely."

        $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

        ch_Jean "Well, good."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "I mean it's really not all that surprising you'd end up with more than one girlfriend."
        ch_Player "It's not?"

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        ch_Jean "Like. . . just look at you. . ."

        $ Jean.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

        ch_Jean "It makes sense."

        $ Jean.change_face("worried1", eyes = "right", mouth = "smirk")

        ch_Jean "But, you better at least tell me before you try dating any additional girls."
        ch_Player "I can do that."

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "I won't have anyone playing with my man's heart. . ."

        $ Jean.change_face("sly")

        ch_Jean "And all these other girlfriends better not hog all of your attention."

        python:
            for C in Partners:
                Jean.knows_about.append(C)

        $ Jean.History.update("told_wants_multiple_partners")
    else:
        menu:
            "Tell her you're interested in multiple partners":
                $ Jean.change_face("perplexed")
                
                ch_Player "But. . ."
                ch_Player "If we are going to be in a relationship, you should know. . ."

                $ Jean.change_face("appalled3")

                ch_Player "I'm interested in having multiple girlfriends. . ."
                ch_Jean "You're interested in what?!"
                ch_Player ". . ."

                $ Jean.change_face("appalled2")

                ch_Player "In having multiple girlfriends. . ."

                $ Jean.change_face("suspicious2")

                ch_Player "I just wanted to make sure you knew. . . before we got more involved. . ."

                $ Jean.change_face("suspicious2", eyes = "right")

                ch_Jean "I guess it makes sense. . ."

                $ Jean.change_face("confused1", eyes = "squint")

                ch_Jean "I mean, look at you. . ."

                $ Jean.change_face("confused1", eyes = "down")

                pause 1.0

                $ Jean.change_face("suspicious1")

                ch_Jean "Hmm. . ."

                $ Jean.change_face("neutral")

                ch_Jean "Fine, I'll let you have your fun. . ."
                ch_Player "Fine?"

                $ Jean.change_face("confused1")

                ch_Jean "But only under a few conditions."

                $ Jean.change_face("suspicious1")

                ch_Jean "As long as your. . . 'other girls' know I'm the main one. . ."

                $ Jean.change_face("worried2")

                ch_Player "[Jean.name], I'm not just talking about having casual relationships with other girls. . ."
                ch_Player "I mean to take my relationships with them as seriously as I do with ours."

                $ Jean.change_face("worried1", eyes = "right")

                ch_Jean "Oh. . ."

                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Jean "Well, you better at least tell me before you try dating another girl."
                ch_Player "I can do that."

                $ Jean.change_face("confused1", mouth = "smirk")

                ch_Jean "I won't have anyone playing with my man's heart. . ."

                $ Jean.change_face("sly")

                ch_Jean "And they better not hog all of your attention."

                $ Jean.History.update("told_wants_multiple_partners")
            "Don't say anything":
                pass

    menu:
        extend ""
        "Encourage the sib dynamic (encourage_quirk)":
            $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

            ch_Player "You'll still be my big sibling. . . right?"

            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
            
            ch_Jean "Of course. . ."
        "Discourage the sib dynamic (discourage_quirk)":
            $ Jean.change_face("worried1")

            ch_Player "We should probably. . . drop the whole big/little sib' thing. . . right?"

            $ Jean.change_face("worried1", eyes = "right") 
            
            ch_Jean "If that's what you want. . ."

    $ Jean.change_face("sexy")

    ch_Jean "Now. . ."
    ch_Jean "I bet you really want to kiss me right now."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Maybe if you say please. . ."

    menu:
        extend ""
        "Go along with it (encourage_quirk)":
            ch_Player "Please."

            $ Jean.change_face("kiss2", blush = 1)

            "Without any warning, she grabs you and pulls you into a kiss."

            $ Jean.change_face("kiss1", blush = 2)

            "Her hand slowly drifts down to your ass, where it stays."
            "After a moment, she pulls away."

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "I can't wait to kiss you many more times. . ."

            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

            ch_Jean "As long as you say please. . ."

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "Now, I gotta go."

            $ Jean.change_face("smirk2", blush = 1)

            ch_Jean "See you later!"
        "Push back (discourage_quirk)":
            ch_Player "Oh come on, you're my girlfriend now."

            $ Jean.change_face("worried2")

            pause 1.0

            $ Jean.change_face("angry1", eyes = "right")

            ch_Jean "Ugh, fine."

            $ Jean.change_face("kiss2", blush = 1)

            "Without any warning, she grabs you and pulls you into a kiss."

            $ Jean.change_face("kiss2", blush = 2)

            "After a moment, she pulls away."

            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "I can't wait to kiss you many more times. . ."

            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "But I gotta go."

            $ Jean.change_face("smirk2", blush = 1)

            ch_Jean "See you later!"

    $ Jean.History.update("kiss")

    call remove_Characters(Jean) from _call_remove_Characters_43

    $ Partners.append(Jean)

    $ temp = Jean.chat_options[:]

    python:
        for chat_option in temp:
            if "girlfriend" in chat_option:
                Jean.chat_options.remove(chat_option)

    $ Jean.chat_options.insert(0, f"Ask why her room isn't decorated")
                
    $ ongoing_Event = False

    call move_location(Player.location) from _call_move_location_36

    return