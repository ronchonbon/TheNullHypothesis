label Rogue_flirt_a:
    $ lines = {
        "a": "You have great taste in music, any recommendations?",
        "b": "You look {i}great{/i} today, as always.",
        "c": "Love the outfit.",
        "d": "Those bottoms make your ass look fantastic.",
        "e": "Do you squat a lot? Because holy shit. . .",
        "f": "You have beautiful eyes, you know that?",
        "g": "Have you been working out more than usual? Everything seems tighter. . . in a good way.",
        "h": "I love your accent by the way.",
        "j": "I love studying with you, you make everything so easy to understand.",
        "k": "You always smell so good.",
        "m": "I saw you in the Danger Room earlier - you looked awesome.",
        "n": "I love your smile - makes me happy whenever I see it.",
        "o": "I've seen you training on your own in the Danger Room. You really are a badass, even without flashy powers."}

    if Rogue.check_traits("quirk"):
        $ lines.update({"i": "You've been a very good girl lately."})

    if not Rogue.History.check("asked_if_hair_dyed"):
        $ lines.update({"l": "I really like your hair, do you dye it?"})

    if Player.scholarship == "athletic":
        $ lines.update({"p": "You're in fantastic shape, you know that? It's really impressive - both aesthetically and what you're capable of. . . (athletic)"})
    elif Player.scholarship == "academic":
        $ lines.update({"r": "Has studying always come so easily to you? And I thought I was smart. . . (academic)"})
    elif Player.scholarship == "artistic":
        $ lines.update({"q": "I absolutely love your aesthetic, your style, your music taste. . . pretty much everything. (artistic)"})

    $ indices = list(lines.keys())

    $ renpy.random.shuffle(indices)

    $ first_compliment = lines[indices[0]]
    $ second_compliment = lines[indices[1]]
    $ third_compliment = lines[indices[2]]

    menu:
        "[first_compliment]":
            $ flirting_type = "a" + indices[0]
        "[second_compliment]":
            $ flirting_type = "a" + indices[1]
        "[third_compliment]":
            $ flirting_type = "a" + indices[2]
        "Back":
            return

    call expression f"Rogue_flirt_{flirting_type}"

    return

label Rogue_flirt_aa:
    if Player.scholarship == "artistic":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased1", blush = 1)

        ch_Rogue "Thanks."

        $ Rogue.change_face("smirk2")
        
        ch_Rogue "Ah could make a playlist for ya, if ya want."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("worried1", blush = 1) 

        ch_Rogue "Maybe we could listen together. . . at some point."
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2", blush = 1)

        ch_Rogue "Ya really think so?" 

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1) 

        ch_Rogue "You've got good taste yerself. . ." 

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Rogue "But, ah can try to make a playlist just for ya."

    return

label Rogue_flirt_ab:
    if Rogue.status["horny"] or Rogue.status["nympho"]:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", blush = 1)

        pause 1.0

        $ Rogue.change_face("worried1", blush = 1) 

        ch_Rogue "Ya really think so?" 

        $ Rogue.change_face("smirk2") 

        ch_Rogue "Thanks. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased2", blush = 1) 

        ch_Rogue "Well, thanks. . ." 

        $ Rogue.change_face("smirk2", eyes = "down")
    elif dice_roll == 3:
        $ Rogue.change_face("sly", eyes = "down")

        pause 1.0

        $ Rogue.change_face("sly", blush = 1) 

        ch_Rogue "Yer lookin' pretty good yourself. . ." 

        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

    return

label Rogue_flirt_ac:
    if Rogue.Outfit.Outfit_type == "custom":
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased1", blush = 1)

        ch_Rogue "Thanks, [Rogue.Player_petname]." 

        $ Rogue.change_face("pleased1", eyes = "down", blush = 1) 

        ch_Rogue "Ah like it too. . ." 

        $ Rogue.change_face("smirk2", blush = 1)
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2", blush = 1)

        ch_Rogue "Really?" 

        $ Rogue.change_face("smirk2", eyes = "down") 

        ch_Rogue "It is nice, ain't it?" 

        $ Rogue.change_face("smirk2")
    elif dice_roll == 3:
        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Rogue "Well ah'd hope ya like it. . ." 

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Rogue "You picked this one out for me."
    elif dice_roll == 4:
        $ Rogue.change_face("pleased1", blush = 1) 

        ch_Rogue "Ya really like the way this one looks, huh?" 

        $ Rogue.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1) 

        ch_Rogue "Ah do too. . ." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Thanks for pickin' it out for me."

    return

