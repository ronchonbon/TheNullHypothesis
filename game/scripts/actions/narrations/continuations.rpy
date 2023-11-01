label makeout_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_pool = [1, 2, 3, 4, 5]

        if Characters[0].History.check("makeout") >= 12:
            $ increase_Character_desire(Characters[0], 5, limit = 75)
            $ increase_Character_desire(Player, 5, limit = 75)

            $ dice_pool.append(6)
            $ dice_pool.append(7)
            $ dice_pool.append(8)
            $ dice_pool.append(9)
            $ dice_pool.append(10)
        elif Characters[0].History.check("makeout") >= 6:
            $ increase_Character_desire(Characters[0], 4, limit = 75)
            $ increase_Character_desire(Player, 4, limit = 75)

            $ dice_pool.append(11)
            $ dice_pool.append(12)
            $ dice_pool.append(13)
            $ dice_pool.append(14)
        else:
            $ increase_Character_desire(Characters[0], 2, limit = 75)
            $ increase_Character_desire(Player, 2, limit = 75)

            $ dice_pool.append(15)
            $ dice_pool.append(16)
            $ dice_pool.append(17)
            $ dice_pool.append(18)

            if renpy.random.random() > 0.9:
                $ dice_pool.append(19)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "Your tongues dance together as you continue to enjoy each other."
        elif dice_roll == 2:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "[Characters[0].name]'s lips are soft against yours, and she tastes a bit like strawberries."
        elif dice_roll == 3:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "[Characters[0].name] squeezes you tightly, pressing her lips firmly against yours."
        elif dice_roll == 4:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "You run a hand through [Characters[0].name]'s hair while continuing to kiss her."
        elif dice_roll == 5:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "[Characters[0].name]'s hands wander across your body as your tongues dance inside each other's mouth."
        elif dice_roll == 6:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "[Characters[0].name]'s lips glides between yours with practiced ease as your tongues meet."
        elif dice_roll == 7:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "[Characters[0].name]'s lips part, inviting yours in with enthusiasm."
        elif dice_roll == 8:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "[Characters[0].name] seems to thoroughly enjoy the taste of your lips as she nibbles on them, using just the right amount of pressure."
        elif dice_roll == 9:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "You gently kiss [Characters[0].name]'s neck, and she shudders in nothing but pure ecstasy."
        elif dice_roll == 10:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "Nibbling on [Characters[0].name]'s ear elicits a shudder and a moan, and she squeezes you tightly."
        elif dice_roll == 11:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "Despite the excitement, [Characters[0].name]'s lips are still a bit clumsy as they move around yours."
        elif dice_roll == 12:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "[Characters[0].name]'s lips part, inviting yours in, and it's clear she's starting to get used to you."
        elif dice_roll == 13:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "[Characters[0].name] seems to be thoroughly enjoying the taste of your lips as she nibbles on them, still a bit too hard."
        elif dice_roll == 14:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "You gently kiss [Characters[0].name]'s neck, and she can't help but shudder despite starting to get used to the sensation."
        elif dice_roll == 15:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "You gently kiss [Characters[0].name]'s neck, causing her to shudder as she's not yet used to such a sensation from you."
        elif dice_roll == 16:
            $ Characters[0].change_face("kiss2", blush = 2) 
            
            "[Characters[0].name] seems to be thoroughly enjoying the taste of your lips, but nibbles on them a bit too hard."
        elif dice_roll == 17:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "[Characters[0].name]'s lips part, inviting yours in, but it's clear she's not quite used to you yet."
        elif dice_roll == 18:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "Despite the excitement, [Characters[0].name]'s lips clumsily move around yours."
        elif dice_roll == 19:
            $ Characters[0].change_face("kiss1", blush = 1) 
            
            "The fun is briefly interrupted as [Characters[0].name]'s teeth come into contact with yours, causing you to wince." 
            
            $ Characters[0].change_face("worried2") 
            
            $ renpy.say(Characters[0].voice, "Sorry. . .")

        $ Characters.remove(Characters[0])

    return

label choke_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 1, limit = 75)
        $ increase_Character_desire(Player, 2, limit = 75)

        $ Characters[0].blush += 1 if Characters[0].blush < 3 else 0

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "Your hand gently squeezes her neck, causing her face to flush."
        elif dice_roll == 2:
            "You feel her pulse quicken as you keep the pressure around her neck."
        elif dice_roll == 3:
            "You feel the blood rush beneath her skin as you put even pressure on her neck."

        $ Characters.remove(Characters[0])

    return

label touch_thighs_over_clothes_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 2, limit = 85)
        $ increase_Character_desire(Player, 1, limit = 75)

        if Characters[0] in [Laura]:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You caress [Characters[0].name]'s inner thigh, causing a slight shudder despite her clothes limiting the sensation."
        elif dice_roll == 2:
            "The touch makes [Characters[0].name]'s leg twitch even through the clothes, as you move your hand up from her knee, making sure not to go too high." 
        elif dice_roll == 3:
            "You can feel [Characters[0].name]'s warmth even through the clothes, and your hands makes its way up and down her thigh."
        elif dice_roll == 4:
            "Your hand glides along [Characters[0].name]'s thigh, feeling the ample muscle beneath her clothes."

        $ Characters.remove(Characters[0])

    return

label touch_thighs_higher_over_clothes_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 4, limit = 85)
        $ increase_Character_desire(Player, 2, limit = 75)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "As your hand moves higher up [Characters[0].name]'s thigh, brushing up against her crotch, you can feel the warmth even through her clothes."        
        elif dice_roll == 2:
            "[Characters[0].name] can't help but twitch, as your hand makes its way up her thigh, briefly touching her crotch through her clothes."
        elif dice_roll == 3:
            "You gently caress [Characters[0].name]'s inner thigh, going as high as her crotch, feeling her warmth even through her clothes."

        $ Characters.remove(Characters[0])

    return

