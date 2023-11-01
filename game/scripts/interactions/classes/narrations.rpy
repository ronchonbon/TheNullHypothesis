label chapter_1_season_1_class_narrations:
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        $ dice_roll = renpy.random.randint(1, 4)
        
        if dice_roll == 1:
            "The lecture is on Mutant Physiology. The professor gives an introductory lesson on understanding the X-Gene, and its role in manifesting mutant abilities. It's made clear that this is closely guarded knowledge, and the majority of the public are kept in the dark about such information."
        elif dice_roll == 2:
            "The lecture is on Mutant Physiology. Today's topic is the various ways mutant abilities can affect our bodies and cause our biology to deviate from normal humans. In many cases, powers provide enhancements. It is not unheard of, however, for mutations to be detrimental to that person or the people around them."
        elif dice_roll == 3:
            "The lecture is on Mutant Physiology. You learn about some of the more extreme mutations that have drastically altered a person's body and how they have affected them both physically and mentally. The professor starts touching upon some higher level concepts and even some biochemistry. You try your best to understand the material, but you've never taken high level biology courses before."
        elif dice_roll == 4:
            "The lecture is on Mutant Physiology. The professor is using Colossus as an example for how a person, with enough control, can actively change the expression of their mutation. Colossus is able to change his body into an organic steel-like substance which drastically alters his physical capabilities. You pay extra attention since this information could directly benefit someone like you."
    elif dice_roll == 2:
        $ dice_roll = renpy.random.randint(1, 4)
        
        if dice_roll == 1:
            "The lecture is on World Politics. The professor briefly goes over the current political landscape before diving into how mutants are viewed globally. From all the terrible things you've heard up until now, it really seems like everyone is out to get mutants. The world isn't a safe place for you anymore, and you didn't even get a say in it."
        elif dice_roll == 2:
            "The lecture is on World Politics. This particular class is highlighting certain high profile political figures who have taken one side or another in the debate concerning mutant-kind. There are some, like Senator Robert Kelly, who are actively working to limit the rights and freedoms of mutants. Public proponents of mutants are unfortunately few and far between."
        elif dice_roll == 3:
            "The lecture is on World Politics. Today's discussion is about the various activists and threats around the world that are actively working against mutant-kind. Aside from certain governments and political figures, there are private institutions, corporations, and individuals with anti-mutant agendas. The professor also briefly talks about how many governments are constantly developing technology capable of combating mutants."
        elif dice_roll == 4:
            "The lecture is on World Politics. The professor outlines the history of politics and how things have changed over time concerning their view towards mutant-kind. Initially, mutants were mostly feared or hated because they were an unknown factor. Unfortunately, things have not progressed in a favorable direction. As things stand, the world may even be more hostile to mutants now that more people are aware of them."
    elif dice_roll == 3:
        if Player.scholarship == "academic":
            $ dice_roll = renpy.random.randint(1, 1)
        else:
            $ dice_roll = renpy.random.randint(1, 4)
        
        if dice_roll == 1:
            "The lecture for Calculus 102 begins. This particular lecture is focused on all the rules pertaining to finding derivatives. You make sure to write them all down in exhaustive detail. The quotient rule, difference rule, power rule, product rule, pussy rule. . . wait what?"
        elif dice_roll == 2:
            "The lecture for Calculus 102 begins. Math was never your strong suit, and you might have failed precalculus in high school. Thankfully, the professor isn't just a brilliant scholar but also knows how to properly teach the material in a digestible manner. You actually enjoyed math class for once. . ."
        elif dice_roll == 3:
            "The lecture for Calculus 102 begins. Today's topic is on derivatives. You quickly learn that you hate derivatives and whatever sadist invented them. You still try your best to understand the concepts, but today's lecture was particularly painful."
        elif dice_roll == 4:
            "The lecture for Calculus 102 begins. The professor reviews some basic pre-calculus concepts before transitioning to more in depth topics. Since you retained virtually nothing from pre-calculus in high school, a lot of the information goes right over your head. You write a note to ask [Rogue.name] for help with some of the harder stuff."
    elif dice_roll == 4:
        $ dice_roll = renpy.random.randint(1, 4)
        
        if dice_roll == 1:
            "The lecture for Psychology 101 begins. The professor is covering topics you recall hearing about in Farouk's class. Just thinking about him sends a shiver down your spine as you recall that inhuman voice from the bathroom that day. . . By the time you snap back to reality, the lecture is almost over."
        elif dice_roll == 2:
            "The lecture for Psychology 101 begins. Today's topic is on the DSM and how classification of mental illnesses currently works in America. The professor also touches on how mental health problems may be more common in mutant populations due to how certain mutations affect our biology."
        elif dice_roll == 3:
            "The lecture for Psychology 101 begins. The professor discusses the prevalence of mental health issues in modern society. You quickly realize that just because mutants have super powers, they are still just as susceptible to mental illness, if not more so than normal people."
        elif dice_roll == 4:
            "The lecture for Psychology 101 begins. Today's class is on the history of psychology and how mental health recognition has changed over time. A bunch of prominent people in the world of psychology are discussed and you try your best to take notes and retain the information. You recognize some of the names from Farouk's class, and just thinking of him makes focusing difficult."

    return

