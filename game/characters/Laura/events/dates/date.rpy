init python:

    import math

    def Laura_date():
        label = "Laura_date"

        conditions = [
            "Laura in Player.date_planned.keys() and 'primary' in Player.date_planned[Laura]",

            "Laura.History.check('went_on_date_with_Player') >= 1",

            "time_index == 2"]

        waiting = True
        traveling = True

        priority = 99
        repeatable = True

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority, repeatable = repeatable)

label Laura_date:
    $ ongoing_Event = True

    hide screen phone_screen

    if weather == "rain":
        $ weather = None

    $ Party = []

    if Player.location != "bg_hallway":
        "You have a date with [Laura.name]: better go and wait for her outside your room."

        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_66
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_73

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed

    "You only have to wait for a few seconds before [Laura.name] appears out of thin air."

    call send_Characters(Laura, "bg_hallway", behavior = "on_date") from _call_send_Characters_63

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Player "Where do you even come from. . . ?"
    "She ignores your question."

    $ Laura.change_face("neutral", eyes = "right")

    "As usual, she grabs you by the wrist and drags you along."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_67
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_74
    call send_Characters(Laura, "bg_campus", behavior = "on_date") from _call_send_Characters_64

    $ Laura.change_face("smirk2", eyes = "right")

    "On the walk to your date, you chat with [Laura.name], telling her about your day."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_68
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_75
    call send_Characters(Laura, "bg_mall", behavior = "on_date") from _call_send_Characters_65

    $ Laura.change_face("neutral")

    $ first_event = {}
    $ second_event = {}

    if "Girl_initiated" in Player.date_planned[Laura]:
        if renpy.random.random() > 0.5:
            ch_Laura "I want to go to dinner."

            $ first_event[Laura] = "dinner"

            call Laura_date_dinner from _call_Laura_date_dinner
        else:
            ch_Laura "I want to see a movie."
            ch_Laura "Let's go."

            $ first_event[Laura] = "movie"

            call Laura_date_movie from _call_Laura_date_movie
    else:
        ch_Laura "What are we doing?"

        menu:
            extend ""
            "Let's grab some dinner first.":
                ch_Laura "Fine."

                $ first_event[Player] = "dinner"

                call Laura_date_dinner from _call_Laura_date_dinner_1
            "Let's go catch a movie.":
                ch_Laura "Fine."

                $ first_event[Player] = "movie"

                call Laura_date_movie from _call_Laura_date_movie_1
            "Actually. . . can we just chill, hang out here?":
                ch_Laura "You know I don't care either way."
                        
                $ Player.date_planned = {}

                $ ongoing_Event = False

                return

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_69
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_76
    call send_Characters(Laura, "bg_mall", behavior = "on_date") from _call_send_Characters_66

    if "Girl_initiated" in Player.date_planned[Laura]:
        if renpy.random.random() > 0.25:
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                if (Player in first_event.keys() and first_event[Player] == "dinner") or (Laura in first_event.keys() and first_event[Laura] == "dinner"):
                    $ second_event[Laura] = "movie"
                elif (Player in first_event.keys() and first_event[Player] == "movie") or (Laura in first_event.keys() and first_event[Laura] == "movie"):
                    $ second_event[Laura] = "dinner"
            elif dice_roll > 0.125:
                $ second_event[Laura] = "mall"
            else:
                $ second_event[Laura] = "end"
    elif "Player_initiated" in Player.date_planned[Laura]:
        if renpy.random.random() > 0.75:
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                if (Player in first_event.keys() and first_event[Player] == "dinner") or (Laura in first_event.keys() and first_event[Laura] == "dinner"):
                    $ second_event[Laura] = "movie"
                elif (Player in first_event.keys() and first_event[Player] == "movie") or (Laura in first_event.keys() and first_event[Laura] == "movie"):
                    $ second_event[Laura] = "dinner"
            elif dice_roll > 0.125:
                $ second_event[Laura] = "mall"
            else:
                $ second_event[Laura] = "end"

    if not second_event:
        $ Laura.change_face("neutral", eyes = "right") 

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "What are we doing next?"
        ch_Laura "You're picking."

        menu:
            extend ""
            "Let's grab dinner. . ." if (Player in first_event.keys() and first_event[Player] == "movie") or (Laura in first_event.keys() and first_event[Laura] == "movie"):
                $ second_event[Player] = "dinner"

                call Laura_date_dinner from _call_Laura_date_dinner_2
            "Let's head to the movie theater." if (Player in first_event.keys() and first_event[Player] == "dinner") or (Laura in first_event.keys() and first_event[Laura] == "dinner"):
                ch_Laura "Fine." 
                ch_Laura "I'm starting to look forward to these 'movies.'" 

                $ second_event[Player] = "movie"

                call Laura_date_movie from _call_Laura_date_movie_2
            "How about we stay in the mall and. . .":
                $ second_event[Player] = "mall"

                call Laura_date_mall from _call_Laura_date_mall
            "Want to head back to the Institute?":
                $ Laura.change_face("sly") 
                
                ch_Laura "Want to finish the date in private?" 
                ch_Laura "Fine, let's go."

                $ second_event[Player] = "end"
    else:
        if Laura in second_event.keys():
            if second_event[Laura] == "dinner":
                call Laura_date_dinner from _call_Laura_date_dinner_3
            elif second_event[Laura] == "movie":
                call Laura_date_movie from _call_Laura_date_movie_3
            elif second_event[Laura] == "mall":
                call Laura_date_mall from _call_Laura_date_mall_1
            elif second_event[Laura] == "end":
                $ Laura.change_face("sexy", eyes = "right") 

                pause 1.0

                $ Laura.change_face("sly")

                ch_Laura "Let's go."

                $ Laura.change_face("sexy", eyes = "right")

                "She grabs your wrist and starts leading you out of the mall."
                ch_Player "Wh-"

                if Laura.status["horny"] or Laura.status["nympho"]:
                    if (Player in first_event.keys() and first_event[Player] == "dinner") or (Laura in first_event.keys() and first_event[Laura] == "dinner"):
                        $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 
                        
                        ch_Laura "You're next on the menu." 
                        
                    $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 1) 
                    
                    pause 1.0 
                        
                    $ Laura.change_face("sly", mouth = "lipbite", blush = 1) 
                    
                    ch_Laura "We've already wasted enough time here." 
                    
                    $ Laura.change_face("sexy", eyes = "right")
                else:
                    ch_Laura "We'll finish our date back at the Institute."

    if Player.location != "bg_mall":
        $ fade_to_black(0.4)

        $ time_index = 3

        $ lighting = "night"

        call remove_Characters(location = "bg_mall") from _call_remove_Characters_70
        call set_the_scene(location = "bg_mall") from _call_set_the_scene_77
        call send_Characters(Laura, "bg_mall", behavior = "on_date") from _call_send_Characters_67

    $ Laura.change_face("smirk2")

    ch_Laura "Let's go."

    $ Laura.change_face("smirk2", eyes = "left")

    "She grabs your wrist and pulls you along."

    $ fade_to_black(0.4)

    "You walk back to the Institute together."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_71
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_78
    call send_Characters(Laura, "bg_campus", behavior = "on_date") from _call_send_Characters_68

    "You continue to chat and enjoy each other's company as you head back into the dorms."

    call Laura_date_end from _call_Laura_date_end

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

    if Laura.location == Player.location:
        jump go_to_sleep
    # else:
    #     call move_location(Player.location) from _call_move_location_13

    return

