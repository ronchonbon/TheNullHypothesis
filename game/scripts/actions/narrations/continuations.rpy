label makeout_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1, 2, 3, 4, 5]

        if temp_Characters[0].History.check("makeout") >= 12:
            $ dice_pool.append(6)
            $ dice_pool.append(7)
            $ dice_pool.append(8)
            $ dice_pool.append(9)
            $ dice_pool.append(10)
        elif temp_Characters[0].History.check("makeout") >= 6:
            $ dice_pool.append(11)
            $ dice_pool.append(12)
            $ dice_pool.append(13)
            $ dice_pool.append(14)
        else:
            $ dice_pool.append(15)
            $ dice_pool.append(16)
            $ dice_pool.append(17)
            $ dice_pool.append(18)

            if renpy.random.random() > 0.9:
                $ dice_pool.append(19)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, "Your tongues dance together as you continue to enjoy each other.")
        elif dice_roll == 2:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"{owner.capitalize()} lips are soft against yours, and she tastes a bit like strawberries.")
        elif dice_roll == 3:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"{subject.capitalize()} squeezes you tightly, pressing her lips firmly against yours.")
        elif dice_roll == 4:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"You run a hand through {owner.capitalize()} hair while continuing to kiss her.")
        elif dice_roll == 5:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"{owner.capitalize()} hands wander across your body as your tongues dance inside each other's mouth.")
        elif dice_roll == 6:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"{owner.capitalize()} lips glides between yours with practiced ease as your tongues meet.")
        elif dice_roll == 7:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"{owner.capitalize()} lips part, inviting yours in with enthusiasm.")
        elif dice_roll == 8:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"{subject.capitalize()} seems to thoroughly enjoy the taste of your lips as she nibbles on them, using just the right amount of pressure.")
        elif dice_roll == 9:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"You gently kiss {owner.capitalize()} neck, and she shudders in nothing but pure ecstasy.")
        elif dice_roll == 10:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"Nibbling on {owner.capitalize()} ear elicits a shudder and a moan, and she squeezes you tightly.")
        elif dice_roll == 11:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"Despite the excitement, {owner.capitalize()} lips are still a bit clumsy as they move around yours.")
        elif dice_roll == 12:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"{owner.capitalize()} lips part, inviting yours in, and it's clear she's starting to get used to you.")
        elif dice_roll == 13:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"{subject.capitalize()} seems to be thoroughly enjoying the taste of your lips as she nibbles on them, still a bit too hard.")
        elif dice_roll == 14:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"You gently kiss {owner.capitalize()} neck, and she can't help but shudder despite starting to get used to the sensation.")
        elif dice_roll == 15:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"You gently kiss {owner.capitalize()} neck, causing her to shudder as she's not yet used to such a sensation from you.")
        elif dice_roll == 16:
            $ temp_Characters[0].change_face("kiss2", blush = 2) 
            
            $ renpy.say(None, f"{subject.capitalize()} seems to be thoroughly enjoying the taste of your lips, but nibbles on them a bit too hard.")
        elif dice_roll == 17:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"{owner.capitalize()} lips part, inviting yours in, but it's clear she's not quite used to you yet.")
        elif dice_roll == 18:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"Despite the excitement, {owner.capitalize()} lips clumsily move around yours.")
        elif dice_roll == 19:
            $ temp_Characters[0].change_face("kiss1", blush = 1) 
            
            $ renpy.say(None, f"The fun is briefly interrupted as {owner.capitalize()} teeth come into contact with yours, causing you to wince.")
            
            $ temp_Characters[0].change_face("worried2")
            
            $ renpy.say(temp_Characters[0].voice, "Sorry. . .")

        $ temp_Characters.remove(temp_Characters[0])

    return

