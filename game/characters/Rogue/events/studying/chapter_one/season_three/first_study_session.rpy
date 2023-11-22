init python:

    def Rogue_chapter_one_season_three_first_study_session():
        label = "Rogue_chapter_one_season_three_first_study_session"

        conditions = [
            "chapter == 1 and season == 3",
            
            "not Rogue.History.check('studied_with_Player', tracker = 'season')",

            "Player.behavior == 'studying' and Rogue in Player.behavior_Partners and Rogue.behavior == 'studying'"]

        priority = 99

        return EventClass(label, conditions, priority = priority)

label Rogue_chapter_one_season_three_first_study_session:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "So, wanna go easy or study hard today, [Rogue.Player_petname]?"

    if Player.History.check("studied") >= 12:
        ch_Player "I've been doing pretty well in class, but we should still at least try a bit."
    else:
        ch_Player "I've been doing. . . okay in class so far. . ." 
        ch_Player "Should probably try a bit today."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Anythin's good with me."

    $ Rogue.change_face("smirk2", eyes = "down")

    "You tell her which class you've been struggling with the most, and she helps you set everything up."

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    "[Rogue.name] hops onto the bed, beckoning you to lay down next to her."
    "Once you do, she leans into your shoulder."

    $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

    "[Rogue.name] has also been struggling with the material, so you end up helping her just as much."

    $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

    "As you both go through study guides and previous assignments, you absentmindedly put your hand out for her to touch."

    $ Rogue.change_face("smirk2", eyes = "down", blush = 2)

    call take_off(Rogue, "gloves") from _call_take_off_15

    "Without taking her eyes off of the material, she takes her gloves off and touches your hand while doing a practice question."

    $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp], any idea how to do this question?"
    "She points to a particularly difficult question."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Player "I think I remember reading about that in the textbook."
    "You find the textbook chapter in question."
    ch_Player "Here it is, so that means it should be choice B."

    $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

    "The session flies by and is quite productive, as you both help each other learn a lot."

    $ Rogue.change_face("smirk2", blush = 1)

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_48

    "She reluctantly pulls her hand away, putting her gloves back on, before helping you clean everything up."

    $ ongoing_Event = False

    return