label Laura_date_dinner:
    if second_event:
        if Laura in second_event.keys():
            $ Laura.change_face("smirk2", eyes = "right", mouth = "lipbite")

            pause 1.0

            $ Laura.change_face("smirk2", mouth = "lipbite")

            ch_Laura "I smell something good."
            ch_Laura "It's making me hungry."

            $ Laura.change_face("smirk2")

            ch_Laura "Let's go, we're getting dinner."

            $ Laura.change_face("smirk2", eyes = "right")

            ch_Player "Wh-"
            "She just grabs your wrist and drags you to the restaurant."
            
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Laura "I want red meat."

                $ cuisine = "steakhouse"
            elif dice_roll == 2:
                ch_Laura "I'm in the mood for fish."

                $ cuisine = "seafood"
            elif dice_roll == 3:
                ch_Laura "We're getting Southern food." 
                
                $ Laura.change_face("smirk2") 
                
                ch_Laura "I think I enjoy the spiciness. . ."

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

            ch_Laura "Good." 
            
            $ Laura.change_face("sly") 
            
            ch_Laura "I was getting hungry." 
    else:
        if Laura in first_event.keys():
            $ dice_roll = renpy.random.randint(1, 3)

            if dice_roll == 1:
                ch_Laura "We're going to the steakhouse again." 
                ch_Laura "I want red meat."

                $ cuisine = "steakhouse"
            elif dice_roll == 2:
                ch_Laura "We're going to that seafood place." 
                ch_Laura "I'm in the mood for fish."

                $ cuisine = "seafood"
            elif dice_roll == 3:
                ch_Laura "We're getting Southern food." 
                
                $ Laura.change_face("smirk2") 
                
                ch_Laura "I think I enjoy the spiciness. . ."

                $ cuisine = "southern"
        elif Player in first_event.keys():
            ch_Laura "Where are we eating?"

            $ Laura.change_face("neutral", eyes = "squint")

            ch_Player "Were you in the mood for anything?"
            ch_Laura "You. Pick."
            ch_Player "Okay. . . then. . ."

            menu:
                extend ""
                "Let's go to that steakhouse.":
                    $ cuisine = "steakhouse"
                "How about seafood?":
                    $ cuisine = "seafood"
                "I'm in the mood for Southern food.":
                    $ cuisine = "southern"

            ch_Laura "Fine."

    $ eating_dinner = True
    $ ordered_food = True
    $ food_arrived = False
    $ drinking_wine = False

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_72
    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_79
    call send_Characters(Laura, "bg_restaurant", behavior = "on_date") from _call_send_Characters_69

    "You get seated quickly, and the waitress hands out the menus."

    $ Laura.change_face("neutral", eyes = "down")

    $ ordered_food = False

    $ Player_picked_food = False

    if renpy.random.random() > 0.66:
        pause 1.0 

        $ Laura.change_face("neutral")

        ch_Laura "I don't know what to get."
        ch_Laura "Pick for me."

        $ Laura.change_face("neutral", eyes = "squint")

        ch_Laura "But, I am {i}not{/i} eating a salad. . ."
        ch_Player "Okay, then why don't you get. . ."

        $ chosen_meal = {}
        $ restaurant_bill = {}

        call restaurant_menu(Laura, cuisine) from _call_restaurant_menu_4

        ch_Player "And I'll get. . ."

        call restaurant_menu(Player, cuisine) from _call_restaurant_menu_5

        $ Player_picked_food = True
    else:
        "You decide to order. . ."

        $ chosen_meal = {}
        $ restaurant_bill = {}

        call restaurant_menu(Player, cuisine) from _call_restaurant_menu_6

    $ Laura.change_face("smirk1")

    "You have a nice time chatting with [Laura.name], as you wait for the waitress to come back and take your orders."

    if Laura in Partners and renpy.random.random() > 0.75:
        "She seems much more comfortable holding a conversation with you, compared to that first date."

    $ Laura.change_face("neutral", eyes = "right")

    "The waitress finally comes back, and. . ."

    $ temp = chosen_meal[Player]

    menu:
        extend ""
        "Let her order for you (encourage_quirk)":
            if Laura.ordered_for_you_last_time:
                "You hold your tongue and wait for [Laura.name]."
                ch_Laura "He'll have the [temp]."
            else:
                "You hold your tongue and wait for [Laura.name]."

                $ Laura.change_face("neutral", eyes = "squint")

                "She glances over, and you just nod your head."

                $ Laura.change_face("neutral", eyes = "right")

                ch_Laura "He'll have the [temp]."

            $ Laura.ordered_for_you_last_time = True

            $ Laura.History.update("quirk_encouraged")
        "Order for yourself (discourage_quirk)":
            if Laura.ordered_for_you_last_time:
                ch_Laura "He-"

                $ Laura.change_face("confused1", eyes = "squint")

                "Before she can finish, you speak up."
                ch_Player "I'll have the [temp]."

                $ Laura.change_face("neutral", eyes = "right")
            else:
                $ Laura.change_face("neutral", eyes = "squint")

                "You notice [Laura.name] staring at you."

                $ Laura.change_face("suspicious1")

                ch_Player "I'll have the [temp]."

                $ Laura.change_face("neutral", eyes = "right")

            $ Laura.ordered_for_you_last_time = False

            $ Laura.History.update("quirk_discouraged")

    if Laura not in chosen_meal.keys():
        if cuisine == "steakhouse":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.25:
                if renpy.random.random() > 0.5:
                    $ chosen_meal[Laura] = "filet mignon"
                else:
                    $ chosen_meal[Laura] = "ribeye"

                $ restaurant_bill[Laura] = 45
            elif dice_roll > 0.25*2/3:
                $ chosen_meal[Laura] = "Chilean sea bass"
                $ restaurant_bill[Laura] = 35
            elif dice_roll > 0.25*1/3:
                $ chosen_meal[Laura] = "penne alla vodka"
                $ restaurant_bill[Laura] = 30
            else:
                $ chosen_meal[Laura] = "chicken parmesan"
                $ restaurant_bill[Laura] = 25
        elif cuisine == "seafood":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                $ chosen_meal[Laura] = "salmon"
                $ restaurant_bill[Laura] = 25
            elif dice_roll > 0.5*2/3:
                $ chosen_meal[Laura] = "lobster tails"
                $ restaurant_bill[Laura] = 45
            elif dice_roll > 0.5*1/3:
                $ chosen_meal[Laura] = "crab-stuffed sole"
                $ restaurant_bill[Laura] = 35
            else:
                $ chosen_meal[Laura] = "crab cakes"
                $ restaurant_bill[Laura] = 30
        elif cuisine == "southern":
            $ dice_roll = renpy.random.random()

            if dice_roll > 0.5:
                $ chosen_meal[Laura] = "short ribs"
                $ restaurant_bill[Laura] = 45
            elif dice_roll > 0.5*2/3:
                $ chosen_meal[Laura] = "catfish"
                $ restaurant_bill[Laura] = 35
            elif dice_roll > 0.5*1/3:
                $ chosen_meal[Laura] = "jambalaya"
                $ restaurant_bill[Laura] = 30
            else:
                $ chosen_meal[Laura] = "fried chicken"
                $ restaurant_bill[Laura] = 25

    $ temp = chosen_meal[Laura]

    ch_Laura "Give me the [temp]."

    if temp in ["filet mignon", "ribeye"]:
        $ Laura.change_face("suspicious1", eyes = "right") 
        
        ch_Laura "Make it medium rare."
        "The poor waitress shrinks under [Laura.name]'s glare."

    $ ordered_food = True

    $ Laura.change_face("smirk1")

    "The waitress scurries away, leaving the two of you alone again."

    $ lines = {
        "b": "You look adorably deadly today.",
        "c": "You look great in that outfit.",
        "d": "Your abs make me feel things. . . good things.",
        "k": "You never wear perfume, but still always smell nice. . ."}

    if EventScheduler.Events["Laura_first_friend_part_three"].completed:
        $ lines.update({"a": "I've noticed you listening to some pretty interesting music, I like your taste."})

    $ indices = list(lines.keys())

    $ renpy.random.shuffle(indices)

    $ first_compliment = lines[indices[0]]
    $ second_compliment = lines[indices[1]]
    $ third_compliment = lines[indices[2]]

    menu:
        extend ""
        "[first_compliment]":
            call expression f"Laura_flirt_a{indices[0]}" from _call_expression_12
        "[second_compliment]":
            call expression f"Laura_flirt_a{indices[1]}" from _call_expression_13
        "[third_compliment]":
            call expression f"Laura_flirt_a{indices[2]}" from _call_expression_14

    $ Laura.change_face("smirk2", blush = 1)

    "You continue to have a surprisingly nice conversation, as you wait for the food to arrive."

    $ Laura.change_face("confused1")

    "She asks you a ton of questions, infinitely perplexed and curious about seemingly mundane things, no matter how much you've already tried to explain by now."
                
    pause 1.0

    $ fade_to_black(0.4)

    $ food_arrived = True

    $ fade_in_from_black(0.4)
    
    $ Laura.change_face("happy", eyes = "right")

    "The waitress finally comes back with your orders, causing [Laura.name]'s face to light up like nothing else can."

    $ Laura.change_face("smirk2", eyes = "down", mouth = "lipbite")

    "The poor waitress can't help but flinch and scurry away after depositing the food." 
    "[Laura.name] doesn't hesitate, as she immediately begins devouring her meal."

    if Player_picked_food and chosen_meal[Laura] in ["ribeye", "salmon", "short ribs"]:
        $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Laura "You picked {i}very{/i} well."

        call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_279
    elif not Player_picked_food and chosen_meal[Laura] not in ["ribeye", "salmon", "short ribs"] and chosen_meal[Player] in ["ribeye", "salmon", "short ribs"]:
        $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

        "After finishing, she starts eyeing your food as well."

        menu:
            extend ""
            "Give her a bite":
                "You cut her a piece, and she eats it directly off of your fork." 

                $ Laura.change_face("neutral", eyes = "down", mouth = "open")

                pause 1.0

                $ Laura.change_face("sly", mouth = "lipbite")

                ch_Laura "Thanks."

                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_280
            "Don't give her a bite":
                $ Laura.change_face("suspicious1") 

                "You don't give her any, and she just glares at you." 

                $ Laura.change_face("angry1", eyes = "right")

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura
                
            call Laura_date_dinner_sex from _call_Laura_date_dinner_sex
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_dinner_sex from _call_Laura_date_dinner_sex_1
                "Just finish the meal normally":
                    pass

    $ Laura.change_face("angry1", eyes = "right")

    "You finish eating, and the waitress comes by with the check."
    "The poor thing looks like she wants to run away, as [Laura.name] continues to glare at her."

    $ Laura.change_face("confused1") 

    menu:
        "Offer to pay":
            if "Player_initiated" in Player.date_planned[Laura]:
                $ Laura.change_face("smirk1")

                ch_Player "I'll cover it."
                ch_Laura "Thanks. . ."

                $ Laura.change_face("angry1", eyes = "right")  

                ch_Laura "I. . . appreciate it."

                $ Laura.change_face("smirk2", blush = 1)

                if Player.cash >= restaurant_bill[Player] + restaurant_bill[Laura]:
                    "You pay the bill and head back into the mall." 
                    
                    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_281

                    $ Player.cash -= restaurant_bill[Player] + restaurant_bill[Laura]
                else:
                    "You realize you don't have enough money. . ." 
                    
                    $ Laura.change_face("confused1", eyes = "squint") 
                    
                    pause 1.0 
                    
                    $ Laura.change_face("suspicious1") 
                    
                    ch_Laura "Here." 
                    "[Laura.name] pays the difference." 
                    
                    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_282 

                    $ Player.cash = 0
            else:
                $ Laura.change_face("angry1", eyes = "squint")

                ch_Laura "No."
                ch_Laura "This date was my idea, I'll pay."
                ch_Player "Thanks, [Laura.petname]."

                $ Laura.change_face("angry1", eyes = "right", blush = 1)

                ch_Laura "You're. . . welcome."
                "[Laura.name] pays the bill, and the waitress basically sprints away."
                "You both head back into the mall."

                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_283
        "Recommend splitting the check":
            if "Player_initiated" in Player.date_planned[Laura]:
                $ Laura.change_face("confused1")

                ch_Player "Why don't we split the bill?"

                $ Laura.change_face("neutral")

                ch_Laura "Fine, that's fair."

                if Player.cash >= math.ceil((restaurant_bill[Player] + restaurant_bill[Laura])/2):
                    "You both pay the bill and head back into the mall."

                    $ Player.cash -= math.ceil((restaurant_bill[Player] + restaurant_bill[Laura])/2)
                else:
                    "You realize you don't have enough money to pay for half. . ." 
                    
                    $ Laura.change_face("confused1", eyes = "squint") 
                    
                    pause 1.0 
                    
                    $ Laura.change_face("suspicious1") 
                    
                    ch_Laura "Here." 
                    "[Laura.name] pays the difference." 
                    
                    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_284 

                    $ Player.cash = 0
            else:
                $ Laura.change_face("angry1", eyes = "squint")

                ch_Laura "No."
                ch_Laura "This date was my idea, I'll pay."
                ch_Player "Thanks, [Laura.petname]."

                $ Laura.change_face("angry1", eyes = "right", blush = 1)

                ch_Laura "You're. . . welcome."
                "[Laura.name] pays the bill, and the waitress basically sprints away."
                "You both head back into the mall."

                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_285

    return

