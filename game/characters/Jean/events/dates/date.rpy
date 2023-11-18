init python:

    def Jean_date():
        label = "Jean_date"

        conditions = [
            "Jean in Player.date_planned.keys() and 'primary' in Player.date_planned[Jean]",

            "Jean.History.check('went_on_date_with_Player') >= 1",

            "time_index == 2"]

        waiting = True
        traveling = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority, repeatable = repeatable)

label Jean_date:
    $ ongoing_Event = True

    hide screen phone_screen

    if weather == "rain":
        $ weather = None

    $ Party = []

    if Player.location != "bg_hallway":
        "You have a date with [Jean.name]: better go and wait for her outside your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_1

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed

    call receive_text(Jean, "On my wayyy") from _call_receive_text
    call open_texts(Jean) from _call_open_texts

    pause

    hide screen phone_screen

    "You only have to wait for a few seconds, before you see [Jean.name] walking down the hall."

    call send_Characters(Jean, "bg_hallway", behavior = "on_date") from _call_send_Characters

    $ Jean.change_face("happy")

    ch_Jean "Hey!"

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Ready to go?"
    ch_Player "I am."
    ch_Player "Did you have a plan?"

    $ Jean.change_face("smirk2")

    $ first_event = {}
    $ second_event = {}

    if "Girl_initiated" in Player.date_planned[Jean]:
        if renpy.random.random() > 0.5:
            ch_Jean "Yep!" 
            ch_Jean "Let's go grab dinner."

            $ first_event[Jean] = "dinner"

            call Jean_date_dinner from _call_Jean_date_dinner
        else:
            ch_Jean "Mhm." 
            ch_Jean "Let's go catch a movie."

            $ first_event[Jean] = "movie"

            call Jean_date_movie from _call_Jean_date_movie
    else:
        ch_Jean "Nope."
        ch_Jean "Why don't you choose?"

        menu:
            extend ""
            "Let's grab some dinner first.":
                ch_Jean "Sounds good."

                $ first_event[Player] = "dinner"

                call Jean_date_dinner from _call_Jean_date_dinner_1
            "Let's go catch a movie.":
                ch_Jean "Sounds good."

                $ first_event[Player] = "movie"

                call Jean_date_movie from _call_Jean_date_movie_1
            "Actually. . . can we just chill, hang out here?":
                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Jean "Sure, [Jean.Player_petname]." 
                
                $ Jean.change_face("smirk2") 
                
                ch_Jean "We don't have to go out."
                        
                call remove_Characters(location = Player.home) from _call_remove_Characters_1
                call set_the_scene(location = Player.home) from _call_set_the_scene_2
                call send_Characters(Jean, Player.home, behavior = "on_date") from _call_send_Characters_1

                $ Player.date_planned = {}

                $ ongoing_Event = False

                return

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_2
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_3
    call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_2

    if "Girl_initiated" in Player.date_planned[Jean]:
        if renpy.random.random() > 0.25:
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                if (Player in first_event.keys() and first_event[Player] == "dinner") or (Jean in first_event.keys() and first_event[Jean] == "dinner"):
                    $ second_event[Jean] = "movie"
                elif (Player in first_event.keys() and first_event[Player] == "movie") or (Jean in first_event.keys() and first_event[Jean] == "movie"):
                    $ second_event[Jean] = "dinner"
            elif dice_roll > 0.125:
                $ second_event[Jean] = "mall"
            else:
                $ second_event[Jean] = "end"
    elif "Player_initiated" in Player.date_planned[Jean]:
        if renpy.random.random() > 0.75:
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                if (Player in first_event.keys() and first_event[Player] == "dinner") or (Jean in first_event.keys() and first_event[Jean] == "dinner"):
                    $ second_event[Jean] = "movie"
                elif (Player in first_event.keys() and first_event[Player] == "movie") or (Jean in first_event.keys() and first_event[Jean] == "movie"):
                    $ second_event[Jean] = "dinner"
            elif dice_roll > 0.125:
                $ second_event[Jean] = "mall"
            else:
                $ second_event[Jean] = "end"

    if not second_event:
        $ Jean.change_face("smirk2", eyes = "right") 

        pause 1.0

        $ Jean.change_face("smirk2")

        ch_Jean "You can pick, [Jean.Player_petname]."

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "What're we doing next?"

        menu:
            extend ""
            "Let's grab dinner. . ." if (Player in first_event.keys() and first_event[Player] == "movie") or (Jean in first_event.keys() and first_event[Jean] == "movie"):
                $ second_event[Player] = "dinner"

                call Jean_date_dinner from _call_Jean_date_dinner_2
            "Let's head to the movie theater." if (Player in first_event.keys() and first_event[Player] == "dinner") or (Jean in first_event.keys() and first_event[Jean] == "dinner"):
                $ Jean.change_face("happy") 
                
                ch_Jean "Yes!" 
                
                $ Jean.change_face("smirk2") 

                ch_Jean "Was hoping you'd suggest that."

                $ second_event[Player] = "movie"

                call Jean_date_movie from _call_Jean_date_movie_2
            "How about we stay in the mall and. . .":
                $ second_event[Player] = "mall"

                call Jean_date_mall from _call_Jean_date_mall
            "Want to head back to the Institute?":
                $ Jean.change_face("confused1", mouth = "smirk")
                
                ch_Jean "Sure." 
                
                $ Jean.change_face("sly") 
                
                ch_Jean "We can finish the date in private."

                $ second_event[Player] = "end"
    else:
        if Jean in second_event.keys():
            if second_event[Jean] == "dinner":
                call Jean_date_dinner from _call_Jean_date_dinner_3
            elif second_event[Jean] == "movie":
                call Jean_date_movie from _call_Jean_date_movie_3
            elif second_event[Jean] == "mall":
                call Jean_date_mall from _call_Jean_date_mall_1
            elif second_event[Jean] == "end":
                $ Jean.change_face("sexy", eyes = "right") 

                pause 1.0

                $ Jean.change_face("sexy", blush = 1)

                ch_Jean "Let's head back. . ."

                $ Jean.change_face("sexy", eyes = "right", blush = 1)

                ch_Player "Why?"

                if Jean.status["horny"] or Jean.status["nympho"]:
                    $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
                    
                    ch_Jean "Because, [Jean.Player_petname]." 
                    
                    $ Jean.change_face("sexy", eyes = "down", blush = 1) 
                    
                    pause 1.0 
                    
                    $ Jean.change_face("sexy", blush = 1) 
                    
                    ch_Jean "We can't finish the date like I planned with so many other people around. . ." 
                    
                    $ Jean.change_face("sexy", eyes = "right")
                else:
                    $ Jean.change_face("sly") 
                    
                    ch_Jean "I just wanna finish our date in private. . ."

    if Player.location != "bg_mall":
        $ fade_to_black(0.4)

        $ time_index = 3

        $ lighting = "night"

        call remove_Characters(location = "bg_mall") from _call_remove_Characters_3
        call set_the_scene(location = "bg_mall") from _call_set_the_scene_4
        call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_3

    $ Jean.change_face("smirk2")

    ch_Jean "C'mon, [Jean.Player_petname], let's go."

    $ Jean.change_face("smirk2", eyes = "left")

    "She takes your hand and pulls you along."

    $ fade_to_black(0.4)

    "You walk back to the Institute together."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_4
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_5
    call send_Characters(Jean, "bg_campus", behavior = "on_date") from _call_send_Characters_4

    "You continue to chat and enjoy each other's company as you head back into the dorms."

    call Jean_date_end from _call_Jean_date_end

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

    if Jean.location == Player.location:
        jump go_to_sleep
    # else:
    #     call move_location(Player.location) from _call_move_location_2

    return

