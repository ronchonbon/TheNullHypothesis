init python:

    def Laura_jealousy_went_on_date():
        label = "Laura_jealousy_went_on_date"

        conditions = [
            "Laura in Partners",
            "not Laura.History.check('told_wants_multiple_girlfriends')",
            "not EventScheduler.Events['Laura_jealousy_flirted'].completed",
            "Laura.History.check('cheated_on_date') or Laura.History.check('cheated_on_relationship')",
            "Laura.location != Player.location"]
            
        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Laura_jealousy_went_on_date:
    $ ongoing_Event = True
    
    call start_new_day from _call_start_new_day_3

    if Player.location == Player.home:
        call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_12

        "You're awoken by harsh knocking on your door."

        if Present:
            $ temp = Present[0].name

            call remove_Characters(fade = False) from _call_remove_Characters_118

            $ fade_in_from_black(0.4)

            "It also looks like [temp] is already gone. . . that's odd."

        if black_screen:
            $ fade_in_from_black(0.4)

        ch_Player "Hold on! I'll be there in a minute."

        call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_13

        "The knocking continues."
        "You get out of bed and put some clothes on, before opening the door."
    else:
        call receive_text(Laura, "Your room, now.") from _call_receive_text_705

        "Your phone buzzing from a text wakes you up."

        call open_texts(Laura) from _call_open_texts_23
        call receive_text(Laura, "NOW") from _call_receive_text_706

        pause

        hide screen phone_screen

        if Present:
            $ Present[0].change_face("confused2")

            ch_Player "Shit, sorry [Present[0].name]. I gotta go take care of something."

            $ Present[0].change_face("confused1")

        "You quickly get dressed and head to your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_119
        call send_Characters(Laura, "bg_hallway", behavior = False) from _call_send_Characters_14
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_333

        $ Laura.change_face("appalled1")

        ch_Laura "Open."
        "You open the door, and she shoves you inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_147
        call set_the_scene(location = Player.home) from _call_set_the_scene_334

    call send_Characters(Laura, location = Player.home, behavior = False) from _call_send_Characters_259

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Characters:
            if Player.History.check(f"cheated_on_Laura_with_{C.tag}_date") and Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_date") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_date")

            if Player.History.check(f"cheated_on_Laura_with_{C.tag}_relationship") and Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_relationship") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_relationship")

    if cheating_Character == Rogue:
        $ cheating_Character = "Rogue"
    elif cheating_Character == Jean:
        $ cheating_Character = "Jean"

    $ Laura.change_face("suspicious2")

    ch_Laura "You went on a date with [cheating_Character]."

    $ Laura.change_face("suspicious1")

    ch_Player "How. . ."
    ch_Laura "Are you denying it?" 

    $ Laura.change_face("angry1")

    ch_Player "No. . ."

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "Is it common for a man to date other women while already having a girlfriend?"

    $ Laura.change_face("furious")

    ch_Laura "Is there something I'm missing?"

    $ Laura.change_face("angry2")

    ch_Player "Not necessarily. . ." 

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "Is this because you're the most attractive male at the Institute and are expecting other women to also want a relationship with you?"
    ch_Player "Wh-"

    $ Laura.change_face("furious")

    ch_Laura "Am I just overreacting?"
    
    $ Laura.change_face("appalled2", mouth = "frown")

    ch_Laura "Do 'normal' people not see this as a breach of trust?!"
    ch_Player "I. . ." 

    $ Laura.change_face("furious", eyes = "right", blush = 1)

    ". . ."

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "{i}Grrrrrr{/i}. . ."
    "She just growls at you before storming out of the room. . ."

    call remove_Characters(Laura) from _call_remove_Characters_240

    $ Laura.give_status("mad")

    "*SLAM*"
    ". . . and slamming the door on the way out."

    call change_Girl_stat(Laura, "trust", -30) from _call_change_Girl_stat_940

    ". . ."
    ch_Player "Well shit. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_36

    "This time, you hear a more civilized knocking at the door."
    "You go over and open it."

    call send_Characters(Kurt, Player.home) from _call_send_Characters_15

    $ Kurt.change_face("surprised")

    ch_Kurt "Bruder. . ."
    ch_Kurt "Is everysing okay?"
    ch_Kurt "You could hear zee yelling from across campus. . ."

    $ Kurt.change_face("confused")

    ch_Player "Not really."
    ch_Player "I pissed [Laura.name] off."

    $ Kurt.change_face("neutral")

    ch_Kurt "Is she not alvays pissed off?"
    ch_Player "Not like this, I really screwed up."

    $ Kurt.change_face("confused")

    "You explain what happened." 

    $ Kurt.change_face("angry")

    ch_Kurt "Schön blöd, vat zee hell is wrong with you?"

    $ Kurt.change_face("confused")

    ch_Kurt "You know better than anyone she has trust issues."
    ch_Kurt "She has every right to be angry."

    $ Kurt.change_face("neutral")

    ch_Player "I know. . ."
    ch_Kurt "I vould stay clear of her for a few days."
    ch_Kurt "She's liable to claw your eyes out if you don't let her calm down first."

    $ Kurt.change_face("confused")

    pause 1.0

    $ Kurt.change_face("sad")

    ch_Kurt ". . . I'm disappointed in you, man."
    "He leaves without another word."

    call remove_Characters(Kurt) from _call_remove_Characters_241

    $ ongoing_Event = False

    return

