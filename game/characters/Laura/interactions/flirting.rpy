label Laura_flirt_a:
    $ lines = {
        "b": "You look adorably deadly today.",
        "d": "Your abs make me feel things. . . good things.",
        "e": "Do you do legs a lot? Because holy shit. . . I wouldn't mind suffocating between those thighs.",
        "f": "Even your gaze feels like it'd cut me. . .",
        "g": "How much do you workout? You're crazy fit.",
        "h": "I don't have to tell you how cool your claws are.",
        "k": "You never wear perfume, but you still always smell nice. . .",
        "l": "Your hair is so sleek, I really like it.",
        "m": "Watching you train in the Danger Room is awe-inspiring. Just an incredible combination of grace and deadliness.",
        "n": "You have a really nice smile, I love when it comes out.",
        "o": "I don't think there's anyone on the planet who could beat you in a hand-to-hand fight."}

    if Player.location == Laura.location:
        $ lines.update({"c": "You look great in that outfit."})

    if EventScheduler.Events["Laura_first_friend_part_three"].completed:
        $ lines.update({"a": "I've noticed you listening to some pretty interesting music, I like your taste."})

    if Laura.quirk:
        $ lines.update({"i": "I love whenever you use me to. . . satisfy yourself."})

    if Laura.History.check("studied_with_Player"):
        $ lines.update({"j": "Y'know, I do actually enjoy tutoring you. You're a great student."})

    if Player.scholarship == "athletic":
        $ lines.update({"p": "I've genuinely never seen someone as physically capable as you. (athletic)"})
    elif Player.scholarship == "academic":
        $ lines.update({"r": "I know you despise studying, but you're really good at it. . . whenever you put in the effort. (academic)"})
    elif Player.scholarship == "artistic":
        $ lines.update({"q": "I really appreciate your style. You're just effortlessly cool. (artistic)"})

    $ indices = list(lines.keys())

    $ renpy.random.shuffle(indices)

    $ first_compliment = lines[indices[0]]
    $ second_compliment = lines[indices[1]]
    $ third_compliment = lines[indices[2]]

    menu:
        "[first_compliment]":
            call expression f"Laura_flirt_a{indices[0]}" from _call_expression_18
        "[second_compliment]":
            call expression f"Laura_flirt_a{indices[1]}" from _call_expression_19
        "[third_compliment]":
            call expression f"Laura_flirt_a{indices[2]}" from _call_expression_20
        "Back":
            return

    return

label Laura_flirt_aa:
    if Player.scholarship == "artistic":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("surprised1", blush = 1)

        ch_Laura "You enjoy those songs as well?"

        $ Laura.change_face("smirk2")
        
        ch_Laura "I like the way they increase my heart rate."
        ch_Laura "Makes training more interesting."

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_469
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        pause 1.0

        $ Laura.change_face("neutral", blush = 1) 

        ch_Laura "Rogue introduced me to that music."

        $ Laura.change_face("neutral", eyes = "squint", blush = 1)

        ch_Laura "You should show me your favorites as well."

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_470
    elif dice_roll == 3:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "My taste?" 

        $ Laura.change_face("neutral", eyes = "left", blush = 1) 

        ch_Laura "Rogue is the one who got me to start listening. . ." 

        $ Laura.change_face("suspicious1", blush = 1)

        ch_Laura "Don't you also have a significant interest in music?"
        ch_Laura "Why haven't you shown me your favorites as well?"

        $ Laura.change_face("neutral", eyes = "squint", blush = 1)

        ch_Laura "You will."

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_471

    return

label Laura_flirt_ab:
    if Laura.status["horny"] or Laura.status["nympho"]:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("confused2", blush = 1)

        pause 1.0

        $ Laura.change_face("suspicious1", blush = 1) 

        ch_Laura "'Adorably'?" 

        $ Laura.change_face("neutral", eyes = "left", blush = 1) 

        ch_Laura "I just look deadly. . . in a cool way. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_472
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 1.0

        $ Laura.change_face("confused1", eyes = "down", blush = 1) 

        ch_Laura "I don't look adorable. . ." 

        $ Laura.change_face("confused1", eyes = "squint")

        ch_Laura "At least you're right about the second part. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_473
    elif dice_roll == 3:
        $ Laura.change_face("sexy", eyes = "down")

        pause 1.0

        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "Deadly, huh?"
        ch_Laura "Like a predator?" 

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "You look like the prey. . ." 

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_474
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_475

    return