label Jean_date_dinner:
    if second_event:
        if Jean in second_event.keys():
            $ Jean.change_face("smirk2", eyes = "right")

            pause 1.0

            $ Jean.change_face("smirk2", mouth = "lipbite")

            ch_Jean "Are you hungry?"
            ch_Jean "I'm hungry."
            ch_Player "Yeah, I could go for a bite to eat."

            $ Jean.change_face("smirk2")

            ch_Jean "C'mon, let's grab some dinner."

            $ Jean.change_face("smirk2", eyes = "right")

            "She grabs your hand, and you head to the restaurant together."

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Jean "I got us a reservation at the steakhouse." 
                
                $ Jean.change_face("happy") 
                
                ch_Jean "It'll be great."

                $ cuisine = "steakhouse"
            elif dice_roll == 2:
                ch_Jean "I got us a reservation at that seafood place." 
                
                $ Jean.change_face("worried1", mouth = "smirk") 
                
                ch_Jean "That stuff's really growing on me."

                $ cuisine = "seafood"
            elif dice_roll == 3:
                ch_Jean "I got us a reservation at that Southern restaurant." 
                
                $ Jean.change_face("worried1", mouth = "smirk") 
                
                ch_Jean "The food's spicy. . ." 
                ch_Jean "But I'm getting used to it."

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

            $ Jean.change_face("smirk2") 
            
            ch_Jean "Sure." 
            ch_Jean "I am pretty hungry."
    else:
        if Jean in first_event.keys():
            $ Jean.change_face("smirk2")

            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Jean "I got us a reservation at the steakhouse." 
                
                $ Jean.change_face("happy") 
                
                ch_Jean "It'll be great."

                $ cuisine = "steakhouse"
            elif dice_roll == 2:
                ch_Jean "I got us a reservation at that seafood place." 
                
                $ Jean.change_face("worried1", mouth = "smirk") 
                
                ch_Jean "That stuff's really growing on me."

                $ cuisine = "seafood"
            elif dice_roll == 3:
                ch_Jean "I got us a reservation at that Southern restaurant." 
                
                $ Jean.change_face("worried1", mouth = "smirk") 
                
                ch_Jean "The food's spicy. . ." 
                ch_Jean "But I'm getting used to it."

                $ cuisine = "southern"
        elif Player in first_event.keys():
            $ Jean.change_face("smirk2")

            ch_Jean "Where did you wanna eat, [Jean.Player_petname]?"

            $ Jean.change_face("confused1", mouth = "smirk")

            ch_Player "Were you in the mood for anything?"
            ch_Jean "Nothing in particular."
            ch_Player "Okay. . . then how about. . ."

            menu:
                extend ""
                "Let's go to that steakhouse.":
                    $ cuisine = "steakhouse"
                "How about seafood?":
                    $ cuisine = "seafood"
                "I'm in the mood for Southern food.":
                    $ cuisine = "southern"

            $ Jean.change_face("smirk2")

            ch_Jean "Sure."

    $ eating_dinner = True
    $ ordered_food = True
    $ food_arrived = False
    $ drinking_wine = False

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_5
    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_6
    call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_5

    "You get seated quickly, and the waitress hands out the menus."

    $ Jean.change_face("smirk1", eyes = "down")

    $ ordered_food = False

    $ Player_picked_food = False

    if renpy.random.random() > 0.66:
        pause 1.0 

        $ Jean.change_face("smirk2", eyes = "squint")

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp], why don't you pick for me?"
        ch_Jean "I trust your judgment."
        ch_Player "Okay, then why don't you get. . ."

        $ chosen_meal = {}
        $ restaurant_bill = {}

        call restaurant_menu(Jean, cuisine) from _call_restaurant_menu

        ch_Player "And I'll get. . ."

        call restaurant_menu(Player, cuisine) from _call_restaurant_menu_1

        $ Player_picked_food = True
    else:
        "You decide to order. . ."

        $ chosen_meal = {}
        $ restaurant_bill = {}

        call restaurant_menu(Player, cuisine) from _call_restaurant_menu_2

    $ Jean.change_face("smirk2")

    "You have a nice time chatting with [Jean.name], as you wait for the waitress to come back and take your orders."

    if Jean in Partners and renpy.random.random() > 0.75:
        "You know how stressed she's been lately." 
        "It's nice to see her relax a bit for once."

    $ Jean.change_face("smirk2", eyes = "right")

    "The waitress finally comes back, and. . ."

    $ temp = chosen_meal[Player]

    menu:
        extend ""
        "Let her order for you  (encourage_quirk)":
            if Jean.ordered_for_you_last_time:
                "You hold your tongue and wait for [Jean.name]."
                ch_Jean "He's gonna get the [temp]."
            else:
                "You hold your tongue and wait for [Jean.name]."

                $ Jean.change_face("confused1")

                pause 1.0

                $ Jean.change_face("happy")

                pause 1.0

                $ Jean.change_face("smirk2", eyes = "right")

                ch_Jean "He's gonna get the [temp]."

            $ Jean.ordered_for_you_last_time = True

            $ Jean.History.update("quirk_encouraged")
        "Order for yourself  (discourage_quirk)":
            if Jean.ordered_for_you_last_time:
                ch_Jean "He-"

                $ Jean.change_face("confused1")

                "Before she can finish, you speak up."
                ch_Player "I'll have the [temp]."

                $ Jean.change_face("worried1")

                ch_Jean "Aw, why couldn't I. . ."

                $ Jean.change_face("worried1", eyes = "right")
            else:
                $ Jean.change_face("confused1", mouth = "smirk")

                ch_Jean "You could just let me. . ."
                ch_Player "I'll have the [temp]."

                $ Jean.change_face("confused1", mouth = "smirk", eyes = "right")

            $ Jean.ordered_for_you_last_time = False

            $ Jean.History.update("quirk_discouraged")

    if Jean not in chosen_meal.keys():
        if cuisine == "steakhouse":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.6:
                $ chosen_meal[Jean] = "penne alla vodka"
                $ restaurant_bill[Jean] = 30
            elif dice_roll > 0.55*2/3 + 0.05:
                if renpy.random.random() > 0.5:
                    $ chosen_meal[Jean] = "filet mignon"
                else:
                    $ chosen_meal[Jean] = "ribeye"

                $ restaurant_bill[Jean] = 45
            elif dice_roll > 0.55*1/3 + 0.05:
                $ chosen_meal[Jean] = "Chilean sea bass"
                $ restaurant_bill[Jean] = 35
            elif dice_roll > 0.55*0/3 + 0.05:
                $ chosen_meal[Jean] = "chicken parmesan"
                $ restaurant_bill[Jean] = 25
            else:
                $ chosen_meal[Jean] = "chopped salad"
                $ restaurant_bill[Jean] = 15
        elif cuisine == "seafood":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.6:
                $ chosen_meal[Jean] = "crab cakes"
                $ restaurant_bill[Jean] = 30
            elif dice_roll > 0.55*2/3 + 0.05:
                $ chosen_meal[Jean] = "lobster tails"
                $ restaurant_bill[Jean] = 45
            elif dice_roll > 0.55*2/3 + 0.05:
                $ chosen_meal[Jean] = "crab-stuffed sole"
                $ restaurant_bill[Jean] = 35
            elif dice_roll > 0.55*0/3 + 0.05:
                $ chosen_meal[Jean] = "salmon"
                $ restaurant_bill[Jean] = 25
            else:
                $ chosen_meal[Jean] = "garden salad"
                $ restaurant_bill[Jean] = 15
        elif cuisine == "southern":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.6:
                $ chosen_meal[Jean] = "jambalaya"
                $ restaurant_bill[Jean] = 30
            elif dice_roll > 0.55*2/3 + 0.05:
                $ chosen_meal[Jean] = "short ribs"
                $ restaurant_bill[Jean] = 45
            elif dice_roll > 0.55*1/3 + 0.05:
                $ chosen_meal[Jean] = "catfish"
                $ restaurant_bill[Jean] = 35
            elif dice_roll > 0.55*0/3 + 0.05:
                $ chosen_meal[Jean] = "fried chicken"
                $ restaurant_bill[Jean] = 25
            else:
                $ chosen_meal[Jean] = "salad"
                $ restaurant_bill[Jean] = 15

    $ temp = chosen_meal[Jean]

    ch_Jean "I'll have the [temp]."

    if chosen_meal[Jean] in ["filet mignon", "ribeye"]:
        $ Jean.change_face("worried1", eyes = "right") 
        
        ch_Jean "Could you make it medium?" 
        ch_Jean "Maybe even medium well. . ." 
        
        $ Jean.change_face("worried2") 
        
        ch_Jean "What?!" 
        
        $ Jean.change_face("worried1") 
        
        ch_Jean "Don't look at me like that. . ." 
        
        $ Jean.change_face("worried1", mouth = "smirk") 

        ch_Jean "I don't like it when it's too pink. . ."

    $ ordered_food = True

    $ Jean.change_face("smirk1")

    "The waitress walks away, leaving the two of you alone again."

    $ lines = {
        "a": "What kind of music are you into? I'm sure you have great taste.",
        "b": "You look drop-dead gorgeous today. . . as always, I mean.",
        "c": "Your outfit looks really cute today.",
        "d": "That top makes your tits look amazing.",
        "k": "You always smell so good."}

    $ indices = list(lines.keys())

    $ renpy.random.shuffle(indices)

    $ first_compliment = lines[indices[0]]
    $ second_compliment = lines[indices[1]]
    $ third_compliment = lines[indices[2]]

    menu:
        extend ""
        "[first_compliment]":
            call expression f"Jean_flirt_a{indices[0]}" from _call_expression
        "[second_compliment]":
            call expression f"Jean_flirt_a{indices[1]}" from _call_expression_1
        "[third_compliment]":
            call expression f"Jean_flirt_a{indices[2]}" from _call_expression_2

    $ Jean.change_face("smirk2", blush = 1)

    "You continue to have a nice conversation, as you wait for the food to arrive."

    $ Jean.change_face("confused1", mouth = "smirk")

    "You learn a lot about each other, your lives before the Institute, and your dreams for the future."
                
    pause 1.0

    $ fade_to_black(0.4)

    $ food_arrived = True

    $ fade_in_from_black(0.4)
    
    $ Jean.change_face("smirk2", eyes = "right")

    "The waitress finally comes back with your orders."
    ch_Jean "Thanks!"

    $ Jean.change_face("smirk2", eyes = "down", mouth = "lipbite")

    ch_Jean "Mmm, this smells great."
    "[Jean.name] digs right in."

    if Player_picked_food and chosen_meal[Jean] in ["penne alla vodka", "crab cakes", "jambalaya"]:
        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "This is delicious."
        ch_Jean "Thanks for making a great choice, [Jean.Player_petname]."

        call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "How's your food?"

        $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Jean "I hope it's this good."
        ch_Player "Yeah, it's great!"
    elif not Player_picked_food and chosen_meal[Jean] not in ["penne alla vodka", "crab cakes", "jambalaya"] and chosen_meal[Player] in ["penne alla vodka", "crab cakes", "jambalaya"]:
        $ Jean.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Jean "That looks really good."
        ch_Jean "You should totally give me a bite of it. . ."

        menu:
            extend ""
            "Give her a bite":
                "You cut her a piece, and she eats it directly off of your fork." 

                $ Jean.change_face("neutral", eyes = "down", mouth = "open")

                pause 1.0

                $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

                ch_Jean "Tasted as good as it looked."

                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1
            "Don't give her a bite":
                $ Jean.change_face("worried1") 

                "You don't give her any and she starts pouting."
                ch_Jean "Why not?!" 

                $ Jean.change_face("confused1", eyes = "right")

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean
                
            call Jean_date_dinner_sex from _call_Jean_date_dinner_sex
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_dinner_sex from _call_Jean_date_dinner_sex_1
                "Just finish the meal normally":
                    pass

    $ Jean.change_face("smirk1", eyes = "right")

    "You finish eating, and the waitress comes by with the check."

    $ Jean.change_face("confused1", mouth = "smirk") 

    menu:
        "Offer to pay":
            if "Player_initiated" in Player.date_planned[Jean]:
                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Player "I'll cover it."
                ch_Jean "Aw, [Jean.Player_petname], you don't have to. . ."

                $ Jean.change_face("smirk2")  

                ch_Player "Don't worry, I got it."
                ch_Jean "Thank you."

                $ Jean.change_face("smirk2", blush = 1)

                if Player.cash >= restaurant_bill[Player] + restaurant_bill[Jean]:
                    "You pay the bill and head back into the mall." 
                    
                    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_2

                    $ Player.cash -= restaurant_bill[Player] + restaurant_bill[Jean]
                else:
                    "You realize you don't have enough money. . ." 
                    
                    $ Jean.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Jean.change_face("confused1", mouth = "smirk") 
                    
                    ch_Jean "If you didn't have enough, you should've just said so." 
                    "[Jean.name] pays the difference." 
                    
                    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_3

                    $ Player.cash = 0
            else:
                $ Jean.change_face("sly")

                ch_Jean "Nope, put your wallet away."
                ch_Jean "This date was my idea."
                ch_Player "Thanks, [Jean.petname]. . ."

                $ Jean.change_face("smirk2", blush = 1)

                ch_Jean "You're welcome, [Jean.Player_petname]."
                "[Jean.name] pays the bill, and you both head back into the mall."

                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_4
        "Recommend splitting the check":
            if "Player_initiated" in Player.date_planned[Jean]:
                $ Jean.change_face("confused1", mouth = "smirk")

                ch_Player "Why don't we split the bill?"

                $ Jean.change_face("smirk2")

                ch_Jean "Oh alright, if you want to that badly."

                if Player.cash >= math.ceil((restaurant_bill[Player] + restaurant_bill[Jean])/2):
                    "You both pay the bill and head back into the mall."

                    $ Player.cash -= math.ceil((restaurant_bill[Player] + restaurant_bill[Jean])/2)
                else:
                    "You realize you don't have enough money to pay for half. . ."  
                    
                    $ Jean.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Jean.change_face("confused1", mouth = "smirk") 
                    
                    ch_Jean "If you didn't have enough, you should've just said so." 
                    "[Jean.name] pays the difference." 
                    
                    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_5

                    $ Player.cash = 0
            else:
                $ Jean.change_face("sly")

                ch_Jean "Nope, put your wallet away."
                ch_Jean "This date was my idea."
                ch_Player "Thanks, [Jean.petname]. . ."

                $ Jean.change_face("smirk2", blush = 1)

                ch_Jean "You're welcome, [Jean.Player_petname]."
                "[Jean.name] pays the bill, and you both head back into the mall."

                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_6

    return

