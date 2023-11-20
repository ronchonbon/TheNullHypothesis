label day_two_intro:
    call start_new_day from _call_start_new_day_6

    $ active_NPCs.append(Kurt)

    call send_Characters(Kurt, "hold") from _call_send_Characters_206
    
    # $ Rogue.Wardrobe.indoor_Outfit = Rogue.Wardrobe.Outfits["Casual 2"]
    # $ Rogue.Wardrobe.outdoor_Outfit = Rogue.Wardrobe.Outfits["Casual 2"]

    call set_Character_Outfits from _call_set_Character_Outfits_9

    $ check_predicted_images()

    call refresh_season_content from _call_refresh_season_content_7

    "You have a deep, dreamless sleep."

    $ Player.messy_bed = True

    call set_the_scene(location = Player.home) from _call_set_the_scene_263

    "You wake up feeling a bit delirious, initially not recognizing your surroundings."
    "Then you remember the events of yesterday."
    ch_Player "Damn. . . I didn't even take my shoes off last night."
    "You get out of bed and start getting ready for class."
        
    play music "sounds/music/Day to Day.ogg" fadeout 1.0 fadein 1.0

    call knock_on_door(times = 2) from _call_knock_on_door_30
    
    "As you brush your teeth, you hear a knock at the door."
    ch_Rogue "[Player.first_name], you awake yet?"
    ch_Player "Yep, be right there!"
    "You get into a fresh change of clothes and open the door."

    call send_Characters(Rogue, "bg_hallway") from _call_send_Characters_207

    $ Rogue.change_face("confused1", mouth = "smirk")

    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_264

    $ Player.messy_bed = False

    ch_Rogue "Good mornin', [Rogue.Player_petname]. How was your first night at the Institute?"

    menu:
        extend ""
        "Too good, that bed is amazing. I'm just worried about what my family must be thinking right now. I feel a bit guilty.":
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_904
            
            $ Rogue.change_face("worried1")
          
            ch_Rogue "Ah know how you feel. But trust me, you're doin' them a favor by stayin' away."
        "I slept like a rock. The beds in this place are really something else.":
            ch_Rogue "They sure are comfortable. We're lucky the Prof is so generous."

    $ Rogue.change_face("neutral")

    ch_Player "Anyway, what brings you here this morning?"

    $ Rogue.change_face("smirk2")

    ch_Rogue "Well, we're in the same lecture this morning, and our first tutoring session will be right after class."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah just thought we could walk to class together. . ."

    $ Rogue.change_face("happy")

    ch_Player "Sounds good to me, lead the way."

    call hide_Character(Rogue) from _call_hide_Character_39

    $ fade_to_black(0.4)

    "You exchange some small talk with [Rogue.name] on the way to class."

    jump day_two_morning_class

label day_two_morning_class:
    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_265
    call add_Characters(Rogue) from _call_add_Characters_66

    $ Rogue.change_face("smirk2")

    "You make it to class on time."
    "[Rogue.name] takes a seat next to you."
    "You see a bunch of other students, none of whom you recognize.{p}There's even a guy who looks like a blue demon."
    "[Ororo.name] also seems to be absent."
    ch_Player "Hey [Rogue.name], where's [Ororo.name]? I thought she'd be teaching today."
    
    $ Rogue.change_face("confused1", mouth = "smirk")
    
    ch_Rogue "She was called out for a mission, somethin' urgent. Pretty common with the X-Men actually."
    
    $ Rogue.change_face("smirk2")
    
    ch_Rogue "Don't you worry much about her, she's not a team member for nothin'."
    "As class begins, the substitute starts by briefly introducing you as a new student."
    "Hushed conversation can be heard throughout the room, no doubt about all the rumors surrounding your power."
    "The lecture finally begins. You quickly realize Mutant Physiology might be more interesting than expected with all of the unique powers out there."

    $ Rogue.change_face(brows = "neutral", eyes = "down", mouth = "lipbite", blush = 1)

    "Out of the corner of your eye, you notice [Rogue.name] fidgeting a bit throughout the lesson."    
    "She glances at your hands more than once as you take notes." 

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 1
    
    $ lighting = "day"

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Player "Now that class is over, where were we gonna. . ."

    call phone_buzz from _call_phone_buzz_8
        
    "You're interrupted by [Rogue.name]'s phone buzzing."

    $ Rogue.change_face("worried1", eyes = "down")
    
    pause 1.0

    $ Rogue.change_face("worried1")

    ch_Rogue "Darn, sorry [Rogue.Player_petname]. It's lookin' like we'll have to push that tutoring session to the evenin'. Ah'll meet ya at your room later?"
    
    call send_Characters(Rogue, "hold") from _call_send_Characters_208

    "She hurries off."

    $ Rogue.change_face("neutral")

    $ Laura.location = "bg_lockers"

    jump day_two_classroom_menu
        