label Laura_flirt_ac:
    if Laura.Outfit.Outfit_type == "custom":
        $ dice_roll = renpy.random.randint(1, 4)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("confused1", eyes = "down", blush = 1)

        ch_Laura "I do?" 

        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "It's just my normal clothes. . ." 

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "But. . . thanks."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_476
    elif dice_roll == 2:
        $ Laura.change_face("pleased1", blush = 1)

        ch_Laura "You like it too?" 

        $ Laura.change_face("smirk2", eyes = "down") 

        ch_Laura "I like functional stuff. . ." 

        $ Laura.change_face("smirk2")

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_477
    elif dice_roll == 3:
        $ Laura.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Laura "You better like it. . ." 

        $ Laura.change_face("smirk2", eyes = "down", blush = 1)

        ch_Laura "It's your fault I'm wearing it in the first place." 

        $ Laura.change_face("smirk2", blush = 1)

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_478
    elif dice_roll == 4:
        $ Laura.change_face("pleased1", blush = 1) 

        ch_Laura "To be honest. . . I don't mind it." 

        $ Laura.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1) 

        ch_Laura "I've let you talk me into worse outfits before." 

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "You're lucky I let you." 

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_479

    return

label Laura_flirt_ad:
    $ start = 1
    $ finish = 1

    if not approval_check(Laura, threshold = [125, 150]):
        $ start = 3
        $ finish = 4
    elif Laura.status["horny"] or Laura.status["nympho"]:
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "They make you 'feel things'?" 

        $ Laura.change_face("confused1", eyes = "down", blush = 1)

        ch_Laura "Interesting. . ." 

        $ Laura.change_face("smirk2", eyes = "squint", blush = 1)

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_480
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "My abs?" 

        $ Laura.change_face("sexy", eyes = "down", blush = 1)

        ch_Laura "You do seem to have a hard time keeping your eyes off of them. . ." 

        $ Laura.change_face("sexy", blush = 1)

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_481
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_482
    elif dice_roll == 3:
        $ Laura.change_face("appalled1")

        pause 1.0

        $ Laura.change_face("angry1")

        call Laura_unsheathes_claws from _call_Laura_unsheathes_claws_4

        ch_Laura "I'll make you feel something sharp if you don't keep your eyes off me." 

        call Laura_sheathes_claws from _call_Laura_sheathes_claws_4

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_483
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_484
    elif dice_roll == 4:
        $ Laura.change_face("perplexed")

        pause 1.0

        $ Laura.change_face("appalled1") 

        ch_Laura "{i}Grrrrrr{/i}"
        ch_Laura "Eyes off me."

        $ Laura.change_face("angry1")

        ch_Laura "Or else."

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_485
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_486

    return

label Laura_flirt_ae:
    $ start = 1
    $ finish = 1

    if not approval_check(Laura, threshold = [125, 150]):
        $ start = 3
        $ finish = 4
    elif Laura.status["horny"] or Laura.status["nympho"]:
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Laura.change_face("pleased1", blush = 1) 

        ch_Laura "I do. . ."

        $ Laura.change_face("pleased1", eyes = "down", blush = 1) 

        ch_Laura "You like them that much?"

        $ Laura.change_face("smirk2", blush = 1)

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1329
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1330
    elif dice_roll == 2:
        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "I work out everything, a lot."

        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "You should know that. . . constantly staring at my muscles. . ."
        ch_Laura "I find myself staring at yours a lot too. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1331
        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1332
    elif dice_roll == 3:
        $ Laura.change_face("appalled1")

        pause 0.5

        $ Laura.change_face("angry1", eyes = "down") 

        pause 0.5

        $ Laura.change_face("angry1")

        ch_Laura "Is something wrong with you?"

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_1333
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_1334
    elif dice_roll == 4:
        $ Laura.change_face("appalled1") 

        ch_Laura "Don't concern yourself with my legs."

        $ Laura.change_face("angry1")

        ch_Laura "Otherwise, you might get kicked."

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_1335
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_1336

    return

label Laura_flirt_af:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("surprised1")

        pause 0.5

        $ Laura.change_face("smirk2", blush = 1) 

        ch_Laura "Thanks. . ."

        $ Laura.change_face("smirk2", eyes = "squint", blush =2)

        ch_Laura "It could if you stare too long. . ."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1337 
    elif dice_roll == 2:
        $ Laura.change_face("confused1")

        pause 0.5

        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "Is that a good thing?"

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "Knowing you. . . you probably like that. . ."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1338

    return

