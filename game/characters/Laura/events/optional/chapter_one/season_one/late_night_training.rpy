init python:

    def Laura_chapter_one_season_one_late_night_training_setup():
        label = "Laura_chapter_one_season_one_late_night_training_setup"

        conditions = [
            "Laura.location not in ['hold', Player.location, Player.destination]",
            "'bg_danger' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.5",

            "not EventScheduler.Events['Laura_chapter_one_season_one_late_night_training'].completed",

            "time_index not in Laura.schedule.keys()",

            "chapter == 1 and season == 1",

            "time_index >= 3",

            "Laura.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_chapter_one_season_one_late_night_training_setup:
    call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_333
    
    return

init python:

    def Laura_chapter_one_season_one_late_night_training():
        label = "Laura_chapter_one_season_one_late_night_training"

        conditions = [
            "Player.destination == 'bg_danger'",

            "chapter == 1 and season == 1",

            "time_index >= 3",
            
            "Laura.location == 'bg_danger'",
            "Laura.behavior == 'training'",
            "len(get_Present(location = 'bg_danger')[0]) == 1",

            "Laura.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_danger": [
                "Player.location != 'bg_danger'",

                "chapter == 1 and season == 1",

                "time_index >= 3",
                
                "Laura.location == 'bg_danger'",
                "Laura.behavior == 'training'",
                "len(get_Present(location = 'bg_danger')[0]) == 1",

                "Laura.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_chapter_one_season_one_late_night_training:
    $ ongoing_Event = True

    $ fade_to_black(0.4)

    "You're surprised to see that, despite the late hour, there's a session in progress."

    $ count = 3

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
            show expression "images/effects/pow.webp" as pow onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0

        $ renpy.pause(renpy.random.random(), hard = True)

        $ count -= 1

    $ Laura.change_arms("fight")
    
    $ Laura.give_trait("left_claw")
    $ Laura.give_trait("right_claw")

    call try_on(Laura, Laura.Wardrobe.Clothes["bun"], instant = True)
    call set_the_scene(location = "bg_danger") from _call_set_the_scene_401

    "You see [Laura.name] beating the hell out of a swarm of combat dummies."

    menu:
        extend ""
        "Watch for a bit":
            pass
        "Don't disturb her training":
            "Looks like the Danger Room is off the table while [Laura.name]'s using it."

            $ EventScheduler.Events["Laura_chapter_one_season_one_late_night_training"].completed = False
            $ EventScheduler.Events["Laura_chapter_one_season_one_late_night_training"].completed_when = 1e8

            $ EventScheduler.Events["Laura_chapter_one_season_one_late_night_training"].counter = 0

            $ ongoing_Event = False

            call move_location(Player.home) from _call_move_location_58

            return

    $ count = 3

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
            show expression "images/effects/pow.webp" as pow onlayer effects:
                anchor (0.5, 0.5) pos (x, y)

                zoom 0.0
                alpha 0.0
                ease 0.1 zoom 1.0 alpha 1.0
                ease 1.0 alpha 0.0

        $ renpy.pause(renpy.random.random(), hard = True)

        $ count -= 1

    "As wild as her fighting style looks, you notice that at no point does she ever look like she's losing control."
    "She barely makes a sound, other than the occasional grunt."

    $ Laura.change_face("suspicious1")
    $ Laura.change_arms("neutral")

    call Laura_sheathes_claws from _call_Laura_sheathes_claws

    "As she finishes off the latest wave, she pauses, turns around and locks eyes with you."
    "She's drenched in sweat, her hair plastered to her face and neck. Her general disheveled look suggests she's been training hard and that she's been here for a while." 
    "Despite her appearance, she does not seem as out of breath as you might expect."
    ch_Laura "What is it?"
    ch_Player "Oh, uh. . . hope I'm not interrupting. . ."

    $ Laura.change_face("confused1", eyes = "squint")
    $ Laura.change_arms("crossed")

    ch_Laura "Yes. You are."

    $ Laura.change_face("confused1")

    ch_Laura "Is this not, by definition, an 'interruption'?"
    "You still don't know [Laura.name] well, but in retrospect, expecting her to be anything other than brutally blunt was probably foolish."

    menu:
        extend ""
        "What are you doing here so late? I take it you can't settle either?":
            call change_Character_stat(Laura, "love", small_stat) from _call_change_Character_stat_852
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_853

            $ Laura.change_face("neutral")

            ch_Laura "I simply had the opportunity for an extended training session. I took it."
        "I know people say you practically live down here, but you haven't actually moved in, have you?":
            call change_Character_stat(Laura, "love", -small_stat) from _call_change_Character_stat_854
            
            $ Laura.change_face("suspicious1")

            ch_Laura "No. Apparently the Danger Room and associated areas have no provisions for long-term habitation, except in a dire emergency."
        "Everything okay? Looks like you've been in here a while.":
            call change_Character_stat(Laura, "love", medium_stat) from _call_change_Character_stat_857
            call change_Character_stat(Laura, "trust", small_stat) from _call_change_Character_stat_881

            $ Laura.change_face("confused3", blush = 1) 
            
            pause 1.0
            
            $ Laura.change_face("confused1", eyes = "right", blush = 1)

            ch_Laura "I. . . yes. I am. I just. . . I feel. . . restless today."

    $ Laura.change_face("angry1")
    $ Laura.change_arms("angry")

    ch_Laura "And besides, I still do not feel tired yet."
    ch_Player "Do you do this often? Just stay up all night training?"

    $ Laura.change_face("neutral")
    $ Laura.change_arms("neutral")

    ch_Laura "Not all night. But yes, I frequently train until late."

    $ Laura.change_face("neutral", eyes = "right")
    $ Laura.change_arms("crossed")

    ch_Laura "I find it helps keep me. . . focused. Grounded."

    $ Laura.change_face("worried1", eyes = "right")
    $ Laura.change_arms("hips", right_arm = "extended")

    ch_Laura "I feel like everything here makes sense in a way it does not out there."
    ch_Player "Out there, like. . . around other people?"

    $ Laura.change_face("angry1", eyes = "right")
    $ Laura.change_arms("angry")

    ch_Laura "Amongst other things." 
    "She's not exactly being unfriendly, but you're still left with the impression that you've intruded upon her personal space."

    $ Laura.change_face("confused1")
    $ Laura.change_arms("neutral")

    ch_Player "Alright, well I won't keep you any longer. Goodnight."
    ch_Laura "Good. . . night."

    $ fade_to_black(0.4)
    
    "You head back upstairs feeling like you've learned something about [Laura.name] tonight. You're not sure what, exactly, but you think you've seen a side of her that no one else has."

    call move_location("bg_hallway") from _call_move_location_61

    $ ongoing_Event = False

    return