label day_two_Player_room:
    $ lights_on = True
    $ door_locked = False

    call set_the_scene(location = Player.home) from _call_set_the_scene_266

    while True:
        menu:
            "Prepare for tutoring session":
                jump day_two_study
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_two_Player_room')",
                    "bg_classroom": "renpy.jump('day_two_classroom')",
                    "bg_danger": "renpy.jump('day_two_danger')",
                    "bg_lockers": "renpy.jump('day_two_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_two_classroom:
    $ lights_on = True
    $ door_locked = False
    
    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_267

    while True:
        menu day_two_classroom_menu:
            "Take afternoon class":
                jump day_two_afternoon_class
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_two_Player_room')",
                    "bg_classroom": "renpy.jump('day_two_classroom')",
                    "bg_danger": "renpy.jump('day_two_danger')",
                    "bg_lockers": "renpy.jump('day_two_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_two_danger:
    $ lights_on = True
    $ door_locked = False
    
    call set_the_scene(location = "bg_danger") from _call_set_the_scene_268

    while True:
        menu:
            "Prepare for combat lesson":
                jump day_two_train
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_two_Player_room')",
                    "bg_classroom": "renpy.jump('day_two_classroom')",
                    "bg_danger": "renpy.jump('day_two_danger')",
                    "bg_lockers": "renpy.jump('day_two_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_two_locker:
    $ lights_on = True
    $ door_locked = False
    $ shower_steam = False

    if not Player.History.check("ran_into_Laura"):
        $ Laura.location = "nearby"
    
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_269

    if not Player.History.check("ran_into_Laura"):
        $ shower_steam = True

        call change_Outfit(Laura, Laura.Wardrobe.swimming_Outfit, instant = True) from _call_change_Outfit_36
        # call try_on(Laura, Laura.Wardrobe.Clothes["towel"], instant = True) from _call_try_on_13

        "As you head over to the showers, you run into [Laura.name]."

        call add_Characters(Laura) from _call_add_Characters_67

        ch_Player "Hey, [Laura.name]. . ."

        $ Laura.change_face("neutral", eyes = "right")

        "She walks right by, only sparing you a passing glance."

        call send_Characters(Laura, "hold") from _call_send_Characters_209

        $ Player.History.update("ran_into_Laura")

    while True:
        menu:
            "Shower":
                jump day_two_take_shower
            "Wait (locked)":
                pass
            "Leave":
                $ available_locations = {
                    Player.home: "renpy.jump('day_two_Player_room')",
                    "bg_classroom": "renpy.jump('day_two_classroom')",
                    "bg_danger": "renpy.jump('day_two_danger')",
                    "bg_lockers": "renpy.jump('day_two_locker')"}

                $ current_Player_menu_page = "map"

                call screen Player_menu()

label day_two_study:
    $ Player.History.update("day_two_study")

    "You start by reviewing your notes from today's lecture and going over the study guide."
    "You spend the rest of your time organizing your textbooks and papers so it's all ready for the tutoring session."

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2
    
    $ lighting = "evening"

    $ fade_in_from_black(0.4)
        
    call knock_on_door(times = 2) from _call_knock_on_door_31

    "You hear a knock at your door."

    jump day_two_tutoring_session

label day_two_afternoon_class:
    $ Player.History.update("day_two_afternoon_class")

    call add_Characters(Laura) from _call_add_Characters_68

    "You see [Laura.name] come in and take a seat alone at the back of the room."

    call send_Characters(Laura, "hold") from _call_send_Characters_210

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2
    
    $ lighting = "evening"

    $ fade_in_from_black(0.4)

    "You head back to your room."

    jump day_two_tutoring_session

label day_two_train:
    $ Player.History.update("day_two_train")

    "You do some stretching and calisthenics as a warmup."
    "You spend the rest of your time asking around for pointers and practicing basic sparring techniques."

    $ fade_to_black(0.4)

    pause 2.0

    $ time_index = 2
    
    $ lighting = "evening"

    $ fade_in_from_black(0.4)

    "You head back to the dorms for your tutoring session."

    jump day_two_tutoring_session

