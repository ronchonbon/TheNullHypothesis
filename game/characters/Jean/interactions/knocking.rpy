label Jean_knocks(arriving_Characters):
    $ choice_disabled = False

    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear someone knocking at the door." 

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]? It's me." 
        ch_Jean "Open up."

        menu:
            extend ""
            "Sure!":
                call add_Characters(arriving_Characters) from _call_add_Characters_4

                $ Jean.change_face("smirk2") 
                
                ch_Jean "Happy to see me?"
            "Sorry, not right now":
                ch_Jean "Oh, come on." 
                
                ch_Jean "Fine, I'll be back later."
            "No, not right now.":
                ch_Jean "Ugh. . . fine." 
                
                call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_245
    elif dice_roll == 2:
        "You hear knocking at your door."  
        ch_Player "Who is it?" 
        ch_Jean "It's [Jean.name]!" 
        ch_Jean "I wanna hang out."

        menu:
            extend ""
            "Sounds fun.":
                call add_Characters(arriving_Characters) from _call_add_Characters_5

                $ Jean.change_face("smirk2") 
                
                ch_Jean "Hey."
            "Sorry, I'm a bit busy.":
                ch_Jean "Fine, I'll just go study I guess."

                call send_Characters(Jean, Jean.home, behavior = "studying") from _call_send_Characters_60
            "I'm busy.":
                ch_Jean "Ugh. . . fine." 
                
                call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_246

    return

label Jean_knocks_relationship(arriving_Characters):
    $ choice_disabled = False

    "Someone is knocking at your door."

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp]? I know you missed me." 
    ch_Jean "Open up."

    menu:
        extend ""
        "Let me get the door.":
            call add_Characters(arriving_Characters) from _call_add_Characters_6

            $ Jean.change_face("smirk2") 
            
            ch_Jean "Hey there."
        "Not right now, maybe come back later?":
            ch_Jean "Really?" 
            ch_Jean "Fine, but you better let me in later."
        "Not in the mood right now.":
            ch_Jean "Not in the mood?" 
            ch_Jean "Ugh, fine." 
            ch_Jean "What about later?" 
            ch_Player "Maybe." 
            
            call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_247

    return

label Jean_knocks_love(arriving_Characters):
    $ choice_disabled = False

    if Jean.quirk:
        "There's knocking at your door."  
        ch_Jean "Better open up, [Jean.Player_petname]." 
        ch_Jean "Your big sis' needs some attention."

        menu:
            extend ""
            "Sorry, let me get the door.":
                call add_Characters(arriving_Characters) from _call_add_Characters_7

                $ Jean.change_face("sly") 
                
                ch_Jean "Say thank you. . ." 
                ch_Player "Uh, for what?"
                
                $ Jean.change_face("suspicious1") 
                
                ch_Jean "Really?" 
                ch_Jean "Your big sis' wants to hang out with you." 
                ch_Jean "Is that not enough?" 
                
                $ Jean.change_face("angry1") 
                
                ch_Player "No it is. . ." 
                ch_Player "I'm sorry." 
                
                $ Jean.change_face("kiss2", blush = 1) 
                
                "She doesn't say anything and just pulls you into a kiss" 
                "One of her hands moves to your crotch." 
                "After a moment, she pulls away from the kiss, but leaving her hand where it is." 

                $ Jean.History.update("kiss")
                
                $ Jean.change_face("sexy", blush = 1) 
                
                ch_Jean "I can tell you liked that."
            "I'm sorry, not right now.":
                ch_Player "Could you come over later?" 
                ch_Jean "Fine." 
                ch_Jean "But now you owe me."
            "I'm busy.":
                ch_Jean "Oh really?" 
                ch_Jean "You're making me mad, [Jean.Player_petname]." 
                
                call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_248
    else:
        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp], it's me!"
        ch_Jean "I know you wanna see me." 
        
        menu:
            extend ""
            "Be right there!":
                call add_Characters(arriving_Characters) from _call_add_Characters_8
                
                $ Jean.change_face("kiss2", blush = 1) 
                
                "As [Jean.name] enters, she pulls you into a kiss." 
                "One of her hands moves to your ass." 
                "After a moment she pulls away." 

                $ Jean.History.update("kiss")
                
                $ Jean.change_face("sexy", blush = 1) 
                
                ch_Jean "God, you're hot." 
                
                $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
                
                ch_Jean "I'm hot too, right?"
            "Sorry, I'm kinda busy right now.":
                ch_Jean "Oh. . . okay." 
                ch_Jean "At least come see me later."
            "Kinda in the middle of something.":
                ch_Jean "Don't have to be rude about it. . ." 
                
                call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_249

    return

label Jean_knocks_mad(arriving_Characters):
    $ choice_disabled = False

    "Someone starts banging on your door." 
    ch_Jean "Open the hell up!" 
    ch_Jean "I'm pissed off."

    "You rush over and open the door." 

    call add_Characters(arriving_Characters) from _call_add_Characters_9

    $ Jean.change_face("furious")

    ch_Player "What's wrong?" 
    ch_Player "Did I do something?" 

    $ Jean.change_face("suspicious2")

    ch_Jean "No. . ."

    return

