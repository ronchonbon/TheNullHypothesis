init python:

    def Rogue_jealousy_went_on_date():
        label = "Rogue_jealousy_went_on_date"

        conditions = [
            "Rogue in Partners",

            "not Rogue.History.check('told_wants_multiple_partners')",

            "not EventScheduler.Events['Rogue_jealousy_flirted'].completed",

            "Rogue.History.check('cheated_on_date') or Rogue.History.check('cheated_on_relationship')",
            
            "Rogue.location != Player.location"]
            
        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Rogue_jealousy_went_on_date:
    $ ongoing_Event = True
    
    call start_new_day from _call_start_new_day_11 

    if Player.location == Player.home:
        if Present:
            $ temp = Present[0].name

            call remove_Characters(fade = False) from _call_remove_Characters_290

            $ fade_in_from_black(0.4)

            "You wake up feeling well rested."
            "It looks like [temp] is already gone. . . that's odd."
            "You go to brush your teeth."
        else:
            $ fade_in_from_black(0.4)

            "You wake up feeling well rested and go to brush your teeth."
        
        "Before you can finish. . ."

        call knock_on_door(times = 3) from _call_knock_on_door_56

        ch_Player "One sec!"
        "You finish up and open the door."
    else:
        call receive_text(Rogue, "Can we talk") from _call_receive_text_805
        call receive_text(Rogue, "Your room") from _call_receive_text_806

        "You wake up right as your phone buzzes from a text."

        call open_texts(Rogue) from _call_open_texts_35 
        call receive_text(Rogue, "Now, please") from _call_receive_text_807

        pause

        hide screen phone_screen

        if Present:
            $ Present[0].change_face("confused2")

            ch_Player "Sorry [Present[0].name], I gotta go take care of something."

            $ Present[0].change_face("confused1")

        "You throw on your clothes and head out."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_291 
        call send_Characters(Rogue, "bg_hallway", behavior = False) from _call_send_Characters_268 
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_376 

        $ Rogue.change_face("angry1")

        "[Rogue.name] doesn't say anything and just waits for you to open the door."
        "You do, and she follows you inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_292 
        call set_the_scene(location = Player.home) from _call_set_the_scene_377 

    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_269 

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Player "What di-"

    $ Rogue.change_face("confused1")

    ch_Rogue "Where were ya last night?"

    $ Rogue.change_face("furious", eyes = "right")

    ch_Player "I. . ."

    $ Rogue.change_face("furious")

    ch_Rogue "Ah know ya weren't 'bout to lie to me."

    $ Rogue.change_face("angry2")

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Rogue_with_{C.tag}_date") and Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_date") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_date")

            if Player.History.check(f"cheated_on_Rogue_with_{C.tag}_relationship") and Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_relationship") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_relationship")

    ch_Rogue "Ah saw ya leavin' campus with [cheating_Character.public_name]."

    $ Rogue.change_face("worried2")

    ch_Player "We. . . went out on a date together. . ."

    $ Rogue.change_face("appalled2")

    ch_Rogue "What in the hell possessed ya to go 'n do that?!"

    $ Rogue.change_face("furious")

    ch_Rogue "Ya didn't even think to ask me first or nothin'?"

    $ Rogue.change_face("angry1")

    ch_Player "I just thought. . ." 

    $ Rogue.change_face("angry1", eyes = "squint")

    ch_Rogue "Apparently ya didn't do much thinkin' at all!" 

    $ Rogue.change_face("worried2")

    ch_Rogue ". . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "{size=-5}Ah'm sorry for yellin'{/size}. . ." 

    $ Rogue.change_face("sad", eyes = "right")

    "She leaves without another word."

    call remove_Characters(Rogue) from _call_remove_Characters_293 

    $ Rogue.give_status("mad")

    call change_Character_stat(Rogue, "trust", -large_stat) from _call_change_Character_stat_1149 

    ch_Player "Fuck. . ."
    "You've never heard [Rogue.name] raise her voice like that before. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_57 

    "You hear a different, gentle knocking at the door."
    "You go over and open it."

    call send_Characters(Kurt, Player.home) from _call_send_Characters_270 

    $ Kurt.change_face("surprised1")

    ch_Kurt "Everysing okay? You could hear zee yelling from down the hall. . ."

    $ Kurt.change_face("angry1")

    ch_Player "I really screwed things up with Rogue."
    ch_Kurt "Schön blöd, I told you to be careful viz her."

    $ Kurt.change_face("confused1")

    ch_Kurt "Vat happened?"
    "You explain."

    $ Kurt.change_face("angry1")

    ch_Kurt "Wirklich, Bruder?"

    $ Kurt.change_face("confused1")

    ch_Kurt "Why zee hell vould you do somesing like that?"

    $ Kurt.change_face("sad")

    ch_Kurt "You know she's been struggling. . ." 

    $ Kurt.change_face("neutral")

    ch_Kurt "I think you should stay avay from her for a few days."
    ch_Kurt "She probably von't be in zee talking mood."

    $ Kurt.change_face("confused1")

    pause 1.0

    $ Kurt.change_face("sad")

    ch_Kurt "I'm. . . disappointed, [Player.first_name]."
    ch_Kurt "Be better."
    "He leaves without another word."

    call remove_Characters(Kurt) from _call_remove_Characters_294 

    $ ongoing_Event = False

    return

