label makeout_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ Characters[0].change_face("kiss2", blush = 1) 
        
        if Characters[0] in [Rogue]:
            "You pull her in close, your lips pressing together."
        elif Characters[0] in [Laura, Jean]:
            "She drags you in close, your lips pressing together."

        $ Characters.remove(Characters[0])

    return

label choke_initiations(Action):
    $ Action.counter += 1

    return

label touch_thighs_over_clothes_initiations(Action):
    $ Action.counter += 1

    return

label touch_thighs_higher_over_clothes_initiations(Action):
    $ Action.counter += 1

    return

label touch_thighs_initiations(Action):
    $ Action.counter += 1

    return

label touch_thighs_higher_initiations(Action):
    $ Action.counter += 1

    return

label touch_breasts_over_clothes_initiations(Action):
    $ Action.counter += 1

    return

label touch_breasts_initiations(Action):
    $ Action.counter += 1

    return

label pinch_nipples_initiations(Action):
    $ Action.counter += 1

    return

label suck_nipples_initiations(Action):
    $ Action.counter += 1

    return

label touch_pussy_over_clothes_initiations(Action):
    $ Action.counter += 1

    return

label touch_pussy_initiations(Action):
    $ Action.counter += 1

    return

label finger_pussy_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        "Your fingers glide across [Characters[0].name]'s pussy, already wet and inviting, and you start gently pushing them inside."
        "She gasps as you enter her, and you feel her tense around your fingers."

        $ Characters.remove(Characters[0])

    return

label eat_pussy_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        "You bring your lips up to [Characters[0].name]'s pussy, giving it a gentle kiss, before slowly teasing it with your tongue."
        "She shudders as your tongue makes contact with her, and it makes its way across her clit."

        $ Characters.remove(Characters[0])

    return

label grab_ass_over_clothes_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0] in [Rogue]:
            "You wrap your hand around [Characters[0].name]'s voluptuous ass. It spills through your fingers, soft and inviting even through her bottoms."
        elif Characters[0] in [Laura, Jean]:
            "You wrap your hand around [Characters[0].name]'s tight ass. It comfortably fits in your hand, supple yet firm even through her bottoms."

        $ Characters.remove(Characters[0])

    return

label grab_ass_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0] in [Rogue]:
            "You wrap your hand around [Characters[0].name]'s voluptuous ass. It spills through your fingers, soft and inviting, her skin warm to the touch."
        elif Characters[0] in [Laura, Jean]:
            "You wrap your hand around [Characters[0].name]'s tight ass. It comfortably fits in your hand, supple yet firm, her skin soft and warm."

        $ Characters.remove(Characters[0])

    return

label finger_ass_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ Characters[0].change_face("surprised1", mouth = "lipbite", blush = 2)

        if Characters[0].History.check("finger_ass") >= 5:
            "As you press your finger up against her hole, [Characters[0].name] leans back into you, inviting it inside. Your finger slides in easily, eliciting a soft moan."
        elif Characters[0].History.check("finger_ass") >= 2:
            "[Characters[0].name]'s still not used to putting anything up there, and you encounter some resistance as your press your finger up against her hole. Eventually it slides in, and she tightens around you."
        else:
            "You press your finger up against [Characters[0].name]'s hole, slowly pressing it inside against the resistance. She involuntarily tightens around your finger, but manages to relax as it slides in all the way."

        $ Characters.remove(Characters[0])

    return

label eat_ass_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        "Spreading [Characters[0].name]'s cheeks with your hands, you slowly drag your tongue along her crack, circling around, licking anywhere but her hole."
        "She shudders as you give her asshole a kiss, before fully diving in with your tongue."

        $ Characters.remove(Characters[0])

    return