label Rogue_flirt_ad:
    if approval_check(Rogue, threshold = Rogue_thresholds["flirting_ad"]):
        if Rogue.status["horny"] or Rogue.status["nympho"]:
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("worried3", blush = 1) 

            ch_Rogue "Ya don't think. . ." 

            $ Rogue.change_face("worried1", eyes = "down", blush = 1)

            ch_Rogue "They make it look too. . . big?" 

            $ Rogue.change_face("worried1", blush = 1)
        elif dice_roll == 2:
            $ Rogue.change_face("sexy", blush = 1) 

            ch_Rogue "Ah know ya like it. . ." 

            $ Rogue.change_face("sexy", eyes = "down", blush = 1)

            ch_Rogue "Maybe ah could let ya touch it later. . ." 

            $ Rogue.change_face("sexy", blush = 1)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("perplexed")

            pause 1.0

            $ Rogue.change_face("angry1") 

            ch_Rogue "Keep yer eyes off my ass."
        elif dice_roll == 2:
            $ Rogue.change_face("perplexed")

            pause 1.0

            $ Rogue.change_face("appalled1") 

            ch_Rogue "What in tarnation possessed ya to say that?!"

    return

label Rogue_flirt_ae:
    if approval_check(Rogue, threshold = Rogue_thresholds["flirting_ae"]):
        if Rogue.status["horny"] or Rogue.status["nympho"]:
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("confused2", blush = 1) 

            ch_Rogue "Ah mean. . ." 

            $ Rogue.change_face("pleased1", eyes = "down", blush = 1) 

            ch_Rogue "Not more than anybody else. . ." 

            $ Rogue.change_face("smirk2", blush = 1)
        elif dice_roll == 2:
            $ Rogue.change_face("sly", blush = 1) 

            ch_Rogue "Ah know you think my ass looks good. . ." 

            $ Rogue.change_face("sexy", blush = 1) 

            ch_Rogue "Maybe ah'll show ya later. . ."
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("confused1")

            ch_Rogue "Ah wouldn't say 'a lot.'" 

            $ Rogue.change_face("confused1", eyes = "down") 

            ch_Rogue "Why, somethin' wrong?"

            $ Rogue.change_face("worried1")
        elif dice_roll == 2:
            $ Rogue.change_face("perplexed") 

            ch_Rogue "The hell?" 

            $ Rogue.change_face("confused1")

            ch_Rogue "Are ya talkin' 'bout my. . . ?" 

            $ Rogue.change_face("angry1")

    return

label Rogue_flirt_af:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Thanks. . ." 

        $ Rogue.change_face("smirk2", blush = 2)

        ch_Rogue "Ah like yours too. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Look into 'em whenever ya want. . ."

    return

label Rogue_flirt_ag:
    if approval_check(Rogue, threshold = Rogue_thresholds["flirting_ag"]):
        if Player.scholarship == "athletic":
            $ dice_roll = renpy.random.randint(1, 2)
        else:
            $ dice_roll = renpy.random.randint(1, 1)

        if dice_roll == 1:
            $ Rogue.change_face("confused3")

            pause 1.0

            $ Rogue.change_face("appalled2", blush = 1) 

            ch_Rogue "That's. . . well. . ." 

            $ Rogue.change_face("worried1", blush = 1) 

            ch_Rogue "Ya really think ah look better?" 
        elif dice_roll == 2:
            $ Rogue.change_face("surprised2")

            pause 1.0

            $ Rogue.change_face("pleased2", blush = 1) 

            ch_Rogue "Ah have been. . ." 

            $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

            ch_Rogue "After seein' how. . . fit you look." 

            $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

            pause 1.0

            $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

            ch_Rogue "Ah've been more motivated. . ." 
    else:
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("perplexed") 

            ch_Rogue "What on god's green earth possessed ya to say somethin' like that?" 

            $ Rogue.change_face("appalled1")
        elif dice_roll == 2:
            $ Rogue.change_face("appalled2") 

            ch_Rogue "Why are ya so damn focused on how 'tight' ah am?" 

            $ Rogue.change_face("angry1")

    return

label Rogue_flirt_ah:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", blush = 1) 

        ch_Rogue "Really?" 

        $ Rogue.change_face("smirk2") 

        ch_Rogue "Ah'm glad. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Sometimes ah forget 'bout how ah might sound." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Glad ya like it. . ."

    return

