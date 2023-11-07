label day_three_intro:
    call start_new_day from _call_start_new_day_5

    $ check_predicted_images()

    call refresh_season_content from _call_refresh_season_content_6

    # menu:
    #     "Skip Day Three?"
    #     "Yes":
    #         jump day_three_end
    #     "No":
    #         pass

    $ Player.messy_bed = True

    call set_the_scene(location = Player.home) from _call_set_the_scene_252

    "You wake up a bit earlier than usual to get ready."
        
    play music "sounds/music/Day to Day.ogg" fadeout 1.0 fadein 1.0

    call phone_buzz from _call_phone_buzz_7

    "Your phone buzzes as a reminder pops up about your combat lesson with [Laura.name] in the evening."

    $ Player.messy_bed = False

    "You head out with plenty of time to spare{w} - just one quick stop before class."

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_253
    call knock_on_door(times = 2) from _call_knock_on_door_29

    "You knock on the door."

    $ Rogue.name = "???"
    
    ch_Rogue "Ah'll be right there!"

    $ Rogue.name = "Rogue"

    call add_Characters(Rogue) from _call_add_Characters_60

    $ Rogue.change_face("surprised2")

    ch_Player "Morning, [Rogue.name]. I just wanted to come by and apologize."

    if not Rogue.History.check("Player_faked_injury"):
        $ Rogue.change_face("pleased2", blush = 1)

        ch_Player "I hope I didn't make you feel uncomfortable last night - you left in a hurry."
        ch_Rogue "Yeah, sorry 'bout that. . . You didn't make me uncomfortable, was just a bit overwhelmed."

        $ Rogue.blush = 2

        ch_Rogue "Touchin' someone for the first time in years. . . and then. . ."

        $ Rogue.change_face("worried2", eyes = "right", mouth = "smirk", blush = 3)

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 3)

        ch_Rogue "Ah do appreciate the compliment though. . .{p}{size=-5}Ah think you're handsome too{/size}."
    else:
        $ Rogue.change_face("worried1")

        ch_Rogue "Oh. . . it's alright. Ah just overreacted a bit. Think nothin' of it."

        $ Rogue.change_face("sad")

        menu:
            "Apologize properly":
                "You can tell she's still bothered."

                $ Rogue.change_face("smirk1")

                ch_Player "You don't have to be nice, you can tell me I'm a jerk."
                ch_Player "I really am sorry. I can't imagine how difficult it's been for you dealing with a power like that."
                ch_Player "I've only had mine for a couple days and I can see now how lucky I got."
                
                $ Rogue.change_face("smirk2")

                ch_Rogue "It {i}was{/i} kind of a jerk thing to do."
                ch_Rogue "But it really is okay. You've only been around other mutants a few days, and your childhood was pretty normal."
                ch_Player "I'll be more sensitive, promise."

                call change_Girl_stat(Rogue, "love", 5) from _call_change_Girl_stat_890
                call change_Girl_stat(Rogue, "trust", 5) from _call_change_Girl_stat_891
            "Accept her forgiveness":
                $ Rogue.change_face("neutral")

                "Really?"

    $ Rogue.change_face("neutral")

    ch_Player "So, did you wanna walk to class together again?"
    
    $ Rogue.change_face("pleased2")

    ch_Rogue "Sure, [Rogue.Player_petname]!"

    call hide_Character(Rogue) from _call_hide_Character_38

    $ fade_to_black(0.4)

    "You both make your way across campus."
    "You tell her a bit about your life before getting rescued by [Charles.name]."
    
    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_254
    call add_Characters(Rogue) from _call_add_Characters_61

    "You get to the classroom a bit early and see a few people slowly stream in."

    call add_Characters(Kurt) from _call_add_Characters_62

    "[Kurt.name] sits across the room and you wave to each other."

    call send_Characters(Kurt, "hold") from _call_send_Characters_192

    $ Rogue.change_face("smirk2")

    "[Rogue.name] sits next to you again. You notice she scoots just a bit closer than yesterday."
    "Class starts on World Politics. You absentmindedly wonder what kind of terrible evil [Ororo.name] has to fight instead of teaching this class."

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 1
    
    $ lighting = "day"

    $ fade_in_from_black(0.4)

    ch_Rogue "Ah'll see ya later, [Rogue.Player_petname], ah'm goin' shoppin' with some friends."

    call send_Characters(Rogue, "hold") from _call_send_Characters_193

    "As [Rogue.name] leaves, you head over to [Kurt.name]."
    
    call add_Characters(Kurt) from _call_add_Characters_63

    ch_Player "Hey [Kurt.name], how's it going?"

    $ Kurt.change_face("confused")

    ch_Kurt "I assume you apologized to [Rogue.name]?"
    ch_Player "Yep! Everything's cool between us."

    $ Kurt.change_face("neutral")

    ch_Kurt "Cool huh? I don't know if you saw the vay she vas looking at you, but sings are a bit varmer zan cool."
    ch_Kurt "Look mein bruder, [Rogue.name] is a nice girl in a very unfortunate situation. You sink anyone is villing to date a person who could kill zem just by holding hands? Nein."
    ch_Kurt "But now you're here."
    ch_Kurt "Don't be surprised ven she gets attached."
    ch_Player "That's. . . a good point."
    ch_Player "By the way, do you know anything about [Laura.name]?"
    ch_Player "Like how to stay on her good side since [Ororo.name] made her my combat instructor?"

    $ Kurt.change_face("happy")

    ch_Kurt "Ha!"
    "[Kurt.name] can't help but laugh in your face."
    ch_Kurt "Sorry, you're on your own viz zat one. I don't even know anyone who'd call her zeir friend. Prepare for a beating, she fights like an animal."
    ch_Kurt "I don't think she spent any time at all in zee outside vorld after escaping vatever facility held her."
    ch_Kurt "Came straight here. . . and zat was only a month ago, hence zee lack of social skills."
    ch_Player "Great. . ."
    "[Kurt.name] excuses himself, still chuckling under his breath as he leaves."

    call send_Characters(Kurt, "hold") from _call_send_Characters_194

    jump day_three_classroom_menu
        
