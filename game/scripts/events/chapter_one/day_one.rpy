label day_one_intro:
    $ chapter = 1
    $ season = 1

    $ day = 1
    $ season_day = 1
    $ weekday = 6

    $ time_index = 0

    $ lighting = "day"

    python:
        for C in all_Characters:
            C.History.manually_reset("event")
            C.History.manually_reset("season")

    $ Player.History.manually_reset("event")
    $ Player.History.manually_reset("season")

    $ sandbox = False

    $ active_Companions.append(Ororo)
    $ active_Companions.append(Rogue)
    $ active_Companions.append(Laura)

    $ active_NPCs.append(Charles)

    $ Player.location = Player.home

    call send_Characters(Rogue, "hold") from _call_send_Characters_176
    call send_Characters(Laura, "hold") from _call_send_Characters_177
    call send_Characters(Ororo, "hold") from _call_send_Characters_178
    call send_Characters(Charles, "hold") from _call_send_Characters_179
    
    $ Rogue.Wardrobe.indoor_Outfit = Rogue.Wardrobe.Outfits["Casual 1"]
    $ Rogue.Wardrobe.outdoor_Outfit = Rogue.Wardrobe.Outfits["Casual 1"]
    
    # $ Ororo.Wardrobe.indoor_Outfit = Ororo.Wardrobe.Outfits["Casual 2"]
    # $ Ororo.Wardrobe.outdoor_Outfit = Ororo.Wardrobe.Outfits["Casual 2"]

    call set_Character_Outfits from _call_set_Character_Outfits_8

    $ check_predicted_images()

    call refresh_season_content from _call_refresh_season_content_5

    "You awake with a start."
    ch_Player "Oh, thank god, it was just a nightmare. . ."
    ch_Player ". . . Damn, has my bed always felt this good?"

    $ Player.give_trait("messy_bed")
    
    call set_the_scene(location = Player.home) from _call_set_the_scene_241

    "You open your eyes to a strange room. You're wearing fresh clothes you don't recognize."
    "Your old outfit is neatly folded in a pile at the foot of the bed."
    "Next to it is a journal and bag with a note:{p}'Might come in handy.'"
    ch_Player "What the. . . Where. . ."

    if Player.check_traits("visible_mutation"):
        ch_Player "Fuck. . . It wasn't a dream. . ."

    $ Charles.name = "???"

    $ sleeping = True
    $ first_counter = 0

    while sleeping:
        menu:
            extend ""
            "Get out of bed":
                $ sleeping = False
            "Go back to sleep":
                if first_counter == 0:
                    $ fade_to_black(0.4)

                if first_counter < 3:
                    if first_counter == 0:
                        "You close your eyes again."
                    elif first_counter == 1:
                        "There's plenty of time."
                    elif first_counter == 2:
                        "This bed is amazing."

                    $ first_counter += 1
                else:
                    $ Charles.give_trait("telepathic")

                    ch_Charles "Wake up, [Player.first_name]."

                    $ Charles.remove_trait("telepathic")

                    $ sleeping = False

    if black_screen:
        $ fade_in_from_black(0.4)

    "You climb out of the ultra-posh bed."
    "The rest of the room is just as nice."

    $ hanging_out = True
    $ second_counter = 0

    while hanging_out:
        menu:
            extend ""
            "Leave room":
                $ hanging_out = False
            "Stay and look around":
                if second_counter < 2:
                    if second_counter == 0:
                        "This room is bigger than my entire living room back home. . ."
                    elif second_counter == 1:
                        "Is this some kind of prank? What is this place?"

                    $ second_counter += 1
                else:
                    $ Charles.give_trait("telepathic")

                    ch_Charles "[Player.first_name], please come find me in my study. I will explain everything."

                    $ Charles.remove_trait("telepathic")

                    "You recognize that voice - the one from your dream."

                    $ hanging_out = False

    "You carefully and quietly open the door to the room."

    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_242

    $ Player.remove_trait("messy_bed")

    "Before you is a beautifully decorated hallway. You look in both directions, but nobody seems to be around."
    "With a shrug, you walk down the corridor."
    "Somehow, you know exactly where to go."

    call send_Characters(Charles, "bg_study") from _call_send_Characters_180
    call set_the_scene(location = "bg_study") from _call_set_the_scene_243

    ch_Charles "Good morning, [Player.first_name]."

    if first_counter + second_counter > 1:
        ch_Charles "Bit slow to get started, I see."

    ch_Player "Who are you? And where the hell am I?"
    ch_Player "Did you kidnap me or something?!"
    ch_Charles "Please, [Player.first_name]. Allow me to explain the situation."
    ch_Charles "I know this must be very stressful for you."

    $ Charles.name = "Charles Xavier"

    ch_Charles "My name is Charles Xavier. This is my school."

    $ Charles.name = "Xavier"

    ch_Charles "Welcome to the Xavier Institute for Higher Learning."
    ch_Charles "You were attacked by. . . an evil entity. One I've faced before."
    ch_Charles "It seems he wanted something from you."
    ch_Player "That actually happened?! It did feel way too real to be a simple nightmare. . ."
    ch_Player "But that thing. . . I heard its voice inside my head. How is this all possible? And why me?!"

    $ Charles.change_face("happy")

    ch_Charles "You are a mutant, [Player.first_name]. Like me. Like the X-Men."
    ch_Charles "It seems you manifested your abilities yesterday."
    
    $ Charles.change_face("neutral")
    
    ch_Charles "How mutant abilities emerge varies between individuals."
    ch_Charles "Sometimes, they appear during puberty. Often, their arrival coincides with stress. . . or trauma."
    
    $ Charles.change_face("neutral", mouth = "frown")
    
    ch_Charles "However, I believe Mr. Farouk has been watching you for some time already."
    
    $ Charles.change_face("neutral")

    $ Amahl.name = "Farouk"
    
    ch_Player "[Amahl.name]??? That was him???"
    ch_Player "Jesus, I thought he was just a normal shitty professor. Not something. . . evil."
    ch_Charles "Mr. Farouk is cunning, he has a history of subversion and deceit. Do not take him lightly."
    ch_Charles "I am uncertain why he has developed an interest in you specifically, but I assure you, you will be safe while at my Institute."
    
    $ Charles.change_face("happy")
    
    ch_Charles "You see, this is both a school and a haven for people like you and me."
    ch_Charles "There are many forces out there that wish to harm - or use - mutants. These threats unfortunately come in the form of both normal humans and other mutants alike."

    $ Charles.change_face("neutral", mouth = "frown")

    ch_Charles "I fear Mr. Farouk may not even be the worst of them."

    menu:
        extend ""
        "Hold on, if [Amahl.name] wants me. . . do you think he'd go after my family too?!":
            ch_Charles "Fear not, [Player.first_name]."
            ch_Charles "We are keeping a close eye on your family to ensure their safety."
            ch_Charles "We possess the means to protect them if it becomes necessary."
            
            $ Player.give_trait("has_family")
        "Never thought I'd say it, but thank god I don't have any family. Who knows what [Amahl.name] would do in order to get to me.":
            ch_Charles "True: it may prove to your benefit in this particular circumstance."
        "Fuck. . .":
            pass

    $ chatting = True
    $ asked_mutant = False
    $ asked_Charles = False
    $ asked_appearance = False

    while chatting:
        menu:
            extend ""
            "Wait a second, I'm a mutant? I have powers, like the X-Men?!" if not asked_mutant:
                call day_one_intro_1A from _call_day_one_intro_1A

                $ asked_mutant = True
            "So. . . what's your power?" if asked_mutant and not asked_Charles:
                $ Charles.change_face("neutral", brows = "furrowed")

                call Charles_activate_psychic from _call_Charles_activate_psychic

                pause 1.0
                
                $ Charles.give_trait("telepathic")

                ch_Charles "I am a telepath, not unlike your old professor. I am a professor as well, in fact. But that is where the similarities end."

                call Charles_deactivate_psychic from _call_Charles_deactivate_psychic
                
                $ Charles.change_face("neutral")
                $ Charles.remove_trait("telepathic")

                $ asked_Charles = True
            "If we're both mutants, why do you look normal and I look. . . like this?" if asked_mutant and Player.check_traits("visible_mutation") and not asked_appearance:
                ch_Charles "Despite our best efforts, much of mutant physiology remains a mystery."
                ch_Charles "Upon manifestation of their abilities, the appearance of some mutants changes in. . . unpredictable ways."

                $ asked_appearance = True
            "Well, I'm out of questions.":
                if not asked_mutant and not asked_Charles:
                    $ Charles.change_face("confused1")

                    ch_Charles ". . . Okay. . ."

                    $ Charles.change_face("neutral")

                $ chatting = False

    ch_Charles "I know it is a lot to take in at once."
    ch_Charles "I hope you will agree to stay here, at least for now. If for nothing else, then for your own protection."
    ch_Charles "In time, you may even decide to call this place home, if you so desire."

    menu:
        extend ""
        "But what about my family. . . ?" if Player.check_traits("has_family"):
            $ Charles.change_face("neutral", mouth = "frown")

            ch_Charles "I am afraid you might only put them in harm's way by going back home."

            $ Charles.change_face("neutral")
        "This is. . . a lot to take in.":
            $ Charles.change_face("neutral", mouth = "frown")

            ch_Charles "I imagine that this must be incredibly difficult for you, [Player.first_name]."
            ch_Charles "It will take time to process everything that has happened."

            $ Charles.change_face("neutral")
        "I could get used to living in a mansion. . .":
            ch_Charles "Please do not take your situation for granted, [Player.first_name]."

    ch_Charles "Ah, and [Player.first_name], one more thing. Take this, your old phone was broken when we found you."

    $ phone_interactable = False

    show screen phone_screen()
    
    ch_Player "What is it? Doesn't look like any cellphone brand I've seen before."
    ch_Charles "That is our own latest technology. You will be able to communicate with anyone just like with a normal phone."
    ch_Charles "It also has additional features for you to keep track of your personal progress."
    ch_Player "Awesome, thanks! I hope it won't break as easily as my last phone."
    ch_Charles "Do not fret, we have tested this model extensively with a variety of mundane as well as mutant forces. It is nigh indestructible."
    "[Charles.name] hands the phone to you and starts explaining how high tech it is."

    hide screen phone_screen

    $ Charles.change_face("neutral", brows = "raised")

    "As soon as you take it, the phone slips out of your hand, performing pirouettes through the air that would make any dancer jealous."

    $ Charles.change_face("neutral", brows = "raised", mouth = "frown")

    show expression "images/effects/crack.webp" as crack onlayer effects:
        anchor (0.5, 0.5) pos (0.5, 0.75)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 2.0 alpha 0.0

    "The sound of the phone hitting the ground makes you wince."
    "An awkward silence fills the air."

    hide crack onlayer effects
    
    $ Player.give_trait("phone_cracked")
    
    $ phone_interactable = False

    show screen phone_screen()

    "You quickly pick the phone back up and check it for damage. . .{p}the screen is cracked."
    ch_Player "So, [Charles.name], you were saying something about it being unbreakable. Do I get a warran. . ."

    $ Charles.change_face("neutral")

    "[Charles.name] looks relieved as a woman approaches, interrupting your conversation."

    $ Charles.change_face("neutral", brows = "raised")

    hide screen phone_screen

    $ phone_interactable = True

    $ Ororo.name = "???"
    $ Ororo.change_face("confused1", eyes = "right")
    $ Ororo.change_arms("hips")

    call add_Characters(Ororo, direction = "right") from _call_add_Characters_50

    ch_Ororo "Charles? You wanted to see me?"

    $ Charles.change_face("happy")

    ch_Charles "Ah, yes, thank you, Ororo."

    $ Charles.change_face("neutral")

    ch_Charles "[Player.first_name], I would like you to meet one of our esteemed professors and X-Men team member, Prof. Munroe. Ororo, this is [Player.full_name]."

    $ Ororo.name = "Prof. Munroe"
    $ Ororo.change_face("smirk1")
    $ Ororo.change_arms("crossed")

    ch_Ororo "It is good to finally meet you, [Player.first_name]. You've been the talk of the campus lately, lots of rumors and speculation regarding your power."

    menu:
        extend ""
        "Wow. . . I uhh. . .":
            $ Ororo.change_face("worried1")
            $ Ororo.change_arms("hips", right_arm = "neutral")

            ch_Ororo "Charles, are you sure he's okay?"
        "It's great to meet you, [Ororo.name]. I can't believe I'm talking to one of the X-Men.":
            $ Ororo.change_face("happy", blush = 1)

            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_872
        "Nice to meet you, too.":
            pass

    ch_Charles "Ororo, I think [Player.first_name] would benefit from a tour of the campus."

    $ Ororo.change_face("neutral")
    $ Ororo.change_arms("hips")

    ch_Charles "I understand you also plan on assigning him some tutors so he can catch up with the rest of his class."
    ch_Ororo "Indeed, I'll take it from here, Charles."
    ch_Charles "Thank you. [Player.first_name], I leave you in Ororo's capable hands. I have pressing matters to attend to."

    $ Ororo.change_arms("neutral")

    menu:
        extend ""
        "Wow. . . I am forever in your debt, [Charles.name].":
            $ Ororo.change_face("confused1", mouth = "smirk")
            $ Ororo.change_arms("angry")

            ch_Charles "Please, [Player.first_name], think nothing of it."

            call send_Characters(Charles, location = "hold") from _call_send_Characters_181
            call swap_Slots(Ororo, "middle") from _call_swap_Slots
        "Thank you, [Charles.name]. I might be dead if not for you.":
            $ Ororo.change_face("smirk1")
            $ Ororo.change_arms("hips", right_arm = "neutral")

            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_873

            ch_Charles "You are very welcome, [Player.first_name]."

            call send_Characters(Charles, location = "hold") from _call_send_Characters_182
            call swap_Slots(Ororo, "middle") from _call_swap_Slots_1

            $ Ororo.change_arms("neutral", left_arm = "extended")

            ch_Ororo "I'm glad you properly appreciate everything Charles is doing for you."

    $ Ororo.change_face("neutral")
    $ Ororo.change_arms("neutral")

    $ Charles.name = "Xavier"

    ch_Ororo "Follow me, if you please."

    call hide_Character(Ororo) from _call_hide_Character_33

    jump day_one_tour