label Jean_knocks_heartbroken(arriving_Characters):
    $ choice_disabled = False

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp]?" 
    ch_Jean "You home?" 

    menu:
        extend ""
        "I am, want to come in?":
            ch_Jean "Please. . ." 
            "You go over and open the door." 

            $ Jean.give(Jean_running_mascara())

            call try_on(Jean, Jean.Wardrobe.Clothes["running mascara"]) from _call_try_on_3

            call add_Characters(arriving_Characters) from _call_add_Characters_10
            
            $ Jean.change_face("worried1") 
            
            ch_Player "You okay?" 
            ch_Jean "Not really, no. . ."
        "Yeah. . . sorry but I'm kinda busy.":
            ch_Jean "Oh. . . Okay. . ."
        "Stay silent":
            ch_Jean ". . . really?" 
            
            call change_Girl_stat(Jean, "love", -5) from _call_change_Girl_stat_250

    return

label Jean_knocks_horny(arriving_Characters):
    $ choice_disabled = False

    "You hear some quick knocks at your door."

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp]!"
    ch_Jean "It's me!"
    ch_Jean "Let me in!"

    menu:
        extend ""
        "Let me get the door.":
            call add_Characters(arriving_Characters) from _call_add_Characters_11

            $ Jean.change_face("sexy") 
            
            ch_Jean "Hi. . ."
        "Sorry, but I'm a bit preoccupied.":
            ch_Jean "Ugh, really?" 
            ch_Jean "Whatever, I'll just spend some time alone. . . in my room. . . {i}touching myself{/i}. . ."

            call send_Characters(Jean, Jean.home, behavior = "masturbating") from _call_send_Characters_61

    return

label Jean_knocks_nympho(arriving_Characters):
    $ choice_disabled = False

    "Someone starts knocking frantically at the door."
    ch_Jean "God, you better open the door right now."
    ch_Player "One sec." 

    call add_Characters(arriving_Characters) from _call_add_Characters_12

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Jean "You better give me some special attention right now. . ." 

    $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Player "Attention?" 
    ch_Jean "Yeah."

    $ Jean.change_face("sexy", eyes = "down", blush = 1)

    ch_Jean "You look like just what I need." 

    $ Jean.change_face("sexy", blush = 1)

    ch_Player "Uh. . . OH!"

    return

label Jean_greets_Player_knocking(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 4)

    if dice_roll == 1:
        ch_Jean "Who is it?" 
        ch_Player "It's me! Can I come in?" 
        ch_Jean "[Player.first_name]? As if I'd say no to you."

        call set_the_scene(location = Jean.home) from _call_set_the_scene_56
    elif dice_roll == 2:
        ch_Jean "One sec!" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_57

        $ Jean.change_face("pleased2")

        ch_Jean "Oh! Hey!" 

        $ Jean.change_face("smirk2")
    elif dice_roll == 3:
        ch_Player "Jean, it's me." 
        ch_Jean "Oh, [Player.first_name]? Come in already."

        call set_the_scene(location = Jean.home) from _call_set_the_scene_58
    elif dice_roll == 4:
        ch_Jean "Be right there!" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_59

        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("smirk2")

        ch_Jean "Well hey." 

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Need anything?"


    return True

label Jean_greets_Player_knocking_relationship(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        ch_Jean "That better be you, [Jean.Player_petname]." 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_60

        $ Jean.change_face("pleased2")

        pause 1.0

        $ Jean.change_face("sly", blush = 1)

        ch_Jean "Good, it is you. . ." 
    elif dice_roll == 2:
        ch_Player "It's [Player.first_name], can I come in?" 

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]?!" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_61

        $ Jean.change_face("happy")

        ch_Jean "Missed me?" 

        $ Jean.change_face("smirk2")
    elif dice_roll == 3:
        ch_Player "It's [Player.first_name]!"
        ch_Jean "You better come on in, [Jean.Player_petname]."

        call set_the_scene(location = Jean.home) from _call_set_the_scene_62

        $ Jean.change_face("sly", blush = 1)

    return True

label Jean_greets_Player_knocking_love(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], can I come in?"
        
        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]?!" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_63

        $ Jean.change_face("kiss2", blush = 1)

        "She pulls you right into a kiss." 

        $ Jean.History.update("kiss")

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "You love me, right?"
        ch_Player "Of course." 

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)
    elif dice_roll == 2:
        ch_Jean "I hope that's you, [Jean.Player_petname]!" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_64

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        ch_Jean "Missed me that much?" 
    elif dice_roll == 3:
        ch_Player "Hey, [Jean.petname]. It's me!" 
        "You hear someone scrambling to get the door open."

        call set_the_scene(location = Jean.home) from _call_set_the_scene_65

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "I definitely wasn't sitting around, waiting for you. . ." 

        $ Jean.change_face("worried1")

        ch_Jean "You missed me, right?"

    return True