label touch_thighs_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 3, limit = 85)
        $ increase_Character_desire(Player, 1, limit = 75)

        if Characters[0] in [Laura]:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You caress [Characters[0].name]'s inner thigh, eliciting a shudder, the sensation unimpeded by any clothing."
        elif dice_roll == 2:
            "The touch makes [Characters[0].name]'s leg twitch as you move your hand up from her knee, making sure not to go too high." 
        elif dice_roll == 3:
            "You can feel the warmth of [Characters[0].name]'s skin as your hand makes its way up and down her thigh."
        elif dice_roll == 4:
            "Your hand glides along the soft skin of [Characters[0].name]'s thigh, feeling its ample muscle."

        $ Characters.remove(Characters[0])

    return

label touch_thighs_higher_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 5, limit = 85)
        $ increase_Character_desire(Player, 2, limit = 75)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "As your hand moves higher up [Characters[0].name]'s thigh, brushing up against her crotch, you can feel the warmth as she shudders from your touch."
        elif dice_roll == 2:
            "[Characters[0].name] can't help but twitch, as your hand makes its way up her thigh, briefly touching her crotch."
        elif dice_roll == 3:
            "You gently caress [Characters[0].name]'s inner thigh, going as high as her crotch, feeling her warmth through her skin."

        $ Characters.remove(Characters[0])

    return

label touch_breasts_over_clothes_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 3, limit = 90)
        $ increase_Character_desire(Player, 2, limit = 80)

        $ dice_pool = [1, 2]

        if Characters[0] in [Rogue, Jean]:
            $ dice_pool.append(3)
        elif Characters[0] in [Laura]:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            "As your hands massage [Characters[0].name]'s breasts, you can feel her nipples stiffen even through her top."
        elif dice_roll == 2:
            "[Characters[0].name] leans into your hand as you fondle her breasts, their softness evident even through her top."
        elif dice_roll == 3:
            "You gently fondle [Characters[0].name]'s breasts through her top, their size too big for a single hand as they spill through your fingers."
        elif dice_roll == 4:
            "You gently fondle [Characters[0].name]'s breasts through her top, their smaller size fitting comfortably in your hand."

        $ Characters.remove(Characters[0])

    return

label touch_breasts_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 5, limit = 90)
        $ increase_Character_desire(Player, 3, limit = 80)

        $ dice_pool = [1, 2]

        if Characters[0] in [Rogue]:
            $ dice_pool.append(3)
        elif Characters[0] in [Laura]:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            "As your hands massage [Characters[0].name]'s breasts, you can feel her soft skin, and her nipples stiffen with even the slightest touch."
        elif dice_roll == 2:
            "[Characters[0].name] leans into your hand as you fondle her breasts, their softness a contrast to the hard nipple under your thumb."
        elif dice_roll == 3:
            "You gently fondle [Characters[0].name]'s breasts, their size too big for a single hand as they spill through your fingers. She shudders as you brush your thumb across her already stiff nipples."
        elif dice_roll == 4:
            "You gently fondle [Characters[0].name]'s breasts, their smaller size fitting comfortably in your hand. She shudders as you brush your thumb across her already stiff nipples."

        $ Characters.remove(Characters[0])

    return

label pinch_nipples_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 6, limit = 90)
        $ increase_Character_desire(Player, 3, limit = 80)

        if Characters[0].piercings["nipple"]:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You put [Characters[0].name]'s nipple in between your thumb and forefinger and give it a good tug, causing her to jerk in surprise."
        elif dice_roll == 2:
            "[Characters[0].name]'s nipple stiffens even further as you give it a pinch, eliciting a moan from her."
        elif dice_roll == 4:
            "[Characters[0].name] stiffens as you give her nipple a pinch."
        elif dice_roll == 5:
            "You give [Characters[0].name]'s piercing a sharp tug, causing her to stiffen."

        $ Characters.remove(Characters[0])

    return

label suck_nipples_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 7, limit = 95)
        $ increase_Character_desire(Player, 4, limit = 90)

        if Characters[0].piercings["nipple"]:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            "You put [Characters[0].name]'s nipple in your mouth and suck, twirling your tongue around it, eliciting a moan."
        elif dice_roll == 2:
            "[Characters[0].name]'s nipple stiffens as you nibble on it, and she runs a hand through your hair."
        elif dice_roll == 3:
            "[Characters[0].name] holds your head to her breast as you continue to lick around and over her nipple."
        elif dice_roll == 4:
            "You cup [Characters[0].name]'s breast in your hand, gently biting down on her nipple."
        elif dice_roll == 5:
            "You tug on [Characters[0].name]'s piercing with your mouth, causing her to lean into you."

        $ Characters.remove(Characters[0])

    return

label touch_pussy_over_clothes_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 3, limit = 90)
        $ increase_Character_desire(Player, 1, limit = 85)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "Your hand presses into [Characters[0].name]'s crotch, causing her to squirm at the touch even if it's through her clothes."
        elif dice_roll == 2:
            "[Characters[0].name]'s crotch radiates warmth as you fondle it, her clothes apparently doing little to dampen the sensation."
        elif dice_roll == 3:
            "[Characters[0].name] leans into your hand, seeking out your touch as it's partially dampened by the fabric."

        $ Characters.remove(Characters[0])

    return