label day_one_intro_1A:
    $ Charles.change_face("neutral")
    
    ch_Charles "Yes, you are. Although your powers may not be so flamboyant as those you frequently see in comic books."

    if Player.check_traits("visible_mutation"):
        if Player.skin_color in ["blue", "green", "red"]:
            "You look down at your [Player.skin_color] skin."
        elif Player.ears:
            "You reach up to brush the tips of your ears."

        ch_Player "I guess that's not the most shocking news after all."

    menu:
        extend ""
        "But still. . . I actually have superpowers! That's awesome!":
            $ Charles.brows = "raised"

            ch_Charles "I'm. . . glad you're taking this so well, [Player.first_name]."
        "Wait. . . fuck. I'll be an outcast now.":
            $ Charles.change_face("happy")

            ch_Charles "Come now, [Player.first_name], you are still the same person you were yesterday. And you are not alone."
            ch_Player "That's. . . not very comforting."
        "You're joking. . . right?":
            $ Charles.brows = "furrowed"
            
            call Charles_activate_psychic from _call_Charles_activate_psychic_1

            pause 1.0

            $ Charles.give_trait("telepathic")

            ch_Charles "I am not."

            call Charles_deactivate_psychic from _call_Charles_deactivate_psychic_1
            
            $ Charles.change_face("neutral")
            $ Charles.remove_trait("telepathic")
            
    ch_Player "So. . . what are my powers?"

    if Player.check_traits("visible_mutation"):
        ch_Player "Other than. . . well, you know."

    ch_Player "I hope I can at least fly."

    $ Charles.change_face("neutral")

    ch_Charles "Our scans have been inconclusive, but it is my hypothesis that you have a very unique ability: close contact with you seems to. . . nullify other mutants' powers."
    ch_Charles "Accordingly, you seem to be impervious to the effects of {i}some{/i} mutant powers."
    ch_Charles "We don't fully understand how it works, and I suspect it will take much time - and training - before you are able to control it reliably."

    menu:
        extend ""
        "Aw. . . no flying?":
            ch_Charles "Scanning powers is an inexact science, you may have other abilities yet to be revealed."
        "That's. . . cool, I guess?":
            ch_Charles "Indeed, news of your arrival has already caused a bit of a commotion around here."

            $ Charles.change_face("neutral", mouth = "frown")

            ch_Charles "If you only knew the lengths some mutants would go to have their abilities removed. . ."

            $ Charles.change_face("neutral")

    return