label Rogue_flirt_ai:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Rogue.change_face("worried2")

        pause 1.0

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1) 

        ch_Rogue "Thanks, [Rogue.Player_petname]. . ." 
        ch_Rogue "Ah've been tryin'." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)
    elif dice_roll == 2:
        $ Rogue.change_face("worried3")

        pause 1.0

        $ Rogue.change_face("worried2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Really?" 

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ya don't have to say it if ya don't mean it. . ."
    elif dice_roll == 3:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah'm glad ya think so." 

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)  

        ch_Rogue "Anythin' for you. . ."
    elif dice_roll == 4:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "If ya ever think ah'm not. . ." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Discipline me." 
        ch_Rogue "Please." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    return

label Rogue_flirt_aj:
    if Player.scholarship == "academic":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", blush = 1) 

        ch_Rogue "Ya really think so?" 

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Ah do try. . ." 
        ch_Rogue "Thanks, [Rogue.Player_petname]."
    elif dice_roll == 2:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1) 

        ch_Rogue "Ah really like studyin' with you as well. . ." 

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Yer a great student."
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Ah'm glad ya think so. . ." 
        ch_Rogue "But yer a big part of it." 
        ch_Rogue "Not hard to teach someone as smart as you. . ."

    return

label Rogue_flirt_ak:
    if approval_check(Rogue, threshold = Rogue_thresholds["flirting_ak"]):
        $ dice_roll = renpy.random.randint(1, 2)

        if dice_roll == 1:
            $ Rogue.change_face("surprised2")

            $ Rogue.change_face("worried1", blush = 1) 

            ch_Rogue "Ah. . . think you smell nice too. . ." 

            $ Rogue.change_face("worried1", eyes =  "down", mouth = "smirk", blush = 1)
        elif dice_roll == 2:
            $ Rogue.change_face("worried2", blush = 1) 

            ch_Rogue "Ah have been tryin' this new shampoo. . ." 

            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

            ch_Rogue "Glad ya like it."
    else:
        $ Rogue.change_face("perplexed") 

        ch_Rogue "Ah reckon you shouldn't be worryin' 'bout how ah smell. . ." 

        $ Rogue.change_face("confused1")

    return

label Rogue_flirt_al:
    $ Rogue.change_face("pleased2") 

    ch_Rogue "Ya really like it?" 

    $ Rogue.change_face("smirk2", blush = 1) 

    ch_Rogue "Ah don't dye it, was born like this. . ."

    $ Rogue.History.update("asked_if_hair_dyed")

    return

label Rogue_flirt_am:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", blush = 1) 

        ch_Rogue "Really?" 

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "You were watchin'?" 
        ch_Rogue "Thanks. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Ah've felt more motivated to train, ever since ya got here. . ." 

        $ Rogue.change_face("smirk2", blush = 2) 

        ch_Rogue "Glad ya think ah look good."
    elif dice_roll == 3:
        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Thanks sugar. . ." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah've seen ya train, yer also makin' some real good progress." 
        ch_Rogue "Look good doin' it too. . ." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 2)

    return

label Rogue_flirt_an:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah'll try to smile more, just for you. . ."
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1)

        ch_Rogue "Well ain't you sweet as pie. . ." 
        ch_Rogue "Thanks. . ." 

        $ Rogue.change_face("smirk2", blush = 2) 
    elif dice_roll == 3:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Thanks, that's real sweet. . ." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

        ch_Rogue "Ah like yer smile too. . ."

    return

label Rogue_flirt_ao:
    if Player.scholarship == "athletic":
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "Ah really 'preciate that, been trainin' real hard lately. . ." 
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Thanks, [Rogue.Player_petname]. . ." 
        ch_Rogue "But look who's talkin'." 

        $ Rogue.change_face("smirk2", eyes = "down", blush = 1)

        pause 1.0

        $ Rogue.change_face("smirk2", blush = 1) 

        ch_Rogue "Yer a natural at all 'o this."

    return

label Rogue_flirt_ap:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("worried1", blush = 1) 

    ch_Rogue "Ah never really thought ah was that good. . ." 
    ch_Rogue "Yer not jokin' 'round, right?" 
    ch_Player "Of course not." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

    ch_Rogue "Thanks. . ." 

    $ Rogue.change_face("worried1", eyes = "down", mouth = "smirk", blush = 1)

    ch_Rogue "Yer. . . impressive too." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    return

