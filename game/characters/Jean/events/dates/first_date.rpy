init python:

    def Jean_first_date():
        label = "Jean_first_date"

        conditions = [
            "Jean in Player.date_planned.keys() and 'primary' in Player.date_planned[Jean]",

            "not Jean.History.check('went_on_date_with_Player')",

            "time_index == 2"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Jean_first_date:
    $ ongoing_Event = True

    hide screen phone_screen

    if weather == "rain":
        $ weather = None

    $ Party = []

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed

    if Player.location != "bg_hallway":
        if Player.location != Jean.location:
            call receive_text(Jean, "Wya???") from _call_receive_text_1
            call open_texts(Jean) from _call_open_texts_1

            pause

            call send_text(Jean, "On my way!") from _call_send_text

            pause 2.0
            
            hide screen phone_screen
        
        "You head into the hallway right outside your room."
        
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_18
        call send_Characters(Jean, "bg_hallway", behavior = "on_date") from _call_send_Characters_23
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_21

        $ Jean.change_face("happy")
        $ Jean.change_arms("sass")

        ch_Jean "There you are, [Jean.Player_petname]."
    elif Jean.location != "bg_hallway":
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_19
        call send_Characters(Jean, "bg_hallway", behavior = "on_date") from _call_send_Characters_24

        $ Jean.change_face("pleased2")
        $ Jean.change_arms("sass")

        ch_Jean "Oh, you're already here."

        $ Jean.change_face("happy")

        ch_Player "Yeah, I didn't have anything to do so I got here early." 

        $ Jean.change_face("smirk2")

        ch_Jean "Good."
        ch_Jean "Wouldn't want to miss our reservation." 

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("neutral")

    ch_Jean "C'mon, [Jean.Player_petname], let's go."

    $ Jean.change_face("smirk2", eyes = "right")

    $ fade_to_black(0.4)

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_20
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_22
    call send_Characters(Jean, "bg_campus", behavior = "on_date") from _call_send_Characters_25

    ch_Player "So, where are we going?"

    $ Jean.change_face("confused1", mouth = "smirk")
    $ Jean.change_arms("hips")

    ch_Player "The restaurants get pretty packed right around now."

    $ Jean.change_face("sly")

    ch_Jean "Don't worry, I have everything all planned out." 

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("hips", right_arm = "extended")

    ch_Jean "Made reservations way ahead of time and everything."

    $ Jean.change_face("smirk2", eyes = "right")
    $ Jean.change_arms("sass")

    "You head to the mall together."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_21
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_23
    call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_26

    $ Jean.change_face("confused1", eyes = "right")

    "As you get to the restaurant, it's quickly evident something's wrong."

    $ Jean.change_face("angry1", eyes = "right")
    $ Jean.change_arms("angry")

    ch_Jean "What the hell, why's it closed?!"

    $ Jean.change_face("worried1", eyes = "right")

    "There's a sign on the door."

    "Dear Customer,\n\nOur kitchen is temporarily closed until further notice. We found a rat in the kitchen trying to be a saucier. The restaurant needs to be fully sanitized. Try again tomorrow!\n\nThanks"

    $ Jean.change_face("angry1")
    $ Jean.change_arms("crossed")

    ch_Jean "I just made this reservation earlier today."

    $ Jean.change_face("worried1")

    ch_Jean "Fat chance we'll find an open table nearby anytime soon."

    $ Jean.change_face("worried1", eyes = "right")

    pause 1.0

    $ Jean.change_face("sad", eyes = "right")

    ch_Jean "{size=-5}Why can't anything go right for once{/size}. . ."
    "You glance around the mall."
    "Most of the restaurants nearby look pretty packed."

    menu:
        extend ""
        "Look around more thoroughly":
            "You don't give up just yet."
            "As [Jean.name] continues to wallow in self pity, you take a look around the corner."
            "There's one a bit further away. . ."

            $ Jean.change_face("confused2")
            $ Jean.change_arms("neutral")

            $ temp = Jean.petname.capitalize()

            ch_Player "[temp], look!"

            $ Jean.change_face("surprised2")
            $ Jean.change_arms("angry")

            ch_Player "There's one over there." 

            $ Jean.change_face("surprised1", eyes = "left")

            ch_Player "It looks like a table just opened up." 

            $ Jean.change_face("surprised1", mouth = "smile", eyes = "left")

            pause 1.0

            $ Jean.change_face("happy")
            $ Jean.change_arms("neutral", left_arm = "extended")

            ch_Jean "Quick!"
            ch_Jean "Before anybody takes it!"

            $ Jean.change_face("smirk2", mouth = "lipbite", eyes = "left")
            $ Jean.change_arms("neutral", left_arm = "fist")

            "She grabs your hand and you both sprint to the new restaurant."

            $ eating_dinner = True
            $ ordered_food = True
            $ food_arrived = False
            $ drinking_wine = False

            call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_22
            call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_24
            call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_27

            $ Jean.change_face("smirk2", mouth = "lipbite")
            $ Jean.change_arms("neutral")

            "You make it just before another couple and get seated fairly quickly."
            ch_Jean "You saved the day, [Jean.Player_petname]."

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_49
        "It's pointless":
            $ Jean.change_face("perplexed")

            ch_Player "It's pointless."

            $ Jean.change_face("angry1", eyes = "left")

            ch_Player "We might as well-"

            $ Jean.change_face("surprised3", eyes = "left")
            $ Jean.change_arms("neutral", right_arm = "extended")

            ch_Jean "Wait! Look over there!"

            $ Jean.change_face("surprised2")

            ch_Jean "A table just opened up, quick!"

            call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_28

            "Before you can respond, she's already running towards a new restaurant."
            "You run after her."

            $ eating_dinner = True
            $ ordered_food = True
            $ food_arrived = False
            $ drinking_wine = False

            call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_23
            call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_29
            call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_25

            "You make it just before another couple and get seated fairly quickly."

            $ Jean.change_face("confused1")
            $ Jean.change_arms("hips")

            ch_Jean "See, maybe you shouldn't have given up so quickly."

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_50
        "Suggest annother activity":
            $ Jean.change_face("surprised2", eyes = "left")
            $ Jean.change_arms("neutral")


            ch_Player "It's okay, we can just do someth-"

            $ Jean.change_face("surprised2")

            ch_Jean "Wait!"

            $ Jean.change_arms("neutral", right_arm = "extended")

            ch_Jean "Look over there!"

            $ Jean.change_face("surprised2", eyes = "left")

            ch_Jean "A table just opened up, quick!"

            call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_30

            "Before you can respond, she's already running to the new restaurant."
            "You run after her."

            $ eating_dinner = True
            $ ordered_food = True
            $ food_arrived = False
            $ drinking_wine = False

            call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_24
            call send_Characters(Jean, "bg_restaurant", behavior = "on_date") from _call_send_Characters_31
            call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_26

            "You make it just before another couple and get seated fairly quickly."

            $ Jean.change_face("sly")
            $ Jean.change_arms("crossed")

            ch_Jean "See, I got it covered."

    $ Jean.change_face("smirk2", eyes = "right") 
    $ Jean.change_arms("sass")

    "The waitress comes by and gives you both a menu."

    $ ordered_food = False

    $ Jean.change_face("worried1", eyes = "down") 

    $ chosen_meal = {}
    $ restaurant_bill = {}

    call restaurant_menu(Player, "seafood") from _call_restaurant_menu_3

    "After you decide, you look up to see [Jean.name] looking a bit worried."

    $ Jean.change_face("worried2") 
    $ Jean.change_arms("crossed")

    ch_Player "What's wrong, [Jean.petname]?"

    $ Jean.change_face("worried1", mouth = "smirk") 

    ch_Jean "I didn't realize this was a seafood place. . ."

    $ Jean.change_face("worried1") 
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Jean "I've never really tried most of this stuff."

    $ Jean.change_arms(right_arm = "extended", left_arm = "rub_neck")

    ch_Jean "What are you getting?" 

    $ Jean.change_face("confused1", mouth = "smirk") 
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    $ temp = chosen_meal[Player].capitalize()

    ch_Player "[temp]."

    $ Jean.change_face("worried1", eyes = "down") 
    $ Jean.change_arms("crossed")

    ch_Jean "Hmm. . ."

    $ Jean.change_face("worried1", mouth = "smirk") 

    ch_Jean "What do you think I should get?"
    ch_Player "Well, if you haven't tried much seafood before. . ."

    menu:
        extend ""
        "I'm a big fan of crab cakes, I think you'll like them." if chosen_meal[Player] == "crab cakes":
            $ Jean.change_face("smirk2")

            ch_Jean "Okay, I'm trusting you."

            $ chosen_meal[Jean] = "crab cakes"
            $ restaurant_bill[Jean] = 30
        "I usually hear good things about crab cakes." if chosen_meal[Player] != "crab cakes":
            $ Jean.change_face("smirk2")

            ch_Jean "Sure, sounds interesting."

            $ chosen_meal[Jean] = "crab cakes"
            $ restaurant_bill[Jean] = 30
        "You probably have expensive taste, just try the lobster.": 
            $ Jean.change_face("angry1")

            ch_Jean "I don't really appreciate that. . ." 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_51

            $ chosen_meal[Jean] = "lobster tails"
            $ restaurant_bill[Jean] = 45
        "Salmon is a pretty safe bet.":
            $ Jean.change_face("worried1")

            ch_Jean "Okay, I'll try it."

            $ chosen_meal[Jean] = "salmon"
            $ restaurant_bill[Jean] = 25
        "If you're that worried, just get a salad.": 
            $ Jean.change_face("worried1")

            ch_Jean "I guess so. . ."

            $ chosen_meal[Jean] = "garden salad"
            $ restaurant_bill[Jean] = 15

    $ Jean.change_face("neutral", eyes = "right")

    "The waitress comes to take your order."

    menu:
        extend ""
        "Order for yourself (discourage_quirk)":
            $ temp = chosen_meal[Player]

            ch_Player "I'll have the [temp]."

            $ temp = chosen_meal[Jean]

            if chosen_meal[Player] == chosen_meal[Jean]:
                ch_Jean "And I'll also have the [temp]."
            else:
                ch_Jean "And I'll have the [temp]."

            $ Jean.change_face("smirk2")

            "The waitress leaves."

            $ Jean.ordered_for_you_last_time = True

            $ Jean.History.update("quirk_encouraged")
        "Let her order for you (encourage_quirk)":
            $ Jean.change_face("confused1")
            $ Jean.change_arms("sass")

            "When you don't say anything at first, [Jean.name] just looks at you, confused."

            $ Jean.change_face("pleased2")
            $ Jean.change_arms("neutral")

            "Then she realizes."

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_52

            $ Jean.change_face("smirk2", eyes = "right", blush = 1)
            $ Jean.change_arms("neutral", left_arm = "extended")

            $ temp = chosen_meal[Player]

            ch_Jean "He'll have the [temp]."

            $ Jean.change_face("smirk2")
            $ Jean.change_arms("sass")

            $ temp = chosen_meal[Jean]

            if chosen_meal[Player] == chosen_meal[Jean]:
                ch_Jean "And I'll also have the [temp]."
            else:
                ch_Jean "And I'll have the [temp]."

            $ Jean.change_face("smirk2", blush = 1)

            "The waitress leaves."
            ch_Player "Thanks, [Jean.petname]." 

            $ Jean.change_face("smirk2", mouth = "lipbite", blush = 1)

            $ Jean.ordered_for_you_last_time = False

            $ Jean.History.update("quirk_discouraged")

    $ ordered_food = True

    pause 1.0

    $ fade_to_black(0.4)

    $ food_arrived = True

    $ fade_in_from_black(0.4)

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("neutral")

    "The food arrives shortly after."

    $ Jean.change_face("smirk2", eyes = "down")

    "You both dig in."

    ch_Player "How is it?"

    if chosen_meal[Player] == "crab cakes" and chosen_meal[Jean] == "crab cakes":
        $ Jean.change_face("happy")

        ch_Jean "It's delicious!"

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_53

        $ Jean.change_face("smirk2")

        ch_Jean "Thanks for the recommendation."

        $ Jean.change_face("confused1", mouth = "smirk")

        ch_Jean "Seems like you have pretty good taste." 

        $ Jean.change_face("smirk2")
    elif chosen_meal[Jean] == "crab cakes":
        $ Jean.change_face("smirk2")

        ch_Jean "It's delicious!" 

        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_54

        ch_Jean "Good recommendation."
    elif chosen_meal[Jean] != "garden salad":
        $ Jean.change_face("smirk2")

        ch_Jean "It's pretty good."
        ch_Jean "I think I might not actually hate seafood."
    else:
        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "It's pretty good. . . for a salad."

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("crossed")

    "You enjoy each other's company as you finish your meals."
    "You figure now's probably a good time to get to know her a bit better."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Player "So, [Jean.petname]. . ."

    $ Jean.change_face("happy")

    ch_Player "I know you're basically top of your class."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("neutral")

    ch_Player "But, what do you do for fun when you're not studying?"

    $ Jean.change_face("worried1", eyes = "right")
    $ Jean.change_arms("neutral", left_arm = "rub_neck")

    ch_Jean "Well, I used to like reading a lot."

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("neutral", left_arm = "extended")

    ch_Jean "You know, those wholesome romance novels that always get a happy ending."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("crossed")

    ch_Jean "When I had more time, I was big on documentaries and movies too. . ."
    ch_Jean "Directors like Edgar Wrong or Quinten Terentano were my favorite."

    $ Jean.change_face("sad", eyes = "right")

    ch_Jean "But nowadays I'm way too busy studying for any of that." 

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("angry")

    ch_Jean "Except for tonight!"
    ch_Jean "I pre-purchased tickets to the perfect movie." 

    $ Jean.change_face("sly")

    ch_Player "Sweet, which one?"
    ch_Jean "Nuh-uh, no spoilers."

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("crossed")

    ch_Jean "You'll see when we get there."

    $ Jean.change_face("smirk2", eyes = "right")

    "The waitress comes and gives you the bill."

    $ Jean.change_face("sly")
    $ Jean.change_arms("neutral", left_arm = "extended")

    "[Jean.name] snatches it out of your hand."

    $ Jean.change_arms("neutral")

    menu:
        extend ""
        "Offer to pay" if Player.cash >= restaurant_bill[Player] + restaurant_bill[Jean]:
            $ Jean.change_face("smirk2")

            ch_Player "Come on, [Jean.petname]." 
            ch_Player "I can pay." 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_55 
            call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_56 
            
            ch_Jean "Nope!" 
            ch_Jean "This is my treat, [Jean.Player_petname]."
        "At least pay half" if Player.cash >= math.ceil((restaurant_bill[Player] + restaurant_bill[Jean])/2):
            $ Jean.change_face("smirk2")

            ch_Player "At least let me pick up my half of the bill." 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_57 
            
            ch_Jean "Nope!"
            ch_Jean "This is my treat, [Jean.Player_petname]."
        "Don't offer to pay":
            $ Jean.change_face("smirk2")

            ch_Player "Thanks." 
            
            ch_Jean "You're welcome, [Jean.Player_petname]."

    $ Jean.change_face("smirk2", eyes = "right")

    "[Jean.name] pays the bill and then you both head to the movie theater."

    $ Jean.change_face("smirk2")

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_25
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_27
    call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_32

    $ Jean.change_face("smirk2", eyes = "down")
    $ Jean.change_arms("neutral", right_arm = "extended")

    "As you approach the theater, [Jean.name] takes out the tickets."

    $ Jean.change_face("worried1", eyes = "down")

    "Suddenly, she stops."

    $ temp = Jean.petname.capitalize()

    ch_Player "[temp]?"

    $ Jean.change_face("worried2")

    ch_Jean "What's today's date?"

    $ Jean.change_face("worried3")

    ch_Player "It's. . ."
    ch_Jean "Shit!" 

    $ Jean.change_face("sad", eyes = "down")

    ch_Jean "I got these for the wrong day."

    $ Jean.change_face("worried1", eyes = "right")
    $ Jean.change_arms("angry")

    ch_Jean "Why is everything falling apart today. . ."

    $ Jean.change_face("worried1")

    ch_Player "I'm sure we can find something else good to watch."
    ch_Jean "Let me take a look at what's playing."

    $ Jean.change_face("worried1", eyes = "right")
    $ Jean.change_arms("crossed")

    "She peruses the listings."

    $ Jean.change_face("worried1", mouth = "smirk")

    $ temp = Jean.Player_petname.capitalize()

    ch_Jean "[temp], help me choose between these two."

    menu:
        extend ""
        "Entering Her Beautiful Flower":
            call Jean_first_date_path_1A from _call_Jean_first_date_path_1A

        "Fated to Be Together":
            call Jean_first_date_path_1B from _call_Jean_first_date_path_1B

    "She leads you to her room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_26
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_28
    call send_Characters(Jean, "bg_girls_hallway", behavior = "on_date") from _call_send_Characters_33

    $ Jean.change_face("smirk2")
    $ Jean.change_arms("sass")

    ch_Jean "See, the date went great. . ."

    $ Jean.change_face("worried1")

    ch_Jean ". . . right?"
    ch_Player "Thanks for treating me, [Jean.petname]." 

    $ Jean.change_face("worried1", mouth = "smirk")
    $ Jean.change_arms("crossed")

    ch_Player "I did have a really good time."
    ch_Jean "Good."

    $ Jean.change_face("smirk2")

    ch_Jean "So did I. . ."

    $ Jean.change_face("sly")
    $ Jean.change_arms("neutral", left_arm = "extended")

    ch_Player "Goodni-" 
    "She interrupts by pulling you into her room."

    call remove_Characters(location = Jean.home) from _call_remove_Characters_27
    call set_the_scene(location = Jean.home) from _call_set_the_scene_29
    call send_Characters(Jean, Jean.home, behavior = "on_date") from _call_send_Characters_34

    $ Jean.change_arms("neutral")

    ch_Jean "You can't leave without giving me a kiss. . ." 
    "She's acting all confident."

    $ Jean.change_face("worried1")
    $ Jean.change_arms("angry")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "If you're okay with that."
    "But the facade starts to crack."

    $ Jean.change_face("worried1", mouth = "smirk")

    $ temp = Jean.petname.capitalize()

    ch_Player "[temp], is everything okay?"
    ch_Jean "Yeah it's just. . ."

    $ Jean.change_face("worried1", eyes = "right")
    $ Jean.change_arms("crossed")

    ch_Jean "I haven't kissed anyone since like. . ."

    $ Jean.change_face("worried2", eyes = "right")

    ch_Jean ". . . {size=-5}middle school{/size}. . ."

    $ Jean.change_face("worried2", blush = 1)
    $ Jean.change_arms("neutral", right_arm = "extended")

    ch_Jean "I've just been focusing on my grades."

    $ Jean.change_face("worried1", eyes = "right")
    $ Jean.change_arms("angry")

    ch_Jean "A {i}lot{/i}."

    menu:
        extend ""
        "There's no pressure.":
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
            
            ch_Player "We don't ha-" 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_58 
            call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_59
        "That doesn't matter to me.":
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
            
            ch_Player "If yo-" 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_60
        "So?":
            $ Jean.change_face("confused1", mouth = "lipbite", blush = 1) 
            
            ch_Player "I don-"

    $ Jean.change_face("kiss2", blush = 1)

    "Before you can finish. . ."
    "[Jean.name] pulls you into a kiss."
    "She's a bit clumsy, but makes up for it with enthusiasm."

    $ Jean.change_face("kiss1", blush = 2)
    $ Jean.change_arms("neutral")

    "Grabbing the back of your head with both hands, she doesn't let you go for a long moment."

    $ Jean.change_face("kiss1", blush = 3)

    "Finally she lets go."

    $ Jean.History.update("kiss")

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)
    $ Jean.change_arms("sass")

    ch_Jean "Mmmm. . . I really liked that."

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "I hope you don't mind giving me plenty more where that came from."
    ch_Player "That was. . . great. . ."

    $ Jean.change_face("happy", brows = "raised", blush = 1)
    $ Jean.change_arms("neutral")

    ch_Jean "Oh, hey!"

    $ Jean.change_face("smirk2", blush = 1)
    $ Jean.change_arms("neutral", right_arm = "extended")

    ch_Jean "We already have the movie tickets for our second date."

    $ Jean.change_arms("hips")

    ch_Jean "Perfect opportunity for you to earn another kiss from me."
    ch_Player "Wh-"

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "Time for bed, [Jean.Player_petname]."
    ch_Jean "G'night!"
    "She pushes you out of her room before you can say anything else."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_28
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_30

    ch_Player ". . ."
    "You head back to your room."

    call remove_Characters(location = Player.home) from _call_remove_Characters_29
    call set_the_scene(location = Player.home) from _call_set_the_scene_31

    "It's late so you go straight to bed."

    $ Jean.History.update("went_on_date_with_Player")
    $ Jean.text_options.remove("free tonight for that date?")

    python:
        for C in Partners:
            if C not in Player.date_planned.keys():
                for other_C in Player.date_planned.keys():
                    if not C.History.check("told_wants_multiple_partners") or other_C not in C.knows_about:
                        C.History.update("cheated_on_date")

                        if not Player.History.check(f"cheated_on_{C.tag}_with_{other_C.tag}_date", tracker = "recent"):
                            Player.History.update(f"cheated_on_{C.tag}_with_{other_C.tag}_date")
                    
    $ Player.History.update("went_on_date")
    $ Player.date_planned = {}

    jump go_to_sleep

    $ ongoing_Event = False

    return