init python:

    def Rogue_jealousy_flirted():
        label = "Rogue_jealousy_flirted"

        conditions = [
            "Rogue in Partners",

            "not Rogue.History.check('told_wants_multiple_partners')",
            
            "not EventScheduler.Events['Rogue_jealousy_went_on_date'].completed",
            
            "Rogue.History.check('cheated_on_flirting_in_public') >= 3 and Rogue.History.permanent['cheated_on_flirting_in_public'].completed[-3] > EventScheduler.Events['Rogue_boyfriend'].completed",
            
            "Rogue.location != Player.location and Player.location == Player.home"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Rogue_jealousy_flirted:
    $ ongoing_Event = True

    "You wake up feeling well rested and go to brush your teeth."
    "Before you can finish. . ."

    call knock_on_door(times = 3) from _call_knock_on_door_58

    ch_Player "One sec!"
    "You finish up and open the door."

    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_271 

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Player "Hey, good mor-"

    $ Rogue.change_face("appalled1")

    ch_Rogue "What the hell, [Rogue.Player_petname]?"

    $ Rogue.change_face("furious")

    ch_Player "Wha. . ."
    ch_Rogue "Don't you play dumb."
    ch_Rogue "Ain't no way ah could miss seein' ya flirt around with them other girls."

    $ Rogue.change_face("angry2")

    ch_Rogue "Ya didn't even think to ask if ah would be okay with somethin' like that?!"

    $ Rogue.change_face("furious")

    ch_Player "I just thought. . ." 

    $ Rogue.change_face("angry1", eyes = "squint")

    ch_Rogue "Apparently ya didn't do much thinkin' at all!" 

    $ Rogue.change_face("worried2")

    ch_Rogue ". . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "{size=-5}Ah'm sorry for yellin'{/size}. . ." 

    $ Rogue.change_face("sad", eyes = "right")

    "She leaves without another word."

    call remove_Characters(Rogue) from _call_remove_Characters_295 

    $ Rogue.give_status("mad")

    call change_Character_stat(Rogue, "trust", -large_stat) from _call_change_Character_stat_1150 

    ch_Player "Fuck. . ."
    "You've never heard [Rogue.name] raise her voice like that before. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_59 

    "You hear a different, gentle knocking at the door."
    "You go over and open it."

    call send_Characters(Kurt, Player.home) from _call_send_Characters_272 

    $ Kurt.change_face("surprised1")

    ch_Kurt "Everysing okay? You could hear zee yelling from down the hall. . ."

    $ Kurt.change_face("angry1")

    ch_Player "I really screwed things up with Rogue."
    ch_Kurt "Schön blöd, I told you to be careful viz her."

    $ Kurt.change_face("confused1")

    ch_Kurt "Vat happened?"
    "You explain."

    $ Kurt.change_face("angry1")

    ch_Kurt "Wirklich, Bruder?"

    $ Kurt.change_face("confused1")

    ch_Kurt "Why zee hell vould you do somesing like that?"

    $ Kurt.change_face("sad")

    ch_Kurt "You know she's been struggling. . ." 

    $ Kurt.change_face("neutral")

    ch_Kurt "I think you should stay avay from her for a few days."
    ch_Kurt "She probably von't be in zee talking mood."

    $ Kurt.change_face("confused1")

    pause 1.0

    $ Kurt.change_face("sad")

    ch_Kurt "I'm. . . disappointed, [Player.first_name]."
    ch_Kurt "Be better."
    "He leaves without another word."

    call remove_Characters(Kurt) from _call_remove_Characters_296 

    $ ongoing_Event = False

    return

init python:

    def Rogue_jealousy_follow_up():
        label = "Rogue_jealousy_follow_up"

        conditions = [
            "EventScheduler.Events['Rogue_jealousy_went_on_date'].completed or EventScheduler.Events['Rogue_jealousy_flirted'].completed",
            
            "Rogue.is_in_normal_mood()",
            
            "Player.location == Player.home and not Present"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Rogue_jealousy_follow_up:
    $ ongoing_Event = True

    call knock_on_door(times = 3) from _call_knock_on_door_60 

    "You're awoken, earlier than usual, by someone knocking at the door."
    ch_Player "*yawn*. . . I'll be right there!"
    "You hop out of bed, get dressed and open the door."

    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_273 

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "Oh, hey, [Rogue.name]. . ." 

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Good mornin'. . . sorry for wakin' ya so early. . ."

    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "Ah just wanted to come by and apologize for how ah acted the other day."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Player "No, I'm the one who should be sorry, you have nothing to apologize for." 

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "But, ah got so angry. . . and was yellin' at you. . ." 

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Player "For good reason."
    ch_Player "I did a shitty thing. . ." 

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "It's not that ah was so angry about what ya did."
    ch_Rogue "More so that you'd go behind my back with somethin' like that. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "I'm really sorry. . ."
    ch_Rogue "Ah mean if ya just asked about wantin' to date another girl, ah wouldn't really mind none."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Player "Wait, really?" 

    ch_Rogue "Ah saw this comin' anyway."
    ch_Rogue "It ain't no secret that yer a real hot commodity 'round here."

    $ Rogue.change_face("confused1", eyes = "right")

    ch_Player "'Hot commodity'?"
    ch_Rogue "Ya don't have to pretend 'round me, [Rogue.Player_petname]."
    ch_Player "Wha-"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "You can have all the girlfriends ya want, so long as ya don't forget about me."
    ch_Player "Well to be honest, I am interested in having multiple girlfriends. . ."
    ch_Player "From now on, I promise I'll tell you who, beforehand." 
    ch_Rogue "Thanks, [Rogue.Player_petname]."

    $ Rogue.change_face("worried1")

    # ch_Rogue "And ah sure as heck don't want more than one boyfriend. . ."

    # $ Rogue.change_face("worried1", mouth = "lipbite")

    # ch_Rogue "Just you, only you."
    ch_Rogue "Ah know it's cliché but. . . can we kiss to make up?" 

    $ Rogue.change_face("worried1")

    ch_Player "Heh, of course."

    $ Rogue.change_face("kiss1", blush = 1)

    "You pull [Rogue.name] into a gentle embrace and kiss her."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    "After a few seconds, you let go."

    $ Rogue.History.update("kiss")

    ch_Rogue "Thanks. . . ah'll see you later, {i}boyfriend{/i}. . ."
    "She leaves."

    $ Rogue.History.update("told_wants_multiple_partners")

    call remove_Characters(Rogue) from _call_remove_Characters_297 

    $ ongoing_Event = False

    return

init python:

    def Rogue_jealousy_went_on_date_anyways():
        label = "Rogue_jealousy_went_on_date_anyways"

        conditions = [
            "Rogue in Partners",
            
            "Rogue.History.check('told_wants_multiple_girlfriend')",
            
            "(Rogue.History.check_when('cheated_on_date') > max(Rogue.History.check_when('told_wants_multiple_partners'), EventScheduler.Events['Rogue_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Rogue_jealousy_flirted_anyways'].completed)) or (Rogue.History.check_when('cheated_on_relationship') > max(Rogue.History.check_when('told_wants_multiple_partners'), EventScheduler.Events['Rogue_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Rogue_jealousy_flirted_anyways'].completed))",
            
            "Rogue.location != Player.location"]
            
        sleeping = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, sleeping = sleeping, priority = priority, repeatable = repeatable)

label Rogue_jealousy_went_on_date_anyways:
    $ ongoing_Event = True
    
    call start_new_day from _call_start_new_day_12 

    if Player.location == Player.home:
        if Present:
            $ temp = Present[0].name

            call remove_Characters(fade = False) from _call_remove_Characters_298

            $ fade_in_from_black(0.4)

            "You wake up feeling well rested."
            "It looks like [temp] is already gone. . . that's odd."
            "You go to brush your teeth."
        else:
            $ fade_in_from_black(0.4)

            "You wake up feeling well rested and go to brush your teeth."
        
        "Before you can finish. . ."

        call knock_on_door(times = 3) from _call_knock_on_door_61

        ch_Player "One sec!"
        "You finish up and open the door."
    else:
        call receive_text(Rogue, "Can we talk") from _call_receive_text_808
        call receive_text(Rogue, "Your room") from _call_receive_text_809

        "You wake up right as your phone buzzes from a text."

        call open_texts(Rogue) from _call_open_texts_36 
        call receive_text(Rogue, "Now, please") from _call_receive_text_810

        pause

        hide screen phone_screen

        if Present:
            $ Present[0].change_face("confused2")

            ch_Player "Sorry [Present[0].name], I gotta go take care of something."

            $ Present[0].change_face("confused1")

        "You throw on your clothes and head out."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_299 
        call send_Characters(Rogue, "bg_hallway", behavior = False) from _call_send_Characters_274 
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_378 

        $ Rogue.change_face("angry1")

        "[Rogue.name] doesn't say anything and just waits for you to open the door."
        "You do, and she follows you inside."

        call remove_Characters(location = Player.home) from _call_remove_Characters_300 
        call set_the_scene(location = Player.home) from _call_set_the_scene_379 

    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_275 

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Player "What di-"

    $ Rogue.change_face("confused1")

    ch_Rogue "Ah just don't get it, [Player.first_name]."

    $ Rogue.change_face("worried2")

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Rogue_with_{C.tag}_date") and Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_date") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_date")

            if Player.History.check(f"cheated_on_Rogue_with_{C.tag}_relationship") and Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_relationship") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_relationship")

    if cheating_Character in Rogue.knows_about:
        ch_Rogue "So, you were already dating [cheating_Character.public_name] anyways?"
    else:
        ch_Rogue "Why wouldn't ya tell me you were interested in [cheating_Character.public_name]?"

        $ Rogue.knows_about.append(cheating_Character)

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "You know ah wouldn't mind. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "It ain't hard."
    ch_Rogue "Why couldn't you just. . ."

    $ Rogue.change_face("worried1")

    call remove_Characters(Rogue) from _call_remove_Characters_301 

    "She leaves without another word."
    ch_Player "Goddamnit. . ."

    call change_Character_stat(Rogue, "trust", -large_stat) from _call_change_Character_stat_1152 

    $ Rogue.give_status("mad")

    $ ongoing_Event = False

    return