init python:

    def Laura_jealousy_flirted():
        label = "Laura_jealousy_flirted"

        conditions = [
            "Laura in Partners",
            "not Laura.History.check('told_wants_multiple_girlfriends')",
            "not EventScheduler.Events['Laura_jealousy_went_on_date'].completed",
            "Laura.History.check('cheated_on_flirting_in_public') >= 3 and Laura.History.permanent['cheated_on_flirting_in_public'][-3] > EventScheduler.Events['Laura_boyfriend'].completed",
            "Laura.location != Player.location",
            "Player.location in public_locations"]
            
        flirting = True

        priority = 99

        return EventClass(label, conditions, flirting = flirting, priority = priority)

label Laura_jealousy_flirted:
    $ ongoing_Event = True

    hide screen interactions_screen
    hide screen phone_screen

    call send_Characters(Laura, Player.location, behavior = False) from _call_send_Characters_70

    $ Laura.change_face("appalled1")

    "[Laura.name] appears out of nowhere, looking pissed."
    ch_Player "He. . ."

    $ Laura.change_face("furious", eyes = "left")

    if Player.temp in all_Characters and Player.temp != Laura:
        $ Player.temp.face("confused1")

    "She just grabs your arm and drags you to her room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_242
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_335
    call send_Characters(Laura, location = "bg_girls_hallway", behavior = False) from _call_send_Characters_260

    "[Laura.name] unlocks the door and shoves you inside."

    call remove_Characters(location = Laura.home) from _call_remove_Characters_243
    call set_the_scene(location = Laura.home) from _call_set_the_scene_336
    call send_Characters(Laura, location = Laura.home, behavior = False) from _call_send_Characters_261

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Characters:
            if Player.History.check(f"cheated_on_Laura_with_{C.tag}_flirting_in_public") and Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_flirting_in_public") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_flirting_in_public")

    if cheating_Character == Rogue:
        $ cheating_Character = "Rogue"
    elif cheating_Character == Jean:
        $ cheating_Character = "Jean"

    ch_Laura "You were flirting with [cheating_Character]."

    $ Laura.change_face("angry2")

    ch_Player "I. . ." 
    ch_Laura "Are you going to deny it too?"
    ch_Player "No. . ."

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "Is it common for a man to flirt with other women while already having a girlfriend?"

    $ Laura.change_face("furious")

    ch_Laura "Is there something I'm missing?"

    $ Laura.change_face("angry2")

    ch_Player "Not necessarily. . ." 

    $ Laura.change_face("confused1", eyes = "squint")

    ch_Laura "Did you think I wouldn't know?"
    ch_Laura "Is this because you're the most attractive male at the Institute and are expecting other women to also want a relationship with you?"
    ch_Player "Wh-"

    $ Laura.change_face("furious")

    ch_Laura "Am I just overreacting?"

    $ Laura.change_face("appalled2", mouth = "frown")

    ch_Laura "Do 'normal' people not see this as a breach of trust?!"
    ch_Player "I. . ." 

    $ Laura.change_face("furious", eyes = "right", blush = 1)

    ". . ."

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "{i}Grrrrrr{/i}. . ."
    "She just growls at you before shoving you out of the room."

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_337

    $ Laura.give_status("mad")

    "*SLAM*"
    ". . . and slamming the door behind you."

    call change_Girl_stat(Laura, "trust", -30) from _call_change_Girl_stat_941

    ". . ."
    ch_Player "Well shit. . ."

    call send_Characters(Kurt, Player.location) from _call_send_Characters_71

    $ Kurt.change_face("surprised")

    ch_Kurt "Bruder. . ."
    ch_Kurt "Is everysing okay?"
    ch_Kurt "I saw her dragging you across campus. . ."
    
    $ Kurt.change_face("confused")

    ch_Player "Not really."
    ch_Player "I pissed [Laura.name] off."

    $ Kurt.change_face("neutral")

    ch_Kurt "Is she not alvays pissed off?"
    ch_Player "Not like this, I really screwed up."

    $ Kurt.change_face("confused")

    "You explain what happened." 

    $ Kurt.change_face("angry")

    ch_Kurt "Schön blöd, vat zee hell is wrong with you?"

    $ Kurt.change_face("confused")

    ch_Kurt "You know better than anyone she has trust issues."
    ch_Kurt "She has every right to be angry."

    $ Kurt.change_face("neutral")

    ch_Player "I know. . ."
    ch_Kurt "I vould stay clear of her for a few days."
    ch_Kurt "She's liable to claw your eyes out if you don't let her calm down first."

    $ Kurt.change_face("confused")

    pause 1.0

    $ Kurt.change_face("sad")

    ch_Kurt ". . . I'm disappointed in you, man."
    "He leaves without another word."

    call remove_Characters(Kurt) from _call_remove_Characters_244

    $ ongoing_Event = False

    return

