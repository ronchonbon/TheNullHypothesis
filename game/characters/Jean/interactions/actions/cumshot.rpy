label Jean_rejects_cumshot_belly:
    if Jean.belly_covered:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "Maybe you actually wanna do my laundry?" 
        ch_Jean ". . . No? Then not happening."
    else:
        $ Jean.change_face("confused1", blush = 1)

        ch_Jean "Don't want that stuff on my stomach."

    return

label Jean_accepts_cumshot_belly_first_time:
    if Jean.belly_covered:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "Fine, but you'll be doing both our laundry, [Jean.Player_petname]."
    else:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "You like my belly?"

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Can't say I get it, but fine."

    return

label Jean_accepts_cumshot_belly_second_time:

    return

label Jean_accepts_cumshot_stomach:
    if Jean.belly_covered:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Fine."
        ch_Jean "I'll just wash this top again."
    else:
        $ Jean.change_face("sly", mouth = "smirk", blush = 1)

        ch_Jean "Sure."

    return

label Jean_accepts_cumshot_belly_love:

    return

label Jean_rejects_cumshot_breasts:
    if Jean.breasts_covered:
        $ Jean.change_face("confused1", blush = 1)

        ch_Jean "This top is brand new, aim somewhere else."
    else:
        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Jean "You really like my tits, huh?" 

        $ Jean.change_face("neutral", eyes = "squint", blush = 1)

        ch_Jean "Too bad."

    return

label Jean_accepts_cumshot_breasts_first_time:
    if Jean.breasts_covered:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "Fine, I'll just wash it later."
    else:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "You're really obsessed with them, huh?"  

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 2)

        ch_Jean "I'll allow it."

    return

label Jean_accepts_cumshot_breasts_second_time:

    return

label Jean_accepts_cumshot_breasts:
    if Jean.breasts_covered:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Go for it."
    else:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Cum all over my tits, [Jean.Player_petname]."

    return

label Jean_accepts_cumshot_breasts_love:

    return

label Jean_rejects_cumshot_face:
    $ Jean.change_face("neutral", eyes = "squint", blush = 1)

    ch_Jean "I did my makeup just for you, not gonna let you ruin it."

    return

label Jean_accepts_cumshot_face_first_time:
    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "I just did my makeup though. . ."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Oh fuck it."

    return

label Jean_accepts_cumshot_face_second_time:

    return

label Jean_accepts_cumshot_face:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Do it."

    return

label Jean_accepts_cumshot_face_love:

    return

label Jean_rejects_cumshot_hair:
    $ Jean.change_face("neutral", eyes = "squint", blush = 1)

    ch_Jean "I don't want that stuff in my hair."  

    return

label Jean_accepts_cumshot_hair_first_time:
    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "In my hair?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Screw it." 

    return

label Jean_accepts_cumshot_hair_second_time:

    return

label Jean_accepts_cumshot_hair:
    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "My hair again?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Jean "Screw it." 

    return

label Jean_accepts_cumshot_hair_love:

    return

label Jean_rejects_cumshot_back:
    if Jean.back_covered:
        $ Jean.change_face("neutral", eyes = "squint", blush = 1)

        ch_Jean "Not there, this is a fresh top."
    else:
        $ Jean.change_face("confused1", blush = 1)

        ch_Jean "Not the back."

    return

label Jean_accepts_cumshot_back_first_time:
    if Jean.back_covered:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "But this is a fresh top. . ." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Oh whatever, fine."
    else:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "If you help clean me up after."

    return

label Jean_accepts_cumshot_back_second_time:

    return

label Jean_accepts_cumshot_back:
    if Jean.back_covered:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Oh whatever, fine."
        ch_Jean "It's easy to clean."
    else:
        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Fine, but you better help clean me up."

    return

label Jean_accepts_cumshot_back_love:

    return

label Jean_rejects_cumshot_ass:
    if Jean.ass_covered:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "I don't want stains, [Jean.Player_petname]."
    else:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "I know my ass is perfect, but don't get anything on it."

    return

label Jean_accepts_cumshot_ass_first_time:
    if Jean.ass_covered:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "It probably won't stain. . ."

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Sure, [Jean.Player_petname]."
    else:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "I know it is perfect."
        ch_Jean "Fine."

    return

label Jean_accepts_cumshot_ass_second_time:

    return

label Jean_accepts_cumshot_ass:
    if Jean.ass_covered:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Sure, [Jean.Player_petname]."
        ch_Jean "But you're doing laundry later."
    else:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Get it all over. . ."

    return

label Jean_accepts_cumshot_ass_love:

    return

label Jean_rejects_cumshot_feet:
    if Jean.feet_covered:
        $ Jean.change_face("neutral", eyes = "squint", blush = 1)

        ch_Jean "I really like these, no stains."
    else:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "I don't want that stuff on my feet, sorry [Jean.Player_petname]."

    return

label Jean_accepts_cumshot_feet_first_time:
    if Jean.feet_covered:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "But I really like these. . ." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Okay fine."
    else:
        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "You really are into my feet, huh?" 

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Heh, okay fine. Weirdo."

    return

label Jean_accepts_cumshot_feet_second_time:

    return

label Jean_accepts_cumshot_feet:
    if Jean.feet_covered:
        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Jean "They weren't that hard to clean last time. . ." 

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "Fine."
    else:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "What are you waiting for?"

    return

label Jean_accepts_cumshot_feet_love:

    return