label Laura_flirt_ag:
    $ start = 1
    $ finish = 1

    if not approval_check(Laura, threshold = [125, 150]):
        $ start = 3
        $ finish = 4
    elif Player.scholarship == "athletic":
        $ finish = 2

    $ dice_roll = renpy.random.randint(start, finish)

    if dice_roll == 1:
        $ Laura.change_face("confused1")

        pause 0.5

        $ Laura.change_face("suspicious1", blush = 1) 

        ch_Laura "I work out more than anyone at this school."

        $ Laura.change_face("neutral", eyes = "left", blush = 1) 

        ch_Laura "You. . . think I look good?"

        $ Laura.change_face("smirk1", blush = 1)

        ch_Laura "My metabolism doesn't let me be anything but lean."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1339
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "You know I train a lot."

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "And I know you like to stare. . ."

        $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        pause 0.5

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "I like to stare at you as well. . ."
        ch_Laura "You're also very fit."

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1340
    elif dice_roll == 3:
        $ Laura.change_face("appalled1") 

        ch_Laura "I work out more in one day than you ever have. . ."

        $ Laura.change_face("angry1")

        ch_Laura "Stop worrying about how lean I am."

        $ Laura.change_face("suspicious1")

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_1341
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_1342
    elif dice_roll == 4:
        $ Laura.change_face("appalled2") 

        ch_Laura "Eyes off."

        $ Laura.change_face("angry1")

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_1343
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_1344

    return

label Laura_flirt_ah:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("pleased1", blush = 1) 

        ch_Laura "I know. . ."

        call Laura_unsheathes_claws from _call_Laura_unsheathes_claws_7

        $ Laura.change_face("smirk2") 

        ch_Laura "I also have claws in my feet."

        call Laura_sheathes_claws from _call_Laura_sheathes_claws_7

        ch_Laura "Good for kicking."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1345
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "People are usually scared by them."

        $ Laura.change_face("smirk2", eyes = "left", blush = 1) 

        ch_Laura "I think they're cool too. . ."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1346

    return

label Laura_flirt_ai:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Laura.change_face("pleased2")

        pause 0.5

        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "I can't control myself around you. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "It's a good thing you enjoy it."
        ch_Laura "I don't plan on stopping any time soon."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1347
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1348
    elif dice_roll == 2:
        $ Laura.change_face("sly")

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "You like when I {i}use{/i} you?"

        $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1) 

        ch_Laura "Good."

        $ Laura.change_face("sly", blush = 1)

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1349
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1350
    elif dice_roll == 3:
        $ Laura.change_face("pleased2")

        pause 0.5

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "I guess I'll have to do it more often then."

        $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)  

        ch_Laura "It's not my fault you turn me on all the time. . ."

        $ Laura.change_face("sexy", blush = 1)

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1351
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1352
    elif dice_roll == 4:
        $ Laura.change_face("pleased2")

        pause 0.5

        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "Of course you love it. . ."

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "You get off on being used by me."
        ch_Laura "I can tell."

        $ Laura.change_face("sexy", eyes = "down", blush = 2)

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1353
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1354

    return

label Laura_flirt_aj:
    if Player.scholarship == "academic":
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "You enjoy teaching me?"

        $ Laura.change_face("smirk2", blush = 1) 

        ch_Laura "It doesn't suck. . . as much, when you're there."

        $ Laura.change_face("neutral", eyes = "left", blush = 1)

        ch_Laura "I do appreciate your help."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1355 
    elif dice_roll == 2:
        $ Laura.change_face("pleased1")

        pause 0.5

        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "Easy to teach?"

        $ Laura.change_face("smirk2", blush = 1) 

        ch_Laura "Thanks."
        ch_Laura "It's easier to focus when you're the one tutoring me."

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "So. . . we will do it more often, then?"

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1356 
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "You {i}enjoy{/i} all this studying shit?"

        $ Laura.change_face("neutral", blush = 1) 

        ch_Laura "I mean. . . it is substantially easier to understand when you're teaching me. . ."

        $ Laura.change_face("suspicious1", blush = 1)

        ch_Laura "But something must be wrong with you."
        ch_Laura "I don't know how it all comes so easily to you."

        $ Laura.change_face("confused1", eyes = "right", blush = 1) 

        ch_Laura "Nobody enjoys studying. . ."

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1357

    return

