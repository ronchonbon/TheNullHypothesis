init python:

    import math

    def Rogue_date():
        label = "Rogue_date"

        conditions = [
            "Rogue in Player.date_planned.keys() and 'primary' in Player.date_planned[Rogue]",
            "time_index == 2",
            "Rogue.History.check('went_on_date_with_Player') >= 1"]

        waiting = True
        traveling = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority, repeatable = repeatable)

label Rogue_date:
    $ ongoing_Event = True

    hide screen phone_screen

    if weather == "rain":
        $ weather = None

    $ Party = []

    if Player.location != "bg_hallway":
        "You have a date with [Rogue.name]: better go and wait for her outside your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_148
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_152

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed

    call receive_text(Rogue, "Omw! :)))") from _call_receive_text_452
    call open_texts(Rogue) from _call_open_texts_6

    pause

    hide screen phone_screen

    "You hear what sounds like running, before [Rogue.name] walks around the corner."

    call send_Characters(Rogue, Player.location, behavior = "on_date") from _call_send_Characters_119

    $ Rogue.change_face("worried2")

    "When she sees you standing there, she slows down and catches her breath before approaching."

    $ Rogue.change_face("worried1")

    ch_Rogue "Howdy. . ."
    ch_Rogue "Ah just didn't wanna be late."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "You ready to go?"
    ch_Rogue "Yep."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_149
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_153
    call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_120

    $ first_event = {}
    $ second_event = {}

    if "Girl_initiated" in Player.date_planned[Rogue]:
        if renpy.random.random() > 0.5:
            ch_Rogue "Ah'm pretty hungry." 
            ch_Rogue "Why don't we start with dinner?"

            $ first_event[Rogue] = "dinner"

            call Rogue_date_dinner from _call_Rogue_date_dinner
        else:
            ch_Rogue "Maybe we could start with a movie?" 
            ch_Rogue "Ah've been in the mood." 

            $ first_event[Rogue] = "movie"

            call Rogue_date_movie from _call_Rogue_date_movie
    else:
        ch_Rogue "Did ya wanna do anythin' in particular?"

        $ Rogue.change_face("smirk2")

        menu:
            extend ""
            "Let's grab some dinner first.":
                ch_Rogue "Whatever ya want."

                $ first_event[Player] = "dinner"

                call Rogue_date_dinner from _call_Rogue_date_dinner_1
            "Let's go catch a movie.":
                ch_Rogue "Whatever ya want."

                $ first_event[Player] = "movie"

                call Rogue_date_movie from _call_Rogue_date_movie_1
            "Actually. . . can we just chill, hang out here?":
                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Rogue "You know ah don't mind, [Rogue.Player_petname]." 
                
                $ Rogue.change_face("smirk2") 
                
                ch_Rogue "So long as ah get to spend time with ya."

                call remove_Characters(location = Player.home) from _call_remove_Characters_150
                call set_the_scene(location = Player.home) from _call_set_the_scene_154
                call send_Characters(Rogue, Player.home, behavior = "on_date") from _call_send_Characters_121

                $ Player.date_planned = {}

                $ ongoing_Event = False

                return

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_151
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_155
    call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_122

    if "Girl_initiated" in Player.date_planned[Rogue]:
        if renpy.random.random() > 0.50:
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                if (Player in first_event.keys() and first_event[Player] == "dinner") or (Rogue in first_event.keys() and first_event[Rogue] == "dinner"):
                    $ second_event[Rogue] = "movie"
                elif (Player in first_event.keys() and first_event[Player] == "movie") or (Rogue in first_event.keys() and first_event[Rogue] == "movie"):
                    $ second_event[Rogue] = "dinner"
            elif dice_roll > 0.125:
                $ second_event[Rogue] = "mall"
            else:
                $ second_event[Rogue] = "end"
    elif "Player_initiated" in Player.date_planned[Rogue]:
        if renpy.random.random() > 0.875:
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                if (Player in first_event.keys() and first_event[Player] == "dinner") or (Rogue in first_event.keys() and first_event[Rogue] == "dinner"):
                    $ second_event[Rogue] = "movie"
                elif (Player in first_event.keys() and first_event[Player] == "movie") or (Rogue in first_event.keys() and first_event[Rogue] == "movie"):
                    $ second_event[Rogue] = "dinner"
            elif dice_roll > 0.125:
                $ second_event[Rogue] = "mall"
            else:
                $ second_event[Rogue] = "end"

    if not second_event:
        $ Rogue.change_face("smirk2", eyes = "right") 

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "What're we doin' next, [Rogue.Player_petname]?" 

        menu:
            extend ""
            "Let's grab dinner. . ." if (Player in first_event.keys() and first_event[Player] == "movie") or (Rogue in first_event.keys() and first_event[Rogue] == "movie"):
                $ second_event[Player] = "dinner"

                call Rogue_date_dinner from _call_Rogue_date_dinner_2
            "Let's head to the movie theater." if (Player in first_event.keys() and first_event[Player] == "dinner") or (Rogue in first_event.keys() and first_event[Rogue] == "dinner"):
                $ Rogue.change_face("smirk2") 
                
                ch_Rogue "Sure thang." 
                ch_Rogue "Ah'm always in the mood for a good movie."

                $ second_event[Player] = "movie"

                call Rogue_date_movie from _call_Rogue_date_movie_2
            "How about we stay in the mall and. . .":
                $ second_event[Player] = "mall"

                call Rogue_date_mall from _call_Rogue_date_mall
            "Want to head back to the Institute?":
                $ Rogue.change_face("confused1", mouth = "smirk") 
                
                ch_Rogue "Sure." 
                
                $ Rogue.change_face("sly") 
                
                ch_Rogue "Ya wanna finish the date in private?"

                $ second_event[Player] = "end"
    else:
        if Rogue in second_event.keys():
            if second_event[Rogue] == "dinner":
                call Rogue_date_dinner from _call_Rogue_date_dinner_3
            elif second_event[Rogue] == "movie":
                call Rogue_date_movie from _call_Rogue_date_movie_3
            elif second_event[Rogue] == "mall":
                call Rogue_date_mall from _call_Rogue_date_mall_1
            elif second_event[Rogue] == "end":
                $ Rogue.change_face("sexy", eyes = "right") 

                pause 1.0

                $ Rogue.change_face("sexy", blush = 1)

                ch_Rogue "Could we just head back. . . ?"

                $ Rogue.change_face("sexy", eyes = "right", blush = 1)

                ch_Player "Why?"

                if Rogue.status["horny"] or Rogue.status["nympho"]:
                    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
                    
                    ch_Rogue "Please, [Rogue.Player_petname]?" 
                    
                    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1) 
                    
                    pause 1.0 
                    
                    $ Rogue.change_face("sexy", blush = 1) 
                    
                    ch_Rogue "Ah'd really like to spend some time with you. . . alone." 
                    
                    $ Rogue.change_face("sexy", eyes = "right", blush = 1) 
                    
                    ch_Rogue "Some {i}special{/i} time with you. . . "
                else:
                    $ Rogue.change_face("sly") 
                    
                    ch_Rogue "Just want to spend some time with ya alone. . ."

    if Player.location != "bg_mall":
        $ fade_to_black(0.4)

        $ time_index = 3

        $ lighting = "night"

        call remove_Characters(location = "bg_mall") from _call_remove_Characters_152
        call set_the_scene(location = "bg_mall") from _call_set_the_scene_130
        call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_123

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "We ready to go, [Rogue.Player_petname]?"

    $ Rogue.change_face("smirk2", eyes = "left")

    ch_Player "Yep, c'mon, let's go."
    "You take her hand, and she follows you out of the mall."

    $ fade_to_black(0.4)

    "You walk back to the Institute together."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_153
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_157
    call send_Characters(Rogue, "bg_campus", behavior = "on_date") from _call_send_Characters_124

    "You continue to chat and enjoy each other's company as you head back into the dorms."

    if EventScheduler.Events["Rogue_I_love_you"].completed and not EventScheduler.Events["Rogue_first_sex"].completed:
        $ EventScheduler.Events["Rogue_first_sex"].start()
    else:
        call Rogue_date_end from _call_Rogue_date_end

    python:
        for C in Player.date_planned.keys():
            C.History.update("went_on_date_with_Player")

        for C in Partners:
            if C not in Player.date_planned.keys():
                for other_C in Player.date_planned.keys():
                    if not C.History.check("told_wants_multiple_partners") or other_C not in C.knows_about:
                        C.History.update("cheated_on_date")

                        if not Player.History.check(f"cheated_on_{C.tag}_with_{other_C.tag}_date", tracker = "recent"):
                            Player.History.update(f"cheated_on_{C.tag}_with_{other_C.tag}_date")

    $ Player.History.update("went_on_date")
    $ Player.date_planned = {}

    $ ongoing_Event = False

    $ clock = 0

    if Rogue.location == Player.location:
        jump go_to_sleep
    # else:
    #     call move_location(Player.location) from _call_move_location_25

    return