label touch_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 5)
        $ increase_Character_desire(Player, 3, limit = 90)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "Your hand presses into [Characters[0].name]'s crotch, gliding across her already wet pussy, eliciting a shudder." 
        elif dice_roll == 2:
            "With a thumb on [Characters[0].name]'s clit, you apply gentle pressure as she leans into you."
        elif dice_roll == 3:
            "[Characters[0].name] lets out a moan as your hand moves its way around her exposed pussy, already slick itself."

        $ Characters.remove(Characters[0])

    return

label finger_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Player, 3, limit = 90)

        $ dice_pool = [1, 2, 3]

        if speed > Action.max_speed[0]/2:
            $ increase_Character_desire(Characters[0], 7)

            $ dice_pool.append(4)
        else:
            $ increase_Character_desire(Characters[0], 6)

        if Characters[0].desire >= 75:
            $ dice_pool.append(5)
            
        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            "As your fingers slide in and out, [Characters[0].name] can't help but shudder, as she involuntarily tightens around your fingers." 
        elif dice_roll == 2:
            "You gently rub [Characters[0].name]'s clit with your thumb as your fingers continue to glide in and out of her."
        elif dice_roll == 3:
            "You curl your fingers slightly hitting just the right spot, eliciting a shudder as [Characters[0].name] involuntarily moans in ecstasy."
        elif dice_roll == 4:
            "Your fingers rapidly thrust in and out, causing moans and shudders throughout [Characters[0].name]'s body."
        elif dice_roll == 5:
            "[Characters[0].name]'s pussy twitches and tightens around your fingers, now dripping wet, as she draws close to the edge."

        $ Characters.remove(Characters[0])

    return

label eat_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 8)
        $ increase_Character_desire(Player, 4, limit = 90)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "Wrapping your lips over [Characters[0].name]'s clit, you suck and play with it with your tongue, eliciting a series of moans."
        elif dice_roll == 2:
            "Your tongue moves its way around [Characters[0].name]'s pussy, leaving no part ignored, as she shudders with every motion."
        elif dice_roll == 3:
            "[Characters[0].name] runs a hand through your hair, anchoring your head in place, as you continue pleasuring her with your mouth."
        
        $ Characters.remove(Characters[0])

    return

label grab_ass_over_clothes_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 3, limit = 85)
        $ increase_Character_desire(Player, 1, limit = 75)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "[Characters[0].name] leans back into your hand, seeking the sensation of your touch as it's dampened by her clothes."
        elif dice_roll == 2:
            "You gently massage [Characters[0].name]'s ass, enjoying it in all its glory, despite the barrier her clothing presents."
        elif dice_roll == 3:
            "With a firm grasp, you spread and kneed [Characters[0].name]'s cheeks, only her clothes preventing anything more."

        $ Characters.remove(Characters[0])

    return

label grab_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 4, limit = 85)
        $ increase_Character_desire(Player, 2, limit = 75)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "[Characters[0].name] leans back into your hand, thoroughly enjoying your touch as you knead into her cheeks."
        elif dice_roll == 2:
            "You gently massage [Characters[0].name]'s ass, enjoying it in all its glory, making sure to explore every inch of it."        
        elif dice_roll == 3:
            "With a firm grasp, you spread and kneed [Characters[0].name]'s cheeks, your hand occasionally sliding in between them, eliciting a moan."

        $ Characters.remove(Characters[0])

    return

label finger_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].History.check("finger_ass") >= 6:
            $ increase_Character_desire(Characters[0], 4)
            $ increase_Character_desire(Player, 2, limit = 90)
        elif Characters[0].History.check("finger_ass") >= 2:
            $ increase_Character_desire(Characters[0], 2)
            $ increase_Character_desire(Player, 1, limit = 90)
        else:
            $ increase_Character_desire(Player, 1, limit = 90)

        $ dice_pool = [1, 2, 3]

        if speed > Action.max_speed[0]/2:
            $ increase_Character_desire(Characters[0], 5)

            $ dice_pool.append(4)
        else:
            $ increase_Character_desire(Characters[0], 4)

        if Characters[0].desire >= 75:
            $ dice_pool.append(5)
            
        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            "[Characters[0].name] tightens even further around your finger, as you continue to slide it in and out of her ass." 
        elif dice_roll == 2:
            "Your finger presses deeper inside [Characters[0].name], her tight hole not providing much resistance."
        elif dice_roll == 3:
            "Pulling your finger out, you tease [Characters[0].name]'s hole before sliding it back inside."
        elif dice_roll == 4:
            "Your finger rapidly slides in and out of [Characters[0].name], as she involuntarily twitches and tightens around."
        elif dice_roll == 5:
            "Every motion causes [Characters[0].name] to twitch and shudder, your finger continuing to slide in and out of her hole as it only gets tighter around you."

        $ Characters.remove(Characters[0])

    return

label eat_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ increase_Character_desire(Characters[0], 7)
        $ increase_Character_desire(Player, 3, limit = 90)

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            "You continue to tease [Characters[0].name]'s rim with your tongue, eliciting a moan whenever you do touch it."
        elif dice_roll == 2:
            "[Characters[0].name] shudders with every pass of your tongue, as you lick around and over her hole."
        elif dice_roll == 3:
            "You pull [Characters[0].name]'s cheeks even farther apart and dive in, sucking and licking her hole, eliciting a moan."

        $ Characters.remove(Characters[0])

    return