label Jean_date_dinner_sex:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    "You notice [Jean.name] looking at you seductively."

    if sex_initiator == Player:
        menu:
            extend ""
            "Ask for a handjob under the table" if Jean.History.check("handjob"):
                $ sex_act = "handjob"
            "Ask for a blowjob under the table" if Jean.History.check("blowjob") and Jean.History.check("swallow_cum"):
                $ sex_act = "blowjob"
            "Suggest a quickie in the bathroom" if Jean.History.check("sex"):
                $ sex_act = "sex"
            "Ask to go down on her in the bathroom" if Jean.History.check("eat_pussy"):
                $ sex_act = "eat_pussy"
            "Decide against it":
                return
    elif sex_initiator == Jean:
        $ sex_acts = []

        if Jean.History.check("handjob"):
            $ sex_acts.append("handjob")

        if Jean.History.check("blowjob") and Jean.History.check("swallow_cum"):
            $ sex_acts.append("blowjob")

        if Jean.History.check("sex"):
            $ sex_acts.append("sex")

        if Jean.History.check("eat_pussy"):
            $ sex_acts.append("eat_pussy")

        if sex_acts:
            if Jean.quirk:
                ch_Jean "Just try and relax." 
                ch_Jean "Your big sister is gonna make you feel {i}really{/i} good."

            menu:
                extend ""
                "Go along with it":
                    $ sex_act = renpy.random.choice(sex_acts)
                "Not right now, [Jean.petname].":
                    $ Jean.change_face("worried1", blush = 1)
                    
                    ch_Jean "Oh alright."

                    return

    call expression f"Jean_date_dinner_sex_{sex_act}" from _call_expression_3

    return

label Jean_date_dinner_sex_handjob:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1)

    call hide_Character(Jean) from _call_hide_Character

    "After making sure nobody is paying attention, she slips out of sight."

    if sex_initiator == Jean:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], what exactly are you doing. . . ?"

    "Thanks to the long table cloth, even if someone was looking, they wouldn't be able to see anything."
    "You can feel her tease you for a while, before pulling your pants down."
    "She continues to tease, drawing out every little touch."
    "After she's satisfied, she gets to work, wrapping her fingers around you."
    "You continue to eat your meal as nonchalantly as possible, meanwhile [Jean.name] starts picking up the pace."

    if Jean.History.check("handjob") >= 11:
        "She knows exactly what she's doing now, so you know it's intentional when she teases you, and you're barely able to hold it in after mere moments."
    elif Jean.History.check("handjob") >= 5:
        "She's getting better, more gentle, but she's still figuring things out, so it takes a while before you're on the edge."
    else:
        "She has a death grip and is a bit too rough, but it brings you to the edge all the same."

    $ Player.desire = 75

    "[Jean.name] can tell you're getting close and slows down, lessening her grip until she's barely touching you."
    "She teases you and makes you twitch for a long while before she's satisfied."

    $ Player.desire = 90

    "Finally, she gets back to it, and you can't hold it in any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0

    if Jean.History.check("swallow_cum"):
        "You feel her lips wrap around your cock right as you cum." 
        ch_Jean "*gulp*" 
        "She makes sure to swallow it all and licks you clean afterwards."

        $ Jean.History.update("swallow_cum")
    else:
        "She takes a napkin and cleans everything up after you're done."

        $ Jean.History.update("clean_cum")

    "She puts your pants back into position, before getting up."

    if Jean.History.check("swallow_cum", tracker = "recent") and renpy.random.random() > 0.5:
        $ Jean.spunk["chin"] = True

    call add_Characters(Jean) from _call_add_Characters_18

    $ Jean.change_face("sexy", blush = 2)

    if Jean.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Jean) from _call_swallow_cum

        $ Jean.change_face("sly", blush = 2)

        ch_Jean "*gulp*"

    $ Jean.change_face("sly", blush = 2)

    ch_Jean "I love making you twitch."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_7
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_8

    return