label chapter_1_season_2_class_narrations:
    $ dice_roll = renpy.random.randint(1, 13)
    
    if dice_roll == 1:
        "Today's class is on 'Law Enforcement Tactics, and Why They Don't Work'. Or at least, that's what it should've been. Seems like the professor's been warned about this sort of thing before. You can't help but feel there's a story or three there. . ."
    elif dice_roll == 2:
        "Today's lecture is on notable figures in mutant popular culture. This time, the focus is on renowned fashion designer Jumbo Carnation and his collaborations with Stark Industries. Not something you find particularly gripping, but Tony Stark's face as he sees Carnation's take on the Iron Man armor gets a good giggle from everyone."
    elif dice_roll == 3:
        "Today's lecture is 'Psychic Defence 101'. You go over some of the ways psychics can infiltrate a mind and how to shore up your defenses by repeating tongue-twisters and song lyrics in your head. One student is praised for their excellent defense, until it turns out they were just staring out the window the whole time."
    elif dice_roll == 4:
        "Today's lecture is 'Psychic Defence 101'. You think. Feels like there's a big hole in your memory where the class was. Hope that wasn't anything important."
    elif dice_roll == 5:
        "You attend a lecture on Mutant Physiology. One student can't stop laughing at the use of the word 'flagellum'. The professor rolls their eyes audibly every time the giggling starts from the back."
    elif dice_roll == 6:
        "You attend a lecture on Mutant Physiology. You learn from the professor that the correct term for prehensile tendrils exhibiting on or around the mouth isn't 'face noodles'. Whoops."
    elif dice_roll == 7:
        "The lecture for flight training begins. You assume the class to be mostly optional for those unable to fly until your ears prick up at the mention of 'jetpacks'. Now it's all you can think about."
    elif dice_roll == 8:
        "You attend a lecture on shapeshifters and how to spot them. One student gets into an argument with the professor about the ethics and morals of impersonating celebrities. You get the impression this is going to take a while."
    elif dice_roll == 9:
        "You attend a lecture about the power of invisibility. You think. It may just be that the professor is running *really* late. It's hard to tell around here sometimes."
    elif dice_roll == 10:
        "You were expecting a test today, but the professor was called out on a mission to some place called 'Madripoor'. No skin off your nose, time for a nice, easy study session!"
    elif dice_roll == 11:
        "The lecture for Psychology 101 begins. The professor is covering the ideas and theories of Carl Jung. One student gets excited, because some of the themes covered came up in a video game they like. The professor is less than impressed."
    elif dice_roll == 12:
        "Today's lesson is on the difference between 'mutants' and 'mutates'. It takes only 7 minutes, 22 seconds for an argument to break out: a new record!"
    elif dice_roll == 13:
        "Today's class is on time travel theory and non-linear events. The test is last Thursday."

    return