label day_two_take_shower:
    $ Player.History.update("day_two_take_shower")

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

    "You get dressed and head back to the dorms for your tutoring session."

    jump day_two_tutoring_session

label day_two_tutoring_session:
    call send_Characters(Rogue, "bg_hallway") from _call_send_Characters_211
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_270

    "You see [Rogue.name] waiting in the hallway outside your room."
    
    $ Rogue.change_face("pleased1")
    
    ch_Rogue "Hey [Rogue.Player_petname], ready to get started?"
    
    $ Rogue.change_face("smirk2")
    
    ch_Player "Yep! Come on in."

    call set_the_scene(location = Player.home) from _call_set_the_scene_271
    call add_Characters(Rogue) from _call_add_Characters_69

    if Player.History.check("day_two_study"):
        $ Rogue.change_face("pleased2")

        ch_Rogue "Oh, looks like everything's already set up."
        
        $ Rogue.change_face("confused1", mouth = "smirk")
        
        "She fixes you with an interested gaze, seemingly impressed."

        $ Rogue.change_face("pleased1")

        ch_Player "Yeah. . . Just wanted to get a bit of a head start."
        
        $ Rogue.change_face("smirk2")
        
        if Player.scholarship == "academic":
            call change_Girl_stat(Rogue, "love", large_stat) from _call_change_Girl_stat_641
            
            ch_Player "I know how important it is to stay on top of my studies. Plus, I enjoy it."
            ch_Player "It helps. . . distract me. . ."
        else:
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_908

            ch_Player "I wasn't a very good student before coming here, thought this was a chance to fix that."
    else:
        ch_Player "Sorry, I didn't get a chance to organize things yet. I got a bit distracted."
        ch_Rogue "Don't worry about it none, it'll only take a few minutes."
        "You and [Rogue.name] start compiling your textbooks, class notes, and study guides."
        ch_Rogue "That oughta do it."

    if Player.scholarship == "artistic":
        $ Rogue.change_face("pleased1", eyes = "down")

        ch_Rogue "Ah noticed you have calluses on yer hands. . ."

        $ Rogue.change_face("smirk2")

        menu:
            extend ""
            "They're from playing guitar. (artistic)":
                call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_910

                ch_Player "Doesn't seem like my guitar made it to the mansion with me, though. . ."

                $ Rogue.change_face("worried1")

                ch_Rogue "Ah'm sorry to hear that."
                ch_Rogue "Well, if ya ever pick a new one up. . ."

                $ Rogue.change_face("worried1", eyes = "down", blush = 1)

                ch_Rogue ". . . maybe you could play for me sometime."
                ch_Player "Sounds like a deal."
            "Yeah. . . I like to draw. (artistic)":
                call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_657
                
                ch_Player "Doesn't seem like any of my supplies made it to the mansion with me, though. . ."

                $ Rogue.change_face("worried1")

                ch_Rogue "Sorry to hear that."
                ch_Rogue "If ya ever do get to drawin' again. . ."
                
                $ Rogue.change_face("worried1", eyes = "down", blush = 1)
                
                ch_Rogue "Maybe ya could draw somethin' for me."
                ch_Player "Definitely."
                
        $ Rogue.change_face("pleased1")

        pause 1.0

        $ Rogue.change_face("happy")

        ch_Rogue "Ah'll look forward to it."

        $ Rogue.change_face("smirk2")

        ch_Rogue "Sorry, ah got sidetracked. . . let's get started."

    $ Rogue.change_face("smirk2")

    "The tutoring session starts."

    $ fade_to_black(0.4)

    "Thankfully, since it's only a few weeks into the quarter you haven't missed too much."
    "[Rogue.name] seems to know her stuff, and things proceed smoothly until. . ."

    $ fade_in_from_black(0.4)

    ch_Rogue ". . . Yeah, exactly. Why don't ya try those practice questions real quick. . ."

    $ Rogue.eyes = "down"

    "Again, you spot [Rogue.name] being fidgety.{p}She doesn't think you notice as she stares intently at your hands while you work."
    "You put down your pen and turn to her."
    ch_Player "Hey, so about when we met. . ."

    $ Rogue.change_face("surprised2", blush = 1)

    "[Rogue.name] snaps out of it, realizes what you're about to ask, and interrupts you."
    ch_Rogue "*gasp*"
    ch_Rogue "Bythewaydo\nyahaveaHumHum\naccount?"

    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1)

    ch_Player "Uhhh. . . a Hum-what account?"
    "[Rogue.name] regains her composure."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "HumHum. It's a social media app made by the Institute. All the students here and even some of the X-Men use it."
    
    $ Rogue.change_face("worried1")

    ch_Player "Haven't heard of it. Honestly, I barely know how to work this fancy phone."
    
    # $ Rogue.right_arm_pose = 2
    $ Rogue.change_face("smirk2")

    ch_Rogue "Gimme, ah'll set up an account for you."
    
    $ Rogue.eyes = "down"

    "You hand her your new phone."
    
    # $ Rogue.right_arm_pose = 1

    pause 1.0

    $ Rogue.change_face("confused1", eyes = "down")

    pause 1.0

    $ Rogue.change_face("confused1")

    pause 1.0

    "She looks up at you, a bit bewildered as to how you managed to crack the screen, but doesn't mention it."

    $ Rogue.change_face("neutral", eyes = "down")
    
    pause 2.0

    $ Rogue.change_face("happy")

    ch_Rogue "Done. Ah added myself as your friend and also put my number in there in case you get any questions while studyin'."

    # $ Rogue.right_arm_pose = 2

    pause 1.0

    # $ Rogue.right_arm_pose = 1
    $ Rogue.change_face("smirk2")

    ch_Player "Thanks, [Rogue.name]. I appreciate it."

    $ humhum_available = True

    jump day_two_after_tutoring

