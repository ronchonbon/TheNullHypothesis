label Rogue_rejects_cumshot_belly:
    if Rogue.belly_covered:
        $ Rogue.change_face("confused1", blush = 1) 

        ch_Rogue "You gonna do my laundry then? Thought not."
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah don't want that all over my belly."

    return

label Rogue_accepts_cumshot_belly_first_time:
    if Rogue.belly_covered:
        $ Rogue.change_face("worried1", blush = 1) 

        ch_Rogue "Ah just did laundry. . ." 
        ch_Rogue "Never mind, it's fine."
    else:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Ah guess, why not. . ."

    return

label Rogue_accepts_cumshot_belly_second_time:

    return

label Rogue_accepts_cumshot_belly:
    if Rogue.belly_covered:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Sure. . ." 
        ch_Rogue "Ah'll just wash it later."
    else:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Alright. . ."

    return

label Rogue_accepts_cumshot_belly_love:

    return

label Rogue_rejects_cumshot_breasts:
    if Rogue.breasts_covered:
        $ Rogue.change_face("worried1", blush = 1) 

        ch_Rogue "Sorry [Rogue.Player_petname], ah just washed this top." 
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah don't know if ah want that on my chest."

    return

label Rogue_accepts_cumshot_breasts_first_time:
    if Rogue.breasts_covered:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Fine [Rogue.Player_petname], ah'll just wash this top later."
    else:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Ah do wanna see how it feels on my chest."

    return

label Rogue_accepts_cumshot_breasts_second_time:

    return

label Rogue_accepts_cumshot_breasts:
    if Rogue.breasts_covered:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Okay, [Rogue.Player_petname]."
        ch_Rogue "Ah don't mind doin' laundry later." 
    else:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Ah do love the way it feels on my chest."

    return

label Rogue_accepts_cumshot_breasts_love:

    return

label Rogue_rejects_cumshot_face:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "But ah just put fresh makeup on."

    return

label Rogue_accepts_cumshot_face_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah do wanna know how it feels. . ."
    ch_Rogue "Just not in my eyes please. . ."

    return

label Rogue_accepts_cumshot_face_second_time:

    return

label Rogue_accepts_cumshot_face:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Make sure ya get it everywhere. . ."
    ch_Rogue "Please. . ."

    return

label Rogue_accepts_cumshot_face_love:

    return

label Rogue_rejects_cumshot_hair:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah ain't washin' my hair just cuz of you." 

    return

label Rogue_accepts_cumshot_hair_first_time:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "My hair?" 

    $ Rogue.change_face("smirk2", blush = 1) 

    ch_Rogue "Ah guess. . ."

    return

label Rogue_accepts_cumshot_hair_second_time:

    return

label Rogue_accepts_cumshot_hair:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Want it in my hair?" 

    $ Rogue.change_face("sexy", blush = 1) 

    ch_Rogue "Sure. . ."

    return

label Rogue_accepts_cumshot_hair_love:

    return

label Rogue_rejects_cumshot_back:
    if Rogue.back_covered:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Sorry [Rogue.Player_petname], ah just washed this top."
    else:
        $ Rogue.change_face("confused1", blush = 1) 

        ch_Rogue "Only if you wanna wipe me off afterwards. . ."

    return

label Rogue_accepts_cumshot_back_first_time:
    if Rogue.back_covered:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Fine, ah'll just wash it later."
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Fine. . ."
        ch_Rogue "But you'll have to help me clean up."

    return

label Rogue_accepts_cumshot_back_second_time:

    return

label Rogue_accepts_cumshot_back:
    if Rogue.back_covered:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Sure, ah don't mind cleanin' it later."
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Alright. . ."
        ch_Rogue "But please help me clean it up."

    return

label Rogue_accepts_cumshot_back_love:

    return

label Rogue_rejects_cumshot_ass:
    if Rogue.ass_covered:
        $ Rogue.change_face("confused1", blush = 1) 

        ch_Rogue "Ah don't want stains on these."
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Please not back there. . ."

    return