init python:

    def Laura_jealousy_follow_up():
        label = "Laura_jealousy_follow_up"

        conditions = [
            "EventScheduler.Events['Laura_jealousy_went_on_date'].completed or EventScheduler.Events['Laura_jealousy_flirted'].completed",
            "not Laura.status['mad']",
            "Player.location == Player.home",
            "not Present"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Laura_jealousy_follow_up:
    $ ongoing_Event = True

    call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_37

    "You wake up to someone banging on the door."
    ch_Player "One minute!"
    "You get out of bed, get dressed, and open the door."

    call send_Characters(Laura, Player.home, behavior = False) from _call_send_Characters_77

    $ Laura.change_face("angry1", blush = 1)

    ch_Player "Hey. . ."
    ". . ."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Player "Look, I'm sor. . ."

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "Why didn't you say anything?" 

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Laura "Do you not trust me?"
    ch_Player "Of course I trust you."

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    ch_Laura "If you just asked, you would've known I don't care." 

    $ Laura.change_face("furious", blush = 1)

    ch_Player "I. . . should've said something."
    ch_Laura "Well, say it now."

    $ Laura.change_face("angry1", blush = 1)

    ch_Player "Okay. . . you should know, I'm interested in having multiple girlfriends. . ." 

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "Fine."
    ch_Player "Wait, fine?"
    ch_Laura "Yes."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Like I said, you would've already known I don't care."
    ch_Laura "As long as you're still mine that is. . ." 
    ch_Player "Of course."

    $ Laura.change_face("confused1")

    ch_Player "You really don't care?"
    ch_Laura "No, like I said, you're the most attractive male at the Institute." 
    ch_Laura "It makes sense. . ."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "I do care when you don't tell me what you plan on doing."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura ". . . Don't keep things from me." 

    $ Laura.change_face("furious", blush = 1)

    ch_Laura "I'll just find out either way."
    ch_Player "From now on, I promise." 

    $ Laura.change_face("smirk2", blush = 1)

    ch_Laura "Good. . . now. . ."

    $ Laura.change_face("kiss1", blush = 2)

    "She roughly pulls you into a kiss."
    "After holding you there for several seconds, she lets go." 

    $ Laura.History.update("kiss")

    # $ Laura.change_face("sly", blush = 1)

    # ch_Laura "Also, I'm only interested in having {i}one{/i} boyfriend."
    "With that, she leaves."

    $ Laura.History.update("told_wants_multiple_girlfriends")

    call remove_Characters(Laura) from _call_remove_Characters_245

    $ ongoing_Event = False

    return

init python:

    def Laura_jealousy_went_on_date_anyways():
        label = "Laura_jealousy_went_on_date_anyways"

        conditions = [
            "Laura in Partners",
            "Laura.History.check('told_wants_multiple_girlfriend')",
            "(Laura.History.check_when('cheated_on_date') > max(Laura.History.check_when('told_wants_multiple_girlfriends'), EventScheduler.Events['Laura_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Laura_jealousy_flirted_anyways'].completed)) or (Laura.History.check_when('cheated_on_relationship') > max(Laura.History.check_when('told_wants_multiple_girlfriends'), EventScheduler.Events['Laura_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Laura_jealousy_flirted_anyways'].completed))",
            "Laura.location != Player.location"]
            
        sleeping = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, sleeping = sleeping, priority = priority, repeatable = repeatable)

