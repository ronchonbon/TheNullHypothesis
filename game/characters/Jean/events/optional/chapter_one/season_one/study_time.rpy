init python:

    def Jean_chapter_one_season_one_study_time_setup():
        label = "Jean_chapter_one_season_one_study_time_setup"

        conditions = [
            "Jean.location not in ['hold', Player.location, Player.destination]",
            "'bg_classroom' not in [Player.location, Player.destination]",

            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Jean_chapter_one_season_one_study_time'].completed",

            "time_index not in Jean.schedule.keys()",

            "chapter == 1 and season == 1",

            "Jean.History.check('studied_with_Player')",

            "time_index >= 3",

            "Jean.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Jean_chapter_one_season_one_study_time_setup:
    call remove_Characters(location = "bg_classroom") from _call_remove_Characters_337
    call send_Characters(Jean, "bg_classroom", behavior = "studying") from _call_send_Characters_332
    
    return

init python:

    def Jean_chapter_one_season_one_study_time():
        label = "Jean_chapter_one_season_one_study_time"

        conditions = [
            "Player.destination == 'bg_classroom'",
            
            "chapter == 1 and season == 1",

            "Jean.History.check('studied_with_Player')",

            "time_index >= 3",
            
            "Jean.location == 'bg_classroom'",
            "Jean.behavior == 'studying'",
            "len(get_Present(location = 'bg_classroom')[0]) == 1",

            "Jean.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_classroom": [
                "Player.location != 'bg_classroom'",

                "chapter == 1 and season == 1",

                "Jean.History.check('studied_with_Player')",

                "time_index >= 3",
                
                "Jean.location == 'bg_classroom'",
                "Jean.behavior == 'studying'",
                "len(get_Present(location = 'bg_classroom')[0]) == 1",

                "Jean.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Jean_chapter_one_season_one_study_time:
    $ ongoing_Event = True

    $ fade_to_black(0.4)

    "As you draw near, you notice the classroom door is slightly ajar, with a dim light shining out of it."
    "You know students are allowed to make use of the classroom if a class is not in session, but this is the first time you've seen or heard of anyone actually doing it, especially this late at night."

    $ Jean.change_face("neutral", eyes = "down")
    $ Jean.change_arms("crossed")

    call set_the_scene(location = "bg_classroom") from _call_set_the_scene_400

    "Peering through the doorway, you see [Jean.name] studying at a desk."
    "She's looking back and forth between a textbook and her own notes, highlighting passages and scribbling things down."

    menu:
        extend ""
        "Knock on the door":
            pass
        "Try not to disturb [Jean.name]":
            $ Jean.change_face("angry1", eyes = "down")
            $ Jean.change_arms("angry")

            "[Jean.name] frowns at her notes, looking like she's pleading with them to make sense."
            "She's so engrossed by what she's doing that she doesn't seem to notice you at all."
            "You head out, leaving her be."

            $ EventScheduler.Events["Jean_chapter_one_season_one_study_time"].completed = False
            $ EventScheduler.Events["Jean_chapter_one_season_one_study_time"].completed_when = 1e8

            $ EventScheduler.Events["Jean_chapter_one_season_one_study_time"].counter = 0

            call move_location("bg_hallway") from _call_move_location_55

            $ ongoing_Event = False

            return

    $ Jean.change_face("surprised3") 
    $ Jean.change_arms("angry")
    
    "She jumps up out of her chair, startled." 
    
    $ Jean.change_face("perplexed") 
    $ Jean.change_arms("hips")
    
    "It takes her a minute to notice you by the door."

    $ Jean.change_face("confused2", eyes = "left")
    $ Jean.change_arms("sass")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Jean "Sorry, didn't notice you there."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "You ever get so wrapped up in something, you wind up dead to the world?"
    ch_Player "Don't worry about it, happens to me all the time. I'm not interrupting anything, am I?"

    $ Jean.change_face("furious", eyes = "down")
    $ Jean.change_arms("angry")

    ch_Jean "Ugh, it's these stupid notes. Or this stupid textbook. Possibly both." 
    "She plops back down in her chair rubbing her temples."

    $ Jean.change_face("angry1")
    $ Jean.change_arms("angry", right_arm = "extended")

    ch_Jean "I had a test last week. I got almost everything right, but apparently, my understanding of this one part was. . ."

    $ Jean.change_face("angry1", eyes = "down")
    $ Jean.change_arms("crossed")

    ch_Jean ". . . lacking."

    $ Jean.change_face("neutral")

    ch_Jean "It's all about the function of melatonin on cortisol, how it. . ."

    $ Jean.change_face("worried1")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "Sorry, you probably don't want to hear about all this."
    "You look down at the crumpled sheets of paper [Jean.name]'s been writing on. So much has been written, scored out, scribbled over and highlighted, it looks more like abstract art than study notes, but apparently this method works for her."

    $ Jean.change_face("confused1")

    ch_Player "Did it count for much?"

    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "About fifteen percent of our entire test grade."

    $ Jean.change_face("worried3")
    $ Jean.change_arms("shrug")

    ch_Jean "Don't get me wrong, I still passed, easily, but. . ."

    $ Jean.change_face("worried1", eyes = "down")
    $ Jean.change_arms("angry")

    ch_Jean "I don't know. I feel like I should be better than that."
    ch_Player "Fifteen percent isn't that much, is it?"

    $ Jean.change_face("worried2")
    $ Jean.change_arms("angry", right_arm = "extended")

    ch_Jean "No, not really, but. . . it really annoys me, you know?"
    ch_Player "So how come you're studying here and not in your room or something?"

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("crossed")

    ch_Jean "Honestly, I find it easier. There's always something going on in the dorms at night: music, shouting, people running around."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "I can't imagine your wing of the mansion being much different."
    ch_Jean "And the library's basically the same, people treat it like a second common room."

    $ Jean.change_face("worried1")

    ch_Jean "But in here, there's no distractions, no noise. Nobody's ever here past six, seven o'clock."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "And there's something about being in a classroom that makes you feel like learning, you know?"
    ch_Player "Makes sense. You study in here often?"

    $ Jean.change_face("pleased1")
    $ Jean.change_arms("neutral")

    ch_Jean "Heh, all the time. If you look closely on some of the desks, you can probably see little impressions of my face from where I've fallen asleep."
    "She laughs it off, but the laugh sounds hollow, and you sense a real sadness behind her words."

    menu:
        extend ""
        "Well, as long as you're not pushing yourself harder than you can take.":
            call change_Character_stat(Jean, "love", medium_stat) from _call_change_Character_stat_164
            call change_Character_stat(Jean, "trust", medium_stat) from _call_change_Character_stat_165
            
            $ Jean.change_face("worried1", mouth = "smirk", eyes = "right")
            $ Jean.change_arms("crossed")           

            ch_Jean "I mean, I probably am, but I can catch up on sleep when all this is over, right?"
        "That's crazy, you do this all the time?":
            call change_Character_stat(Jean, "love", -small_stat) from _call_change_Character_stat_166
            
            $ Jean.change_face("worried1", mouth = "smirk")
            $ Jean.change_arms("crossed")       

            ch_Jean "It's the sacrifice we have to pay for the top grade."
        "I think you're the only person I've ever met who willingly spends time in class when they don't have to.":
            call change_Character_stat(Jean, "love", small_stat) from _call_change_Character_stat_167
            call change_Character_stat(Jean, "trust", -small_stat) from _call_change_Character_stat_168
            
            $ Jean.change_face("confused1", mouth = "smirk")
            $ Jean.change_arms("crossed")        

            ch_Jean "Honestly, I'm actually grateful for that. It means I know I can get peace and quiet whenever I want."

    $ Jean.change_face("worried1")

    ch_Jean "And besides, if you want the top grade, you have to do whatever it takes. Even if you'd rather be doing anything else. . ." 

    $ Jean.change_face("worried1", eyes = "right")

    "You get the feeling she's talking to herself more than anyone. After a moment, she shakes herself out of her reverie and gives you a smile."

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("sass")       

    ch_Player "Anyways, I'll let you get back to it."
    ch_Player "Just. . . try not to be too hard on yourself or stay up too late."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "I'll try."

    $ Jean.change_face("sad", eyes = "down")

    "Looking back as you leave, you see [Jean.name] with her head buried in the textbook again, looking every bit as stressed as she did before you arrived."

    call move_location("bg_hallway") from _call_move_location_60

    $ ongoing_Event = False

    return