label Laura_date_dinner_sex:
    $ Laura.change_face("sexy", blush = 1)

    "You notice [Laura.name] looking at you lasciviously."

    if sex_initiator == Player:
        menu:
            extend ""
            "Ask for a handjob under the table" if Laura.History.check("handjob"):
                $ sex_act = "handjob"
            "Ask for a blowjob under the table" if Laura.History.check("blowjob") and Laura.History.check("swallow_cum"):
                $ sex_act = "blowjob"
            "Suggest a quickie in the bathroom" if Laura.History.check("sex"):
                $ sex_act = "sex"
            "Ask to go down on her in the bathroom" if Laura.History.check("eat_pussy"):
                $ sex_act = "eat_pussy"
            "Decide against it":
                return
    elif sex_initiator == Laura:
        $ sex_acts = []

        if Laura.History.check("handjob"):
            $ sex_acts.append("handjob")

        if Laura.History.check("blowjob") and Laura.History.check("swallow_cum"):
            $ sex_acts.append("blowjob")

        if Laura.History.check("sex"):
            $ sex_acts.append("sex")

        if Laura.History.check("eat_pussy"):
            $ sex_acts.append("eat_pussy")

        if sex_acts:
            menu:
                extend ""
                "Go along with it":
                    $ sex_act = renpy.random.choice(sex_acts)
                "Not right now, [Laura.petname].":
                    $ Laura.change_face("confused1")

                    pause 1.0

                    $ Laura.change_face("angry1")

                    ch_Laura "Fine."

                    return

    call expression f"Laura_date_dinner_sex_{sex_act}" from _call_expression_15

    $ Laura.History.update(sex_act)

    return

label Laura_date_dinner_sex_handjob:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    call hide_Character(Laura) from _call_hide_Character_10

    "After making sure nobody is paying attention, she slips out of sight."

    if sex_initiator == Laura:
        $ temp = Laura.petname.capitalize()

        ch_Player "[temp], what are you doing. . . ?"

    "Thanks to the long table cloth, even if someone was looking, they wouldn't be able to see anything."
    "You can feel her tease you for a while, before pulling your pants down."
    "[Laura.name] gets right to work, wrapping her fingers around you."
    "You continue to eat your meal as nonchalantly as possible, meanwhile [Laura.name] picks up the pace."

    if Laura.History.check("handjob") >= 11:
        "By now you know she's this rough on purpose, it seems like your body likes it, and you're barely able to hold it in after mere moments."
    elif Laura.History.check("handjob") >= 5:
        "She still has a bit of a death grip and is quite rough, but she's getting better, and you're on the edge faster than ever."
    else:
        "She doesn't seem to know what to do, but makes up for it with enthusiasm, bringing you to the edge all the same."

    $ Player.desire = 75

    "You frantically grasp at her arm in an attempt to get her to slow down, but this only makes her speed up."

    $ Player.desire = 90

    "You can't hold on any longer. . ." 
    ". . ." with small_screenshake

    $ Player.desire = 0

    if Laura.History.check("swallow_cum"):
        "You feel her lips wrap around your cock right as you cum." 
        ch_Laura "*gulp*" 
        "She makes sure to swallow it all and licks you clean afterwards."

        $ Laura.History.update("swallow_cum")
    else:
        "She takes a napkin and cleans everything up after you're done."

        $ Laura.History.update("clean_cum")

    "She puts your pants back into position, before getting up."

    if Laura.History.check("swallow_cum", tracker = "recent") and renpy.random.random() > 0.5:
        $ Laura.spunk["chin"] = True

    call add_Characters(Laura) from _call_add_Characters_81

    $ Laura.change_face("sexy", blush = 2)

    if Laura.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Laura.change_face("sexy", eyes = "down", blush = 2)

        call swallow_cum(Laura) from _call_swallow_cum_4

        $ Laura.change_face("sly", blush = 2)

        ch_Laura "*gulp*"

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I can tell you enjoyed that."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_286
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_287

    return

label Laura_date_dinner_sex_blowjob:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    call hide_Character(Laura) from _call_hide_Character_11

    "After making sure nobody is paying attention, [Laura.name] slips out of sight."

    if sex_initiator == Laura:
        $ temp = Laura.petname.capitalize()

        ch_Player "[temp], what are you doing. . . ?"

    "Thanks to the long table cloth, even if someone was looking, they wouldn't be able to see anything."
    "You can feel her tease you for a while, before pulling your pants down."
    "She gets right to work, wrapping her lips around you."
    "You continue to eat your meal as nonchalantly as possible, meanwhile [Laura.name] picks up the pace."

    if Laura.History.check("blowjob") >= 11:
        "At this point she knows exactly what buttons to push and is able to bring you to the edge in mere moments."
    elif Laura.History.check("blowjob") >= 5:
        "She's still a bit too rough, but is quickly learning what gets you going, and you're about to lose control faster than ever."
    else:
        "She doesn't quite know what she's doing just yet, there's too much teeth involved, but it brings you to the edge all the same."

    $ Player.desire = 75

    "You frantically tap her in an attempt to get her to slow down, but this only makes her speed up."

    $ Player.desire = 90

    "You can't hold on any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0

    ch_Laura "*slurp*"
    "As you cum, she pulls you in as deep as she can handle, moaning around your cock as she swallows."
    ch_Laura "*gulp*"
    "[Laura.name] doesn't stop and just keeps sucking, causing you to twitch involuntarily."
    "Finally, after getting every last drop, she pulls away."
    "She puts your pants back into position, before getting up."

    if renpy.random.random() > 0.5:
        $ Laura.spunk["chin"] = True

    call add_Characters(Laura) from _call_add_Characters_82

    $ Laura.change_face("sexy", blush = 2)

    if Laura.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Laura.change_face("sexy", eyes = "down", blush = 2)

        call swallow_cum(Laura) from _call_swallow_cum_5

        $ Laura.change_face("sly", blush = 2)

        ch_Laura "*gulp*"

    ch_Laura "The best meal they serve in this place."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_288
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_289

    $ Laura.History.update("swallow_cum")

    return

