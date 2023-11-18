init python:

    import math

    def Rogue_first_date():
        label = "Rogue_first_date"

        conditions = [
            "Rogue in Player.date_planned.keys()",
            "time_index == 2",
            "not Rogue.History.check('went_on_date_with_Player')"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Rogue_first_date:
    $ ongoing_Event = True

    hide screen phone_screen

    if weather == "rain":
        $ weather = None

    $ Party = []

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed

    if Rogue.location != Player.location:
        if Player.location != "bg_hallway":
            if Player.location != Rogue.location:
                call receive_text(Rogue, "Im here") from _call_receive_text_453
                call receive_text(Rogue, "Ill be waitin :))") from _call_receive_text_454
                call open_texts(Rogue) from _call_open_texts_7

                pause

                call send_text(Rogue, "On my way!") from _call_send_text_33

                pause 2.0
                
                hide screen phone_screen
            
            "You head into the hallway right outside your room."
            
            call remove_Characters(location = "bg_hallway") from _call_remove_Characters_166
            call send_Characters(Rogue, "bg_hallway", behavior = "on_date") from _call_send_Characters_143
            call set_the_scene(location = "bg_hallway") from _call_set_the_scene_172

            $ Rogue.change_face("happy")
                    
            ch_Rogue "Hey [Rogue.Player_petname]!"

            $ Rogue.change_face("worried1", mouth = "smirk")

            ch_Player "Hey [Rogue.name], sorry to keep you waiting." 
            ch_Rogue "It ain't your fault."

            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

            ch_Rogue "Ah got here. . . real early."

            $ Rogue.change_face("worried1", mouth = "smirk")
        else:
            "You hang out for a while, wasting time before the date."
            "A good 20 minutes before she was supposed to show up. . ."

            call remove_Characters(location = "bg_hallway") from _call_remove_Characters_167
            call send_Characters(Rogue, "bg_hallway", behavior = "on_date") from _call_send_Characters_144

            $ Rogue.change_face("surprised2")

            ch_Rogue "Oh, howdy. . ." 

            $ Rogue.change_face("worried2", mouth = "smirk", blush = 1)

            ch_Rogue "Didn't expect ya to be here yet." 

            $ Rogue.change_face("confused1", mouth = "smirk", blush = 1)

            ch_Player "Heh, yeah, I decided to get here a bit early."

            $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 2)

            pause 1.0

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Player "Looks like we had the same idea." 

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_573

            $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "You ready to go?"

    $ Rogue.change_face("smirk2")

    ch_Rogue "Yup!"

    $ Rogue.change_face("smirk2", eyes = "right")

    "[Rogue.name] follows you out of the mansion."

    $ fade_to_black(0.4)

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_168
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_173
    call send_Characters(Rogue, "bg_campus", behavior = "on_date") from _call_send_Characters_145

    "As you walk to the mall. . ."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Rogue "So, what's the plan?"

    $ Rogue.change_face("smirk2", eyes = "right", blush = 1)

    ch_Rogue "Ah don't care much what we do. . . {size=-5}so long as we're together{/size}. . ."
    ch_Player "I figured we could start with dinner."
    ch_Player "I heard some good things about this one restaurant in the mall."

    $ Rogue.change_face("happy", blush = 1)

    ch_Player "Great Southern food, which I figured you'd enjoy."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Perfect, ah've been cravin' a taste of home."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "Speaking of, where was 'home'?"
    ch_Rogue "Ah never got 'round to tellin' ya?"

    $ Rogue.change_face("happy")

    ch_Rogue "Mississippi, born and raised." 

    $ fade_to_black(0.4)

    "On the way over, [Rogue.name] walks alongside you, close enough to brush shoulders."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_169
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_174
    call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_146

    $ Rogue.change_face("confused1", eyes = "right", mouth = "smirk")

    "As you get to the restaurant, you realize you forgot to make a reservation. . ."

    $ Rogue.change_face("smirk2")

    "Thankfully it's not too busy, and you're seated rather quickly."

    $ eating_dinner = True
    $ ordered_food = True
    $ food_arrived = False
    $ drinking_wine = False

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_170
    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_175
    call send_Characters(Rogue, "bg_restaurant", behavior = "on_date") from _call_send_Characters_147

    $ Rogue.change_face("smirk2", eyes = "right")

    "The waitress comes by and gives you both a menu."

    $ Rogue.change_face("worried1", eyes = "down")

    $ ordered_food = False

    "You pick. . ."

    $ chosen_meal = {}
    $ restaurant_bill = {}

    call restaurant_menu(Player, "southern") from _call_restaurant_menu_11

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Rogue "Hey, [Rogue.Player_petname]."
    ch_Rogue "Ah'm stuck between a few choices. . ." 

    $ Rogue.change_face("sly")

    ch_Rogue "Why don't ya break the tie for me?"

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "You want me to pick?" 

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "You're supposed to be the expert here."
    ch_Rogue "Well yeah. . . but ah've had it all before."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "Ah want your input."

    $ suggested_salad = False

    menu:
        extend ""
        "Well, I'm getting the fried chicken. That's what I'd pick if I were you." if chosen_meal[Player] == "fried chicken":
            $ Rogue.change_face("pleased1")

            ch_Rogue "Ah was leanin' towards that." 
            
            $ Rogue.change_face("smirk2") 
            
            ch_Rogue "Good choice."

            $ chosen_meal[Rogue] = "fried chicken"
            $ restaurant_bill[Rogue] = 25
        "Fried chicken is a pretty safe bet." if chosen_meal[Player] != "fried chicken":
            $ Rogue.change_face("smirk2")

            pause 1.0

            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Rogue "It does sound real good."

            $ chosen_meal[Rogue] = "fried chicken"
            $ restaurant_bill[Rogue] = 25
        "Jambalaya is a Mississippi thing, right?":
            $ Rogue.change_face("confused1") 
            
            ch_Player "You should get that."

            ch_Rogue "No, Louisiana. . ." 
            
            $ Rogue.change_face("confused1", mouth = "smirk") 
            
            ch_Rogue "But ah do still like it."

            $ chosen_meal[Rogue] = "jambalaya"
            $ restaurant_bill[Rogue] = 30
        "Hard to go wrong with short ribs.":
            $ Rogue.change_face("smirk2")

            ch_Rogue "Ain't that right."

            $ chosen_meal[Rogue] = "short ribs"
            $ restaurant_bill[Rogue] = 45
        "I dunno, just get a salad or something if you're that indecisive. . .":
            $ Rogue.change_face("worried1")

            ch_Rogue "Ah'll just pick on my own then. . ." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_574

            $ chosen_meal[Rogue] = "fried chicken"
            $ restaurant_bill[Rogue] = 25

            $ suggested_salad = True

    $ Rogue.change_face("smirk2", eyes = "right")

    "The waitress comes to take your order." 

    menu:
        extend ""
        "Order for [Rogue.name] (encourage_quirk)":
            $ Rogue.change_face("surprised2", blush = 1)

            $ temp = chosen_meal[Rogue]

            ch_Player "She'll have the [temp]."

            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

            $ temp = chosen_meal[Player]

            if chosen_meal[Player] == chosen_meal[Rogue]:
                ch_Player "I'll also have the [temp]."
            else:
                ch_Player "I'll have the [temp]." 

            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

            ch_Rogue "Thanks, [Rogue.Player_petname]. . ." 
            ch_Rogue "Ah don't mind ya orderin' for me."

            $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_575

            $ Rogue.ordered_for_last_time = True

            $ Rogue.History.update("quirk_encouraged")
        "Let [Rogue.name] order for herself (discourage_quirk)":
            $ temp = chosen_meal[Rogue]

            ch_Rogue "Ah'll have the [temp]."

            $ Rogue.change_face("smirk2")

            $ temp = chosen_meal[Player]

            if chosen_meal[Player] == chosen_meal[Rogue]:
                ch_Player "And I'll also have the [temp]."
            else:
                ch_Player "And I'll have the [temp]."

            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_576

            $ Rogue.ordered_for_last_time = False

            $ Rogue.History.update("quirk_discouraged")

    $ ordered_food = True

    pause 1.0

    $ fade_to_black(0.4)

    $ food_arrived = True

    $ fade_in_from_black(0.4)

    $ Rogue.change_face("neutral", eyes = "down", mouth = "lipbite")

    $ Rogue.change_face("smirk2", eyes = "down")

    "The food arrives shortly after."
    "You both dig in."

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "How's the food?"
    ch_Player "Did I pick restaurants well?"

    if chosen_meal[Player] == "fried chicken" and chosen_meal[Rogue] == "fried chicken" and not suggested_salad:
        $ Rogue.change_face("smirk2", mouth = "lipbite")

        ch_Rogue "So good that ah might need to get seconds." 

        $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

        ch_Rogue "Thanks for pushin' me in the right direction."

        $ Rogue.change_face("smirk2", eyes = "down", mouth = "lipbite", blush = 1)

        "She starts eyeing your plate."

        menu:
            "If you say please, maybe I'll let you have an extra wing. (encourage_quirk)":
                $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

                $ Rogue.change_face("worried1", mouth = "lipbite", blush = 3) 
                
                ch_Rogue ". . . please." 
                
                call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_578 
                
                ch_Player "Here."

                $ Rogue.History.update("quirk_encouraged")
            "Here, you can have an extra wing. (discourage_quirk)": 
                $ Rogue.change_face("pleased2")

                pause 1.0
                
                $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1) 
                
                ch_Rogue "Thanks, [Rogue.Player_petname]."

                $ Rogue.History.update("quirk_discouraged")

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_577 
    elif chosen_meal[Rogue] == "fried chicken" and not suggested_salad:
        ch_Rogue "For New York?"

        $ Rogue.change_face("smirk2")

        ch_Rogue "Amazin'."
        ch_Rogue "Great choice, [Rogue.Player_petname]." 

        call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_579
    elif not suggested_salad:
        ch_Rogue "Real good."

        $ Rogue.change_face("sly")

        ch_Rogue "For New York that is. . ."
    else:
        $ Rogue.change_face("worried1", mouth = "smirk")

        ch_Rogue "It's real good."
        ch_Rogue "Ah'm so glad ah didn't get a salad. . ."

    $ Rogue.change_face("smirk2")

    "You have a pleasant chat while finishing your meals."

    $ Rogue.change_face("confused1", mouth = "smirk")

    "[Rogue.name] wonders about your life and hobbies before the Institute."
    "You tell her more about yourself."

    $ Rogue.change_face("worried1", mouth = "smirk")

    ch_Player "But what about you?"

    $ Rogue.change_face("confused1", mouth = "smirk")

    ch_Player "You're obviously a Southern food connoisseur." 

    $ Rogue.change_face("smirk2")

    ch_Player "What else do you do in your free time?"
    ch_Rogue "Heh, ah sure do enjoy it, but connoisseur is a bit of an exaggeration. . ."
    ch_Rogue "Ah'm into fashion, some Nu-Goth stuff mostly."

    $ Rogue.change_face("sly")

    ch_Rogue "Ah am a connoisseur of good storytellin', though."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Love readin', watchin' theater, movies, and stuff."

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "What kind of stories are your favorite?"

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Rogue "Oh, ya'know. . . stuff with drama. . ."

    $ Rogue.change_face("worried2", eyes = "right", mouth = "lipbite", blush = 2)

    ch_Rogue "{size=-5}Especially romance{/size}."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah also like writin' my own stories sometimes." 

    $ Rogue.change_face("worried2", blush = 1)

    ch_Player "Maybe I'll get to read one someday." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Maybe. . ."

    $ Rogue.change_face("worried1", eyes = "right")

    "The waitress comes and gives you the bill."

    $ Rogue.change_face("worried1")

    menu:
        extend ""
        "Pay it all yourself":
            "[Rogue.name] tries to grab the bill, but you hold it out of reach." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Player "It's my treat." 
            ch_Rogue "Are ya sure?" 
            ch_Player "Yep." 
            ch_Rogue "Thanks, ah really appreciate it." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_581
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_582

            $ Player.cash -= restaurant_bill[Player] + restaurant_bill[Rogue]
        "Split the bill":
            "[Rogue.name] tries to grab the bill, but you hold it out of reach." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 
            
            ch_Player "Why don't we split it." 
            ch_Rogue "Oh alright." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_583

            $ Player.cash -= math.ceil((restaurant_bill[Player] + restaurant_bill[Rogue])/2)
        "Let [Rogue.name] pay":
            "[Rogue.name] reaches over to grab the bill, and you let her." 
            
            $ Rogue.change_face("worried1", mouth = "smirk") 

            ch_Rogue "Let me cover it, [Rogue.Player_petname]."
            ch_Player "Thanks, [Rogue.petname]."

    "The bill is paid."

    $ Rogue.change_face("pleased1")

    ch_Player "I was thinking we could check out a movie after dinner."
    ch_Player "Sound good?" 

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'd love to." 

    "You both head over to the movie theater."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_171
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_176
    call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_148

    "You arrive at the ticket counter."

    $ movie_choice = None

    menu:
        extend ""
        "Pick a movie":
            menu:
                extend ""
                "Steamy romance":
                    $ movie_choice = "steamy_romance"

                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_584
                "Dramatic thriller":
                    $ movie_choice = "dramatic_thriller"

                    call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_585
        "Let [Rogue.name] pick":
            $ movie_choice = "dramatic_thriller"

            ch_Rogue "Thanks." 
            
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_586 
            
            "She picks a dramatic thriller."

    "You pay for the tickets since this was your idea and go inside to find your seats."

    $ Player.cash -= 40

    call remove_Characters(location = "bg_movies") from _call_remove_Characters_172
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_177
    call send_Characters(Rogue, "bg_movies", behavior = "on_date") from _call_send_Characters_149

    if movie_choice == "dramatic_thriller":
        call Rogue_first_date_path_1A from _call_Rogue_first_date_path_1A
    elif movie_choice == "steamy_romance":
        call Rogue_first_date_path_1B from _call_Rogue_first_date_path_1B

    $ fade_to_black(0.4)

    $ Rogue.change_face("smirk2", eyes = "right", blush = 1)

    "You continue discussing the movie on the walk back."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_173
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_178
    call send_Characters(Rogue, "bg_campus", behavior = "on_date") from _call_send_Characters_150

    "She leads you to her room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_174
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_179
    call send_Characters(Rogue, "bg_girls_hallway", behavior = "on_date") from _call_send_Characters_151

    "[Rogue.name] doesn't hesitate in pulling you into her room after she opens the door."

    call remove_Characters(location = Rogue.home) from _call_remove_Characters_175
    call set_the_scene(location = Rogue.home) from _call_set_the_scene_180
    call send_Characters(Rogue, Rogue.home, behavior = "on_date") from _call_send_Characters_152

    $ Rogue.change_face("smirk2", mouth = "lipbite", blush = 1)

    ch_Player "So. . ."
    ch_Player "About that kiss."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    "She looks apprehensive."
    ch_Player "Everything okay?"    

    menu:
        extend ""
        "We don't have to if you're not ready.":
            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_587 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_588
        "I'd really like to. . .":
            $ Rogue.change_face("worried1", mouth = "smirk", blush = 1) 

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_589
        "C'mon, it'll be fine.":
            $ Rogue.change_face("confused1", eyes = "right", blush = 1)

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_590

    pause 1.0

    $ Rogue.change_face("worried1", eyes = "right", blush = 1)

    ch_Rogue "It's just. . ."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Ah think ya can imagine how my power never let me give anyone a proper kiss. . ."

    pause 1.0

    $ Rogue.give(Rogue_running_mascara())

    call try_on(Rogue, Rogue.Wardrobe.Clothes["running mascara"]) from _call_try_on_9

    pause 1.0

    "Is she. . . crying?"
    ch_Player "[Rogue.name], really, are you okay?" 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Yeah. . . ah am, for once." 
    ch_Rogue "Ah really really like you."
    ch_Rogue "It just means a lot to me. . . that ah can finally do this with someone, and that someone is you. . ."
    ch_Rogue "Ah think ah'm ready." 

    menu:
        "Pull her into a kiss":
            $ Rogue.change_face("surprised2", mouth = "kiss", blush = 2) 
            
            "She's surprised at first, but quickly melts into your arms." 
            
            $ Rogue.change_face("kiss1", blush = 2) 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_591
        "Let her go at her own pace":
            $ Rogue.change_face("kiss1", blush = 2) 
            
            "She hesitates for a moment before tentatively pressing her lips against yours." 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_592 
            call change_Girl_stat(Rogue, "trust", 0) from _call_change_Girl_stat_593

    "You enjoy the feeling of each other's lips for a long moment. . ."

    $ Rogue.change_face("kiss1", blush = 3)

    ". . . before letting go."

    $ Rogue.History.update("kiss")

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "That was. . . real nice." 

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thanks for tonight, [Rogue.Player_petname]."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "Ah had a real nice time."
    ch_Player "I had a great time too."

    $ Rogue.change_face("sly", blush = 1)

    ch_Player "I'm sure our second, third, fourth. . . dates will be just as fun." 

    $ Rogue.change_face("smirk2")

    ch_Rogue "Heh, ah'm sure you're right."
    ch_Rogue "Ah can't wait."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "Also. . . you can call me Anna or Anna Marie if ya want." 

    $ Rogue.names.append("Anna")
    $ Rogue.names.append("Anna Marie")

    menu:
        extend ""
        "Continue calling her Rogue":
            pass
        "Call her Anna":
            $ Rogue.name = "Anna"
        "Call her Anna Marie":
            $ Rogue.name = "Anna Marie"

    if Rogue.petname == "Rogue":
        $ Rogue.petname = Rogue.name

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Player "Okay, [Rogue.name]."

    $ Rogue.change_face("worried1", eyes = "down", blush = 1)

    ch_Rogue "Damn, guess ah messed up my makeup too. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah gotta go deal with this."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "Goodnight, [Rogue.Player_petname]."
    ch_Player "Goodnight."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_176
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_181

    "You head back to your room."

    call remove_Characters(location = Player.home) from _call_remove_Characters_177
    call set_the_scene(location = Player.home) from _call_set_the_scene_182

    "It's getting late so you go straight to bed."

    $ Rogue.History.update("went_on_date_with_Player")
    $ Rogue.text_options.remove("want to go on that date tonight?")

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

    $ ongoing_Event = False

    jump go_to_sleep

