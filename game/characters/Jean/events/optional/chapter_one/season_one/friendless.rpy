define ch_bully = Character("???")

init python:

    def Jean_chapter_one_season_one_friendless_setup():
        label = "Jean_chapter_one_season_one_friendless_setup"

        conditions = [
            "Jean.location not in ['hold', Player.location, Player.destination]",
            "'bg_danger' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Jean_chapter_one_season_one_friendless'].completed",

            "time_index not in Jean.schedule.keys()",

            "chapter == 1 and season == 1",

            "Jean.History.check('trained_with_Player', tracker = 'season') >= 2",
            
            "time_index < 3",

            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_chapter_one_season_one_friendless_setup:
    call send_Characters(Jean, "bg_danger", behavior = "training") from _call_send_Characters_331
    
    return

init python:

    def Jean_chapter_one_season_one_friendless():
        label = "Jean_chapter_one_season_one_friendless"

        conditions = [
            "Player.destination == 'bg_danger'",

            "chapter == 1 and season == 1",

            "Jean.History.check('trained_with_Player', tracker = 'season') >= 2",
            
            "time_index < 3",
            
            "Jean.location == 'bg_danger'",
            "Jean.behavior == 'training'",
            "len(get_Present(location = 'bg_danger')[0]) == 1",

            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_danger": [
                "Player.location != 'bg_danger'",

                "chapter == 1 and season == 1",

                "Jean.History.check('trained_with_Player', tracker = 'season') >= 2",
                
                "time_index < 3",
                
                "Jean.location == 'bg_danger'",
                "Jean.behavior == 'training'",
                "len(get_Present(location = 'bg_danger')[0]) == 1",
                
                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Jean_chapter_one_season_one_friendless:
    $ ongoing_Event = True

    call set_the_scene(location = "bg_danger", show_Characters = False) from _call_set_the_scene_398

    "You spot [Jean.name] across the room talking to a couple girls you don't recognize."

    call show_Character(Jean, x = stage_far_right) from _call_show_Character_16

    $ Jean.change_face("worried1", eyes = "left")
    $ Jean.change_arms("crossed")

    ch_bully "Seriously?"
    ch_bully "If you think you're that much better than us, just say it."

    $ Jean.change_face("confused1", eyes = "left")

    ch_bully "Stop making excuses. {i}Nobody{/i} needs to study {i}that{/i} much."
    ch_bully "You just don't wanna hang out with us, we get it."

    $ Jean.change_face("angry1", eyes = "left")
    $ Jean.change_arms("angry")

    ch_Jean "It's not just an excuse!"
    ch_Jean "This exam counts for like a third of our entire grade."

    $ Jean.change_face("worried1", eyes = "left")

    ch_bully "It's not like you haven't been studying constantly for the past few weeks!"
    ch_bully "Whatever, we're leaving."
    "The girls leave looking very irritated. [Jean.name] just watches them go."

    $ Jean.change_face("worried1", eyes = "down")
    $ Jean.change_arms("crossed")

    menu:
        extend ""
        "Go up to [Jean.name]":
            pass
        "Don't involve yourself":
            "You keep your distance and don't get involved."

            call remove_Characters(Jean) from _call_remove_Characters_327

            $ EventScheduler.Events["Jean_chapter_one_season_one_friendless"].completed = False
            $ EventScheduler.Events["Jean_chapter_one_season_one_friendless"].completed_when = 1e8

            $ EventScheduler.Events["Jean_chapter_one_season_one_friendless"].counter = 0

            $ ongoing_Event = False

            return

    call swap_Slots(Jean, "middle") from _call_swap_Slots_4

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms(left_arm = "rub_neck", right_arm = "neutral")

    "As you approach, [Jean.name] looks up and gives you a sad smile."
    ch_Jean "You saw all that, huh?"

    $ Jean.change_face("worried1", eyes = "left")
    $ Jean.change_arms("neutral")

    ch_Player "Yeah. . . they weren't being very subtle."
    ch_Player "Friends of yours?"

    $ Jean.change_face("worried1")
    $ Jean.change_arms("crossed")

    ch_Jean "Maybe at one point."
    ch_Jean "Don't see why they'd wanna be now. . ."

    $ Jean.change_face("worried1", eyes = "left")

    ch_Jean ". . . Not really sure I blame them either."

    menu:
        extend ""
        "Hey, it's their loss. I wouldn't want to be friends with people who can't respect what's important to me.":
            call change_Character_stat(Jean, "love", small_stat) from _call_change_Character_stat_132
            call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_133
            
            $ Jean.change_face("worried1", mouth = "smirk")

            ch_Jean "I guess you're right. . . but I wouldn't even wanna be friends with me if I was in their shoes."
        "Maybe you're better off without them. Real friends would realize how important your grades are to you and not make it about themselves.":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_134
            call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_161
            
            $ Jean.change_face("worried1", mouth = "smirk")

            ch_Jean "Maybe. . . but if I was in their shoes, I'd probably feel the same way."
        "What did you expect when you prioritize books over people. . . but they seemed like assholes anyways, making it all about themselves.":
            call change_Character_stat(Jean, "love", -medium_stat) from _call_change_Character_stat_162
            call change_Character_stat(Jean, "trust", small_stat) from _call_change_Character_stat_163
            
            $ Jean.change_face("worried1")

            ch_Jean "I don't know what I expected. . . not like it wasn't obvious how they were starting to feel."

    $ Jean.change_face("suspicious1")
    $ Jean.change_arms("angry")

    ch_Jean "And don't tell me I'm being ridiculous."

    $ Jean.change_face("worried2")
    $ Jean.change_arms("neutral")

    ch_Player "I. . . wasn't about to. . ."

    $ Jean.change_face("worried1", eyes = "left")
    $ Jean.change_arms(left_arm = "rub_neck", right_arm = "neutral")

    ch_Jean "Oh, sorry."
    ch_Jean "I'm just used to that sort of response."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("crossed")

    ch_Jean "But those girls just don't understand."

    $ Jean.change_face("worried3")

    ch_Jean "I {i}need{/i} to keep my grades top of the class."
    ch_Jean "I have so many years invested in keeping my spot, slowing down now would be such a waste. . ."

    $ Jean.change_face("worried1", eyes = "left")

    ch_Player "You don't have to convince me."

    $ Jean.change_face("confused2")
    $ Jean.change_arms("angry")

    ch_Player "But maybe you're just trying to convince yourself?"
    "You see a wave of confusion roll over [Jean.name]'s face, before a determined expression takes shape."

    $ Jean.change_face("angry1")
    $ Jean.change_arms("sass")

    ch_Jean "No, that's not it."

    $ Jean.change_face("angry1", eyes = "left")

    ch_Jean "Why would I need to convince myself?"
    ch_Jean "I know why I'm doing this."

    $ Jean.change_face("neutral")
    $ Jean.change_arms("neutral")

    ch_Jean "Anyway, I really do have to go study."

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("crossed")

    ch_Jean "Thanks for caring, it's cute."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "left")

    "[Jean.name] starts to leave but only makes it a few steps before looking over her shoulder at you."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("neutral", right_arm = "extended")

    ch_Jean "It'll be worth it. . . right?"
    ch_Player "Tha-"

    $ Jean.change_face("neutral", eyes = "left")
    $ Jean.change_arms("neutral")

    "Before you can finish she answers her own question."
    ch_Jean "Right. What am I saying, of course it will be. . ."

    call remove_Characters(Jean) from _call_remove_Characters_336

    $ ongoing_Event = False

    return