label choke_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ temp_Characters[0].blush += 1 if temp_Characters[0].blush < 3 else 0

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"Your hand gently squeezes {owner} neck, causing her face to flush.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You feel {owner} pulse quicken as you keep the pressure around her neck.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You feel the blood rush beneath {owner} skin as you put even pressure on her neck.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_over_clothes_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0] in [Laura]:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"You caress {owner} inner thigh, causing a slight shudder despite her clothes limiting the sensation.")
        elif dice_roll == 2:
            $ renpy.say(None, f"The touch makes {owner} leg twitch even through the clothes, as you move your hand up from her knee, making sure not to go too high.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You can feel {owner} warmth even through the clothes, and your hands makes its way up and down her thigh.")
        elif dice_roll == 4:
            $ renpy.say(None, f"Your hand glides along {owner} thigh, feeling the ample muscle beneath her clothes.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_higher_over_clothes_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"As your hand moves higher up {owner} thigh, brushing up against her crotch, you can feel the warmth even through her clothes.")     
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} can't help but twitch as your hand makes its way up her thigh, briefly touching her crotch through her clothes.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You gently caress {owner} inner thigh, going as high as her crotch, feeling her warmth even through her clothes.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0] in [Laura]:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"You caress {owner} inner thigh, eliciting a shudder, the sensation unimpeded by any clothing.")
        elif dice_roll == 2:
            $ renpy.say(None, f"The touch makes {owner} leg twitch as you move your hand up from her knee, making sure not to go too high.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You can feel the warmth of {owner} skin as your hand makes its way up and down her thigh.")
        elif dice_roll == 4:
            $ renpy.say(None, f"Your hand glides along the soft skin of {owner} thigh, feeling its ample muscle.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_thighs_higher_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"As your hand moves higher up {owner} thigh, brushing up against her crotch, you can feel the warmth as she shudders from your touch.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} can't help but twitch as your hand makes its way up her thigh, briefly touching her crotch.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You gently caress {owner} inner thigh, going as high as her crotch, feeling her warmth through her skin.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_breasts_over_clothes_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "breasts"
        else:
            $ noun = "tits"

        $ dice_pool = [1, 2]

        if temp_Characters[0] in [Rogue, Jean]:
            $ dice_pool.append(3)
        elif temp_Characters[0] in [Laura]:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"As your hands massage {owner} {noun}, you can feel her nipples stiffen even through her top.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} leans into your hand as you fondle her {noun}, their softness evident even through her top.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You gently fondle {owner} {noun} through her top, their size too big for a single hand as they spill through your fingers.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You gently fondle {owner} {noun} through her top, their smaller size fitting comfortably in your hand.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_breasts_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "breasts"
        else:
            $ noun = "tits"

        $ dice_pool = [1, 2]

        if temp_Characters[0] in [Rogue]:
            $ dice_pool.append(3)
        elif temp_Characters[0] in [Laura]:
            $ dice_pool.append(4)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"As your hands massage {owner} {noun}, you can feel her soft skin, and her nipples stiffen with even the slightest touch.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} leans into your hand as you fondle her {noun}, their softness a contrast to the hard nipple under your thumb.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You gently fondle {owner} {noun}, their size too big for a single hand as they spill through your fingers. She shudders as you brush your thumb across her already stiff nipples.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You gently fondle {owner} {noun}, their smaller size fitting comfortably in your hand. She shudders as you brush your thumb across her already stiff nipples.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label pinch_nipples_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.75:
            $ adjective = "stiff "
        elif renpy.random.random() > 0.5:
            $ adjective = "sensitive "
        elif renpy.random.random() > 0.25:
            $ adjective = "firm "
        else:
            $ adjective = ""

        if temp_Characters[0].piercings["nipple"]:
            $ dice_roll = renpy.random.randint(1, 4)
        else:
            $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"You put {owner} {adjective}nipple in between your thumb and forefinger and give it a good tug, causing her to jerk in surprise.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{owner.capitalize()} {adjective}nipple stiffens even further as you give it a pinch, eliciting a moan from her.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} stiffens as you give her {adjective}nipple a pinch.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You give {owner} piercing a gentle tug, causing her to stiffen.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label suck_nipples_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.75:
            $ adjective = "stiff "
        elif renpy.random.random() > 0.5:
            $ adjective = "sensitive "
        elif renpy.random.random() > 0.25:
            $ adjective = "firm "
        else:
            $ adjective = ""

        if temp_Characters[0].piercings["nipple"]:
            $ dice_roll = renpy.random.randint(1, 5)
        else:
            $ dice_roll = renpy.random.randint(1, 4)

        if dice_roll == 1:
            $ renpy.say(None, f"You put {owner} {adjective}nipple in your mouth and suck, twirling your tongue around it, eliciting a moan.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{owner.capitalize()} {adjective}nipple stiffens as you nibble on it, and she runs a hand through your hair.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} holds your head to her breast as you continue to lick around and over her {adjective}nipple.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You cup {owner} breast in your hand, gently biting down on her {adjective}nipple.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You tug on {owner} piercing with your mouth, causing her to lean into you.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_pussy_over_clothes_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "pussy"
        else:
            $ noun = "crotch"

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"Your hand presses into {owner} {noun}, causing her to squirm at the touch even if it's through her clothes.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{owner.capitalize()} {noun} radiates warmth as you fondle it, her clothes apparently doing little to dampen the sensation.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} leans into your hand, seeking out your touch as it's partially dampened by the fabric.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label touch_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "folds"
        elif renpy.random.random() > 0.33:
            $ noun = "cunt"
        else:
            $ noun = "pussy"

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"Your hand presses into {owner} crotch, gliding across her already wet {noun}, eliciting a shudder.")
        elif dice_roll == 2:
            $ renpy.say(None, f"With a thumb on {owner} clit, you apply gentle pressure as she leans into you.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} lets out a moan as your hand moves its way around her exposed {noun}, already slick.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label finger_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "hole"
        elif renpy.random.random() > 0.33:
            $ noun = "folds"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4, 5]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(6)
            
        $ dice_roll = renpy.random.choice(dice_pool)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} squirms uncomfortably as your fingers slide in and out of her {noun}.") 
        elif dice_roll == 2:
            $ renpy.say(None, f"As your fingers slide in and out, {subject} can't help but shudder, as she involuntarily tightens around your fingers.") 
        elif dice_roll == 3:
            $ renpy.say(None, f"You gently rub {owner} clit with your thumb as your fingers continue to glide in and out of her {adjective}{noun}.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You curl your fingers slightly hitting just the right spot, eliciting a shudder as {subject} involuntarily moans in ecstasy.")
        elif dice_roll == 5:
            $ renpy.say(None, f"Your fingers thrust in and out of {owner} {adjective}{noun}, causing moans and shudders throughout her body.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} {noun} twitches and tightens around your fingers, now dripping wet, as she draws close to the edge.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label eat_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "folds"
        elif renpy.random.random() > 0.33:
            $ noun = "labia"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"Wrapping your lips over {owner} clit, you suck and play with it with your tongue, eliciting a series of moans.")
        elif dice_roll == 2:
            $ renpy.say(None, f"Your tongue moves its way around {owner} {adjective}{noun}, leaving no part ignored, as she shudders with every motion.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} runs a hand through your hair, anchoring your head in place, as you continue pleasuring her with your mouth.")
        
        $ temp_Characters.remove(temp_Characters[0])

    return