label Rogue_first_date_path_1A:
    "The story is about a struggling writer who can't find any passion or inspiration for his stories."

    menu:
        extend ""
        "Hold [Rogue.name]'s hand":
            "You grab [Rogue.name]'s hand and give it a gentle squeeze, before interlacing your fingers with hers." 
            
            $ Rogue.change_face("surprised2", blush = 1) 
            
            pause 1.0 
            
            $ Rogue.change_face("sexy", eyes = "right", blush = 1) 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_594
        "Don't make a move":
            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 
            
            "After a few minutes. . ." 
            
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 

            $ temp = Rogue.Player_petname.capitalize()

            ch_Rogue "[temp]. . . can ah hold your hand?" 
            ch_Player "Sure." 
            
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 
            
            "She takes your hand and interlaces her fingers with yours." 
            
            $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 2)

    $ Rogue.change_face("worried1", eyes = "right")

    "The writer's monotonous life goes on as normal until he starts finding messages and sticky notes appearing out of nowhere around his apartment."

    $ Rogue.change_face("worried2", eyes = "right")

    "He has no idea where they're coming from, but they all have great ideas which he uses to jumpstart his writing."

    $ Rogue.change_face("confused1", eyes = "right")

    "Unbeknownst to the writer, a carbon monoxide leak in his apartment is simultaneously poisoning him, while also the cause for his inspiration."

    $ Rogue.change_face("worried1", eyes = "right")

    "His imaginative writing lands him a new job, but the gas also starts causing him to become delusional. "

    $ Rogue.change_face("worried2", eyes = "right")

    "The movie climaxes as the writer unknowingly acts out his latest story. . ."
    "Which is about a disturbed maniac who goes on a murder spree at their new job."
    "[Rogue.name] squeezes your hand tightly as the massacre unfolds on screen."

    $ Rogue.change_face("worried1", mouth = "smirk")

    "The movie ends and you both start heading back to campus, still holding hands."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_178
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_183
    call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_153

    ch_Rogue "Ah wasn't expectin' it to get so. . . nerve wrackin'."
    ch_Player "Yeah that got pretty twisted at the end."

    $ Rogue.change_face("smirk2")

    ch_Player "It had an interesting premise though. . ."

    return