label day_three_Player_room:
    $ lights_on = True
    $ door_locked = False

    call set_the_scene(location = Player.home) from _call_set_the_scene_255

    while True:
        menu:
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_three_Player_room')",
                    "bg_classroom": "renpy.jump('day_three_classroom')",
                    "bg_danger": "renpy.jump('day_three_danger')",
                    "bg_lockers": "renpy.jump('day_three_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_three_classroom:
    $ lights_on = True
    $ door_locked = False
    
    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_256

    while True:
        menu day_three_classroom_menu:
            "Take afternoon class":
                jump day_three_afternoon_class
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_three_Player_room')",
                    "bg_classroom": "renpy.jump('day_three_classroom')",
                    "bg_danger": "renpy.jump('day_three_danger')",
                    "bg_lockers": "renpy.jump('day_three_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_three_danger:
    $ lights_on = True
    $ door_locked = False
    
    call set_the_scene(location = "bg_danger") from _call_set_the_scene_257

    while True:
        menu:
            "Spectate other sparring matches":
                jump day_three_spectate
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_three_Player_room')",
                    "bg_classroom": "renpy.jump('day_three_classroom')",
                    "bg_danger": "renpy.jump('day_three_danger')",
                    "bg_lockers": "renpy.jump('day_three_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_three_locker:
    $ lights_on = True
    $ door_locked = False
    $ shower_steam = False
    
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_258

    while True:
        menu:
            "Shower":
                jump day_three_take_shower
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_three_Player_room')",
                    "bg_classroom": "renpy.jump('day_three_classroom')",
                    "bg_danger": "renpy.jump('day_three_danger')",
                    "bg_lockers": "renpy.jump('day_three_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_three_afternoon_class:
    $ Player.History.update("day_three_afternoon_class")

    call add_Characters(Laura) from _call_add_Characters_64

    "You see [Laura.name] come in and take a seat alone at the back of the room."

    call send_Characters(Laura, "hold") from _call_send_Characters_195

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2
    
    $ lighting = "evening"

    $ fade_in_from_black(0.4)

    "You head to the Danger Room for your combat lesson."

    call set_the_scene(location = "bg_danger") from _call_set_the_scene_259

    jump day_three_combat_lesson

label day_three_spectate:
    $ Player.History.update("day_three_spectate")

    "You spend the last of your time before your session with [Laura.name] spectating various scenarios and matches."
    "You ask around for pointers and try to cram every possible nugget of information so [Laura.name] doesn't end up killing you (accidentally)."

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2

    $ lighting = "evening"

    $ fade_in_from_black(0.4)

    "Soon it's time for your lesson."

    jump day_three_combat_lesson