label grab_ass_over_clothes_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} leans back into your hand, seeking the sensation of your touch as it's dampened by her clothes.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You gently massage {owner} ass, enjoying it in all its glory despite the barrier her clothing presents.")
        elif dice_roll == 3:
            $ renpy.say(None, f"With a firm grasp, you spread and kneed {owner} cheeks, only her clothes preventing anything more.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label grab_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} leans back into your hand, thoroughly enjoying your touch as you knead into her cheeks.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You gently massage {owner} ass, enjoying it in all its glory, making sure to explore every inch of it.")
        elif dice_roll == 3:
            $ renpy.say(None, f"With a firm grasp, you spread and kneed {owner} cheeks, your hand occasionally sliding in between them, eliciting a moan.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label finger_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4, 5]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(6)
            
        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("grimace", eyes = "left")
            else:
                $ temp_Characters[0].change_face("grimace", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} winces a little in discomfort as you finger her {noun} - you should probably warm her up a little bit first.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} tightens even further around your finger as you continue to slide it in and out of her {adjective}{noun}.")
        elif dice_roll == 3:
            $ renpy.say(None, f"Your finger presses deeper inside {object}, her {adjective}{noun} not providing much resistance.")
        elif dice_roll == 4:
            $ renpy.say(None, f"Pulling your finger out, you tease {owner} {adjective}{noun} before sliding it back inside.")
        elif dice_roll == 5:
            $ renpy.say(None, f"Your finger slides in and out of {object}, as she involuntarily twitches and tightens around.")
        elif dice_roll == 6:
            $ renpy.say(None, f"Every motion causes {object} to twitch and shudder, your finger continuing to slide in and out of her {adjective}{noun} as it only gets tighter around you.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label eat_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.66:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.33:
            $ adjective = "perfect "
        else:
            $ adjective = ""

        $ dice_roll = renpy.random.randint(1, 3)

        if dice_roll == 1:
            $ renpy.say(None, f"You continue to tease {owner} {adjective}{noun} with your tongue, eliciting a moan whenever you do touch it.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} shudders with every pass of your tongue, as you lick around and over her {adjective}{noun}.")
        elif dice_roll == 3:
            $ renpy.say(None, f"You pull {owner} cheeks even farther apart and dive in, sucking and licking her {adjective}{noun}, eliciting a moan.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label handjob_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0].History.check("handjob") >= 10:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{subject.capitalize()} strokes you with a light but deft touch, her experience pleasuring you clear as she pushes all the right buttons.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{owner.capitalize()} grip is gentle but firm at the same time, each stroke sending waves of pleasure through you, especially when she plays with the head as well.")
            elif dice_roll == 3:
                $ renpy.say(None, f"Every stroke feels like it's designed to make you cum as fast as possible, {owner} hand a perfect fit around you, maximizing the pleasure.")
        elif temp_Characters[0].History.check("handjob") >= 5:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{subject.capitalize()} strokes you with more finesse and less trepidation this time, but an inconsistent grip makes her lack of experience evident.")
            elif dice_roll == 2:
                $ renpy.say(None, f"You wince when {subject} accidentally nudges one of your balls, but despite that she's getting better, if still having a way to go.")
            elif dice_roll == 3:
                $ renpy.say(None, f"A wave of pleasure runs through you as {subject} plays with your head, but it's ruined when she squeezes a bit too tightly. . . at least she's getting better.")
        else:
            $ dice_roll = renpy.random.randint(1, 4)

            if dice_roll == 1:
                if temp_Characters[0] in [Rogue]:
                    $ renpy.say(None, f"{subject.capitalize()} fumbles around a bit, still not used to having you in her hand. As a result, she's a bit too gentle, providing minimal sensation.")
                elif temp_Characters[0] in [Laura]:
                    $ renpy.say(None, f"{subject.capitalize()} has a death grip and is a bit too enthusiastic, causing more pain than pleasure. Although, she does lessen the pressure when you wince.")
                elif temp_Characters[0] in [Jean]:
                    $ renpy.say(None, f"{subject.capitalize()} is overly cautious and has a light touch. . . too light, and you struggle to feel much.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} continues to stroke you but still doesn't quite know what she's doing, and she ends up being too rough for comfort.")
            elif dice_roll == 3:
                $ renpy.say(None, f"You wince slightly with the next stroke, feeling more pain than pleasure, as {subject} struggles to figure out what she's doing.")
            elif dice_roll == 4:
                $ renpy.say(None, f"Instead of being too rough, {subject} overcompensates and ends up being too gentle, causing you to barely feel anything as she continues to stroke.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label fondle_balls_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0].History.check("fondle_balls") >= 6:
            if temp_Characters[0] in [Laura]:
                $ dice_roll = renpy.random.randint(1, 5)
            else:
                $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{subject.capitalize()} fondles your balls, applying just the right amount of pressure.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} gives your balls a gentle squeeze, and it seems like she enjoys playing with them.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{owner.capitalize()} hand is wrapped around your balls, and some gentle fondling shows she knows what she's doing.")
            elif dice_roll == 4:
                $ renpy.say(None, f"{subject.capitalize()} fondles your balls less than gently, seeming to enjoy squeezing them too hard and making you wince.")
            elif dice_roll == 5:
                $ renpy.say(None, f"{subject.capitalize()} grips your balls tightly, slowly squeezing harder and harder before finally releasing.")
        else:
            if temp_Characters[0] in [Laura]:
                $ dice_roll = renpy.random.randint(1, 4)
            else:
                $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"One of {owner} hands plays with your balls, much too roughly, causing more pain than pleasure.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} tries to fondle your balls, but fumbles around more than anything, not accomplishing much.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} accidentally squeezes one of your balls too tightly, causing you to wince.")
            elif dice_roll == 4:
                $ renpy.say(None, f"{subject.capitalize()} roughly plays with your balls, seemingly on purpose, despite all the wincing you do.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label blowjob_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if Action.mode == 1:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{owner.capitalize()} soft lips press against your shaft as she kisses every inch of you.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} makes sure to kiss you from top to bottom, enjoying how you twitch with every touch of her lips.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} pays special attention to the head, as her lips press into you.")
        elif Action.mode == 2:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{owner.capitalize()} tongue slides up and down your shaft, every time it slides over the head, a wave of pleasure flows through you.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} swirls her tongue around the head before licking down the length of your shaft.")
            elif dice_roll == 3:
                $ renpy.say(None, f"Each pass of {owner} tongue makes you twitch, as she makes sure to cover every last inch.")
        elif Action.mode == 3:
            if temp_Characters[0].History.check("blowjob") >= 10:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(None, f"{owner.capitalize()} lips apply just the right amount of pressure as her tongue swirls around your head. She knows exactly what gets you off, and is capitalizing on all that experience.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{subject.capitalize()} takes you deeper than before, causing waves of pleasure to flow through you with each movement. Her masterful movements display how intimately familiar she is with your cock by now.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} sucks with the perfect amount of pressure, pushing all the right buttons to get you off as fast as possible. It's like she's enjoying this even more than you do.")
            elif temp_Characters[0].History.check("blowjob") >= 5:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} sucks your cock, putting her tongue to good use, but still manages to go too deep causing her to gag. She's getting better, but still has a way to go.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{owner.capitalize()} tongue swirls around your head as she continues to suck your cock, sending waves of pleasure through you. That is, until her teeth start getting involved. . . at least she's getting better.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} goes a bit too deep, gagging slightly, but quickly corrects herself and keeps sucking. You can tell she's improving as she doesn't skip a beat.")
            else:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()}'s enthusiastic, but there's a bit too much teeth, and too little sucking to be a proper blowjob. Her lack of experience shows.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{owner.capitalize()} tongue fumbles around as she tries to suck your cock. It's not un-pleasurable per se, but it's clear she doesn't quite know what she's doing.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} doesn't seem to know her own limits yet when she takes you too deep, causing her to gag. She keeps sucking, but could use a lot of practice.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label suck_balls_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label deepthroat_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if temp_Characters[0].throat_training == 1:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{subject.capitalize()} only manages the first few inches, before gagging. She's not deterred at all, as she goes right back for more.")
            elif dice_roll == 2:
                $ renpy.say(None, f"You can feel {owner} throat involuntarily tighten around you, as she gags, forcing her to pull back.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} chokes and has to come up for air before she can take you deeper than a couple inches.")
        elif temp_Characters[0].throat_training == 2:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"{subject.capitalize()} gets a bit over confident going too deep, as she gags, her throat tightening around your cock. Undeterred, she manages to keep sucking.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} keeps sucking, not going too much deeper than before, but at least she knows her limits. And when she does gag, she doesn't let it stop her.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} makes up for lack of depth with enthusiasm, as she tries to push past her gag reflex. She also doesn't have to come up for breath as often.")
        elif temp_Characters[0].throat_training == 3:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"You feel your cock touch the back of {owner} throat before she has to pull back. She gags slightly, but manages to keep it together and keep sucking.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} seems like she's really starting to enjoy this, as you can feel the occasional moan around your cock. She's able to go deeper than before, but still doesn't seem satisfied.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} tries pushing it, and you feel her throat tighten around you as she gags. She's very determined to get those last couple inches as she keeps on trying.")
        elif temp_Characters[0].throat_training == 4:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"Your cock slides all the way down {owner} throat, as she manages to take you up to the hilt. You feel her moan around you, and it seems like she's getting off to it just as much as you.")
            elif dice_roll == 2:
                $ renpy.say(None, f"{subject.capitalize()} shows off her progress, as your cock slides smoothly down her throat. She still gags a bit, but seems to enjoy the sensation of choking on you.")
            elif dice_roll == 3:
                $ renpy.say(None, f"You feel your cock hit the back of {owner} throat, but she pushes you deeper, pulling you all the way down. Every inch of you fits inside her, and she doesn't seem to want to come up for air, thoroughly enjoying the sensation.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label titjob_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label footjob_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label self_touch_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} continues masturbating, her fingers focusing on her clit as she shudders.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} slides her fingers across her slit, twitching with every motion as she masturbates.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} strokes her pussy with deliberate motions, not too slow, not too fast.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} shudders violently as she continues to masturbate, her pussy now dripping wet.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{owner.capitalize()} fingers are slick, and she can't help but twitch as she continues focusing on her clit.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{subject.capitalize()} continues to masturbate, picking up the pace as she gets closer to the edge.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_finger_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} slowly slides her finger in and out of her {adjective}{noun}, occasionally trying two at a time.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{owner.capitalize()} {adjective}{noun} twitches as she fingers it, enjoying the novel sensation.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} pulls her finger all the way out of her {adjective}{noun} and you watch it twitch before she puts it back in.")
        if dice_roll == 4:
            $ renpy.say(None, f"{subject.capitalize()} slides her finger in and out of her {adjective}{noun} even faster, causing it to twitch.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{owner.capitalize()} {adjective}{noun} quivers as she pushes her fingers into it as deep as she can reach.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} fingers rapidly slide in and out of her {adjective}{noun} as she quivers with every motion.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_vibrator_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "clit"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "pulsing "
            elif renpy.random.random() > 0.33 and temp_Characters[0].desire >= 75:
                $ adjective = "throbbing "
            else:
                $ adjective = ""
        else:
            $ noun = "pussy"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "soaking wet "
            elif renpy.random.random() > 0.33:
                $ adjective = "glistening "
            else:
                $ adjective = ""

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} presses the vibrator up against her {adjective}{noun}, moaning as it makes contact.")
        elif dice_roll == 2:
            $ renpy.say(None, f"The vibrator makes its way across {owner} {adjective}{noun}, causing her to shudder.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} is unable to suppress her moans as the vibrator presses against her {adjective}{noun}.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{owner.capitalize()} legs quiver and she moans uncontrollably as the vibrator brings her right up to the edge.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You notice {owner} twitches and shudders getting more frequent as she presses the vibrator into herself.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} whole body starts to shudder as waves of pleasure radiate throughout her thanks to the vibrator.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_dildo_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
            $ noun = "cunt"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(5)
            $ dice_pool.append(6)
            $ dice_pool.append(7)
            
        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize} moves the dildo in and out of her, but seems fairly uncomfortable.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize} steadily slides the dildo in and out of her {adjective}{noun}.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize} guides the dildo into her {adjective}{noun}, holding it inside and grinding it around, before pulling it back out.")
        elif dice_roll == 4:
            $ renpy.say(None, f"The dildo doesn't quite seem to satisfy {object} as she slides it in and out, undoubtedly wishing it was you instead.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{subject.capitalize} slides the dildo in and out of her {adjective}{noun} even faster, shuddering with every motion.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} thumb toys with her clit as she continues playing with the dildo, every movement eliciting a moan.")
        elif dice_roll == 7:
            $ renpy.say(None, f"{subject.capitalize} moans louder and louder as the dildo slides in and out of her {adjective}{noun}.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label self_dildo_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(5)
            $ dice_pool.append(6)
            $ dice_pool.append(7)
            
        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} winces as she slides the dildo into her {noun} - she could probably use more foreplay.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} steadily slides the dildo in and out of her {adjective}{noun}, making sure not to go too deep.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} guides the dildo into her {adjective}{noun}, holding it inside and grinding it around, before pulling it back out.")
        elif dice_roll == 4:
            $ renpy.say(None, f"The dildo doesn't quite seem to satisfy {object} as she slides it in and out, undoubtedly wishing it was you instead.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{subject.capitalize()} slides the dildo in and out of her {adjective}{noun} even faster, shuddering with every motion as her ass quivers around it.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} thumb plays with her clit as she continues playing with the dildo, every movement eliciting a moan.")
        elif dice_roll == 7:
            $ renpy.say(None, f"{subject.capitalize()} moans louder and louder as the dildo slides in and out of her {adjective}{noun}, her entire body shuddering.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label jerk_off_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        $ temp_Characters.remove(temp_Characters[0])

    return

label grind_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if intensity >= Action.max_intensity[0]/2:
            $ dice_pool.append(5)
        elif speed >= Action.max_speed[0]/2:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You continue to grind against {object}, her hips pushing back into you in response.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} moans as her pussy slides along the length of your cock, the pressure mounting.")
        elif dice_roll == 3:
            $ renpy.say(None, f"Your cock presses against {owner} pussy, every stroke causing her to shudder.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You press up against {object} harder, her body starting to shudder uncontrollably as your cock grinds against her.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{subject.capitalize()} shudders, as every inch of your cock grinds against her.")
        elif dice_roll == 6:
            $ renpy.say(None, f"You grind against {object}, faster and faster, the friction against her pussy causing her to twitch.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label grind_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)

        if intensity >= Action.max_intensity[0]/2:
            $ dice_pool.append(5)
        elif speed >= Action.max_speed[0]/2:
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You continue to grind against {object}, her hips pushing back into you in response.")
        elif dice_roll == 2:
            $ renpy.say(None, f"{subject.capitalize()} moans as your cock presses up against her hole, causing it to quiver.")
        elif dice_roll == 3:
            $ renpy.say(None, f"Your cock slides between {owner} cheeks, every stroke causing her to shudder.")
        elif dice_roll == 4:
            $ renpy.say(None, f"You press up against {owner} ass harder, her body starting to shudder uncontrollably and her hole quivering.")
        elif dice_roll == 5:
            $ renpy.say(None, f"{subject.capitalize()} shudders as every inch of your cock grinds against her.")
        elif dice_roll == 6:
            $ renpy.say(None, f"You grind against {object}, faster and faster, the friction against her ass causing her to twitch.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label sex_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
            $ noun = "cunt"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        if Action.mode == 1:
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                $ renpy.say(None, f"You press the tip into {object} until it pushes past the resistance, only going in to the head, before pulling back out.")
            elif dice_roll == 2:
                $ renpy.say(None, f"As you slide it back out you feel the grip of {owner} lips, as if they're trying to stop you.")
            elif dice_roll == 3:
                $ renpy.say(None, f"{subject.capitalize()} shudders as the head slides in, and you can feel how wet and warm she is before pulling back out.")
        elif Action.mode == 2:
            if temp_Characters[0].History.check("sex") >= 10:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(None, f"{subject.capitalize()} pushes her hips towards you trying to take you as deep as possible, as every thrust elicits a shudder and a moan from her.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"Your cock glides back and forth inside {object}, feeling like it was meant to be there. She can't help but moan and twitch with every motion.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"Every thrust sends a wave of pleasure through both of you, causing {subject} to moan and shudder uncontrollably, her {adjective}{noun} tightening around your cock.")
            elif temp_Characters[0].History.check("sex") >= 5:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(None, f"You thrust in and out, {owner} {adjective}{noun} twitching around your cock. She's starting to get used to the feeling of you inside her, but still occasionally winces in pain.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{subject.capitalize()} tries pushing her hips against you in time with your thrusts, getting into the flow of things, but accidentally takes you too deep causing her to gasp from the pain.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"{subject.capitalize()} moans as you continue to thrust into her, enjoying the sensation as much as you are. She does gasp from pain when you go a bit too hard.")
            else:
                $ dice_roll = renpy.random.randint(1, 3)

                if dice_roll == 1:
                    $ renpy.say(None, f"You steadily thrust in and out causing {object} to shudder, but she also cringes in pain a few times.")
                elif dice_roll == 2:
                    $ renpy.say(None, f"{subject.capitalize()}'s not quite used to you yet, grimacing as you continue to thrust into her.")
                elif dice_roll == 3:
                    $ renpy.say(None, f"Your cock glides in and out of {owner} {adjective}{noun}, causing both pleasure and a bit of pain as she winces.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label anal_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75 and temp_Characters[0].anal_training >= 1:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.7:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        if temp_Characters[0].History.check("anal") >= 2:
            if Action.mode == 1:
                if temp_Characters[0].anal_training == 1:
                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        $ renpy.say(None, f"{subject.capitalize()} winces as you slide the tip in and out of her {adjective}{noun}, pushing against the substantial resistance.")
                    elif dice_roll == 2:
                        $ renpy.say(None, f"{subject.capitalize()}'s still way too tight, and you couldn't go any deeper even if you tried. She squeaks in pain every time your tip pushes inside.")
                    elif dice_roll == 3:
                        $ renpy.say(None, f"Your tip slides in and out of {owner} {adjective}{noun}, every motion causing her to wince.")
                elif temp_Characters[0].anal_training == 2:
                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        $ renpy.say(None, f"You slide the tip inside with relative ease as {subject}'s starting to get used to it, but she still winces.")
                    elif dice_roll == 2:
                        $ renpy.say(None, f"It seems like Psubject's starting to enjoy it as you hear the occasional moan when your cock presses inside her. Although, she winces more often than not.")
                    elif dice_roll == 3:
                        $ renpy.say(None, f"{subject.capitalize()} twitches as the tip of your cock slides inside her. You think she could take it deeper, but don't push it when she grimaces in pain.")
                elif temp_Characters[0].anal_training == 3:
                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        $ renpy.say(None, f"The tip of your cock slides in and out of {owner} {adjective}{noun} with ease, the occasional moan escaping from her mouth.")
                    elif dice_roll == 2:
                        $ renpy.say(None, f"{subject.capitalize()} pushes back against you as your cock slides inside her, as if she's trying to make you go deeper.")
                    elif dice_roll == 3:
                        $ renpy.say(None, f"{subject.capitalize()} shudders with every motion, and the tip of your cock smoothly glides in and out of her.")
            elif Action.mode == 2:
                if temp_Characters[0].anal_training == 1:
                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        $ renpy.say(None, f"{subject.capitalize()} winces as you slide the tip in and out of her {adjective}{noun}, pushing against the substantial resistance.")
                    elif dice_roll == 2:
                        $ renpy.say(None, f"{subject.capitalize()}'s still way too tight, and you couldn't go any deeper even if you tried. She squeaks in pain every time your tip pushes inside.")
                    elif dice_roll == 3:
                        $ renpy.say(None, f"Your tip slides in and out of {owner} {adjective}{noun}, every motion causing her to wince.")
                elif temp_Characters[0].anal_training == 2:
                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        $ renpy.say(None, f"You manage to push at least a couple inches inside {object}, but she winces, stopping you from going too deep yet.")
                    elif dice_roll == 2:
                        $ renpy.say(None, f"Your cock glides back and forth inside {owner} {adjective}{noun} as it involuntarily tightens around you, preventing you from going too deep.")
                    elif dice_roll == 3:
                        $ renpy.say(None, f"It seems like {subject}'s starting to feel more pleasure than pain, as your cock slides in deeper than before, eliciting a moan.")
                elif temp_Characters[0].anal_training == 3:
                    $ dice_roll = renpy.random.randint(1, 3)

                    if dice_roll == 1:
                        $ renpy.say(None, f"Your cock easily glides in and out of {owner} {adjective}{noun}, every motion causing her to shudder in ecstasy. Her hips push back against you as she tries to force you deeper inside.")
                    elif dice_roll == 2:
                        $ renpy.say(None, f"{subject.capitalize()} seems like she's really starting to enjoy this, as you can feel her {adjective}{noun} tighten around you. She's able to take you all the way in and moans with every motion.")
                    elif dice_roll == 3:
                        $ renpy.say(None, f"{owner.capitalize()} {adjective}{noun} quivers as your cock thrusts back and forth inside it. The deeper you go, the more she seems to enjoy it")

        $ temp_Characters.remove(temp_Characters[0])

    return

label vibrator_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.5:
            $ noun = "clit"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "pulsing "
            elif renpy.random.random() > 0.33 and temp_Characters[0].desire >= 75:
                $ adjective = "throbbing "
            else:
                $ adjective = ""
        else:
            $ noun = "pussy"

            if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
                $ adjective = "soaking wet "
            elif renpy.random.random() > 0.33:
                $ adjective = "glistening "
            else:
                $ adjective = ""

        $ dice_pool = [1, 2, 3]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(4)
            $ dice_pool.append(5)
            $ dice_pool.append(6)

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"You press the vibrator up against her clit causing {object} to moan as it makes contact.")
        elif dice_roll == 2:
            $ renpy.say(None, f"The vibrator makes its way across {owner} {adjective}{noun} causing her to shudder.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} is unable to suppress her moans, as the vibrator presses into her.")
        elif dice_roll == 4:
            $ renpy.say(None, f"{owner.capitalize()} legs quiver and she moans uncontrollably, as the vibrator brings her right up to the edge.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You notice {owner} twitches and shudders get more frequent as you press the vibrator into her with more pressure.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{owner.capitalize()} whole body starts to shudder as waves of pleasure radiate throughout her thanks to the vibrator.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label dildo_pussy_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66 and temp_Characters[0].desire >= 75:
            $ noun = "cunt"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "pussy"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "soaking wet "
        elif renpy.random.random() > 0.5:
            if temp_Characters[0].body_hair["pubic"] in ["bush", "hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "glistening "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(5)
            $ dice_pool.append(6)
            $ dice_pool.append(7)
            $ dice_pool.append(8)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("confused1", eyes = "left")
            else:
                $ temp_Characters[0].change_face("confused1", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} seems a little uncomfortable - maybe she'd appreciate being a little more warmed up?")
        elif dice_roll == 2:
            $ renpy.say(None, f"You steadily slide the dildo in and out of {owner} {adjective}{noun}.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} twitches as you guide the dildo into her {adjective}{noun}, holding it inside and grinding it around, before sliding it back out.")
        elif dice_roll == 4:
            $ renpy.say(None, f"The dildo doesn't quite seem to satisfy {object} as you slide it in and out. She undoubtedly wishes it was you inside her instead.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You steadily slide the dildo in and out of {owner} {adjective}{noun}, causing her to shudder with every motion.")
        elif dice_roll == 6:
            $ renpy.say(None, f"{subject.capitalize()} thrusts her hips towards you as the dildo slides in and out, every movement eliciting a moan.")
        elif dice_roll == 7:
            $ renpy.say(None, f"{subject.capitalize()} moans louder and louder as the dildo slides in and out of her dripping wet pussy.")
        elif dice_roll == 8:
            $ renpy.say(None, f"You pick up the pace, thrusting the dildo in and out of {owner} {adjective}{noun}, eliciting moans and involuntary shudders.")

        $ temp_Characters.remove(temp_Characters[0])

    return

label dildo_ass_continuations(Action):
    $ renpy.dynamic(temp_Characters = get_Action_Characters(Action))

    while temp_Characters:
        if renpy.random.random() > 0.5:
            $ subject = temp_Characters[0].name
            $ object = temp_Characters[0].name
            $ owner = temp_Characters[0].name + "'s"
        else:
            $ subject = "she"
            $ object = "her"
            $ owner = "her"

        if renpy.random.random() > 0.66:
            $ noun = "asshole"
        elif renpy.random.random() > 0.33:
            $ noun = "hole"
        else:
            $ noun = "ass"

        if renpy.random.random() > 0.75 and temp_Characters[0].desire >= 75:
            $ adjective = "hungry "
        elif renpy.random.random() > 0.7:
            if temp_Characters[0].body_hair["anus"] in ["hairy"]:
                $ adjective = "hairy "
            else:
                $ adjective = "smooth "
        elif renpy.random.random() > 0.25:
            $ adjective = "tight "
        else:
            $ adjective = ""

        $ dice_pool = [2, 3, 4]

        if temp_Characters[0].desire >= 75:
            $ dice_pool.append(5)
            $ dice_pool.append(6)
            $ dice_pool.append(7)
            $ dice_pool.append(8)

        if temp_Characters[0].desire < eval(f"{temp_Characters[0].tag}_Action_desire_thresholds['{Action.Action_type}']"):
            if renpy.random.random() > 0.5:
                $ temp_Characters[0].change_face("grimace", eyes = "left")
            else:
                $ temp_Characters[0].change_face("grimace", eyes = "right")

            $ dice_pool = [1]

        $ dice_roll = renpy.random.choice(dice_pool)

        if dice_roll == 1:
            $ renpy.say(None, f"{subject.capitalize()} tenses with every thrust of the dildo - she seems pretty uncomfortable.")
        elif dice_roll == 2:
            $ renpy.say(None, f"You steadily slide the dildo in and out of {owner} {adjective}{noun}, making sure not to go too deep.")
        elif dice_roll == 3:
            $ renpy.say(None, f"{subject.capitalize()} quivers as you guide the dildo into her {adjective}{noun}, holding it inside and grinding it around, before pulling it back out.")
        elif dice_roll == 4:
            $ renpy.say(None, f"The dildo doesn't quite seem to satisfy {object} as you slide it in and out. She undoubtedly wishes it was you inside her instead.")
        elif dice_roll == 5:
            $ renpy.say(None, f"You pick up the pace, thrusting the dildo in and out of {owner} {adjective}{noun}, eliciting moans and involuntary shudders.")
        elif dice_roll == 6:
            $ renpy.say(None, f"You steadily slide the dildo in and out of {owner} {adjective}{noun} even faster. She moans with every motion as her ass quivers around it.")
        elif dice_roll == 7:
            $ renpy.say(None, f"{subject.capitalize()} thrusts her hips towards you as the dildo slides in and out, every movement eliciting a moan.")
        elif dice_roll == 8:
            $ renpy.say(None, f"{subject.capitalize()} moans louder and louder as the dildo slides in and out of her {adjective}{noun}, her entire body shuddering.")

        $ temp_Characters.remove(temp_Characters[0])

    return