label Rogue_first_date_path_1B:
    "The movie starts off following a bartender at a popular spot in the city."

    $ Rogue.change_face("smirk2", eyes = "right")

    menu:
        extend ""
        "Hold [Rogue.name]'s hand":
            "You grab [Rogue.name]'s hand and give it a gentle squeeze, before interlacing your fingers with hers." 
            
            $ Rogue.change_face("surprised2", blush = 1) 
            
            pause 1.0 
            
            $ Rogue.change_face("sexy", eyes = "right", blush = 1) 
            
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_595
        "Don't make a move":
            $ Rogue.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1) 
            
            "After a few minutes. . ." 
            
            $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2) 
            
            $ temp = Rogue.Player_petname.capitalize()

            ch_Rogue "[temp]. . . can ah hold your hand?" 
            ch_Player "Sure." 
            
            $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2) 
            
            "She takes your hand and interlaces her fingers with yours." 
            
            $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 2)

    $ Rogue.change_face("worried1", eyes = "right")

    "The bartender is good at her job - and beautiful - so plenty of male customers try flirting with her to no avail." 
    "She was recently widowed."

    $ Rogue.change_face("sad", eyes = "right")

    "She's been struggling to move on from her husband's death, until one night she spots a despondent man sitting at the far end of the bar. "

    $ Rogue.change_face("confused1", eyes = "right")

    "The man looks similar to her late husband, and she can't help but find out what's bothering him."

    $ Rogue.change_face("worried1", eyes = "right")

    "He tells her about his plight, how a former business partner started a conspiracy against him and it's ruining his life."

    $ Rogue.change_face("surprised1", eyes = "right", blush = 2)

    "The chance meeting turns into a thrilling romance as they rapidly fall in love, and the bartender uses her skills as a former super spy to stop the conspiracy."

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 2)

    "Nearly every other minute there's a graphic sex scene as the bartender demonstrates her prowess to her new beau."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    "The movie ends and you both start heading back to campus, still holding hands."

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_179
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_184
    call send_Characters(Rogue, "bg_mall", behavior = "on_date") from _call_send_Characters_154

    ch_Player "Well that was a. . . fun movie." 

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Rogue "Yeah. . . ah really enjoyed it."

    $ Rogue.change_face("smirk2", blush = 1)

    ch_Rogue "The female lead was a real badass."

    return