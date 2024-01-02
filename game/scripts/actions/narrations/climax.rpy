label Player_orgasm_narrations(Character, location):
    if renpy.random.random() > 0.5:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    if location == "cumshot_belly":
        $ renpy.say(None, f"You point your cock at {owner} stomach, ready to cover it.")
    elif "breasts" in location:
        if "clothes" in location:
            if Character.check_traits("breasts_covered"):
                $ renpy.say(None, f"You aim your cock right at {owner} tits, intent on getting it all over her clothes.")
            else:
                if Character.Clothes["bra"].string:
                    call fix(Character, "bra") from _call_fix_2

                if Character.Clothes["top"].string:
                    call fix(Character, "top") from _call_fix_3

                $ renpy.say(None, f"You pull {owner} top back down and aim your cock right at her tits.")
        else:
            if Character.check_traits("breasts_covered"):
                if Character.Clothes["jacket"].string:
                    call undress(Character, "jacket") from _call_undress_13
                    
                if Character.Clothes["top"].string:
                    call undress(Character, "top") from _call_undress_14
                    
                if Character.Clothes["bra"].string:
                    call undress(Character, "bra") from _call_undress_15

                $ renpy.say(None, f"You pull {owner} top out of the way and aim your cock right at her tits.")
            else:
                $ renpy.say(None, f"You aim your cock right at {owner} tits, ready to cover them.")
    elif location == "cumshot_face":
        $ renpy.say(None, f"You point your cock right at {owner} face.")
        
        $ Character.change_face("sexy", eyes = "closed", blush = 2) 
        
        $ renpy.say(None, f"{subject.capitalize()} shuts her eyes, ready to take it.")
    elif location == "cumshot_hair":
        $ renpy.say(None, f"You take your cock and aim it at the top of {owner} head, intent on covering her hair.")
    elif location == "cumshot_back":
        $ renpy.say(None, f"You point your cock at {owner} back, ready to cover it.")
    elif location == "cumshot_ass":
        $ renpy.say(None, f"You take your cock and aim it at {owner} ass.")
    elif location == "cumshot_feet":
        $ renpy.say(None, f"You point your cock down towards {owner} feet.")
    elif location == "creampie":
        if Character.vagina_Actions and Character.vagina_Actions[0].animation_type == "sex":
            $ renpy.say(None, f"You keep your cock inside {object} as you prepare to blow.")
        else:
            $ renpy.say(None, f"You slide your cock into {object}, getting ready to blow.")
    elif location == "cum_in_mouth":
        if Character.mouth_Actions and Character.mouth_Actions[0].animation_type == "blowjob":
            $ renpy.say(None, f"You keep your cock in {owner} mouth, ready to blow.")
        else:
            $ renpy.say(None, f"You put your cock just inside {owner} mouth, ready to blow.")
    elif location == "cumshot_tongue":
        if Character.mouth_Actions and Character.mouth_Actions[0].animation_type == "blowjob":
            $ renpy.say(None, f"{subject.capitalize()} opens wide for you, and you pull back slightly, aiming right at her tongue.")
        else:
            $ renpy.say(None, f"{subject.capitalize()} opens wide for you as your aim directly at her tongue.")
    elif location == "cum_down_throat":
        if Character.mouth_Actions and Character.mouth_Actions[0].animation_type == "deepthroat":
            $ renpy.say(None, f"You keep your cock down {owner} throat as you prepare to blow.")
        else:
            $ renpy.say(None, f"You slide your cock down {owner} throat, preparing to blow.")
    elif location == "anal_creampie":
        if Character.anus_Actions and Character.anus_Actions[0].animation_type == "anal":
            $ renpy.say(None, f"You keep your cock up {owner} ass as you prepare to blow.")
        else:
            $ renpy.say(None, f"You insert your cock into {owner} ass, getting ready to blow.")
    elif location == "bukkake":
        $ renpy.say(None, f"You take your cock, pointing it in {owner} general direction, ready to cover every inch of her.")
    elif location == "floor":
        $ renpy.say(None, f"You aim your cock away from {object}.")

    return