label Laura_date_dinner_sex_sex:
    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Follow me."

    call hide_Character(Laura) from _call_hide_Character_12

    "[Laura.name] heads to the bathroom and, after a minute, you follow after her."

    $ fade_to_black(0.4)

    "You see her waiting for you outside the bathroom, and you both head inside together."

    call set_the_scene(location = "bg_restaurant_bathroom") from _call_set_the_scene_80
    call send_Characters(Laura, "bg_restaurant_bathroom", behavior = "on_date") from _call_send_Characters_72

    "Good thing it's a private one."
    "She locks the door behind you."
        
    if sex_initiator == Laura:
        $ has_position_control = False
        $ has_movement_control = False

    $ Laura.available_Actions = ["sex"]

    if Laura.History.check("anal"):
        $ Laura.available_Actions.append("anal")

    $ Laura.available_poses = ["missionary"]

    if Laura.History.check("doggy"):
        $ Laura.available_poses.append("doggy")

    $ chosen_Action = renpy.random.choice(Laura.available_Actions)
    $ chosen_pose = renpy.random.choice(Laura.available_poses)

    $ Laura.History.update("hookup")
        
    $ Laura.History.update(chosen_Action)
    
    call request_position(Laura, chosen_pose, automatic = True) from _call_request_position_13

    $ Action = ActionClass(chosen_Action, Player, Laura)

    call undress(Laura, "underwear") from _call_undress_19
    call start_Action(Action) from _call_start_Action_3
    call screen Action_screen(automatic = True)
    
    $ choice_disabled = False
        
    # if renpy.random.random() > 0.5:
    #     call try_on(Laura, Laura.Wardrobe.Clothes["messy hair"]) from _call_try_on_5

    call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_52
    
    $ locations = list(Laura.spunk.keys())

    while locations:
        if Laura.spunk[locations[0]]:
            call clean_cum(Laura) from _call_clean_cum_5

        $ locations.remove(locations[0])

    "After you both put your clothes back on, [Laura.name] leaves and heads back to the table."

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_73
    call send_Characters(Laura, "bg_restaurant", behavior = "on_date") from _call_send_Characters_73

    "You wait a minute before leaving the bathroom as well."

    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_81

    $ Laura.change_face("sly", blush = 2)
    
    pause 1.0

    if Laura.Clothes["hair"].string == "messy":
        ch_Player "Your hair's a bit. . ."

        $ Laura.change_face("confused1", mouth = "smirk", blush = 1)

        "She straightens it out."

        call try_on(Laura, Laura.Wardrobe.Clothes["straight hair"]) from _call_try_on_6

    $ Laura.change_face("sexy")

    ch_Laura "I enjoyed that. . . {i}a lot{/i}."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_290
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_291

    $ Laura.available_Actions = []
    $ Laura.available_poses = []

    return

label Laura_date_dinner_sex_eat_pussy:
    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "Follow me."

    call hide_Character(Laura) from _call_hide_Character_13

    "[Laura.name] heads to the bathroom and, after a minute, you follow after her."

    $ fade_to_black(0.4)

    "You see her waiting for you outside the bathroom, and you both head inside together."

    call set_the_scene(location = "bg_restaurant_bathroom") from _call_set_the_scene_82
    call send_Characters(Laura, "bg_restaurant_bathroom", behavior = "on_date") from _call_send_Characters_74

    "Good thing it's a private one."
    "She locks the door behind you."
        
    $ has_movement_control = False

    $ Laura.available_Actions = ["eat_pussy"]
    $ Laura.available_poses = ["masturbation"]

    $ chosen_Action = renpy.random.choice(Laura.available_Actions)
    $ chosen_pose = renpy.random.choice(Laura.available_poses)

    $ Laura.History.update("hookup")
        
    $ Laura.History.update(chosen_Action)
    
    call request_position(Laura, chosen_pose, automatic = True) from _call_request_position_14

    $ Action = ActionClass(chosen_Action, Player, Laura)

    call undress(Laura, "underwear") from _call_undress_20
    call start_Action(Action) from _call_start_Action_9
    call screen Action_screen(automatic = True)
    
    $ choice_disabled = False

    call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_53

    "After you both put your clothes back on, [Laura.name] leaves and heads back to the table."

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_74
    call send_Characters(Laura, "bg_restaurant", behavior = "on_date") from _call_send_Characters_75
    
    "You wait a minute before leaving the bathroom as well."

    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_83

    $ Laura.change_face("sly", blush = 2)

    pause 1.0

    $ Laura.change_face("sexy")

    ch_Laura "I enjoyed that. . . {i}a lot{/i}."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_292
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_293

    $ Laura.available_Actions = []
    $ Laura.available_poses = []

    return

label Laura_date_movie:
    if second_event:
        if Laura in second_event.keys():
            $ Laura.change_face("neutral", eyes = "right") 

            pause 1.0

            $ Laura.change_face("smirk2")

            ch_Laura "I want to watch another one of those 'movies.'"

            $ Laura.change_face("smirk2", eyes = "right")

            ch_Laura "Let's go."
            ch_Player "Wh-"
            "She just grabs your wrist and drags you to the theater."
    
    $ Laura.change_face("neutral", eyes = "right")

    "You arrive at the ticket counter, and [Laura.name] looks over all the available movies."

    $ Laura.change_face("suspicious1", eyes = "right")

    pause 1.0

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "I still don't understand any of these titles."
    ch_Laura "You pick."

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

    $ Laura.change_face("confused1", eyes = "right")

    ch_Laura "That one?"

    $ Laura.change_face("neutral")

    ch_Laura "Fine."

    menu:
        extend ""
        "Offer to pay":
            if "Player_initiated" in Player.date_planned[Laura]:
                $ Laura.change_face("smirk2")

                ch_Player "I'll cover it."
                ch_Laura "Thanks. . ."

                $ Laura.change_face("angry1", eyes = "right")  

                ch_Laura "I. . . appreciate it."

                $ Laura.change_face("smirk2", blush = 1)

                if Player.cash >= 2*ticket_price:
                    "You pay for the tickets." 
                    
                    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_294

                    $ Player.cash -= 2*ticket_price
                else:
                    "You realize you don't have enough money. . ." 
                    
                    $ Laura.change_face("confused1", eyes = "squint") 
                    
                    pause 1.0 
                    
                    $ Laura.change_face("suspicious1") 
                    
                    ch_Laura "Here." 
                    "[Laura.name] pays the difference." 
                    
                    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_295

                    $ Player.cash = 0
            else:
                $ Laura.change_face("suspicious1") 

                ch_Laura "Put your wallet away." 
                ch_Laura "I'm paying."
                ch_Player "Thanks, [Laura.petname]."

                $ Laura.change_face("angry1", eyes = "right", blush = 1)

                ch_Laura "You're. . . welcome."
                "[Laura.name] pays for the tickets."

                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_296
        "Recommend splitting the ticket price":
            if "Player_initiated" in Player.date_planned[Laura]:
                $ Laura.change_face("confused1")

                ch_Player "Why don't we split the cost?"

                $ Laura.change_face("neutral")

                ch_Laura "Fine, that's fair."

                if Player.cash >= ticket_price:
                    "You both pay for the tickets."

                    $ Player.cash -= ticket_price
                else:
                    "You realize you don't have enough money to pay for half. . ." 
                    
                    $ Laura.change_face("confused1", eyes = "squint") 
                    
                    pause 1.0 
                    
                    $ Laura.change_face("suspicious1") 
                    
                    ch_Laura "Here." 
                    "[Laura.name] pays the difference." 

                    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_297 

                    $ Player.cash = 0
            else:
                $ Laura.change_face("angry1", eyes = "squint")

                ch_Laura "No."
                ch_Laura "This date was my idea, I'll pay."
                ch_Player "Thanks, [Laura.petname]."

                $ Laura.change_face("angry1", eyes = "right", blush = 1)

                ch_Laura "You're. . . welcome."

    call remove_Characters(location = "bg_movies") from _call_remove_Characters_75
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_84
    call send_Characters(Laura, "bg_movies", behavior = "on_date") from _call_send_Characters_76

    call expression f"Laura_date_movie_{movie_choice}" from _call_expression_16

    "With the movie over, you get up and leave the theater."

    return