label Rogue_accepts_cumshot_ass_first_time:
    if Rogue.ass_covered:
        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ya want me to keep this on?" 
        ch_Rogue "Ah guess. . ."
    else:
        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

        ch_Rogue "On my butt?" 

        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Heh, alright."

    return

label Rogue_accepts_cumshot_ass_second_time:

    return

label Rogue_accepts_cumshot_ass:
    if Rogue.ass_covered:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Back there is fine. . ."
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "On my butt?" 

        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Cover it thoroughly."

    return

label Rogue_accepts_cumshot_ass_love:

    return

label Rogue_rejects_cumshot_feet:
    if Rogue.feet_covered:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah don't want stains on these!"
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah don't wanna feel that between my toes. . ."

    return

label Rogue_accepts_cumshot_feet_first_time:
    if Rogue.feet_covered:
        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

        ch_Rogue "With my feet covered. . . ?" 
        ch_Rogue "Ah guess. . ."
    else:
        $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

        ch_Rogue "On my feet?" 

        $ Rogue.change_face("sexy", blush = 1)

        ch_Rogue "Ah wouldn't mind seein' how it feels. . ."

    return

label Rogue_accepts_cumshot_feet_second_time:

    return

label Rogue_accepts_cumshot_feet:
    if Rogue.feet_covered:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "All over. . . ?" 
        ch_Rogue "Alright. . ."
    else:
        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Ah really like the way it feels. . ." 

        $ Rogue.change_face("sexy", blush = 2)

        ch_Rogue ". . . in between my toes."

    return

label Rogue_accepts_cumshot_feet_love:

    return

label Rogue_rejects_bukkake:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah don't want to get covered with your. . ."

    return

label Rogue_accepts_bukkake_first_time:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "All over?" 

    $ Rogue.change_face("sexy", blush = 1)

    ch_Rogue "You can try if ya want. . ."

    return

label Rogue_accepts_bukkake_second_time:

    return

label Rogue_accepts_bukkake:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "All over?" 

    $ Rogue.change_face("sexy", blush = 1)

    ch_Rogue "Please be thorough. . ."

    return

label Rogue_accepts_bukkake_love:

    return

label Rogue_rejects_clean_cum:

    return

label Rogue_accepts_clean_cum_first_time:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "It's so warm. . ."

    return

label Rogue_accepts_clean_cum_second_time:

    return

label Rogue_accepts_clean_cum:
    $ Rogue.change_face("sexy", mouth = "lipbite", blush = 1)

    return

label Rogue_accepts_clean_cum_love:

    return

label Rogue_rejects_swallow_cum:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if not Rogue.History.check("cum_in_mouth") and not Rogue.History.check("swallow_cum"):
        ch_Rogue "Ah'm not ready to taste that yet. . ."
    else:
        ch_Rogue "No. . ."

    return

label Rogue_accepts_swallow_cum_first_time:
    $ Rogue.change_face("manic", blush = 1) 

    if not Rogue.History.check("cum_in_mouth") and not Rogue.History.check("swallow_cum"):
        ch_Rogue "Ah've been wonderin' what it tastes like. . ."
    else:
        ch_Rogue "Ah guess it can't hurt. . ."

    return

label Rogue_accepts_swallow_cum_second_time:

    return

label Rogue_accepts_swallow_cum:
    $ Rogue.change_face("manic", blush = 1)

    ch_Rogue "Yum. . ."

    return

label Rogue_accepts_swallow_cum_love:

    return

label Rogue_rejects_wear_cum:
    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah can't just leave it on me!"

    return