label Jean_rejects_bukkake:
    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "Not all over. I just took a shower."

    return

label Jean_accepts_bukkake_first_time:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 1) 

    ch_Jean "All over?" 

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Jean "Do you even have enough. . . to cover everything?"

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "Whatever, we can just take a shower after I guess."

    return

label Jean_accepts_bukkake_second_time:

    return

label Jean_accepts_bukkake:
    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 1) 

    ch_Jean "Again?" 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 

    ch_Jean "Like seeing me get covered?" 

    return

label Jean_accepts_bukkake_love:

    return

label Jean_rejects_clean_cum:

    return

label Jean_accepts_clean_cum_first_time:
    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "It's really gooey. . ."

    return

label Jean_accepts_clean_cum_second_time:

    return

label Jean_accepts_clean_cum:
    $ Jean.change_face("sexy", blush = 1)
    
    ch_Jean "Like watching me clean off your cum?"

    return

label Jean_accepts_clean_cum_love:

    return

label Jean_rejects_swallow_cum:
    $ Jean.change_face("worried1", blush = 1)

    if not Jean.History.check("cum_in_mouth") and not Jean.History.check("swallow_cum"):
        ch_Jean "I don't really wanna try tasting that stuff. . ."
    else:
        ch_Jean "No. . ."

    return

label Jean_accepts_swallow_cum_first_time:
    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    if not Jean.History.check("cum_in_mouth") and not Jean.History.check("swallow_cum"):
        ch_Jean "I have been wondering what it tastes like. . ."
    else:
        ch_Jean "Hmm. . . okay. . ."

    return

label Jean_accepts_swallow_cum_second_time:

    return

label Jean_accepts_swallow_cum:
    $ Jean.change_face("sly", blush = 1)

    ch_Jean "Happily. . ."

    return

label Jean_accepts_swallow_cum_love:

    return

label Jean_rejects_wear_cum:
    $ Jean.change_face("apalled1", blush = 2)

    ch_Jean "There's no way I'm just 'leaving it there'!"

    return

label Jean_accepts_wear_cum_first_time:
    $ Jean.change_face("worried1", blush = 1)

    ch_Jean "You sure it's not. . . too. . . {i}slutty{/i}?"

    return

label Jean_accepts_wear_cum_second_time:

    return

label Jean_accepts_wear_cum:
    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Mmm."

    return

label Jean_accepts_wear_cum_love:

    return

label Jean_decides_cumshot:
    $ chosen_location = None

    if renpy.random.random() > 0.25:
        $ possible_locations = []

        if Jean.birth_control and Jean.History.check("creampie") and approval_check(Jean, threshold = "creampie"):
            $ possible_locations.append("creampie")
        
        if Jean.History.check("anal_creampie") and approval_check(Jean, threshold = "anal_creampie"):
            $ possible_locations.append("anal_creampie")
        
        if Jean.History.check("cum_in_mouth") and approval_check(Jean, threshold = "cum_in_mouth"):
            $ possible_locations.append("cum_in_mouth")
        
        if Jean.History.check("cum_down_throat") and approval_check(Jean, threshold = "cum_down_throat"):
            $ possible_locations.append("cum_down_throat")

        if possible_locations:
            $ chosen_location = renpy.random.choice(possible_locations)

            if chosen_location == "creampie":
                $ description = "pussy"
            elif chosen_location == "anal_creampie":
                $ description = "ass"
            elif chosen_location in ["cum_in_mouth", "cum_down_throat"]:
                $ description = "mouth"

            $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

            "Without a word, she takes your cock and puts it in her [description] as you blow."
    else:
        $ possible_locations = []

        if Jean.History.check("cumshot_belly") and approval_check(Jean, threshold = "cumshot_belly"):
            $ possible_locations.append("belly")
        
        if Jean.History.check("cumshot_breasts") and approval_check(Jean, threshold = "cumshot_breasts"):
            $ possible_locations.append("breasts")
        
        if Jean.History.check("cumshot_face") and approval_check(Jean, threshold = "cumshot_face"):
            $ possible_locations.append("face")
        
        if Jean.History.check("cumshot_hair") and approval_check(Jean, threshold = "cumshot_hair"):
            $ possible_locations.append("hair")
        
        if Jean.History.check("cumshot_back") and approval_check(Jean, threshold = "cumshot_back"):
            $ possible_locations.append("back")
        
        if Jean.History.check("cumshot_ass") and approval_check(Jean, threshold = "cumshot_ass"):
            $ possible_locations.append("ass")
        
        if Jean.History.check("cumshot_feet") and approval_check(Jean, threshold = "cumshot_feet"):
            $ possible_locations.append("feet")

        if possible_locations:
            $ chosen_location = renpy.random.choice(possible_locations)

            $ Jean.change_face("sexy", blush =2)

            ch_Jean "C'mere." 

            $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

            "She aims your cock at her [chosen_location] as you blow." 

    if chosen_location:
        return chosen_location

    return False

label Jean_lets_Player_decide_cumshot:
    $ Jean.change_face("sly", blush = 2) 
    
    ch_Jean "I think I'll let you pick where. . ."

    return

label Jean_decides_clean_cum:
    $ decision_pool = ["clean_cum"]

    if approval_check(Jean, threshold = "swallow_cum"):
        $ decision_pool.append("swallow_cum")
    
    if approval_check(Jean, threshold = "wear_cum"):
        $ decision_pool.append("wear_cum")

    return renpy.random.choice(decision_pool)