label handjob_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].History.check("handjob") >= 10:
            $ increase_Character_desire(Characters[0], 5, limit = 85)
            $ increase_Character_desire(Player, 16)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "She strokes you with a light but deft touch, her experience pleasuring you clear as she pushes all the right buttons."
            elif dice_roll == 2:
                "Her grip is gentle but firm at the same time, each stroke sending waves of pleasure through you, especially when she plays with the head as well."
            elif dice_roll == 3:
                "Every stroke feels like it's designed to make you cum as fast as possible, her hand a perfect fit around you, maximizing the pleasure."
        elif Characters[0].History.check("handjob") >= 5:
            $ increase_Character_desire(Characters[0], 4, limit = 85)
            $ increase_Character_desire(Player, 12)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "She strokes you with more finesse and less trepidation this time, but an inconsistent grip makes her lack of experience evident."
            elif dice_roll == 2:
                "You wince when she accidentally nudges one of your balls, but despite that she's getting better, if still having a way to go."
            elif dice_roll == 3:
                "A wave of pleasure runs through you as she plays with your head, but it's ruined when she squeezes a bit too tightly. . . at least she's getting better."
        else:
            $ increase_Character_desire(Characters[0], 2, limit = 85)
            $ increase_Character_desire(Player, 8)

            $ dice_roll = renpy.random.randint(1, 4)

            if dice_roll == 1:
                if Characters[0] in [Rogue]:
                    "[Rogue.name] fumbles around a bit, still not used to having you in her hand. As a result, she's a bit too gentle, providing minimal sensation."
                elif Characters[0] in [Laura]:
                    "[Laura.name] has a death grip and is a bit {i}too{/i} enthusiastic, causing more pain than pleasure. Although, she does lessen the pressure when you wince."
                elif Characters[0] in [Jean]:
                    "[Jean.name] is overly cautious and has a light touch. . . {i}too{/i} light, and you struggle to feel much."
            elif dice_roll == 2:
                "She continues to stroke you but still doesn't quite know what she's doing, and she ends up being too rough for comfort."
            elif dice_roll == 3:
                "You wince slightly with the next stroke, feeling more pain than pleasure, as she struggles to figure out what she's doing."
            elif dice_roll == 4:
                "Instead of being too rough, she overcompensates and ends up being too gentle, causing you to barely feel anything as she continues to stroke."

        $ Characters.remove(Characters[0])

    return

label fondle_balls_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].History.check("fondle_balls") >= 6:
            $ increase_Character_desire(Characters[0], 2, limit = 85)
            $ increase_Character_desire(Player, 4, limit = 95)
            
            if Characters[0] in [Laura]:
                $ dice_roll = renpy.random.randint(1, 5)
            else:
                $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] fondles your balls, applying just the right amount of pressure."
            elif dice_roll == 2:
                "[Characters[0].name] gives your balls a gentle squeeze, and it seems like she enjoys playing with them."
            elif dice_roll == 3:
                "[Characters[0].name]'s hand is wrapped around your balls, and some gentle fondling shows she knows what she's doing."
            elif dice_roll == 4:
                "[Characters[0].name] fondles your balls less than gently, seeming to enjoy squeezing them too hard and making you wince."
            elif dice_roll == 5:
                "[Characters[0].name] grips your balls tightly, slowly squeezing harder and harder before finally releasing."
        else:
            $ increase_Character_desire(Characters[0], 1, limit = 85)
            $ increase_Character_desire(Player, 2, limit = 95)

            if Characters[0] in [Laura]:
                $ dice_roll = renpy.random.randint(1, 4)
            else:
                $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "One of [Characters[0].name]'s hands plays with your balls, much too roughly, causing more pain than pleasure."
            elif dice_roll == 2:
                "[Characters[0].name] tries to fondle your balls, but fumbles around more than anything, not accomplishing much."
            elif dice_roll == 3:
                "[Characters[0].name] accidentally squeezes one of your balls too tightly, causing you to wince."
            elif dice_roll == 4:
                "[Characters[0].name] roughly plays with your balls, seemingly on purpose, despite all the wincing you do."

        $ Characters.remove(Characters[0])

    return

label blowjob_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Action.mode == 1:
            $ increase_Character_desire(Characters[0], 2, limit = 90)
            $ increase_Character_desire(Player, 6)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "Her soft lips press against your shaft as she kisses every inch of you."
            elif dice_roll == 2:
                "She makes sure to kiss you from top to bottom, enjoying how you twitch with every touch of her lips."
            elif dice_roll == 3:
                "She pays special attention to the head, as her lips press into you."
        elif Action.mode == 2:
            $ increase_Character_desire(Characters[0], 3, limit = 90)
            $ increase_Character_desire(Player, 8)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "Her tongue slides up and down your shaft, every time it slides over the head, a wave of pleasure flows through you."
            elif dice_roll == 2:
                "She swirls her tongue around the head before licking down the length of your shaft."
            elif dice_roll == 3:
                "Each pass of her tongue makes you twitch, as she makes sure to cover every last inch."
        elif Action.mode == 3:
            if Characters[0].History.check("blowjob") >= 10:
                $ increase_Character_desire(Characters[0], 6, limit = 95)
                $ increase_Character_desire(Player, 20)

                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    "Her lips apply just the right amount of pressure as her tongue swirls around your head. She knows exactly what gets you off, and is capitalizing on all that experience."
                elif dice_roll == 2:
                    "She takes you deeper than before, causing waves of pleasure to flow through you with each movement. Her masterful movements display how intimately familiar she is with your cock by now."
                elif dice_roll == 3:
                    "She sucks with the perfect amount of pressure, pushing all the right buttons to get you off as fast as possible. It's like she's enjoying this even more than you do."
            elif Characters[0].History.check("blowjob") >= 5:
                $ increase_Character_desire(Characters[0], 5, limit = 95)
                $ increase_Character_desire(Player, 15)

                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    "She sucks your cock, putting her tongue to good use, but still manages to go too deep causing her to gag. She's getting better, but still has a way to go."
                elif dice_roll == 2:
                    "Her tongue swirls around your head as she continues to suck your cock, sending waves of pleasure through you. That is, until her teeth start getting involved. . . at least she's getting better."
                elif dice_roll == 3:
                    "She goes a bit too deep, gagging slightly, but quickly corrects herself and keeps sucking. You can tell she's improving as she doesn't skip a beat."
            else:
                $ increase_Character_desire(Characters[0], 4, limit = 95)
                $ increase_Character_desire(Player, 10)

                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    "She's enthusiastic, but there's a bit too much teeth, and too little sucking to be a proper blowjob. Her lack of experience shows."
                elif dice_roll == 2:
                    "Her tongue fumbles around as she tries to suck your cock. It's not un-pleasurable per se, but it's clear she doesn't quite know what she's doing."
                elif dice_roll == 3:
                    "She doesn't seem to know her own limits yet when she takes you too deep, causing her to gag. She keeps sucking, but could use a lot of practice."

        $ Characters.remove(Characters[0])

    return

