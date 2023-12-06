init python:

    def Jean_jealousy_went_on_date_text():
        label = "Jean_jealousy_went_on_date_text"

        conditions = [
            "Jean in Partners",

            "not Jean.History.check('told_wants_multiple_partners')",

            "not EventScheduler.Events['Jean_jealousy_flirted'].completed",

            "Jean.History.check('cheated_on_date') >= 2 or Jean.History.check('cheated_on_relationship')",

            "Jean.location != Player.location"]
            
        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Jean_jealousy_went_on_date_text:
    $ ongoing_Event = True

    call receive_text(Jean, f"Heyyyyyy {Jean.Player_petname} <3", buzz = False) from _call_receive_text_756
    call receive_text(Jean, "Got any plans tonight???", buzz = False) from _call_receive_text_757
    call receive_text(Jean, "Been wondering where you were tonight </3 </3 </3", buzz = False) from _call_receive_text_758
    call receive_text(Jean, "Well???", buzz = False) from _call_receive_text_759
    call receive_text(Jean, "You're not out with another girl, are you????", buzz = False) from _call_receive_text_760
    call receive_text(Jean, "HA", buzz = False) from _call_receive_text_761
    call receive_text(Jean, "Imagine", buzz = False) from _call_receive_text_762
    call receive_text(Jean, "As if", buzz = False) from _call_receive_text_763
    call receive_text(Jean, "Actually, just don't answer that", buzz = False) from _call_receive_text_764
    call receive_text(Jean, "Forget I even asked", buzz = False) from _call_receive_text_765
    call receive_text(Jean, "Just like, pretend you never got any of these", buzz = False) from _call_receive_text_766

    "As you're about to fall asleep, your phone buzzes."

    call open_texts(Jean) from _call_open_texts_30

    "You take your phone out and realize you missed a bunch of texts from [Jean.name]."

    pause

    hide screen phone_screen

    "Before you can send a reply, you pass out."

    $ ongoing_Event = False

    return

init python:

    def Jean_jealousy_went_on_date():
        label = "Jean_jealousy_went_on_date"

        conditions = [
            "Jean in Partners",

            "not Jean.History.check('told_wants_multiple_partners')",

            "not EventScheduler.Events['Jean_jealousy_flirted'].completed",

            "Jean.History.check('cheated_on_date') >= 2 or Jean.History.check('cheated_on_relationship')",

            "Jean.location != Player.location"]
            
        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Jean_jealousy_went_on_date:
    $ ongoing_Event = True
    
    call start_new_day from _call_start_new_day_9 

    "You were super tired and slept like a rock."

    if Player.location == Player.home:
        if Present:
            $ temp = Present[0].name

            call remove_Characters(fade = False) from _call_remove_Characters_267

            call knock_on_door(times = 3) from _call_knock_on_door_47

            $ fade_in_from_black(0.4)

            "You wake up to someone knocking at the door."
            "It looks like [temp] is already gone. . . that's odd."
        else:
            call knock_on_door(times = 3) from _call_knock_on_door_48

            $ fade_in_from_black(0.4)

            "You wake up to someone knocking at the door."

        ch_Jean "{i}Open up{/i}!"
        "You hear a muffled voice yelling at you."
        ch_Player "One sec!"
        "You quickly throw on some clothes and open the door."
    else:
        call receive_text(Jean, "You're in big trouble >:(") from _call_receive_text_767
        call receive_text(Jean, "Come to your own room, now.") from _call_receive_text_768

        "You're woken up by your phone buzzing repeatedly."

        call open_texts(Jean) from _call_open_texts_31 

        pause

        hide screen phone_screen

        if Present:
            $ Present[0].change_face("confused2")

            ch_Player "Shit, sorry [Present[0].name], I gotta go take care of something."

            $ Present[0].change_face("confused1")

        "You throw on your clothes and head out."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_268 
        call send_Characters(Jean, "bg_hallway", behavior = False) from _call_send_Characters_235 
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_361 

        $ Jean.change_face("appalled2")

        ch_Jean "Your room, now."
        "You do as she says, and she follows you into your room."

        call remove_Characters(location = Player.home) from _call_remove_Characters_269 
        call set_the_scene(location = Player.home) from _call_set_the_scene_362 

    call send_Characters(Jean, location = Player.home, behavior = False) from _call_send_Characters_236 

    $ Jean.change_face("appalled3")

    ch_Jean "What the actual fuck?!"

    $ Jean.change_face("suspicious2")

    ch_Player "Wha. . ."

    $ Jean.change_face("suspicious2", blush = 1)

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Jean_with_{C.tag}_date") and Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_date") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_date")

            if Player.History.check(f"cheated_on_Jean_with_{C.tag}_relationship") and Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_relationship") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_relationship")

    ch_Jean "I went to find you last night and saw you leave campus with [cheating_Character.public_name]."
    ch_Jean "Don't play dumb."

    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "Did you think I wouldn't notice?!"

    $ Jean.change_face("furious", blush = 1)

    ch_Player "I'm. . ."

    $ Jean.change_face("furious", eyes = "right", blush = 1)

    ch_Jean "Ughhhhh, don't even speak." 

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean ". . ."

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "You went on a date with her, didn't you?"

    $ Jean.change_face("angry1", blush = 1)

    ch_Player "Yes. . ."

    $ Jean.change_face("appalled1", blush = 1)

    ch_Jean "You didn't think to even ask me first?!"

    $ Jean.change_face("furious", blush = 1)

    ch_Player "I. . ."
    ch_Jean "Shush!"

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean ". . ."
    "She just leaves. . ."

    call remove_Characters(Jean) from _call_remove_Characters_270 

    "*SLAM*"
    ". . . and slams the door on the way out."

    $ Jean.give_status("mad")

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1108 

    ch_Player "Shit. . ."

    call knock_on_door(times = 2) from _call_knock_on_door_49 

    "You hear a more civilized knocking at the door."
    "You go over and open it."

    call send_Characters(Kurt, Player.home) from _call_send_Characters_237 

    $ Kurt.change_face("surprised")

    ch_Kurt "Everysing okay? Zat slam was quite loud. . ."

    $ Kurt.change_face("confused")

    ch_Player "Not really. . ." 
    ch_Player "I fucked things up with [Jean.name]."
    ch_Kurt "Vat did you do?"

    $ Kurt.change_face("confused")

    "You explain what happened."

    $ Kurt.change_face("angry")

    ch_Kurt "Schön blöd, what made you sink zat was a good idea?!"

    $ Kurt.change_face("confused")

    ch_Kurt "She has good reason to be angry viz you. . ."

    $ Kurt.change_face("neutral")

    ch_Kurt "Give her some space for zee next few days, I doubt she'll want to be talking to you." 

    $ Kurt.change_face("confused")

    pause 1.0

    $ Kurt.change_face("sad")

    ch_Kurt "I expected better from you. . ."
    "He leaves without another word."

    call remove_Characters(Kurt) from _call_remove_Characters_271 

    $ ongoing_Event = False

    return