label Laura_jealousy_went_on_date_anyways:
    $ ongoing_Event = True
    
    call start_new_day from _call_start_new_day_8

    if Player.location == Player.home:
        call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_38

        "You're awoken by harsh knocking on your door."

        if Present:
            $ temp = Present[0].name

            call remove_Characters(fade = False) from _call_remove_Characters_246

            $ fade_in_from_black(0.4)

            "It also looks like [temp] is already gone. . . that's odd."

        if black_screen:
            $ fade_in_from_black(0.4)

        ch_Player "Hold on! I'll be there in a minute."

        call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_39

        "The knocking continues."
        "You get out of bed and put some clothes on, before opening the door."
    else:
        call receive_text(Laura, "Your room, now.") from _call_receive_text_707

        "Your phone buzzing from a text wakes you up."

        call open_texts(Laura) from _call_open_texts_24
        call receive_text(Laura, "NOW") from _call_receive_text_708

        pause

        hide screen phone_screen

        if Present:
            $ Present[0].change_face("confused2")

            ch_Player "Shit, sorry [Present[0].name]. I gotta go take care of something."

            $ Present[0].change_face("confused1")

        "You quickly get dressed and head to your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_247
        call send_Characters(Laura, "bg_hallway", behavior = False) from _call_send_Characters_78
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_338

        $ Laura.change_face("appalled1")

        ch_Laura "Open."
        "You open the door, and she shoves you inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_248
        call set_the_scene(location = Player.home) from _call_set_the_scene_339

    $ Laura.change_face("suspicious2")

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Characters:
            if Player.History.check(f"cheated_on_Laura_with_{C.tag}_date") and Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_date") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_date")

            if Player.History.check(f"cheated_on_Laura_with_{C.tag}_relationship") and Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_relationship") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_relationship")

    if cheating_Character == Rogue:
        $ cheating_Character = "Rogue"

        if Rogue in Laura.knows_about:
            ch_Laura "So, you were already dating [cheating_Character] anyways?"
        else:
            ch_Laura "Why didn't you tell me you were planning on dating [cheating_Character]?"
    elif cheating_Character == Jean:
        $ cheating_Character = "Jean"

        if Jean in Laura.knows_about:
            ch_Laura "So, you were already dating [cheating_Character] anyways?"
        else:
            ch_Laura "Why didn't you tell me you were planning on dating [cheating_Character]?"

    if cheating_Character not in Laura.knows_about:
        $ Laura.knows_about.append(cheating_Character)

    $ Laura.change_face("furious")

    ch_Player "Shit. . . I'm so-"

    $ Laura.change_face("appalled2", mouth = "frown")

    ch_Laura "{i}Grrrrrr{/i}. . ."

    $ Laura.change_face("appalled3")

    ch_Laura "Are promises meaningless to you?!"

    call remove_Characters(Laura) from _call_remove_Characters_249

    "*SLAM*"
    "She has no mercy on the door either."
    ch_Player "Shit. . ."

    call change_Girl_stat(Laura, "trust", -15 - 5*(EventScheduler.Events["Laura_jealousy_went_on_date_anyways"].completed + EventScheduler.Events["Laura_jealousy_flirted_anyways"].completed)) from _call_change_Girl_stat_942

    $ Laura.give_status("mad")

    $ ongoing_Event = False

    return

init python:

    def Laura_jealousy_flirted_anyways():
        label = "Laura_jealousy_flirted_anyways"

        conditions = [
            "Laura in Partners",
            "Laura.History.check('told_wants_multiple_girlfriend')",
            "Laura.History.check('cheated_on_flirting_in_public') >= 3 and Laura.History.permanent['cheated_on_flirting_in_public'][-3] > max(Laura.History.check_when('told_wants_multiple_girlfriends'), EventScheduler.Events['Laura_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Laura_jealousy_flirted_anyways'].completed)",
            "Laura.location != Player.location",
            "Player.location in public_locations"]
            
        flirting = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, flirting = flirting, priority = priority, repeatable = repeatable)