label day_three_take_shower:
    $ Player.History.update("day_three_take_shower")

    "You take a quick shower."

    $ Player.showering = True
    $ shower_steam = True
            
    pause 5.0

    $ fade_to_black(0.4)

    pause 2.0

    $ Player.showering = False

    $ time_index = 2
    
    $ lighting = "evening"

    $ fade_in_from_black(0.4)

    "You get dressed and head to the Danger Room for your combat lesson."

    call set_the_scene(location = "bg_danger") from _call_set_the_scene_260

    jump day_three_combat_lesson

label day_three_combat_lesson:
    "You stretch as you wait for [Laura.name] to arrive."

    call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_196

    if Player.History.check("day_three_spectate") or Player.History.check("day_two_train"):
        if Player.History.check("day_three_spectate"):
            ch_Laura "What do you think you were doing?"
        else:
            ch_Laura "What do you think you were doing yesterday?"

        ch_Player "Uh. . . what?"
        
        if Player.History.check("day_three_spectate"):
            ch_Laura "I saw you watching scenarios."
        else:
            ch_Laura "When you came here."

        ch_Player "Oh, I just thought I'd try preparing for today's session."

        if Player.History.check("day_three_spectate") and Player.History.check("day_two_train"):
            ch_Player "I was also here yesterday to actually workout."
        
        ch_Player "You know, try and familiarize myself with the basics to make up for my late start."
        
        "You feel a bit proud of yourself."

        $ Laura.change_face("angry1")

        ch_Laura "So, you tried sabotaging yourself on purpose?"
        ch_Player "I. . . wait, how was I sabotaging myself?"
        ch_Laura "Who was teaching you those basics?"

        $ Laura.change_face("furious")

        ch_Player "Well, I asked around for tips and pointers, it was more than one person."
        ch_Laura "So you learned the {i}basics{/i} from who knows how many people."
        ch_Laura "All of whom have different powers, combat experiences, fighting styles, levels of conditioning. . ."
        "She continues rattling off reasons why what you did was stupid."

        $ Laura.change_face("perplexed")

        ch_Player "Okay, okay, I get it. Honestly I just wanted a headstart so I didn't look like a fool in front of you. . ."

        $ Laura.change_face("angry1")

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_892
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_893

        ch_Laura "If you've developed any bad habits, I {i}will{/i} beat them out of you."

        $ Laura.mouth = "smirk"

        pause 1.0

        $ Laura.change_face("neutral")

        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_894
    else:
        $ Laura.change_face("confused1")

        ch_Player "Hey, [Laura.name], I'm ready to get started."
        ch_Laura "No, you are not."
        ch_Player "Wha. . ."

    ch_Laura "We will start by warming up."

    $ fade_to_black(0.4)
    
    "Apparently a 'warm-up' for [Laura.name] is an intense full-body exercise lasting nearly an hour."
    "By the end, you already feel gassed."
    "[Laura.name] finally starts teaching you basic fighting concepts and techniques."

    $ fade_in_from_black(0.4)

    ch_Laura ". . . No. Stagger your feet like this, arms up higher. . ."
    "She smacks one of your arms that you weren't holding in the right position."

    $ Laura.change_face("surprised2", blush = 1)

    if not Laura.History.check("was_warned_about_Player_power"):
        pause 1.0
        
        $ Laura.change_face("appalled1", blush = 1)

    "[Laura.name] shudders."

    call Laura_unsheathes_claws from _call_Laura_unsheathes_claws_6

    "She reflexively unsheathes her claws and gets into a fighting stance."
    
    if Laura.History.check("was_warned_about_Player_power"):
        $ Laura.change_face("angry1", blush = 1)

        ch_Player "Are you okay? I did say it would feel a bit weird."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_895
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_896
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_897

        ch_Laura "That felt. . . {size=-5}dangerous{/size}."
    else:
        $ Laura.change_face("furious", blush = 1)

        ch_Laura "What was that?"

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_898
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_899

        ch_Player "Oh shit, sorry! I forgot to tell you touching me might be a bit weird. Can't really control my powers. . ."
        "[Laura.name] glares at you."

    pause 1.0

    call Laura_sheathes_claws from _call_Laura_sheathes_claws_6

    pause 1.0

    $ Laura.change_face("neutral", mouth = "frown")

    "You can tell the accidental touch is bothering her."
    "The lesson continues, and you're not sure if this is her normal tempo or she's going harder on purpose."
    ch_Laura "Enough, we're moving on to scenarios now."
    ch_Player "Wai. . ."
    "Things suddenly take a turn you weren't expecting, as [Laura.name] shows you exactly why this is called the 'Danger Room'."

    $ fade_to_black(0.4)

    $ count = 7

    while count > 0:
        $ dice_roll = renpy.random.randint(1, 2)

        $ x = renpy.random.random()*0.7 + 0.15
        $ y = renpy.random.random()*0.7 + 0.15

        if dice_roll == 1:
            show expression "images/effects/clang.webp" as clang onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0
        elif dice_roll == 2:
            show expression "images/effects/bzilll.webp" as bzilll onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0

        $ renpy.pause(renpy.random.random(), hard = True)

        $ count -= 1

    "Within the first five seconds, a robot arm nearly decapitates you, and a laser stops just short of slicing your leg off." 
    "Surprised by your lack of ability, [Laura.name] drastically tones down the difficulty settings."
    "After hours of near misses and painful mistakes, she decides to shift the focus back to techniques."

    $ fade_in_from_black(0.4)

    $ Laura.change_face("angry1")

    "The constant torture is really starting to fray your nerves."

    menu:
        "Grit your teeth and push through the pain":
            "You force yourself through the various exercises [Laura.name] has you perform."

            $ Laura.change_face("confused1")

            "You realize you've gone a bit too far when you wipe out and hit the ground hard."
            "[Laura.name] just stands there waiting for you to get up."

            $ Laura.change_face("angry2")

            ch_Laura "That's it?"
            ch_Laura "Do you not even know your own limits?"
            ch_Laura "At least you have the willpower to go past them, unlike most of the people at this school."

            call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_900
            call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_901
        "You've hit your limit":
            $ Laura.change_face("angry1")

            ch_Player "*huff*. . . I. . . don't think I can keep going. . . *huff*"
            ch_Laura "That's it? Why is every student at this school so weak?"

    ch_Player "Really?!"
    ch_Player "I don't know what kind of hellish training you must've been put through, but any normal person would be exhausted after all of that. . ."
    ch_Player "I swear, I almost died like 5 times over." 

    $ Laura.change_face("suspicious2")

    ch_Laura "'Normal person'?"

    $ Laura.change_face("confused1", mouth = "frown")

    ch_Laura "It was only 3 hours, was this tempo not expected of you when you were a child?"
    ch_Player "Absolutely not!"
    ch_Player "My parents didn't try to kill me when I was a child!" 

    if Player.scholarship == "athletic":
        ch_Player "I've had my fair share of painful workouts."
        ch_Player "But holy shit."
        ch_Player "Making a child do something like that is beyond fucked. . ."
    else:
        ch_Player "I stayed in pretty good shape during school."
        ch_Player "But making a child do things like that. . ."

    $ Laura.change_face("angry1")

    ch_Player "Goddamnit. . . Is this my life now?"
    ch_Player "Constantly having people try to kill me?"

    $ Laura.change_face("confused1", mouth = "frown")

    ch_Player "I mean for fuck's sake! I grew up in a normal home, had a loving family, and had normal friends."
    ch_Player "Never once did I worry about getting killed. . . until these past few days. . ."

    $ Laura.change_face("angry1", eyes = "squint")

    "[Laura.name] stares at you."
    "It's a little. . . uncomfortable."

    $ Laura.change_face("furious", blush = 1)

    "Her expression turns to anger."
    ch_Laura "'Normal,' huh."
    ch_Laura "We're done. You obviously can't continue."

    $ Laura.left_arm_pose = 2
    $ Laura.blush = 0

    ch_Laura "Give me your phone."
    
    $ Laura.left_arm_pose = 1

    pause 2.0

    $ Laura.left_arm_pose = 2

    "You hand her your phone. She enters her number and hands it back."
    
    $ Laura.left_arm_pose = 1

    ch_Laura "Text me when you're ready for the next session."
    "She briefly shows you how to train properly on your own, then leaves."

    call send_Characters(Laura, "hold") from _call_send_Characters_197

    jump day_three_after_lesson