label day_one_tour:
    $ fade_to_black(0.4)

    $ time_index = 1

    $ lighting = "day"

    call set_the_scene(location = Player.home) from _call_set_the_scene_244
    call add_Characters(Ororo) from _call_add_Characters_51

    pause 1.0

    $ Ororo.change_arms("neutral", right_arm = "extended")

    ch_Ororo "I trust you've already seen your room? You won't need to worry about roommates, all students have gotten private rooms since the expansion, although the floors are coed."
    
    $ Ororo.change_arms("neutral")

    ch_Ororo "The rooms also have private bathrooms and showers."
    ch_Ororo "Each door is labeled with the resident's name."

    $ Ororo.change_arms("hips", right_arm = "neutral")

    ch_Player "This room is amazing. And is this floor only student housing?"
    ch_Ororo "Yes, the professors and non-student residents live in a separate wing of the mansion."

    call hide_Character(Ororo) from _call_hide_Character_34

    jump meet_Rogue

label meet_Rogue:
    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_245
    call add_Characters(Ororo) from _call_add_Characters_52

    pause 1.0

    $ Ororo.change_arms("neutral", right_arm = "extended")

    ch_Ororo "This is one of our classrooms. You won't see large lecture halls like your previous school due to our relatively small student population."
    
    $ Ororo.change_arms("hips", right_arm = "neutral")

    ch_Ororo "There are a number of {i}unorthodox{/i} elective courses you can sign up for, but there is still a general education curriculum."

    menu:
        extend ""
        "So, what courses do you teach?":
            $ Ororo.change_face("smirk1")
            $ Ororo.change_arms("crossed")

            ch_Ororo "Mutant Physiology, World Politics, a few other electives as well."
        "Damn, and here I thought I could get away from freshman psychology.":
            $ Ororo.change_face("neutral", eyes = "squint")
            $ Ororo.change_arms("crossed")

            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_874
            call change_Character_stat(Ororo, "trust", 0) from _call_change_Character_stat_875

            ch_Ororo "I'm afraid not, [Player.first_name]."
        "How would you compare the difficulty of the curriculum to a normal university's? (academic)" if Player.scholarship == "academic":
            $ Ororo.change_face("pleased1")
            $ Ororo.change_arms("hips")

            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_876

            ch_Ororo "Well, I'd venture to say even the introductory courses are quite advanced. . ."

            $ Ororo.change_face("smirk1")

            ch_Ororo "They were developed by our own staff after all."

    if approval_check(Ororo, threshold = 40):
        $ Ororo.change_arms("neutral")

        ch_Ororo "The curriculum we teach may be different from what you're used to, [Player.first_name]. But don't worry, I have just the thing."

    $ Rogue.name = "???"
    $ Rogue.change_face("confused1")

    call add_Characters(Rogue, direction = "right") from _call_add_Characters_53

    $ Ororo.change_face("neutral", eyes = "left")
    
    ch_Rogue "Professor? Ya wanted to see me?"

    $ Ororo.change_face("smirk1")
    $ Ororo.change_arms("neutral", left_arm = "storm2")

    ch_Ororo "Yes, Rogue, thank you for joining us. I'll be assigning you as [Player.full_name]'s tutor so he can catch up with the rest of the class."

    $ Rogue.name = "Rogue"
    $ Rogue.change_face("smirk2")
    $ Rogue.change_arms("hips")

    $ Ororo.change_arms("crossed")

    ch_Ororo "You two may acquaint yourselves while I go find extra study materials for him."

    call send_Characters(Ororo, "hold") from _call_send_Characters_183
    call swap_Slots(Rogue, "middle") from _call_swap_Slots_2

    $ Rogue.change_face("happy")
    $ Rogue.change_arms("neutral")

    ch_Rogue "Howdy! [Player.first_name] right? You can call me Rogue, everyone does. Ah'm a sophomore here."
    ch_Player "Nice to meet you, [Rogue.name]."

    $ Rogue.change_face("worried1")
    $ Rogue.change_arms("sheepish")

    ch_Rogue "So. . . is it true what they've been sayin'? Can ya really remove a mutant's abilities?"

    menu:
        extend ""
        "Looks like the rumors are a bit exaggerated. Xavier seems to think my power only makes me impervious to other mutant powers.":
            call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_637

            $ Rogue.change_face("pleased2")
            $ Rogue.change_arms("neutral")
            
            ch_Rogue "Wow. . ."

            $ Rogue.change_face("smirk2")

            ch_Rogue "So. . . ya see, my ability allows me to absorb the memories, talents, and powers of those ah touch."
        "No, looks like my power only makes me immune to other powers. Why do you care?":
            call change_Character_stat(Rogue, "love", -medium_stat) from _call_change_Character_stat_877
            
            $ Rogue.change_face("worried2")
            $ Rogue.change_arms("angry")

            ch_Rogue "Because my ability has me absorb the memories, talents, and powers of those ah touch."
    
    $ Rogue.change_face("worried1")
    $ Rogue.change_arms("crossed")

    ch_Rogue "Thing is, it's more of a curse to tell ya the truth. Ah can't control it too well so touchin' someone could seriously harm them."
    ch_Rogue "Ah haven't been able to touch someone in a really long time. . ."
    ch_Rogue "Do ya think maybe ah could. . ."

    $ Rogue.change_face("worried2")
    $ Rogue.change_arms("neutral", left_arm = "extended")

    "She almost starts taking off one of her gloves."
    
    call add_Characters(Ororo, direction = "left") from _call_add_Characters_54

    $ Rogue.change_face("surprised2", eyes = "right", blush = 1)
    $ Rogue.change_arms("neutral")

    $ Ororo.change_arms("neutral", left_arm = "extended")

    ch_Ororo "Here we are, [Player.first_name]. These are some textbooks and study guides you will need for class. I do hope you and Rogue are getting along." 

    $ Rogue.change_face("neutral", mouth = "lipbite", blush = 1)
    $ Rogue.change_arms("sheepish", right_arm = "neutral")

    $ Ororo.change_arms("hips")

    menu:
        extend ""
        ". . . Yes, [Rogue.name] has just been telling me a little about the Institute.":
            call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_638
            
            $ Rogue.change_face("pleased1", blush = 1)
        "Definitely! I can tell we're going to get along really well.":
            call change_Character_stat(Rogue, "love", medium_stat) from _call_change_Character_stat_878
            
            $ Rogue.change_face("surprised2", eyes = "down", blush = 1)

            "You glance at [Rogue.name]'s gloved hand as you say it."

            $ Rogue.History.update("Player_looked_at_glove")
        "We are. Thank you very much, [Ororo.name], I'll make sure to study hard.":
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_639
            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_879

            $ Rogue.change_face("pleased1", blush = 1)

            $ Ororo.change_face("pleased1")

    pause 1.0

    $ Rogue.change_face("smirk2", blush = False)
    $ Rogue.change_arms("neutral")

    $ Ororo.change_face("smirk2", eyes = "left")
    $ Ororo.change_arms("neutral", left_arm = "storm2")

    ch_Ororo "Alright, thank you, [Rogue.name], you are dismissed."
    
    $ Rogue.change_face("happy")

    $ Ororo.change_arms("hips", right_arm = "neutral")

    ch_Rogue "See y'all tomorrow!"

    call send_Characters(Rogue, "hold") from _call_send_Characters_184

    call hide_Character(Ororo) from _call_hide_Character_35
    call set_the_scene(location = "bg_pool") from _call_set_the_scene_246
    call add_Characters(Ororo) from _call_add_Characters_55

    $ Ororo.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Ororo.change_face("smirk2")
    $ Ororo.change_arms("neutral", right_arm = "extended")

    ch_Ororo "As you can see, the mansion is equipped with quite a lovely swimming pool."
    ch_Ororo "It is free for students and faculty to use for 'recreational' purposes, as well as training."

    $ Ororo.change_face("confused1", mouth = "smirk")
    $ Ororo.change_arms("hips")

    ch_Ororo "However. . . and it pains me to have to make such a thing clear. . ."

    $ Ororo.change_face("confused1", eyes = "squint", mouth = "smirk")

    ch_Ororo "Please refrain from training underwater breath holds."
    ch_Ororo "Passing out in the pool does constitute 'drowning,' and we take such eventualities seriously, regardless of any 'competitions.'"

    call hide_Character(Ororo) from _call_hide_Character_36
    call set_the_scene(location = "bg_lockers") from _call_set_the_scene_247
    call add_Characters(Ororo) from _call_add_Characters_56

    $ Ororo.change_face("smirk2")

    pause 1.0
    
    $ Ororo.change_arms("crossed")

    ch_Ororo "These are the locker room's communal showers."
    ch_Ororo "They are for washing off after a swim or workout."
    
    $ Ororo.change_face("confused1", eyes = "squint")
    
    ch_Ororo "This means everyone is expected to maintain their modesty. You will wear a swimsuit at minimum while showering here."

    $ Ororo.change_face("confused1")

    ch_Ororo "Is that understood?"
    ch_Player "Yes, Professor."

    pause 1.0

    $ Ororo.change_face("smirk1", blush = 1)
    $ Ororo.change_arms("hips", right_arm = "neutral")

    pause 1.0

    $ Ororo.blush = 0

    ch_Ororo "Very good."
    
    $ Ororo.change_face("neutral")

    ch_Ororo "Now, please follow me to the Danger Room."

    call hide_Character(Ororo) from _call_hide_Character_37

    ch_Player "Wait. . . did she say {u}Danger{/u} Room?"
    
    jump meet_Laura