label Jean_date_dinner_sex_blowjob:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1)

    call hide_Character(Jean) from _call_hide_Character_1

    "After making sure nobody is paying attention, [Jean.name] slips out of sight."

    if sex_initiator == Jean:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], what exactly are you doing. . . ?"

    "Thanks to the long table cloth, even if someone was looking, they wouldn't be able to see anything."
    "You can feel her tease you for a while, before pulling your pants down."
    "She continues to tease, drawing out every little touch."
    "After she's satisfied, she gets to work, wrapping her lips around you."
    "You continue to eat your meal as nonchalantly as possible, meanwhile [Jean.name] starts picking up the pace."

    if Jean.History.check("blowjob") >= 11:
        "By now, she knows exactly what gets you going and is able to bring you to the edge in mere moments."    
    elif Jean.History.check("blowjob") >= 5:
        "She's getting better, but still fumbles around a bit with her hands, yet you're about to lose control faster than ever."
    else:
        "She still fumbles around quite a bit, showing her lack of experience, but it brings you to the edge all the same."
    
    $ Player.desire = 75

    "[Jean.name] can tell you're close and stops what she's doing."
    "She continues teasing for a while, causing you to twitch."

    $ Player.desire = 90

    "Finally, she has mercy on you and continues until you can't hold on any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0

    ch_Jean "*slurp*"
    "She pulls back a bit, holding your cock in her mouth as you cum."
    ch_Jean "*gulp*"
    "[Jean.name] starts sucking again, trying to squeeze out every last drop."
    "You twitch involuntarily until she's finally satisfied and pulls away."
    "She puts your pants back into position, before getting up."

    if renpy.random.random() > 0.5:
        $ Jean.spunk["chin"] = True

    call add_Characters(Jean) from _call_add_Characters_19

    $ Jean.change_face("sexy", blush = 2)

    if Jean.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Jean) from _call_swallow_cum_1

        $ Jean.change_face("sly", blush = 2)

        ch_Jean "*gulp*"

    ch_Jean "You taste {i}really{/i} good."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_9
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_10

    $ Jean.History.update("swallow_cum")

    return

label Jean_date_dinner_sex_sex:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "C'mon, [Jean.Player_petname]."
    ch_Jean "Let's have some fun. . ."

    call hide_Character(Jean) from _call_hide_Character_2

    "[Jean.name] heads to the bathroom and, after a minute, you follow after her."

    $ fade_to_black(0.4)

    "You see her waiting for you outside the bathroom, and you both head inside together."

    call set_the_scene(location = "bg_restaurant_bathroom") from _call_set_the_scene_7
    call send_Characters(Jean, "bg_restaurant_bathroom", behavior = "on_date") from _call_send_Characters_8

    "Good thing it's a private one."
    "She locks the door behind you."
        
    if sex_initiator == Jean:
        $ has_position_control = False
        $ has_movement_control = False

    $ Jean.available_Actions = ["sex"]

    if Jean.History.check("anal"):
        $ Jean.available_Actions.append("anal")

    $ Jean.available_poses = ["missionary"]

    if Jean.History.check("doggy"):
        $ Jean.available_poses.append("doggy")

    $ chosen_Action = renpy.random.choice(Jean.available_Actions)
    $ chosen_pose = renpy.random.choice(Jean.available_poses)

    $ Jean.History.update("hookup")
        
    $ Jean.History.update(chosen_Action)
    
    call request_position(Jean, chosen_pose, automatic = True) from _call_request_position_11

    $ Action = ActionClass(chosen_Action, Player, Jean)

    call undress(Jean, "underwear") from _call_undress_17
    call start_Action(Action) from _call_start_Action
    call screen Action_screen(automatic = True)

    $ choice_disabled = False

    if renpy.random.random() > 0.5:
        call try_on(Jean, Jean.Wardrobe.Clothes["messy hair"]) from _call_try_on

    call change_Outfit(Jean, Jean.Wardrobe.Outfits[Jean.Outfit.name]) from _call_change_Outfit_24
    
    $ locations = list(Jean.spunk.keys())

    while locations:
        if Jean.spunk[locations[0]]:
            call clean_cum(Jean) from _call_clean_cum_4

        $ locations.remove(locations[0])

    "After you both put your clothes back on, [Jean.name] leaves and heads back to the table."

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_6
    call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_9

    "You wait a minute before leaving the bathroom as well."

    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_8

    $ Jean.change_face("sly", blush = 2)
    
    pause 1.0

    if Jean.Clothes["hair"].string == "messy":
        ch_Player "Your hair's a bit. . ."

        $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

        "She straightens it out."

        call try_on(Jean, Jean.Wardrobe.Clothes["straight hair"]) from _call_try_on_1

    $ Jean.change_face("sexy")

    ch_Jean "That was a {i}lot{/i} of fun. . ."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_11
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_12

    $ Jean.available_Actions = []
    $ Jean.available_poses = []

    return

label Jean_date_dinner_sex_eat_pussy:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "C'mon, [Jean.Player_petname]."
    ch_Jean "Let's have some fun. . ."

    call hide_Character(Jean) from _call_hide_Character_3

    "[Jean.name] heads to the bathroom and, after a minute, you follow after her."

    $ fade_to_black(0.4)

    "You see her waiting for you outside the bathroom, and you both head inside together."

    call set_the_scene(location = "bg_restaurant_bathroom") from _call_set_the_scene_9
    call send_Characters(Jean, "bg_restaurant_bathroom", behavior = "on_date") from _call_send_Characters_10

    "Good thing it's a private one."
    "She locks the door behind you."
        
    $ has_movement_control = False

    $ Jean.available_Actions = ["eat_pussy"]
    $ Jean.available_poses = ["masturbation"]

    $ chosen_Action = renpy.random.choice(Jean.available_Actions)
    $ chosen_pose = renpy.random.choice(Jean.available_poses)

    $ Jean.History.update("hookup")
        
    $ Jean.History.update(chosen_Action)
    
    call request_position(Jean, chosen_pose, automatic = True) from _call_request_position_12

    $ Action = ActionClass(chosen_Action, Player, Jean)

    call undress(Jean, "underwear") from _call_undress_18
    call start_Action(Action) from _call_start_Action_1
    call screen Action_screen(automatic = True)
    
    $ choice_disabled = False

    call change_Outfit(Jean, Jean.Wardrobe.Outfits[Jean.Outfit.name]) from _call_change_Outfit_27

    "After you both put your clothes back on, [Jean.name] leaves and heads back to the table."
    
    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_7
    call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_11

    "You wait a minute before leaving the bathroom as well."

    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_10

    $ Jean.change_face("sly", blush = 2)

    pause 1.0

    $ Jean.change_face("sexy")

    ch_Jean "That was a {i}lot{/i} of fun. . ."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_13
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_14

    $ Jean.available_Actions = []
    $ Jean.available_poses = []

    return