label Laura_flirt_ak:
    if approval_check(Laura, threshold = [125, 150]) or Laura.History.check("studied_with_Player"):    
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(3, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2")

        $ Laura.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Laura "I do. . . ?" 

        $ Laura.change_face("sly", blush = 1)

        ch_Laura "You always smell {i}very{/i} good as well."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_487
    elif dice_roll == 2:
        $ Laura.change_face("pleased1", blush = 1) 

        ch_Laura "You like the way I smell?" 

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "I like the way you smell too. . ."
        ch_Laura "I've never met anyone who smells as good as you do."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_488
    elif dice_roll == 3:
        $ Laura.change_face("confused3") 

        pause 1.0

        $ Laura.change_face("angry1")

        ch_Laura "Why do you know what I smell like?" 

        $ Laura.change_face("suspicious1")

        ch_Laura "You should stop standing so close."

        call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_489
        call change_Girl_stat(Laura, "trust", -5) from _call_change_Girl_stat_490

    return

label Laura_flirt_al:
    $ Laura.change_face("surprised2") 

    pause 0.5

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "Sleek?"

    $ Laura.change_face("smirk2", blush = 1) 

    ch_Laura "Thanks. . ."

    call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1358 

    return

label Laura_flirt_am:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("pleased2") 

        pause 0.5

        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "You've been watching me train. . . ?"

        $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1)

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "I've been watching you as well."
        ch_Laura "You're still clumsy, but you look good."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1359
    elif dice_roll == 2:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("confused1", mouth = "smirk", blush = 1) 

        ch_Laura "You think I look deadly. . . ?"

        $ Laura.change_face("sly", blush = 2) 

        ch_Laura "I am deadly."
        ch_Laura "You're lucky I'm the one teaching you how to fight."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1360
    elif dice_roll == 3:
        $ Laura.change_face("confused1", blush = 1)

        pause 1.0

        $ Laura.change_face("sly", blush = 1) 

        ch_Laura "Maybe you should stop staring at me while I train."
        ch_Laura "You're already distracted enough as it is. . ."

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 2)

        ch_Laura "At least you're catching on relatively quickly."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1361

    return

label Laura_flirt_an:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("worried1", eyes = "left", blush = 1) 

        ch_Laura "Smiling is. . . new to me. . ."

        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura "You like mine?"

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1362
    elif dice_roll == 2:
        $ Laura.change_face("pleased1")

        pause 0.5

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "Thanks. . ."

        $ Laura.change_face("neutral", eyes = "left", blush = 1) 

        ch_Laura "It just doesn't feel. . . natural."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1363
    elif dice_roll == 3:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("smirk2", eyes = "left", blush = 1) 

        ch_Laura "I find myself doing it more often when you're around. . ."

        $ Laura.change_face("suspicious1", blush = 2) 

        ch_Laura "There's just something about you."
        ch_Laura "It's suspicious. . ."

        call change_Girl_stat(Laura, "love", 7) from _call_change_Girl_stat_1364

    return

label Laura_flirt_ao:
    if Player.scholarship == "athletic":
        $ dice_roll = renpy.random.randint(1, 2)
    else:
        $ dice_roll = renpy.random.randint(1, 1)

    if dice_roll == 1:
        $ Laura.change_face("confused2")

        pause 0.5

        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "How are you, of all people, able to tell?"

        $ Laura.change_face("sly", blush = 1) 

        ch_Laura ". . . you're not wrong."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1365
        call change_Girl_stat(Laura, "trust", 3) from _call_change_Girl_stat_1366
    elif dice_roll == 2:
        $ Laura.change_face("pleased2")

        pause 0.5

        $ Laura.change_face("smirk2", blush = 1) 

        ch_Laura "Thanks. . ."
        ch_Laura "With my training, you might at least be able to survive a fight against me. . ."

        $ Laura.change_face("smirk2", eyes = "down", blush = 1)

        pause 0.5

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "For a few minutes. . ."
        ch_Laura "You're in surprisingly good shape, all things considered."

        call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1367
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1368

    return

label Laura_flirt_ap:
    $ Laura.change_face("surprised2")

    pause 0.5

    $ Laura.change_face("confused1", blush = 1) 
    
    pause 0.5

    $ Laura.change_face("smirk2", eyes = "left", blush = 1)

    ch_Laura "I've been training non-stop since before I can remember. . ."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I didn't have a choice but to be good enough. . . capable enough."

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)
    
    ch_Laura "Thanks for calling me beautiful."

    $ Laura.change_face("smirk2", mouth = "lipbite", eyes = "down", blush = 1) 

    ch_Laura "And. . . you're in better shape than 90\% of people here too. . ."

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

    call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1369
    call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1370

    return

label Laura_flirt_aq:
    $ Laura.change_face("confused2")

    pause 0.5

    $ Laura.change_face("confused1", blush = 1) 

    ch_Laura "'Effortlessly'? You mean because I don't wear useless shit?"

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Laura "At least you also appreciate it."

    $ Laura.change_face("smirk2", blush = 1) 

    ch_Laura "A fight could break out at any time."
    ch_Laura "Wearing clothes that would get in the way is just idiotic. . ."

    call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1371
    call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1372

    return