label Laura_date_movie_ron_bic1:
    "You quickly find your seats, and the movie starts shortly after."

    $ Laura.change_face("pleased1", eyes = "right")

    "Once the action starts, you look over to see [Laura.name] entranced by all the killing on screen."
    "Despite already seeing this particular movie before, she doesn't seem to care one bit."
    "Ron Bic is in a sticky situation after he's unwittingly sent to kill the CEO of his favorite lighter company."
    "Ron quickly realizes a rival lighter company set him up, and he vows to get revenge."

    $ Laura.change_face("happy", eyes = "right")

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_1
                "Just finish watching the movie":
                    pass

    "The movie continues, as Ron kills legions of men in the pursuit of revenge."
    "He has to fight his way through hundreds of evil henchmen in a lighter factory and finally takes out the real bad guy in the end."
    "There's a plethora of violent and fiery deaths as well as some impressive choreography."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "It's over?!"

    $ Laura.change_face("angry1")

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_298

    return

label Laura_date_movie_ron_bic2:
    "[Laura.name] seems quite excited, as she rushes you to your seats."
    "You get seated just in time, as the movie is already starting."

    $ Laura.change_face("pleased1", eyes = "right")

    "After the events of the first movie, things are more dangerous than ever for our hero, Ron Bic."
    "The world's lighter making companies have been reeling from the deaths of so many important executives."
    "And they want to know who's responsible."

    $ Laura.change_face("furious", eyes = "right")

    "Poor Ron can't seem to avoid trouble, as he has to kill dozens of people in an attempt to prevent everyone from learning of his terrible mistake. . ."
    "You look over to see [Laura.name] so thoroughly emotionally invested in the movie that she's seething with rage."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_2
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_3
                "Just finish watching the movie":
                    pass

    $ Laura.change_face("confused1", eyes = "right")

    "The movie continues and, unfortunately, Ron isn't fast enough - the information gets out."

    $ Laura.change_face("angry1", eyes = "right")

    "Once the world knows that Ron killed the CEO of an allied lighter company, even if it was an accident, everyone he knows and loves turns on him."

    $ Laura.change_face("pleased1", eyes = "right")

    "In the end, after a crescendo of blood, gore, and fiery death, Ron Bic is able to clear his name. . ."

    $ Laura.change_face("angry1", eyes = "right")

    "But, did he survive? Does he even know of his own success?"

    $ Laura.change_face("furious", eyes = "right")

    ch_Laura "{i}Grrrrrr{/i}. . ."

    $ Laura.change_face("furious")

    ch_Laura "Is this what you call a 'cliffhanger'?"

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "I do not like 'cliffhangers.'"

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_299

    return

label Laura_date_movie_hamburg_portfolio:
    "The previews are already over, but you get seated just in time for the movie to start."

    $ Laura.change_face("confused1", eyes = "right")

    "The movie is set in modern day Philadelphia, only. . . magic is real."

    $ Laura.change_face("surprised1", eyes = "right")

    "The main character is a wizard, but the world doesn't know about all things supernatural, so he has to lay low."
    "He tries to be a good person and help people with his gift, but it's never that easy."
    "It seems like whoever wrote the movie absolutely despises the main character, because they keep putting him in horrible situations and giving him insane amounts of trauma."

    $ Laura.change_face("pleased1", eyes = "right")

    "Although, it is quite entertaining, as he uses his considerable talent with magic to kill his enemies in very creative ways."

    $ Laura.change_face("smirk2", eyes = "right")

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_4
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_5
                "Just finish watching the movie":
                    pass

    $ Laura.change_face("confused1", eyes = "right")

    "As the movie continues, the main character is forced to confront his morality."
    "If he wants to save the people he loves, innocent people must die."

    $ Laura.change_face("angry1", eyes = "right")

    pause 1.0

    $ Laura.change_face("furious")

    pause 1.0

    $ Laura.change_face("angry1", eyes = "right")

    "[Laura.name] seems a bit bothered, as she watches the main character struggle so much with himself."
    "In the end, he isn't able to put aside his morals, and his inaction causes everyone to suffer."

    $ Laura.change_face("furious", eyes = "right")

    "At least he survives and gets revenge. . . however hollow it is. . ."

    $ Laura.change_face("suspicious1")

    ch_Laura "If you were the one in danger. . ."

    $ Laura.change_face("furious", eyes = "right")

    ch_Laura "I wouldn't hesitate, like him."

    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_300

    return

label Laura_date_movie_beautiful_flower:
    "You find your seats, and the movie starts shortly after."

    $ Laura.change_face("confused1", eyes = "right")

    "You look over at [Laura.name], and she seems perplexed by what's happening on screen." 

    "The movie is about a man who wanted to buy his mom some nice flowers for Mother's day."
    "He does this every year, but this time all the local florists are sold out."

    $ Laura.change_face("suspicious1", eyes = "right")

    "He's running around frantically trying to find flowers to buy because his mother is very ill."
    "This might be his last chance, ever, to give her flowers."
    "Any time the mother is mentioned, you notice [Laura.name] looking uncomfortable."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_6
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_7
                "Just finish watching the movie":
                    pass

    "The movie continues and, as it turns out, the female lead only recently opened her own florist and has had trouble finding customers."
    "The guy has almost given up when he finally reaches her small hidden shop."
    "The shop's name is 'Beautiful Flower.'"

    $ Laura.change_face("surprised1", eyes = "right")

    "[Laura.name] still seems a bit bothered, which is odd, considering the wholesome story about a budding romance between a guy and his florist."

    $ Laura.change_face("suspicious1")

    ch_Laura "Hmm. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_301
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_302

    return

label Laura_date_movie_fated:
    "You get seated just as the movie starts."

    $ Laura.change_face("confused1", eyes = "right")

    "The movie starts out as a simple romance between two coworkers."
    "Admiring each other from a distance, they never interacted much at work."
    "That is until they were unwittingly set up on a blind date with each other."

    $ Laura.change_face("smirk1", eyes = "right")

    pause 1.0

    $ Laura.change_face("smirk1")

    pause 1.0

    $ Laura.change_face("smirk2", eyes = "right")

    "You catch [Laura.name] sneaking glances at you throughout the movie."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_8
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_9
                "Just finish watching the movie":
                    pass

    $ Laura.change_face("confused1", eyes = "right")

    "As the movie continues, it quickly takes a turn away from the wholesome, as the two mutually agree not to start a relationship."

    $ Laura.change_face("surprised1", eyes = "right", blush = 1)

    "Instead the two become friends with benefits, ending the night with a very graphic sex scene."

    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_303

    $ Laura.change_face("surprised1", eyes = "right", blush = 2)

    pause 1.0

    $ Laura.change_face("neutral", eyes = "squint", blush = 2)

    pause 1.0

    $ Laura.change_face("sexy", eyes = "right", blush = 2)

    "There are many {i}very{/i} graphic sex scenes, as the two continue denying their romantic feelings for each other."
    "Eventually they do officially get together, and the movie ends."

    $ Laura.change_face("sexy", eyes = "squint", blush = 2)

    ch_Laura "Hmm. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_304
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_305

    return

label Laura_date_movie_refilling_empty_glass:
    "You get seated just as the movie starts."

    $ Laura.change_face("neutral", eyes = "right")

    "It begins following a bartender at a popular spot in the city."

    $ Laura.change_face("confused1", eyes = "right") 

    "The bartender is good at her job - and beautiful - so plenty of male customers try flirting with her to no avail."

    $ Laura.change_face("angry1", eyes = "right") 

    "She was recently widowed." 
    "She's been struggling to move on from her husband's death, until one night she spots a despondent man sitting at the far end of the bar."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_10
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_11
                "Just finish watching the movie":
                    pass

    "The movie continues, and the bartender becomes interested in the despondent man, since he looks similar to her late husband."

    $ Laura.change_face("surprised1", eyes = "right") 

    "He tells her about his plight, how a former business partner started a conspiracy against him and it's ruining his life."

    $ Laura.change_face("surprised1", eyes = "right", blush = 2)

    "The chance meeting turns into a thrilling romance as they rapidly fall in love, and the bartender uses her skills as a former super spy to stop the conspiracy."

    $ Laura.change_face("sexy", eyes = "right", blush = 2)

    "Nearly every other minute there's a graphic sex scene as the bartender demonstrates her prowess to her new beau."

    $ Laura.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Laura "I like that character. . ."
    ch_Laura "She's a badass."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_306
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_307

    return