label handjob_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].History.check("handjob") >= 2:
            if Characters[0] in [Rogue]:
                $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                
                "[Characters[0].name] reaches out excitedly, wrapping her fingers around you and relishing the sensation of you in her hand."
            elif Characters[0] in [Laura]:
                $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] doesn't waste any time and grabs you as if she's been waiting for this all day, her gaze locked onto yours with a glint of desire."
            elif Characters[0] in [Jean]:
                $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                
                "[Characters[0].name] teases you a bit with some light touches, enjoying how you involuntarily twitch, before finally wrapping her fingers around you."
        else:
            if Characters[0] in [Rogue]:
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] tentatively reaches out, slowly wrapping her fingers around you. She relishes the feeling of you between her fingers, before starting to move." 
                
                $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "Let me know if ah do anythin' wrong. . .")
            elif Characters[0] in [Laura]:
                $ Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] reaches out, grabbing you as if she expects it to run off. Her grip is tight, and she spends a moment marveling at the sensation before starting to move." 
                
                $ Characters[0].change_face("confused1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "It feels. . . interesting. . .")
            elif Characters[0] in [Jean]:
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] reaches out, dragging a finger across your length, feeling the novel texture. She gently wraps her fingers around you, a bit too gently, before starting to move." 
                
                $ Characters[0].change_face("worried1", mouth = "smirk", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "This is how you do it, right?")

        $ Characters.remove(Characters[0])

    return

label fondle_balls_initiations(Action):
    $ Action.counter += 1

    return

label blowjob_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Action.mode == 3:
            if Characters[0].History.check("blowjob") >= 2:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", blush = 2) 
                    
                    "She eagerly wraps her lips around you and starts sucking with enthusiasm."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    "She pulls you into her mouth without hesitation."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("sexy", blush = 2) 
                    
                    "She teases you a bit, thoroughly enjoying the look on your face, before finally wrapping her lips around you."
            else:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "Ah'll try my best. . .")
                    
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "She tentatively laps her lips around the head, slowly bringing you inside her mouth."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("confused1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "I still don't fully understand how this works. . .")
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "But it does taste good.")
                    
                    "She eagerly wraps her lips around you, bringing you in a bit too deep, causing her to gag, and pull back a bit."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It really is that big. . .")
                    
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "Don't expect me to take it too deep.")

                    "With some hesitation, she wraps her lips around you, only bringing in a couple inches."
        else:
            if Characters[0].History.check("blowjob") >= 2:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "[Characters[0].name] reaches out excitedly, pulling you up to her lips, hungry for the feeling of you in her mouth."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] pulls you up to her mouth, not wasting a single second, as her lips press into your cock."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "[Characters[0].name] teases you a bit with some gentle kissing, enjoying how you involuntarily twitch, before finally pressing her lips up against your cock."
            else:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("worried2", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It's still a bit dauntin'. . . how big it is. . .") 
                    
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "kiss", blush = 2) 
                    
                    "[Characters[0].name] slowly brings her lips down to you, lightly brushing them against your cock. After the first touch, it seems like she can't help herself and goes in for more." 
                    
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "Ah love how it feels on my lips. . .")
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "I'm not certain. . . my mouth is big enough. . .")
                    
                    $ Characters[0].change_face("confused1", eyes = "down", mouth = "kiss", blush = 2) 
                    
                    "Despite her compunctions, [Characters[0].name] presses her lips up against you, inhaling your scent all the while." 
                    
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    "After that first touch, she gets a feral gleam in her eye." 

                    $ renpy.say(Characters[0].voice, "Hmmm. . .")
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "God, it's so big. . .")
                    
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "kiss", blush = 2) 
                    
                    "[Characters[0].name] slowly pulls her lips down to you, touching them lightly to your cock causing you to involuntarily twitch. She still seems apprehensive, but seeing you twitch like that. . ." 
                    
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "You liked that?")

        $ Characters.remove(Characters[0])

    return

