label Player_orgasm_narrations(Character, location):
    if location == "cumshot_belly":
        "You point your cock at her stomach, ready to cover it."
    elif "breasts" in location:
        if "clothes" in location:
            if Character.breasts_covered:
                "You aim your cock right at her tits, intent on getting it all over her clothes."
            else:
                if Character.Clothes["bra"].string:
                    call fix(Character, "bra") from _call_fix_2

                if Character.Clothes["top"].string:
                    call fix(Character, "top") from _call_fix_3

                "You pull her top back down and aim your cock right at her tits."
        else:
            if Character.breasts_covered:
                if Character.Clothes["jacket"].string:
                    call undress(Character, "jacket") from _call_undress_13
                    
                if Character.Clothes["top"].string:
                    call undress(Character, "top") from _call_undress_14
                    
                if Character.Clothes["bra"].string:
                    call undress(Character, "bra") from _call_undress_15

                "You pull her top out of the way and aim your cock right at her tits."
            else:
                "You aim your cock right at her tits, ready to cover them."
    elif location == "cumshot_face":
        "You point your cock right at her face." 
        
        $ Character.change_face("sexy", eyes = "closed", blush = 2) 
        
        "She shuts her eyes, ready to take it."
    elif location == "cumshot_hair":
        "You take your cock and aim it at the top of her head, intent on covering her hair."
    elif location == "cumshot_back":
        "You point your cock at her back, ready to cover it."
    elif location == "cumshot_ass":
        "You take your cock and aim it at her ass."
    elif location == "cumshot_feet":
        "You point your cock down towards her feet."
    elif location == "creampie":
        if Character.vagina_Actions and Character.vagina_Actions[0].animation_type == "sex":
            "You keep your cock inside her as you prepare to blow."
        else:
            "You slide your cock into her, getting ready to blow."
    elif location == "cum_in_mouth":
        if Character.mouth_Actions and Character.mouth_Actions[0].animation_type == "blowjob":
            "You keep your cock in her mouth, ready to blow."
        else:
            "You put your cock just inside her mouth, ready to blow."
    elif location == "cumshot_tongue":
        if Character.mouth_Actions and Character.mouth_Actions[0].animation_type == "blowjob":
            "She opens wide for you, and you pull back slightly, aiming right at her tongue."
        else:
            "She opens wide for you as your aim directly at her tongue."
    elif location == "cum_down_throat":
        if Character.mouth_Actions and Character.mouth_Actions[0].animation_type == "deepthroat":
            "You keep your cock down her throat as you prepare to blow."
        else:
            "You slide your cock down her throat, preparing to blow."
    elif location == "anal_creampie":
        if Character.anus_Actions and Character.anus_Actions[0].animation_type == "anal":
            "You keep your cock up her ass as you prepare to blow."
        else:
            "You insert your cock into her ass, getting ready to blow."
    elif location == "bukkake":
        "You take your cock, pointing it in her general direction, ready to cover every inch of her."
    elif location == "floor":
        "You aim your cock away from her."

    return

label Player_cumshot_narrations(Character, location):
    if location == "cumshot_belly":
        $ increase_Character_desire(Character, 5)
        
        "You lose control, your cum shooting all over her stomach."
    elif "breasts" in location:
        $ increase_Character_desire(Character, 10)
        
        "You lose control, your cum shooting all over her tits, slowly dripping down their curves."
    elif location == "cumshot_face":
        $ increase_Character_desire(Character, 8)
        
        "Your cum lands on her face causing her to flinch, but lean in trying to catch every last drop."
    elif location == "cumshot_hair":
        $ increase_Character_desire(Character, 5)

        "You shudder and finally lose control, showering her with cum, getting it all in her hair."
    elif location == "cumshot_back":
        $ increase_Character_desire(Character, 5)
        
        "You shudder, as your cum shoots all over her back."
    elif location == "cumshot_ass":
        $ increase_Character_desire(Character, 7)
        
        "Your cum sprays all over her ass, dripping down its curves."
    elif location == "cumshot_feet":
        $ increase_Character_desire(Character, 5)
        
        "Her feet and toes are covered, as you shudder and spray all over them."
    elif location == "creampie":
        $ increase_Character_desire(Character, 12)

        "You can't help but shudder as you fill her, cumming right inside her pussy."
    elif location == "cum_in_mouth":
        $ increase_Character_desire(Character, 10)
        
        "Her lips tighten around you as your cum sprays into the back of her mouth."
    elif location == "cumshot_tongue":
        $ increase_Character_desire(Character, 8)
        
        "You spray across her tongue, getting most of the cum on it, but some ends up in the back of her mouth."
    elif location == "cum_down_throat":
        $ increase_Character_desire(Character, 10)
        
        "[Character.name] gags and sputters as you cum down her throat. She struggles to swallow with you still deep inside her."
    elif location == "anal_creampie":
        $ increase_Character_desire(Character, 8)
        
        "Her ass tightens around you as you cum inside, filling it to the brim."
    elif location == "bukkake":
        $ increase_Character_desire(Character, 10)

        "You convulse as waves of pleasure flow through you, your cum spraying all over her body."
    elif location == "floor":
        $ increase_Character_desire(Character, 3)

        "You spray across the room, landing on some towels you set up beforehand."

    return

label Character_orgasm_narrations(Character):
    if (Character.vagina_Actions and Character.vagina_Actions[0].animation_type == "sex") or (Character.anus_Actions and Character.anus_Actions[0].animation_type == "anal"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Character.change_face("surprised2", mouth = "lipbite", blush = 2) 
            
            "[Character.name]'s body shudders uncontrollably and she tightens, orgasming around your cock." 
        elif dice_roll == 2:
            $ Character.change_face("sly", mouth = "lipbite", blush = 2) 
            
            "[Character.name]'s legs wrap around you as she convulses and tightens around your cock, the orgasm racking her body."
 
        with orgasm_shake
    elif Character.mouth_Actions and Character.mouth_Actions[0].animation_type in ["blowjob", "deepthroat"]:
        $ Character.change_face("surprised2", mouth = "lipbite", blush = 2) 
        
        "[Character.name]'s body shudders as waves of pleasure flow throughout her body." 
 
        with orgasm_shake

        $ Character.change_face("sexy", blush = 2) 
        
        "That doesn't stop her, though, as she just keeps sucking."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Character.change_face("surprised2", mouth = "lipbite", blush = 2) 
            
            "[Character.name] starts twitching uncontrollably as the orgasm takes over her body. It lasts for a minute before she's able to calm down."
        elif dice_roll == 2:
            $ Character.change_face("surprised2", mouth = "lipbite", blush = 2) 
            
            "[Character.name] moans as waves of pleasure run through her. The orgasm causes her to shake uncontrollably."
 
        with orgasm_shake

    return