init python:

    def Rogue_jealousy_flirted_anyways():
        label = "Rogue_jealousy_flirted_anyways"

        conditions = [
            "Rogue in Partners",
            
            "Rogue.History.check('told_wants_multiple_girlfriend')",
            
            "Rogue.History.check('cheated_on_flirting_in_public') >= 3 and Rogue.History.permanent['cheated_on_flirting_in_public'].completed[-3] > max(Rogue.History.check_when('told_wants_multiple_partners'), EventScheduler.Events['Rogue_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Rogue_jealousy_flirted_anyways'].completed)",
            
            "Rogue.location != Player.location and Player.location == Player.home"]
            
        waking = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waking = waking, priority = priority, repeatable = repeatable)

label Rogue_jealousy_flirted_anyways:
    $ ongoing_Event = True

    "You wake up feeling well rested and go to brush your teeth."
    "Before you can finish. . ."

    call knock_on_door(times = 3) from _call_knock_on_door_62

    ch_Player "One sec!"
    "You finish up and open the door."

    call send_Characters(Rogue, location = Player.home, behavior = False) from _call_send_Characters_276 

    $ Rogue.change_face("angry1", eyes = "right")

    ch_Player "Hey, good mor-"

    $ Rogue.change_face("confused1")

    ch_Rogue "Ah just don't get it, [Player.first_name]."

    $ Rogue.change_face("worried2")

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Rogue_with_{C.tag}_flirting_in_public") and Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_flirting_in_public") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Rogue_with_{C.tag}_flirting_in_public")

    if cheating_Character in Rogue.knows_about:
        ch_Rogue "So, you were already dating [cheating_Character.public_name] anyways?"
    else:
        ch_Rogue "Why wouldn't ya tell me you were interested in [cheating_Character.public_name]?"

        $ Rogue.knows_about.append(cheating_Character)

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue "You know ah wouldn't mind. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "It ain't hard."
    ch_Rogue "Why couldn't you just. . ."

    $ Rogue.change_face("worried1")

    call remove_Characters(Rogue) from _call_remove_Characters_302 

    "She leaves without another word."
    ch_Player "Goddamnit. . ."

    call change_Character_stat(Rogue, "trust", -large_stat) from _call_change_Character_stat_1154 

    $ Rogue.give_status("mad")

    $ ongoing_Event = False

    return