init python:

    def Jean_jealousy_flirted():
        label = "Jean_jealousy_flirted"

        conditions = [
            "Jean in Partners",

            "not Jean.History.check('told_wants_multiple_partners')",

            "not EventScheduler.Events['Jean_jealousy_went_on_date'].completed",

            "Jean.History.check('cheated_on_flirting_in_public') >= 4 and Jean.History.permanent['cheated_on_flirting_in_public'].completed[-4] > EventScheduler.Events['Jean_boyfriend'].completed",
            
            "Jean.location != Player.location and Player.location in public_locations"]
            
        flirting = True

        priority = 99

        return EventClass(label, conditions, flirting = flirting, priority = priority)

label Jean_jealousy_flirted:
    $ ongoing_Event = True

    hide screen interactions_screen
    hide screen phone_screen

    call send_Characters(Jean, Player.location, behavior = False) from _call_send_Characters_238

    $ Jean.change_face("appalled1")

    "[Jean.name] walks in, looking pissed."

    ch_Jean "My room, now."

    if Player.temp in all_Companions and Player.temp != Jean:
        $ Player.temp.face("confused1")

    "She looks pretty angry, so you just go along with her."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_272
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_363
    call send_Characters(Jean, location = "bg_girls_hallway", behavior = False) from _call_send_Characters_239

    "[Jean.name] unlocks the door and pushes you inside."

    call remove_Characters(location = Jean.home) from _call_remove_Characters_273
    call set_the_scene(location = Jean.home) from _call_set_the_scene_364
    call send_Characters(Jean, location = Jean.home, behavior = False) from _call_send_Characters_240

    $ Jean.change_face("angry1")

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Jean_with_{C.tag}_flirting_in_public") and Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_flirting_in_public") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_flirting_in_public")

    ch_Jean "I might not be able to sense your emotions, but I could sense [cheating_Character.public_name]'s."

    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "Did you think I wouldn't notice?!"

    $ Jean.change_face("furious", blush = 1)

    ch_Player "I'm. . ."

    $ Jean.change_face("furious", eyes = "right", blush = 1)

    ch_Jean "Ughhhhh, don't even speak."

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean ". . ."

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "You were flirting with her, weren't you?"

    $ Jean.change_face("angry1", blush = 1)

    ch_Player "Yes. . ."

    $ Jean.change_face("appalled1", blush = 1)

    ch_Jean "You didn't think to even ask me first?!" 

    $ Jean.change_face("furious", blush = 1)

    ch_Player "I. . ."

    ch_Jean "Shush!"

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Jean ". . ."
    "She pushes you out the door."

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_365

    $ Jean.give_status("mad")

    "*SLAM*"
    ". . . and slams the door behind you."

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1109

    ch_Player "Shit. . ."

    call send_Characters(Kurt, Player.location) from _call_send_Characters_241

    $ Kurt.change_face("surprised")

    ch_Kurt "Everysing okay? Zat slam was quite loud. . ."

    $ Kurt.change_face("confused")

    ch_Player "Not really. . ." 
    ch_Player "I fucked things up with [Jean.name]."
    ch_Kurt "Vat did you do?"

    $ Kurt.change_face("confused")

    "You explain what happened."

    $ Kurt.change_face("angry")

    ch_Kurt "Schön blöd, what made you sink zat was a good idea?!"

    $ Kurt.change_face("confused")

    ch_Kurt "She has good reason to be angry viz you. . ."

    ch_Kurt "Give her some space for zee next few days, I doubt she'll want to be talking to you." 

    $ Kurt.change_face("confused")

    pause 1.0

    $ Kurt.change_face("sad")

    ch_Kurt "I expected better from you. . ."
    "He leaves without another word."

    call remove_Characters(Kurt) from _call_remove_Characters_274

    $ ongoing_Event = False

    return