label Jean_date_movie:
    if second_event:
        if Jean in second_event.keys():
            $ Jean.change_face("smirk2", eyes = "right") 

            ch_Jean "I've really been in the mood to watch another movie."

            $ Jean.change_face("smirk2")

            ch_Jean "I heard there are a bunch of good ones out right now."
            ch_Player "Yeah, I wouldn't mind catching one."

            $ Jean.change_face("happy")

            ch_Jean "Then let's go!"

            $ Jean.change_face("smirk2", eyes = "right")

            "She grabs your hand, and you head to the theater together."

    if Player.location != "bg_mall":
        call remove_Characters(location = "bg_mall") from _call_remove_Characters_8
        call set_the_scene(location = "bg_mall") from _call_set_the_scene_11
        call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_12

    $ chosen_movie = None

    if "Girl_initiated" in Player.date_planned[Jean]:
        if renpy.random.random() > 0.25:
            if dice_roll > 0.50:
                $ chosen_movie = 2
            elif dice_roll > 0.25:
                $ chosen_movie = 1
            else:
                $ chosen_movie = 3
    elif "Player_initiated" in Player.date_planned[Jean]:
        if renpy.random.random() > 0.75:
            if dice_roll > 0.50:
                $ chosen_movie = 2
            elif dice_roll > 0.25:
                $ chosen_movie = 1
            else:
                $ chosen_movie = 3

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
        $ Jean.change_face("smirk2", eyes = "right")

        "You arrive at the ticket counter, and [Jean.name] looks over all the available movies."

        ch_Jean "Hmm. . ."
        ch_Jean "Why don't we see this one."

        $ Jean.change_face("smirk2")

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
        ch_Player "Sure."
    else:
        $ Jean.change_face("smirk2", eyes = "right")

        "You arrive at the ticket counter, and [Jean.name] looks over all the available movies."

        $ Jean.change_face("confused1", eyes = "right")

        pause 1.0

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean "I don't know which one to pick. . ."

        $ Jean.change_face("smirk2")

        ch_Jean "Why don't you choose this time, [Jean.Player_petname]?"

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

        $ Jean.change_face("confused1", mouth = "smirk", eyes = "right")

        ch_Jean "That one?"

        $ Jean.change_face("smirk2")

        ch_Jean "Sure, it looks good."

    menu:
        extend ""
        "Offer to pay":
            if "Player_initiated" in Player.date_planned[Jean]:
                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Player "I'll cover it."
                ch_Jean "Aw, [Jean.Player_petname], you don't have to. . ."

                $ Jean.change_face("smirk2")  

                ch_Player "Don't worry, I got it."
                ch_Jean "Thank you."

                $ Jean.change_face("smirk2", blush = 1)

                if Player.cash >= 2*ticket_price:
                    "You pay for the tickets." 
                    
                    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_15

                    $ Player.cash -= 2*ticket_price
                else:
                    "You realize you don't have enough money. . ." 
                    
                    $ Jean.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Jean.change_face("confused1", mouth = "smirk") 
                    
                    ch_Jean "If you didn't have enough, you should've just said so." 
                    "[Jean.name] pays the difference." 
                    
                    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_16

                    $ Player.cash = 0
            else:
                $ Jean.change_face("sly")

                ch_Jean "Nope, put your wallet away."
                ch_Jean "This date was my idea."
                ch_Player "Thanks, [Jean.petname]. . ."

                $ Jean.change_face("smirk2", blush = 1)

                ch_Jean "You're welcome, [Jean.Player_petname]."
                "[Jean.name] pays for the tickets."

                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_17
        "Recommend splitting the ticket price":
            if "Player_initiated" in Player.date_planned[Jean]:
                $ Jean.change_face("confused1", mouth = "smirk")

                ch_Player "Why don't we split the ticket price?"

                $ Jean.change_face("smirk2")

                ch_Jean "Oh alright, if you want to that badly."

                if Player.cash >= ticket_price:
                    "You both pay for the tickets."

                    $ Player.cash -= ticket_price
                else:
                    "You realize you don't have enough money to pay for half. . ." 
                    
                    $ Jean.change_face("confused1") 
                    
                    pause 1.0 
                    
                    $ Jean.change_face("confused1", mouth = "smirk") 
                    
                    ch_Jean "If you didn't have enough, you should've just said so." 
                    "[Jean.name] pays the difference." 
                    
                    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_18

                    $ Player.cash = 0
            else:
                $ Jean.change_face("sly")

                ch_Jean "Nope, put your wallet away."
                ch_Jean "This date was my idea."
                ch_Player "Thanks, [Jean.petname]. . ."

                $ Jean.change_face("smirk2", blush = 1)

                ch_Jean "You're welcome, [Jean.Player_petname]."
                "[Jean.name] pays for the tickets."

    call remove_Characters(location = "bg_movies") from _call_remove_Characters_9
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_12
    call send_Characters(Jean, "bg_movies", behavior = "on_date") from _call_send_Characters_13

    call expression f"Jean_date_movie_{movie_choice}" from _call_expression_4

    "With the movie over, you get up and leave the theater."

    return

label Jean_date_movie_ron_bic1:
    "You quickly find your seats, and the movie starts shortly after."
    "[Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("surprised1", eyes = "right")

    "Once the action starts, you look over to see [Jean.name] entranced by all the action on screen."
    "Ron Bic is in a sticky situation after he's unwittingly sent to kill the CEO of his favorite lighter company."
    "Ron quickly realizes a rival lighter company set him up, and he vows to get revenge."

    $ Jean.change_face("worried1", eyes = "right")

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_1
                "Just finish watching the movie":
                    pass

    "The movie continues, as Ron kills legions of men in the pursuit of revenge."
    "He has to fight his way through hundreds of evil henchmen in a lighter factory and finally takes out the real bad guy in the end."
    "There's a plethora of violent and fiery deaths as well as some impressive choreography."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "That was violent. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "Really well made, though."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_19
    call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_20

    return

label Jean_date_movie_ron_bic2:
    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "The first one was pretty good. . ."
    "You get seated just in time."
    "[Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("smirk2", eyes = "right")

    "After the events of the first movie, things are more dangerous than ever for our hero, Ron Bic."
    "The world's lighter making companies have been reeling from the deaths of so many important executives."
    "And they want to know who's responsible."

    $ Jean.change_face("worried1", eyes = "right")

    "Poor Ron can't seem to avoid trouble, as he has to kill dozens of people in an attempt to prevent everyone from learning of his terrible mistake. . ."
    "You look over to see [Jean.name] looking quite worried about Ron's predicament."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_2
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_3
                "Just finish watching the movie":
                    pass

    $ Jean.change_face("confused1", eyes = "right")

    "The movie continues and, unfortunately, Ron isn't fast enough, and the information gets out."

    $ Jean.change_face("neutral", eyes = "right")

    "Once the world knows that Ron killed the CEO of an allied lighter company, even if it was an accident, everyone he knows and loves turns on him."

    $ Jean.change_face("smirk2", eyes = "right")

    "In the end, after a crescendo of blood, gore, and fiery death, Ron Bic is able to clear his name. . ."

    $ Jean.change_face("angry1", eyes = "right")

    "But, did he survive? Does he even know of his own success?"

    $ Jean.change_face("furious", eyes = "right")

    ch_Jean "Really?!"

    $ Jean.change_face("angry1")

    ch_Jean "I hate cliffhangers."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_21
    call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_22

    return

label Jean_date_movie_hamburg_portfolio:
    "The previews are already over by the time you reach your seats."
    "[Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("smirk2", eyes = "right")

    "The movie is set in modern day Philadelphia, only. . . magic is real."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "right")

    "The main character is a wizard, but the world doesn't know about all things supernatural, so he has to lay low."
    "He tries to be a good person and help people with his gift, but it's never that easy."
    "It seems like whoever wrote the movie absolutely despises the main character, because they keep putting him in horrible situations and giving him insane amounts of trauma."

    $ Jean.change_face("worried1", eyes = "right")

    "Although, it is quite entertaining, as he uses his considerable talent with magic to kill his enemies in very creative ways."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_4
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_5
                "Just finish watching the movie":
                    pass

    $ Jean.change_face("confused1", eyes = "right")

    "As the movie continues, the main character is forced to confront his morality."
    "If he wants to save the people he loves, innocent people must die."

    $ Jean.change_face("worried2", eyes = "right")

    pause 1.0

    $ Jean.change_face("worried2")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right")

    "[Jean.name] glances at you a few times, as she watches the main character struggle so much with himself."
    "In the end, he isn't able to put aside his morals, and his inaction causes everyone to suffer."

    $ Jean.change_face("sad", eyes = "right")

    "At least he survives and gets revenge. . . however hollow it is. . ."

    $ Jean.change_face("worried1")

    ch_Jean "I hope we never have to make a decision like that. . ."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_23
    call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_24

    return

label Jean_date_movie_beautiful_flower:
    "You quickly find your seats."
    "[Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("smirk2", eyes = "right")

    "The movie is about a man who wanted to buy his mom some nice flowers for Mother's day."
    "He does this every year, but this time all the local florists are sold out."

    $ Jean.change_face("worried1", eyes = "right")

    "He's running around frantically trying to find flowers to buy because his mother is very ill."
    "This might be his last chance, ever, to give her flowers."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_6
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_7
                "Just finish watching the movie":
                    pass

    $ Jean.change_face("worried2", eyes = "right")

    "The movie continues and, as it turns out, the female lead only recently opened her own florist and has had trouble finding customers."
    "The guy has almost given up when he finally reaches her small hidden shop."
    "The shop's name is 'Beautiful flower.'"

    $ Jean.change_face("pleased2", eyes = "right")

    "[Jean.name] seems quite happy about the story's happy ending."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "That was really sweet. . ."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_25

    return

label Jean_date_movie_fated:
    "You get seated and [Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "right")

    "The movie starts out as a simple romance between two coworkers."
    "Admiring each other from a distance, they never interacted much at work."
    "That is until they were unwittingly set up on a blind date with each other."

    $ Jean.change_face("smirk2", eyes = "right")

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_8
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_9
                "Just finish watching the movie":
                    pass

    $ Jean.change_face("surprised2", eyes = "right")

    "As the movie continues, it quickly takes a turn away from the wholesome, as the two mutually agree not to start a relationship."

    $ Jean.change_face("sexy", eyes = "right", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", eyes = "right", blush = 1)

    "Instead the two become friends with benefits, ending the night with a very graphic sex scene."

    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_26 

    "There are many, very graphic sex scenes, as the two continue denying their romantic feelings for each other."
    "Eventually they do officially get together, and the movie ends."

    $ Jean.change_face("sexy", blush = 2)

    ch_Jean "I'm glad they officially got together in the end. . ."

    $ Jean.change_face("sexy", eyes = "squint", blush = 2)

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_27
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_28

    return

label Jean_date_movie_refilling_empty_glass:
    "You get seated and [Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("smirk1", eyes = "right")

    "It begins following a bartender at a popular spot in the city."

    $ Jean.change_face("confused1", eyes = "right") 

    "The bartender is good at her job and beautiful, so plenty of male customers try flirting with her to no avail."

    $ Jean.change_face("worried1", eyes = "right") 

    "She was recently widowed." 
    "She's been struggling to move on from her husband's death, until one night she spots a despondent man sitting at the far end of the bar."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_10
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_11
                "Just finish watching the movie":
                    pass

    "The movie continues, and the bartender becomes interested in the despondent man, since he looks similar to her late husband."

    $ Jean.change_face("surprised1", eyes = "right") 

    "He tells her about his plight, how a former business partner started a conspiracy against him and it's ruining his life."

    $ Jean.change_face("pleased2", eyes = "right", blush = 2)

    "The chance meeting turns into a thrilling romance as they rapidly fall in love, and the bartender uses her skills as a former super spy to stop the conspiracy."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 2)

    "Nearly every other minute there's a graphic sex scene as the bartender demonstrates her prowess to her new beau."

    $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Jean "That was really good. . ."
    ch_Jean "That lead actress was a badass."

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "I bet you thought she was hot."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_29
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_30

    return

