label Laura_knocks(arriving_Characters):
    $ choice_disabled = False

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear someone knocking."
        ch_Laura "Open the door."

        menu:
            extend ""
            "Sure, one sec.":
                $ Laura.change_face("smirk2")

                call add_Characters(arriving_Characters) from _call_add_Characters_21

                ch_Laura "Finally."
            "Sorry. . . not right now":
                ch_Laura "Fine."
                ch_Laura "Later."
            "I'd rather not. . .":
                ch_Laura "Fine."

                call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_491
    elif dice_roll == 2:
        "You hear knocking at your door."
        ch_Player "Who is it?"
        ch_Laura "You really can't tell?"

        if len(arriving_Characters) > 1:
            ch_Laura "Let us in."
        else:
            ch_Laura "Let me in."

        menu:
            extend ""
            "No. . . but sure, let me get the door.":
                $ Laura.change_face("confused1")

                call add_Characters(arriving_Characters) from _call_add_Characters_22

                ch_Laura "You should really have more awareness."
            "Sorry, [Laura.name]. I'm a bit busy.":
                if len(arriving_Characters) > 1:
                    ch_Laura "Fine, we'll be back later."
                else:
                    ch_Laura "Fine, I'll be back later."
            "No, I'm busy.":
                call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_492

    return

label Laura_knocks_relationship(arriving_Characters):
    $ choice_disabled = False

    "Someone starts knocking on your door. . . more like banging."
    ch_Laura "Open the door."

    menu:
        extend ""
        "One sec!":
            call add_Characters(arriving_Characters) from _call_add_Characters_23

            $ Laura.change_face("sly")

            ch_Player "Is everything okay?"

            $ Laura.change_face("confused1")

            ch_Laura "Yes, why?"
            ch_Laura "Just wanted to be with you."

            $ Laura.change_face("smirk2")
        "Not right now, maybe come back later?":
            ch_Laura "{i}Grrrrr{/i}. . . fine."
        "Not in the mood, [Laura.name].":
            ch_Laura "Fine. . ."
            ch_Laura "I'll be back later."

            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_493

    return

label Laura_knocks_love(arriving_Characters):
    $ choice_disabled = False

    if Laura.quirk:
        "Someone's banging on your door."
        ch_Laura "Open."
        ch_Laura "I know for a fact you're inside."

        menu:
            extend ""
            "Be right there.":
                call add_Characters(arriving_Characters) from _call_add_Characters_24

                $ Laura.change_face("angry1")

                ch_Laura "Took you long enough. . ."
                ch_Laura "Don't know why I can't just keep you in my room."
                ch_Player "'Keep me'?"

                $ Laura.change_face("confused1")

                ch_Laura "Yes. . . you're {i}mine{/i}."
                ch_Laura "I should have access to you whenever I want."
                ch_Player "Well. . ."
                "Without a word, she roughly pulls you into a kiss and shoves a hand down your pants."

                $ Laura.change_face("kiss2", blush = 1)

                "She fondles your manhood for a moment, and your body involuntarily responds."
                "She pulls away after a good groping."

                $ Laura.History.update("kiss")

                $ Laura.change_face("sexy", blush = 2)
            "Not right now. Can you come back later?":
                ch_Laura "{i}Grrrrr{/i}"
                ch_Laura "You're gonna pay for this."
            "I'm busy.":
                ch_Laura "Bad excuse. . ."

                call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_494
    else:
        if len(arriving_Characters) == 2:
            ch_Laura "It's me and [arriving_Characters[1].name]."
        elif len(arriving_Characters) > 1:
            ch_Laura "It's a few of us."
        else:
            ch_Laura "It's me."

        ch_Laura "Open the door."
        ch_Laura "I know you're in there."

        menu:
            extend ""
            "One sec!":
                call add_Characters(arriving_Characters) from _call_add_Characters_25

                $ Laura.change_face("smirk2")

                "As [Laura.name] enters, she pulls you into a kiss."

                $ Laura.change_face("kiss2")

                "She moves one of your hands to her crotch, while also starting to fondle yours."

                $ Laura.blush = 1

                "After a moment, she pulls away."

                $ Laura.History.update("kiss")

                ch_Player "What was that for?"

                $ Laura.change_face("confused1")

                ch_Laura "There needs to be a reason?"
            "Sorry, I'm kinda busy right now.":
                ch_Laura "Fine, just come find me later."
            "Kinda in the middle of something.":
                ch_Laura "Yeah, right."

                call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_495

    return

label Laura_knocks_mad(arriving_Characters):
    $ choice_disabled = False

    "Someone starts banging on your door."
    ch_Laura "Open the door before I kick it in."
    "You rush over and open it."

    call add_Characters(arriving_Characters) from _call_add_Characters_26

    $ Laura.change_face("appalled1")

    ch_Player "Everything okay?"

    $ Laura.change_face("angry1", eyes = "squint")

    ch_Laura "Yeah. . . I'm just pissed off."
    ch_Player "At?"
    ch_Laura "No."

    return