label chapter_1_season_3_class_narrations:
    $ dice_roll = renpy.random.randint(1, 13)
    
    if dice_roll == 1:
        "Today's class is on 'Law Enforcement Tactics, and Why They Don't Work'. Or at least, that's what it should've been. Seems like the professor's been warned about this sort of thing before. You can't help but feel there's a story or three there. . ."
    elif dice_roll == 2:
        "Today's lecture is on notable figures in mutant popular culture. This time, the focus is on renowned fashion designer Jumbo Carnation and his collaborations with Stark Industries. Not something you find particularly gripping, but Tony Stark's face as he sees Carnation's take on the Iron Man armor gets a good giggle from everyone."
    elif dice_roll == 3:
        "Today's lecture is 'Psychic Defence 101'. You go over some of the ways psychics can infiltrate a mind and how to shore up your defenses by repeating tongue-twisters and song lyrics in your head. One student is praised for their excellent defense, until it turns out they were just staring out the window the whole time."
    elif dice_roll == 4:
        "Today's lecture is 'Psychic Defence 101'. You think. Feels like there's a big hole in your memory where the class was. Hope that wasn't anything important."
    elif dice_roll == 5:
        "You attend a lecture on Mutant Physiology. One student can't stop laughing at the use of the word 'flagellum'. The professor rolls their eyes audibly every time the giggling starts from the back."
    elif dice_roll == 6:
        "You attend a lecture on Mutant Physiology. You learn from the professor that the correct term for prehensile tendrils exhibiting on or around the mouth isn't 'face noodles'. Whoops."
    elif dice_roll == 7:
        "The lecture for flight training begins. You assume the class to be mostly optional for those unable to fly until your ears prick up at the mention of 'jetpacks'. Now it's all you can think about."
    elif dice_roll == 8:
        "You attend a lecture on shapeshifters and how to spot them. One student gets into an argument with the professor about the ethics and morals of impersonating celebrities. You get the impression this is going to take a while."
    elif dice_roll == 9:
        "You attend a lecture about the power of invisibility. You think. It may just be that the professor is running *really* late. It's hard to tell around here sometimes."
    elif dice_roll == 10:
        "You were expecting a test today, but the professor was called out on a mission to some place called 'Madripoor'. No skin off your nose, time for a nice, easy study session!"
    elif dice_roll == 11:
        "The lecture for Psychology 101 begins. The professor is covering the ideas and theories of Carl Jung. One student gets excited, because some of the themes covered came up in a video game they like. The professor is less than impressed."
    elif dice_roll == 12:
        "Today's lesson is on the difference between 'mutants' and 'mutates'. It takes only 7 minutes, 22 seconds for an argument to break out: a new record!"
    elif dice_roll == 13:
        "Today's class is on time travel theory and non-linear events. The test is last Thursday."

    return

label chapter_1_season_4_class_narrations:
    $ dice_roll = renpy.random.randint(1, 13)
    
    if dice_roll == 1:
        "Today's class is on 'Law Enforcement Tactics, and Why They Don't Work'. Or at least, that's what it should've been. Seems like the professor's been warned about this sort of thing before. You can't help but feel there's a story or three there. . ."
    elif dice_roll == 2:
        "Today's lecture is on notable figures in mutant popular culture. This time, the focus is on renowned fashion designer Jumbo Carnation and his collaborations with Stark Industries. Not something you find particularly gripping, but Tony Stark's face as he sees Carnation's take on the Iron Man armor gets a good giggle from everyone."
    elif dice_roll == 3:
        "Today's lecture is 'Psychic Defence 101'. You go over some of the ways psychics can infiltrate a mind and how to shore up your defenses by repeating tongue-twisters and song lyrics in your head. One student is praised for their excellent defense, until it turns out they were just staring out the window the whole time."
    elif dice_roll == 4:
        "Today's lecture is 'Psychic Defence 101'. You think. Feels like there's a big hole in your memory where the class was. Hope that wasn't anything important."
    elif dice_roll == 5:
        "You attend a lecture on Mutant Physiology. One student can't stop laughing at the use of the word 'flagellum'. The professor rolls their eyes audibly every time the giggling starts from the back."
    elif dice_roll == 6:
        "You attend a lecture on Mutant Physiology. You learn from the professor that the correct term for prehensile tendrils exhibiting on or around the mouth isn't 'face noodles'. Whoops."
    elif dice_roll == 7:
        "The lecture for flight training begins. You assume the class to be mostly optional for those unable to fly until your ears prick up at the mention of 'jetpacks'. Now it's all you can think about."
    elif dice_roll == 8:
        "You attend a lecture on shapeshifters and how to spot them. One student gets into an argument with the professor about the ethics and morals of impersonating celebrities. You get the impression this is going to take a while."
    elif dice_roll == 9:
        "You attend a lecture about the power of invisibility. You think. It may just be that the professor is running *really* late. It's hard to tell around here sometimes."
    elif dice_roll == 10:
        "You were expecting a test today, but the professor was called out on a mission to some place called 'Madripoor'. No skin off your nose, time for a nice, easy study session!"
    elif dice_roll == 11:
        "The lecture for Psychology 101 begins. The professor is covering the ideas and theories of Carl Jung. One student gets excited, because some of the themes covered came up in a video game they like. The professor is less than impressed."
    elif dice_roll == 12:
        "Today's lesson is on the difference between 'mutants' and 'mutates'. It takes only 7 minutes, 22 seconds for an argument to break out: a new record!"
    elif dice_roll == 13:
        "Today's class is on time travel theory and non-linear events. The test is last Thursday."

    return