label Rogue_flirt_aq:
    $ Rogue.change_face("surprised2")

    pause 1.0

    $ Rogue.change_face("pleased2", blush = 1) 

    ch_Rogue "Ah really 'preciate that. . ." 

    $ Rogue.change_face("smirk2", blush = 1) 

    ch_Rogue "Most people are makin' assumptions 'bout my appearance and everythin'." 
    ch_Rogue "But ah know you actually care."

    return

label Rogue_flirt_ar:
    $ Rogue.change_face("pleased2")

    pause 1.0

    $ Rogue.change_face("smirk1", blush = 1) 

    ch_Rogue "Not really, if ah'm honest." 
    ch_Rogue "Ah wouldn't say it comes easy, ah try pretty hard. . ." 

    $ Rogue.change_face("worried1", blush = 1) 

    ch_Rogue "And ah reckon yer way smarter than me." 
    ch_Rogue "You absorb everythin' ah teach ya like a sponge."

    return

label Rogue_flirt_b:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Player "Are you from Tennessee? Because you're the only ten I see."

        $ Rogue.change_face("confused1", mouth = "smirk") 

        ch_Rogue "No. . . Mississippi. . ."
    elif dice_roll == 2:
        ch_Player "Are you from Georgia? Because your peach is gigan. . . wait that's not it. . ." 

        $ Rogue.change_face("perplexed") 

        ch_Rogue "Haven't ah told ya ah'm from Mississippi?"

        $ Rogue.change_face("confused1")
    elif dice_roll == 3:
        ch_Player "You lost? Heaven is a long ways away." 

        $ Rogue.change_face("confused1", mouth = "smirk") 

        ch_Rogue "Really, darlin'?"
    elif dice_roll == 4:
        ch_Player "If you were a biscuit, you wouldn't need any gravy, because you're perfect as it is." 

        $ Rogue.change_face("confused1", mouth = "smirk") 

        ch_Rogue "Heh, at least yer creative. . ."

    return

label Rogue_flirt_c:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Rogue.change_face("pleased2", blush = 1) 

        ch_Rogue "Hey there. . ." 

        $ Rogue.change_face("smirk2", blush = 1)
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

        ch_Rogue ". . . Howdy." 

        $ Rogue.change_face("worried1", blush = 1) 

        ch_Rogue "Did ya need somethin'?" 
        ch_Player "No, just thought your eyes looked really pretty." 

        $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1) 

        ch_Rogue "{size=-5}Thanks{/size}. . ." 

        $ Rogue.change_face("smirk2", eyes = "right", blush = 1)

    return

label Rogue_flirt_d:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Rogue "Sure." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        "You gently grasp her hand."
    elif dice_roll == 2:
        ch_Rogue "Yes please." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        "She reaches out and takes your hand, interlacing her fingers with yours."
    elif dice_roll == 3:
        ch_Rogue "Was hopin' you'd wanna. . ." 

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        "You take her hand in yours and give it a light squeeze."

    return

label Rogue_flirt_ea:
    "She gives you a quick peck."
    ch_Rogue "Sure."

    $ Rogue.change_face("smirk2")

    return

label Rogue_flirt_eb:
    if Player.location in public_locations and approval_check(Rogue, threshold = [75, 75]):
        $ Rogue.change_face("worried1", eyes = "left", blush = 1) 

        ch_Rogue "Alright, a real quick one. . ."

        $ Rogue.change_face("kiss1", blush = 1) 

        "You briefly lock lips before she pulls away."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah hope there's more later. . ."

        $ Rogue.change_face("worried1", blush = 1)
    elif Player.location in public_locations:
        $ Rogue.change_face("worried1", eyes = "right", blush = 1) 

        ch_Rogue "Ah dunno. . . people are lookin'."
        ch_Rogue "Maybe later. . ."

        $ Rogue.change_face("worried1", blush = 1)
    elif Rogue.check_traits("quirk"):
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah wouldn't mind if ya. . . just took it upon yourself some time. . ."

        $ Rogue.change_face("kiss2", blush = 2)  

        "After a passionate moment, she pulls away."

        $ Rogue.change_face("sexy", blush = 2) 

        ch_Rogue "Ah am yours. . . after all."
    else:
        $ Rogue.change_face("pleased2", mouth = "lipbite", blush = 1) 

        ch_Rogue "Gladly. . ."

        $ Rogue.change_face("kiss2", blush = 1) 

        "As your lips touch, she holds on to you for dear life."

        $ Rogue.change_face("worried1", blush = 2)

        ch_Rogue "Sorry. . . got a bit carried away. . ."

    return

