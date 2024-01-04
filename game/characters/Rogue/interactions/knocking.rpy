label Rogue_knocks(arriving_Characters):
    $ choice_disabled = False

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear someone knocking at the door."

        if len(arriving_Characters) > 2:
            ch_Rogue "Sugar? It's a few of us."
            ch_Rogue "Can we come in?"
        elif len(arriving_Characters) == 2:
            ch_Rogue "Sugar? It's me and [arriving_Characters[1].name]."
            ch_Rogue "Can we come in?"
        else:
            ch_Rogue "Sugar? It's me."
            ch_Rogue "Can ah come in?"

        menu:
            extend ""
            "Sure!":
                $ Rogue.change_face("smirk2")

                call add_Characters(arriving_Characters) from _call_add_Characters_37

                ch_Rogue "How are ya?"
            "Sorry, not right now":
                ch_Rogue "Oh, alright."
                ch_Rogue "Sorry to bother ya."
            "Nah.":
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_773

                ch_Rogue "Oh. . . okay."
    elif dice_roll == 2:
        "You hear knocking at your door."
        ch_Player "Who is it?"
        
        if len(arriving_Characters) > 2:
            ch_Rogue "It's a few of us!"
            ch_Rogue "Can we come in?"
        elif len(arriving_Characters) == 2:
            ch_Rogue "It's [Rogue.name] and [arriving_Characters[1].name]!"
            ch_Rogue "Can we come in and hang?"
        else:
            ch_Rogue "It's [Rogue.name]!"
            ch_Rogue "Can ah come in and hang?"

        menu:
            extend ""
            "Of course.":
                $ Rogue.change_face("smirk2")

                call add_Characters(arriving_Characters) from _call_add_Characters_38

                ch_Rogue "Howdy."
            "Sorry, [Rogue.name]. I'm a bit busy.":
                if len(arriving_Characters) > 1:
                    ch_Rogue "It's alright, maybe we'll see ya later."
                else:
                    ch_Rogue "It's alright, maybe ah'll see ya later."
            "I'm busy.":
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_774

    return

label Rogue_knocks_relationship(arriving_Characters):
    $ choice_disabled = False

    "Someone is knocking at your door."

    $ temp = Rogue.Player_petname.capitalize()
    
    ch_Rogue "[temp]? Could ah come in?"
    ch_Rogue "Ah've been missin' ya."

    menu:
        extend ""
        "Let me get the door.":
            call add_Characters(arriving_Characters) from _call_add_Characters_39

            $ Rogue.change_face("pleased2")

            ch_Rogue "Always good to see ya."

            $ Rogue.change_face("smirk2")
        "Not right now, maybe come back later?":
            ch_Rogue "Okay, sorry."
            ch_Rogue "Ah'll try again later."
        "Not in the mood, [Rogue.name].":
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_775

            ch_Rogue "Sorry. . ."
            ch_Rogue "Maybe ah'll see you later?"
            ch_Player "Maybe."

    return

label Rogue_knocks_love(arriving_Characters):
    $ choice_disabled = False

    "There's knocking at your door."

    if Rogue.check_traits("quirk"):
        $ temp = Rogue.Player_petname.capitalize()
        
        ch_Rogue "[temp]?"
        ch_Rogue "May ah please come in?"

        menu:
            extend ""
            "You can come in, let me get the door.":
                ch_Rogue "Thanks. . ."
                ch_Rogue "Ah missed ya. . ."
                ch_Player "But I just saw you not too long ago?"

                call add_Characters(arriving_Characters) from _call_add_Characters_40

                $ Rogue.change_face("worried2")

                ch_Rogue "Ah know. . . but still."
                ch_Rogue "Can ah have a hug?"
                ch_Player "Sure."

                pause 1.0

                $ Rogue.change_face("smirk2", eyes = "closed")

                "You pull her into a quick hug, and she squeezes you tightly before letting go."

                pause 1.0

                $ Rogue.change_face("smirk2")

                ch_Rogue "Thanks. . ."
            "Not right now. Go back to your room and I might come over later.":
                ch_Rogue "Alright."
                ch_Rogue "Ah'll wait 'round for a while."

                call send_Characters(Rogue, Rogue.home) from _call_send_Characters_166
            "I'm busy.":
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_776

                ch_Rogue "Sorry to bother ya. . ."
    else:
        $ temp = Rogue.Player_petname.capitalize()
        
        ch_Rogue "[temp], it's me!"
        ch_Rogue "Ah wanna see ya."

        menu:
            extend ""
            "I'll be right there!":
                call add_Characters(arriving_Characters) from _call_add_Characters_41

                $ Rogue.change_face("pleased2")

                pause 1.0

                $ Rogue.eyes = "closed"

                "You pull her into a quick hug, and she squeezes you tightly before letting go."

                pause 1.0

                $ Rogue.change_face("happy")

                ch_Rogue "Ah needed that."
            "Sorry, I'm kinda busy right now.":
                ch_Rogue "Oh, alright."
                ch_Rogue "Ah'll see ya later, maybe."
            "Kinda in the middle of something.":
                call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_777

                ch_Rogue "Didn't mean to bother ya. . ."

    return