label Laura_flirt_ar:
    $ Laura.change_face("pleased2")

    pause 0.5

    $ Laura.change_face("smirk1", eyes = "left", blush = 1) 

    ch_Laura "The issue was never being capable of learning. . ."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Just feels like a waste of time. Time that would be better spent training."

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

    ch_Laura "It's just easier to. . . relax around you."
    ch_Laura "I only catch on so fast thanks to you."

    call change_Girl_stat(Laura, "love", 10) from _call_change_Girl_stat_1373
    call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1374

    return

label Laura_flirt_b:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Player "Do you have a map? I keep getting lost in your abs. . . I mean, eyes."

        $ Laura.change_face("confused1", mouth = "smirk") 

        ch_Laura "A map?"

        $ Laura.change_face("suspicious1")

        ch_Laura "Did you hit your head again. . . ?"

        call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1375
    elif dice_roll == 2:
        ch_Player "I'm gonna have to ask you to leave. You're making everyone else look bad in comparison."

        $ Laura.change_face("appalled1") 

        pause 0.5

        $ Laura.change_face("confused1", mouth = "smirk")

        ch_Laura "I thought you were being serious for a moment. . ."

        call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1376
    elif dice_roll == 3:
        ch_Player "Just looking at you is like a workout. . ."

        $ Laura.change_face("confused1") 

        ch_Player ". . . because I can't help my heart rate from sky rocketing ."

        $ Laura.change_face("confused2", blush = 1)

        pause 0.5 

        $ Laura.change_face("sly", blush = 1)

        ch_Laura "I can tell you're not lying."

        call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1377
    elif dice_roll == 4:
        ch_Player "I know you have super sharp claws, but your other hidden weapon is even deadlier."

        $ Laura.change_face("confused1") 

        ch_Laura "The claws in my feet?"
        ch_Player "You have claws in your feet?!"
        ch_Player "No. . . I was talking about your beauty, because just looking at you hurts. . ."

        $ Laura.change_face("pleased1")

        pause 0.5

        $ Laura.change_face("confused1", mouth = "smirk")

        ch_Laura "I think the claws in my feet are still deadlier."
        ch_Player "Probably. . ."

        call change_Girl_stat(Laura, "love", 4) from _call_change_Girl_stat_1378

    return

label Laura_flirt_c:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ Laura.change_face("confused2", blush = 1)

        pause 0.5

        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 

        ch_Laura "What are you doing. . . ?"

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1379 
    elif dice_roll == 2:
        $ Laura.change_face("confused1", blush = 1) 

        ch_Laura ". . . why are you staring?"
        ch_Player "Your eyes are just really pretty. . ."

        $ Laura.change_face("pleased2", blush = 1) 

        pause 0.5

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Oh. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1380

    return

label Laura_flirt_d:
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ Laura.change_face("confused1", blush = 1)

        ch_Laura "I know this is a thing couples do. . . but. . ."

        $ Laura.change_face("neutral", mouth = "lipbite", blush = 1)

        ch_Laura "Fuck it."
        "She grabs your hand and squeezes. . . a bit too hard."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1381
    elif dice_roll == 2:
        ch_Laura "I still don't get it. . ."
        ch_Laura "Fine."

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        "She reaches out and takes your hand, interlacing her fingers with yours."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1382
    elif dice_roll == 3:
        $ Laura.change_face("smirk2", eyes = "left", blush = 1)

        "She doesn't say anything and just grabs your hand."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1383

    return

label Laura_flirt_ea:
    "She gives you a rough kiss on the cheek."
    ch_Laura "I don't know why you wanted that over a real kiss. . ."

    $ Laura.change_face("confused1", mouth = "lipbite")

    call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1384

    return