label Rogue_date_dinner:
    if second_event:
        if Rogue in second_event.keys():
            $ Rogue.change_face("smirk2", eyes = "right")

            pause 1.0

            $ Rogue.change_face("worried1", mouth = "lipbite")

            ch_Rogue "Ah'm real hungry."
            ch_Rogue "What about you?"
            ch_Player "Yeah, I could go for a bite to eat."

            $ Rogue.change_face("smirk2")

            ch_Rogue "Why don't we go grab some dinner?"

            $ Rogue.change_face("smirk2", eyes = "right")

            "She grabs your hand, and you head to the restaurant together."

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Rogue "Let's go to the steakhouse." 

                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "If that's alright with you."

                $ cuisine = "steakhouse"
            elif dice_roll == 2:
                ch_Rogue "Seafood's always a good choice." 
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "Ah've been cravin' it."

                $ cuisine = "seafood"
            elif dice_roll == 3:
                ch_Rogue "Ah've really wanted to go back to that Southern food place." 
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "Can't get enough of it. . ."

                $ cuisine = "southern"
        elif Player in second_event.keys():
            menu:
                "Let's grab dinner. . ."
                ". . . at the steakhouse.":
                    $ cuisine = "steakhouse"
                ". . . at the seafood restaurant.":
                    $ cuisine = "seafood"
                ". . . at the Southern food restaurant":
                    $ cuisine = "southern"

            $ Rogue.change_face("smirk2") 
            
            ch_Rogue "Sounds like a treat." 
            ch_Rogue "Ah'm starvin'."
    else:
        if Rogue in first_event.keys():
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Rogue "Let's go to the steakhouse." 

                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "If that's alright with you."

                $ cuisine = "steakhouse"
            elif dice_roll == 2:
                ch_Rogue "Seafood's always a good choice." 
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "Ah've been cravin' it."

                $ cuisine = "seafood"
            elif dice_roll == 3:
                ch_Rogue "Ah've really wanted to go back to that Southern food place." 
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "Can't get enough of it. . ."

                $ cuisine = "southern"
        elif Player in first_event.keys():
            $ Rogue.change_face("smirk2")

            ch_Rogue "Where are we eatin', [Rogue.Player_petname]?"

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Player "Were you in the mood for anything?"
            ch_Rogue "You know ah can't answer that fairly."
            ch_Rogue "Ah could always go for Southern food. . ."
            ch_Player "Then how about. . ."

            menu:
                extend ""
                "Let's go to that steakhouse.":
                    $ cuisine = "steakhouse"
                "How about seafood?":
                    $ cuisine = "seafood"
                "I'm in the mood for Southern food.":
                    $ cuisine = "southern"

            $ Rogue.change_face("smirk2")

            ch_Rogue "Works for me."

    $ eating_dinner = True
    $ ordered_food = True
    $ food_arrived = False
    $ drinking_wine = False

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_154
    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_158
    call send_Characters(Rogue, "bg_restaurant", behavior = "on_date") from _call_send_Characters_125

    "You get seated quickly, and the waitress hands out the menus."

    $ Rogue.change_face("smirk1", eyes = "down")

    $ ordered_food = False

    $ Player_picked_food = False

    if renpy.random.random() > 0.66:
        pause 1.0 

        $ Rogue.change_face("worried1", mouth = "lipbite")
        
        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp]. . ."
        ch_Rogue "What am ah eatin' today?"
        ch_Player "Why don't you get. . ."

        $ chosen_meal = {}
        $ restaurant_bill = {}

        call restaurant_menu(Rogue, cuisine) from _call_restaurant_menu_8

        ch_Player "And I'll get. . ."

        call restaurant_menu(Player, cuisine) from _call_restaurant_menu_9

        $ Player_picked_food = True
    else:
        "You decide to order. . ."

        $ chosen_meal = {}
        $ restaurant_bill = {}

        call restaurant_menu(Player, cuisine) from _call_restaurant_menu_10

    $ Rogue.change_face("smirk2")

    "You have a nice time chatting with [Rogue.name], as you wait for the waitress to come back and take your orders."

    if Rogue in Partners and renpy.random.random() > 0.75:
        "It's nice to see [Rogue.name] relax." 
        "Seems like it's easier for her whenever she's around you."

    $ Rogue.change_face("smirk2", eyes = "right")

    "The waitress finally comes back, and. . ."

    if Rogue not in chosen_meal.keys():
        if cuisine == "steakhouse":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.6:
                $ chosen_meal[Rogue] = "Chilean sea bass"
                $ restaurant_bill[Rogue] = 35
            elif dice_roll > 0.55*2/3 + 0.05:
                if renpy.random.random() > 0.5:
                    $ chosen_meal[Rogue] = "filet mignon"
                else:
                    $ chosen_meal[Rogue] = "ribeye"

                $ restaurant_bill[Rogue] = 45
            elif dice_roll > 0.55*1/3 + 0.05:
                $ chosen_meal[Rogue] = "penne alla vodka"
                $ restaurant_bill[Rogue] = 30
            elif dice_roll > 0.55*0/3 + 0.05:
                $ chosen_meal[Rogue] = "chicken parmesan"
                $ restaurant_bill[Rogue] = 25
            else:
                $ chosen_meal[Rogue] = "chopped salad"
                $ restaurant_bill[Rogue] = 15
        elif cuisine == "seafood":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.6:
                $ chosen_meal[Rogue] = "crab-stuffed sole"
                $ restaurant_bill[Rogue] = 35
            elif dice_roll > 0.55*2/3 + 0.05:
                $ chosen_meal[Rogue] = "lobster tails"
                $ restaurant_bill[Rogue] = 45
            elif dice_roll > 0.55*2/3 + 0.05:
                $ chosen_meal[Rogue] = "crab cakes"
                $ restaurant_bill[Rogue] = 30
            elif dice_roll > 0.55*0/3 + 0.05:
                $ chosen_meal[Rogue] = "salmon"
                $ restaurant_bill[Rogue] = 25
            else:
                $ chosen_meal[Rogue] = "garden salad"
                $ restaurant_bill[Rogue] = 15
        elif cuisine == "southern":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.6:
                $ chosen_meal[Rogue] = "fried chicken"
                $ restaurant_bill[Rogue] = 25
            elif dice_roll > 0.55*2/3 + 0.05:
                $ chosen_meal[Rogue] = "short ribs"
                $ restaurant_bill[Rogue] = 45
            elif dice_roll > 0.55*1/3 + 0.05:
                $ chosen_meal[Rogue] = "catfish"
                $ restaurant_bill[Rogue] = 35
            elif dice_roll > 0.55*0/3 + 0.05:
                $ chosen_meal[Rogue] = "jambalaya"
                $ restaurant_bill[Rogue] = 30
            else:
                $ chosen_meal[Rogue] = "salad"
                $ restaurant_bill[Rogue] = 15

    menu:
        extend ""
        "Order for [Rogue.name] (encourage_quirk)":
            if Rogue.ordered_for_last_time:
                $ Rogue.change_face("worried1", mouth = "lipbite")

                "[Rogue.name] holds her tongue, staring at you expectantly."

                $ temp = chosen_meal[Rogue]

                ch_Player "She'll have the [temp]."

                $ temp = chosen_meal[Player]

                if chosen_meal[Player] == chosen_meal[Rogue]:
                    ch_Player "And I'll also have the [temp]."
                else:
                    ch_Player "And I'll have the [temp]."
            else:
                ch_Rogue "Ah'll get th-"

                "You interrupt."

                $ Rogue.change_face("worried2")

                $ temp = chosen_meal[Rogue]

                ch_Player "She'll have the [temp]."

                $ Rogue.change_face("worried1", mouth = "lipbite")

                ch_Rogue "Sorry. . ."

                $ temp = chosen_meal[Player]

                if chosen_meal[Player] == chosen_meal[Rogue]:
                    ch_Player "And I'll also have the [temp]."
                else:
                    ch_Player "And I'll have the [temp]."

            $ Rogue.ordered_for_last_time = True

            $ Rogue.History.update("quirk_encouraged")
        "Only order for yourself (discourage_quirk)":
            if Rogue.ordered_for_last_time:
                $ Rogue.change_face("worried1", mouth = "lipbite")

                "[Rogue.name] holds her tongue, staring at you expectantly."
            
                $ temp = chosen_meal[Player]

                ch_Player "I'll have the [temp]."

                $ Rogue.change_face("worried1")

                "When you don't say anything else, she gets the hint."

                $ Rogue.change_face("worried1", eyes = "right")

                $ temp = chosen_meal[Rogue]

                if chosen_meal[Player] == chosen_meal[Rogue]:
                    ch_Rogue "And ah'll also get the [temp]."
                else:
                    ch_Rogue "And ah'll get the [temp]."
            else:
                $ Rogue.change_face("worried1", eyes = "right")

                $ temp = chosen_meal[Rogue]

                ch_Rogue "Ah'll get the [temp]."

                $ temp = chosen_meal[Player]

                if chosen_meal[Player] == chosen_meal[Rogue]:
                    ch_Player "And I'll also have the [temp]."
                else:
                    ch_Player "And I'll have the [temp]."

                $ Rogue.change_face("worried1", mouth = "lipbite")

            $ Rogue.ordered_for_last_time = False

            $ Rogue.History.update("quirk_discouraged")

    if chosen_meal[Rogue] in ["filet mignon", "ribeye"]:
        $ Rogue.change_face("worried1", eyes = "right") 
        
        ch_Rogue "Ah'd like it medium rare, please." 
        
        $ Rogue.change_face("worried1", mouth = "smirk") 
        
        ch_Rogue "Just the right amount of pink. . ."

    $ ordered_food = True

    $ Rogue.change_face("smirk2")

    "The waitress walks away, leaving the two of you alone again."

    $ lines = {
        "a": "You have great taste in music, any recommendations?",
        "b": "You look {i}great{/i} today, as always.",
        "c": "Love the outfit.",
        "d": "Those bottoms make your ass look fantastic.",
        "k": "You always smell so good."}

    $ indices = list(lines.keys())

    $ renpy.random.shuffle(indices)

    $ first_compliment = lines[indices[0]]
    $ second_compliment = lines[indices[1]]
    $ third_compliment = lines[indices[2]]

    menu:
        extend ""
        "[first_compliment]":
            call expression f"Rogue_flirt_a{indices[0]}" from _call_expression_27
        "[second_compliment]":
            call expression f"Rogue_flirt_a{indices[1]}" from _call_expression_28
        "[third_compliment]":
            call expression f"Rogue_flirt_a{indices[2]}" from _call_expression_29

    $ Rogue.change_face("smirk2", blush = 1)

    "You continue to have a nice conversation, as you wait for the food to arrive."

    $ Rogue.change_face("worried1", mouth = "smirk")

    "You learn a lot about each other, your lives before the Institute, and your dreams for the future."
    "Although, [Rogue.name] still is and has always been quite guarded about her past."

    pause 1.0

    $ fade_to_black(0.4)

    $ food_arrived = True

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("smirk2", eyes = "right")

    "The waitress finally comes back with your orders."
    ch_Rogue "Thanks darlin'."

    $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite")

    if Rogue.quirk:
        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp]. . . am ah allowed to start eatin'?"

        menu:
            extend ""
            "Yes, you can eat.":
                pass
            "No, not yet.":
                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

                "You dig into the meal, as [Rogue.name] watches on, obediently waiting for you to say the word."
                "After a minute. . ."

                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

                ch_Player "Alright, you can eat."
                ch_Rogue "Thank you."

    $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite")

    "[Rogue.name] digs right in."

    if Player_picked_food and chosen_meal[Rogue] in ["Chilean sea bass", "crab-stuffed sole", "fried chicken"]:
        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Rogue "Thanks for choosin' this for me."
        ch_Rogue "It's darn good."

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_525

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Is yer food good too?"

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Player "Yeah, it's great!"
    elif not Player_picked_food and chosen_meal[Rogue] not in ["Chilean sea bass", "crab-stuffed sole", "fried chicken"] and chosen_meal[Player] in ["Chilean sea bass", "crab-stuffed sole", "fried chicken"]:
        $ Rogue.change_face("worried1", eyes = "squint", mouth = "lipbite", blush = 1)
        
        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp]. . ."
        ch_Rogue "Yer food looks real good."

        $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Rogue "Maybe ah could get a bite of it?"

        menu:
            extend ""
            "Give her a bite":
                "You cut her a piece, and she eats it directly off of your fork." 

                $ Rogue.change_face("neutral", eyes = "down", mouth = "open")

                pause 1.0

                $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

                ch_Rogue "Delicious, thank you."

                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_526
            "Don't give her a bite":
                $ Rogue.change_face("worried1") 

                ch_Rogue "Don't worry none." 

                $ Rogue.change_face("worried1", mouth = "smirk") 

                ch_Rogue "My food's good too."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue
                
            call Rogue_date_dinner_sex from _call_Rogue_date_dinner_sex
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_dinner_sex from _call_Rogue_date_dinner_sex_1
                "Just finish the meal normally":
                    pass

    $ Rogue.change_face("smirk1", eyes = "right")

    "You finish eating, and the waitress comes by with the check."

    $ Rogue.change_face("worried1", mouth = "smirk") 

    menu:
        "Offer to pay":
            if "Player_initiated" in Player.date_planned[Rogue]:
                $ Rogue.change_face("worried2")

                ch_Player "I'll cover it."
                ch_Rogue "Are ya sure?"

                $ Rogue.change_face("worried1") 

                ch_Rogue "Ah don't mind payin'."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Player "Don't worry, I got it."
                ch_Rogue "Thank you."

                $ Rogue.change_face("smirk2", blush = 1)

                if Player.cash >= restaurant_bill[Player] + restaurant_bill[Rogue]:
                    "You pay the bill and head back into the mall." 
                    
                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_527

                    $ Player.cash -= restaurant_bill[Player] + restaurant_bill[Rogue]
                else:
                    "You realize you don't have enough money. . ." 
                    
                    $ Rogue.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Rogue.change_face("worried1", mouth = "smirk") 
                    
                    ch_Rogue "Why didn't ya just say somethin'?" 
                    "[Rogue.name] pays the difference." 
                    
                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_528

                    $ Player.cash = 0
            else:
                $ Rogue.change_face("confused1")

                ch_Rogue "Ain't no way ah'm lettin' you pay."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Rogue "Ah asked ya in the first place."
                ch_Player "Thanks, [Rogue.petname]. . ."

                $ Rogue.change_face("smirk2", blush = 1)

                ch_Rogue "Yer welcome, [Rogue.Player_petname]."

                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_529

                "[Rogue.name] pays the bill, and you both head back into the mall."
        "Recommend splitting the check":
            if "Player_initiated" in Player.date_planned[Rogue]:
                $ Rogue.change_face("confused1", mouth = "smirk")

                ch_Player "Why don't we split the bill?"

                $ Rogue.change_face("smirk2")

                ch_Rogue "Sure, if ya want."

                if Player.cash >= math.ceil((restaurant_bill[Player] + restaurant_bill[Rogue])/2):
                    "You both pay the bill and head back into the mall."

                    $ Player.cash -= math.ceil((restaurant_bill[Player] + restaurant_bill[Rogue])/2)
                else:
                    "You realize you don't have enough money to pay for half. . ." 
                    
                    $ Rogue.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Rogue.change_face("worried1", mouth = "smirk") 
                    
                    ch_Rogue "Why didn't ya just say somethin'?" 
                    "[Rogue.name] pays the difference." 
                    
                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_530

                    $ Player.cash = 0
            else:
                $ Rogue.change_face("confused1")

                ch_Rogue "Ain't no way ah'm lettin' you pay."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Rogue "Ah asked ya in the first place."
                ch_Player "Thanks, [Rogue.petname]. . ."

                $ Rogue.change_face("smirk2", blush = 1)

                ch_Rogue "Yer welcome, [Rogue.Player_petname]."
                "[Rogue.name] pays the bill, and you both head back into the mall."

                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_531

    return

