init python:

    def Jean_chapter_one_season_one_first_training_session():
        label = "Jean_chapter_one_season_one_first_training_session"

        conditions = [
            "chapter == 1 and season == 1",

            "not Jean.History.check('trained_with_Player', tracker = 'season')",
            
            "Player.behavior == 'training' and Jean in Player.behavior_Partners and Jean.behavior == 'training'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Jean_chapter_one_season_one_first_training_session:
    $ ongoing_Event = True

    $ fade_to_black(0.4)

    call remove_everyone_but(Jean, fade = False) from _call_remove_everyone_but_1

    "You both warm up quickly with some dynamic stretches."
    "[Jean.name] suggests starting with a test of your power."

    $ fade_in_from_black(0.4)

    $ Jean.change_face("confused1")
    $ Jean.change_arms("hips")

    ch_Jean "Your power is mostly passive and defensive, huh?"
    
    $ Jean.change_arms("hips", left_arm = "extended")

    ch_Jean "Like, I can barely sense your emotions right now, if at all. I can for most people."
    
    $ Jean.change_arms("hips")

    ch_Player "I guess so, I'm not really trying to do anything."

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("crossed")

    ch_Jean "Hmmm. . . maybe I'll just chuck some tennis balls at you and see what happens."

    $ Jean.change_arms("psychic1")

    call Jean_activate_psychic from _call_Jean_activate_psychic_5

    ch_Player "Wai. . ."
    "Before you can protest, a tennis ball zips towards you."
    "It's going at major league fastball speeds straight towards your face."
    "You flinch."
    "But as the ball gets within a couple feet of you, it suddenly loses all momentum."
    "All you feel is a tiny twinge somewhere in the back of your mind."
    "The ball harmlessly bounces off your chest."

    $ Jean.change_face("perplexed")
    
    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_5

    $ Jean.change_arms("sass")

    ch_Jean "That was weird."

    $ Jean.change_arms("neutral", left_arm = "extended")

    ch_Jean "Once the tennis ball got close to you it just. . . disappeared from my mind."
    
    $ Jean.change_arms("sass")

    ch_Jean "I couldn't feel it at all."
    ch_Player "I {i}definitely{/i} didn't do anything on purpose."
    ch_Player "I think I felt something, though. Try it again, but I'll close my eyes this time."

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("psychic1")

    "She looks a bit too happy about this."

    $ fade_to_black(0.4)

    "[Jean.name] continues trying to pelt you with tennis balls."
    "She starts randomizing their trajectories to try to hit you from odd angles."
    "Even with your eyes closed, they all lose momentum close to you."
    "Each time one of the balls approaches you, you feel that tiny twinge again."
    "You try to anticipate the feeling for the next ball."
    "You feel the twinge and immediately try diving out of the way."
    "The ball still hits your shoulder{p}. . . and you somehow hit your funny bone on the way down."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    $ fade_in_from_black(0.4)

    ch_Player "Oof. . . that hurt."
    ch_Jean "You okay?"

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("crossed")

    ch_Player "Yeah, just hit my elbow on the way down. . ."

    $ Jean.change_face("neutral")

    ch_Jean "Good. But that was interesting, you can stop them without even looking."
    ch_Jean "And I guess you even anticipated that last one."
    
    $ Jean.change_arms("sass")

    ch_Jean "Seems like it's some instinctual thing."

    $ Jean.change_face("smirk1")
    $ Jean.change_arms("sass", right_arm = "extended")

    ch_Jean "I think with plenty of practice - and help from yours truly - we can totally get you to control it. . ."
    
    $ Jean.change_face("smirk2")
    $ Jean.change_arms("sass")

    ch_Jean ". . . probably. . ."
    ch_Jean ". . . if you're lucky. . ."

    $ chatting = True
    $ smart = False
    $ control = False
    $ help = False

    while chatting:
        menu:
            extend ""
            "You are pretty damn smart." if not smart:
                call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_392
                call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_393
                
                $ Jean.change_face("pleased2", blush = 1)
                $ Jean.change_arms("crossed")

                ch_Player "I'm sure I can do it with your help."
                ch_Jean "You think so?"
                ch_Jean ". . ."

                $ Jean.change_face("smirk2")
                $ Jean.change_arms("sass")

                ch_Jean "I mean, yeah! I totally am."
                ch_Jean "You're lucky I'm so generous."

                $ smart = True
            "Eventually? I guess you'll be helpful. . ." if not smart:
                call change_Character_stat(Jean, "love", -medium_stat) from _call_change_Character_stat_423

                $ Jean.change_face("worried1")
                $ Jean.change_arms("crossed")

                ch_Jean "You guess?"
                ch_Jean "I don't think you realize how difficult this stuff can be. . ."

                $ Jean.change_face("angry1", blush = 1)
                $ Jean.change_arms("angry")

                ch_Jean "That wasn't very nice, say you're sorry."
                ch_Player ". . . Sorry, [Jean.petname]. I just didn't imagine it would be that hard."

                $ Jean.change_face("neutral")
                $ Jean.change_arms("neutral")

                $ smart = True
            "How long did it take you to gain control?" if smart and not control:
                call Jean_chapter_one_season_one_first_training_session_1A from _call_Jean_chapter_one_season_one_first_training_session_1A

                $ control = True
            "Really? You'll help me out?" if smart and not control:
                call Jean_chapter_one_season_one_first_training_session_1B from _call_Jean_chapter_one_season_one_first_training_session_1B

                $ chatting = False
            "So, you'll help me out?" if smart and control:
                call Jean_chapter_one_season_one_first_training_session_1B from _call_Jean_chapter_one_season_one_first_training_session_1B_1

                $ chatting = False
            "Sure, I wouldn't mind the help." if smart and not control:
                call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_424
                
                $ Jean.change_face("angry1")
                $ Jean.change_arms("angry")

                ch_Jean "Wouldn't mind?"

                $ Jean.change_face("worried1")
                $ Jean.change_arms("crossed")

                ch_Jean "Are you trying to make me sad?"
                ch_Jean "You should be thrilled. . ."
                ch_Player "Sorry, I am. . . thrilled."

                $ chatting = False
            "I wouldn't mind your help either." if smart and control:                
                $ Jean.change_face("angry1")
                $ Jean.change_arms("angry")

                ch_Jean "Wouldn't mind?"

                $ Jean.change_face("worried1")
                $ Jean.change_arms("crossed")

                ch_Jean "Are you trying to make me sad?"
                ch_Jean "You should be thrilled. . ."
                ch_Player "Sorry, I am. . . thrilled."

                $ chatting = False

    $ Jean.change_face("neutral")
    $ Jean.change_arms("sass")

    ch_Jean "Alright, let's spar a bit."
    ch_Jean "I don't usually get in close enough for actual melee."

    $ Jean.change_face("smirk1")
    $ Jean.change_arms("fight")

    ch_Jean "But I'm feeling generous today. I'll show you some of my amazing skills."
    ch_Jean "Plus, without an offensive or ranged power. . ."
    ch_Jean "You don't really have a choice but to get in close."

    $ fade_to_black(0.4)

    "[Jean.name] restrains her power, and you both start exchanging blows."
    "You can tell she's pretty good, despite this not being her main fighting style."

    if Laura.History.check("trained_with_Player") >= 2:
        "However, all the beatdowns from training with [Laura.name] weren't for nothing."
        "You have a long way to go, but you're a quick learner and it's obvious you've been training."

        call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_204
        call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_205

        $ Jean.change_face("pleased2")
        $ Jean.change_arms("hips")

        $ fade_in_from_black(0.4)

        ch_Jean "Damn, I'm impressed!"
        ch_Player "I figured I'd have to make up for my lack of offense somehow."
        ch_Player "I don't have much choice but to get good with more mundane weapons and martial arts."
        ch_Player "[Laura.name] does a good job of hammering those lessons in. . . right into my bones. . ."

        $ Jean.change_face("smirk1", eyes = "squint", blush = 1)
        $ Jean.change_arms("crossed")

        ch_Jean "Hmm. . ."
    else:
        "If the beatdown with [Laura.name] wasn't enough, losing to someone who isn't even a close combat specialist shows you just how far behind you are."

        $ Jean.change_face("worried2")
        $ Jean.change_arms("crossed")

        $ fade_in_from_black(0.4)

        ch_Jean "At least you're fit enough to keep up."
        
        $ Jean.change_face("worried1")

        ch_Jean "You're gonna have to put a lot of work in, [Player.first_name]."
        
        $ Jean.change_arms("hips", right_arm = "extended")

        ch_Jean "Weapons and martial arts are kinda your only choice for offense. . ."
        
        $ Jean.change_face("neutral")
        $ Jean.change_arms("hips")

        ch_Player "I know. . ."

        $ Jean.change_face("smirk2")

        ch_Jean "But don't worry - with me as your teacher, I'll make sure you get up to speed."

    $ Jean.blush = 1
    $ Jean.change_arms(right_arm = "extended", left_arm = "rub_neck")

    ch_Jean "So uh. . . touching you is also supposed to have an effect, right?"
    
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Player "Yeah, it seems to nullify powers."

    $ Jean.change_arms("neutral")

    ch_Player "It requires skin-to-skin contact, though."

    call take_off(Jean, "gloves") from _call_take_off_2

    ch_Jean "I wanna see how it feels."
    ch_Player "Are you sure?"

    $ Jean.change_face("worried1")
    $ Jean.change_arms("angry")

    pause 1.0

    $ Jean.change_face("neutral")

    "She seems to struggle with something for a second."
    ch_Jean "I'm sure."

    $ Jean.change_arms("neutral", left_arm = "extended")

    "Without another word, she grabs your hand."

    $ Jean.change_face("surprised3", blush = 1)
    $ Jean.change_arms("angry", left_arm = "extended")

    "She shudders and her eyes widen."
    ch_Jean "Wow."
    ch_Jean "I couldn't even lift a feather with my power right now."
    ch_Jean "And everything feels so much. . . quieter."
    ch_Jean "Like I don't have a million different thoughts going through my head at once."
    
    $ Jean.change_face("confused2")

    "She stares at you."

    pause 1.5

    $ Jean.change_face("smirk2", blush = 2)

    pause 1.5

    "She finally pulls her hand away."

    $ Jean.blush = 0
    $ Jean.change_arms("crossed")

    ch_Jean "{i}Ahem{/i}. . . okay I think it's my turn to show off a bit."
    
    $ Jean.change_arms("sass", right_arm = "extended")

    ch_Jean "Not to toot my own horn, but my powers are pretty impressive."
    
    $ Jean.change_arms("neutral")

    pause 1.0

    $ Jean.change_arms("psychic2")

    $ fade_to_black(0.4)

    "[Jean.name] tries flexing her powers a bit to see where the limit is."
    "'Impressive' seems like an understatement."
    "She's able to lift scary amounts of weight with just a thought."
    "More and more objects start to fly around the room under her direction. . ."
    "Suddenly, everything freezes." with small_screenshake
    "You realize something's wrong as the air in the room starts crackling with palpable energy."

    $ Jean.change_face("worried4")
    
    call Jean_activate_psychic from _call_Jean_activate_psychic_6

    $ fade_in_from_black(0.4)

    ch_Jean "[Player.first_name]!!!!"

    $ Jean.change_arms("angry", left_arm = "extended")

    "You sprint over and grab her hand."

    $ Jean.brows = "worried"
    $ Jean.eyes = "closed"
    $ Jean.mouth = "frown"
    
    call Jean_deactivate_psychic from _call_Jean_deactivate_psychic_6

    "She shudders again."
    "The crashes of various objects dropping echoes across the Danger Room."
    "You're about to let go, but she grabs your hand and forces you to keep it there."

    $ Jean.eyes = "wide"
    $ Jean.blush = 1

    ch_Jean "Not yet. . ."
    ch_Jean "I can tell it still hasn't calmed down."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("neutral", left_arm = "extended")

    "She holds on tightly for another moment, then finally starts to relax."
    "She lets go."

    $ Jean.change_arms("crossed")

    ch_Player "Are you okay?"
    ch_Jean "I. . . am now. Thanks, [Player.first_name]."

    $ Jean.change_face("worried1", mouth = "frown", blush = 1)

    ch_Jean "I. . . probably could've reined that in on my own."
    "You can tell she's putting on a brave face."

    menu:
        extend ""
        "I'm glad you're not hurt.":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_426
            call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_588
                        
            $ Jean.change_face("neutral", blush = 1)

            ch_Jean ". . . Thanks."

            $ Jean.change_face("smirk2")

            ch_Jean "It's cute that you're worried about me. . ."

            $ Jean.blush = 2
        "Good thing I was here, someone might've gotten hurt.":
            call change_Character_stat(Jean, "trust", -small_stat) from _call_change_Character_stat_683
            
            $ Jean.change_face("angry1", blush = 1)
            $ Jean.change_arms("angry")

            pause 1.0

            $ Jean.change_face("worried1", blush = 1)

            ch_Jean "I. . . had it under control."
    
    $ Jean.change_face("worried1")
    $ Jean.change_arms("sass")

    ch_Jean "Ugh, I guess my power's still pretty unstable. . ."

    $ Jean.change_face("worried2")

    ch_Player "Would be bad if that happened during a real fight."
    ch_Jean "Yeah. . ."

    $ Jean.change_face("neutral")
    $ Jean.change_arms("crossed")

    ch_Jean "I think that's enough for today."
    ch_Jean "Text me when you're ready for the next session."
    ch_Jean "I'm gonna head out. I'll see you later. . ."
    ch_Player "See ya, [Jean.name]."

    call remove_Characters(Jean) from _call_remove_Characters_52
    
    $ ongoing_Event = False

    return

label Jean_chapter_one_season_one_first_training_session_1A:
    $ Jean.change_face("sad")
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Jean "Well. . ."
    ch_Jean "I don't really have full control either."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("crossed")

    ch_Jean "Prof. X sealed away some of my more dangerous abilities."

    $ Jean.change_face("neutral")

    ch_Jean "Like, I get it. I could've hurt someone."

    $ Jean.change_face("angry1")
    $ Jean.change_arms("angry")

    ch_Jean "But you'd think he trusts me at least a bit more than when I was 15!"
    ch_Jean "And now this crap with my powers being unstable."

    $ Jean.change_face("furious")

    ch_Jean "I'm supposed to be perfect. . ."
    ch_Player "I can see how that's. . . frustrating."

    menu:
        extend ""
        "I want to help however I can.":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_828
            call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_829

            ch_Player "I know I'm new to all this, but I don't care."

            $ Jean.change_face("pleased1", blush = 1)
            $ Jean.change_arms("crossed")

            ch_Player "I'll try my best."
            ch_Jean "Thanks, [Player.first_name]. . ."

            $ Jean.change_face("sly")

            ch_Jean "But you were gonna help me either way."

            $ Jean.change_face("smirk2")

            ch_Jean "It's for your own good."
        "I don't know if I can be of much help.":
            call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_830
            call change_Character_stat(Jean, "trust", -small_stat) from _call_change_Character_stat_842
            
            $ Jean.change_face("sad")
            $ Jean.change_arms("crossed")

            ch_Player "This is all still really new to me."
            ch_Jean "That's okay!"

            $ Jean.change_face("smirk2")

            ch_Jean "Don't worry, I'll do all the heavy lifting."

    return

label Jean_chapter_one_season_one_first_training_session_1B:
    $ Jean.change_face("confused1")
    $ Jean.change_arms("sass")

    ch_Jean "Of course. . ."
    ch_Jean "You're my 'little sib' now."
    
    menu:
        extend ""
        "Uh, I guess. . .":
            call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_843
            
            $ Jean.change_face("worried1")

            ch_Jean "You don't sound so happy about it. . ."
        "Thanks, [Jean.petname], I really appreciate it.":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_844
            call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_845

            $ Jean.change_face("happy", blush = 1)

            ch_Jean "You're welcome."
            ch_Jean "You should be happy."
            ch_Jean "I don't spend my time with just anyone. . ."

    return