label suck_balls_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label deepthroat_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].throat_training == 1:
            $ increase_Character_desire(Characters[0], 2, limit = 95)
            $ increase_Character_desire(Player, 10)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] only manages the first few inches, before gagging. She's not deterred at all, as she goes right back for more."
            elif dice_roll == 2:
                "You can feel her throat involuntarily tighten around you, as she gags, forcing her to pull back."
            elif dice_roll == 3:
                "She chokes, and has to come up for air before she can take you deeper than a couple inches."
        elif Characters[0].throat_training == 2:
            $ increase_Character_desire(Characters[0], 5, limit = 95)
            $ increase_Character_desire(Player, 12)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] gets a bit over confident going too deep, as she gags, her throat tightening around your cock. Undeterred, she manages to keep sucking."
            elif dice_roll == 2:
                "[Characters[0].name] keeps sucking, not going too much deeper than before, but at least she knows her limits. And when she does gag, she doesn't let it stop her."
            elif dice_roll == 3:
                "[Characters[0].name] makes up for lack of depth with enthusiasm, as she tries to push past her gag reflex. She also doesn't have to come up for breath as often."
        elif Characters[0].throat_training == 3:
            $ increase_Character_desire(Characters[0], 7, limit = 95)
            $ increase_Character_desire(Player, 14)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "You feel your cock touch the back of her throat before she has to pull back. She gags slightly, but manages to keep it together and keep sucking."
            elif dice_roll == 2:
                "[Characters[0].name] seems like she's really starting to enjoy this, as you can feel the occasional moan around your cock. She's able to go deeper than before, but still doesn't seem satisfied."
            elif dice_roll == 3:
                "[Characters[0].name] tries pushing it, and you feel her throat tighten around you as she gags. She's very determined to get those last couple inches as she keeps on trying."
        elif Characters[0].throat_training == 4:
            $ increase_Character_desire(Characters[0], 8, limit = 95)
            $ increase_Character_desire(Player, 18)
            
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "Your cock slides all the way down her throat, as she manages to take you up to the hilt. You feel her moan around you, and it seems like [Characters[0].name]'s getting off to it just as much as you."
            elif dice_roll == 2:
                "[Characters[0].name] shows off her progress, as your cock slides smoothly down her throat. She still gags a bit, but seems to enjoy the sensation of choking on you."
            elif dice_roll == 3:
                "You feel your cock hit the back of her throat, but she pushes you deeper, pulling you all the way down. Every inch of you fits inside her, and she doesn't seem to want to come up for air, thoroughly enjoying the sensation."

        $ Characters.remove(Characters[0])

    return

label titjob_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label footjob_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label self_touch_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 12)
            $ increase_Character_desire(Player, 6, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] shudders violently as she continues to masturbate, her pussy now dripping wet."
            elif dice_roll == 2:
                "[Characters[0].name]'s fingers are slick, and she can't help but twitch as she continues focusing on her clit."
            elif dice_roll == 3:
                "[Characters[0].name] continues to masturbate, picking up the pace as she gets closer to the edge." 
        else:
            $ increase_Character_desire(Characters[0], 8)
            $ increase_Character_desire(Player, 4, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] continues masturbating, her fingers focusing on her clit as she shudders."
            elif dice_roll == 2:
                "[Characters[0].name] slides her fingers across her slit, twitching with every motion as she masturbates."
            elif dice_roll == 3:
                "[Characters[0].name] strokes her pussy with deliberate motions, not too slow, not too fast."

        $ Characters.remove(Characters[0])

    return

label self_finger_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 10)
            $ increase_Character_desire(Player, 7, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] slides her finger in and out of her ass even faster, causing it to twitch."
            elif dice_roll == 2:
                "[Characters[0].name]'s ass quivers as she pushes her fingers into it, as deep as she can reach."
            elif dice_roll == 3:
                "[Characters[0].name]'s fingers rapidly slide in and out of her ass as she quivers with every motion."
        else:
            $ increase_Character_desire(Characters[0], 6)
            $ increase_Character_desire(Player, 5, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] slowly slides her finger in and out of her ass, occasionally trying two at a time."
            elif dice_roll == 2:
                "[Characters[0].name]'s ass twitches as she fingers it, enjoying the novel sensation."
            elif dice_roll == 3:
                "[Characters[0].name] pulls her finger all the way out of her ass and you watch it twitch before she puts it back in."

        $ Characters.remove(Characters[0])

    return