label Laura_jealousy_flirted_anyways:
    $ ongoing_Event = True

    hide screen interactions_screen
    hide screen phone_screen

    call send_Characters(Laura, Player.location, behavior = False) from _call_send_Characters_110

    $ Laura.change_face("appalled1")

    "[Laura.name] appears out of nowhere, looking pissed."
    ch_Player "He. . ."

    $ Laura.change_face("furious", eyes = "left")

    if Player.temp in all_Characters and Player.temp != Laura:
        $ Player.temp.face("confused1")

    "She just grabs your arm and drags you to her room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_250
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_340
    call send_Characters(Laura, location = "bg_girls_hallway", behavior = False) from _call_send_Characters_262

    "[Laura.name] unlocks the door and shoves you inside."

    $ Laura.change_face("angry1")

    call remove_Characters(location = Laura.home) from _call_remove_Characters_251
    call set_the_scene(location = Laura.home) from _call_set_the_scene_341
    call send_Characters(Laura, location = Laura.home, behavior = False) from _call_send_Characters_263

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Characters:
            if Player.History.check(f"cheated_on_Laura_with_{C.tag}_flirting_in_public") and Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_flirting_in_public") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Laura_with_{C.tag}_flirting_in_public")

    if cheating_Character == Rogue:
        $ cheating_Character = "Rogue"

        if Rogue in Laura.knows_about:
            ch_Laura "So, you were already pursuing [cheating_Character] anyways?"
        else:
            ch_Laura "Why didn't you tell me you were planning on pursuing [cheating_Character]?"
    elif cheating_Character == Jean:
        $ cheating_Character = "Jean"

        if Jean in Laura.knows_about:
            ch_Laura "So, you were already pursuing [cheating_Character] anyways?"
        else:
            ch_Laura "Why didn't you tell me you were planning on pursuing [cheating_Character]?"

    if cheating_Character not in Laura.knows_about:
        $ Laura.knows_about.append(cheating_Character)

    $ Laura.change_face("furious")

    ch_Player "Shit. . . I'm so-"

    $ Laura.change_face("appalled2", mouth = "frown")

    ch_Laura "{i}Grrrrrr{/i}. . ."

    $ Laura.change_face("appalled3")

    ch_Laura "Are promises meaningless to you?!"
    "She seethes with anger, and shoves you out of the room."

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_342

    "*SLAM*"
    ". . . slamming the door behind you."
    ". . ."
    ch_Player "Well, shit. . ."

    call change_Girl_stat(Laura, "trust", -15 - 5*(EventScheduler.Events["Laura_jealousy_went_on_date_anyways"].completed + EventScheduler.Events["Laura_jealousy_flirted_anyways"].completed)) from _call_change_Girl_stat_1039

    $ Laura.give_status("mad")

    $ ongoing_Event = False

    # call move_location(Player.location) from _call_move_location_55

    return

init python:

    def Laura_jealousy_follow_up_again():
        label = "Laura_jealousy_follow_up_again"

        conditions = [
            "(EventScheduler.Events['Laura_jealousy_went_on_date_anyways'].completed and EventScheduler.Events['Laura_jealousy_went_on_date_anyways'].completed > EventScheduler.Events['Laura_jealousy_follow_up_again'].completed) or (EventScheduler.Events['Laura_jealousy_flirted_anyways'].completed and EventScheduler.Events['Laura_jealousy_flirted_anyways'].completed > EventScheduler.Events['Laura_jealousy_follow_up_again'].completed)",
            "not Laura.status['mad']",
            "Player.location == Player.home",
            "not Present"]
            
        waking = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waking = waking, priority = priority, repeatable = repeatable)

label Laura_jealousy_follow_up_again:
    $ ongoing_Event = True

    call knock_on_door(times = 4, intensity = 2.0) from _call_knock_on_door_40

    "You wake up to someone banging on the door."

    ch_Player "One minute!"
    "You get out of bed, get dressed, and open the door."

    call send_Characters(Laura, Player.home, behavior = False) from _call_send_Characters_111

    $ Laura.change_face("angry1", blush = 1)

    pause 1.0

    $ Laura.change_face("worried1", blush = 1)

    ch_Laura "You know I don't care, yet still neglected to tell me. . ."
    ch_Player "I know, I'm sorry, [Laura.name]."

    $ Laura.change_face("angry1", blush = 1)

    ch_Player "I'm just a forgetful idiot."
    ch_Laura "Don't do it again."

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Laura "Now. . ."

    $ Laura.change_face("kiss2", blush = 1)

    "[Laura.name] grabs you by the collar, pulling you into a kiss."
    "She holds it for a moment before letting go."

    $ Laura.History.update("kiss")

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "You'll see me later."

    call remove_Characters(Laura) from _call_remove_Characters_252

    $ ongoing_Event = False

    return