label day_two_after_tutoring:
    ch_Player "So. . ."

    $ Rogue.change_face("worried1")

    "[Rogue.name] looks conflicted about what to say next.{p}Finally, she caves."

    if Rogue.History.check("Player_looked_at_glove"):
        # $ Rogue.left_arm_pose = 2

        ch_Rogue "Ah know you realized what ah was meanin' to ask when we first met. . ."
        
        $ Rogue.change_face("worried2", blush = 1)
        
        ch_Player "I did, y-"
        ch_Rogue "-and ah know it's kinda weird!"
        ch_Player "I don't-"

        $ Rogue.change_face("worried3")

        ch_Rogue "Ahwasjustwonderin'if\nmaybeahcouldtrytouchin'\nyousinceyou'reimmune\nanditwon'thurtyou."    
    else:
        # $ Rogue.left_arm_pose = 2

        ch_Rogue "So ah told you how my power works when we first met. . ."
        ch_Player "Right."
        ch_Rogue ". . . and about how ah can't control it too well. . ."
        ch_Player "Mhm."
        ch_Rogue ". . . and that ah haven't touched anyone in a really long time. . ."
        ch_Rogue "Ah was just wonderin'. . .{p}{size=-5}if maybe{/size}. . .{p}{size=-10}ah could try touchin' you{/size}. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)
    # $ Rogue.left_arm_pose = 1

    menu:
        extend ""
        "I don't know. . . I'm sorry, I'm just worried about getting hurt.":
            call change_Girl_stat(Rogue, "love", -small_stat) from _call_change_Girl_stat_658
            call change_Girl_stat(Rogue, "trust", small_stat) from _call_change_Girl_stat_659

            $ Rogue.change_face("sad")

            ch_Rogue "Please? Ah promise it'll be super quick."
            ch_Rogue "If anythin' goes wrong ah'll stop immediately."

            $ Rogue.change_face("pleased2")

            ch_Player "Okay, okay, we can give it a try."
        "Fine by me!":
            call change_Girl_stat(Rogue, "love", small_stat) from _call_change_Girl_stat_660
            call change_Girl_stat(Rogue, "trust", -medium_stat) from _call_change_Girl_stat_670
        
            "You stick your hand out for her to touch."

            $ Rogue.change_face("perplexed", blush = 1)

            ch_Rogue "Uhm. . . [Rogue.Player_petname], are you sure?"
            ch_Player "100\%."
        "This means a lot to you, doesn't it? Sure, I'm willing to try.":
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_676
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_677
            
            $ Rogue.change_face("surprised2")

            ch_Rogue "Really?!?!"
            ch_Player "Of course, it's worth a shot."

    $ Rogue.change_face("pleased2", mouth = "smile")

    ch_Rogue "Thank you!"

    $ Rogue.change_face("smirk2")
    # $ Rogue.right_arm_pose = 2

    pause 1.0

    call take_off(Rogue, "gloves") from _call_take_off_10

    pause 1.0
    
    menu:
        extend ""
        "You give her a reassuring smile as she reaches out to touch your hand":
            $ Rogue.eyes = "closed"

            pause 1.0

            $ Rogue.change_face("pleased2", blush = 1)

            "A shudder runs up [Rogue.name]'s arm."

            $ Rogue.change_face("pleased2", mouth = "smile", blush = 1)

            "When she realizes you aren't dying, her face lights up with pure joy."
            
            pause 1.0

            $ Rogue.change_face("sad", eyes = "wide", mouth = "smirk", blush = 1)

            ch_Rogue "Do you feel alright?"
            
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_682

            ch_Player "I feel great. I'm holding hands with a beautiful girl, after all."

            call change_Girl_stat(Rogue, "love", large_stat) from _call_change_Girl_stat_915

            $ Rogue.change_face("surprised2", blush = 1)
            # $ Rogue.right_arm_pose = 1

            "[Rogue.name] lets go of your hand and stands up, looking quite flustered."
            
            $ Rogue.change_face("surprised2", eyes = "right", mouth = "lipbite", blush = 1)
            
            ch_Rogue ". . . Well, this was a productive session."
            ch_Rogue "Ah'll see you tomorrow."

            call send_Characters(Rogue, "hold") from _call_send_Characters_212

            "She packs up and leaves in a hurry."
        "Make her jump by faking convulsions. Pranks are funny, right?":
            $ Rogue.change_face("worried4")
            # $ Rogue.right_arm_pose = 1

            "[Rogue.name] looks horrified and immediately removes her hand."

            $ Rogue.change_face("worried3")

            ch_Rogue "Oh lord, [Rogue.Player_petname], are you okay?!"
            "You chuckle to yourself like the dumbass you are."
            
            $ Rogue.change_face("furious")
            
            call change_Girl_stat(Rogue, "love", -large_stat) from _call_change_Girl_stat_918
            call change_Girl_stat(Rogue, "trust", -massive_stat) from _call_change_Girl_stat_919

            ch_Rogue "Well, ah'm glad someone's havin' fun."
            "She grabs her things and walks out of your room in a huff."

            call send_Characters(Rogue, "hold") from _call_send_Characters_213

            "Good job, ass."

            $ Rogue.History.update("Player_faked_injury")
            
    ch_Player "[Rogue.name], wait. . ."

    jump meet_Kurt