label Rogue_accepts_wear_cum_first_time:
    $ Rogue.change_face("confused1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Just, leave it. . . ?" 

    $ Rogue.change_face("sexy", blush = 1)

    ch_Rogue "Okay. . ."

    return

label Rogue_accepts_wear_cum_second_time:

    return

label Rogue_accepts_wear_cum:
    $ Rogue.change_face("kiss1", blush = 1)

    ch_Rogue "You got it."

    return

label Rogue_accepts_wear_cum_love:

    return

label Rogue_decides_cumshot:
    $ chosen_location = None

    if renpy.random.random() > 0.25:
        $ possible_locations = []

        if Rogue.birth_control and Rogue.History.check("creampie") and approval_check(Rogue, threshold = "creampie"):
            $ possible_locations.append("creampie")
        
        if Rogue.History.check("anal_creampie") and approval_check(Rogue, threshold = "anal_creampie"):
            $ possible_locations.append("anal_creampie")
        
        if Rogue.History.check("cum_in_mouth") and approval_check(Rogue, threshold = "cum_in_mouth"):
            $ possible_locations.append("cum_in_mouth")
        
        if Rogue.History.check("cum_down_throat") and approval_check(Rogue, threshold = "cum_down_throat"):
            $ possible_locations.append("cum_down_throat")

        if possible_locations:
            $ chosen_location = renpy.random.choice(possible_locations)

            if chosen_location == "creampie":
                $ description = "pussy"
            elif chosen_location == "anal_creampie":
                $ description = "ass"
            elif chosen_location in ["cum_in_mouth", "cum_down_throat"]:
                $ description = "mouth"

            $ dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

                ch_Rogue "Yer lettin' me choose?" 

                $ Rogue.change_face("sexy", blush = 2)

                "Without a word, she takes your cock and puts it in her [description] as you blow."
            elif dice_roll == 2:
                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

                ch_Rogue "Ah'm allowed to choose?" 

                $ Rogue.change_face("sexy", blush = 2) 

                "Without a word, she takes your cock and puts it in her [description] as you blow."
    else:
        $ possible_locations = []

        if Rogue.History.check("cumshot_belly") and approval_check(Rogue, threshold = "cumshot_belly"):
            $ possible_locations.append("belly")
        
        if Rogue.History.check("cumshot_breasts") and approval_check(Rogue, threshold = "cumshot_breasts"):
            $ possible_locations.append("breasts")
        
        if Rogue.History.check("cumshot_face") and approval_check(Rogue, threshold = "cumshot_face"):
            $ possible_locations.append("face")
        
        if Rogue.History.check("cumshot_hair") and approval_check(Rogue, threshold = "cumshot_hair"):
            $ possible_locations.append("hair")
        
        if Rogue.History.check("cumshot_back") and approval_check(Rogue, threshold = "cumshot_back"):
            $ possible_locations.append("back")
        
        if Rogue.History.check("cumshot_ass") and approval_check(Rogue, threshold = "cumshot_ass"):
            $ possible_locations.append("ass")
        
        if Rogue.History.check("cumshot_feet") and approval_check(Rogue, threshold = "cumshot_feet"):
            $ possible_locations.append("feet")

        if possible_locations:
            $ chosen_location = renpy.random.choice(possible_locations)

            $ dice_roll = renpy.random.randint(1, 2)

            if dice_roll == 1:
                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

                ch_Rogue "Ah get to choose?" 

                $ Rogue.change_face("sexy", blush = 2) 

                "She aims your cock at her [chosen_location] as you blow." 
            elif dice_roll == 2:
                $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 1) 

                ch_Rogue "You want me to choose?"

                $ Rogue.change_face("sexy", blush = 2) 
                
                ch_Rogue "Thanks, [Rogue.Player_petname]."
                "She aims your cock at her [chosen_location] as you blow." 

    if chosen_location:
        return chosen_location

    return False

label Rogue_lets_Player_decide_cumshot:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 
    
    ch_Rogue "Just put it wherever ya want. . ."

    return

label Rogue_decides_clean_cum:
    $ decision_pool = ["clean_cum"]

    if approval_check(Rogue, threshold = "swallow_cum"):
        $ decision_pool.append("swallow_cum")
    
    if approval_check(Rogue, threshold = "wear_cum"):
        $ decision_pool.append("wear_cum")

    return renpy.random.choice(decision_pool)