label meet_Laura:
    call set_the_scene(location = "bg_danger") from _call_set_the_scene_248
    call add_Characters(Ororo) from _call_add_Characters_57

    ch_Ororo "This is the Danger Room."

    $ Ororo.change_face("worried1")

    ch_Ororo "I'm sure Charles mentioned that the outside world can be a dangerous place for mutants."
    ch_Ororo "As such, teaching students to protect themselves is an important part of our curriculum."
    
    $ Ororo.change_face("neutral")
    $ Ororo.change_arms("neutral", right_arm = "extended")

    ch_Ororo "The advanced technology in this room can simulate combat scenarios which will be used to train you."

    $ Ororo.change_face("worried1")
    $ Ororo.change_arms("crossed")

    ch_Ororo "I understand this is all new to you. You probably have very little, if any, real world combat experience."

    $ Ororo.change_face("confused1")

    ch_Player "I was in a couple schoolyard brawls back in high school, but you're right, nothing that would help me fight evil mutants."
    ch_Ororo "That is why you will have a combat instructor for your first few months at our school."

    $ Ororo.eyes = "left"

    "[Ororo.name] looks at a figure at the other end of the room."
    
    $ Ororo.change_arms("neutral", left_arm = "storm2")

    ch_Ororo "X-23! Come here please."

    $ Laura.name = "X-23"

    # call change_Outfit(Laura, Laura.Wardrobe.Outfits["Hero (Chapter I)"], instant = True) from _call_change_Outfit_34
    call add_Characters(Laura, direction = "right") from _call_add_Characters_58

    pause 1.0

    $ Laura.change_arms("neutral")

    $ Ororo.change_face("neutral")
    $ Ororo.change_arms("hips", right_arm = "neutral")

    ch_Laura "So this is the newbie?"
    "She looks you up and down."

    $ Laura.eyes = "down"

    pause 1.0

    $ Laura.eyes = "neutral"

    $ Ororo.change_face("surprised1", blush = 1)

    if Player.scholarship == "athletic":
        ch_Laura "Hmmm. His resting heart rate is low."
        ch_Laura "And he looks well built."
        ch_Laura "Interesting."

        call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_880
    else:
        ch_Laura "He looks reasonably well-built."
    
    $ Ororo.change_face("smirk1", eyes = "left", blush = 1)
    $ Ororo.change_arms("neutral", left_arm = "extended")
    
    ch_Ororo "Yes, this is [Player.full_name]. He was recently rescued."
    
    $ Laura.change_face("confused1", eyes = "squint")

    $ Ororo.change_face("smirk1")
    $ Ororo.change_arms("hips")
    
    ch_Ororo "He lacks combat experience and will need to be brought up to speed relatively quickly. I am assigning you as his combat instructor so you can help him establish a good foundation."
    
    $ Laura.change_face("suspicious1")
    $ Laura.change_arms("angry")

    $ Ororo.change_face("perplexed", eyes = "left")

    ch_Laura "Oh. . . so his muscles are just for show?"

    $ Ororo.change_arms("crossed")

    "[Ororo.name] gives [Laura.name] a pointed look."
    ch_Ororo "[Laura.public_name], what did I say about. . ."

    $ Laura.change_face("neutral", eyes = "squint")

    $ Ororo.change_face("confused1", eyes = "down")

    call phone_buzz from _call_phone_buzz_5

    "[Ororo.name]'s phone buzzes."

    $ Ororo.change_face("confused1")

    ch_Ororo "I have to take this. [Player.first_name], meet me in front of the Institute when you're done here."

    call send_Characters(Ororo, "hold") from _call_send_Characters_185
    call swap_Slots(Laura, "middle") from _call_swap_Slots_3

    $ Laura.change_face("confused1")
    $ Laura.change_arms("crossed")

    ch_Player "So uh. . . It's nice to meet you."
    ch_Laura "Yeah, ok."

    $ Laura.change_face("neutral")

    $ chatting = True
    $ asked_freshman = False
    $ asked_name = False
    $ asked_fighting = False
    $ asked_costume = False
    $ asked_powers = False
    $ asked_rumor = False
    $ asked_heartrate = False

    while chatting:
        menu:
            "Are you also a freshman?" if not asked_freshman:
                ch_Laura "Yes."

                $ asked_freshman = True
            "Is 'X-23' your real name?" if not asked_name:
                ch_Laura "Yes. It's the one I was born with."
                ch_Player "Do you go by anything else?"

                $ Laura.change_face("neutral", eyes = "squint")
                $ Laura.change_arms("angry")

                ch_Laura "I was also given the name 'Laura' later on. Only my closest allies can call me that."
                ch_Laura "You cannot."

                $ Laura.change_face("neutral")
                $ Laura.change_arms("crossed")

                $ asked_name = True
            "You must be pretty good at fighting to be a combat instructor." if not asked_fighting:
                $ Laura.change_face("smirk1")

                ch_Laura "I am. I have a lot of experience. It's why I was made."
                ch_Player "Made?"

                $ Laura.change_face("neutral")

                $ asked_fighting = True
            "I like your costume." if not asked_costume:
                $ Laura.change_face("confused1")

                ch_Laura "It's not a costume. . . It's a functional suit"

                pause 1.0
                
                $ Laura.eyes = "down"
                $ Laura.blush = 1

                pause 1.0

                $ Laura.change_face("neutral")

                $ asked_costume = True
            "What kind of powers do you have?" if not asked_powers:
                call meet_Laura_1A from _call_meet_Laura_1A

                $ asked_powers = True
            "Have you heard the rumors about my power?" if asked_powers and not asked_rumor:
                ch_Laura "Nope."
                ch_Player "Well, as a word of warning, I'm seemingly impervious to other mutant powers."
                ch_Player "Touching me might be a bit weird."

                $ Laura.change_face("confused1", eyes = "squint")

                ch_Laura "So touching you might disable my regeneration?"
                ch_Player "Maybe? Just wanted to give you a heads up."

                $ Laura.change_face("neutral")

                call change_Character_stat(Laura, "trust", medium_stat) from _call_change_Character_stat_882

                $ Laura.History.update("was_warned_about_Player_power")

                $ asked_rumor = True
            "So. . . how did you know my resting heart rate was low? (athletic)" if Player.scholarship == "athletic" and not asked_heartrate:
                $ Laura.change_face("confused1")

                ch_Laura "I was listening to it."

                $ Laura.change_face("neutral")

                ch_Laura "It was clearly lower than a normal person's."

                $ Laura.change_face("suspicious1")

                ch_Laura "You've been physically conditioned, but apparently not martially trained."

                $ asked_heartrate = True
            "Anyways. . . I should probably go catch up with [Ororo.name].":
                $ Laura.change_face("neutral")

                ch_Laura "You should. Be back here in two days so we can start."
                "After struggling with your new phone, you manage to set a reminder."

                $ chatting = False

    call send_Characters(Laura, "hold") from _call_send_Characters_186

    $ fade_to_black(0.4)

    "You head out of the Danger Room."

    jump day_one_tour_farewell
    