label Laura_knocks_heartbroken(arriving_Characters):
    $ choice_disabled = False

    ch_Laura "[Player.first_name]?"
    ch_Laura ". . ."

    menu:
        extend ""
        "[Laura.name]? Want to come in?":
            ch_Laura "Yes. . ."
            "You go over and open the door."

            call add_Characters(arriving_Characters) from _call_add_Characters_27

            $ Laura.change_face("worried1")

            pause 1.0

            $ Laura.change_face("angry1")

            ch_Player "You okay?"
            ch_Laura "No. . ."

            $ Laura.eyes = "right"

            pause 1.0

            $ Laura.eyes = "down"
        "Sorry. . . but I'm kinda busy.":
            ch_Laura ". . . sorry."
        "Stay silent":
            ch_Laura ". . . I know you're ignoring me."

            call change_Girl_stat(Laura, "love", -5) from _call_change_Girl_stat_496

    return

label Laura_knocks_horny(arriving_Characters):
    $ choice_disabled = False

    "You hear some harsh knocking at your door."
    ch_Laura "Open the door."
    ch_Laura "Hurry. . ."

    menu:
        extend ""
        "Be right there.":
            call add_Characters(arriving_Characters) from _call_add_Characters_28

            $ Laura.change_face("angry1", blush = 1)

            ch_Laura "It's your fault. . . I'm like this. . ."

            $ Laura.mouth = "lipbite"

            ch_Player "Like what?"

            $ Laura.change_face("furious", blush = 2)

            ch_Laura "Really. . ."
        "Sorry, but I'm a bit preoccupied.":
            ch_Laura "{i}Grrrrr{/i}"
            ch_Laura "Fine. . . I'l just deal with it on my own. . ."

            call send_Characters(Laura, Laura.home, behavior = "masturbating") from _call_send_Characters_118

    return

label Laura_knocks_nympho(arriving_Characters):
    $ choice_disabled = False

    "Someone starts knocking frantically at the door."
    ch_Laura "You need to open the door."
    ch_Laura "Now!"
    ch_Player "Just give me one sec."

    call add_Characters(arriving_Characters) from _call_add_Characters_29

    $ Laura.change_face("appalled2", blush = 2)

    ch_Laura "It's your fault I'm like this."
    ch_Player "Like what?"
    
    $ Laura.change_face("angry1", mouth = "lipbite", blush = 3)

    ch_Laura "If you don't do something about it. . ."

    $ Laura.eyes = "down"

    pause 1.0

    $ Laura.eyes = "neutral"

    ch_Laura "I might just make you watch while I do it to myself."
    ch_Player "Oh. Oh!"

    return