label Rogue_date_dinner_sex:
    $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

    "You notice [Rogue.name] looking at you seductively."

    if sex_initiator == Player:
        menu:
            extend ""
            "Ask for a handjob under the table" if Rogue.History.check("handjob"):
                $ sex_act = "handjob"
            "Ask for a blowjob under the table" if Rogue.History.check("blowjob") and Rogue.History.check("swallow_cum"):
                $ sex_act = "blowjob"
            "Suggest a quickie in the bathroom" if Rogue.History.check("sex"):
                $ sex_act = "sex"
            "Ask to go down on her in the bathroom" if Rogue.History.check("eat_pussy"):
                $ sex_act = "eat_pussy"
            "Decide against it":
                return
    elif sex_initiator == Rogue:
        $ sex_acts = []

        if Rogue.History.check("handjob"):
            $ sex_acts.append("handjob")

        if Rogue.History.check("blowjob") and Rogue.History.check("swallow_cum"):
            $ sex_acts.append("blowjob")

        if Rogue.History.check("sex"):
            $ sex_acts.append("sex")

        if Rogue.History.check("eat_pussy"):
            $ sex_acts.append("eat_pussy")

        if sex_acts:
            if Rogue.quirk:
                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
                        
                $ temp = Rogue.Player_petname.capitalize()

                ch_Rogue "[temp], ah want to. . ."
                
                $ Rogue.change_face("sly", mouth = "lipbite", blush = 1) 
                
                ch_Rogue "Will ya let me make you feel {i}real{/i} good?"

            menu:
                extend ""
                "Go along with it":
                    $ sex_act = renpy.random.choice(sex_acts)
                "Not right now, [Rogue.petname].":
                    $ Rogue.change_face("worried1", blush = 1) 
                    
                    ch_Rogue "Alright, sorry. . ."

                    return

    call expression f"Rogue_date_dinner_sex_{sex_act}" from _call_expression_30

    return

label Rogue_date_dinner_sex_handjob:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1)

    call hide_Character(Rogue) from _call_hide_Character_20

    "After making sure nobody is paying attention, she slips out of sight."

    if sex_initiator == Rogue:
        if Rogue.petname not in ["Anna Marie"]:
            $ temp = Rogue.petname.capitalize()
        else:
            $ temp = Rogue.petname

        ch_Player "[temp], what exactly did you have in mind. . . ?"

    "Thanks to the long table cloth, even if someone was looking, they wouldn't be able to see anything."
    "You can feel her tease you for a while, before pulling your pants down."
    "She continues to tease, making sure you're good and hard."
    "After she's satisfied, she gets to work, wrapping her fingers around you."
    "You continue to eat your meal as nonchalantly as possible, meanwhile [Rogue.name] starts picking up the pace."

    if Rogue.History.check("handjob") >= 11:
        "Her attentiveness has paid off, and she knows exactly where to touch and how much pressure is required to bring you to the edge faster than ever."
    elif Rogue.History.check("handjob") >= 5:
        "She still fumbles around a bit, but has been very attentive, quickly learning what works and what doesn't." 
        "With just a bit of work, you're already about to blow."
    else:
        "She's still not quite used to touching you down there and has a bit of a death grip." 
        "Regardless, her enthusiasm brings you to the edge all the same."

    $ Player.desire = 75

    "[Rogue.name] can tell you're getting close and maintains the pace."
    "You hear her stifling moans, as it seems she's touching herself as well."

    $ Player.desire = 90

    "Finally, she speeds things up, and you can't hold it in any longer. . ."
    "She can't either."
    ". . ." with small_screenshake

    $ Player.desire = 0

    ch_Rogue "Mmm. . ."

    if Rogue.History.check("swallow_cum"):
        "You feel her lips wrap around your cock right as you cum." 
        ch_Rogue "*gulp*" 
        "She makes sure to swallow it all and licks you clean afterwards."

        $ Rogue.History.update("swallow_cum")
    else:
        "She takes a napkin and cleans everything up after you're done."

        $ Rogue.History.update("clean_cum")

    "She puts your pants back into position, before getting up."

    if Rogue.History.check("swallow_cum", tracker = "recent") and renpy.random.random() > 0.5:
        $ Rogue.spunk["chin"] = True

    call add_Characters(Rogue) from _call_add_Characters_91

    $ Rogue.change_face("sexy", blush = 2)

    if Rogue.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Rogue) from _call_swallow_cum_8

        $ Rogue.change_face("sly", blush = 2)

        ch_Rogue "*gulp*"

    ch_Rogue "Did ya enjoy that as much as ah did?"

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_532
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_533

    return