label suck_balls_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label deepthroat_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].History.check("deepthroat") >= 2:
            if Characters[0].throat_training == 1:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] looks down at you, a bit apprehensive."
                    "She tentatively wraps her lips around you, taking you in slowly."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] has a determined look on her face, as she gets ready to try and take you all in." 
                    "Her lips wrap around you, and it doesn't seem like she's learned much as she goes too deep too fast and gags."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name]'s eyes are locked on your cock, sizing you up." 
                    "After a bit of hesitation, she finally wraps her lips around you." 
            elif Characters[0].throat_training == 2:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", blush = 2) 
                    
                    "[Characters[0].name] looks into your eyes, a gleam of excitement in her own."
                    "She wraps her lips around you, taking you in with more confidence than before."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] stares down at your cock for a while, like a predator sizing up its prey."
                    "Her lips wrap around you, more cautiously this time, and she takes things slow."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("confused1", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] looks down at your cock with less apprehension than before."
                    "You can tell she's starting to get a bit more confident as she wraps her lips around you." 
            elif Characters[0].throat_training == 3:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "[Characters[0].name] looks down at your cock, ready to take you as deep as she can handle."
                    "She wraps her lips around you with zero hesitation."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("sexy", blush = 2) 
                    
                    "[Characters[0].name] stares into your eyes, a gleam of excitement in them." 
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "She hungrily wraps her lips around you, taking you deeper and showing all the progress she's made so far."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("sexy", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "I'm starting to get pretty good at this.")
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "She doesn't hesitate to start taking you in, showing off all her progress."
            elif Characters[0].throat_training == 4:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "[Characters[0].name] looks down at your cock with lustful eyes."
                    "She starts taking you in like she's been waiting for this all day."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] stares into your eyes, you get a sense of self satisfaction in them." 
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "She doesn't hesitate for a second, wrapping her lips around you, ready to take you all the way."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "I think enjoy this as much as you do.")
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "With more confidence than ever, she wraps her lips around you, ready to take you in all the way."
        else:
            if Characters[0] in [Rogue]:
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] stares down at your cock, a bit daunted by the task in front of her." 
                
                $ renpy.say(Characters[0].voice, "Ah reckon it'll be a while before ah can take all of it. . .")
                
                "She wraps her lips around you and starts taking you in, slowly, one inch at a time."
            elif Characters[0] in [Laura]:
                $ Characters[0].change_face("confused2", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "I am supposed to swallow all of it?")
                
                $ Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "She stares down at your cock, looking quite skeptical that it's even possible." 
                
                $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "That's not to say she lets it stop her from trying, as she wraps her lips around you."
            elif Characters[0] in [Jean]:
                $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "I'm still not convinced this is even possible. . .")
                
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "She looks down at your cock, clearly intimidated by its size." 
                "That doesn't stop her from trying, as she wraps her lips around you."

        $ Characters.remove(Characters[0])

    return

label titjob_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label footjob_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label self_touch_pussy_initiations(Action):
    $ Action.counter += 1

    return

label self_finger_ass_initiations(Action):
    $ Action.counter += 1

    return

label self_vibrator_initiations(Action):
    $ Action.counter += 1

    return

label self_dildo_pussy_initiations(Action):
    $ Action.counter += 1

    return

label self_dildo_ass_initiations(Action):
    $ Action.counter += 1

    return

label jerk_off_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label grind_pussy_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            "You lay your cock across [Characters[0].name]'s crotch, immediately feeling the heat radiating off of it."
        elif dice_roll == 2:
            "[Characters[0].name] leans her hips into you, seeking to feel your cock press against her."

        $ Characters.remove(Characters[0])

    return

label grind_ass_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            "You lay your cock in between [Characters[0].name]'s cheeks and press up against her hole."
        elif dice_roll == 2:
            "[Characters[0].name] leans her hips into you, seeking to feel your cock press against her."

        $ Characters.remove(Characters[0])

    return

label sex_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Action.mode == 2:
            "You slide the tip inside her, and istead of pulling it back out, you start to move."
        else:
            if Characters[0].History.check("sex") >= 3:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "[Characters[0].name] looks down excitedly, wiggling her hips at you, ready to take it in." 
                    "You gently press yourself up against her hole, teasing it, feeling how wet she already is."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] has that look in her eye, one that says she wants you to fuck her already." 
                    "You press the tip up against her hole, which is already dripping wet, as you prepare to slide it in."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("sly", blush = 2) 
                    
                    "[Characters[0].name] teases you a bit, pulling her hips away." 
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "Finally, she lets you get close, and you press the tip up against her hole."
            else:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("worried2", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "The first time wasn't so bad. . . but it's just so big. . .")
                    
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "You gently press yourself up against her hole, teasing it, feeling how wet she already is." 
                    
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                    $ renpy.say(Characters[0].voice, "Ah'm ready. . .")
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "The first time was only slightly painful at the start. . .")
                    
                    $ Characters[0].change_face("sexy", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "And felt very good by the end.")
                    $ renpy.say(Characters[0].voice, "Put it in already. . .")
                    
                    $ Characters[0].change_face("sexy", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "You press the tip up against her hole, which is already dripping wet, as you prepare to slide it in."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It kinda hurt the first time. . .")
                    
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "But I need to get used to it.")
                    
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "You press the tip up against her, causing her to twitch, as you prepare to slide it in." 
                    
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "You can start. . .")

        $ Characters.remove(Characters[0])

    return