label Laura_greets_Player_knocking(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Laura "Who is it?"
        ch_Player "It's [Player.first_name]."
        ch_Laura "Oh."
        ch_Laura "Come in."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_137

        $ Laura.change_face("neutral", blush = 1)

        pause 1.0

        $ Laura.blush = 0
    elif dice_roll == 2:
        ch_Laura "One second."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_138

        $ Laura.change_face("neutral")

        ch_Laura "What do you want?"
    elif dice_roll == 3:
        ch_Player "[Laura.name], it's me."
        ch_Laura "The door swings open."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_139

        $ Laura.change_face("neutral")

        ch_Laura "Hi."
    elif dice_roll == 4:
        ch_Laura "I'll be right there, [Player.first_name]."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_140
        
        $ Laura.change_face("neutral", eyes = "squint")

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "How'd you know it was me?"

        $ Laura.change_face("confused1")
        
        ch_Laura "I can smell {i}you{/i} of all people from a mile away."
        ch_Laura "Not in a. . . bad way. . ."

        $ Laura.change_face("neutral", blush = 1)

    return

label Laura_greets_Player_knocking_relationship(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        call set_the_scene(location = Laura.home) from _call_set_the_scene_141

        $ Laura.change_face("smirk2", blush = 1)
        
        ch_Player "What the-"
        ch_Laura "Think I wouldn't hear you coming?"

        $ Laura.eyes = "squint"
    elif dice_roll == 2:
        ch_Player "Can I come in?"
        ch_Laura "Yes."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_142

        $ Laura.change_face("confused1")

        ch_Laura "Where have you been?"

        $ Laura.eyes = "squint"
    elif dice_roll == 3:
        ch_Player "It's me!"

        call set_the_scene(location = Laura.home) from _call_set_the_scene_143

        $ Laura.change_face("pleased2")

        ch_Laura "Good, come in."

        $ Laura.change_face("smirk2")

    return

label Laura_greets_Player_knocking_love(welcoming_Characters):
    if Laura.quirk:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ temp = Laura.petname.capitalize()

        ch_Player "[temp]!"
        ch_Laura "Be right there."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_144

        $ Laura.change_face("smirk2")

        pause 1.0

        $ Laura.change_face("kiss2", eyes = "closed")

        "She pulls you right into a kiss."

        $ Laura.History.update("kiss")

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "I'm going to need more than that. . ."
    elif dice_roll == 2:
        ch_Player "[Laura.name], can I come in?"
        "The door instantly swings open, and [Laura.name] pulls you inside."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_145

        $ Laura.change_face("neutral", blush = 1)

        ch_Laura "Stay."

        $ Laura.change_face("angry1")
        
        ch_Laura "You're going to hang out with me. . ."
    elif dice_roll == 3:
        ch_Laura "I know you're there."
        ch_Laura "Just come in already, [Player.first_name]."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_146

        $ Laura.change_face("confused1")

        ch_Laura "I know where you are. . . pretty much all the time."

        $ Laura.change_face("smirk2")

    return

label Laura_greets_Player_knocking_mad(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        "As you get close to the door, it sounds like someone is beating the shit out of a punching bag."
        ch_Player "[Laura.name]?"
        ch_Laura "Fuck off!"
    elif dice_roll == 2:
        "You knock on the door."
        ch_Laura "{i}Grrrrr{/i}"
        ch_Laura "Go away, [Player.first_name]."
        ch_Laura "Not in the mood."
    elif dice_roll == 3:
        ch_Laura "Leave before I get even angrier."

    $ Laura.wants_alone_time = 1

    call move_location("bg_girls_hallway") from _call_move_location_22

    return

label Laura_greets_Player_knocking_heartbroken(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear sounds of anger mixed with sobs on the other side of the door."
        ch_Laura "{i}Grrrrrr{/i}, go away, [Player.first_name]."
        ch_Laura "*sniffle* I know you're there."
        ch_Player "Sorry. . ."

        $ Laura.wants_alone_time = 1

        call move_location("bg_girls_hallway") from _call_move_location_23
    elif dice_roll == 2:
        ch_Player "[Laura.name]?"
        ch_Laura "{size=-5}Fuck{/size}. . . one sec. . ."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_147

        $ Laura.change_face("angry1", eyes = "right")

        ch_Player "You okay?"

        $ Laura.change_face("furious")

        ch_Laura "Shut up, I'm fine."

    return

label Laura_greets_Player_knocking_horny(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "Come in already, [Player.first_name]."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_148

        $ Laura.change_face("sly", blush = 1)
        
        ch_Laura "You smell {i}really{/i} good right now. . ."

        $ Laura.eyes = "down"
        $ Laura.mouth = "lipbite"

        pause 1.0

        $ Laura.eyes = "neutral"
        $ Laura.blush = 2
    elif dice_roll == 2:
        ch_Player "[Laura.name]?"
        ch_Laura "Good, come in."

        call set_the_scene(location = Laura.home) from _call_set_the_scene_149

        $ Laura.change_face("pleased1", blush = 1)

        ch_Laura "If you didn't stop by, I might've had to track you down. . ."

        $ Laura.change_face("sexy")

    return

label Laura_greets_Player_knocking_nympho(welcoming_Characters):
    ch_Laura "You better stop standing there and come in already."

    call set_the_scene(location = Laura.home) from _call_set_the_scene_150

    $ Laura.change_face("manic", blush = 1)

    ch_Laura "I was just about to go out and. . . 'kidnap' you."

    $ Laura.eyes = "sexy"
    $ Laura.blush = 2

    pause 1.0

    $ Laura.eyes = "down"

    pause 1.0

    $ Laura.eyes = "sexy"

    return

label Laura_greets_Player_knocking_reject(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Player "[Laura.name]? You there?"
        ch_Laura "Yes."
        ch_Player "Can I. . ."
        ch_Laura "No."
    elif dice_roll == 2:
        ch_Player "[Laura.name]? You there?"
        ch_Laura "No."
        ch_Player "I guess I'll come back later. . ."
    elif dice_roll == 3:
        "You knock on the door."
        ch_Laura "I know it's you, [Player.first_name]!"
        ch_Player "How. . ."
        ch_Laura "You can't come in."
        ch_Laura "I'm about to take a shower."
    elif dice_roll == 4:
        "You hear water running as you walk up to the door."
        "You knock a couple times, but she probably can't hear you. . ."
        ch_Laura "I'm showering, [Player.first_name]!"
        ch_Laura "Come back later."
        ch_Player "{size=-5}How did you know{/size}. . ."
        ch_Laura "I heard that!"

    return

label Laura_greets_Player_knocking_reject_asked_once:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "I said fuck off!"
    elif dice_roll == 2:
        ch_Laura "Don't push it."

    return

label Laura_greets_Player_knocking_reject_asked_twice:
    ch_Laura "Stop before I put a hole through the door."

    return

label Laura_greets_Player_knocking_late:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Player "[Laura.name]? It's me. Can I come in?"
        ch_Laura "Come back tomorrow."
    elif dice_roll == 2:
        "You knock on the door."
        ch_Player "It's [Player.first_name]."
        ch_Laura "Not tonight."

    return

label Laura_greets_Player_knocking_late_asked_once:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Laura "I said fuck off!"
    elif dice_roll == 2:
        ch_Laura "Don't push it."

    return

label Laura_greets_Player_knocking_late_asked_twice:
    ch_Laura "Stop before I put a hole through the door."

    return

label Laura_not_invited_in:
    ch_Laura "I don't want to go in."

    return