label Rogue_date_dinner_sex_blowjob:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1)

    call hide_Character(Rogue) from _call_hide_Character_21

    "After making sure nobody is paying attention, [Rogue.name] slips out of sight."

    if sex_initiator == Rogue:
        if Rogue.petname not in ["Anna Marie"]:
            $ temp = Rogue.petname.capitalize()
        else:
            $ temp = Rogue.petname

        ch_Player "[temp], what exactly did you have in mind. . . ?"

    "Thanks to the long table cloth, even if someone was looking, they wouldn't be able to see anything."
    "You can feel her tease you for a while, before pulling your pants down."
    "She gets right to work, wrapping her lips around you."
    "You continue to eat your meal as nonchalantly as possible, meanwhile [Rogue.name] starts picking up the pace."

    if Rogue.History.check("blowjob") >= 11:
        "Her attentiveness has been paying off, as she knows exactly how you like it and brings you to the edge in record time."
    elif Rogue.History.check("blowjob") >= 5:
        "She still fumbles around a bit, but is very attentive and is quickly learning what gets you off." 
        "You're about to blow already."
    else:
        "She's still not used to touching you down there, let alone blowing you, and she fumbles around quite a bit." 
        "Despite her lack of experience, she does her best to get you off, and you're brought to the edge all the same."

    $ Player.desire = 75

    "[Rogue.name] can tell you're close and starts speeding up."
    "She starts moaning around your cock, apparently getting off to this just as much as you are."

    $ Player.desire = 90

    "Finally, you can't hold on any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0

    ch_Rogue "*slurp*"
    "You put a hand on the back of her head, pushing her down as you cum."
    "She moans and pushes down as well, trying to take your cum as deep as she can handle."
    ch_Rogue "*gulp*"
    "[Rogue.name] keeps sucking, trying to squeeze out every last drop."
    "You twitch involuntarily until she's finally satisfied."
    "She dutifully licks you clean, before putting your pants back into position."

    if renpy.random.random() > 0.5:
        $ Rogue.spunk["chin"] = True

    call add_Characters(Rogue) from _call_add_Characters_92

    $ Rogue.change_face("sexy", blush = 2)

    if Rogue.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Rogue) from _call_swallow_cum_9

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "*gulp*"

    ch_Rogue "Thanks for lettin' me. . ."
    ch_Rogue "Ah really love the way you taste." 

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_534
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_535

    $ Rogue.History.update("swallow_cum")

    return

label Rogue_date_dinner_sex_sex:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ya wanna have some fun. . . ?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Follow me."

    call hide_Character(Rogue) from _call_hide_Character_22

    "[Rogue.name] heads to the bathroom and, after a minute, you follow after her."

    $ fade_to_black(0.4)

    "You see her waiting for you outside the bathroom, and you both head inside together."

    call set_the_scene(location = "bg_restaurant_bathroom") from _call_set_the_scene_159
    call send_Characters(Rogue, "bg_restaurant_bathroom", behavior = "on_date") from _call_send_Characters_128

    "Good thing it's a private one."
    "She locks the door behind you."
        
    if sex_initiator == Rogue:
        $ has_Action_control = False
        $ has_position_control = False
        $ has_movement_control = False

    $ Rogue.available_Actions = ["sex"]

    if Rogue.History.check("anal"):
        $ Rogue.available_Actions.append("anal")

    $ Rogue.available_poses = ["missionary"]

    if Rogue.History.check("doggy"):
        $ Rogue.available_poses.append("doggy")

    $ chosen_Action = renpy.random.choice(Rogue.available_Actions)
    $ chosen_pose = renpy.random.choice(Rogue.available_poses)

    $ Rogue.History.update("hookup")
        
    $ Rogue.History.update(chosen_Action)
    
    call request_position(Rogue, chosen_pose, automatic = True) from _call_request_position_15

    $ Action = ActionClass(chosen_Action, Player, Rogue)

    call undress(Rogue, "underwear") from _call_undress_21
    call start_Action(Action) from _call_start_Action_10
    call screen Action_screen(automatic = True)
    
    $ choice_disabled = False

    # if renpy.random.random() > 0.5:
    #     call try_on(Rogue, Rogue.Wardrobe.Clothes["messy hair"])

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_54
    
    $ locations = list(Rogue.spunk.keys())

    while locations:
        if Rogue.spunk[locations[0]]:
            call clean_cum(Rogue) from _call_clean_cum_6

        $ locations.remove(locations[0])

    "After you both put your clothes back on, [Rogue.name] leaves and heads back to the table."

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_155
    call send_Characters(Rogue, "bg_restaurant", behavior = "on_date") from _call_send_Characters_129
    
    "You wait a minute before leaving the bathroom as well."

    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_160

    $ Rogue.change_face("sly", blush = 2)
    
    pause 1.0

    if Rogue.Clothes["hair"].string == "messy":
        ch_Player "Your hair's a bit. . ."

        $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

        "She straightens it out."

        call try_on(Rogue, Rogue.Wardrobe.Clothes["straight hair"]) from _call_try_on_8

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Ah hope that was as good for you as it was for me. . ."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_536
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_537

    $ Rogue.available_Actions = []
    $ Rogue.available_poses = []

    return

label Rogue_date_dinner_sex_eat_pussy:
    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ya wanna have some fun. . . ?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Follow me."

    call hide_Character(Rogue) from _call_hide_Character_23

    "[Rogue.name] heads to the bathroom and, after a minute, you follow after her."

    $ fade_to_black(0.4)

    "You see her waiting for you outside the bathroom, and you both head inside together."

    call set_the_scene(location = "bg_restaurant_bathroom") from _call_set_the_scene_161
    call send_Characters(Rogue, "bg_restaurant_bathroom", behavior = "on_date") from _call_send_Characters_130

    "Good thing it's a private one."
    "She locks the door behind you."
        
    $ has_movement_control = False

    $ Rogue.available_Actions = ["eat_pussy"]
    $ Rogue.available_poses = ["masturbation"]

    $ chosen_Action = renpy.random.choice(Rogue.available_Actions)
    $ chosen_pose = renpy.random.choice(Rogue.available_poses)

    $ Rogue.History.update("hookup")
        
    $ Rogue.History.update(chosen_Action)
    
    call request_position(Rogue, chosen_pose, automatic = True) from _call_request_position_16

    $ Action = ActionClass(chosen_Action, Player, Rogue)

    call undress(Rogue, "underwear") from _call_undress_22
    call start_Action(Action) from _call_start_Action_11
    call screen Action_screen(automatic = True)
    
    $ choice_disabled = False

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_55

    "After you both put your clothes back on, [Rogue.name] leaves and heads back to the table."

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_156
    call send_Characters(Rogue, "bg_restaurant", behavior = "on_date") from _call_send_Characters_131

    "You wait a minute before leaving the bathroom as well."

    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_162

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Ah hope that was as good for you as it was for me. . ."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_538
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_539

    $ Rogue.available_Actions = []
    $ Rogue.available_poses = []

    return