init python:

    def Jean_jealousy_follow_up():
        label = "Jean_jealousy_follow_up"

        conditions = [
            "EventScheduler.Events['Jean_jealousy_went_on_date'].completed or EventScheduler.Events['Jean_jealousy_flirted'].completed",

            "Jean.is_in_normal_mood()",

            "Player.location == Player.home and not Present"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Jean_jealousy_follow_up:
    $ ongoing_Event = True

    call knock_on_door(times = 3) from _call_knock_on_door_50 

    "You wake up and hear a soft knocking from your door."
    ch_Player "I'll be right there!"
    "You quickly put some clothes on and open the door."

    call send_Characters(Jean, Player.home, behavior = False) from _call_send_Characters_242 

    $ Jean.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "Oh. . . hey, [Jean.petname]."

    $ Jean.change_face("angry1", blush = 1)

    ch_Jean ". . ." 

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "Damnit, I can't stay mad at you." 

    $ Jean.change_face("sad", blush = 1)

    ch_Jean "I just don't know why'd you'd go behind my back like that."

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "I guess it makes sense. . ." 
    ch_Jean "I mean, look at you. . ." 

    $ Jean.change_face("worried1", eyes = "down")

    pause 1.0

    $ Jean.change_face("angry1")

    ch_Player "I'm sorry, [Jean.petname]." 

    $ Jean.change_face("furious", blush = 1)

    ch_Player "I really am, I did a shitty thing." 

    $ Jean.change_face("angry1", eyes = "right", blush = 1)

    ch_Jean "You did."

    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "But I don't even really care if you have some side girls."
    ch_Player "Wait, really?"

    $ Jean.change_face("angry1", blush = 1)

    ch_Jean "Yeah, dummy." 
    ch_Jean "I would've let you have your fun if you just asked beforehand." 

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
    ch_Player "From now on, I promise."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "I won't have anyone playing with my man's heart. . ."

    $ Jean.change_face("sly")

    ch_Jean "And they better not hog all of your attention."

    # $ Jean.change_face("worried1", eyes = "right")

    # ch_Jean "But. . ."

    # $ Jean.change_face("worried1", mouth = "smirk")

    # ch_Jean "You're the {i}only{/i} boyfriend I want."

    $ Jean.change_face("sexy")

    ch_Jean "Now, give me a kiss to apologize." 

    $ Jean.change_face("kiss2", blush = 1)

    "She pulls you into a tight embrace and kisses you."

    $ Jean.change_face("sexy")

    "After a few moments, she finally lets go."

    $ Jean.History.update("kiss")

    ch_Jean "Good. . . still {i}mine{/i}."
    "With that, she leaves."

    $ Jean.History.update("told_wants_multiple_partners")

    call remove_Characters(Jean) from _call_remove_Characters_275 

    $ ongoing_Event = False

    return

init python:

    def Jean_jealousy_went_on_date_anyways():
        label = "Jean_jealousy_went_on_date_anyways"

        conditions = [
            "Jean in Partners",
            
            "Jean.History.check('told_wants_multiple_girlfriend')",
            
            "(Jean.History.check_when('cheated_on_date') > max(Jean.History.check_when('told_wants_multiple_partners'), EventScheduler.Events['Jean_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Jean_jealousy_flirted_anyways'].completed)) or (Jean.History.check_when('cheated_on_relationship') > max(Jean.History.check_when('told_wants_multiple_partners'), EventScheduler.Events['Jean_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Jean_jealousy_flirted_anyways'].completed))",
            
            "Jean.location != Player.location"]
            
        sleeping = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, sleeping = sleeping, priority = priority, repeatable = repeatable)