label meet_Laura_1A:
    ch_Laura "I have regeneration abilities."
    ch_Laura "Also. . . I have indestructible claws."

    $ Laura.change_face("neutral", eyes = "squint")
    $ Laura.change_arms("neutral", left_arm = "X")
    
    call Laura_unsheathes_claws(hand = "left") from _call_Laura_unsheathes_claws_5

    $ Laura.change_face("neutral")

    menu:
        "Whoa! Sick!":
            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_884

            $ Laura.change_face("smirk2")

            ch_Laura "They are. . . effective."
        "Damn, those look wicked sharp.":
            ch_Laura "They are."
        "Doesn't that hurt?":
            call change_Character_stat(Laura, "love", -small_stat) from _call_change_Character_stat_885

            $ Laura.change_face("neutral", eyes = "squint")

            ch_Laura "For someone like you, maybe."

            $ Laura.change_face("neutral")

    call Laura_sheathes_claws from _call_Laura_sheathes_claws_5

    $ Laura.change_arms("neutral")

    return

label day_one_tour_farewell:
    $ time_index = 2
    
    $ lighting = "evening"

    call set_the_scene(location = "bg_campus") from _call_set_the_scene_249

    $ Ororo.change_face("neutral")
    $ Ororo.change_arms("hips", right_arm = "neutral")

    call add_Characters(Ororo) from _call_add_Characters_59

    pause 1.0

    $ Ororo.change_face("happy")

    ch_Ororo "Hello again, [Player.first_name]."

    $ Ororo.change_face("smirk1")
    $ Ororo.change_arms("crossed")

    ch_Ororo "Please don't think unkindly of [Laura.public_name], I know she can come off as a bit abrasive."
    
    $ Ororo.change_face("worried1")
    $ Ororo.change_arms("sheepish")
    
    ch_Ororo "It's not that she doesn't like you, she's just been through a lot and didn't have a lot of healthy social interaction before coming here."
    
    $ Ororo.change_arms("hips", right_arm = "neutral")

    ch_Player "Don't sweat it, I won't hold it against her."
    
    $ Ororo.change_face("smirk1")

    ch_Player "What exactly did she go through?"

    $ Ororo.change_face("sad")

    ch_Ororo "I'll leave it to her if she wishes to tell you the full story. But suffice it to say, she was made to be a weapon, not a person."
    ch_Player "Damn. . ."

    $ Ororo.change_face("worried1")
    $ Ororo.change_arms("hips", right_arm = "extended")

    ch_Ororo "Indeed. So treat her kindly and try to cut her some slack."

    $ Ororo.change_face("worried1", eyes = "down")
    $ Ororo.change_arms("hips", right_arm = "neutral")

    call phone_buzz from _call_phone_buzz_6

    "[Ororo.name]'s phone buzzes."

    $ Ororo.change_face("worried1")
    
    ch_Ororo "It seems I am needed again. I expect you'll be able to find your way back." 

    $ Ororo.change_face("neutral")

    ch_Ororo "It was a pleasure, [Player.first_name]."

    $ Ororo.change_arms("neutral", left_arm = "extended")

    "She reaches out to shake your hand."

    menu:
        extend ""
        "It really was a pleasure.":
            $ Ororo.change_face("surprised2", blush = 1)
            $ Ororo.change_arms(right_arm = "fist", left_arm = "extended")

            "A shiver runs up the professor's arm as you shake her hand."

            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_886
            call change_Character_stat(Ororo, "trust", 0) from _call_change_Character_stat_887

            $ Ororo.change_arms("crossed")

            ch_Ororo "{i}Ahem{/i}. . . Well, goodbye, [Player.first_name]. I have a mission to attend to."
        "Are you sure?":
            $ Ororo.change_face("smirk1")

            ch_Ororo "I am. I'd like to see firsthand what all the fuss is about."

            $ Ororo.change_face("surprised2", blush = 1)
            $ Ororo.change_arms(right_arm = "fist", left_arm = "extended")

            "A shiver runs up the professor's arm as you shake her hand."

            call change_Character_stat(Ororo, "love", 0) from _call_change_Character_stat_888
            call change_Character_stat(Ororo, "trust", 0) from _call_change_Character_stat_889

            $ Ororo.change_arms("crossed")

            ch_Ororo "Wow, that was. . . unexpected. I will see you when I return from my mission, [Player.first_name]."

    $ Ororo.change_arms("neutral")

    pause 1.0

    call send_Characters(Ororo, "hold") from _call_send_Characters_187

    $ fade_to_black(0.4)

    "You take in the views of the gorgeous campus as you make your way back to the dorm."

    jump day_one_tour_end