label Rogue_date_movie:
    if second_event:
        if Rogue in second_event.keys():
            $ Rogue.change_face("smirk2", eyes = "right") 

            ch_Rogue "Ah was wonderin' if ya wanted to go see a movie?"

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Rogue "There are some real good ones out right now."
            ch_Player "Yeah, I wouldn't mind catching one."

            $ Rogue.change_face("happy")

            ch_Rogue "Sweet."

            $ Rogue.change_face("smirk2", eyes = "right")

            "She grabs your hand, and you head to the theater together."

    if Player.location != "bg_mall":
        call remove_Characters(location = "bg_mall") from _call_remove_Characters_157
        call set_the_scene(location = "bg_mall") from _call_set_the_scene_163
        call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_132

    $ chosen_movie = None

    if "Girl_initiated" in Player.date_planned[Rogue]:
        if renpy.random.random() > 0.75:
            if dice_roll > 0.50:
                $ chosen_movie = 3
            elif dice_roll > 0.25:
                $ chosen_movie = 1
            else:
                $ chosen_movie = 2
    elif "Player_initiated" in Player.date_planned[Rogue]:
        if renpy.random.random() > 0.75:
            if dice_roll > 0.50:
                $ chosen_movie = 3
            elif dice_roll > 0.25:
                $ chosen_movie = 1
            else:
                $ chosen_movie = 2

    $ movie1_titles = {
        "ron_bic1": ["Ron Bic I (Action)", 20],
        "hamburg_portfolio": ["The Hamburg Portfolio (Action)", 20]}

    if Player.History.update("seen_Ron_Bic_I"):
        $ movie1_titles.update({"ron_bic2": ["Ron Bic II (Action)", 20]})
    
    $ indices1 = list(movie1_titles.keys())
    $ renpy.random.shuffle(indices1)
    $ movie1_title = movie1_titles[indices1[0]][0]
    $ movie1_ticket_price = movie1_titles[indices1[0]][1]

    $ movie2_titles = {
        "beautiful_flower": ["Entering Her Beautiful Flower (Wholesome Romance)", 20],
        "fated": ["Fated to Be Together (Explicit Romance)", 20],
        "refilling_empty_glass": ["Refilling an Empty Glass (Explicit Romance)", 20]}

    $ indices2 = list(movie2_titles.keys())
    $ renpy.random.shuffle(indices2)
    $ movie2_title = movie2_titles[indices2[0]][0]
    $ movie2_ticket_price = movie2_titles[indices2[0]][1]

    $ movie3_titles = {
        "stale_air": ["Stale Air, Bright Ideas (Thriller)", 20],
        "devils_spring_break": ["The Devil's Spring Break (Cheesy Horror)", 20],
        "unsanctioned_crusade": ["The Unsanctioned Crusade (Horror)", 20]}

    $ indices3 = list(movie3_titles.keys())
    $ renpy.random.shuffle(indices3)
    $ movie3_title = movie3_titles[indices3[0]][0]
    $ movie3_ticket_price = movie3_titles[indices3[0]][1]
    
    if chosen_movie:
        $ Rogue.change_face("smirk2", eyes = "right")

        "You arrive at the ticket counter, and [Rogue.name] looks over all the available movies."

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Could ah pick the movie this time?"

        $ Rogue.change_face("smirk2")

        ch_Player "Sure."

        if chosen_movie == 1:
            $ movie_choice = indices1[0]
            $ movie_title = movie1_title
            $ ticket_price = movie1_ticket_price
        elif chosen_movie == 2:
            $ movie_choice = indices2[0]
            $ movie_title = movie2_title
            $ ticket_price = movie2_ticket_price
        elif chosen_movie == 3:
            $ movie_choice = indices3[0]
            $ movie_title = movie3_title
            $ ticket_price = movie3_ticket_price

        $ temp = movie_title.split(" (")

        "She points to [temp[0]]."
        ch_Rogue "How 'bout we see this one."
    else:
        $ Rogue.change_face("smirk2", eyes = "right")

        "You arrive at the ticket counter, and [Rogue.name] looks over all the available movies."

        $ Rogue.change_face("worried1", eyes = "right")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Which one are we seein', [Rogue.Player_petname]?"

        menu:
            extend ""
            "[movie1_title] ($[movie1_ticket_price])":
                $ movie_choice = indices1[0]
                $ movie_title = movie1_title
                $ ticket_price = movie1_ticket_price
            "[movie2_title] ($[movie2_ticket_price])":
                $ movie_choice = indices2[0]
                $ movie_title = movie2_title
                $ ticket_price = movie2_ticket_price
            "[movie3_title] ($[movie3_ticket_price])":
                $ movie_choice = indices3[0]
                $ movie_title = movie3_title
                $ ticket_price = movie3_ticket_price

        $ Rogue.change_face("confused1", mouth = "smirk", eyes = "right")

        ch_Rogue "That one sounds interestin'."

        $ Rogue.change_face("smirk2")

    menu:
        extend ""
        "Offer to pay":
            if "Player_initiated" in Player.date_planned[Rogue]:
                $ Rogue.change_face("worried2")

                ch_Player "I'll cover it."
                ch_Rogue "Are ya sure?"

                $ Rogue.change_face("worried1") 

                ch_Rogue "Ah don't mind payin'."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Player "Don't worry, I got it."
                ch_Rogue "Thank you."

                $ Rogue.change_face("smirk2", blush = 1)

                if Player.cash >= 2*ticket_price:
                    "You pay for the tickets." 
                    
                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_540

                    $ Player.cash -= 2*ticket_price
                else:
                    "You realize you don't have enough money. . ." 
                    
                    $ Rogue.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Rogue.change_face("worried1", mouth = "smirk") 
                    
                    ch_Rogue "Why didn't ya just say somethin'?" 
                    "[Rogue.name] pays the difference." 
                    
                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_541

                    $ Player.cash = 0
            else:
                $ Rogue.change_face("confused1")

                ch_Rogue "Ain't no way ah'm lettin' you pay."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Rogue "Ah asked ya in the first place."
                ch_Player "Thanks, [Rogue.petname]. . ."

                $ Rogue.change_face("smirk2", blush = 1)

                ch_Rogue "Yer welcome, [Rogue.Player_petname]."
                "[Rogue.name] pays for the tickets."

                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_542
        "Recommend splitting the ticket price":
            if "Player_initiated" in Player.date_planned[Rogue]:
                $ Rogue.change_face("confused1", mouth = "smirk")

                ch_Player "Why don't we split the bill?"

                $ Rogue.change_face("smirk2")

                ch_Rogue "Sure, if ya want."

                if Player.cash >= ticket_price:
                    "You both pay for the tickets."

                    $ Player.cash -= ticket_price
                else:
                    "You realize you don't have enough money to pay for half. . ." 
                    
                    $ Rogue.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Rogue.change_face("worried1", mouth = "smirk") 
                    
                    ch_Rogue "Why didn't ya just say somethin'?" 
                    "[Rogue.name] pays the difference." 
                    
                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_543

                    $ Player.cash = 0
            else:
                $ Rogue.change_face("confused1")

                ch_Rogue "Ain't no way ah'm lettin' you pay."

                $ Rogue.change_face("worried1", mouth = "smirk")

                ch_Rogue "Ah asked ya in the first place."
                ch_Player "Thanks, [Rogue.petname]. . ."

                $ Rogue.change_face("smirk2", blush = 1)

                ch_Rogue "Yer welcome, [Rogue.Player_petname]."
                "[Rogue.name] pays for the tickets."

                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_544

    call remove_Characters(location = "bg_movies") from _call_remove_Characters_158
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_164
    call send_Characters(Rogue, "bg_movies", behavior = "on_date") from _call_send_Characters_133

    call expression f"Rogue_date_movie_{movie_choice}" from _call_expression_31

    "With the movie over, you get up and leave the theater."

    return

label Rogue_date_movie_ron_bic1:
    "You quickly find your seats, and the movie starts shortly after."
    "[Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("surprised1", eyes = "right")

    "Once the action starts, you look over to see [Rogue.name] entranced by all the action on screen."
    "Ron Bic is in a sticky situation after he's unwittingly sent to kill the CEO of his favorite lighter company."
    "Ron quickly realizes a rival lighter company set him up, and he vows to get revenge."

    $ Rogue.change_face("worried1", eyes = "right")

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_1
                "Just finish watching the movie":
                    pass

    "The movie continues, as Ron kills legions of men in the pursuit of revenge."
    "He has to fight his way through hundreds of evil henchmen in a lighter factory and finally takes out the real bad guy in the end."
    "There's a plethora of violent and fiery deaths as well as some impressive choreography."

    $ Rogue.change_face("smirk2", eyes = "right")

    ch_Rogue "That was fun. . ."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Makes me wanna see the sequel."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_545
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_546

    return

label Rogue_date_movie_ron_bic2:
    $ Rogue.change_face("pleased1")

    ch_Rogue "Ah've been lookin' forward to this one. . ."
    "You get seated just in time."
    "[Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("smirk2", eyes = "right")

    "After the events of the first movie, things are more dangerous than ever for our hero, Ron Bic."
    "The world's lighter making companies have been reeling from the deaths of so many important executives."
    "And they want to know who's responsible."

    $ Rogue.change_face("worried1", eyes = "right")

    "Poor Ron can't seem to avoid trouble, as he has to kill dozens of people in an attempt to prevent everyone from learning of his terrible mistake. . ."
    "You look over to see [Rogue.name] looking quite worried about Ron's predicament."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_2
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_3
                "Just finish watching the movie":
                    pass

    $ Rogue.change_face("confused1", eyes = "right")

    "The movie continues and, unfortunately, Ron isn't fast enough, and the information gets out."

    $ Rogue.change_face("angry1", eyes = "right")

    "Once the world knows that Ron killed the CEO of an allied lighter company, even if it was an accident, everyone he knows and loves turns on him."

    $ Rogue.change_face("smirk2", eyes = "right")

    "In the end, after a crescendo of blood, gore, and fiery death, Ron Bic is able to clear his name. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    "But, did he survive? Does he even know of his own success?"

    $ Rogue.change_face("furious", eyes = "right")

    ch_Rogue "Ah really ain't a fan of cliffhangers."

    $ Rogue.change_face("angry1")

    ch_Rogue "Also that whole misinformation thing rubs me the wrong way."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_547
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_548

    return

label Rogue_date_movie_hamburg_portfolio:
    "The previews are already over by the time you reach your seats."
    "[Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("smirk2", eyes = "right")

    "The movie is set in modern day Philadelphia, only. . . magic is real."

    $ Rogue.change_face("worried1", mouth = "smirk", eyes = "right")

    "The main character is a wizard, but the world doesn't know about all things supernatural, so he has to lay low."
    "He tries to be a good person and help people with his gift, but it's never that easy."
    "It seems like whoever wrote the movie absolutely despises the main character, because they keep putting him in horrible situations and giving him insane amounts of trauma."

    $ Rogue.change_face("worried1", eyes = "right")

    "Although, it is quite entertaining, as he uses his considerable talent with magic to kill his enemies in very creative ways."

    $ Rogue.change_face("smirk2", eyes = "right")

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_4
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_5
                "Just finish watching the movie":
                    pass

    $ Rogue.change_face("confused1", eyes = "right")

    "As the movie continues, the main character is forced to confront his morality."
    "If he wants to save the people he loves, innocent people must die."

    $ Rogue.change_face("angry1", eyes = "right")

    pause 1.0

    $ Rogue.change_face("worried1")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right")

    "[Rogue.name] glances at you a few times, as she watches the main character struggle so much with himself."
    "In the end, he isn't able to put aside his morals, and his inaction causes everyone to suffer."

    $ Rogue.change_face("angry1", eyes = "right")

    "At least he survives and gets revenge. . . however hollow it is. . ."

    $ Rogue.change_face("angry1")

    ch_Rogue "If it came down to it. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah wouldn't hesitate to save you."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_549
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_550

    return

label Rogue_date_movie_beautiful_flower:
    "You quickly find your seats."
    "[Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("smirk2", eyes = "right")

    "The movie is about a man who wanted to buy his mom some nice flowers for Mother's day."
    "He does this every year, but this time all the local florists are sold out."

    $ Rogue.change_face("worried1", eyes = "right")

    "He's running around frantically trying to find flowers to buy because his mother is very ill."
    "This might be his last chance, ever, to give her flowers."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_6
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_7
                "Just finish watching the movie":
                    pass

    $ Rogue.change_face("worried2", eyes = "right")

    "The movie continues and, as it turns out, the female lead only recently opened her own florist and has had trouble finding customers."
    "The guy has almost given up when he finally reaches her small hidden shop."
    "The shop's name is 'Beautiful flower.'"

    $ Rogue.change_face("pleased2", eyes = "right")

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Ah do like happy endings. . ."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_551

    return