label self_vibrator_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 14)
            $ increase_Character_desire(Player, 7, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name]'s legs quiver and she moans uncontrollably as the vibrator brings her right up to the edge."
            elif dice_roll == 2:
                "You notice the twitches and shudders start to get more frequent as [Characters[0].name] presses the vibrator into herself."
            elif dice_roll == 3:
                "[Characters[0].name]'s whole body starts to shudder as waves of pleasure radiate throughout her thanks to the vibrator."
        else:
            $ increase_Character_desire(Characters[0], 12)
            $ increase_Character_desire(Player, 5, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] presses the vibrator up against her clit, moaning as it makes contact."
            elif dice_roll == 2:
                "The vibrator makes its way across [Characters[0].name]'s pussy, causing her to shudder."
            elif dice_roll == 3:
                "[Characters[0].name] is unable to suppress her moans as the vibrator presses against her."

        $ Characters.remove(Characters[0])

    return

label self_dildo_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 12)
            $ increase_Character_desire(Player, 7, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] slides the dildo in and out of her pussy even faster, shuddering with every motion."
            elif dice_roll == 2:
                "[Characters[0].name]'s thumb toys with her clit as she continues playing with the dildo, every movement eliciting a moan."
            elif dice_roll == 3:
                "[Characters[0].name] moans louder and louder as the dildo slides in and out of her dripping wet pussy."
        else:
            $ increase_Character_desire(Characters[0], 10)
            $ increase_Character_desire(Player, 5, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] steadily slides the dildo in and out of her pussy."
            elif dice_roll == 2:
                "[Characters[0].name] guides the dildo into her pussy, holding it inside and grinding it around, before pulling it back out."
            elif dice_roll == 3:
                "The dildo doesn't quite seem to satisfy [Characters[0].name] as she slides it in and out, undoubtedly wishing it was you instead."
        $ Characters.remove(Characters[0])

    return

label self_dildo_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 10)
            $ increase_Character_desire(Player, 8, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] slides the dildo in and out of her ass even faster, shuddering with every motion as her ass quivers around it."
            elif dice_roll == 2:
                "[Characters[0].name]'s thumb plays with her clit as she continues playing with the dildo, every movement eliciting a moan."
            elif dice_roll == 3:
                "[Characters[0].name] moans louder and louder as the dildo slides in and out of her ass, her entire body shuddering."
        else:
            $ increase_Character_desire(Characters[0], 8)
            $ increase_Character_desire(Player, 6, limit = 90)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name] steadily slides the dildo in and out of her ass, making sure not to go too deep."
            elif dice_roll == 2:
                "[Characters[0].name] guides the dildo into her ass, holding it inside and grinding it around, before pulling it back out."
            elif dice_roll == 3:
                "The dildo doesn't quite seem to satisfy [Characters[0].name] as she slides it in and out, undoubtedly wishing it was you instead."

        $ Characters.remove(Characters[0])

    return

label jerk_off_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:

        $ Characters.remove(Characters[0])

    return

label grind_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_pool = [1, 2, 3]

        if intensity >= 50:
            $ increase_Character_desire(Characters[0], 10)
            $ increase_Character_desire(Player, 10)

            $ dice_pool.append(4)
        elif speed >= 50:
            $ increase_Character_desire(Characters[0], 8)
            $ increase_Character_desire(Player, 10)

            $ dice_pool.append(5)
        else:
            $ increase_Character_desire(Characters[0], 7)
            $ increase_Character_desire(Player, 8)

        if Characters[0].desire >= 75:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            "You continue to grind against [Characters[0].name], her hips pushing back into you in response."
        elif dice_roll == 2:
            "[Characters[0].name] moans as her pussy slides along the length of your cock, the pressure mounting."
        elif dice_roll == 3:
            "Your cock presses against [Characters[0].name]'s pussy, every stroke causing her to shudder."
        elif dice_roll == 4:
            "[Characters[0].name] shudders, as every inch of your cock grinds against her."
        elif dice_roll == 5:
            "You grind against [Characters[0].name], faster and faster, the friction against her pussy causing her to twitch."
        elif dice_roll == 6:
            "You press up against [Characters[0].name] harder, her body starting to shudder uncontrollably as your cock grinds against her."

        $ Characters.remove(Characters[0])

    return

label grind_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_pool = [1, 2, 3]

        if intensity >= 50:
            $ increase_Character_desire(Characters[0], 8)
            $ increase_Character_desire(Player, 9)

            $ dice_pool.append(4)
        elif speed >= 50:
            $ increase_Character_desire(Characters[0], 6)
            $ increase_Character_desire(Player, 8)

            $ dice_pool.append(5)
        else:
            $ increase_Character_desire(Characters[0], 5)
            $ increase_Character_desire(Player, 7)

        if Characters[0].desire >= 75:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            "You continue to grind against [Characters[0].name], her hips pushing back into you in response."
        elif dice_roll == 2:
            "[Characters[0].name] moans as your cock presses up against her hole, causing it to quiver."
        elif dice_roll == 3:
            "Your cock slides between [Characters[0].name]'s cheeks, every stroke causing her to shudder."
        elif dice_roll == 4:
            "[Characters[0].name] shudders as every inch of your cock grinds against her."
        elif dice_roll == 5:
            "You grind against [Characters[0].name], faster and faster, the friction against her ass causing her to twitch."
        elif dice_roll == 6:
            "You press up against [Characters[0].name]'s ass harder, her body starting to shudder uncontrollably and her hole quivering."

        $ Characters.remove(Characters[0])

    return