label Jean_jealousy_went_on_date_anyways:
    $ ongoing_Event = True
    
    call start_new_day from _call_start_new_day_10 

    "You were super tired and slept like a rock."

    if Player.location == Player.home:
        if Present:
            $ temp = Present[0].name

            call remove_Characters(fade = False) from _call_remove_Characters_276

            call knock_on_door(times = 3) from _call_knock_on_door_51

            $ fade_in_from_black(0.4)

            "You wake up to someone knocking at the door."
            "It looks like [temp] is already gone. . . that's odd."
        else:
            call knock_on_door(times = 3) from _call_knock_on_door_52

            $ fade_in_from_black(0.4)

            "You wake up to someone knocking at the door."

        ch_Jean "{i}Open up{/i}!"
        "You hear a muffled voice yelling at you."
        ch_Player "One sec!"
        "You quickly throw on some clothes and open the door."
    else:
        call receive_text(Jean, "You're in big trouble >:(") from _call_receive_text_769
        call receive_text(Jean, "Come to your own room, now.") from _call_receive_text_770

        "You're woken up by your phone buzzing repeatedly."

        call open_texts(Jean) from _call_open_texts_32 

        pause

        hide screen phone_screen

        if Present:
            $ Present[0].change_face("confused2")

            ch_Player "Shit, sorry [Present[0].name], I gotta go take care of something."

            $ Present[0].change_face("confused1")

        "You throw on your clothes and head out."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_277 
        call send_Characters(Jean, "bg_hallway", behavior = False) from _call_send_Characters_243 
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_366 

        $ Jean.change_face("appalled2")

        ch_Jean "Your room, now."
        "You do as she says, and she follows you into your room."

        call remove_Characters(location = Player.home) from _call_remove_Characters_278 
        call set_the_scene(location = Player.home) from _call_set_the_scene_367 

    call send_Characters(Jean, location = Player.home, behavior = False) from _call_send_Characters_244 

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Jean_with_{C.tag}_date") and Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_date") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_date")

            if Player.History.check(f"cheated_on_Jean_with_{C.tag}_relationship") and Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_relationship") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_relationship")

    if cheating_Character in Jean.knows_about:
        ch_Jean "So you were dating [cheating_Character.public_name] anyways?"
    else:
        ch_Jean "Why didn't you tell me you wanted to date [cheating_Character.public_name]?"

        $ Jean.knows_about.append(cheating_Character)

    $ Jean.change_face("appalled1")

    ch_Jean "What the fuck, [Jean.Player_petname]?"

    $ Jean.change_face("furious")

    ch_Jean "Why didn't you tell me you wanted to date [cheating_Character]?!"
    ch_Player "OH. . . shit. . ."

    $ Jean.change_face("worried3", blush = 1)

    ch_Jean "You {i}promised{/i} to tell me beforehand. . ."
    ch_Jean "Why. . ."

    $ Jean.change_face("furious") 

    ch_Jean "This is {i}REALLY{/i} not cool, [Jean.Player_petname]."

    $ Jean.change_face("furious", eyes = "right")

    ch_Jean "I don't know why it's so hard just to ask. . ."

    call remove_Characters(Jean) from _call_remove_Characters_279 

    "She leaves without another word."
    ch_Player "Goddamnit. . ."

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1110 

    $ Jean.give_status("mad")

    $ ongoing_Event = False

    return

init python:

    def Jean_jealousy_flirted_anyways():
        label = "Jean_jealousy_flirted_anyways"

        conditions = [
            "Jean in Partners",
            
            "Jean.History.check('told_wants_multiple_girlfriend')",
            
            "Jean.History.check('cheated_on_flirting_in_public') >= 4 and Jean.History.permanent['cheated_on_flirting_in_public'].completed[-3] > max(Jean.History.check_when('told_wants_multiple_partners'), EventScheduler.Events['Jean_jealousy_went_on_date_anyways'].completed, EventScheduler.Events['Jean_jealousy_flirted_anyways'].completed)",
            
            "Jean.location != Player.location and Player.location in public_locations"]
            
        flirting = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, flirting = flirting, priority = priority, repeatable = repeatable)