label Rogue_date_movie_fated:
    "You get seated and [Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("confused1", mouth = "smirk", eyes = "right")

    "The movie starts out as a simple romance between two coworkers."
    "Admiring each other from a distance, they never interacted much at work."
    "That is until they were unwittingly set up on a blind date with each other."

    $ Rogue.change_face("smirk2", eyes = "right")

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_8
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_9
                "Just finish watching the movie":
                    pass

    $ Rogue.change_face("confused1", eyes = "right")

    "As the movie continues, it quickly takes a turn away from the wholesome, as the two mutually agree not to start a relationship."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", eyes = "right", blush = 1)

    "Instead the two become friends with benefits, ending the night with a very graphic sex scene."

    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_552 

    "There are many, very graphic sex scenes, as the two continue denying their romantic feelings for each other."
    "Eventually they do officially get together, and the movie ends."

    $ Rogue.change_face("sexy", blush = 2)

    ch_Rogue "That was. . ."

    $ Rogue.change_face("sexy", eyes = "right", blush = 2)

    ch_Rogue ". . . interestin'."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_553
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_554

    return

label Rogue_date_movie_refilling_empty_glass:
    "You get seated and [Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("smirk1", eyes = "right")

    "It begins following a bartender at a popular spot in the city."

    $ Rogue.change_face("confused1", eyes = "right") 

    "The bartender is good at her job and beautiful, so plenty of male customers try flirting with her to no avail."

    $ Rogue.change_face("worried1", eyes = "right") 

    "She was recently widowed." 
    "She's been struggling to move on from her husband's death, until one night she spots a despondent man sitting at the far end of the bar."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_10
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_11
                "Just finish watching the movie":
                    pass

    "The movie continues, and the bartender becomes interested in the despondent man, since he looks similar to her late husband."

    $ Rogue.change_face("surprised1", eyes = "right") 

    "He tells her about his plight, how a former business partner started a conspiracy against him and it's ruining his life."

    $ Rogue.change_face("pleased2", eyes = "right", blush = 2)

    "The chance meeting turns into a thrilling romance as they rapidly fall in love, and the bartender uses her skills as a former super spy to stop the conspiracy."

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 2)

    "Nearly every other minute there's a graphic sex scene as the bartender demonstrates her prowess to her new beau."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah like how they wrote the female lead."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "She was real hot. . ."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_555
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_556

    return

label Rogue_date_movie_stale_air:
    "The movie starts only a few minutes after you get seated, and [Rogue.name] starts holding your hand."

    $ Rogue.change_face("smirk1", eyes = "right")

    "The story is about a struggling writer who can't find any passion or inspiration for his stories."

    $ Rogue.change_face("confused1", eyes = "right")

    "The writer's monotonous life goes on as normal until he starts finding messages and sticky notes appearing out of nowhere around his apartment."

    $ Rogue.change_face("surprised1", eyes = "right")

    "He has no idea where they're coming from, but they all have great ideas which he uses to jumpstart his writing."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_12
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_13
                "Just finish watching the movie":
                    pass

    "As the movie continues, it quickly becomes clear what's going on."
    "Unbeknownst to the writer, a carbon monoxide leak in his apartment is simultaneously poisoning him, while also the cause for his inspiration."

    $ Rogue.change_face("worried1", eyes = "right")

    "His imaginative writing lands him a new job, but the gas also starts causing him to become delusional."

    $ Rogue.change_face("surprised1", eyes = "right")

    "The movie climaxes as the writer unknowingly acts out his latest story. . ."
    "Which is about a disturbed maniac who goes on a murder spree at their new job."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah really enjoyed that."
    ch_Rogue "Had an interestin' premise."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_557
    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_558

    return

label Rogue_date_movie_devils_spring_break:
    "You take your seats, and [Rogue.name] holds your hand as the movie starts."

    $ Rogue.change_face("confused1", eyes = "right")

    "The movie seems to follow a generic horror movie formula, with reckless college kids and everything."

    $ Rogue.change_face("neutral", eyes = "right")

    "One of the college students has a rich family, and they just bought a new summer home, one that of course is rumored to be haunted."
    "The rich kid brings a bunch of his friends down to the house, to spend their spring break getting drunk and partying."

    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    ch_Rogue "Ain't this one predictable. . ."
    "Despite the rumors, the house isn't actually haunted. . . at least not by ghosts."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_14
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_15
                "Just finish watching the movie":
                    pass

    $ Rogue.change_face("surprised1", eyes = "right")

    "As the movie continues, the college students are slowly and gruesomely killed by a demon, their souls stolen in the process."

    $ Rogue.change_face("worried1", eyes = "right")

    "They try to put up a fight, after they sober up enough to realize how fucked they are."
    "During one particularly tense moment, you look over and see [Rogue.name] wide-eyed, staring at the screen in suspense."

    $ Rogue.change_face("worried3", eyes = "right")

    "Suddenly, there's a jumpscare, and she squeezes your hand, leaning into you for comfort."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "You could tell they wanted us to root for the demon."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Was still pretty entertainin''."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_559

    return

label Rogue_date_movie_unsanctioned_crusade:
    "You take your seats just as the final preview ends."
    "[Rogue.name] starts holding your hand as the movie starts."

    $ Rogue.change_face("surprised1", eyes = "right")

    "The movie starts on a high note, as it instantly earns its 'R' rating."

    $ Rogue.change_face("worried1", eyes = "right")

    "It's set in medieval Europe and starts with a massacre."
    "Although, despite being bloody, the massacre is rather mundane, as it was perpetrated by an order of deeply religious knights."

    $ Rogue.change_face("confused1", eyes = "right") 

    "The knights are on their own form of crusade, driven by deep seated religious beliefs."
    "They do terrible things in a misguided attempt at worship."
    "Only, God is real and is less than pleased by these atrocities."

    if Player.stamina and Rogue.stamina:
        if (Rogue.status["horny"] or Rogue.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Rogue

            call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_16
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Rogue_date_movie_sex from _call_Rogue_date_movie_sex_17
                "Just finish watching the movie":
                    pass

    $ Rogue.change_face("worried1", eyes = "right")

    "As the movie continues, the knights are plagued by various, horrifying, heavenly tribulations."
    "It starts slowly at first, suspense building, as the knights are mercilessly terrorized."

    $ Rogue.change_face("angry1", eyes = "right")

    "The knights are directly confronted by the atrocities they themselves committed and systematically eradicated in cruel and disturbing fashion."

    $ Rogue.change_face("confused1")

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right")

    ch_Rogue "Ah reckon they got what they deserved. . ." 

    call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_560

    return

label Rogue_date_movie_sex:
    $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

    "You notice [Rogue.name] looking at you seductively."

    if sex_initiator == Player:
        menu:
            extend ""
            "Ask if she wants to make out" if Rogue.History.check("makeout"):
                $ sex_act = "makeout"
            "Ask for a handjob" if Rogue.History.check("handjob"):
                $ sex_act = "handjob"
            "Ask if you can put a hand down her pants" if Rogue.History.check("touch_pussy") and Rogue.History.check("seen_pussy"):
                $ sex_act = "touch_pussy"
            "Ask if you can finger her" if Rogue.History.check("finger_pussy"):
                $ sex_act = "finger_pussy"
            "Ask for a blowjob" if Rogue.History.check("blowjob") and Rogue.History.check("swallow_cum"):
                $ sex_act = "blowjob"
            "Decide against it":
                return
    elif sex_initiator == Rogue:
        $ sex_acts = []

        if Rogue.History.check("makeout"):
            $ sex_acts.append("makeout")

        if Rogue.History.check("handjob"):
            $ sex_acts.append("handjob")

        if Rogue.History.check("touch_pussy") and Rogue.History.check("seen_pussy"):
            $ sex_acts.append("touch_pussy")

        if Rogue.History.check("finger_pussy"):
            $ sex_acts.append("finger_pussy")

        if Rogue.History.check("blowjob") and Rogue.History.check("swallow_cum"):
            $ sex_acts.append("blowjob")

        if sex_acts:
            if Rogue.quirk:
                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 

                $ temp = Rogue.Player_petname.capitalize()

                ch_Rogue "[temp], ah want to. . ."
                
                $ Rogue.change_face("sly", mouth = "lipbite", blush = 1) 
                
                ch_Rogue "Will ya let me make you feel {i}real{/i} good?"

            menu:
                extend ""
                "Go along with it":
                    $ sex_act = renpy.random.choice(sex_acts)
                "Not right now, [Rogue.petname].":
                    $ Rogue.change_face("worried1", blush = 1) 
                    
                    ch_Rogue "Alright, sorry. . ."

                    return

    call expression f"Rogue_date_movie_sex_{sex_act}" from _call_expression_32

    return

label Rogue_date_movie_sex_makeout:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1) 

    "Once you're sure there's nobody around, you reach over and pull [Rogue.name] in."

    $ Rogue.change_face("kiss1", blush = 1)

    "The movie plays on in the background, as the two of you lock lips, your tongues dancing in each other's mouth."

    $ Rogue.change_face("kiss2", blush = 2)

    "You have one hand firmly around her neck, preventing her from going anywhere."
    "[Rogue.name] takes your other hand, running it across her body."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    "Before things go too far, you pull away."
    ch_Rogue "Mmm. . ."
    ch_Rogue "Wish ah could kiss ya forever."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_561
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_562

    return