label day_three_after_lesson:
    $ fade_to_black(0.4)

    pause 1.0

    $ time_index = 3
    
    $ lighting = "night"

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0

    $ fade_in_from_black(0.4)

    "As you get ready to leave, you see [Kurt.name] approaching you."

    call send_Characters(Kurt, "bg_danger", behavior = "training") from _call_send_Characters_198

    ch_Kurt "I'm glad to see you survived."
    ch_Kurt "It seems you have a knack for leaving girls angry and confused."
    ch_Player "Yeah. . . Maybe it's an as-yet-undiscovered power of mine."

    $ Kurt.change_face("neutral", brows = "furrowed")

    "[Kurt.name] looks at you with a thoughtful expression."
    ch_Player "Don't look at me like that, it's not like I'm doing it on purpose."
    "You explain what happened."

    $ Kurt.change_face("neutral")

    ch_Kurt "You really need to be more careful viz your vords."
    ch_Kurt "'Normal' is. . . vell not everyone here has ever been able to feel 'normal.'"

    $ Kurt.change_face("neutral", brows = "furrowed")

    ch_Kurt "Especially zat one."

    $ Kurt.change_face("confused")

    ch_Kurt "Not only is she probably zee fiercest fighter in zee mansion. . . viz actual combat experience."
    ch_Kurt "A standard vorkout for her would put any of us in zee ground, as I'm sure you just learned."
    ch_Player "Yeah, I just kind of broke down at the end. . ."
    ch_Player "And. . . I know. I'm just not used to navigating all the baggage that comes with having superpowers. . ."

    $ Kurt.change_face("sad")

    ch_Kurt "You'll learn. . . one vay or anozer."
    ch_Kurt "Gute Nacht, [Player.first_name]."

    call send_Characters(Kurt, "hold") from _call_send_Characters_199

    jump day_three_meet_Jean

