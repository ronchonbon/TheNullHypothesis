init python:

    def Laura_Rogue_hasnt_seen_penis_setup():
        label = "Laura_Rogue_hasnt_seen_penis_setup"

        conditions = [
            "Laura.location not in ['hold', Player.location]",
            "Rogue.location not in ['hold', Player.location]",
            
            "renpy.random.random() > 0.75",

            "not EventScheduler.Events['Laura_Rogue_hasnt_seen_penis'].completed",

            "time_index not in Laura.schedule.keys()",
            "time_index not in Rogue.schedule.keys()",

            "Rogue.History.check('seen_Player_naked') and not Laura.History.check('seen_Player_naked') and Laura in Partners and Rogue in Partners and Rogue in Laura.knows_about and Laura in Rogue.knows_about",

            "Laura.is_in_normal_mood()",
            "Rogue.is_in_normal_mood()"]

        repeatable = True
        automatic = True

        return EventClass(label, conditions, repeatable = repeatable, automatic = automatic)

label Laura_Rogue_hasnt_seen_penis_setup:
    call send_Characters(Laura, Laura.home, behavior = False) from _call_send_Characters_309
    call send_Characters(Rogue, Laura.home, behavior = False) from _call_send_Characters_310

    return

init python:

    def Laura_Rogue_hasnt_seen_penis():
        label = "Laura_Rogue_hasnt_seen_penis"

        conditions = [
            "Player.destination == Laura.home",

            "Laura.location == Laura.home and Rogue.location == Laura.home",

            "Rogue.History.check('seen_Player_naked') and not Laura.History.check('seen_Player_naked') and Laura in Partners and Rogue in Partners and Rogue in Laura.knows_about and Laura in Rogue.knows_about",

            "Laura.is_in_normal_mood()",
            "Rogue.is_in_normal_mood()"]

        traveling = True

        markers = {
            Laura.home: [
                "Player.location != Laura.home",
                
                "Laura.location == Laura.home and Rogue.location == Laura.home",

                "Rogue.History.check('seen_Player_naked') and not Laura.History.check('seen_Player_naked') and Laura in Partners and Rogue in Partners and Rogue in Laura.knows_about and Laura in Rogue.knows_about",

                "Laura.is_in_normal_mood()",
                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, markers = markers)

label Laura_Rogue_hasnt_seen_penis:
    $ ongoing_Event = True

    $ Laura.temp = Laura.name
    $ Laura.name = "???"

    $ Rogue.temp = Rogue.name
    $ Rogue.name = "???"

    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_110
    
    ch_Laura "I want to see his. . ."
    ch_Laura "I can't stop thinking about it. . ."
    ch_Rogue "He hasn't shown ya yet?"
    ch_Rogue "Ah would've thought. . . {size=-5}since ah've seen it already{/size}. . ."
    ch_Laura "WHAT?!"
    ch_Laura ". . ."
    ch_Laura "{size=-5}What did it look like{/size}. . ."
    ch_Laura "{size=-5}I've never seen a real one{/size}. . ."
    ch_Rogue "Lord. . . ah'll just say it was everthin' ya could hope for. . ."
    ch_Laura "{i}Grrrrrr{/i}. . ."
        
    call knock_on_door(times = 2) from _call_knock_on_door_5

    ch_Player "[Laura.name], you home?"
    ch_Laura "Yes, come in."
    ch_Rogue "Wait!"

    $ Laura.name = Laura.temp

    $ Rogue.name = Rogue.temp

    call set_the_scene(location = Laura.home) from _call_set_the_scene_111
    
    $ Laura.change_face("furious")
    
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Laura "We were just talking about you."

    $ Laura.change_face("suspicious2")
    
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Sorry. . ."

    $ Laura.change_face("confused1", eyes = "right")

    ch_Rogue "Ah'm gonna head out."
    ch_Rogue "Bye."

    call remove_Characters(Rogue) from _call_remove_Characters_98

    $ ongoing_Event = False

    return