label Jean_first_date_path_1A:
    $ Jean.change_face("confused2", mouth = "smirk") 
    $ Jean.change_arms("sass")
            
    call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_61

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Jean "That one sounds a bit. . ."

    $ Jean.change_face("smirk2")

    ch_Jean "Whatever, I'm sure it'll be fun."

    $ Jean.change_face("confused1", eyes = "squint")

    "You're about to take your wallet out to pay when [Jean.name] just glares at you."

    $ Jean.change_face("sly")

    ch_Jean "Nope."
    "She pays for the tickets."

    call remove_Characters(location = "bg_movies") from _call_remove_Characters_30
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_32
    call send_Characters(Jean, "bg_movies", behavior = "on_date") from _call_send_Characters_35

    $ Jean.change_face("smirk2")

    "You both take your seats."

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)
    $ Jean.change_arms("neutral", right_arm = "fist")

    "As the movie starts, [Jean.name] just grabs your hand to hold."
    "The movie is about a man who wanted to buy his mom some nice flowers for Mother's day."
    "He does this every year, but this time all the local florists are sold out."

    $ Jean.change_face("worried1", eyes = "right")

    "He's running around frantically trying to find flowers to buy because his mother is very ill."
    "This might be his last chance, ever, to give her flowers."
    "[Jean.name] gives your hand a squeeze."

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)

    "As it turns out, the female lead only recently opened her own florist and has had trouble finding customers."
    "The guy has almost given up when he finally reaches her small hidden shop."
    "The shop's name is 'Beautiful Flower.'"

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "right")

    "You thought 'Entering Her Beautiful Flower' was quite a suggestive title, but turns out it's actually a wholesome story about a budding romance between a guy and his florist."

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)

    "The movie ends and you both start heading back to campus, still holding hands."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_31
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_33
    call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_36

    $ Jean.change_face("smirk2", blush = 1)
    $ Jean.change_arms("hips", right_arm = "fist")

    ch_Jean "That was surprisingly sweet, good choice."
    ch_Jean "I'm more of a fan of wholesome romance anyway."
    ch_Player "Yeah, it was actually pretty well written." 

    $ fade_to_black(0.4)

    "You continue discussing the movie on your walk back."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_32
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_34
    call send_Characters(Jean, "bg_campus", behavior = "on_date") from _call_send_Characters_37

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)

    return