label Rogue_flirt_f:
    if Player.location in public_locations and approval_check(Rogue, threshold = [50, 50]):
        $ Rogue.change_face("worried1") 

        ch_Rogue "Ah'd never say no to another hug from you. . ."

        $ Rogue.change_face("worried1", eyes = "closed") 

        "You pull her into your arms and hold her briefly before letting go."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

        ch_Rogue "You. . . smell nice. . ."
    elif Player.location in public_locations:
        $ Rogue.change_face("worried1", eyes = "right") 

        pause 1.0

        $ Rogue.change_face("worried1") 

        ch_Rogue "Ah wouldn't mind. . ."
        ch_Rogue "But. . . maybe later, when there's not so many people 'round."
    elif approval_check(Rogue, threshold = [50, 50]):
        $ Rogue.change_face("pleased2", blush = 1) 

        ch_Rogue "Yes!"

        $ Rogue.change_face("pleased2", eyes = "closed", blush = 1) 

        "Without another word, she jumps into your arms."
        "Pressing her head into your chest, she squeezes you tightly."
        "After a moment, she lets go."

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "Could ya. . . hug me more often?"
    else:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Ah'd very much like to. . ."

        $ Rogue.change_face("worried1", eyes = "closed", blush = 1) 

        "She wraps her arms around you and squeezes gently."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Thank you. . ."
        ch_Rogue "You can imagine ah don't get to do that too often. . ."

    return

label Rogue_flirt_g:
    $ Rogue.change_face("confused1", mouth = "smirk") 

    ch_Rogue "Ah wouldn't mind a shoulder rub. . ."

    $ Rogue.change_face("smirk2", eyes = "closed") 

    "You get to work, and it seems like you do a pretty good job as she almost moans in pleasure."

    $ Rogue.change_face("worried1", blush = 1) 

    ch_Rogue "That was. . . great, thanks, [Rogue.Player_petname]."

    return

label Rogue_flirt_h:
    if approval_check(Rogue, threshold = [175, 175]):
        $ Rogue.change_face("pleased2", blush = 1)

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 1) 

        "You run your hand through [Rogue.name]'s hair, and she leans her head against it."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah. . . really like when you do that. . ."
    else:
        $ Rogue.change_face("surprised2", blush = 1) 

        "You run your hand through [Rogue.name]'s hair, feeling how soft it is."

        $ Rogue.change_face("worried1", eyes = "closed", blush = 1)

        "She shudders slightly."

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "Why. . ."

        $ Rogue.change_face("worried2", blush = 1) 

        ch_Rogue "Not that ah mind. . ."

    return

label Rogue_flirt_i:
    if Player.location in public_locations and approval_check(Rogue, threshold = [125, 125]):
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased1", blush = 1) 

        "As you wrap your arm around [Rogue.name], she smiles and leans into you."

        $ Rogue.change_face("smirk2", eyes = "closed", blush = 1) 

        ch_Rogue "Ah like it when you hold me. . ."
        "After another moment, she pulls away."

        $ Rogue.change_face("smirk2", blush = 1)
    elif Player.location in public_locations:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("worried2", eyes = "right")

        pause 1.0

        $ Rogue.change_face("worried2", blush = 1) 

        "As you wrap your arm around [Rogue.name], she stiffens slightly."

        $ Rogue.change_face("worried1", blush = 1) 

        ch_Rogue "Ah don't usually mind. . . if it's you. . ."
        "She pulls away."
        ch_Rogue "But maybe not 'round so many people. . ."
    elif approval_check(Rogue, threshold = [125, 125]):
        $ Rogue.change_face("pleased1", blush = 1) 

        "As you wrap your arm around [Rogue.name], she turns and hugs you."

        $ Rogue.change_face("smirk2", eyes = "closed", blush = 1) 

        "After a moment she pulls you into a kiss."

        $ Rogue.change_face("kiss2", blush = 2) 

        "She squeezes you tightly, and her breath starts running ragged."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah couldn't help it. . ."
    else:
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("pleased1", blush = 1) 

        "As you wrap your arm around [Rogue.name], she leans her head on your shoulder."

        $ Rogue.change_face("smirk2", eyes = "closed", blush = 1)

        "After a moment she pulls away."

        $ Rogue.change_face("smirk2", blush = 1)

    return

label Rogue_flirt_ja:

    return

label Rogue_flirt_jb:

    return

label Rogue_flirt_jc:

    return

label Rogue_flirt_jd:

    return

