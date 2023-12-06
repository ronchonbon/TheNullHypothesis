init python:

    def Jean_before_study_session_part_one():
        label = "Jean_before_study_session_part_one"

        conditions = [
            "chapter == 1 and season == 1",

            "day - EventScheduler.Events['Jean_back_from_mission'].completed_when > 3",

            "not Jean.History.check('studied_with_Player', tracker = 'season')",

            "Player.location in public_locations",
            "time_index == 2"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, priority = priority, waiting = waiting, traveling = traveling)

label Jean_before_study_session_part_one:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location) from _call_send_Characters_53

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Hey, [Jean.Player_petname]."
    ch_Jean "I was about to do some studying, wanna join?"

    menu:
        extend ""
        "Oh, sure!":
            $ Jean.change_face("happy")

            ch_Jean "Awesome!"

            if Player.location != Player.home:
                call send_Characters(Jean, Jean.home, behavior = "studying") from _call_send_Characters_292
                call set_the_scene(location = Jean.home) from _call_set_the_scene_51

            call actually_study(Jean) from _call_actually_study_2
        "Sorry, I had other plans. . .":
            $ Jean.change_face("worried1", mouth = "smirk")

            ch_Jean "Oh, okay. . ."

            $ Jean.History.update("Player_rejected_studying")
        "Nah, I'm good.":
            call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_129

            $ Jean.change_face("confused1")

            ch_Jean "Really?" 
            
            $ Jean.History.update("Player_rejected_studying")

    $ Jean.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Jean "Well, just let me know when you do want to study together, okay?"
    ch_Player "Sure."

    $ Jean.change_face("smirk2")

    ch_Jean "Bye!"

    call remove_Characters(Jean) from _call_remove_Characters_47

    $ ongoing_Event = False

    return

init python:

    def Jean_before_study_session_part_two():
        label = "Jean_before_study_session_part_two"

        conditions = [
            "chapter == 1 and season == 1",

            "day - EventScheduler.Events['Jean_before_study_session_part_one'].completed_when > 0",

            "not Jean.History.check('studied_with_Player', tracker = 'season')",
            "Rogue.History.check('studied_with_Player', tracker = 'season') or Laura.History.check('studied_with_Player', tracker = 'season')",
            
            "Player.location in public_locations",
            "time_index == 2"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, priority = priority, waiting = waiting, traveling = traveling)

label Jean_before_study_session_part_two:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location) from _call_send_Characters_54

    $ Jean.change_face("happy")

    ch_Jean "Hey, [Jean.Player_petname]!"

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "So. . ."
    ch_Jean "I have some free time."
    ch_Jean "Wanna study together?"

    menu:
        extend ""
        "That would be great, thanks.":
            $ Jean.change_face("happy")

            ch_Jean "Of course!"

            if Player.location != Player.home:
                call send_Characters(Jean, Jean.home, behavior = "studying") from _call_send_Characters_293
                call set_the_scene(location = Jean.home) from _call_set_the_scene_52

            call actually_study(Jean) from _call_actually_study_3
        "Not right now, sorry. . .":
            $ Jean.change_face("worried1", mouth = "smirk")

            ch_Jean "Oh. . ."

            $ Jean.History.update("Player_rejected_studying")
        "Not particularly.":
            call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_130

            $ Jean.change_face("confused1")

            ch_Jean "Oh really?" 

            $ Jean.History.update("Player_rejected_studying")

    $ Jean.change_face("confused1", eyes = "right")

    if Rogue.History.check("studied_with_Player", tracker = "season"):
        $ studied_with_Rogue_on = Rogue.History.check_when("studied_with_Player", tracker = "season")
    else:
        $ studied_with_Rogue_on = 0

    if Laura.History.check("studied_with_Player", tracker = "season"):
        $ studied_with_Laura_on = Laura.History.check_when("studied_with_Player", tracker = "season")
    else:
        $ studied_with_Laura_on = 0

    if studied_with_Rogue_on >= studied_with_Laura_on:
        ch_Jean "{size=-5}But you'll study with [Rogue.public_name], huh{/size}. . ."
    else:
        ch_Jean "{size=-5}But you'll study with [Laura.public_name], huh{/size}. . ."

    $ Jean.change_face("confused1")

    ch_Player "What was that?"
    ch_Jean "Hm?"

    $ Jean.change_face("neutral")

    ch_Jean "Oh, nothing. . ."
    ch_Jean "I'll see you later."

    call remove_Characters(Jean) from _call_remove_Characters_48

    $ ongoing_Event = False

    return

init python:

    def Jean_before_study_session_part_three():
        label = "Jean_before_study_session_part_three"

        conditions = [
            "chapter == 1 and season == 1",

            "day - EventScheduler.Events['Jean_before_study_session_part_two'].completed_when > 3",

            "not Jean.History.check('studied_with_Player', tracker = 'season')",
            
            "Player.location in public_locations",
            "time_index == 2"]

        waiting = True
        traveling = True

        priority = 1

        return EventClass(label, conditions, priority = priority, waiting = waiting, traveling = traveling)

label Jean_before_study_session_part_three:
    $ ongoing_Event = True

    call send_Characters(Jean, Player.location) from _call_send_Characters_55

    $ Jean.change_face("neutral", eyes = "squint")

    ch_Jean "Hey, [Jean.Player_petname]."
    ch_Player "Hey, what's up?"

    $ Jean.change_face("smirk2")

    ch_Jean "How have you been doing in class so far?"
    ch_Player "Not too badly, why?"

    $ Jean.change_face("smirk1", eyes = "right")

    ch_Jean "Oh, nothing. . ."

    $ Jean.change_face("smirk1")

    ch_Jean "It's just that [Charles.name] wanted me to check up on you."
    ch_Player "Th-"

    $ Jean.change_face("smirk2")

    ch_Jean "And!"
    ch_Jean "He told me to study with you today. . ."
    ch_Jean "You know, to make sure you're not too overwhelmed."
    ch_Player "Oh. . . he did?"

    $ Jean.change_face("smirk2", eyes = "right")

    ch_Jean "Yep!"

    $ Jean.change_face("smirk2")

    ch_Jean "Totally. . ."

    $ Jean.change_face("happy")

    ch_Jean "Now, c'mon!"
    ch_Jean "Let's get to it."

    if Player.location != Player.home:
        call send_Characters(Jean, Jean.home, behavior = "studying") from _call_send_Characters_294
        call set_the_scene(location = Jean.home) from _call_set_the_scene_53

    call actually_study(Jean) from _call_actually_study_4

    $ ongoing_Event = False

    return