label Player_cumshot_narrations(Character, location):
    if renpy.random.random() > 0.5:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    $ renpy.pause(1.0, hard = True)

    if location == "cumshot_belly":
        with orgasm_shake
        $ renpy.say(None, f"You lose control, your cum shooting all over {owner} stomach.")
    elif "breasts" in location:
        with orgasm_shake
        $ renpy.say(None, f"You lose control, your cum shooting all over {owner} tits, slowly dripping down their curves.")
    elif location == "cumshot_face":
        with orgasm_shake
        $ renpy.say(None, f"{subject.capitalize()} flinches at first as your cum lands on her face, then she leans in to try to catch every last drop.")
    elif location == "cumshot_hair":
        with orgasm_shake
        $ renpy.say(None, f"You shudder and finally lose control, showering {object} with cum, getting it all in her hair.")
    elif location == "cumshot_back":
        with orgasm_shake
        $ renpy.say(None, f"You shudder, as your cum shoots all over {owner} back.")
    elif location == "cumshot_ass":
        with orgasm_shake
        $ renpy.say(None, f"Your cum sprays all over {owner} ass, dripping down its curves.")
    elif location == "cumshot_feet":
        with orgasm_shake
        $ renpy.say(None, f"{owner.capitalize()} feet and toes are covered, as you shudder and spray all over them.")
    elif location == "creampie":
        with orgasm_shake
        $ renpy.say(None, f"You can't help but shudder as you fill {object}, cumming right inside her pussy.")
    elif location == "cum_in_mouth":
        with orgasm_shake
        $ renpy.say(None, f"{owner.capitalize()} lips tighten around you as your cum sprays into the back of her mouth.")
    elif location == "cumshot_tongue":
        with orgasm_shake
        $ renpy.say(None, f"You spray across {owner} tongue, getting most of the cum on it, but some ends up in the back of her mouth.")
    elif location == "cum_down_throat":
        with orgasm_shake
        $ renpy.say(None, f"{subject.capitalize()} gags and sputters as you cum down her throat. She struggles to swallow with you still deep inside her.")
    elif location == "anal_creampie":
        with orgasm_shake
        $ renpy.say(None, f"{owner.capitalize()} ass tightens around you as you cum inside, filling it to the brim.")
    elif location == "bukkake":
        with orgasm_shake
        $ renpy.say(None, f"You convulse as waves of pleasure flow through you, your cum spraying all over {owner} body.")
    elif location == "floor":
        with orgasm_shake
        $ renpy.say(None, f"You spray across the room, landing on some towels you set up beforehand.")

    $ renpy.pause(1.0, hard = True)

    return

label Character_orgasm_narrations(Character):
    if renpy.random.random() > 0.5:
        $ subject = Character.name
        $ object = Character.name
        $ owner = Character.name + "'s"
    else:
        $ subject = "she"
        $ object = "her"
        $ owner = "her"

    if (Character.vagina_Actions and Character.vagina_Actions[0].animation_type == "sex") or (Character.anus_Actions and Character.anus_Actions[0].animation_type == "anal"):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ renpy.say(None, f"{owner.capitalize()} body shudders uncontrollably and she tightens, orgasming around your cock.") 
        elif dice_roll == 2:
            $ renpy.say(None, f"{owner.capitalize()} legs wrap around you as she convulses and tightens around your cock, the orgasm racking her body.")
    elif Character.mouth_Actions and Character.mouth_Actions[0].animation_type in ["blowjob", "deepthroat"]:
        $ renpy.say(None, f"{owner.capitalize()} body shudders as waves of pleasure flow throughout her body.")

        $ Character.change_face("sexy", blush = 2) 
        
        $ renpy.say(None, f"That doesn't stop her, though, as she just keeps sucking.")
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} starts twitching uncontrollably as an orgasm takes over her body. It lasts for a minute before she's able to calm down.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} moans as waves of pleasure run through her. The orgasm causes her to shake uncontrollably.")

    $ renpy.pause(1.0, hard = True)

    return