label Rogue_date_movie_sex_handjob:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1)

    "Once [Rogue.name]'s sure there's nobody around, she reaches over."

    if sex_initiator == Rogue:
        if Rogue.petname not in ["Anna Marie"]:
            $ temp = Rogue.petname.capitalize()
        else:
            $ temp = Rogue.petname

        ch_Player "[temp], what exactly did you have in mind. . . ?"

    "She starts teasing you, making it quite difficult to focus on the movie."

    $ Rogue.change_face("sexy", eyes = "right", blush = 1)

    "Once you're hard, she takes your cock out, wrapping her fingers around you."
    "You try to continue watching the movie, but [Rogue.name] keeps speeding up."

    if Rogue.History.check("handjob") >= 11:
        "Her attentiveness has paid off, and she knows exactly where to touch and how much pressure is required to bring you to the edge faster than ever."
    elif Rogue.History.check("handjob") >= 5:
        "She still fumbles around a bit, but has been very attentive, quickly learning what works and what doesn't." 
        "With just a bit of work, you're already about to blow."
    else:
        "She's still not quite used to touching you down there and has a bit of a death grip." 
        "Regardless, her enthusiasm brings you to the edge all the same."

    "[Rogue.name] can tell you're getting close and maintains the pace."

    $ Player.desire = 75

    call expose(Rogue, "pussy") from _call_expose_6

    "You hear her stifling moans, as it seems she's touching herself as well."

    $ Player.desire = 90

    "Finally, she speeds things up, and you can't hold it in any longer. . ."
    "She can't either."
    ". . ." with small_screenshake

    $ Player.desire = 0

    ch_Rogue "Mmm. . ."

    if Rogue.History.check("swallow_cum"):
        "Just as you're about to cum, she leans over." 
        
        call hide_Character(Rogue) from _call_hide_Character_24
        
        "You feel her lips wrap around your cock right as you cum." 
        ch_Rogue "*gulp*" 
        "She makes sure to swallow it all and licks you clean afterwards." 

        call add_Characters(Rogue) from _call_add_Characters_93

        $ Rogue.History.update("swallow_cum")
    else:
        "She takes a napkin and cleans everything up after you're done."

        $ Rogue.History.update("clean_cum")

    $ Rogue.change_face("sexy", blush = 1)

    "She puts your pants back into position."

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_11

    if Rogue.History.check("swallow_cum", tracker = "recent") and renpy.random.random() > 0.5:
        $ Rogue.spunk["chin"] = True

    $ Rogue.change_face("sexy", blush = 2)

    if Rogue.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Rogue) from _call_swallow_cum_10

        $ Rogue.change_face("sly", blush = 2)

        ch_Rogue "*gulp*"

    ch_Rogue "Ah really like touchin' ya like that."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_563
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_564

    return

label Rogue_date_movie_sex_touch_pussy:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1) 

    "Once you're sure nobody's around, you reach over."
    "You can instantly feel how wet she is, as you slowly move your hand over her crotch."

    $ Rogue.change_face("sexy", eyes = "right", blush = 1)
    call expose(Rogue, "pussy") from _call_expose_7

    "Slipping your hand under her pants, you tease her for a bit, before getting right to work."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Rogue "Lord. . . please, [Rogue.Player_petname]. . ."
    "[Rogue.name] tries to continue watching the movie, but she seems more focused on suppressing any moans."
    "You make sure to give every part of her pussy ample attention."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

    "Whatever you're doing seems to be working as she starts squirming and grinding against your hand."
    "She also reaches over and starts teasing you as well."

    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 3)

    "You pick up the pace, and [Rogue.name] grabs your arm, holding it in place."

    ch_Rogue "Don't stop, please!"
    "She's not letting go until you finish the job."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 3)

    ch_Rogue "*gasp*" with small_screenshake

    $ Rogue.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 3)

    "She finally reaches the climax and can't help but violently shudder." with small_screenshake
    "You don't stop, and the shuddering continues, her grip on your arm tightening." with small_screenshake

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    "Finally, after a minute, she lets go."
    "She's still twitching even as you pull your hand away."

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_12

    ch_Rogue "Lord. . . that felt amazin'." 

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_565
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_566

    return

label Rogue_date_movie_sex_finger_pussy:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1) 

    "Once you're sure nobody's around, you reach over."
    "You can instantly feel how wet she is, as you slowly move your hand over her crotch."

    $ Rogue.change_face("sexy", eyes = "right", blush = 1)
    call expose(Rogue, "pussy") from _call_expose_8

    "Slipping your hand under her pants, you tease her for a bit, before sliding your fingers inside."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Rogue "Lord. . . please, [Rogue.Player_petname]. . ."
    "[Rogue.name] tries to continue watching the movie, but she seems more focused on suppressing any moans."
    "Your fingers slide in and out while your thumb teases her clit."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

    "Whatever you're doing seems to be working as she starts squirming and grinding against your hand."
    "She also reaches over and starts teasing you as well."

    $ Rogue.change_face("surprised2", mouth = "lipbite", blush = 3)

    "You pick up the pace, and [Rogue.name] grabs your arm, holding it in place."

    ch_Rogue "Don't stop, please!"
    "She's not letting go until you finish the job."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 3)

    ch_Rogue "*gasp*" with small_screenshake

    $ Rogue.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 3)

    "She finally reaches the climax and can't help but violently shudder." with small_screenshake
    "You don't stop, and the shuddering continues, her grip on your arm tightening." with small_screenshake

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    "Finally, after a minute, she lets go."
    "She's still twitching even as you pull your hand away."

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_13

    ch_Rogue "Lord. . . that felt amazin'." 

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_567
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_568

    return

label Rogue_date_movie_sex_blowjob:
    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Rogue.change_face("sexy", blush = 1)

    "The theater is basically empty, and nobody's anywhere near the two of you."

    call hide_Character(Rogue) from _call_hide_Character_25

    if sex_initiator == Rogue:
        if Rogue.petname not in ["Anna Marie"]:
            $ temp = Rogue.petname.capitalize()
        else:
            $ temp = Rogue.petname

        ch_Player "[temp], what exactly did you have in mind. . . ?"

    "[Rogue.name] leans over and starts teasing you."
    "Once you're hard, she starts undoing your pants, taking your cock out."
    "She gets right to work, wrapping her lips around you."
    ch_Rogue "*slurp*"
    "You hold her hair out of the way, and she starts speeding up."

    if Rogue.History.check("blowjob") >= 11:
        "Her attentiveness has been paying off, as she knows exactly how you like it and brings you to the edge in record time."
    elif Rogue.History.check("blowjob") >= 5:
        "She still fumbles around a bit, but is very attentive and is quickly learning what gets you off." 
        "You're about to blow already."
    else:
        "She's still not used to touching you down there, let alone blowing you, and she fumbles around quite a bit." 
        "Despite her lack of experience, she does her best to get you off, and you're brought to the edge all the same."

    $ Player.desire = 75

    "[Rogue.name] can tell you're close and starts speeding up."
    "She starts moaning around your cock, apparently getting off to this just as much as you are."

    $ Player.desire = 90
    
    "Finally, you can't hold on any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0
    
    ch_Rogue "*slurp*"
    "You put a hand on the back of her head, pushing her down as you cum."
    "She moans and pushes down as well, trying to take your cum as deep as she can handle."
    ch_Rogue "*gulp*"
    "[Rogue.name] keeps sucking, trying to squeeze out every last drop."
    "You twitch involuntarily until she's finally satisfied."
    "She dutifully licks you clean, before putting your pants back into position."

    if renpy.random.random() > 0.5:
        $ Rogue.spunk["chin"] = True

    call add_Characters(Rogue) from _call_add_Characters_94

    $ Rogue.change_face("sexy", blush = 2)

    if Rogue.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Rogue.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Rogue) from _call_swallow_cum_11

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

        ch_Rogue "*gulp*"

    ch_Rogue "Ah really like the way ya taste. . ."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_569
    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_570

    $ Rogue.History.update("swallow_cum")

    return

label Rogue_date_mall:
    if Rogue in second_event.keys():
        $ Rogue.change_face("smirk2", eyes = "right") 

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "Could we just hang out in the mall?"

        $ Rogue.change_face("smirk2", eyes = "right")

        ch_Player "Sure."

        if renpy.random.random() > 0.5 or Player.cash < 10:
            ch_Rogue "Let's wander 'round."

            $ second_event[Rogue] = "wander"
        else:
            $ Rogue.change_face("happy", brows = "raised", eyes = "right") 
            
            ch_Rogue "Oh!" 
            
            $ Rogue.change_face("pleased2") 
            
            ch_Rogue "How 'bout dessert!"

            $ second_event[Rogue] = "dessert"

        "She grabs your hand, and you walk through the mall."
    elif Player in second_event.keys():
        menu:
            "How about we stay in the mall and. . ."
            ". . . wander around.":
                $ second_event[Player] = "wander"
            ". . . grab dessert." if Player.cash >= 10:
                $ second_event[Player] = "dessert"

        $ Rogue.change_face("smirk2") 
        ch_Rogue "Whatever ya want, [Rogue.Player_petname]." 

    if (Player in second_event.keys() and second_event[Player] == "wander") or (Rogue in second_event.keys() and second_event[Rogue] == "wander"):
        call Rogue_date_mall_wander from _call_Rogue_date_mall_wander
    elif (Player in second_event.keys() and second_event[Player] == "dessert") or (Rogue in second_event.keys() and second_event[Rogue] == "dessert"):
        call Rogue_date_mall_dessert from _call_Rogue_date_mall_dessert

    return

label Rogue_date_mall_wander:
    $ Rogue.change_face("smirk1", eyes = "right")

    "Without any specific destination in mind, you wander around the mall with [Rogue.name]."

    $ Rogue.change_face("smirk2", eyes = "right")

    "She's deferential, as usual, but you share a very pleasant conversation with her about anything that comes to mind."

    $ holding_hands = False

    if Player in second_event.keys() and Rogue in Partners:
        menu:
            extend ""
            "Hold hands with [Rogue.name]":
                $ Rogue.change_face("smirk2", eyes = "right", blush = 1)

                "She doesn't protest and just gives your hand a squeeze in response." 
                
                $ Rogue.change_face("smirk2", mouth = "lipbite", eyes = "right", blush = 1) 
                
                call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_571

                $ holding_hands = True
            "Do nothing":
                pass
    elif Rogue in second_event.keys() and Rogue in Partners:
        $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite")

        pause 1.0

        $ Rogue.change_face("worried1", eyes = "left", mouth = "lipbite")

        pause 1.0

        $ Rogue.change_face("worried1", mouth = "lipbite")
        
        $ temp = Rogue.Player_petname.capitalize()

        ch_Rogue "[temp], can ah hold your hand?"
        "You put your hand out, and she starts holding it, interlacing your fingers."

        $ Rogue.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 1)

        $ holding_hands = True

    if holding_hands:
        "She squeezes your hand tightly and inches even closer, as you continue walking alongside each other."

    $ Rogue.change_face("smirk2", eyes = "right", blush = 1)

    "Time flies by, spent well, doing nothing much at all aside from being close to each other."

    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_572

    return