label Laura_flirt_eb:
    if Player.location in public_locations and approval_check(Laura, threshold = [50, 100]):
        $ Laura.change_face("smirk2", eyes = "left", mouth = "lipbite", blush = 1) 

        ch_Laura "Fuck it. . ." 

        $ Laura.change_face("kiss1", blush = 1) 

        "She roughly pulls you into a kiss, holding it for a moment before pulling away." 

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

        ch_Laura "I'm going to need more than that later. . ." 

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1385
    elif Player.location in public_locations:
        $ Laura.change_face("confused1", eyes = "right", mouth = "lipbite", blush = 1) 

        ch_Laura "I like kissing you. . ." 
        ch_Laura "But not when other people are looking." 

        $ Laura.change_face("neutral", blush = 1)
    elif Laura.quirk:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "How'd you know I was thinking about doing just that?"

        $ Laura.change_face("sexy", blush = 1)

        ch_Laura "If you don't come here, I'll make you."
        ch_Player ". . ."

        $ Laura.change_face("sexy", eyes = "down", blush = 2)

        call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1386
        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1387

        $ Laura.change_face("kiss2", blush = 2)  

        "After a quick kiss, you pull away." 

        $ Laura.change_face("angry1", mouth = "lipbite", blush = 2) 

        ch_Laura "That's it?"
        ch_Laura "I wasn't done."

        if Player.stamina and Laura.stamina:
            menu:
                extend ""
                "Let her do as she pleases":
                    ch_Player "If you want to keep going. . ."
                    ch_Player "You don't need my permission."

                    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

                    ch_Laura "Good."

                    call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1388
                    call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1389

                    "Without a word, she pulls you back into the kiss."

                    $ Laura.History.update("hookup")
                    $ Laura.History.update("makeout")

                    $ Action = ActionClass("makeout", Player, Laura)

                    call start_Action(Action) from _call_start_Action_15
                    call screen Action_screen(automatic = True)
                "Pull away":
                    pass
    else:
        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 

        ch_Laura "Get over here."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1390 

        $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Laura "Don't make me wait."

        $ Laura.change_face("kiss2", blush = 1) 

        "She pulls you down into a kiss, her hands holding on to you for dear life."
        "She starts clumsily using her tongue, and her enthusiasm is evident."

        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1391 

        $ Laura.change_face("kiss2", blush = 2)

        if Player.stamina and Laura.stamina:
            menu:
                extend ""
                "Make out with her":
                    call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1392

                    $ Laura.History.update("hookup")
                    $ Laura.History.update("makeout")

                    $ Action = ActionClass("makeout", Player, Laura)

                    call start_Action(Action) from _call_start_Action_16
                    call screen Action_screen(automatic = True)
                "Pull away":
                    $ Laura.change_face("confused1", blush = 2) 

                    ch_Laura "I wasn't done. . ."

                    $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

                    ch_Laura "Fine, we'll just continue later."

        ch_Laura "Sorry. . . got a bit carried away. . ."

    return

label Laura_flirt_f:
    if Player.location in public_locations and approval_check(Laura, threshold = [125, 150]):
        $ Laura.change_face("confused1", eyes = "left")

        "She doesn't say anything, and instead pulls you into a bear hug."

        $ Laura.change_face("angry1", eyes = "closed") 

        "She squeezes the breath out of you before letting go." 

        $ Laura.change_face("angry1", mouth = "lipbite", blush = 1) 

        ch_Player "I thought you didn't do hugs. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1393
    elif Player.location in public_locations:
        $ Laura.change_face("confused1") 

        pause 0.5

        $ Laura.change_face("angry1") 

        ch_Laura "I don't do hugs. . ." 

        $ Laura.change_face("angry1", eyes = "left")

        ch_Laura "Especially not with an audience."

        call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1394
    elif approval_check(Laura, threshold = [125, 150]):
        $ Laura.change_face("pleased1", blush = 1) 

        ch_Laura "Fine. . ." 

        $ Laura.change_face("smirk2", eyes = "closed", blush = 1) 

        "Without another word, she pulls you into her arms." 
        "She squeezes you tightly and holds the embrace for a long moment." 

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "I. . . think I understand why people do it now."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1395
    else:
        $ Laura.change_face("confused2")

        pause 0.5

        $ Laura.change_face("suspicious1")

        ch_Laura "A hug?"
        ch_Laura "Why. . . ?"

        $ Laura.change_face("neutral", eyes = "right", blush = 1) 

        ch_Laura "No." 

        call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1396

    return

label Laura_flirt_g:
    $ Laura.change_face("pleased1") 

    ch_Laura "Fine, you're the only one I trust with my back anyway. . .."

    $ Laura.change_face("smirk2", eyes = "closed") 

    "You get right to work, kneading her prominent back muscles."
    "She leans back into your hands, shuddering." 

    $ Laura.change_face("smirk2", blush = 1) 

    ch_Laura "Do that more often."

    call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1397

    return

label Laura_flirt_h:
    if approval_check(Laura, threshold = [150, 175]):
        $ Laura.change_face("surprised2", blush = 1)

        pause 0.5

        $ Laura.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 1) 

        "You run your hand through [Laura.name]'s hair."
        "She leans into it, and holds your hand against her head for a moment." 

        $ Laura.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Laura "I. . . didn't hate that. . ." 

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1398
    else:
        $ Laura.change_face("angry1", blush = 1) 

        "You reach out to touch [Laura.name]'s hair, but she forcefully swats your hand away." 

        $ Laura.change_face("suspicious1", blush = 1)

        ch_Laura "The fuck are you trying to do?"

        call change_Girl_stat(Laura, "trust", -3) from _call_change_Girl_stat_1399

    return

