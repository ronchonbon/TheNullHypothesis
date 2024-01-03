init python:

    def Rogue_chapter_one_season_one_standoffish_part_one_setup():
        label = "Rogue_chapter_one_season_one_standoffish_part_one_setup"

        conditions = [
            "Rogue.location not in ['hold', Player.location, Player.destination]",
            "'bg_girls_hallway' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_one'].completed",

            "time_index not in Rogue.schedule.keys()",
            "time_index not in Kurt.schedule.keys()",

            "chapter == 1 and season == 1",

            "EventScheduler.Events['Rogue_chapter_one_season_one_people_watching'].completed",

            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_chapter_one_season_one_standoffish_part_one_setup:
    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_342
    call send_Characters(Rogue, "bg_girls_hallway", behavior = False) from _call_send_Characters_316
    call send_Characters(Kurt, "bg_girls_hallway", behavior = False) from _call_send_Characters_317

    return

init python:

    def Rogue_chapter_one_season_one_standoffish_part_one():
        label = "Rogue_chapter_one_season_one_standoffish_part_one"

        conditions = [
            "Player.destination == 'bg_girls_hallway'",

            "chapter == 1 and season == 1",

            "EventScheduler.Events['Rogue_chapter_one_season_one_people_watching'].completed",

            "Rogue.location == 'bg_girls_hallway' and Kurt.location == 'bg_girls_hallway'",
            "len(get_Present(location = 'bg_girls_hallway')[0]) == 2",

            "Rogue.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_girls_hallway": [
                "Player.location != 'bg_girls_hallway'",

                "chapter == 1 and season == 1",

                "EventScheduler.Events['Rogue_chapter_one_season_one_people_watching'].completed",

                "Rogue.location == 'bg_girls_hallway' and Kurt.location == 'bg_girls_hallway'",
                "len(get_Present(location = 'bg_girls_hallway')[0]) == 2",

                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Rogue_chapter_one_season_one_standoffish_part_one:
    $ ongoing_Event = True

    $ fade_to_black(0.4)

    $ temp_Rogue_name = Rogue.name
    $ temp_Kurt_name = Kurt.name

    $ Rogue.name = "???"
    $ Kurt.name = "???"

    "You're about to round a corner when you hear the tail end of a conversation."
    ch_Kurt "I don't understand."
    ch_Kurt "Zose girls asked you to go to zee mall viz zem?"
    ch_Kurt "Zey vere just trying to be polite."
    ch_Kurt "So vy did you. . . ?"
    ch_Rogue "Ah don't know, alright!"
    ch_Rogue "Kurt, please, ah know how ya are."
    ch_Rogue "You get along with everyone like biscuits 'n gravy."
    ch_Rogue "Ah ain't like that, not at all. . ."
    ch_Rogue "Never will be."

    call set_the_scene(location = "bg_girls_hallway", silent = True) from _call_set_the_scene_390

    if Rogue.sprite_position[0] >= Kurt.sprite_position[0]:
        $ Rogue.change_face("confused1", eyes = "right")
        $ Kurt.change_face("sad", eyes = "left")
    else:
        $ Rogue.change_face("confused1", eyes = "left")
        $ Kurt.change_face("sad", eyes = "right")

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_391

    $ Rogue.name = temp_Rogue_name
    $ Rogue.change_arms("crossed")

    $ Kurt.name = temp_Kurt_name
    $ Kurt.change_arms("sheepish")

    ch_Kurt "Zere is nothing wrong viz that."
    ch_Kurt "But I know vy you do it. . ."

    $ Rogue.change_face("worried1", eyes = "down")

    $ Kurt.change_arms("neutral")

    ch_Kurt "Vy you push people avay, on purpose. . ."

    pause 1.0

    call Kurt_teleports_out from _call_Kurt_teleports_out_7

    pause 1.0

    menu:
        "Approach [Rogue.name]":
            pass
        "Don't get involved":
            "[Rogue.name] lingers a little bit before walking to her room and shutting the door."

            call send_Characters(Rogue, Rogue.home, behavior = False) from _call_remove_Characters_329

            $ Rogue.wants_alone_time = 1

            $ EventScheduler.Events["Rogue_chapter_one_season_one_standoffish_part_one"].completed = False
            $ EventScheduler.Events["Rogue_chapter_one_season_one_standoffish_part_one"].completed_when = 1e8

            $ EventScheduler.Events["Rogue_chapter_one_season_one_standoffish_part_one"].counter = 0

            $ ongoing_Event = False

            return

    $ Rogue.change_face("worried2", blush = 1)
    $ Rogue.change_arms("angry")

    ch_Player "[Rogue.name]?"
    ch_Rogue "Wha. . ."
    ch_Player "I kinda heard that last bit with [Kurt.name]. . ."

    menu:
        extend ""
        "Don't mean to pry, but is everything okay? I'm here if you wanna talk or even just vent.":
            call change_Character_stat(Rogue, "love", small_stat) from _call_change_Character_stat_190
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_196

            $ Rogue.change_face("worried1", eyes = "right")
            $ Rogue.change_arms("sheepish", right_arm = "neutral")

            ch_Rogue "Ah. . . just. . . reckon everythin' is not okay. . ."
        "Are you okay? That didn't seem like a happy conversation, so if you wanted someone else to talk to. . .":
            call change_Character_stat(Rogue, "love", small_stat) from _call_change_Character_stat_197
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_209

            $ Rogue.change_face("worried1", mouth = "smirk")
            $ Rogue.change_arms("sheepish", right_arm = "neutral")

            ch_Rogue "It. . . wasn't a very happy conversation. . ."
        "Something about you not getting along with people and pushing them away? What's up with that?":
            call change_Character_stat(Rogue, "love", -small_stat) from _call_change_Character_stat_215

            $ Rogue.change_face("worried1", eyes = "down")

            ch_Rogue "It. . . ain't that simple. . ."

    $ Rogue.change_face("worried1")
    $ Rogue.change_arms("neutral", right_arm = "extended")

    ch_Rogue "[Kurt.public_name]'s a good guy. . . but he's everybody's friend."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Nothin' against him, but ah just don't think he understands where ah'm comin' from."

    $ Rogue.change_face("worried3")

    ch_Player "But, you don't think he's wrong?"

    $ Rogue.change_face("worried2")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "down")

    ch_Rogue ". . . Ah'd be lyin' if ah said ah did."

    $ Rogue.change_face("worried1", eyes = "right")
    $ Rogue.change_arms("sheepish")

    ch_Rogue "Let's not talk out here."
    ch_Rogue "Come with me to my room."

    call remove_Characters(Rogue) from _call_remove_Characters_330
    call set_the_scene(location = Rogue.home) from _call_set_the_scene_392
    call send_Characters(Rogue, Rogue.home, behavior = False) from _call_send_Characters_318

    $ Rogue.change_face("worried2")
    $ Rogue.change_arms("crossed")

    ch_Player "I'm guessing this isn't the first time this has happened?"
    ch_Player "Pushing people away, that is."
    ch_Player "[Kurt.name] seems well liked around here, but even him. . ."

    $ Rogue.change_face("worried1", eyes = "right")
    $ Rogue.change_arms("neutral", right_arm = "extended")

    ch_Rogue "Like ah said, he wouldn't understand."
    ch_Rogue "[Kurt.public_name]'s got good intentions, don't get me wrong, but it ain't so simple."

    $ Rogue.change_face("worried1")
    $ Rogue.change_arms("angry")

    ch_Rogue "He thinks he understands why ah push people away, but there ain't no way he could."

    $ Rogue.change_face("worried1", mouth = "smirk")
    $ Rogue.change_arms("hips")

    ch_Player "Well, you're not pushing me away. . ."
    ch_Rogue "No. . . yer a different story. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)
    $ Rogue.change_arms("sheepish")

    ch_Rogue "It's real easy to talk to you, and ah feel. . . more comfortable 'round you."

    $ Rogue.change_face("worried1", eyes = "right")
    $ Rogue.change_arms("neutral")

    ch_Rogue "Those girls that [Kurt.public_name] was talkin' about, they invited me to hang out at the mall with 'em."

    $ Rogue.change_face("angry1", eyes = "right")
    $ Rogue.change_arms("angry")

    ch_Rogue "Ah could see it, see the same pity in their eyes that ah saw from [Kurt.public_name]."
    ch_Rogue "They think ah'm all withdrawn because of my power, and that's why ah don't have many friends 'round here. . ."

    $ Rogue.change_face("worried1")
    $ Rogue.change_arms("sheepish", right_arm = "neutral")

    ch_Rogue "Ah'll admit that's part of it, but it ain't the whole story."

    menu:
        extend ""
        "I'm always happy to listen. Maybe I could give you a different perspective than you're used to, since I'm so new here.":
            call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_216

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Maybe you could, but as much as ah appreciate it, ah can't. . ."
        "I'm all ears if you're willing. Maybe my perspective could be useful.":
            call change_Character_stat(Rogue, "love", small_stat) from _call_change_Character_stat_383
            call change_Character_stat(Rogue, "trust", medium_stat) from _call_change_Character_stat_384

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Ah appreciate yer willingness, ah really do, but ah can't. . ."
        "Well, then give me the full story, I'm willing to listen. You can't expect people to understand your situation when they don't have all the information.":
            call change_Character_stat(Rogue, "love", -medium_stat) from _call_change_Character_stat_394

            $ Rogue.change_face("worried1", eyes = "down")

            ch_Rogue "It ain't that simple, and ah know ah'm doin' it to myself, but ah just can't. . ."

    $ Rogue.change_face("worried1", eyes = "right")
    $ Rogue.change_arms("crossed")

    ch_Rogue "Not with everythin' goin' on lately."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "But, maybe one day. . . ah'll take ya up on that."
    ch_Rogue "Ah'm just glad yer here now."
    ch_Player "Just let me know if anything changes, okay?"
    ch_Rogue "Sure, ah can do at least that much."

    $ ongoing_Event = False

    return

init python:

    def Rogue_chapter_one_season_one_standoffish_part_two_setup():
        label = "Rogue_chapter_one_season_one_standoffish_part_two_setup"

        conditions = [
            "Rogue.location not in ['hold', Player.location, Player.destination]",
            "'bg_classroom' not in [Player.location, Player.destination]",
            
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_two'].completed",

            "time_index not in Rogue.schedule.keys()",

            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",

            "day - EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_one'].completed_when >= 1",

            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_chapter_one_season_one_standoffish_part_two_setup:
    call send_Characters(Rogue, "bg_classroom", behavior = "in_class") from _call_send_Characters_319

    return

init python:

    def Rogue_chapter_one_season_one_standoffish_part_two():
        label = "Rogue_chapter_one_season_one_standoffish_part_two"

        conditions = [
            "Player.destination == 'bg_classroom'",

            "chapter == 1 and season == 1",

            "weekday < 5 and time_index < 2",

            "day - EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_one'].completed_when >= 1",

            "Rogue.destination == 'bg_classroom'",

            "Rogue.is_in_normal_mood()"]

        waiting = True
        traveling = True

        markers = {
            "bg_classroom": [
                "Player.location != 'bg_classroom'",

                "chapter == 1 and season == 1",

                "weekday < 5 and time_index < 2",

                "day - EventScheduler.Events['Rogue_chapter_one_season_one_standoffish_part_one'].completed_when >= 1",

                "Rogue.destination == 'bg_classroom'",

                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, markers = markers)

label Rogue_chapter_one_season_one_standoffish_part_two:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_classroom", show_Characters = False) from _call_set_the_scene_393

    python:
        for C in Present:
            if C != Rogue:
                send_Characters_Offscreen(C, location = "bg_classroom")
            else:
                middle_Slot = C
    
    "As you enter the classroom, you notice a few people look up from their seats at something behind you."
    "They not so discreetly point and start a hushed conversation about something."

    $ Rogue.change_face("angry1", eyes = "down")
    $ Rogue.change_arms("crossed")

    call add_Characters(Rogue, fade = False) from _call_add_Characters_95

    "You turn around and see [Rogue.name] with a cloudy expression on her face. . ."

    with small_screenshake
    
    ch_Player "Oof. . ."

    $ Rogue.change_face("worried3")
    $ Rogue.change_arms("angry")

    "She wasn't paying attention and walked right into you." 
    "[Rogue.name] stares up at you, mortified, but once she realizes it's you, she calms down a bit."

    $ Rogue.change_face("worried1", mouth = "smirk")
    $ Rogue.change_arms("sheepish", right_arm = "neutral")

    "Seems like she was listening to music and got distracted."
    "She takes out her earbuds before talking."
    ch_Rogue "Ah'm so sorry, [Player.first_name]. . ."
    ch_Player "Don't worry about it."

    menu:
        extend ""
        "Did something happen? You looked pretty upset there before bumping into me.":
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_395

            $ Rogue.change_face("worried1", eyes = "right")

            ch_Rogue "Nothin' happened, don't worry. . ."
        "I'm fine, but are {i}you{/i} okay? You looked like someone just killed your cat. . .":
            call change_Character_stat(Rogue, "love", small_stat) from _call_change_Character_stat_396
            call change_Character_stat(Rogue, "trust", small_stat) from _call_change_Character_stat_397

            $ Rogue.change_face("worried1", eyes = "right")

            ch_Rogue "Ah'm the same as ever. . ."
        "You sure? It looked like you just killed someone or something. . .":
            call change_Character_stat(Rogue, "love", -medium_stat) from _call_change_Character_stat_403
            
            $ Rogue.change_face("worried2") 
            
            pause 1.0
            
            $ Rogue.change_face("sad", eyes = "right")

            ch_Rogue "No, ah just. . ."

    $ Rogue.change_face("worried1")
    $ Rogue.change_arms("angry")

    ch_Rogue "Those girls that asked me to come to the mall came 'round earlier, but ain't nothin' bad happened. . ."
    ch_Rogue "Ah was just tryin' to keep my head down, listen to some music."

    $ Rogue.change_face("sad", eyes = "down", mouth = "smirk")
    $ Rogue.change_arms("crossed")

    ch_Rogue "Reckon ah've just got a terminal case of 'restin' bitch face.'"
    ch_Player "Nah, that can't be right."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Nothin' bitchy about it."
    ch_Player "Can I hear what song you were listening to?"

    $ Rogue.change_face("worried2", mouth = "smirk", blush = 1)
    $ Rogue.change_arms("neutral", left_arm = "extended")

    ch_Rogue "Oh! Heh, sure. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite")
    $ Rogue.change_arms("crossed")

    "She hands you an earbud, and after a few seconds you grow even more confused."
    "That is {i}not{/i} the type of song you'd expect to hear from someone who was just wearing a face like that."

    $ Rogue.change_face("worried1", mouth = "smirk")

    "After giving the earbud back, she goes to take a seat."
    "Maybe something did happen with those girls. . ."

    $ ongoing_Event = False

    return