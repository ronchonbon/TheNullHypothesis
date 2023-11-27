init python:

    def Rogue_chapter_one_season_one_people_watching_setup():
        label = "Rogue_chapter_one_season_one_people_watching_setup"

        conditions = [
            "Rogue.location not in ['hold', Player.location, Player.destination]",
            
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Rogue_chapter_one_season_one_people_watching'].completed",

            "time_index not in Rogue.schedule.keys()",

            "chapter == 1 and season == 1",

            "time_index < 3",
            "weather != 'rain'",    

            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Rogue_chapter_one_season_one_people_watching_setup:
    call remove_Characters(location = "bg_campus") from _call_remove_Characters_331
    call send_Characters(Rogue, "bg_campus", behavior = False) from _call_send_Characters_315

    return

init python:

    def Rogue_chapter_one_season_one_people_watching():
        label = "Rogue_chapter_one_season_one_people_watching"

        conditions = [
            "Player.destination == 'bg_campus'",

            "chapter == 1 and season == 1",

            "time_index < 3",
            "weather != 'rain'",    

            "Rogue.location == 'bg_campus'",
            "len(get_Present(location = 'bg_campus')) == 1",

            "Rogue.is_in_normal_mood()"]

        traveling = True

        markers = {
            "bg_campus": [
                "Player.location != 'bg_campus'",

                "chapter == 1 and season == 1",

                "time_index < 3",
                "weather != 'rain'",    

                "Rogue.location == 'bg_campus'",
                "len(get_Present(location = 'bg_campus')) == 1",

                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Rogue_chapter_one_season_one_people_watching:
    $ ongoing_Event = True

    $ Rogue.eyes = "left"

    call set_the_scene(location = "bg_campus") from _call_set_the_scene_389

    "Walking across campus, you notice [Rogue.name] sitting alone on a bench near one of the footpaths, glancing at people as they walk past."

    menu:
        extend ""
        "See what [Rogue.name]'s up to":
            pass
        "Mind your own business":
            $ EventScheduler.Events["Rogue_chapter_one_season_one_people_watching"].completed = False
            $ EventScheduler.Events["Rogue_chapter_one_season_one_people_watching"].completed_when = 1e8

            $ EventScheduler.Events["Rogue_chapter_one_season_one_people_watching"].counter = 0

            $ ongoing_Event = False

            return

    call remove_everyone_but(Rogue) from _call_remove_everyone_but_11

    $ Rogue.change_face("neutral") 

    "Catching her eye, you nod to her and walk over to say hi."

    $ Rogue.change_face("confused1") 

    ch_Player "Hey, [Rogue.name], what are you up to?"

    $ Rogue.change_face("neutral", eyes = "right") 

    "She just shrugs."
    ch_Rogue "Ah've been stuck in my room all day, wanted to come out for some fresh air."
    ch_Player "I've seen you sitting here a couple of times. You like the view that much?"

    $ Rogue.change_face("confused1", eyes = "squint")

    ch_Rogue "What, you been followin' me or somethin'?"
    ch_Player "No, nothing like that, just noticed you seem to like this bench a lot."

    $ Rogue.change_face("worried1")

    ch_Rogue "Oh."

    $ Rogue.change_face("worried1", eyes = "right")

    "She looks slightly embarrassed. There's an odd silence before she speaks again."

    $ Rogue.change_face("worried1") 

    ch_Rogue "Nah, it's nothin' like that, it's. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Lord, this is gonna sound weird as hell."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "I have a friend covered head to literal tail in blue fur. My bar for 'weird' has shifted significantly since I arrived here."

    $ Rogue.change_face("smirk2") 

    ch_Rogue "Fair point."

    $ Rogue.change_face("worried1")

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Sigh. . ."
    ch_Rogue "Ah come here 'cause it. . . it makes me feel a little less alone."

    menu:
        extend ""
        "You sit alone to feel. . . less alone?":   
            call change_Girl_stat(Rogue, "love", small_stat) from _call_change_Girl_stat_138

            $ Rogue.change_face("confused1", mouth = "smirk")

            ch_Rogue "Yeah, that's. . . that ain't exactly what ah mean."
        "Because you're surrounded by other people?":
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_140
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_141

            $ Rogue.change_face("confused1")

            ch_Rogue "Ah mean. . . kinda?"
        "Maybe being out is good for you then? Staying cooped up doesn't help anyone.":
            call change_Girl_stat(Rogue, "trust", small_stat) from _call_change_Girl_stat_159

            $ Rogue.change_face("angry1")

            ch_Rogue "Ah don't think you're really understandin' what ah'm really sayin' here."

    $ Rogue.change_face("worried1")

    ch_Rogue "Ya know how my powers make it hard for me to be near people?"

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Well, so does most everyone else here."
    ch_Rogue "Ah take every precaution to avoid touchin' people, but there's always the risk, 'n ah can't really blame people for avoidin' me because of it. . ."
    ch_Rogue ". . . that don't mean it doesn't still really suck."

    $ Rogue.change_face("worried1")

    ch_Rogue "Every now 'n then, it just hits a little harder than usual."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "So ah sit here, ah watch the people goin' by, 'n for a moment ah feel like a part of someone else's world."
    ch_Rogue "Ah hear 'em talk 'n it almost feels like ah'm part of the conversation."

    $ Rogue.change_face("worried2")

    ch_Rogue "Ah know it's not quite the same thing, but. . . it helps, even just a little, y'know?"

    $ Rogue.change_face("worried3")

    pause 0.5

    $ Rogue.change_face("worried1", eyes = "down")

    "She shakes her head, suddenly very self-conscious."

    $ Rogue.change_face("angry1", eyes = "down")

    menu:
        extend ""
        "I don't know if I exactly get it, but if it helps you, it can't be all bad, right?":
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_160
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_180

            $ Rogue.change_face("worried2")

            ch_Rogue ". . . really? That's. . . that's sweet of you to say so, thanks."
        "As long as you're not keeping detailed lists of what everyone's up to, I think it's okay.":
            call change_Girl_stat(Rogue, "love", medium_stat) from _call_change_Girl_stat_181
            
            $ Rogue.change_face("confused1", mouth = "smirk")

            ch_Rogue "Ha! Some of the stuff ah've heard, maybe ah should think about it!"
        "I've heard of worse coping mechanisms.":
            call change_Girl_stat(Rogue, "love", small_stat) from _call_change_Girl_stat_182
            call change_Girl_stat(Rogue, "trust", medium_stat) from _call_change_Girl_stat_183

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "Sure it ain't the worst one, but it's still kinda silly, right?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Anyway, thanks for listenin' without bein' all judgey about it."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "It's a weird thing to do, ah know, but with how things are for me, it's kinda hard for me to be social."
    ch_Player "Well, any time you want to hang-"

    $ Rogue.change_face("neutral", eyes = "down")

    call phone_buzz(times = 3) from _call_phone_buzz_11

    "You're stopped by the sound of [Rogue.name]'s phone going off in her pocket. She takes it out, looks at the screen, and hesitates."

    $ Rogue.change_face("confused1", eyes = "down")

    pause 0.5

    $ Rogue.change_face("angry1", eyes = "down")

    "For a second, there's a flash of anger on her face and she looks like she's about to throw it across the grounds, but she stops."

    $ Rogue.change_face("worried2")

    ch_Rogue "Hey, sorry, but. . . ah gotta take this, it's important."

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Do you. . . do you think we can talk later? Maybe?"

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "Sure, whenever you want."
    ch_Rogue "Thanks. Ah mean it."

    call remove_Characters(Rogue) from _call_remove_Characters_328

    "She heads off and takes the call."
    "You can't hear what she's saying, but by the tone of her voice, it's not good."
    "You sit for another minute or two before heading back on your way."

    $ ongoing_Event = False

    return