label Laura_flirt_i:
    if Player.location in public_locations and approval_check(Laura, threshold = [125, 150]):
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("suspicious1", blush = 1) 

        "You wrap your arm around [Laura.name] and her body stiffens slightly."
        "Probably readying herself to throw you off if the need arises." 

        $ Laura.change_face("neutral", eyes = "closed", blush = 1) 

        ch_Laura "I don't know how I feel about this. . ." 
        "After a moment, she pulls away." 

        $ Laura.change_face("neutral", blush = 1)

        ch_Laura "Especially in front of other people."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1400
    elif Player.location in public_locations:
        $ Laura.change_face("appalled1")

        "As you go to put an arm around [Laura.name], she swiftly steps out of reach."

        $ Laura.change_face("suspicious1")

        ch_Laura "What do you think you're doing?"
        ch_Laura "Don't get so close."
    elif approval_check(Laura, threshold = [125, 150]):
        $ Laura.change_face("surprised2", blush = 1) 

        pause 0.5

        $ Laura.change_face("sly", blush = 1)

        "As you wrap an arm around [Laura.name], she puts a hand on your ass." 

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1401

        $ Laura.change_face("kiss2", blush = 2) 

        "She turns, and doesn't hesitate to start kissing you." 

        call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1402

        "Her grip on your ass tightens, and tongue starts getting involved." 

        menu:
            extend ""
            "Make out with her":
                call change_Girl_stat(Laura, "love", 2) from _call_change_Girl_stat_1403
                call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1404

                $ Laura.History.update("hookup")
                $ Laura.History.update("makeout")

                $ Action = ActionClass("makeout", Player, Laura)

                call start_Action(Action) from _call_start_Action_17
                call screen Action_screen(automatic = True)
            "Pull away":
                $ Laura.change_face("confused1", mouth = "lipbite", blush = 1) 

                ch_Laura "You're done?"
    else:
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("suspicious", blush = 1) 

        "As you try to wrap your arm around [Laura.name], she steps out of reach." 

        ch_Laura "Don't get so close. . ."

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1405

    return

label Laura_flirt_ja:

    return

label Laura_flirt_jb:

    return

label Laura_flirt_jc:

    return

label Laura_flirt_jd:

    return

label Laura_flirt_ka:

    return

label Laura_flirt_kb:

    return