label meet_Kurt:
    call knock_on_door(times = 2) from _call_knock_on_door_32

    "You hear a knock at the door."
    "You get up and open it."

    $ Kurt.name = "???"

    call add_Characters(Kurt) from _call_add_Characters_70

    ch_Player "Gah! What the hell!"

    $ Kurt.change_face("happy")

    "You realize it's the demon you saw in class earlier today."

    ch_Kurt "Hallo, [Player.first_name], right?"
    ch_Player "Yeah, sorry about that. I'm not used to uh. . . You just look uh. . . different?"

    $ Kurt.name = "Kurt"

    ch_Kurt "You can call me Kurt."
    ch_Player "Nice to meet you, [Kurt.name]."

    if Player.visible_mutation:
        ch_Kurt "You look a little different yourself."

        if Player.skin_color in ["blue", "green", "red"]:
            "You look down at your new skin color."
        elif Player.ears:
            "You again reach up to feel your ears."
        
        ch_Player "Yeah. . . good point."
    else:
        ch_Kurt "You'll get used to it, plenty of 'different' people around here."
        ch_Player "Can't argue with that."

    $ Kurt.change_face("neutral")

    if not Rogue.History.check("Player_faked_injury"):
        $ Kurt.change_face("confused")

        ch_Kurt "Übrigens, I passed [Rogue.name] on my vay here. She vas blushing pretty hard."
        ch_Kurt "Vat exactly did you do?"
        ch_Player "Nothing bad, I swear!"

        $ Kurt.change_face("neutral")

        ch_Player "She just tried touching my hand to see if my immunity really worked."
        ch_Player "She got a bit flustered and. . . left?"
        ch_Kurt "I see. . ."
    else:
        $ Kurt.change_face("angry1")
        
        ch_Kurt "Übrigens, I passed [Rogue.name] on my vay here. She looked pretty pissed."
        ch_Kurt "Vat exactly did you do?"
        ch_Player "I know, I feel bad. It was a stupid joke."
        ch_Player "I pretended like it hurt when she tried touching my hand. . ."

        $ Kurt.change_face("surprised")

        ch_Kurt "Schön blöd, is something wrong viz your brain?"
        ch_Kurt "Don't have to be at zis school for a day to know zat's a touchy subject for her."
        ch_Player "I know, I know. I'm a dumbass. . ."

        $ Kurt.change_face("neutral")

        ch_Kurt "You better apologize to zee fraulein tomorrow."
        ch_Player "Way ahead of you."

    ch_Kurt "So zat power of yours really vorks as advertised zen?"
    ch_Player "So it seems."
    ch_Kurt "Huh. Anyvay, I came by to see if you vanted a tour of zee more entertaining spots around town."
    ch_Player "Sounds great! Lead the way."

    call hide_Character(Kurt) from _call_hide_Character_40

    "You follow [Kurt.name] outside."

    jump day_two_tour