label Laura_date_movie_stale_air:
    "The movie starts only a few minutes after you get seated."

    $ Laura.change_face("neutral", eyes = "right")

    "The story is about a struggling writer who can't find any passion or inspiration for his stories."

    $ Laura.change_face("confused1", eyes = "right")

    "The writer's monotonous life goes on as normal until he starts finding messages and sticky notes appearing out of nowhere around his apartment."

    $ Laura.change_face("surprised1", eyes = "right")

    "He has no idea where they're coming from, but they all have great ideas which he uses to jumpstart his writing."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_12
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_13
                "Just finish watching the movie":
                    pass

    "As the movie continues, it quickly becomes clear what's going on."
    "Unbeknownst to the writer, a carbon monoxide leak in his apartment is simultaneously poisoning him, while also the cause for his inspiration."

    $ Laura.change_face("confused1", eyes = "right")

    "His imaginative writing lands him a new job, but the gas also starts causing him to become delusional."

    $ Laura.change_face("pleased1", eyes = "right")

    "The movie climaxes as the writer unknowingly acts out his latest story. . ."
    "Which is about a disturbed maniac who goes on a murder spree at their new job."

    $ Laura.change_face("sly")

    ch_Laura "That was. . . interesting. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_308
    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_309

    return

label Laura_date_movie_devils_spring_break:
    "You take your seats, and the movie starts shortly after."

    $ Laura.change_face("confused1", eyes = "right")

    "The movie seems to follow a generic horror movie formula, with reckless college kids and everything."

    $ Laura.change_face("angry1", eyes = "right")

    "One of the college students has a rich family, and they just bought a new summer home, one that of course is rumored to be haunted."
    "The rich kid brings a bunch of his friends down to the house, to spend their spring break getting drunk and partying."

    $ Laura.change_face("furious", eyes = "right")

    ch_Laura "They're idiotic. . ."
    "Despite the rumors, the house isn't actually haunted. . . at least not by ghosts."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_14
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_15
                "Just finish watching the movie":
                    pass

    $ Laura.change_face("surprised1", eyes = "right")

    "As the movie continues, the college students are slowly and gruesomely killed by a demon, their souls stolen in the process."
    "[Laura.name] seems quite satisfied as the reckless students are taken out one by one."

    $ Laura.change_face("pleased1", eyes = "right")

    "They try to put up a fight, after they sober up enough to realize how fucked they are."
    "During one particularly tense moment, you look over and see [Laura.name] wide-eyed, staring at the screen in suspense."

    $ Laura.change_face("angry1", eyes = "right")

    "Suddenly, there's a jumpscare, but instead of freaking out, she actually puts an arm in front of you, as if in protection."

    $ Laura.change_face("appalled1")

    "She quickly pulls her arm back, pretending like nothing happened."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "Those characters were annoying. . ."

    $ Laura.change_face("confused1")

    ch_Laura "Was I supposed to root for the demon?"

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_310

    return

label Laura_date_movie_unsanctioned_crusade:
    "You take your seats just as the final preview ends."

    $ Laura.change_face("smirk1", eyes = "right")

    "The movie starts on a high note, as it instantly earns its 'R' rating."

    $ Laura.change_face("neutral", eyes = "right")

    "It's set in medieval Europe and starts with a massacre."
    "Although, despite being bloody, the massacre is rather mundane, as it was perpetrated by an order of deeply religious knights."

    $ Laura.change_face("confused1", eyes = "right") 

    "The knights are on their own form of crusade, driven by deep seated religious beliefs."
    "They do terrible things in a misguided attempt at worship."
    "Only, God is real and is less than pleased by these atrocities."

    if Player.stamina and Laura.stamina:
        if (Laura.status["horny"] or Laura.status["nympho"]) and renpy.random.random() > 0.5:
            $ sex_initiator = Laura

            call Laura_date_movie_sex from _call_Laura_date_movie_sex_16
        elif renpy.random.random() > 0.5:
            menu:
                "Recommend some fooling around":
                    $ sex_initiator = Player

                    call Laura_date_movie_sex from _call_Laura_date_movie_sex_17
                "Just finish watching the movie":
                    pass

    $ Laura.change_face("surprised1", eyes = "right")

    "As the movie continues, the knights are plagued by various, horrifying, heavenly tribulations."
    "It starts slowly at first, suspense building, as the knights are mercilessly terrorized."

    $ Laura.change_face("confused1", eyes = "right")

    "You notice [Laura.name] get increasingly tense, a look of anger or confusion on her face."

    $ Laura.change_face("angry1", eyes = "right")

    "The knights are directly confronted by the atrocities they themselves committed and systematically eradicated in cruel and disturbing fashion."

    $ Laura.change_face("angry1")

    pause 1.0

    $ Laura.change_face("worried1", eyes = "right")

    pause 1.0

    $ Laura.change_face("confused1")

    ch_Laura "I. . ."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "Thanks for being my friend, despite. . ."

    $ Laura.change_face("neutral")

    ch_Laura "Never mind."

    call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_311

    return

label Laura_date_movie_sex:
    $ Laura.change_face("sexy", blush = 1)

    "You notice [Laura.name] looking at you lasciviously."

    if sex_initiator == Player:
        menu:
            extend ""
            "Ask if she wants to make out" if Laura.History.check("makeout"):
                $ sex_act = "makeout"
            "Ask for a handjob" if Laura.History.check("handjob"):
                $ sex_act = "handjob"
            "Ask if you can put a hand down her pants" if Laura.History.check("touch_pussy") and Laura.History.check("seen_pussy"):
                $ sex_act = "touch_pussy"
            "Ask if you can finger her" if Laura.History.check("finger_pussy"):
                $ sex_act = "finger_pussy"
            "Ask for a blowjob" if Laura.History.check("blowjob") and Laura.History.check("swallow_cum"):
                $ sex_act = "blowjob"
            "Decide against it":
                return
    elif sex_initiator == Laura:
        $ sex_acts = []

        if Laura.History.check("makeout"):
            $ sex_acts.append("makeout")

        if Laura.History.check("handjob"):
            $ sex_acts.append("handjob")

        if Laura.History.check("touch_pussy") and Laura.History.check("seen_pussy"):
            $ sex_acts.append("touch_pussy")

        if Laura.History.check("finger_pussy"):
            $ sex_acts.append("finger_pussy")

        if Laura.History.check("blowjob") and Laura.History.check("swallow_cum"):
            $ sex_acts.append("blowjob")

        if sex_acts:
            menu:
                extend ""
                "Go along with it":
                    $ sex_act = renpy.random.choice(sex_acts)
                "Not right now, [Laura.petname].":
                    $ Laura.change_face("confused1")

                    pause 1.0

                    $ Laura.change_face("angry1")

                    ch_Laura "Fine."

                    return

    call expression f"Laura_date_movie_sex_{sex_act}" from _call_expression_17

    $ Laura.History.update(sex_act)

    return

label Laura_date_movie_sex_makeout:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    "Once [Laura.name]'s sure there's nobody around, she reaches over and pulls you in."

    $ Laura.change_face("kiss1", blush = 1)

    "The movie plays on in the background, as the two of you lock lips, your tongues dancing in each other's mouth."

    $ Laura.change_face("kiss2", blush = 2)

    "With one hand firmly around your neck, preventing you from going anywhere, the other one starts wandering across your body."

    $ Laura.change_face("sexy", blush = 1)

    "Before things go too far, [Laura.name] stops herself and pulls away."
    ch_Laura "Mmm. . ."
    ch_Laura "You taste {i}good{/i}."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_312
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_313

    return

label Laura_date_movie_sex_handjob:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    "Once [Laura.name]'s sure there's nobody around, she reaches over."

    if sex_initiator == Laura:
        $ temp = Laura.petname.capitalize()

        ch_Player "[temp], what are you doing. . . ?"

    "After a bit of teasing, she pulls your cock out."

    $ Laura.change_face("sexy", eyes = "right", blush = 1)

    "[Laura.name] gets right to work, wrapping her fingers around you."
    "You try to continue watching the movie, but [Laura.name] keeps speeding up."

    if Laura.History.check("handjob") >= 11:
        "By now you know she's this rough on purpose, it seems like your body likes it, and you're barely able to hold it in after mere moments."
    elif Laura.History.check("handjob") >= 5:
        "She still has a bit of a death grip and is quite rough, but she's getting better, and you're on the edge faster than ever."
    else:
        "She doesn't seem to know what to do, but makes up for it with enthusiasm, bringing you to the edge all the same."

    $ Laura.change_face("sexy", eyes = "right", blush = 2)

    $ Player.desire = 75

    "You frantically try pulling her hand away, but this only makes her speed up."
   
    $ Player.desire = 90

    "You can't hold on any longer. . ." 
    ". . ." with small_screenshake

    $ Player.desire = 0

    if Laura.History.check("swallow_cum"):
        "Just as you're about to cum, she leans over." 
        
        call hide_Character(Laura) from _call_hide_Character_14
        
        "You feel her lips wrap around your cock right as you cum." 
        ch_Laura "*gulp*" 
        "She makes sure to swallow it all and licks you clean afterwards." 

        call add_Characters(Laura) from _call_add_Characters_83

        $ Laura.History.update("swallow_cum")
    else:
        "She takes a napkin and cleans everything up after you're done."

        $ Laura.History.update("clean_cum")

    $ Laura.change_face("sexy", blush = 1)

    "She puts your pants back into position."

    if Laura.History.check("swallow_cum", tracker = "recent") and renpy.random.random() > 0.5:
        $ Laura.spunk["chin"] = True

    $ Laura.change_face("sexy", blush = 2)

    if Laura.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Laura.change_face("sexy", eyes = "down", blush = 2)

        call swallow_cum(Laura) from _call_swallow_cum_6

        $ Laura.change_face("sly", blush = 2)

        ch_Laura "*gulp*"

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I enjoy the way you squirm."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_314
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_315

    return