label Jean_date_movie_stale_air:
    "The movie starts only a few minutes after you get seated, and [Jean.name] starts holding your hand."

    $ Jean.change_face("smirk1", eyes = "right")

    "The story is about a struggling writer who can't find any passion or inspiration for his stories."

    $ Jean.change_face("confused1", eyes = "right")

    "The writer's monotonous life goes on as normal until he starts finding messages and sticky notes appearing out of nowhere around his apartment."

    $ Jean.change_face("surprised1", eyes = "right")

    "He has no idea where they're coming from, but they all have great ideas which he uses to jumpstart his writing."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_12
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_13
                "Just finish watching the movie":
                    pass

    "As the movie continues, it quickly becomes clear what's going on."
    "Unbeknownst to the writer, a carbon monoxide leak in his apartment is simultaneously poisoning him, while also the cause for his inspiration."

    $ Jean.change_face("worried1", eyes = "right")

    "His imaginative writing lands him a new job, but the gas also starts causing him to become delusional."

    $ Jean.change_face("sad", eyes = "right")

    "The movie climaxes as the writer unknowingly acts out his latest story. . ."
    "Which is about a disturbed maniac who goes on a murder spree at their new job."

    $ Jean.change_face("worried1")

    ch_Jean "That was. . . disturbing. . ."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_31
    call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_32

    return

label Jean_date_movie_devils_spring_break:
    "You take your seats, and [Jean.name] holds your hand as the movie starts."

    $ Jean.change_face("confused1", eyes = "right")

    "The movie seems to follow a generic horror movie formula, with reckless college kids and everything."

    $ Jean.change_face("neutral", eyes = "right")

    "One of the college students has a rich family, and they just bought a new summer home, one that of course is rumored to be haunted."
    "The rich kid brings a bunch of his friends down to the house, to spend their spring break getting drunk and partying."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "I can tell where this is going. . ."
    "Despite the rumors, the house isn't actually haunted. . . at least not by ghosts."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_14
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_15
                "Just finish watching the movie":
                    pass

    $ Jean.change_face("surprised1", eyes = "right")

    "As the movie continues, the college students are slowly and gruesomely killed by a demon, their souls stolen in the process."

    $ Jean.change_face("worried1", eyes = "right")

    "They try to put up a fight, after they sober up enough to realize how fucked they are."
    "During one particularly tense moment, you look over and see [Jean.name] wide-eyed, staring at the screen in suspense."

    $ Jean.change_face("worried3", eyes = "right")

    "Suddenly, there's a jumpscare, and she squeezes your hand, leaning into you for comfort."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "They were pretty annoying. . ."

    $ Jean.change_face("worried1")

    ch_Jean "But I still felt kinda bad for them."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_33

    return

label Jean_date_movie_unsanctioned_crusade:
    "You take your seats just as the final preview ends."
    "[Jean.name] starts holding your hand as the movie starts."

    $ Jean.change_face("surprised1", eyes = "right")

    "The movie starts on a high note, as it instantly earns its 'R' rating."

    $ Jean.change_face("worried1", eyes = "right")

    "It's set in medieval Europe and starts with a massacre."
    "Although, despite being bloody, the massacre is rather mundane, as it was perpetrated by an order of deeply religious knights."

    $ Jean.change_face("confused1", eyes = "right") 

    "The knights are on their own form of crusade, driven by deep seated religious beliefs."
    "They do terrible things in a misguided attempt at worship."
    "Only, God is real and is less than pleased by these atrocities."

    if Player.stamina and Jean.stamina:
        if (Jean.status["horny"] or Jean.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Jean

            call Jean_date_movie_sex from _call_Jean_date_movie_sex_16
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Jean_date_movie_sex from _call_Jean_date_movie_sex_17
                "Just finish watching the movie":
                    pass

    $ Jean.change_face("worried1", eyes = "right")

    "As the movie continues, the knights are plagued by various, horrifying, heavenly tribulations."
    "It starts slowly at first, suspense building, as the knights are mercilessly terrorized."

    $ Jean.change_face("sad", eyes = "right")

    "The knights are directly confronted by the atrocities they themselves committed and systematically eradicated in cruel and disturbing fashion."

    $ Jean.change_face("worried1")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "I guess they deserved it. . ." 

    call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_34

    return

label Jean_date_movie_sex:
    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    "You notice [Jean.name] looking at you seductively."

    if sex_initiator == Player:
        menu:
            extend ""
            "Ask if she wants to make out" if Jean.History.check("makeout"):
                $ sex_act = "makeout"
            "Ask for a handjob" if Jean.History.check("handjob"):
                $ sex_act = "handjob"
            "Ask if you can put a hand down her pants" if Jean.History.check("touch_pussy") and Jean.History.check("seen_pussy"):
                $ sex_act = "touch_pussy"
            "Ask if you can finger her" if Jean.History.check("finger_pussy"):
                $ sex_act = "finger_pussy"
            "Ask for a blowjob" if Jean.History.check("blowjob") and Jean.History.check("swallow_cum"):
                $ sex_act = "blowjob"
            "Decide against it":
                return
    elif sex_initiator == Jean:
        $ sex_acts = []

        if Jean.History.check("makeout"):
            $ sex_acts.append("makeout")

        if Jean.History.check("handjob"):
            $ sex_acts.append("handjob")

        if Jean.History.check("touch_pussy") and Jean.History.check("seen_pussy"):
            $ sex_acts.append("touch_pussy")

        if Jean.History.check("finger_pussy"):
            $ sex_acts.append("finger_pussy")

        if Jean.History.check("blowjob") and Jean.History.check("swallow_cum"):
            $ sex_acts.append("blowjob")

        if sex_acts:
            if Jean.quirk:
                ch_Jean "Just try and relax." 
                ch_Jean "Your big sister is gonna make you feel {i}really{/i} good."

            menu:
                extend ""
                "Go along with it":
                    $ sex_act = renpy.random.choice(sex_acts)
                "Not right now, [Jean.petname].":
                    $ Jean.change_face("worried1", blush = 1)
                    
                    ch_Jean "Oh alright."

                    return

    call expression f"Jean_date_movie_sex_{sex_act}" from _call_expression_5

    return

label Jean_date_movie_sex_makeout:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1) 

    "Once [Jean.name]'s sure there's nobody around, she reaches over and pulls you in."

    $ Jean.change_face("kiss1", blush = 1)

    "The movie plays on in the background, as the two of you lock lips, your tongues dancing in each other's mouth."

    $ Jean.change_face("kiss2", blush = 2)

    "She has one hand firmly around your neck, preventing you from going anywhere."
    "[Jean.name] takes your hand, running it across her body."

    $ Jean.change_face("sexy", blush = 1)

    "Before things go too far, [Jean.name] stops herself and pulls away."
    ch_Jean "Mmm. . ."
    ch_Jean "I can never get enough of you, [Jean.Player_petname]."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_35
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_36

    return

label Jean_date_movie_sex_handjob:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1) 

    "Once [Jean.name]'s sure there's nobody around, she reaches over."

    if sex_initiator == Jean:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], what exactly are you doing. . . ?"

    "She starts teasing you, making it quite difficult to focus on the movie."

    $ Jean.change_face("sexy", eyes = "right", blush = 1)

    "Once you're hard enough for her, she takes your cock out, wrapping her fingers around you."
    "You try to continue watching the movie, but [Jean.name] keeps speeding up."

    if Jean.History.check("handjob") >= 11:
        "She knows exactly what she's doing now, so you know it's intentional when she teases you, and you're barely able to hold it in after mere moments."
    elif Jean.History.check("handjob") >= 5:
        "She's getting better, more gentle, but is still figuring things out, so it takes a while before you're on the edge."    
    else:
        "She has a death grip and is a bit too rough, but it brings you to the edge all the same."

    $ Player.desire = 75

    "[Jean.name] can tell you're getting close and slows down, lessening her grip until she's barely touching you."
    "She teases you and makes you twitch for a long while before she's satisfied."

    $ Player.desire = 90

    "Finally, she gets back to it, and you can't hold it in any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0

    if Jean.History.check("swallow_cum"):
        "Just as you're about to cum, she leans over." 
        
        call hide_Character(Jean) from _call_hide_Character_4
        
        "You feel her lips wrap around your cock right as you cum." 
        ch_Jean "*gulp*" 
        "She makes sure to swallow it all and licks you clean afterwards." 

        call add_Characters(Jean) from _call_add_Characters_20

        $ Jean.History.update("swallow_cum")
    else:
        "She takes a napkin and cleans everything up after you're done."

        $ Jean.History.update("clean_cum")

    $ Jean.change_face("sexy", blush = 1)

    "She puts your pants back into position."

    if Jean.History.check("swallow_cum", tracker = "recent") and renpy.random.random() > 0.5:
        $ Jean.spunk["chin"] = True

    $ Jean.change_face("sexy", blush = 2)

    if Jean.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Jean) from _call_swallow_cum_2

        $ Jean.change_face("sly", blush = 2)

        ch_Jean "*gulp*"

    ch_Jean "I love making you twitch."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_37
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_38

    return

