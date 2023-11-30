init python:

    def Rogue_boyfriend_trigger_part_one():
        label = "Rogue_boyfriend_trigger_part_one"

        conditions = [
            "QuestPool.Quests['Rogue_dating_Quest'].completed"]

        automatic = True

        return EventClass(label, conditions, automatic = automatic)

label Rogue_boyfriend_trigger_part_one:
    $ Rogue.chat_options.insert(0, f"Ask her to be your girlfriend")

    python:
        for C in Partners:
            if C != Rogue:
                if not C.History.check("told_wants_multiple_partners") or Rogue not in C.knows_about:
                    C.History.update("cheated_on_relationship")

                    if not Player.History.check(f"cheated_on_{C.tag}_with_Rogue_relationship", tracker = "recent"):
                        Player.History.update(f"cheated_on_{C.tag}_with_Rogue_relationship")

    return

init python:

    def Rogue_boyfriend_trigger_part_two():
        label = "Rogue_boyfriend_trigger_part_two"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_boyfriend_trigger_part_two:
    $ ongoing_Event = True

    if Rogue.location == Player.location and Player.location != Player.home:
        $ Rogue.change_face("confused1", mouth = "smirk") 
        
        ch_Player "Hey, [Rogue.name]. Can we talk in my room?" 
        ch_Rogue "Sure, hon'."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_182
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_200
        call send_Characters(Rogue, "bg_hallway", behavior = False) from _call_send_Characters_161

        "You open your door and let [Rogue.name] inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_183
        call set_the_scene(location = Player.home) from _call_set_the_scene_201
    elif Rogue.location != Player.location:
        if current_phone_screen == "text":
            call send_text(Rogue, "mind meeting me in my room?") from _call_send_text_36
            call send_text(Rogue, "I wanna talk about something") from _call_send_text_37
            call receive_text(Rogue, "Sure! Omw :))") from _call_receive_text_487
        elif current_phone_screen == "call":
            ch_Player "Hey, [Rogue.name]. Can we talk in my room?"
            ch_Rogue "Sure, hon'!"
            ch_Rogue "I'm on my way."

        pause

        hide screen phone_screen

        call remove_Characters(location = Player.home) from _call_remove_Characters_184
        call set_the_scene(location = Player.home) from _call_set_the_scene_202

        pause 1.0

        call knock_on_door(times = 1) from _call_knock_on_door_21

        "It feels like you're only waiting for mere seconds before you hear a knock on the door."
        "You open it and let [Rogue.name] in."

    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_162

    $ Rogue.change_face("worried1", mouth = "lipbite", blush  = 1)

    ch_Rogue "Ah think ah know what this is about. . ." 

    $ Rogue.History.update("Player_initiated_relationship_talk")

    $ EventScheduler.Events["Rogue_boyfriend"].start()

    $ ongoing_Event = False

    return

init python:

    def Rogue_boyfriend_alternate_trigger():
        label = "Rogue_boyfriend_alternate_trigger"

        conditions = [
            "not EventScheduler.Events['Rogue_boyfriend'].completed",

            "day - EventScheduler.Events['Rogue_boyfriend_trigger_part_one'].completed_when >= 4",
            
            "Player.location in public_locations and Rogue.location not in ['hold', Player.location]",

            "Rogue.is_in_normal_mood()"]

        waiting = True

        priority = 1

        return EventClass(label, conditions, waiting = waiting, priority = priority)

label Rogue_boyfriend_alternate_trigger:
    $ ongoing_Event = True

    call send_Characters(Rogue, Player.location, greetings = True, behavior = False) from _call_send_Characters_163

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Hey, [Rogue.Player_petname]. . ."
    ch_Rogue "Can we talk in private?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Of course. Your room or mine?"
    ch_Rogue "Yours is fine." 

    if Player.location != "bg_hallway":
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_185
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_203
        call send_Characters(Rogue, location = "bg_hallway", behavior = False) from _call_send_Characters_264
        
        "She follows you to your room."
        
    "You open your door and let [Rogue.name] inside."

    call remove_Characters(location = Player.home) from _call_remove_Characters_186
    call set_the_scene(location = Player.home) from _call_set_the_scene_204
    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_265

    $ Rogue.change_face("worried1", mouth = "lipbite", blush  = 1)

    ch_Rogue "Ah have a feelin' you might know what this is about. . ." 

    menu:
        extend ""
        "Progress your relationship with [Rogue.name]":
            pass
        "Postpone relationship talk":
            $ Rogue.change_face("surprised2", blush = 3)

            ch_Player "Uh. . . this is actually a pretty bad time, [Rogue.name]."

            $ Rogue.change_face("worried1", eyes = "right", blush = 1)

            pause 1.0

            $ Rogue.change_face("worried1", blush = 2)

            pause 1.0

            ch_Rogue "Oh! Sorry hon'. Ah'll. . . we can talk later!"

            call remove_Characters(Rogue) from _call_remove_Characters_187

            ch_Player "Everything o-"
            "She's out the door in a jiff, and you hear quick footsteps leaving your hallway."

            $ Rogue.wants_alone_time = 2

            return

    $ EventScheduler.Events["Rogue_boyfriend"].start()

    $ ongoing_Event = False

    return