label sex_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Action.mode == 1:
            $ increase_Character_desire(Characters[0], 6)
            $ increase_Character_desire(Player, 8)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "You press the tip into her until it pushes past the resistance, only going in to the head, before pulling back out."
            elif dice_roll == 2:
                "As you slide it back out you feel the grip of her lips, as if they're trying to stop you."
            elif dice_roll == 3:
                "She shudders as the head slides in, and you can feel how wet and warm she is before pulling back out."
        elif Action.mode == 2:
            if Characters[0].History.check("sex") >= 10:
                $ increase_Character_desire(Characters[0], 14)
                $ increase_Character_desire(Player, 16)

                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    "[Characters[0].name] pushes her hips towards you trying to take you as deep as possible, as every thrust elicits a shudder and a moan from her."
                elif dice_roll == 2:
                    "Your cock glides back and forth inside her, feeling like it was meant to be there. She can't help but moan and twitch with every motion."
                elif dice_roll == 3:
                    "Every thrust sends a wave of pleasure through both of you, causing [Characters[0].name] to moan and shudder uncontrollably, her pussy tightening around your cock."
            elif Characters[0].History.check("sex") >= 5:
                $ increase_Character_desire(Characters[0], 10)
                $ increase_Character_desire(Player, 14)

                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    "You thrust in and out, her pussy twitching around your cock. [Characters[0].name] is starting to get used to the feeling of you inside her, but still occasionally winces in pain."
                elif dice_roll == 2:
                    "She tries pushing her hips against you in time with your thrusts, getting into the flow of things, but accidentally takes you too deep causing her to gasp from the pain."
                elif dice_roll == 3:
                    "[Characters[0].name] moans as you continue to thrust into her, enjoying the sensation as much as you are. She does gasp from pain when you go a bit too hard."
            else:
                $ increase_Character_desire(Characters[0], 8)
                $ increase_Character_desire(Player, 12)

                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    "You steadily thrust in and out causing her to shudder, but she also cringes in pain a few times."
                elif dice_roll == 2:
                    "She's not quite used to you yet, grimacing as you continue to thrust into her."
                elif dice_roll == 3:
                    "Your cock glides in and out of her, causing both pleasure and a bit of pain as she winces."

        $ Characters.remove(Characters[0])

    return

label anal_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].History.check("anal") >= 2:
            if Action.mode == 1:
                if Characters[0].anal_training == 1:
                    $ increase_Character_desire(Characters[0], 1)
                    $ increase_Character_desire(Player, 6)

                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        "[Characters[0].name] winces as you slide the tip in and out of her ass, pushing against the substantial resistance."
                    elif dice_roll == 2:
                        "[Characters[0].name]'s still way too tight, and you couldn't go any deeper even if you tried. She squeaks in pain every time your tip pushes inside."
                    elif dice_roll == 3:
                        "Your tip slides in and out of [Characters[0].name]'s ass, every motion causing her to wince."
                elif Characters[0].anal_training == 2:
                    $ increase_Character_desire(Characters[0], 4)
                    $ increase_Character_desire(Player, 12)

                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        "You slide the tip inside with relative ease as [Characters[0].name]'s starting to get used to it, but she still winces."
                    elif dice_roll == 2:
                        "It seems like [Characters[0].name]'s starting to enjoy it as you hear the occasional moan when your cock presses inside her. Although, she winces more often than not."
                    elif dice_roll == 3:
                        "[Characters[0].name] twitches as the tip of your cock slides inside her. You think she could take it deeper, but don't push it when she grimaces in pain."
                elif Characters[0].anal_training == 3:
                    $ increase_Character_desire(Characters[0], 10)
                    $ increase_Character_desire(Player, 14)

                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        "The tip of your cock slides in and out of [Characters[0].name]'s hole with ease, the occasional moan escaping from her mouth."
                    elif dice_roll == 2:
                        "[Characters[0].name] pushes back against you as your cock slides inside her, as if she's trying to make you go deeper."
                    elif dice_roll == 3:
                        "[Characters[0].name] shudders with every motion, and the tip of your cock smoothly glides in and out of her."
            elif Action.mode == 2:
                if Characters[0].anal_training == 1:
                    $ increase_Character_desire(Characters[0], 1)
                    $ increase_Character_desire(Player, 6)

                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        "[Characters[0].name] winces as you slide the tip in and out of her ass, pushing against the substantial resistance."
                    elif dice_roll == 2:
                        "[Characters[0].name]'s still way too tight, and you couldn't go any deeper even if you tried. She squeaks in pain every time your tip pushes inside."
                    elif dice_roll == 3:
                        "Your tip slides in and out of her ass, every motion causing her to wince."
                elif Characters[0].anal_training == 2:
                    $ increase_Character_desire(Characters[0], 5)
                    $ increase_Character_desire(Player, 12)

                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        "You manage to push at least a couple inches inside [Characters[0].name], but she winces, stopping you from going too deep yet."
                    elif dice_roll == 2:
                        "Your cock glides back and forth inside [Characters[0].name]'s ass as it involuntarily tightens around you, preventing you from going too deep."
                    elif dice_roll == 3:
                        "It seems like [Characters[0].name]'s starting to feel more pleasure than pain, as your cock slides in deeper than before, eliciting a moan."
                elif Characters[0].anal_training == 3:
                    $ increase_Character_desire(Characters[0], 12)
                    $ increase_Character_desire(Player, 16)

                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        "Your cock easily glides in and out of [Characters[0].name]'s ass, every motion causing her to shudder in ecstasy. Her hips push back against you as she tries to force you deeper inside."
                    elif dice_roll == 2:
                        "[Characters[0].name] seems like she's really starting to enjoy this, as you can feel her ass tighten around you. She's able to take you all the way in and moans with every motion."
                    elif dice_roll == 3:
                        "[Characters[0].name]'s ass quivers as your cock thrusts back and forth inside it. The deeper you go, the more she seems to enjoy it"  
        else:
            $ increase_Character_desire(Player, 2, limit = 60)
            
            if Characters[0] in [Rogue]:
                $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                
                "You press the tip up against her, her tight hole providing a lot of resistance." 
                "You manage to get the head in before she whimpers and stops you from going further." 
                
                $ Characters[0].change_face("worried1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "Ah'm sorry, deeper than that hurts too much. . .")
                $ renpy.say(Characters[0].voice, "At least ah can handle the tip for now.")
                
                $ Characters[0].change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] will have to practice before she can take it any deeper."
            elif Characters[0] in [Laura]:
                $ Characters[0].change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 
                
                "You press your cock up against her hole, [Characters[0].name]'s small stature not doing her any favors. . ."
                "It's a very tight fit, and you only manage to get the tip in before she growls from pain." 
                
                $ Characters[0].change_face("angry1", mouth = "lipbite", blush = 2) 
                
                $ renpy.say(Characters[0].voice, "That is deep enough for now. . .")
                
                $ Characters[0].change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2) 
                
                "[Characters[0].name] will have to practice before she can take it any deeper."
            elif Characters[0] in [Jean]:
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