label Jean_date_movie_sex_touch_pussy:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1) 

    "Once you're sure nobody's around, you reach over."
    "You can instantly feel how wet she is, as you slowly move your hand over her crotch."

    $ Jean.change_face("sexy", eyes = "right", blush = 1)
    call expose(Jean, "pussy") from _call_expose

    "Slipping your hand under her pants, you tease her for a bit, before getting right to work."

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Jean "Oh. . . [Jean.Player_petname]. . ."
    "[Jean.name] tries to continue watching the movie, but she seems more focused on suppressing any moans."
    "You make sure to give every part of her pussy ample attention."

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

    "Whatever you're doing seems to be working as she starts squirming and grinding against your hand."
    "She also reaches over and starts teasing you as well."

    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 3)

    "You pick up the pace, and [Jean.name] grabs your arm, holding it in place."
    "She's not letting go until you finish the job."

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 3)

    ch_Jean "*gasp*" with small_screenshake

    $ Jean.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 3)

    "She finally reaches the climax and can't help but violently shudder." with small_screenshake
    "You don't stop, and the shuddering continues, her grip on your arm tightening." with small_screenshake

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    "Finally, after a minute, she lets go."
    "She's still twitching even as you pull your hand away."

    call change_Outfit(Jean, Jean.Wardrobe.Outfits[Jean.Outfit.name]) from _call_change_Outfit

    ch_Jean "God. . ."
    ch_Jean "You make me feel so amazing."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_39
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_40

    return

label Jean_date_movie_sex_finger_pussy:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1) 

    "Once you're sure nobody's around, you reach over."
    "You can instantly feel how wet she is, as you slowly move your hand over her crotch."

    $ Jean.change_face("sexy", eyes = "right", blush = 1)
    call expose(Jean, "pussy") from _call_expose_1

    "Slipping your hand under her pants, you tease her for a bit, before sliding your fingers inside."

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Jean "Oh. . . [Jean.Player_petname]. . ."
    "[Jean.name] tries to continue watching the movie, but she seems more focused on suppressing any moans."
    "Your fingers slide in and out while your thumb teases her clit."

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 3)

    "Whatever you're doing seems to be working as she starts squirming and grinding against your hand."
    "She also reaches over and starts teasing you as well."

    $ Jean.change_face("surprised2", mouth = "lipbite", blush = 3)

    "You pick up the pace, and [Jean.name] grabs your arm, holding it in place."
    "She's not letting go until you finish the job."

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 3)

    ch_Jean "*gasp*" with small_screenshake

    $ Jean.change_face("worried1", eyes = "closed", mouth = "lipbite", blush = 3)

    "She finally reaches the climax and can't help but violently shudder." with small_screenshake
    "You don't stop, and the shuddering continues, her grip on your arm tightening." with small_screenshake

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    "Finally, after a minute, she lets go."
    "She's still twitching even as you pull your hand away."

    call change_Outfit(Jean, Jean.Wardrobe.Outfits[Jean.Outfit.name]) from _call_change_Outfit_1

    ch_Jean "God. . ."
    ch_Jean "You make me feel so amazing."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_41
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_42

    return

label Jean_date_movie_sex_blowjob:
    $ Jean.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1)

    call hide_Character(Jean) from _call_hide_Character_5

    "The theater is basically empty, and nobody's anywhere near the two of you."

    if sex_initiator == Jean:
        $ temp = Jean.petname.capitalize()

        ch_Player "[temp], what exactly are you doing. . . ?"

    "[Jean.name] leans over and starts teasing you."
    "Once you're hard enough for her, she starts undoing your pants, taking your cock out."
    "She teases you some more, before getting to work, wrapping her lips around you."
    ch_Jean "*slurp*"
    "You hold her hair out of the way, and she starts speeding up."

    if Jean.History.check("blowjob") >= 11:
        "By now, she knows exactly what gets you going and is able to bring you to the edge in mere moments."
    elif Jean.History.check("blowjob") >= 5:
        "She's getting better, but still fumbles around a bit with her hands, yet you're about to lose control faster than ever."
    else:
        "She still fumbles around quite a bit, showing her lack of experience, but it brings you to the edge all the same."

    $ Player.desire = 75

    "[Jean.name] can tell you're close and stops what she's doing."
    "She continues teasing you for a while, causing you to twitch."

    $ Player.desire = 90
    
    "Finally, she has mercy on you and continues until you can't hold on any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0
    
    ch_Jean "*slurp*"
    "She pulls back a bit, holding your cock in her mouth as you cum."
    ch_Jean "*gulp*"
    "[Jean.name] starts sucking again, trying to squeeze out every last drop."
    "You twitch involuntarily until she's finally satisfied and pulls away."
    "She puts your pants back into position, before getting up."

    if renpy.random.random() > 0.5:
        $ Jean.spunk["chin"] = True

    call add_Characters(Jean) from _call_add_Characters_80

    $ Jean.change_face("sexy", blush = 2)

    if Jean.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Jean.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 2)

        call swallow_cum(Jean) from _call_swallow_cum_3

        $ Jean.change_face("sly", blush = 2)

        ch_Jean "*gulp*"

    ch_Jean "You taste {i}really{/i} good."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_43
    call change_Girl_stat(Jean, "desire", 0) from _call_change_Girl_stat_44

    $ Jean.History.update("swallow_cum")

    return

label Jean_date_mall:
    if Jean in second_event.keys():
        $ Jean.change_face("smirk2", eyes = "right") 

        pause 1.0

        $ Jean.change_face("smirk2")

        ch_Jean "I kinda just want to hang out around the mall."

        $ Jean.change_face("smirk2", eyes = "right")

        ch_Player "Could be fun."

        if renpy.random.random() > 0.5 or Player.cash < 10:
            ch_Jean "C'mon, let's wander around."

            $ second_event[Jean] = "wander"
        else:
            $ Jean.change_face("happy", brows = "raised", eyes = "right") 
            
            ch_Jean "Oh, look!" 
            
            $ Jean.change_face("smirk2") 
            
            ch_Jean "We gotta get dessert too."

            $ second_event[Jean] = "dessert"

        "She grabs your hand, and you walk through the mall."
    elif Player in second_event.keys():
        menu:
            "How about we stay in the mall and. . ."
            ". . . wander around.":
                $ second_event[Player] = "wander"
            ". . . grab dessert." if Player.cash >= 10:
                $ second_event[Player] = "dessert"

        $ Jean.change_face("smirk2") 
        
        ch_Jean "Okay, sure."

    if (Player in second_event.keys() and second_event[Player] == "wander") or (Jean in second_event.keys() and second_event[Jean] == "wander"):
        call Jean_date_mall_wander from _call_Jean_date_mall_wander
    elif (Player in second_event.keys() and second_event[Player] == "dessert") or (Jean in second_event.keys() and second_event[Jean] == "dessert"):
        call Jean_date_mall_dessert from _call_Jean_date_mall_dessert

    return

label Jean_date_mall_wander:
    $ Jean.change_face("smirk1", eyes = "right")

    "Without any specific destination in mind, you wander around the mall with [Jean.name]."

    $ Jean.change_face("smirk2", eyes = "right")

    "She's quite animated, as you have a pleasant conversation about any and everything that comes to mind."

    $ holding_hands = False

    if Player in second_event.keys() and Jean in Partners:
        menu:
            extend ""
            "Ask [Jean.name] if you can hold hands.":
                $ Jean.change_face("confused1", mouth = "smirk")

                ch_Jean "I was waiting for you to ask, [Jean.Player_petname]. . ." 
                
                $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "right", blush = 1) 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_45
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_46 

                $ holding_hands = True
            "Just grab [Jean.name]'s hand.": 
                $ Jean.change_face("sly")

                "She doesn't protest and just gives your hand a squeeze in response." 
                
                $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "right", blush = 1) 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_47

                $ holding_hands = True
            "Do nothing":
                pass
    elif Jean in second_event.keys() and Jean in Partners:
        $ Jean.change_face("smirk2", eyes = "right", mouth = "lipbite")

        pause 1.0

        $ Jean.change_face("smirk2", eyes = "left", mouth = "lipbite")

        pause 1.0

        $ Jean.change_face("sly", mouth = "lipbite")

        ch_Jean "Gimme your hand, [Jean.Player_petname]."
        "You put your hand out, and she starts holding it, interlacing your fingers."

        $ Jean.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 1)

        $ holding_hands = True

    if holding_hands:
        "She squeezes your hand tightly and inches even closer, as you continue walking alongside each other."

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)

    "Time flies by, spent well, doing nothing much at all aside from being close to each other."

    call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_48

    return