label Laura_date_movie_sex_touch_pussy:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    "Once you're sure nobody's around, you reach over."
    "You can instantly feel how wet she is, as you slowly move your hand over her crotch."

    $ Laura.change_face("sexy", eyes = "right", blush = 1)
    call expose(Laura, "pussy") from _call_expose_3

    "Slipping your hand under her pants, you tease her for a bit, before getting right to work."

    $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Laura "Hnng. . ."
    "[Laura.name] tries to continue watching the movie, but she seems more focused on suppressing any moans."
    "You make sure to give every part of her pussy ample attention."

    $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 3)

    "Whatever you're doing seems to be working as she starts squirming and grinding against your hand."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 3)

    "You pick up the pace, and [Laura.name] grabs your arm, anchoring it in place."
    "She's not letting go until you finish the job."

    $ Laura.change_face("appalled1", mouth = "lipbite", blush = 3)

    ch_Laura "{i}Grrrrrr{/i}. . ." with small_screenshake

    $ Laura.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 3)

    "She finally reaches the climax and can't help but violently shudder." with small_screenshake
    "You don't stop, and the shuddering continues, her death grip on your arm only tightening." with small_screenshake

    $ Laura.change_face("sexy", blush = 2)

    "Finally, after a minute, she lets go."
    "She's still twitching even as you pull your hand away."

    call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_6

    ch_Laura "Mmm. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_316
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_317

    return

label Laura_date_movie_sex_finger_pussy:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    "Once you're sure nobody's around, you reach over."
    "You can instantly feel how wet she is, as you slowly move your hand over her crotch."

    $ Laura.change_face("sexy", eyes = "right", blush = 1)
    call expose(Laura, "pussy") from _call_expose_4

    "Slipping your hand under her pants, you tease her for a bit, before sliding your fingers inside."

    $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Laura "Hnng. . ."
    "[Laura.name] tries to continue watching the movie, but she seems more focused on suppressing any moans."
    "Your fingers slide in and out while your thumb teases her clit."

    $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 3)

    "Whatever you're doing seems to be working as she starts squirming and grinding against your hand."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 3)

    "You pick up the pace, and [Laura.name] grabs your arm, anchoring it in place."
    "She's not letting go until you finish the job."

    $ Laura.change_face("appalled1", mouth = "lipbite", blush = 3)

    ch_Laura "{i}Grrrrrr{/i}. . ." with small_screenshake

    $ Laura.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 3)

    "She finally reaches the climax and can't help but violently shudder." with small_screenshake
    "You don't stop, and the shuddering continues, her death grip on your arm only tightening." with small_screenshake

    $ Laura.change_face("sexy", blush = 2)

    "Finally, after a minute, she lets go."
    "She's still twitching even as you pull your hand away."

    call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_7

    ch_Laura "Mmm. . ."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_318
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_319

    return

label Laura_date_movie_sex_blowjob:
    $ Laura.change_face("confused1", eyes = "right", mouth = "smirk")

    pause 1.0

    $ Laura.change_face("confused1", mouth = "lipbite", eyes = "down", blush = 1)

    pause 1.0

    $ Laura.change_face("sexy", blush = 1)

    "The theater is basically empty, and nobody's anywhere near the two of you."

    call hide_Character(Laura) from _call_hide_Character_15

    if sex_initiator == Laura:
        $ temp = Laura.petname.capitalize()

        ch_Player "[temp], what are you doing. . . ?"

    "[Laura.name] leans over, undoing your pants, before taking your cock out."
    "She gets right to work, wrapping her lips around you."
    ch_Laura "*slurp*"
    "You hold her hair out of the way, and she starts speeding up."

    if Laura.History.check("blowjob") >= 11:
        "At this point she knows exactly what buttons to push and is able to bring you to the edge in mere moments."
    elif Laura.History.check("blowjob") >= 5:
        "She's still a bit too rough, but is quickly learning what gets you going, and you're about to lose control faster than ever."
    else:
        "She doesn't quite know what she's doing just yet, there's too much teeth involved, but it brings you to the edge all the same."

    $ Player.desire = 75

    "You try to make her slow down, but she just latches on even harder, only going faster."
    
    $ Player.desire = 90
    
    "You can't hold on any longer. . ."
    ". . ." with small_screenshake

    $ Player.desire = 0
    
    ch_Laura "*slurp*"
    "As you cum, she pulls you in as deep as she can handle, moaning around your cock as she swallows."
    ch_Laura "*gulp*"
    "[Laura.name] doesn't stop and just keeps sucking, causing you to twitch involuntarily."
    "Finally, after getting every last drop, she pulls away."
    "She puts your pants back into position, before sitting back up."

    if renpy.random.random() > 0.5:
        $ Laura.spunk["chin"] = True

    call add_Characters(Laura) from _call_add_Characters_84

    $ Laura.change_face("sexy", blush = 2)

    if Laura.spunk["chin"]:
        ch_Player "You have a little something. . ."

        $ Laura.change_face("sexy", eyes = "down", blush = 2)

        call swallow_cum(Laura) from _call_swallow_cum_7

        $ Laura.change_face("sly", blush = 2)

        ch_Laura "*gulp*"

    ch_Laura "I always want more."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_320
    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_321

    $ Laura.History.update("swallow_cum")

    return

label Laura_date_mall:
    if Laura in second_event.keys():
        $ Laura.change_face("neutral", eyes = "right") 

        pause 1.0

        $ Laura.change_face("smirk2")

        ch_Laura "Let's go."

        $ Laura.change_face("smirk2", eyes = "right")

        ch_Player "Wh-"

        if renpy.random.random() > 0.5 or Player.cash < 10:
            ch_Laura "We're going to wander around."

            $ second_event[Laura] = "wander"
        else:
            ch_Laura "We're getting dessert."

            $ second_event[Laura] = "dessert"

        "She grabs your wrist and drags you along."
    elif Player in second_event.keys():
        menu:
            "How about we stay in the mall and. . ."
            ". . . wander around.":
                $ second_event[Player] = "wander"
            ". . . grab dessert." if Player.cash >= 10:
                $ second_event[Player] = "dessert"

        ch_Laura "Fine." 
        ch_Laura "Let's go."

    if (Player in second_event.keys() and second_event[Player] == "wander") or (Laura in second_event.keys() and second_event[Laura] == "wander"):
        call Laura_date_mall_wander from _call_Laura_date_mall_wander
    elif (Player in second_event.keys() and second_event[Player] == "dessert") or (Laura in second_event.keys() and second_event[Laura] == "dessert"):
        call Laura_date_mall_dessert from _call_Laura_date_mall_dessert

    return

label Laura_date_mall_wander:
    $ Laura.change_face("smirk1", eyes = "right")

    "Without any specific destination in mind, you wander around the mall with [Laura.name]."

    $ Laura.change_face("smirk2", eyes = "right")

    "She's her usual stoic self, but still listens attentively as you have a nice, if slightly one-sided, conversation."

    $ holding_hands = False

    if Player in second_event.keys() and Laura in Partners:
        menu:
            extend ""
            "Ask [Laura.name] if you can hold hands.":
                $ Laura.change_face("confused1", mouth = "smirk")

                ch_Laura "Fine. . ." 
                
                $ Laura.change_face("smirk2", mouth = "lipbite", eyes = "right", blush = 1) 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_322
                call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_323

                $ holding_hands = True
            "Just grab [Laura.name]'s hand.": 
                $ Laura.change_face("angry1", mouth = "smirk")

                "She doesn't protest, but gives your hand a firm squeeze in response. . ." 
                "You can almost hear your bones creak."
                
                $ Laura.change_face("smirk2", mouth = "lipbite", eyes = "right", blush = 1) 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_324

                $ holding_hands = True
            "Do nothing":
                pass
    elif Laura in second_event.keys() and Laura in Partners and renpy.random.random() > 0.25:
        $ Laura.change_face("smirk2", eyes = "right", mouth = "lipbite")

        pause 1.0

        $ Laura.change_face("smirk2", eyes = "left", mouth = "lipbite")

        pause 1.0

        $ Laura.change_face("smirk2", eyes = "right", mouth = "lipbite")

        "[Laura.name] suddenly reaches out, grabbing your hand."

        $ Laura.change_face("smirk2", eyes = "right", mouth = "lipbite", blush = 1)

        $ holding_hands = True

    if holding_hands:
        "She squeezes your hand tightly and inches even closer, as you continue walking alongside each other."

    $ Laura.change_face("smirk2", eyes = "right", blush = 1)

    "Time flies by, spent well, doing nothing much at all aside from being close to each other."

    call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_325

    return