label Rogue_knocks_mad(arriving_Characters):
    $ choice_disabled = False

    "Someone starts banging on your door."
    ch_Rogue "It's [Rogue.name]! Let me in."
    ch_Rogue "Ah'm not in the mood to mess around."
    "You rush over and open the door."

    call add_Characters(arriving_Characters) from _call_add_Characters_42

    $ Rogue.change_face("appalled1")

    ch_Player "What's wrong?"

    $ Rogue.change_face("angry1", eyes = "squint")

    ch_Rogue "Ah'm just in a mood. . ."

    return

label Rogue_knocks_heartbroken(arriving_Characters):
    $ choice_disabled = False

    ch_Rogue "[Player.first_name]?"
    ch_Rogue "Are ya home?"

    menu:
        extend ""
        "I am, want to come in?":
            ch_Rogue "Yeah. . ."
            "You go over and open the door."

            call add_Characters(arriving_Characters) from _call_add_Characters_43

            $ Rogue.change_face("worried1")

            ch_Player "You okay?"
            ch_Rogue "Ah dunno. . ."

            $ Rogue.eyes = "down"
        "I am, sorry but I'm kinda busy.":
            ch_Rogue "Okay. . . sorry."
        "Stay silent":
            call change_Character_stat(Rogue, "love", -tiny_stat) from _call_change_Character_stat_778

            ch_Rogue ". . . sorry."

    return

label Rogue_knocks_horny(arriving_Characters):
    $ choice_disabled = False

    "You hear some quick knocks at your door."

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]. It's me."
    ch_Rogue "Could ah come in?"

    menu:
        extend ""
        "Let me get the door.":
            call add_Characters(arriving_Characters) from _call_add_Characters_44

            $ Rogue.change_face("worried1", blush = 2)

            ch_Rogue "Hey. . ."

            $ Rogue.mouth = "lipbite"
        "Sorry, but I'm a bit preoccupied.":
            ch_Rogue "It's okay. . ."
            ch_Rogue "Ah'll just spend some time alone. . . in my room. . ."

            call send_Characters(Rogue, Rogue.home, behavior = "masturbating") from _call_send_Characters_167

    return

label Rogue_knocks_nympho(arriving_Characters):
    $ choice_disabled = False
    
    "Someone starts knocking frantically at the door."

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp], please."
    ch_Rogue "Ah need to see you."
    ch_Player "Be right there."

    call add_Characters(arriving_Characters) from _call_add_Characters_45

    $ Rogue.change_face("manic", blush = 2)

    ch_Rogue "Ah really need some attention right now. . ."
    ch_Player "Attention?"

    $ Rogue.blush = 3

    ch_Rogue "You know. . ."

    $ Rogue.eyes = "down"

    pause 1.0

    $ Rogue.eyes = "neutral"

    ch_Rogue ". . . {i}attention{/i}."
    ch_Player "Oh. Oh!"

    return