label Laura_flirt_l:
    if Player.location in public_locations and approval_check(Laura, threshold = [175, 200]):
        $ Laura.change_face("surprised2")

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Fine. . . do it. . ."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (Laura.sprite_position[0], 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "You give her ass a proper smack, and she doesn't make a sound." 

        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1406

        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "I enjoyed that. . ." 

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1407
    elif Player.location in public_locations:
        $ Laura.change_face("confused2")

        pause 0.5

        $ Laura.change_face("suspicious1")

        ch_Laura "Why would I let you hit me?"
        ch_Laura "In front of other people no less."

        call change_Girl_stat(Laura, "love", -2) from _call_change_Girl_stat_1408
    elif Laura.quirk:
        $ Laura.change_face("confused1")

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "First. . ."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (0.5, 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "Without saying anything, she gives your ass a hard smack, leaving a stinging sensation." 

        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1409

        $ Laura.change_face("sexy", blush = 1) 

        ch_Laura "Now you can do it to me."
        ch_Laura "Make sure you do it hard. . ."

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (Laura.sprite_position[0], 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "You comply, and smack her ass with quite a lot of force."
        "She doesn't even flinch, but instead you hear a soft moan escape her lips."

        $ Laura.change_face("surprised2", mouth = "lipbite", blush = 2) 

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1410

        ch_Laura "Almost hard enough. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1411
    else:
        $ Laura.change_face("confused1")

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Fine, I'll allow it."

        $ Laura.change_face("sexy", blush = 1)

        show expression "images/effects/smack.webp" as smack onlayer effects:
            anchor (0.5, 0.5) pos (Laura.sprite_position[0], 0.7)

            zoom 0.0
            alpha 0.0
            ease 0.1 zoom 1.0 alpha 1.0
            ease 1.0 alpha 0.0

        with small_screenshake
        
        "You give her ass a proper smack, and she shudders slightly from the impact."

        call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1412

        $ Laura.change_face("surprised2", mouth = "lipbite", blush = 2) 

        pause 0.5

        $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Laura "Harder next time. . ." 

        call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1413

    return

label Laura_flirt_ma:

    return

label Laura_flirt_mb:

    return

label Laura_flirt_mc:

    return

label Laura_flirt_na:

    return

label Laura_flirt_nb:

    return

label Laura_flirt_nc:

    return

label Laura_flirt_oa:
    "You walk up to her, and give her a quick kiss on the cheek." 

    $ Laura.change_face("confused2")

    call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1414
    call change_Girl_stat(Laura, "desire", 5) from _call_change_Girl_stat_1415

    $ Laura.change_face("smirk2", blush = 1) 

    ch_Laura "Why not a real kiss. . . ?"

    return

label Laura_flirt_ob:
    "As you get close, she does all the work for you, and pulls you into a deep kiss." 

    $ Laura.change_face("kiss2", blush = 1) 

    call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1416
    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1417

    "She keeps kissing you another moment, before letting go." 

    $ Laura.change_face("smirk2", mouth = "lipbite", blush = 1) 

    ch_Laura "I really like doing that with you. . ." 

    return

label Laura_flirt_pa:

    return

label Laura_flirt_pb:

    return

label Laura_flirt_pc:

    return

label Laura_flirt_pd:

    return

label Laura_flirt_qa:
    $ Laura.change_face("pleased2", blush = 1)

    call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1418
    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1419 

    pause 0.5

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "Good, I didn't plan on stopping any time soon."
    ch_Laura "I can tell how aroused you are whenever you're near me." 
    ch_Player "You can?" 

    $ Laura.change_face("sexy", blush = 1) 

    ch_Laura "Yes. . ." 
    ch_Laura "It makes me want to use you even more. . ."

    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1420 

    return

label Laura_flirt_qb:
    $ Laura.change_face("appalled2", blush = 1) 

    call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1421
    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1422

    pause 0.5

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Laura "I can't control myself around you."
    ch_Laura "If I don't use you to satisfy myself, I find it hard to be rational." 

    $ Laura.change_face("sexy", eyes = "down", blush = 1) 

    ch_Laura "But, you enjoy being mine to use. . ." 

    $ Laura.change_face("sexy", blush = 1) 

    ch_Laura "So it isn't an issue."

    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1423

    return

label Laura_flirt_qc:
    $ Laura.change_face("pleased2", blush = 1) 

    call change_Girl_stat(Laura, "love", 3) from _call_change_Girl_stat_1424
    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1425

    pause 0.5

    $ Laura.change_face("sly", blush = 1)

    ch_Laura "I can easily tell you enjoy it." 
    ch_Laura "How the thought of me abducting you to satisfy my needs, makes you. . ."

    $ Laura.change_face("sexy", eyes = "down", blush = 1) 

    ch_Laura "Like that." 

    $ Laura.change_face("sly", blush = 1) 

    ch_Laura "And I can smell whenever you're. . ." 

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "It just makes me want to do it even more. . ."

    call change_Girl_stat(Laura, "desire", 10) from _call_change_Girl_stat_1426 

    return

label Laura_flirt_r:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ Laura.change_face("confused3", blush = 1)

        ch_Player "Just wanted to say I love you."
        ch_Laura "I. . ."

        $ Laura.change_face("worried1", mouth = "smirk", eyes = "right", blush = 1)

        ch_Laura ". . . good."

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "I love you too."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1427
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1428
    elif dice_roll == 2:
        $ Laura.change_face("worried2", blush = 1)

        ch_Player "I love you, by the way."

        $ Laura.change_face("worried1", mouth = "smirk", eyes = "right", blush = 1)

        ch_Laura "It makes me happy to hear you say that. . ."

        $ Laura.change_face("smirk2", blush = 1)

        ch_Laura "I love you too."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1429
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1430
    elif dice_roll == 3:
        $ Laura.change_face("worried2", blush = 1)

        ch_Player "Hey, I love you."
        ch_Laura "You are being genuine?"

        $ Laura.change_face("smirk2", blush = 1)

        ch_Player "I am, as always."
        ch_Laura "I love you as well. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1431
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1432
    elif dice_roll == 4:
        $ Laura.change_face("suspicious1", blush = 1)

        "Just as you start to speak, [Laura.name] talks over you."
        ch_Laura "I love you."

        $ Laura.change_face("sly", blush = 1)

        ch_Player "I was about to say the same thing."
        ch_Laura "Good. . ."

        call change_Girl_stat(Laura, "love", 5) from _call_change_Girl_stat_1433
        call change_Girl_stat(Laura, "trust", 5) from _call_change_Girl_stat_1434

    return