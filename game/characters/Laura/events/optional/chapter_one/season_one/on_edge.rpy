init python:

    def Laura_chapter_one_season_one_on_edge_setup():
        label = "Laura_chapter_one_season_one_on_edge_setup"

        conditions = [
            "Laura.location not in ['hold', Player.location, Player.destination]",
            "'bg_campus' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_chapter_one_season_one_on_edge'].completed",

            "time_index not in Laura.schedule.keys()",

            "chapter == 1 and season == 1",

            "Laura.History.check('studied_with_Player', tracker = 'season')",
            "EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed",

            "time_index < 3",
            "weather != 'rain'",

            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_chapter_one_season_one_on_edge_setup:
    call remove_Characters(location = "bg_campus") from _call_remove_Characters_338
    call send_Characters(Laura, "bg_campus", behavior = False) from _call_send_Characters_334
    
    return

init python:

    def Laura_chapter_one_season_one_on_edge():
        label = "Laura_chapter_one_season_one_on_edge"

        conditions = [
            "Player.destination == 'bg_campus'",

            "chapter == 1 and season == 1",

            "Laura.History.check('studied_with_Player', tracker = 'season')",
            "EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed",

            "time_index < 3",
            "weather != 'rain'",
            
            "Laura.location == 'bg_campus'",
            "len(get_Present(location = 'bg_campus')[0]) == 1",

            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_campus": [
                "Player.location != 'bg_campus'",

                "chapter == 1 and season == 1",

                "Laura.History.check('studied_with_Player', tracker = 'season')",
                "EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed",
                
                "time_index < 3",
                "weather != 'rain'",
            
                "Laura.location == 'bg_campus'",
                "len(get_Present(location = 'bg_campus')[0]) == 1",

                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_chapter_one_season_one_on_edge:
    $ ongoing_Event = True

    $ Laura.change_face("worried1", eyes = "right")
    $ Laura.change_arms("angry")

    call set_the_scene(location = "bg_campus") from _call_set_the_scene_402
    
    "As you walk across the grounds, you notice [Laura.name] standing by a tree a ways off the path. She looks unusually tense and you notice her eyes darting about."

    pause 1.0

    $ Laura.change_face("angry1", eyes = "left")

    menu:
        extend ""
        "See if [Laura.name] is okay":
            pass
        "She's probably fine":
            "She's probably just doing some kind of 'advance awareness training' or something. . ."

            call remove_Characters(Laura) from _call_remove_Characters_332

            $ EventScheduler.Events["Laura_chapter_one_season_one_on_edge"].completed = False
            $ EventScheduler.Events["Laura_chapter_one_season_one_on_edge"].completed_when = 1e8

            $ EventScheduler.Events["Laura_chapter_one_season_one_on_edge"].counter = 0

            $ ongoing_Event = False

            return

    "You walk over to her, maintaining a respectful distance. She already looks on edge and you don't want to make a potentially bad situation worse."
    ch_Player "[Laura.name], everything okay?"

    $ Laura.change_face("worried2", mouth = "open")
    $ Laura.change_arms("claws")

    pause 1.0

    $ Laura.change_face("furious", eyes = "right")
    $ Laura.change_arms("crossed")

    pause 1.0

    $ Laura.change_face("worried2")

    ch_Laura "I am. . . fine."
    "You notice an odd tone in her voice. She sounds. . . nervous?"

    ch_Player "Okay. . . Whatcha doin'? You look tense."

    $ Laura.change_face("worried1", eyes = "left") 

    pause 1.0

    $ Laura.change_face("appalled1") 

    ch_Laura "I was training in the Danger Room when a large group of students came in to practice."

    $ Laura.change_face("angry1", eyes = "right")
    $ Laura.change_arms("angry")

    ch_Laura "I prefer to train when it is quiet, so I left and came outside."

    $ Laura.change_face("angry1", eyes = "squint")
    $ Laura.change_arms("angry", right_arm = "extended")

    ch_Laura "Then, as I was crossing the grounds, I heard an unfamiliar noise up in the branches."

    $ Laura.change_arms("crossed")

    menu:
        extend ""
        "A strange noise?! Are we under attack?":
            call change_Character_stat(Laura, "love", -small_stat) from _call_change_Character_stat_883
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_893

            $ Laura.change_face("confused3") 
            
            pause 1.0
            
            $ Laura.change_face("confused1")

            ch_Laura "No. At least, not on this occasion."
        "Was it anything worth worrying about?":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_894
            call change_Character_stat(Laura, "trust", medium_stat) from _call_change_Character_stat_897

            $ Laura.change_face("neutral", eyes = "right") 
            
            pause 1.0
            
            $ Laura.change_face("angry1", eyes = "right")

            ch_Laura "I do not believe it was. I. . . overreacted."
        "Do you. . . do you recognise every little noise you hear out here?":
            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_898

            $ Laura.change_face("confused1", eyes = "squint") 

            ch_Laura ". . . yes? It is important to be fully aware of your surroundings at all times." 
            
            $ Laura.change_face("angry1", eyes = "right") 

            ch_Laura "The fact that the rest of you do not understand this is a constant source of irritation to me."

            $ Laura.change_face("worried1", eyes = "left") 

            ch_Laura "But on this occasion, I think I may have. . . overestimated the threat."

    $ Laura.change_face("angry1", eyes = "right", blush = 1) 
    $ Laura.change_arms("angry")

    ch_Laura ". . . it was a cat."

    $ Laura.change_face("furious", blush = 1)
    $ Laura.change_arms("crossed")

    ch_Player ". . . a cat?"
    ch_Laura "Yes. Black. Amber eyes. Sleek. And it looked like it was stuck."

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Player "Did you try and help it?"

    $ Laura.change_arms("hips", right_arm = "extended")

    ch_Laura "I tried. It didn't understand what I was trying to do, so it kept swiping at me. I think it was scared of me."

    $ Laura.change_face("confused1")
    $ Laura.change_arms("neutral")

    ch_Player "It didn't hurt you, did it?"
    ch_Laura "They are fierce creatures, but no. . ."

    $ Laura.change_face("neutral")

    ch_Laura "Once it started screaming at me, I backed away."

    $ Laura.change_face("neutral", eyes = "left")
    $ Laura.change_arms("neutral", left_arm = "extended")

    ch_Laura "It saw this and leapt down, running away. I think it may be somewhere in the bushes over there."
    
    $ Laura.change_arms("crossed")

    ch_Player "So, what are you doing here?"

    $ Laura.change_face("confused1")

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right")

    "She hesitates, as if she's struggling with the question."

    $ Laura.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Laura "I turned around and I realized I had attracted an audience. It felt like everyone was staring at me."
    
    $ Laura.change_arms("angry")

    ch_Laura "I felt. . . exposed. Like there were too many people and I had nowhere to hide."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I did not like it."
    "She seems a little calmer now, but this is still a side of [Laura.name] you've never seen before."
    "If you didn't know any better, you'd swear she sounded. . . anxious."

    menu:
        extend ""
        "Stay with her for a while":
            "You get the impression [Laura.name] could use some company, but you don't want to make her think you're taking pity on her." 
            ch_Player "Listen, I don't need to be anywhere for a while, do you want me to hang around for a bit?"

            $ Laura.change_face("confused3") 
            $ Laura.change_arms("neutral")

            ch_Laura "That. . . I would. . ."

            $ Laura.change_face("neutral", eyes = "right") 

            ch_Laura ". . . appreciate that. Thank you."

            $ Laura.change_face("neutral")

            "You stand and talk to [Laura.name] for a bit. After a while, she seems to feel more like herself and heads back to her room.."

            call change_Character_stat(Laura, "trust", large_stat) from _call_change_Character_stat_903

            call remove_Characters(Laura) from _call_remove_Characters_339
        "Head on your way":
            "[Laura.name] seems less on edge. You tell yourself she'll be fine on her own. . ."
            
            call change_Character_stat(Laura, "trust", -medium_stat) from _call_change_Character_stat_415

            ch_Player "Listen, I need to head back to my room, but. . . is there anything I can do for you?"

            $ Laura.change_face("suspicious1")

            ch_Laura "No. I will be fine, I just need to. . ."

            $ Laura.change_face("angry1", eyes = "right") 

            ch_Laura "Gather my thoughts."
            "You remind her to send you a message if she needs anything and head on your way."

            call move_location(Player.home) from _call_move_location_62

    $ ongoing_Event = False

    return