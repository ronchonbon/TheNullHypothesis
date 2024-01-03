init python:

    def Laura_chapter_one_season_one_outcast_setup():
        label = "Laura_chapter_one_season_one_outcast_setup"

        conditions = [
            "Laura.location not in ['hold', Player.location, Player.destination]",
            "'bg_classroom' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_chapter_one_season_one_outcast'].completed",

            "time_index not in Laura.schedule.keys()",

            "chapter == 1 and season == 1",

            "Laura.History.check('trained_with_Player', tracker = 'season') >= 2",

            "weekday < 5 and time_index < 2",
            "clock == Player.max_stamina",

            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_chapter_one_season_one_outcast_setup:
    call send_Characters(Laura, "bg_classroom", behavior = "in_class") from _call_send_Characters_335
    
    return

init python:

    def Laura_chapter_one_season_one_outcast():
        label = "Laura_chapter_one_season_one_outcast"

        conditions = [
            "Player.destination == 'bg_classroom'",
            
            "chapter == 1 and season == 1",

            "Laura.History.check('trained_with_Player', tracker = 'season') >= 2",

            "weekday < 5 and time_index < 2",
            "clock == Player.max_stamina",
            
            "Laura.location == 'bg_classroom'",
            "Laura.behavior == 'in_class'",

            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_classroom": [
                "Player.location != 'bg_classroom'",

                "chapter == 1 and season == 1",

                "Laura.History.check('trained_with_Player', tracker = 'season') >= 2",

                "weekday < 5 and time_index < 2",
                "clock == Player.max_stamina",
                
                "Laura.location == 'bg_classroom'",
                "Laura.behavior == 'in_class'",

                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_chapter_one_season_one_outcast:
    $ ongoing_Event = True

    $ Present = get_Present(location = "bg_classroom")[0]
    
    python:
        for C in Present:
            if C != Laura:
                send_Characters_Offscreen(C, location = "bg_classroom")
            else:
                middle_Slot = C

    $ Laura.change_face("neutral", eyes = "left") 
    $ Laura.change_arms("crossed")

    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_403

    "Upon entering the classroom, you see a curious sight."
    "[Laura.name] is seated at the desk, but while most other students are packed in next to each other, nobody is sitting within ten feet of her."
    "She doesn't seem to notice, but hushed conversation around the room tells you the others are very aware of her presence."

    menu:
        extend ""
        "Sit next to [Laura.name]":
            pass
        "Take a random seat":
            "You grab a seat in the chair closest to you."

            call hide_Character(Laura) from _call_hide_Character_48
            
            $ EventScheduler.Events["Laura_chapter_one_season_one_outcast"].completed = False
            $ EventScheduler.Events["Laura_chapter_one_season_one_outcast"].completed_when = 1e8

            $ EventScheduler.Events["Laura_chapter_one_season_one_outcast"].counter = 0

            call move_location(Player.home) from _call_move_location_59

            $ ongoing_Event = False

            return

    "As you approach, you notice a tension in her shoulders. . . maybe she is aware of the situation around her. . ."
    "Pushing past all the looks you get from other students, you move to sit down right next to her."

    $ Laura.change_face("confused1")
    $ Laura.change_arms("angry")

    ch_Player "Is this seat taken?"
    ch_Laura ". . ."

    $ Laura.change_face("confused1", eyes = "squint")
    $ Laura.change_arms("crossed")

    ch_Laura "No. . ."
    "You sit down, and the tension in [Laura.name]'s muscles only increases."
    ch_Laura "Why?"
    ch_Player "Why. . . ?"

    $ Laura.change_face("suspicious1")

    ch_Laura "You are sitting next to me."
    ch_Laura "Does that not make you uncomfortable?"

    menu:
        extend ""
        "Not sure why it would, I think I enjoy your company. Always know where I stand when it comes to you.":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_905
            call change_Character_stat(Laura, "trust", medium_stat) from _call_change_Character_stat_906

            $ Laura.change_face("confused3")

            ch_Laura "You. . . enjoy it?" 
            
            $ Laura.change_face("confused1", eyes = "right") 
            
            ch_Laura "I see. . ."
        "I mean you are a bit intimidating, but that doesn't make me uncomfortable. I appreciate your bluntness.":
            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_907
            call change_Character_stat(Laura, "trust", medium_stat) from _call_change_Character_stat_909
            
            $ Laura.change_face("confused1")

            ch_Laura "Oh." 
            
            $ Laura.change_face("confused1", eyes = "right") 
            
            ch_Laura "I see. . ."
        "Nope. Is that what this is about? You think you make everyone uncomfortable? I can see why they might be, but it doesn't bother me.":
            call change_Character_stat(Laura, "love", -small_stat) from _call_change_Character_stat_911
            
            $ Laura.change_face("confused1")

            ch_Laura ". . ." 
            
            $ Laura.change_face("angry1", eyes = "right")

            pause 1.0

    $ Laura.change_face("neutral", eyes = "right")
    $ Laura.change_arms("neutral")

    "[Laura.name] remains silent as class begins, and she doesn't say another word for the remainder of class."
    "Although, you do notice some of the tension is gone from her shoulders, and she seems a bit more relaxed."
    
    $ fade_to_black(0.4)

    call expression f"chapter_{chapter}_season_{season}_class_narrations" from _call_expression_85

    pause 2.0

    call after_class from _call_after_class
    
    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral")

    "You pack up your things, but before you stand. . ."

    $ Laura.change_face("neutral", eyes = "right")
    $ Laura.change_arms("angry")

    ch_Laura "Everyone else always keeps their distance."

    $ Laura.change_face("confused1")
    $ Laura.change_arms("crossed")

    ch_Player "Wait, even someone like [Kurt.name]?"
    ch_Player "He seems like literally everyone's friend."
    ch_Laura "He is polite to me, but I can see it in his eyes. . ."
    ch_Laura ". . . the tension and fear when we interact."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Player "Fear?"
    ch_Laura "There are rumors about the things I've done before coming here."
    "You notice how she doesn't try to refute any of them. . ."

    $ Laura.change_arms("angry")

    ch_Laura "They have ideas about how dangerous I am."
    ch_Laura "I have overheard some call me a 'feral killing machine.'"

    $ Laura.change_face("neutral")

    ch_Player "What the hell? That's-"
    ch_Laura "It is fine."

    $ Laura.change_face("neutral", eyes = "right")
    $ Laura.change_arms("crossed")

    ch_Laura "An expected reaction from them. . ."

    $ Laura.change_face("smirk1", eyes = "right")

    ch_Laura "I did not mind you sitting next to me."
    
    $ Laura.change_arms("neutral")

    ch_Laura "Thank you. . ."
    ch_Laura "Bye."

    call remove_Characters(Laura) from _call_remove_Characters_340

    $ Laura.schedule[time_index + 1] = [Laura.home, "studying"]

    ch_Player "Bye. . ."

    $ ongoing_Event = False

    return