label Rogue_date_mall_dessert:
    $ Rogue.change_face("smirk1", eyes = "right")

    "Being in a mall provides a number of opportunities and problems, simultaneously."
    "There are so many different options that it can be difficult to decide what to get." 

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "You in the mood for anything, [Rogue.petname]?"
    ch_Rogue "Ah'll get whatever ya want."
    ch_Player "Then how about. . ."

    menu:
        extend ""
        "Ice Cream ($10)":
            $ Player.cash -= 10
        "Donuts ($10)":
            $ Player.cash -= 10
        "Soft Pretzels ($10)":
            $ Player.cash -= 10
        "Milkshakes ($10)":
            $ Player.cash -= 10
        "Cupcakes ($10)":
            $ Player.cash -= 10
        "Crepes ($10)":
            $ Player.cash -= 10
        "Fresh Baked Cookies ($10)":
            $ Player.cash -= 10

    $ Rogue.change_face("smirk2", eyes = "right")

    "After paying for the dessert, you both wander around the mall while enjoying it."

    $ Rogue.change_face("smirk1", eyes = "down", mouth = "lipbite")

    "Looks like you chose well, as [Rogue.name] looks like she's enjoying the dessert quite a lot."

    $ Rogue.change_face("smirk2", eyes = "right", blush = 1)

    "Even after finishing, you spend a while just walking and talking."
    "Time flies by."

    return

label Rogue_date_end:
    if "Player_initiated" in Player.date_planned[Rogue]:
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_159
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_165
        call send_Characters(Rogue, "bg_hallway", behavior = "on_date") from _call_send_Characters_136

        $ Rogue.change_face("worried1", mouth = "smirk")

        menu:
            extend ""
            "Invite her into your room":
                call Rogue_date_end_invite from _call_Rogue_date_end_invite
            "Give her a goodnight kiss":
                call Rogue_date_end_goodnight from _call_Rogue_date_end_goodnight
    else:
        call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_160
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_166
        call send_Characters(Rogue, "bg_girls_hallway", behavior = "on_date") from _call_send_Characters_137

        if Rogue.status["horny"] or Rogue.status["nympho"]:
            call Rogue_date_end_invite from _call_Rogue_date_end_invite_1
        elif renpy.random.random() > 0.25:
            call Rogue_date_end_invite from _call_Rogue_date_end_invite_2
        else:
            call Rogue_date_end_goodnight from _call_Rogue_date_end_goodnight_1

    return

label Rogue_date_end_invite:
    if Player.location == "bg_hallway":
        $ Rogue.change_face("sexy")

        ch_Player "Come on in."

        call remove_Characters(location = Player.home) from _call_remove_Characters_161
        call set_the_scene(location = Player.home) from _call_set_the_scene_167
        call send_Characters(Rogue, Player.home, behavior = "on_date") from _call_send_Characters_138
        
        if Rogue.status["horny"] or Rogue.status["nympho"]:
            $ Rogue.change_face("sexy", blush = 1) 
            
            ch_Rogue "Thanks for takin' me out. . ." 
            
            $ Rogue.change_face("sly", mouth = "lipbite", blush = 2) 
            
            ch_Rogue "But ah sure hope you have some {i}fun{/i} plans for me. . ." 
            
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1) 
            
            ch_Rogue "You know ah'm {i}all{/i} yours."
        else:
            $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right") 
            
            ch_Rogue "Ah had a real nice time tonight." 
            
            $ Rogue.change_face("worried1", mouth = "lipbite")

        menu:
            extend ""
            "Recommend something {i}fun{/i}" if approval_check(Rogue, threshold = "hookup"):
                $ Rogue.History.update("hookup")

                call screen Action_screen(automatic = True)
                
                $ choice_disabled = False

                $ Rogue.change_face("worried1", mouth = "lipbite")

                ch_Rogue "Can ah sleep over tonight, [Rogue.Player_petname]?"

                $ Rogue.change_face("pleased2")

                ch_Player "I'd love that, [Rogue.petname]."
            "Invite her to sleep over" if Rogue.History.check("sleepover"):
                $ Rogue.change_face("worried1", mouth = "lipbite") 
                
                ch_Rogue "Yer tired?" 
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "'Course ah'll keep ya company tonight."
            "Say goodnight":
                $ Rogue.change_face("worried1", mouth = "lipbite") 
                
                ch_Rogue "Could ah. . . have a kiss before ah go?" 
                "You pull her into a brief kiss." 
                
                $ Rogue.change_face("kiss2") 
                
                ch_Rogue "Mmm. . ." 

                $ Rogue.History.update("kiss")
                
                $ Rogue.change_face("worried1", mouth = "smirk") 
                
                ch_Rogue "Goodnight, [Rogue.Player_petname]."

                call send_Characters(Rogue, Rogue.home) from _call_send_Characters_139
    elif Player.location == "bg_girls_hallway":
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Maybe ya wanted to. . ."

        if approval_check(Rogue, threshold = "hookup"):
            $ Rogue.change_face("sexy", blush = 1)

            ch_Rogue "Finish things up in my room."
        else:
            ch_Rogue "Come in real quick?"

        menu:
            extend ""
            "Go inside with her":
                call Rogue_date_invite_accept from _call_Rogue_date_invite_accept
            "Say goodnight":
                call Rogue_date_invite_reject from _call_Rogue_date_invite_reject

    return

label Rogue_date_invite_accept:
    "[Rogue.name] grabs you by the hand and drags you inside the room."

    call remove_Characters(location = Rogue.home) from _call_remove_Characters_162
    call set_the_scene(location = Rogue.home) from _call_set_the_scene_168
    call send_Characters(Rogue, Rogue.home, behavior = "on_date") from _call_send_Characters_140

    $ Rogue.change_face("sexy", blush = 2)

    ch_Player "What did you have in mind?"

    $ Rogue.change_face("sly", mouth = "lipbite", blush = 2)

    if approval_check(Rogue, threshold = "hookup"):
        $ Rogue.History.update("hookup")

        call screen Action_screen(automatic = True)
        
        $ choice_disabled = False

        if approval_check(Rogue, threshold = "sleepover"):
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Could ya please sleep over?"

            menu:
                extend ""
                "I can.":
                    $ Rogue.change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    ch_Rogue "Ah'm always able to relax better when yer around."
                "Not tonight.":
                    $ Rogue.change_face("worried1") 
                    
                    ch_Rogue "It's alright." 
                    
                    $ Rogue.change_face("worried1", mouth = "smirk") 
                    
                    ch_Rogue "Goodnight, [Rogue.Player_petname]." 
                    ch_Rogue "Maybe ah'll see you tomorrow."

                    call remove_Characters(location = Player.home) from _call_remove_Characters_163
                    call set_the_scene(location = Player.home) from _call_set_the_scene_169
        else:
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "Goodnight, [Rogue.Player_petname]." 
            ch_Rogue "Maybe ah'll see you tomorrow."

            call remove_Characters(location = Player.home) from _call_remove_Characters_259
            call set_the_scene(location = Player.home) from _call_set_the_scene_355
    else:
        "She pulls you in for a kiss." 
        
        $ Rogue.change_face("kiss2") 
        
        ch_Rogue "Mmm. . ." 

        $ Rogue.History.update("kiss")

        $ Rogue.change_face("worried1", mouth = "smirk") 
        
        ch_Rogue "Goodnight, [Rogue.Player_petname]." 
        ch_Rogue "Maybe ah'll see you tomorrow."

        call remove_Characters(location = Player.home) from _call_remove_Characters_260
        call set_the_scene(location = Player.home) from _call_set_the_scene_356

    return

label Rogue_date_invite_reject:
    $ Rogue.change_face("worried1")

    ch_Player "Sorry, not tonight, [Rogue.petname]."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "It's alright, so long as ah get a kiss. . ."

    $ Rogue.change_face("kiss1", blush = 1)

    "You pull her into a brief kiss, before pulling away."

    $ Rogue.History.update("kiss")

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Hopefully ah'll see ya tomorrow, [Rogue.Player_petname]."

    call send_Characters(Rogue, Rogue.home) from _call_send_Characters_141
    call remove_Characters(location = Player.home) from _call_remove_Characters_164
    call set_the_scene(location = Player.home) from _call_set_the_scene_170

    return

label Rogue_date_end_goodnight:
    if Player.location == "bg_hallway":
        $ Rogue.change_face("kiss1", blush = 1)

        "You pull [Rogue.name] into a brief kiss."
        "She holds on for a moment, running her hands across your body, before letting go."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Player "Goodnight, [Rogue.petname]."
        ch_Rogue "Goodnight, [Rogue.Player_petname]."
        ch_Rogue "Hopefully ah'll see you tomorrow."
    else:
        $ Rogue.change_face("worried1", mouth = "lipbite")

        ch_Rogue "Could ah get a kiss?"

        $ Rogue.change_face("kiss1", blush = 1)

        "You put a hand around [Rogue.name]'s neck, pulling her into a kiss."
        "Her hands wander across your body."
        "After a long moment, you pulls away."

        $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Rogue "Ah had a real great time with ya tonight."
        ch_Rogue "Goodnight, [Rogue.Player_petname]."
        ch_Rogue "Hopefully ah'll see you tomorrow."

    $ Rogue.History.update("kiss")

    call send_Characters(Rogue, Rogue.home) from _call_send_Characters_142
    call remove_Characters(location = Player.home) from _call_remove_Characters_165
    call set_the_scene(location = Player.home) from _call_set_the_scene_171

    return