label Jean_date_mall_dessert:
    $ Jean.change_face("smirk1", eyes = "right")

    "Being in a mall provides a number of opportunities and problems, simultaneously."
    "There are so many different options that it can be difficult to decide what to get." 

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "You in the mood for anything, [Jean.Player_petname]?"
    ch_Player "How about. . ."

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

    $ Jean.change_face("smirk2", eyes = "right")

    "After paying for the dessert, you both wander around the mall while enjoying it."

    $ Jean.change_face("smirk1", eyes = "down", mouth = "lipbite")

    "Looks like you chose well, as [Jean.name] looks like she's enjoying the dessert quite a lot."

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)

    "Even after finishing, you spend a while just walking and talking."
    "Time flies by."

    return

label Jean_date_end:
    if "Player_initiated" in Player.date_planned[Jean]:
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_10
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_13
        call send_Characters(Jean, "bg_hallway", behavior = "on_date") from _call_send_Characters_16

        $ Jean.change_face("confused1", mouth = "smirk")

        menu:
            extend ""
            "Invite her into your room":
                call Jean_date_end_invite from _call_Jean_date_end_invite
            "Give her a goodnight kiss":
                call Jean_date_end_goodnight from _call_Jean_date_end_goodnight
    else:
        call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_11
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_14
        call send_Characters(Jean, "bg_girls_hallway", behavior = "on_date") from _call_send_Characters_17

        if Jean.status["horny"] or Jean.status["nympho"]:
            call Jean_date_end_invite from _call_Jean_date_end_invite_1
        elif renpy.random.random() > 0.25:
            call Jean_date_end_invite from _call_Jean_date_end_invite_2
        else:
            call Jean_date_end_goodnight from _call_Jean_date_end_goodnight_1

    return

label Jean_date_end_invite:
    if Player.location == "bg_hallway":
        $ Jean.change_face("sly")

        ch_Player "Come on in."

        call remove_Characters(location = Player.home) from _call_remove_Characters_12
        call set_the_scene(location = Player.home) from _call_set_the_scene_15
        call send_Characters(Jean, Player.home, behavior = "on_date") from _call_send_Characters_18
        
        if Jean.status["horny"] or Jean.status["nympho"]:
            $ Jean.change_face("sexy", blush = 1) 
            
            ch_Jean "That was nice." 
            
            $ Jean.change_face("sly", blush = 2) 
            
            ch_Jean "But I think it's time for some fun. . ."
        else:
            $ Jean.change_face("smirk2", eyes = "right") 
            
            ch_Jean "Every date with you is so much fun." 
            
            $ Jean.change_face("smirk2") 

        menu:
            extend ""
            "Recommend something {i}fun{/i}" if approval_check(Jean, threshold = "hookup"):
                $ Jean.History.update("hookup")

                call screen Action_screen(automatic = True)
                
                $ choice_disabled = False

                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Jean "I'm sleeping over tonight, right?"

                $ Jean.change_face("smirk2") 

                ch_Player "Of course."
            "Invite her to sleep over" if Jean.History.check("sleepover"):
                $ Jean.change_face("confused1", mouth = "smirk") 
                
                pause 1.0 
                
                $ Jean.change_face("sexy") 
                
                ch_Jean "Is [Jean.Player_petname] tired?" 
                ch_Jean "Don't worry, I'll keep you company tonight."
            "Say goodnight":
                $ Jean.change_face("kiss1", blush = 1) 
                
                "She pulls you into a brief kiss." 
                
                $ Jean.change_face("sexy") 
                
                ch_Jean "Fine, goodnight, [Jean.Player_petname]."

                $ Jean.History.update("kiss")

                call send_Characters(Jean, Jean.home) from _call_send_Characters_19
    elif Player.location == "bg_girls_hallway":
        $ Jean.change_face("sly", mouth = "lipbite")

        ch_Jean "I think you should come inside."

        if approval_check(Jean, threshold = "hookup"):
            $ Jean.change_face("sexy", blush = 1)

            ch_Jean "We have unfinished business."

        menu:
            extend ""
            "Go inside with her":
                call Jean_date_invite_accept from _call_Jean_date_invite_accept
            "Say goodnight":
                call Jean_date_invite_reject from _call_Jean_date_invite_reject

    return

label Jean_date_invite_accept:
    "[Jean.name] grabs you by the hand and drags you inside the room."

    call remove_Characters(location = Jean.home) from _call_remove_Characters_13
    call set_the_scene(location = Jean.home) from _call_set_the_scene_16
    call send_Characters(Jean, Jean.home, behavior = "on_date") from _call_send_Characters_20

    $ Jean.change_face("sexy", blush = 2)

    ch_Player "What did you have in mind?"

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    if approval_check(Jean, threshold = "hookup"):
        $ Jean.History.update("hookup")

        call screen Action_screen(automatic = True)
        
        $ choice_disabled = False

        if approval_check(Jean, threshold = "sleepover"):
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Jean "You're sleeping over tonight, right?"

            menu:
                extend ""
                "I can.":
                    $ Jean.change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    ch_Jean "Good, I love when you keep me company."
                "Not tonight.":
                    $ Jean.change_face("worried1") 
                    
                    ch_Jean "Oh alright." 
                    
                    $ Jean.change_face("smirk2") 
                    
                    ch_Jean "Goodnight, [Jean.Player_petname]."
                    ch_Jean "I'll see you tomorrow."

                    call remove_Characters(location = Player.home) from _call_remove_Characters_14
                    call set_the_scene(location = Player.home) from _call_set_the_scene_17
        else:
            $ Jean.change_face("smirk2") 
            
            ch_Jean "Goodnight, [Jean.Player_petname]."
            ch_Jean "I'll see you tomorrow."

            call remove_Characters(location = Player.home) from _call_remove_Characters_15
            call set_the_scene(location = Player.home) from _call_set_the_scene_18
    else:
        $ Jean.change_face("kiss1", blush = 1) 
        
        "She pulls you in for a kiss." 
        
        $ Jean.change_face("sexy") 
        
        ch_Jean "Goodnight, [Jean.Player_petname]."

        $ Jean.History.update("kiss")

        call remove_Characters(location = Player.home) from _call_remove_Characters_63
        call set_the_scene(location = Player.home) from _call_set_the_scene_131

    return

label Jean_date_invite_reject:
    $ Jean.change_face("worried1")

    ch_Player "Sorry, not tonight, [Jean.petname]."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "Fine, but first you have to give me a kiss. . ."

    $ Jean.change_face("kiss1", blush = 1)

    "She pulls you into a brief kiss, before pulling away."

    $ Jean.change_face("sexy")

    ch_Jean "I'll see you tomorrow, [Jean.Player_petname]."

    $ Jean.History.update("kiss")

    call send_Characters(Jean, Jean.home) from _call_send_Characters_21
    call remove_Characters(location = Player.home) from _call_remove_Characters_16
    call set_the_scene(location = Player.home) from _call_set_the_scene_19

    return

label Jean_date_end_goodnight:
    if Player.location == "bg_hallway":
        $ Jean.change_face("kiss1", blush = 1)

        "You pull [Jean.name] into a brief kiss."
        "She holds on for a moment, groping your ass, before letting go."

        $ Jean.change_face("sexy")

        ch_Player "Goodnight, [Jean.petname]."
        ch_Jean "Goodnight, [Jean.Player_petname]."
        ch_Jean "You'll see me tomorrow."
    else:
        $ Jean.change_face("sexy")

        pause 1.0

        $ Jean.change_face("kiss1", blush = 1)

        "[Jean.name] grabs you by the collar and pulls you into a kiss."
        "Her hands wander across your body."
        "After a long moment, she pulls away."

        $ Jean.change_face("sexy")

        ch_Jean "I love going on dates with you."
        ch_Jean "Goodnight, [Jean.Player_petname]."
        ch_Jean "You'll see me tomorrow."

    $ Jean.History.update("kiss")

    call send_Characters(Jean, Jean.home) from _call_send_Characters_22
    call remove_Characters(location = Player.home) from _call_remove_Characters_17
    call set_the_scene(location = Player.home) from _call_set_the_scene_20

    return