label Jean_jealousy_flirted_anyways:
    $ ongoing_Event = True

    hide screen interactions_screen
    hide screen phone_screen

    call send_Characters(Jean, Player.location, behavior = False) from _call_send_Characters_245

    $ Jean.change_face("appalled1")

    "[Jean.name] walks in, looking pissed."

    ch_Jean "My room, now."

    if Player.temp in all_Companions and Player.temp != Jean:
        $ Player.temp.face("confused1")

    "She looks pretty angry, so you just go along with her."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_280
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_368
    call send_Characters(Jean, location = "bg_girls_hallway", behavior = False) from _call_send_Characters_246

    "[Jean.name] unlocks the door and pushes you inside."

    call remove_Characters(location = Jean.home) from _call_remove_Characters_281
    call set_the_scene(location = Jean.home) from _call_set_the_scene_369
    call send_Characters(Jean, location = Jean.home, behavior = False) from _call_send_Characters_247

    $ Jean.change_face("confused1")

    ch_Jean "Really, [Jean.Player_petname]?"

    $ Jean.change_face("angry1")

    $ cheating_Character = None
    $ cheating_date = 0

    python:
        for C in all_Companions:
            if Player.History.check(f"cheated_on_Jean_with_{C.tag}_flirting_in_public") and Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_flirting_in_public") > cheating_date:
                cheating_Character = C
                cheating_date = Player.History.check_when(f"cheated_on_Jean_with_{C.tag}_flirting_in_public")

    if cheating_Character in Jean.knows_about:
        ch_Jean "So, you were already flirting with [cheating_Character.public_name] anyways?"
    else:
        ch_Jean "Why the hell didn't you tell me you wanted to get with [cheating_Character.public_name]?"

        $ Jean.knows_about.append(cheating_Character)

    $ Jean.change_face("furious1")

    ch_Player "Shit. . . I'm so-"

    $ Jean.change_face("appalled1")

    ch_Jean "{i}NOT{/i} cool. . ."

    $ Jean.change_face("furious", eyes = "right")

    ch_Jean "I don't know why it's so hard just to ask. . ."

    call remove_Characters(Jean) from _call_remove_Characters_282 

    "She leaves without another word."
    ch_Player "Goddamnit. . ."

    call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1111 

    $ Jean.give_status("mad")

    $ ongoing_Event = False

    return

init python:

    def Jean_jealousy_follow_up_again():
        label = "Jean_jealousy_follow_up_again"

        conditions = [
            "(EventScheduler.Events['Jean_jealousy_went_on_date_anyways'].completed and EventScheduler.Events['Jean_jealousy_went_on_date_anyways'].completed_when > EventScheduler.Events['Jean_jealousy_follow_up_again'].completed) or (EventScheduler.Events['Jean_jealousy_flirted_anyways'].completed and EventScheduler.Events['Jean_jealousy_flirted_anyways'].completed_when > EventScheduler.Events['Jean_jealousy_follow_up_again'].completed)",
            
            "Jean.is_in_normal_mood()",

            "Player.location == Player.home and not Present"]
            
        waking = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waking = waking, priority = priority, repeatable = repeatable)

label Jean_jealousy_follow_up_again:
    $ ongoing_Event = True

    call knock_on_door(times = 3, intensity = 0.5) from _call_knock_on_door_53 

    "You wake up and hear a soft knocking from your door."
    ch_Player "I'll be right there!"
    "You quickly put some clothes on and open the door."

    call send_Characters(Jean, Player.home, behavior = False) from _call_send_Characters_248 

    $ Jean.change_face("angry1")

    pause 1.0

    $ Jean.change_face("worried1")

    ch_Jean "It's so hard to stay mad at you. . ."
    ch_Player "Hey, Jean.petname]."
    ch_Player "I really am sorry. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "I'm a forgetful idiot."
    ch_Jean "You got that right."

    $ Jean.change_face("worried1")

    ch_Jean "But, you know I'd say yes, so just ask me next time, okay?"
    ch_Player "Okay."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Good, now. . ."

    $ Jean.change_face("kiss2", blush = 1)

    "[Jean.name] pulls you into a kiss, one hand finding its way to your ass, as usual."
    "She holds it for a moment before letting go."

    $ Jean.History.update("kiss")

    $ Jean.change_face("smirk2", blush = 1)

    ch_Jean "I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_283 

    $ ongoing_Event = False

    return