label Rogue_greets_Player_knocking(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Rogue "Who is it?"
        ch_Player "It's me! Can I come in?"
        ch_Rogue "Course you can come in, hon'."
    elif dice_roll == 2:
        ch_Rogue "Ah'll be right there!"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_213

        $ Rogue.change_face("pleased2")

        ch_Rogue "Howdy!"
    elif dice_roll == 3:
        ch_Player "[Rogue.name], it's me."
        ch_Rogue "Come on in, sugar."
    elif dice_roll == 4:
        ch_Rogue "Be there in a jiff!"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_214
        
        $ Rogue.change_face("surprised2")

        pause 1.0

        $ Rogue.change_face("smirk2")

        ch_Rogue "Hey! What can ah do for ya?"

    return

label Rogue_greets_Player_knocking_relationship(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Rogue "Ah'll be there in a sec."

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_215

        $ Rogue.change_face("pleased2", blush = 1)

        $ temp = Rogue.Player_petname.capitalize()
        
        ch_Rogue "[temp]! Ah'm glad yer here. . ."

        $ Rogue.change_face("smirk2")
    elif dice_roll == 2:
        ch_Player "Can I come in?"
        ch_Rogue "[Player.first_name]?!"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_216

        $ Rogue.change_face("worried2")

        ch_Rogue "As if ah would say no. . ."
    elif dice_roll == 3:
        ch_Player "It's me!"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_217

        $ Rogue.change_face("pleased2")

        ch_Rogue "Darlin'! Come on in."

    return

label Rogue_greets_Player_knocking_love(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ temp = Rogue.petname.capitalize()

        ch_Player "[temp]!"

        $ temp = Rogue.Player_petname.capitalize()
        
        ch_Rogue "[temp]?!"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_218

        $ Rogue.change_face("pleased2")

        pause 1.0

        $ Rogue.change_face("smirk2", eyes = "closed")

        "She pulls you right into a hug."

        pause 1.0

        $ Rogue.change_face("smirk2")

        ch_Rogue "Glad yer here. . ."
    elif dice_roll == 2:
        ch_Rogue "Is that you, sugar?"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_219

        $ Rogue.change_face("happy")

        ch_Rogue "Am ah happy to see you. . ."

        $ Rogue.change_face("smirk2")
    elif dice_roll == 3:
        ch_Player "Hey, [Rogue.name]. It's me!"
        "You hear someone scrambling to get the door open."

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_220

        $ Rogue.change_face("pleased2", blush = 1)

        ch_Rogue "Ah was hopin' you'd come by."

        $ Rogue.change_face("worried1")

        ch_Rogue "Please stick around for a while. . ."

    return

label Rogue_greets_Player_knocking_mad(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Player "[Rogue.name]? Can I come in?"
        ch_Rogue "Ah'm not in the mood. . ."
    elif dice_roll == 2:
        "You knock on the door."
        ch_Rogue "Ah'm not openin' the door."
        ch_Rogue "Go away, whoever it is. . ."
    elif dice_roll == 3:
        ch_Rogue "Go away!"
        ch_Rogue "Ah'm not in the mood. . ."

    $ Rogue.wants_alone_time = 1

    call move_location("bg_girls_hallway") from _call_move_location_34

    return

label Rogue_greets_Player_knocking_heartbroken(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear faint sobbing from inside the room."
        ch_Rogue "*sniffle* Who is it?"
        ch_Player "[Rogue.name], it's me."
        ch_Rogue "[Player.first_name]?"
        ch_Rogue "Sorry, ah want to be alone right now. . ."

        $ Rogue.wants_alone_time = 1

        call move_location("bg_girls_hallway") from _call_move_location_35
    elif dice_roll == 2:
        ch_Player "[Rogue.name]?"
        ch_Rogue "One sec. . ."

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_221

        $ Rogue.change_face("worried1", eyes = "down")
        
        ch_Rogue "You can come in if ya want. . ."

    return

label Rogue_greets_Player_knocking_horny(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Rogue "Ah sure hope that's you, [Rogue.Player_petname]."

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_222

        $ Rogue.change_face("pleased2", blush = 1)
        
        ch_Rogue "It is you."

        $ Rogue.mouth = "lipbite"

        ch_Rogue "Ah was just thinkin' 'bout ya. . ."

        $ Rogue.blush = 2
    elif dice_roll == 2:
        ch_Player "[Rogue.name]?"
        ch_Rogue "Is that my stud?"

        call set_the_scene(location = Rogue.home) from _call_set_the_scene_223

        $ Rogue.change_face("surprised2", blush = 1)

        ch_Rogue "Ah was hopin' you'd come by. . ."

        $ Rogue.change_face("sexy")

    return

label Rogue_greets_Player_knocking_nympho(welcoming_Characters):
    ch_Player "[Rogue.name], you home?"

    $ temp = Rogue.Player_petname.capitalize()

    ch_Rogue "[temp]!"
    ch_Rogue "Sure, ah'll get the door."

    call set_the_scene(location = Rogue.home) from _call_set_the_scene_224

    $ Rogue.change_face("manic", blush = 1)

    ch_Rogue "God, you don't know how much ah was hopin' you'd come 'round. . ."

    $ Rogue.eyes = "sexy"
    $ Rogue.blush = 2

    pause 1.0

    $ Rogue.eyes = "down"

    pause 1.0

    $ Rogue.eyes = "sexy"

    return

label Rogue_greets_Player_knocking_reject(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Player "[Rogue.name]? It's me. Can I come in?"
        ch_Rogue "[Player.first_name]?"
        ch_Rogue "Sorry, ah'm a bit busy."
        ch_Rogue "Maybe you can come by later."
    elif dice_roll == 2:
        "You knock on the door."
        ch_Rogue "Who is it?"
        ch_Player "It's [Player.first_name]."
        ch_Rogue "Sorry, ah was just about to shower."
        ch_Rogue "Can ya come by later?"

    return

label Rogue_greets_Player_knocking_reject_asked_once:
    call Rogue_asked_once("knocking")

    return

label Rogue_greets_Player_knocking_reject_asked_twice:
    call Rogue_asked_twice("knocking")
    
    return

label Rogue_greets_Player_knocking_late:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Player "[Rogue.name]? It's me. Can I come in?"
        ch_Rogue "[Player.first_name]?"
        ch_Rogue "Sorry, it's a little late."
        ch_Rogue "Let's talk tomorrow."
    elif dice_roll == 2:
        "You knock on the door."
        ch_Player "It's [Player.first_name]."
        ch_Rogue "Sorry, ah'm about to go to sleep."
        ch_Rogue "Talk tomorrow?"

    return

label Rogue_greets_Player_knocking_late_asked_once:
    call Rogue_asked_once("knocking")

    return

label Rogue_greets_Player_knocking_late_asked_twice:
    call Rogue_asked_twice("knocking")
    
    return

label Rogue_not_invited_in:
    $ Rogue.change_face("worried1")
    
    ch_Rogue "Let's stay out here for now, [Rogue.Player_petname]."

    return