label day_three_meet_Jean:
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_261

    "As you're heading back to your room, someone calls out to you."

    $ Jean.name = "???"

    ch_Jean "Hey!"
    "You look around to see who it is."

    call change_Outfit(Jean, Jean.Wardrobe.Outfits["Casual 1"], instant = True) from _call_change_Outfit_35
    
    call add_Characters(Jean) from _call_add_Characters_65

    ch_Jean "You're the new kid, right?"
    ch_Player "Uh, hey, yeah that's me. Name's [Player.full_name]."

    $ Jean.name = "Jean"

    ch_Jean "Hi [Player.first_name], I'm Jean!" 

    $ Jean.change_face("happy")

    ch_Player "Nice to meet you, [Jean.name]." 

    $ Jean.change_face("smirk2")

    pause 1.0

    $ Jean.change_face("worried1")

    ch_Jean "I saw you wipe out pretty hard during that training session earlier. . ." 
    ch_Jean "You okay?"
    ch_Jean "I know this must all be a lot for you."

    menu:
        extend ""
        "Yeah, I'm okay. . . it is a lot to be honest.":
            $ Jean.change_face("sad") 
            
            call change_Girl_stat(Jean, "love", 5) from _call_change_Girl_stat_902
        "Nah, I'm not really okay. . . but I'll live.":
            $ Jean.change_face("confused1") 
        "I'm okay, and it is a lot, but I'll adapt. I have to.":
            $ Jean.change_face("smirk2") 
            
            call change_Girl_stat(Jean, "trust", 5) from _call_change_Girl_stat_903

    $ Jean.change_face("neutral")

    ch_Jean "Well. . . I'm usually pretty busy so I don't know if you'll see me around too much. . ."

    $ Jean.change_face("worried1", mouth = "lipbite")

    ch_Jean "But if you do, feel free to ask if you need help with anything."

    $ Jean.change_face("sly")

    ch_Jean "So you don't get quite so beat up next time. . ."
    ch_Player "Thanks, [Jean.name]."
    ch_Player "I appreciate that."

    $ Jean.change_face("happy")

    ch_Jean "You're welcome!"

    $ Jean.change_face("smirk2")

    ch_Jean "I gotta go now, nice meeting you!"

    call send_Characters(Jean, "hold") from _call_send_Characters_200
    call set_the_scene(location = Player.home) from _call_set_the_scene_262

    jump day_three_end

label day_three_end:
    $ sandbox = True

    $ unlocked_Characters.append(Jean)

    $ Contacts.append(Laura)

    call send_Characters(Rogue, Rogue.home) from _call_send_Characters_201
    call send_Characters(Laura, Laura.home) from _call_send_Characters_202
    call send_Characters(Jean, "hold") from _call_send_Characters_203
    call send_Characters(Kurt, Kurt.home) from _call_send_Characters_204
    call send_Characters(Charles, Charles.home) from _call_send_Characters_205
    
    $ Laura.History.update("trained_with_Player")

    $ Jean.History.update("met")

    $ Player.History.update("trained")

    $ time_index = 3
    
    $ lighting = "night"

    $ clock = Player.max_stamina

    $ available_locations = unlocked_locations

    $ EventScheduler.update_conditions()

    call refresh_season_content from _call_refresh_season_content_3

    if black_screen:
        $ fade_in_from_black(0.4)

    call move_location(Player.home) from _call_move_location_37

    return