label Jean_greets_Player_knocking_mad(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 3)

    if dice_roll == 1:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp]? Can I come in?" 
        ch_Jean "Ugh, I'm not in the mood for company."
        ch_Jean "Go away."
    elif dice_roll == 2:
        ch_Jean "I don't care who it is." 
        ch_Jean "I'm not in the mood. . ."
    elif dice_roll == 3:
        ch_Jean "Just go away!"

    $ Jean.wants_alone_time = 1

    call move_location("bg_girls_hallway") from _call_move_location_7

    return True

label Jean_greets_Player_knocking_heartbroken(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        "You hear someone crying inside the room."
        ch_Jean "*sniffle* Go away!"

        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], it's me."
        ch_Jean "I. . . don't want you to see me like this." 
        ch_Jean "Go away. . ."

        $ Jean.wants_alone_time = 1

        call move_location("bg_girls_hallway") from _call_move_location_8
    elif dice_roll == 2:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp]?" 
        ch_Jean "*sniffle* [Jean.Player_petname]?" 
        ch_Jean "You can come in." 

        $ Jean.give(Jean_running_mascara())

        call try_on(Jean, Jean.Wardrobe.Clothes["running mascara"]) from _call_try_on_4

        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_66

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "Just don't look too closely. . ." 

        $ Jean.change_face("worried1")

        ch_Jean ". . . my makeup is a bit messed up." 
        ch_Player "Are you okay?" 

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "I'm fine. . ."

    return True

label Jean_greets_Player_knocking_horny(welcoming_Characters):
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Jean "That better be you, [Jean.Player_petname]!" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_67

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Good." 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        ch_Jean "You look {i}really{/i} good right now. . ." 

        $ Jean.change_face("sexy", blush = 1)
    elif dice_roll == 2:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp]?" 
        ch_Jean "That you, [Jean.Player_petname]?" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_68

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "I might've been about to go looking for you. . ." 

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "Thanks for saving me the trouble."

    return True

label Jean_greets_Player_knocking_nympho(welcoming_Characters):
    if Jean.quirk:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp]?" 
        "The door swings open, and you're yanked inside." 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_69

        $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

        ch_Jean "Your big sis' needs some {i}special{/i} attention right now. . ." 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)
    else:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp]?" 
        
        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]?" 

        call set_the_scene(location = Jean.home) from _call_set_the_scene_70

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "God I was hoping you'd come see me. . ." 
        ch_Jean "I {i}need{/i} some attention right now." 

        $ Jean.change_face("sexy", eyes = "down", blush = 1)

        pause 1.0

        $ Jean.change_face("sexy", blush = 1)

    return True

label Jean_greets_Player_knocking_reject(welcoming_Characters):
    if Jean.showering:
        $ dice_roll = renpy.random.randint(1, 3)
    else:
        $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp]? It's me. Can I come in?" 

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp]?" 
        ch_Jean "I'm busy right now." 
        ch_Jean "Definitely come by later, though."
    elif dice_roll == 2:
        ch_Jean "Who is it?"  
        ch_Player "It's, [Player.first_name]." 
        ch_Jean "I'm about to take a shower." 
        ch_Jean "Come by later!"

        $ reset_behavior(Jean)

        $ Jean.showering = True
    elif dice_roll == 3:
        "You hear water running as you walk up to the door." 
        "You knock a couple times, but she probably can't hear you from the shower." 
        "Better try again later."

        $ Jean.wants_alone_time = 1

    return True

label Jean_greets_Player_knocking_reject_asked_once:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Jean "Cut it out!"
    elif dice_roll == 2:
        ch_Jean "Really?" 
        ch_Jean "Go away!"

    return True

label Jean_greets_Player_knocking_reject_asked_twice:
    ch_Jean "You better cut it the hell out!"

    return True

label Jean_greets_Player_knocking_late:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Player "[Jean.name]? It's me. Can I come in?"
        ch_Jean "[Player.first_name]?"
        ch_Jean "It's kind of late."
        ch_Jean "Talk tomorrow?"
    elif dice_roll == 2:
        "You knock on the door."
        ch_Player "It's [Player.first_name]."
        ch_Jean "I'm getting ready for bed, sorry!"
        ch_Jean "Let's catch up tomorrow!"

    return True

label Jean_greets_Player_knocking_late_asked_once:
    $ dice_roll = renpy.random.randint(1, 2)

    if dice_roll == 1:
        ch_Jean "Cut it out!"
    elif dice_roll == 2:
        ch_Jean "Really?" 
        ch_Jean "Go away!"

    return True

label Jean_greets_Player_knocking_late_asked_twice:
    ch_Jean "You better cut it the hell out!"

    return True

label Jean_not_invited_in:
    $ Jean.change_face("smirk2")

    ch_Jean "I'm comfy out here."

    return