label day_two_tour:
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_272

    pause 1.0

    call set_the_scene(location = "bg_mall") from _call_set_the_scene_273
    call add_Characters(Kurt) from _call_add_Characters_71

    ch_Kurt "Zis is zee mall, it closes pretty soon but we can still valk around for a bit."
    ch_Kurt "You can get new clothing items here."
    ch_Kurt "Zere are other stores nearby vere you can get accessories."

    call hide_Character(Kurt) from _call_hide_Character_41
    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_274
    call add_Characters(Kurt) from _call_add_Characters_72

    ch_Kurt "Zey have pretty decent food here, nice place to take a date."

    call hide_Character(Kurt) from _call_hide_Character_42
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_275
    call add_Characters(Kurt) from _call_add_Characters_73

    ch_Kurt "Of course zere is a movie theater."
    ch_Kurt "Zat's about it, let's head back!"

    call hide_Character(Kurt) from _call_hide_Character_43
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_276

    pause 1.0

    $ time_index = 3
    
    $ lighting = "night"

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0

    pause 1.0

    call set_the_scene(location = Player.home) from _call_set_the_scene_277
    call add_Characters(Kurt) from _call_add_Characters_74

    jump day_two_tutorial

label day_two_tutorial:
    $ belt_disabled = True

    ch_Player "One last thing. . . can you teach me how to use this damn phone?"
    ch_Kurt "Vat? Zee Professor didn't tell you how to use it?"
    "[Kurt.name] snatches your phone and gives you a dumbfounded look."

    $ Kurt.change_face("confused")

    ch_Kurt "Dude, how did you manage to break it?"
    ch_Player "I don't want to talk about it. . ."
    ch_Kurt "Fine, here's how it vorks."

    $ Kurt.change_face("neutral")

    $ phone_interactable = False

    show screen phone_screen()

    ch_Kurt "Here's zee home screen."
    ch_Kurt "You can see zee latest HumHum feed and zee rest of your apps."
    ch_Kurt "Zee button vich looks like a phone - zat is vere you can find your contacts and start a phone call."
    ch_Kurt "Your text messages are zee middle app. Look out for notifications zere."
    ch_Kurt "X-Profile is vere you track your personal progress."

    $ current_home_page = 1

    ch_Kurt "You can look at all your apps on zee next screen."
    ch_Kurt "I sink you can figure out vich app is HumHum."

    $ current_home_page = 0

    $ sandbox = True
    $ Character_picker_disabled = True
    
    ch_Kurt "Your belt is on zee top right of zee screen. From it, you can access your journal, inventory, map, and phone."

    $ sandbox = False
    $ Character_picker_disabled = False

    hide screen phone_screen

    $ phone_interactable = True

    ch_Kurt "Zere, I put in my number and added you on HumHum."
    ch_Kurt "Zat's about it, got it?"
    ch_Player "Yeah, thanks man."

    $ Kurt.change_face("happy")

    ch_Kurt "I'm gonna head out, see you in class tomorrow."
    ch_Player "See ya."

    call send_Characters(Kurt, "hold") from _call_send_Characters_214

    "It's getting pretty late, so you go to bed."

    $ lights_on = False

    $ lighting = "moonlight"

    call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_278

    pause 2.0

    $ fade_to_black(0.4)

    pause 2.0

    jump day_two_end

label day_two_end:
    $ belt_disabled = False
    $ phone_interactable = True
    $ humhum_available = True

    $ unlocked_Characters.append(Kurt)

    $ Contacts.append(Rogue)
    $ Contacts.append(Kurt)
    
    call send_Characters(Rogue, "hold") from _call_send_Characters_215
    call send_Characters(Laura, "hold") from _call_send_Characters_216
    call send_Characters(Kurt, "hold") from _call_send_Characters_217

    $ unlocked_locations.update({"bg_mall": "renpy.call('travel', 'bg_mall')"})

    $ Kurt.name = "Kurt"

    $ Player.History.update("studied")

    $ Rogue.History.update("studied_with_Player")

    jump day_three_intro