label vibrator_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 14)
            $ increase_Character_desire(Player, 8, limit = 75)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "[Characters[0].name]'s legs quiver and she moans uncontrollably, as the vibrator brings her right up to the edge."
            elif dice_roll == 2:
                "You notice [Characters[0].name]'s twitches and shudders get more frequent as you press the vibrator into her with more pressure."
            elif dice_roll == 3:
                "[Characters[0].name]'s whole body starts to shudder as waves of pleasure radiate throughout her thanks to the vibrator."
        else:
            $ increase_Character_desire(Characters[0], 12)
            $ increase_Character_desire(Player, 6, limit = 75)

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                "You press the vibrator up against her clit causing [Characters[0].name] to moan as it makes contact."
            elif dice_roll == 2:
                "The vibrator makes its way across [Characters[0].name]'s' pussy, causing her to shudder."
            elif dice_roll == 3:
                "[Characters[0].name] is unable to suppress her moans, as the vibrator presses into her."

        $ Characters.remove(Characters[0])

    return

label dildo_pussy_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_pool = [1, 2, 3]

        if speed >= 75:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 12)
            $ increase_Character_desire(Player, 7, limit = 75)

            if dice_roll == 1:
                "You steadily slide the dildo in and out of [Characters[0].name]'s pussy, causing her to shudder with every motion."
            elif dice_roll == 2:
                "[Characters[0].name] thrusts her hips towards you as the dildo slides in and out, every movement eliciting a moan."
            elif dice_roll == 3:
                "[Characters[0].name] moans louder and louder as the dildo slides in and out of her dripping wet pussy."
            elif dice_roll == 4:
                "You pick up the pace, thrusting the dildo in and out of [Characters[0].name]'s pussy, eliciting moans and involuntary shudders."
        else:
            $ increase_Character_desire(Characters[0], 10)
            $ increase_Character_desire(Player, 5, limit = 75)

            if dice_roll == 1:
                "You steadily slide the dildo in and out of [Characters[0].name]'s pussy."
            elif dice_roll == 2:
                "[Characters[0].name] twitches as you guide the dildo into her pussy, holding it inside and grinding it around, before sliding it back out."
            elif dice_roll == 3:
                "The dildo doesn't quite seem to satisfy [Characters[0].name] as you slide it in and out. She undoubtedly wishes it was you inside her instead."
            elif dice_roll == 4:
                "You pick up the pace, thrusting the dildo in and out of [Characters[0].name]'s pussy, eliciting moans and involuntary shudders."

        $ Characters.remove(Characters[0])

    return

label dildo_ass_continuations(Action):
    $ Characters = get_Action_Characters(Action)

    while Characters:
        $ dice_pool = [1, 2, 3]

        if speed >= 75:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if Characters[0].desire >= 75:
            $ increase_Character_desire(Characters[0], 10)
            $ increase_Character_desire(Player, 6, limit = 75)

            if dice_roll == 1:
                "You steadily slide the dildo in and out of [Characters[0].name]'s ass even faster. She moans with every motion as her ass quivers around it."
            elif dice_roll == 2:
                "[Characters[0].name] thrusts her hips towards you as the dildo slides in and out, every movement eliciting a moan."
            elif dice_roll == 3:
                "[Characters[0].name] moans louder and louder as the dildo slides in and out of her ass, her entire body shuddering."
            elif dice_roll == 4:
                "You pick up the pace, thrusting the dildo in and out of [Characters[0].name]'s ass, eliciting moans and involuntary shudders."
        else:
            $ increase_Character_desire(Characters[0], 8)
            $ increase_Character_desire(Player, 5, limit = 75)

            if dice_roll == 1:
                "You steadily slide the dildo in and out of [Characters[0].name]'s ass, making sure not to go too deep."
            elif dice_roll == 2:
                "[Characters[0].name] quivers as you guide the dildo into her ass, holding it inside and grinding it around, before pulling it back out."
            elif dice_roll == 3:
                "The dildo doesn't quite seem to satisfy [Characters[0].name] as you slide it in and out. She undoubtedly wishes it was you inside her instead."
            elif dice_roll == 4:
                "You pick up the pace, thrusting the dildo in and out of [Characters[0].name]'s ass, eliciting moans and involuntary shudders."

        $ Characters.remove(Characters[0])

    return