label Jean_first_date_path_1B:
    $ Jean.change_face("pleased1")
    $ Jean.change_arms("sass")

    pause 1.0

    $ Jean.change_face("smirk2")

    ch_Jean "This one sounds sweet, I'm sure it'll be fun."

    $ Jean.change_face("confused1", eyes = "squint")

    "You're about to take your wallet out to pay when [Jean.name] just glares at you."

    $ Jean.change_face("sly")

    ch_Jean "Nope."
    "She pays for the tickets."
    
    call remove_Characters(location = "bg_movies") from _call_remove_Characters_33
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_35
    call send_Characters(Jean, "bg_movies", behavior = "on_date") from _call_send_Characters_38

    "You both take your seats."

    $ Jean.change_face("smirk2", eyes = "right", blush = 1)
    $ Jean.change_arms("neutral", right_arm = "fist")

    "As the movie starts, [Jean.name] grabs your hand to hold."
    "The movie starts out as a simple romance between two coworkers."
    "Admiring each other from a distance, they never interacted much while at work." 

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "right")

    "That is until they were unwittingly set up on a blind date with each other."

    $ Jean.change_face("surprised1", eyes = "right", mouth = "lipbite", blush = 1)

    "The story quickly takes a turn away from the wholesome, as the two mutually agree not to start a relationship, but instead become friends with benefits, ending the night with a very graphic sex scene."

    $ Jean.change_face("perplexed", mouth = "lipbite", blush = 2)

    pause 1.0

    $ Jean.change_face("surprised1", eyes = "right", mouth = "lipbite", blush = 1)

    "There are many very graphic sex scenes, as the two continue denying their romantic feelings for each other."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "right", blush = 1)

    "Eventually they do officially get together, and the movie ends on a happy note."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "That's. . . not what I was expecting. . ."
    ch_Player "Me neither."
    ch_Player "The title didn't sound that bad. . ."
    ch_Jean "It sounded pretty wholesome. . ."

    $ Jean.change_face("worried1", mouth = "smirk", eyes = "right", blush = 1)

    ch_Jean "I prefer the wholesome ones."

    $ Jean.change_face("smirk2", blush = 1)

    ch_Player "At least the acting was pretty good."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "Heh, yeah, it was definitely entertaining." 

    $ Jean.change_face("confused1", mouth = "smirk", blush = 1)

    ch_Jean "I could never do that friends with benefits thing though." 

    $ Jean.change_face("confused1", mouth = "smirk", eyes = "squint", blush = 1)
    $ Jean.change_arms("hips", right_arm = "fist")

    ch_Jean "I'm an all-in type of girl. . ."
    "She gives you a pointed look."

    $ fade_to_black(0.4)

    "You continue discussing the movie on your walk back, still holding hands."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_34
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_36
    call send_Characters(Jean, "bg_mall", behavior = "on_date") from _call_send_Characters_39

    pause 2.0

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_35
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_37
    call send_Characters(Jean, "bg_campus", behavior = "on_date") from _call_send_Characters_40

    $ Jean.change_face("smirk2", eyes = "right")

    return