label Rogue_flirt_ka:

    return

label Rogue_flirt_kb:

    return

label Rogue_flirt_l:
    show expression "images/effects/smack.webp" as smack onlayer effects:
        anchor (0.5, 0.5) pos (Rogue.sprite_position[0], 0.7)

        zoom 0.0
        alpha 0.0
        ease 0.1 zoom 1.0 alpha 1.0
        ease 1.0 alpha 0.0

    with small_screenshake

    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Rogue.change_face("surprised2") 

        "As you smack her glorious ass, she lets out a small yelp."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Have ah been a bad girl?"

        $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)
    elif dice_roll == 2:
        $ Rogue.change_face("pleased2")

        "As you smack her ass, she moans slightly."

        $ Rogue.change_face("sexy", blush = 1) 

        ch_Rogue "Havin' fun?"
        ch_Rogue "Maybe. . . harder next time?"

        $ Rogue.change_face("sexy", eyes = "down", blush = 2) 
    elif dice_roll == 3:
        $ Rogue.change_face("worried3") 

        "As you smack her ass, she lets out a gasp."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

        ch_Rogue "Ah like when you do that. . ."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    return

label Rogue_flirt_ma:

    return

label Rogue_flirt_mb:

    return

label Rogue_flirt_mc:

    return

label Rogue_flirt_na:

    return

label Rogue_flirt_nb:

    return

label Rogue_flirt_nc:

    return

label Rogue_flirt_oa:
    "You walk up to her and give her a quick kiss on the cheek."

    $ Rogue.change_face("pleased2")

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

    ch_Rogue "Ah wouldn't mind a real kiss. . ."

    return

label Rogue_flirt_ob:
    "You walk up to her, put a hand behind her neck, and pull her into a deep kiss."

    $ Rogue.change_face("kiss1", brows = "raised", blush = 1) 

    "You hold her tight for another second, before letting go."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

    ch_Rogue "What did ah do to deserve that?"

    $ Rogue.change_face("worried1", blush = 1) 

    ch_Rogue "Not that ah'm complainin'."

    return

label Rogue_flirt_pa:

    return

label Rogue_flirt_pb:

    return

label Rogue_flirt_pc:

    return

label Rogue_flirt_pd:

    return

label Rogue_flirt_qa:
    $ Rogue.change_face("worried2", blush = 1)

    ch_Rogue "Ah have? Ah'm sorry. . ." 

    $ Rogue.change_face("worried1", blush = 1) 

    ch_Rogue "Ah'll be better." 
    ch_Rogue "Just tell me what you want." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Maybe you want to. . . punish me?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

    return

label Rogue_flirt_qb:
    $ Rogue.change_face("worried3", blush = 1)

    ch_Rogue "Ah will, [Rogue.Player_petname], ah promise." 

    $ Rogue.change_face("worried1", eyes = "down", blush = 1) 

    ch_Rogue "You know yer always my top priority. . ." 

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

    ch_Rogue "Ah'm yours to use however ya want."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    return

label Rogue_flirt_qc:
    $ Rogue.change_face("worried3", blush = 1)

    ch_Rogue "Ah'm sorry!" 

    $ Rogue.change_face("worried1", blush = 1) 

    ch_Rogue "Ah'll try harder, ah swear." 

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1) 

    ch_Rogue "Please don't ignore me. . ." 
    ch_Rogue "Ah deserve to be punished."

    return

label Rogue_flirt_r:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Rogue.change_face("worried2", mouth = "smirk", blush = 1)

        ch_Player "Just wanted to say I love you."

        $ Rogue.change_face("worried1", eyes = "closed", mouth = "smirk", blush = 1)

        "She just pulls you into a warm hug."
        ch_Rogue "You. . ."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Have no idea how happy it makes me to hear ya say that."
        ch_Rogue "I love you too."
    elif dice_roll == 2:
        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Player "I love you, by the way."
        ch_Rogue "Ah love you too. . ."

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "Ah love you so much."
    elif dice_roll == 3:
        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Player "Just wanted to say I love you."
        ch_Rogue "Ah love you too."

        $ Rogue.change_face("worried1", blush = 1)

        ch_Rogue "And ah love when you say it. . ."
    elif dice_roll == 4:
        $ Rogue.change_face("worried3", blush = 1)

        ch_Player "I lov-"
        "Before you can finish. . ."
        ch_Rogue "Ahloveyou!"

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Sorry, ah just had to get that out. . ."
        ch_Player "Heh, I love you too."

    return