label day_one_tour_end:
    $ time_index = 3
    
    $ lighting = "night"

    call set_the_scene(location = Player.home) from _call_set_the_scene_250

    "The excitement of the past two days finally overcomes you."

    $ lights_on = False

    $ lighting = "moonlight"

    call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_251

    pause 2.0

    $ fade_to_black(0.4)

    "You collapse on the bed and fall asleep instantly."

    pause 2.0

    jump day_one_end

label day_one_end:
    $ unlocked_Characters.append(Charles)
    $ unlocked_Characters.append(Ororo)
    $ unlocked_Characters.append(Rogue)
    $ unlocked_Characters.append(Laura)

    $ Ororo.History.update("met")
    $ Rogue.History.update("met")
    $ Laura.History.update("met")

    call send_Characters(Rogue, "hold") from _call_send_Characters_188
    call send_Characters(Laura, "hold") from _call_send_Characters_189
    call send_Characters(Ororo, "hold") from _call_send_Characters_190
    call send_Characters(Charles, "hold") from _call_send_Characters_191

    $ active_Companions.remove(Ororo)

    $ reset_behavior()
    
    $ unlocked_locations.update({Rogue.home: "renpy.call('travel', Rogue)"})
    $ unlocked_locations.update({Laura.home: "renpy.call('travel', Laura)"})
    $ unlocked_locations.update({"bg_girls_hallway": "renpy.call('travel', 'bg_girls_hallway')"})
    $ unlocked_locations.update({"bg_hallway": "renpy.call('travel', 'bg_hallway')"})
    $ unlocked_locations.update({"bg_study": "renpy.call('travel', 'bg_study')"})
    $ unlocked_locations.update({"bg_campus": "renpy.call('travel', 'bg_campus')"})
    $ unlocked_locations.update({"bg_classroom": "renpy.call('travel', 'bg_classroom')"})
    $ unlocked_locations.update({"bg_danger": "renpy.call('travel', 'bg_danger')"})
    $ unlocked_locations.update({"bg_pool": "renpy.call('travel', 'bg_pool')"})
    $ unlocked_locations.update({"bg_lockers": "renpy.call('travel', 'bg_lockers')"})
    
    $ Charles.name = "Xavier"
    $ Charles.names.append("Xavier")
    
    $ Ororo.name = "Prof. Munroe"
    $ Ororo.names.append("Prof. Munroe")
    $ Ororo.names.remove("Ororo")
    
    $ Rogue.name = "Rogue"
    
    $ Laura.name = "X-23"
    $ Laura.names.append("X-23")
    $ Laura.names.remove("Laura")

    $ Laura.petname = "X-23"

    $ Player.give_trait("phone_cracked")

    jump day_two_intro