label anal_initiations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Action.mode < 2 or Characters[0].anal_training >= 2:
            if Characters[0].anal_training == 1:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It doesn't hurt too bad. . .")
                    $ renpy.say(Characters[0].voice, "So long as yer gentle.")
                    
                    $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                    
                    "You gently press yourself up against her hole, slowly pushing the tip in as she whimpers in pain."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "The pain is not the issue. . .")
                    $ renpy.say(Characters[0].voice, "You are just too big.")
                    
                    $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "You slowly press your cock into her, the tight hole providing a lot of resistance as [Characters[0].name] growls from the pain."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It kinda hurts. . . a lot. . .")
                    $ renpy.say(Characters[0].voice, "Just be careful.")
                    
                    $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                    
                    "Her tight hole provides a lot of resistance as you gently force your cock inside."
                    "Slowly, you manage to get the tip in, [Characters[0].name] whimpering from the pain." 
            elif Characters[0].anal_training == 2:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] looks down at you, still a bit of apprehension in her eyes." 
                    "You slowly press the tip into her, and she takes it without showing too much discomfort."
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name]'s starting to get used to your size, but still looks down at your cock with trepidation." 
                    "You gently push your cock inside her and it goes in without too much difficulty."
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] looks down at your cock, worry written across her face." 
                    "She's starting to get used to you, but has a long way to go." 
                    "You slowly press the tip inside her, and she manages not to whimper in pain." 
            elif Characters[0].anal_training == 3:
                if Characters[0] in [Rogue]:
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    "[Characters[0].name] looks down at your cock, ready to take you as deep as you can give her." 
                    
                    "You press the tip into her, and it slides in like it was always meant to be there." 
                elif Characters[0] in [Laura]:
                    $ Characters[0].change_face("sly", eyes = "down", mouth = "lipbite", blush = 2) 
                    
                    "[Characters[0].name] stares down at your cock, an air of excitement about her, as taking all of you isn't a problem anymore." 
                    "Your cock slides into her ass with ease, a perfect fit." 
                elif Characters[0] in [Jean]:
                    $ Characters[0].change_face("sexy", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It doesn't hurt anymore. . .")
                    
                    $ Characters[0].change_face("sexy", eyes = "down", blush = 2) 
                    
                    $ renpy.say(Characters[0].voice, "It actually feels really good.")

                    "You cock slides into her ass like it's meant to be there, and she even lets out a moan as you push deeper inside." 
        else:
            $ Action.mode = 1

            $ selected_Action_mode = 1

            if Characters[0] in [Rogue]:
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "It's real big. . .")
                
                $ Characters[0].change_face("worried2", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "Please don't force it.")

                $ Action.counter += 1
                
                $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                
                "You press the tip up against her, her tight hole providing a lot of resistance." 
                "You manage to get the head in before she whimpers and stops you from going further." 
                
                $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "Ah'm sorry, deeper than that hurts too much. . .")
                
                $ renpy.say(Characters[0].voice, "At least ah can handle the tip for now.")
                
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] will have to practice before she can take it any deeper."
            elif Characters[0] in [Laura]:
                $ Characters[0].change_face("confused2", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "I still do not understand how this would even be possible. . .")
                
                $ Characters[0].change_face("confused1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "Go slowly. . .")

                $ Action.counter += 1 
                
                $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                
                "You press your cock up against her hole, [Characters[0].name]'s small stature not doing her any favors. . ."
                "It's a very tight fit, and you only manage to get the tip in before she growls from pain." 
                
                $ Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "That is deep enough for now. . .")
                
                $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] will have to practice before she can take it any deeper."
            elif Characters[0] in [Jean]:
                $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "I still don't understand how all of you. . .")
                
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, ". . . could fit back there.")
                $ renpy.say(Characters[0].voice, "You better be gentle.")

                $ Action.counter += 1
                
                $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                
                "You press the tip up against her tight hole, easing it inside." 
                "She winces, and you're only able to fit the tip in before she gasps, forcing you to stop." 
                
                $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "That's as far as you're going. . .")
                $ renpy.say(Characters[0].voice, "It hurts too much.")

                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] will have to practice before she can take it any deeper."

            $ speed = 0.1
            $ intensity = 0.1

        $ Characters.remove(Characters[0])

    return

label vibrator_initiations(Action):
    $ Action.counter += 1

    return

label dildo_pussy_initiations(Action):
    $ Action.counter += 1

    return

label dildo_ass_initiations(Action):
    $ Action.counter += 1

    return