init python:

    def Rogue_boyfriend():
        label = "Rogue_boyfriend"

        conditions = [
            "False"]

        priority = 1

        return EventClass(label, conditions, priority = priority)

label Rogue_boyfriend:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk", blush  = 1) 
    
    if Rogue.History.check("Player_initiated_relationship_talk"):
        ch_Player "You do?" 
    else:
        ch_Player "I do?" 

    ch_Rogue "Well, at least ah think so."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue ". . ." 

    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "It's about 'us'. . . ain't it?" 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush  = 1)

    if Rogue.History.check("Player_initiated_relationship_talk"):
        ch_Player "You're not wrong. . ."
    else:
        ch_Player "'Us'?"

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah reckon yer aware. . . just how much ah like you. . ."
    ch_Player "I re. . ."

    $ Rogue.change_face("worried3", blush = 1)

    "As soon as you open your mouth, she talks over you."
    ch_Rogue "And it ain't cause yer the only person ah can touch or nothin'!"

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "Even if we weren't mutants, ah know for sure we'd still be right for each other." 

    $ Rogue.change_face("worried3", blush = 1)

    ch_Player "Wha. . ."
    "Every time you try to speak, you can almost see her anxiety increase, as she gets more frantic."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush  = 1)

    ch_Rogue "Ah think ya really like me too. . . you've never tried anythin' untoward. . ."

    if EventScheduler.Events["ch1_Juggernaut_attack"].completed:
        ch_Rogue "Not to mention what ya did for me when ah got hurt. . ."

    menu:
        extend ""
        "It's true, [Rogue.name], I really do like you. And I care about you very much.":
            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_611 
            call change_Companion_stat(Rogue, "trust", 0) from _call_change_Companion_stat_612
        "Of course I like you, [Rogue.name]. How couldn't I?":
            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_613
        "You really need to relax. Why would I continuously go on dates with you if I didn't like you?":
            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_614 
            call change_Companion_stat(Rogue, "trust", 0) from _call_change_Companion_stat_615

    $ Rogue.change_face("worried3", blush  = 1)

    if Rogue.History.check("Player_initiated_relationship_talk"):
        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush  = 1)

        ch_Rogue "Ah was just. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush  = 2)

        ch_Rogue "Ah wanted to know. . ."

        $ Rogue.change_face("worried2", mouth = "lipbite", blush  = 2)

        ch_Rogue "If you'd let me be yer girlfriend. . ." 
    else:
        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush  = 1)

        ch_Rogue "We've gone on a few dates. . ."

        $ Rogue.change_face("worried1", eyes = "right", blush  = 1)

        ch_Rogue "And. . . kissed. . ." 

        $ Rogue.change_face("worried2", blush  = 1)

        ch_Rogue "But. . ." 

        $ Rogue.change_face("worried1", eyes = "right", blush  = 1)

        ch_Rogue "Well, It's been a while now. . ."

        $ Rogue.change_face("sad", eyes = "right", blush  = 1)

        ch_Rogue "Ah get it if ya don't want to take things further. . . with me. . ." 

    if len(Partners) > 0:
        $ Rogue.change_face("worried1", eyes = "right", blush  = 2)

        if len(Partners) == 1:
            ch_Rogue "Ah know yer already datin' [Partners[0].public_name], so ah reckon it was a long shot anyways. . ."
        elif len(Partners) == 2:
            ch_Rogue "Ah know yer already datin' [Partners[0].public_name] and [Partners[1].public_name], so ah reckon it was a long shot anyways. . ."
        else:
            ch_Rogue "Ah know yer already datin'. . . a few others, so ah reckon it was a long shot anyways. . ."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Player "[Rogue.name], take a deep breath." 

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "Don't worry. . . I do want to take things further." 

    if len(Partners) > 0:
        $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

        ch_Rogue "Ah saw this comin'."
        ch_Rogue "It ain't no secret that yer a real hot commodity 'round here."

        $ Rogue.change_face("confused1", eyes = "right")

        ch_Player "'Hot commodity'?"
        ch_Rogue "Ya don't have to pretend 'round me, [Rogue.Player_petname]."
        ch_Player "Wha-"

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Ah knew there was gonna be a ton of competition for ya."
        ch_Rogue "You gettin' a girlfriend or two. . . or three. . . was only a matter of time."
        ch_Rogue "Ah'm fine with it as long as ah get a piece of ya too. . ."

        $ Rogue.change_face("worried1", eyes = "right")

        ch_Rogue "But, ah'd really appreciate it if you could tell me who you plan on datin', before you go after 'em."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Player "Of course."

        python:
            for C in Partners:
                Rogue.knows_about.append(C)

        $ Rogue.History.update("told_wants_multiple_partners")
    else:
        menu:
            "Tell her you're interested in multiple partners":
                ch_Player "But, you should know. . ." 

                $ Rogue.change_face("confused2")

                ch_Player "I'm interested in having multiple girlfriends. . ."

                $ Rogue.change_face("worried1")

                ch_Rogue "So. . . ya wanna date other girls, while also bein' with me?" 

                $ Rogue.change_face("worried1", eyes = "right")

                ch_Player "Yeah. . ."

                if Laura.History.check("went_on_date_with_Player"):
                    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

                    ch_Rogue "Ah guess ah already knew that. . ."
                    ch_Player "You did?"

                    $ Rogue.change_face("confused1", mouth = "smirk")

                    ch_Rogue "Well yeah. . ."
                    ch_Rogue "Ya did tell [Laura.name] to talk to me about girl stuff after all." 

                    $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk")

                    ch_Rogue "She talks about you a LOT."
                    ch_Rogue "More than anythin' else, ah reckon. . ."

                    $ Rogue.change_face("confused1", eyes = "squint", mouth = "smirk", blush = 1)

                    ch_Rogue "Specifically 'bout how much she liked kissin' you. . ."
                    ch_Player "Oh, yeah, that's right. . ."

                    $ Rogue.change_face("worried1")

                    ch_Player "So, you don't mind if I date her. . . as well as other people, potentially?" 

                    $ Rogue.change_face("worried1", mouth = "smirk")

                    ch_Rogue "Ah don't. . ."
                else:
                    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

                    ch_Rogue "Ah guess ah don't really mind. . ." 

                    $ Rogue.change_face("worried1", mouth = "smirk")

                    ch_Player "You don't?"
                    ch_Rogue "Ah don't."

                $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

                ch_Rogue "Ah saw this comin' anyway."
                ch_Rogue "It ain't no secret that yer a real hot commodity 'round here."

                $ Rogue.change_face("confused1", eyes = "right")

                ch_Player "'Hot commodity'?"
                ch_Rogue "Ya don't have to pretend 'round me, [Rogue.Player_petname]."
                ch_Player "Wha-"

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Rogue "You can have all the girlfriends ya want, so long as ya don't forget about me."

                $ Rogue.change_face("worried1", eyes = "right")

                ch_Rogue "But, ah'd really appreciate it if you could tell me who you plan on datin' before you go after 'em."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Player "Of course."

                $ Rogue.History.update("told_wants_multiple_partners")
            "Don't say anything":
                pass
        
    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "Well, I'd love to start a relationship with you."
    ch_Rogue "So. . . ah'm your girlfriend now?"

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Player "Yep!" 
    ch_Rogue "Am ah. . . allowed to kiss you now. . . ?"

    menu:
        extend ""
        "If you say please. (encourage_quirk)":
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
            
            call change_Companion_stat(Rogue, "desire", 0) from _call_change_Companion_stat_616

            ch_Rogue "Ah promise ah will, from now on." 

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

            ch_Rogue "Can ah have a kiss, please?" 

            call change_Companion_stat(Rogue, "love", 0) from _call_change_Companion_stat_617

            $ Rogue.change_face("kiss1", blush = 1)

            "You pull [Rogue.name] into a gentle kiss, running your hand through her hair."

            $ Rogue.change_face("kiss2", blush = 1)

            "She takes your other hand and starts moving it under her shirt. . ."

            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

            "She stops herself before going too far." 

            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

            ch_Rogue "Sorry, ah got a bit carried away. . ."
            ch_Rogue "Don't know if ah'm ready to go that far yet."

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

            ch_Rogue "Thank you for lettin' me have a kiss. . ." 
            ch_Rogue "But, ah gotta go, ah'll see you later. . ."
        "You're my girlfriend now, you don't have to keep asking for permission. (discourage_quirk)":
            $ Rogue.change_face("worried1", blush = 1)

            ch_Rogue "Oh alright, hon'."

            $ Rogue.change_face("kiss1", blush = 1)

            "You pull [Rogue.name] into a gentle kiss, running your hand through her hair." 

            $ Rogue.change_face("kiss2", blush = 1)

            "She squeezes you tight and, after a long moment, you let go."

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

            ch_Rogue "Ah hope we can do that a lot more. . ."
            ch_Rogue "But, for now, ah gotta go."
            ch_Rogue "Ah'll see you later. . ." 

    $ Rogue.History.update("kiss")

    call remove_Characters(Rogue) from _call_remove_Characters_188

    $ Partners.append(Rogue)

    $ temp = Rogue.chat_options[:]

    python:
        for chat_option in temp:
            if "girlfriend" in chat_option:
                Rogue.chat_options.remove(chat_option)

    $ Rogue.chat_options.insert(0, f"Ask why her room isn't decorated")
                
    $ ongoing_Event = False

    call move_location(Player.location) from _call_move_location_41

    return