label Laura_date_mall_dessert:
    $ Laura.change_face("smirk1", eyes = "right")

    "Being in a mall provides a number of opportunities - and problems - simultaneously."
    "There are so many different options that it can be difficult to decide what to get."

    $ Laura.change_face("confused1", mouth = "smirk")

    ch_Laura "You know I've never had basically anything here."

    $ Laura.change_face("neutral")

    ch_Laura "Just pick anything, I'll try it all."

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

            $ Laura.History.update("tried_chocolate")
        "Cupcakes ($10)":
            $ Player.cash -= 10

            $ Laura.History.update("tried_chocolate")
        "Crepes ($10)":
            $ Player.cash -= 10

            $ Laura.History.update("tried_chocolate")
        "Fresh Baked Cookies ($10)":
            $ Player.cash -= 10

            $ Laura.History.update("tried_chocolate")

    $ Laura.change_face("smirk2", eyes = "right")

    "After paying for the dessert, you both wander around the mall while enjoying it."

    $ Laura.change_face("smirk1", eyes = "down", mouth = "lipbite")

    "Like pretty much all food. . . except salads. . . [Laura.name] looks like she's enjoying it quite a lot."

    $ Laura.change_face("smirk2", eyes = "right", blush = 1)

    "Even after finishing, you spend a while just walking and talking."
    "Time flies by."

    return

label Laura_date_end:
    if "Player_initiated" in Player.date_planned[Laura]:
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_76
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_85
        call send_Characters(Laura, "bg_hallway", behavior = "on_date") from _call_send_Characters_79

        $ Laura.change_face("confused1", mouth = "smirk")

        menu:
            extend ""
            "Invite her into your room":
                call Laura_date_end_invite from _call_Laura_date_end_invite
            "Give her a goodnight kiss":
                call Laura_date_end_goodnight from _call_Laura_date_end_goodnight
    else:
        call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_77
        call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_86
        call send_Characters(Laura, "bg_girls_hallway", behavior = "on_date") from _call_send_Characters_80

        if Laura.status["horny"] or Laura.status["nympho"]:
            call Laura_date_end_invite from _call_Laura_date_end_invite_1
        elif renpy.random.random() > 0.25:
            call Laura_date_end_invite from _call_Laura_date_end_invite_2
        else:
            call Laura_date_end_goodnight from _call_Laura_date_end_goodnight_1

    return

label Laura_date_end_invite:
    if Player.location == "bg_hallway":
        $ Laura.change_face("sly")

        ch_Player "Come on in."

        call remove_Characters(location = Player.home) from _call_remove_Characters_78
        call set_the_scene(location = Player.home) from _call_set_the_scene_87
        call send_Characters(Laura, Player.home, behavior = "on_date") from _call_send_Characters_81
        
        if Laura.status["horny"] or Laura.status["nympho"]:
            $ Laura.change_face("sexy", blush = 1) 
            
            ch_Laura "That was fun." 
            
            $ Laura.change_face("sexy", blush = 2) 
            
            ch_Laura "Are we having more fun?"
        else:
            $ Laura.change_face("smirk2", eyes = "right")
            
            ch_Laura "That was. . . fun." 
            
            $ Laura.change_face("smirk2")

        menu:
            extend ""
            "Recommend something {i}fun{/i}" if approval_check(Laura, threshold = "hookup"):
                $ Laura.History.update("hookup")

                call screen Action_screen(automatic = True)
                
                $ choice_disabled = False

                ch_Laura "I'm sleeping over tonight."
                ch_Player "Perfect."
            "Invite her to sleep over" if Laura.History.check("sleepover"):
                $ Laura.change_face("confused1", mouth = "smirk") 
                
                pause 1.0 
                
                $ Laura.change_face("sexy") 
                
                ch_Laura "As long as you sleep naked. . ."
            "Say goodnight":
                $ Laura.change_face("kiss1", blush = 1) 
                
                "She pulls you into a brief kiss." 

                $ Laura.History.update("kiss")
                
                $ Laura.change_face("sexy") 
                
                ch_Laura "Goodnight."

                call send_Characters(Laura, Laura.home) from _call_send_Characters_82
    elif Player.location == "bg_girls_hallway":
        $ Laura.change_face("confused1", mouth = "smirk")

        ch_Laura "Why are you just standing there?"

        if approval_check(Laura, threshold = "hookup"):
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "I'm not done with you yet."

        menu:
            extend ""
            "Go inside with her":
                call Laura_date_invite_accept from _call_Laura_date_invite_accept
            "Say goodnight":
                call Laura_date_invite_reject from _call_Laura_date_invite_reject

    return

label Laura_date_invite_accept:
    "[Laura.name] grabs you by the wrist and drags you inside the room."

    call remove_Characters(location = Laura.home) from _call_remove_Characters_79
    call set_the_scene(location = Laura.home) from _call_set_the_scene_88
    call send_Characters(Laura, Laura.home, behavior = "on_date") from _call_send_Characters_83

    $ Laura.change_face("sly", blush = 2)

    ch_Player "What did you have in mind?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    if approval_check(Laura, threshold = "hookup"):
        $ Laura.History.update("hookup")

        call screen Action_screen(automatic = True)
        
        $ choice_disabled = False

        if approval_check(Laura, threshold = "sleepover"):
            $ Laura.change_face("sexy", blush = 1)

            ch_Laura "You should sleep over tonight."

            menu:
                extend ""
                "I should.":
                    $ Laura.change_face("sly", mouth = "lipbite", blush = 2) 
                    
                    ch_Laura "You should also sleep naked. . ."
                "Not tonight.":
                    $ Laura.change_face("confused1") 
                    
                    ch_Laura "Fine." 
                    
                    $ Laura.change_face("neutral") 
                    
                    ch_Laura "Goodnight, [Laura.Player_petname]."

                    call remove_Characters(location = Player.home) from _call_remove_Characters_80
                    call set_the_scene(location = Player.home) from _call_set_the_scene_89
        else:
            $ Laura.change_face("neutral") 
            
            ch_Laura "Goodnight, [Laura.Player_petname]."

            call remove_Characters(location = Player.home) from _call_remove_Characters_111
            call set_the_scene(location = Player.home) from _call_set_the_scene_134
    else:
        $ Laura.change_face("kiss1", blush = 1) 
        
        "She pulls you in for a kiss." 

        $ Laura.History.update("kiss")
        
        $ Laura.change_face("sexy") 
        
        ch_Laura "Goodnight."

        call remove_Characters(location = Player.home) from _call_remove_Characters_112
        call set_the_scene(location = Player.home) from _call_set_the_scene_136

    return

label Laura_date_invite_reject:
    $ Laura.change_face("confused1")

    ch_Player "Sorry, not tonight, [Laura.petname]."

    $ Laura.change_face("neutral")

    ch_Laura "Fine, but you're not leaving without. . ."

    $ Laura.change_face("kiss1", blush = 1)

    "She pulls you into a brief kiss, before pulling away."

    $ Laura.History.update("kiss")

    $ Laura.change_face("sexy")

    ch_Laura "Good, [Laura.Player_petname]."

    call send_Characters(Laura, Laura.home) from _call_send_Characters_84
    call remove_Characters(location = Player.home) from _call_remove_Characters_81
    call set_the_scene(location = Player.home) from _call_set_the_scene_90

    return

label Laura_date_end_goodnight:
    if Player.location == "bg_hallway":
        $ Laura.change_face("kiss1", blush = 1)

        "You pull [Laura.name] into a brief kiss."
        "She holds on for a moment, before letting go."

        $ Laura.change_face("sexy")

        ch_Player "Goodnight, [Laura.petname]."
        ch_Laura "Goodnight."
    else:
        $ Laura.change_face("sexy")

        pause 1.0

        $ Laura.change_face("kiss1", blush = 1)

        "[Laura.name] grabs you by the collar and pulls you into a kiss."
        "After a long moment, she pulls away."

        $ Laura.change_face("sexy")

        ch_Laura "I had. . . fun."
        ch_Laura "Goodnight, [Laura.Player_petname]."

    $ Laura.History.update("kiss")

    call send_Characters(Laura, Laura.home) from _call_send_Characters_85
    call remove_Characters(location = Player.home) from _call_remove_Characters_82
    call set_the_scene(location = Player.home) from _call_set_the_scene_91

    return