init python:

    def Rogue_jealousy_follow_up_again():
        label = "Rogue_jealousy_follow_up_again"

        conditions = [
            "(EventScheduler.Events['Rogue_jealousy_went_on_date_anyways'].completed and EventScheduler.Events['Rogue_jealousy_went_on_date_anyways'].completed_when > EventScheduler.Events['Rogue_jealousy_follow_up_again'].completed) or (EventScheduler.Events['Rogue_jealousy_flirted_anyways'].completed and EventScheduler.Events['Rogue_jealousy_flirted_anyways'].completed_when > EventScheduler.Events['Rogue_jealousy_follow_up_again'].completed)",
            
            "Rogue.is_in_normal_mood()",
            
            "Player.location == Player.home and not Present"]
            
        waking = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waking = waking, priority = priority, repeatable = repeatable)

label Rogue_jealousy_follow_up_again:
    $ ongoing_Event = True

    call knock_on_door(times = 3) from _call_knock_on_door_63 

    "You're awoken, earlier than usual, by someone knocking at the door."
    ch_Player "*yawn*. . . I'll be right there!"
    "You hop out of bed, get dressed and open the door."

    call send_Characters(Rogue, Player.home, behavior = False) from _call_send_Characters_277 

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "Hey, [Rogue.name]. . ." 

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Good mornin'. . ."
    ch_Player "Look, I know I messed up."
    ch_Player "I really am sorry."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "It's alright."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah just overreacted."
    ch_Player "No, really, you didn't."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Could ya please just ask me next time?"
    ch_Rogue "You know ah'd let ya. . ."
    ch_Player "I will."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thanks. . ."

    $ Rogue.change_face("kiss2", blush = 1)

    "You pull [Rogue.name] into a kiss, holding her close."

    $ Rogue.History.update("kiss")

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah gotta go, but maybe you could come see me later?"

    call remove_Characters(Rogue) from _call_remove_Characters_303 

    $ ongoing_Event = False

    return