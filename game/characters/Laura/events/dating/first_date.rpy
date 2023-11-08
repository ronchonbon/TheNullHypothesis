init python:

    import math

    def Laura_first_date():
        label = "Laura_first_date"

        conditions = [
            "Laura in Player.date_planned.keys()",
            "time_index == 2",
            "not Laura.History.check('went_on_date_with_Player')"]

        waiting = True
        traveling = True

        priority = 99

        return EventClass(label, conditions, waiting = waiting, traveling = traveling, priority = priority)

label Laura_first_date:
    $ ongoing_Event = True

    hide screen phone_screen

    if weather == "rain":
        $ weather = None

    $ Party = []

    play music "sounds/music/Evening.ogg" fadeout 1.0 fadein 1.0 if_changed

    if Laura.History.check("quirk_encouraged") < Laura.History.check("quirk_discouraged") or Player.location != "bg_hallway":
        "You head into the hallway right outside your room."
        
        call remove_Characters(location = "bg_hallway") from _call_remove_Characters_83
        call set_the_scene(location = "bg_hallway") from _call_set_the_scene_92

        "[Laura.name] doesn't seem to be here for the date yet."
        "You wait around for a bit."

    $ Laura.change_face("neutral")

    call send_Characters(Laura, "bg_hallway", behavior = "on_date") from _call_send_Characters_86

    "[Laura.name] suddenly appears right in front of you."
    ch_Laura "Let's go."

    $ Laura.change_face("neutral", eyes = "right")

    "She grabs you by the wrist and starts dragging you along."
    ch_Player "Jesus, where the hell did you come from??"

    $ fade_to_black(0.4)

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_84
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_93
    call send_Characters(Laura, "bg_campus", behavior = "on_date") from _call_send_Characters_87

    $ Laura.change_face("neutral", eyes = "right")

    ch_Player "Where are we going???"

    $ Laura.change_face("confused1")

    "She lets go of your wrist and faces you."
    ch_Laura ". . . On a date."

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Laura "Did you hit your head?"
    ch_Player "I know that. . . but {i}where{/i} are we going on this date?"

    $ Laura.change_face("smirk2")

    ch_Laura "I have done research, we are going to a restaurant." 
    ch_Player "Okay, which restaurant?"

    $ Laura.change_face("smirk1")

    ch_Laura "It's in the mall, I just picked the one with the most steak options." 

    $ Laura.change_face("smirk1", eyes = "right")

    "She grabs your wrist again, and you both head to the mall."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_85
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_94
    call send_Characters(Laura, "bg_mall", behavior = "on_date") from _call_send_Characters_88

    $ Laura.change_face("confused2", eyes = "right")

    "You arrive outside the restaurant, but apparently [Laura.name] didn't know reservations were a thing. . ."
    "Luckily it's not too busy, and you get seated quickly."

    $ eating_dinner = True
    $ ordered_food = True
    $ food_arrived = False
    $ drinking_wine = False

    call remove_Characters(location = "bg_restaurant") from _call_remove_Characters_86
    call set_the_scene(location = "bg_restaurant") from _call_set_the_scene_95
    call send_Characters(Laura, "bg_restaurant", behavior = "on_date") from _call_send_Characters_89

    $ Laura.change_face("neutral", eyes = "down")

    "The waitress comes by and hands you both a menu."

    $ ordered_food = False

    "You pick. . ."

    $ chosen_meal = {}
    $ restaurant_bill = {}

    call restaurant_menu(Player, "steakhouse") from _call_restaurant_menu_7

    $ Laura.change_face("furious", eyes = "down") 

    "After deciding, you look up to see [Laura.name] staring intensely at her menu."
    ch_Player "Is everything okay?"

    $ Laura.change_face("confused1")

    pause 1.0

    $ Laura.change_face("neutral")

    ch_Player "You're gonna burn a hole through that poor menu with such an intense stare." 
    ch_Laura "What are you getting?"

    if chosen_meal[Player] in ["filet mignon", "ribeye"]:
        ch_Player "Steak."
    else:
        $ temp = chosen_meal[Player].capitalize()

        ch_Player "[temp]."
        
    $ Laura.change_face("furious", eyes = "down") 

    ch_Laura "I thought more steak options was a good thing. . ."

    $ Laura.change_face("angry1", blush = 1) 

    ch_Laura "What is the difference between a 'ribeye' and a 'filet mignon'?!"

    $ Laura.change_face("confused1") 

    "You explain the different cuts of meat."
    ch_Laura "Which is better?" 

    $ temp = chosen_meal[Player]

    if chosen_meal[Player] in ["filet mignon", "ribeye"]:
        menu:
            extend ""
            "I prefer the [temp], was gonna order that one.":
                ch_Laura "Hmm. . ." 
                
                $ Laura.change_face("neutral") 
                
                ch_Player "Get the other cut, and you can try mine too." 
                ch_Laura "Fine."

                if chosen_meal[Player] == "filet mignon":
                    $ chosen_meal[Laura] = "ribeye"
                elif chosen_meal[Player] == "ribeye":
                    $ chosen_meal[Laura] = "filet mignon"
    else:
        menu:
            extend ""
            "Filet mignon is better.":
                $ Laura.change_face("neutral")

                ch_Laura "Then I will try that one."

                $ chosen_meal[Laura] = "filet mignon"
            "Ribeye is better.":
                $ Laura.change_face("neutral")

                ch_Laura "Then I will try that one."

                $ chosen_meal[Laura] = "ribeye"
            "I don't really eat steak. . .":
                $ Laura.change_face("suspicious1") 
                
                ch_Player "I hear the filet is good?" 

                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_326

                ch_Laura "Fine, I will try that one." 
                
                $ Laura.change_face("neutral")

                $ chosen_meal[Laura] = "filet mignon"

    $ restaurant_bill[Laura] = 45

    $ Laura.change_face("neutral", eyes = "right")

    "The waitress comes to take your order."
    ch_Player "I'll h-"

    "[Laura.name] interrupts you."

    $ temp = chosen_meal[Laura]

    ch_Laura "Give me the [temp]."

    $ Laura.change_face("neutral")

    $ temp = chosen_meal[Player]

    ch_Laura "He'll have the [temp]."
    ch_Player ". . ."

    $ Laura.ordered_for_you_last_time = True

    $ ordered_food = True

    pause 1.0

    $ fade_to_black(0.4)

    $ food_arrived = True

    $ fade_in_from_black(0.4)

    $ Laura.change_face("neutral", eyes = "down", mouth = "lipbite")

    "The food arrives, and you can tell she's restraining her desire to devour the meal like an animal."
    "[Laura.name] does her best impression of table manners."

    if chosen_meal[Player] in ["filet_mignon", "ribeye"]:
        $ Laura.change_face("neutral", eyes = "down")

        pause 1.0

        $ Laura.change_face("neutral", eyes = "squint")

        "You notice she's eyeing your steak as well."

        ch_Player "Wanna try it?" 

        $ Laura.change_face("neutral")

        "She just nods."
        "You cut her a piece, and she leans over, eating it right off of your fork."

        $ Laura.change_face("neutral", eyes = "down", mouth = "open")

        pause 1.0

        $ Laura.change_face("neutral", eyes = "down")

        if chosen_meal[Player] == "ribeye":
            $ Laura.change_face("neutral")

            ch_Laura "You were right, ribeye is better." 

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_327
        else:
            $ Laura.change_face("neutral")

            ch_Laura "Ribeye is better."
    else:
        ch_Player "How is it?"

        $ Laura.change_face("smirk2")

        if chosen_meal[Laura] == "ribeye":
            ch_Laura "Great."
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_328
        else:
            ch_Laura "Good."

    $ Laura.change_face("neutral", eyes = "down")

    "Despite restraining her appetite, [Laura.name] finishes her food well before you."
    "You decide now is probably a good time to find out more about her."

    $ Laura.change_face("confused1")

    ch_Player "So. . . what do you do for fun?"
    ch_Laura "Fun?"
    ch_Player "Yeah, in your free time."

    $ Laura.change_face("confused3")

    ch_Laura "Free time?"
    ch_Player "Something you enjoy doing when you're not busy." 

    $ Laura.change_face("confused1")

    ch_Laura "I 'enjoy' training."

    $ Laura.change_face("confused2")

    ch_Player "Okay, but after you finish training for the day."
    ch_Laura "Why would I have free time after training?"

    $ Laura.change_face("neutral")

    ch_Laura "That would only mean I didn't train for long enough."
    ch_Player "Exactly how long do you train?"
    ch_Laura "Depends if I'm required to attend class or not." 

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "Such a waste of time. . ."

    $ Laura.change_face("neutral")

    ch_Laura "Usually six to eight hours per day." 

    $ Laura.change_face("confused1")

    ch_Player "Jesus. . ."
    ch_Player "Okay, but let's say you're satisfied with how much you've trained one day."
    ch_Player "And you still have time left before bed."

    $ Laura.change_face("confused2")

    ch_Player "What would you want to do?"

    $ Laura.change_face("confused3")

    pause 1.0

    $ Laura.change_face("neutral", eyes = "right")

    ch_Player "For fun. . ."
    ch_Laura "Fun. . ." 

    $ Laura.change_face("neutral")

    ch_Laura "Storm did show me one of those television shows. . ."

    $ Laura.change_face("neutral", eyes = "right")

    ch_Laura "Where people fought each other inside a cage."

    $ Laura.change_face("confused1")

    ch_Laura "I. . . think I had 'fun' watching that."

    ch_Player "Okay, so you like combat sports."

    $ Laura.change_face("neutral")

    ch_Player "Boxing, MMA, martial arts, and stuff?"
    ch_Laura "Yes."

    $ Laura.change_face("confused1")

    ch_Player "Did [Ororo.name] show you any other shows or movies?" 
    ch_Laura "What exactly is. . . a 'movie'?"

    $ Laura.change_face("confused3")

    ch_Player "You don't know what a movie is?" 

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "No. . ."

    $ Laura.change_face("confused1")

    ch_Player "Well then we're going to see one after dinner."
    ch_Player "There's a theater right here in the mall." 

    $ Laura.change_face("neutral") 

    ch_Laura "Fine, my research mentioned this as a common dating event."

    $ Laura.change_face("neutral", eyes = "right")

    "The waitress comes and gives you the bill."

    $ Laura.change_face("neutral")

    ch_Laura "Also, the man is apparently expected to pay for the date."

    menu:
        extend ""
        "Don't argue and pay" if Player.cash >= restaurant_bill[Player] + restaurant_bill[Laura]:
            $ Laura.change_face("smirk2")

            ch_Player "Fine, I've got it." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_329

            $ Player.cash -= restaurant_bill[Player] + restaurant_bill[Laura]
        "Explain why you should split the bill" if Player.cash >= math.ceil((restaurant_bill[Player] + restaurant_bill[Laura])/2):
            ch_Player "It's become more common recently for people to split the bill while on a date." 
            
            $ Laura.change_face("confused1") 
            
            ch_Laura "That seems fair." 
            
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_330

            $ Player.cash -= math.ceil((restaurant_bill[Player] + restaurant_bill[Laura])/2)
        "Have her pay":
            ch_Player "The person who asked for the date in the first place is usually expected to pay. . ." 
            
            $ Laura.change_face("neutral", eyes = "squint") 
            
            ch_Laura "Fine." 
            ch_Laura "Then you will pay for the movie since that was your idea." 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_331

    "The bill is paid."
    "You both head over to the movie theater."

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_87
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_96
    call send_Characters(Laura, "bg_mall", behavior = "on_date") from _call_send_Characters_90

    $ Laura.change_face("angry1", eyes = "right")

    "You arrive at the ticket counter."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura ". . ."

    $ Laura.change_face("angry1")

    ch_Laura "None of these names mean anything to me." 

    $ Laura.change_face("neutral")

    ch_Laura "You pick."
    "After a moment of consideration. . ."
    "You end up choosing the new 'Ron Bic' movie."
    "The main character in this series is known for killing people with a bic lighter in very creative ways."
    "There's also plenty of gun-fu and martial arts."
    "You pay for the tickets, since this was your idea, and you both go inside to find your seats."

    $ Player.cash -= 40

    call remove_Characters(location = "bg_movies") from _call_remove_Characters_88
    call set_the_scene(location = "bg_movies") from _call_set_the_scene_97
    call send_Characters(Laura, "bg_movies", behavior = "on_date") from _call_send_Characters_91

    $ Laura.change_face("surprised1", eyes = "right")

    "Once the movie gets going, and the action starts, you look over to see [Laura.name] entranced by all the killing on screen."
    "Ron Bic is in a sticky situation after he's unwittingly sent to kill the CEO of his favorite lighter company."
    "Ron quickly realizes a rival lighter company set him up, and he vows to get revenge."

    $ Laura.change_face("surprised1", mouth = "smirk", eyes = "right")

    "He has to fight his way through hundreds of evil henchmen in a lighter factory finally takes out the real bad guy in the end."
    "There's a plethora of violent and fiery deaths as well as some impressive choreography."

    $ Laura.change_face("angry1", eyes = "right")

    ch_Laura "It's over?!"

    $ Laura.change_face("angry1")

    ch_Laura "I want to know what happens next."
    "With the movie over, you leave the theater." 

    $ time_index = 3

    $ lighting = "night"

    call remove_Characters(location = "bg_mall") from _call_remove_Characters_89
    call set_the_scene(location = "bg_mall") from _call_set_the_scene_98
    call send_Characters(Laura, "bg_mall", behavior = "on_date") from _call_send_Characters_92

    $ Laura.change_face("confused1")

    ch_Laura "Where do they get all the people to kill in the movie?"
    ch_Laura "Do they use death row prisoners?"

    $ Laura.change_face("confused2")

    ch_Player "You realize that was all fake. . . right?"
    ch_Laura "Those were fake people?"

    $ Laura.change_face("neutral", eyes = "squint")

    ch_Player "They were real people, but they used special effects to make it look convincing."
    "You continue to explain during the walk back."

    call remove_Characters(location = "bg_campus") from _call_remove_Characters_90
    call set_the_scene(location = "bg_campus") from _call_set_the_scene_99
    call send_Characters(Laura, "bg_campus", behavior = "on_date") from _call_send_Characters_93

    $ Laura.change_face("neutral")

    "[Laura.name] leads you to her room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_91
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_100
    call send_Characters(Laura, "bg_girls_hallway", behavior = "on_date") from _call_send_Characters_94

    ch_Player "I had a really nic-"
    ch_Laura "Come in."
    "She doesn't let you respond and pulls you into the room after her."

    call remove_Characters(location = Laura.home) from _call_remove_Characters_92
    call set_the_scene(location = Laura.home) from _call_set_the_scene_101
    call send_Characters(Laura, Laura.home, behavior = "on_date") from _call_send_Characters_95

    $ Laura.change_face("neutral", eyes = "right", blush = 1)

    ch_Laura "My research also indicated people usually. . . kiss after a date."

    menu:
        extend ""
        "If you're not ready, that's totally fine.":
            ch_Player "There's no pressure." 
            
            $ Laura.change_face("smirk2", eyes = "right", blush = 2) 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_332 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_333
        "That's usually the case, yeah.":
            $ Laura.change_face("confused1", mouth = "smirk", eyes = "squint", blush = 2) 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_334
        ". . . Well?":
            $ Laura.change_face("angry1", eyes = "right", blush = 1)

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_335

    $ Laura.change_face("neutral", eyes = "right", mouth = "lipbite", blush = 1)

    "You can tell she's still a bit apprehensive."

    ch_Player "If you don't wan-" 

    $ Laura.change_face("neutral", eyes = "squint", mouth = "lipbite", blush = 1)

    "[Laura.name] doesn't let you finish and just pulls you in for a kiss."

    $ Laura.change_face("kiss1", blush = 2)

    "She shudders as your lips connect and pulls away after a couple seconds."

    $ Laura.change_face("sexy", blush = 3)

    ch_Player "That w-"

    $ Laura.change_face("kiss1", blush = 2)

    "She pulls you right into another kiss, squeezing you tightly against her. She doesn't pull away for even longer this time."

    $ Laura.History.update("kiss")

    $ Laura.change_face("neutral", mouth = "lipbite", blush = 1)

    ch_Player "{i}Ahem{/i}. . . I guess you liked it."

    $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Laura "My instincts were screaming at me. . ."

    $ Laura.change_face("neutral", eyes = "squint", blush = 1)

    ch_Laura "But. . . I think I can trust you."
    ch_Player "You can." 
    ch_Player "Did you wa-" 

    $ Laura.change_face("smirk2", blush = 1)

    ch_Laura "I enjoyed this date, we will do it again."

    $ Party = []

    "With that, she unceremoniously pushes you out of the room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_93
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_102

    ch_Player ". . . I enjoyed it too."
    "You head back to your room."

    call remove_Characters(location = Player.home) from _call_remove_Characters_94
    call set_the_scene(location = Player.home) from _call_set_the_scene_103

    "It's late so you go straight to bed."

    $ fade_to_black(0.4)

    "You have a couple of dreams, but you don't remember any details about them."

    call wait_around from _call_wait_around

    "You wake up feeling well rested."

    call set_the_scene(location = "bg_shower_Player") from _call_set_the_scene_104

    "Getting out of bed, you go to the bathroom and start brushing your teeth."

    call knock_on_door(times = 3, intensity = 1.5) from _call_knock_on_door_1

    "You hear someone knocking on the door, forcefully."
    ch_Player "I'll be there in a second!"
    "The knocking stops."

    call set_the_scene(location = Player.home) from _call_set_the_scene_105

    "You finish brushing your teeth and unlock the door."

    $ Laura.change_face("angry1", blush = 1)

    call send_Characters(Laura, Player.home, behavior = False) from _call_send_Characters_96

    "[Laura.name] pushes her way in as soon as you unlock it."

    $ Laura.change_face("angry1", eyes = "squint", blush = 1)

    ch_Player "Uh, good morning?"
    "She doesn't say anything, before trying to pull you into another kiss."

    $ Laura.change_face("kiss1", blush = 1)

    menu:
        extend ""
        "Let her":
            pass
        "She should ask first (discourage_quirk)":
            ch_Player "Wait." 
            ch_Player "You should really ask first." 
            
            $ Laura.change_face("confused1", blush = 1) 
            
            pause 1.0 
            
            $ Laura.change_face("angry1", blush = 1) 
            
            ch_Laura "Why?" 
            ch_Laura "You wanted to do this last night." 
            ch_Player "Right, but just because someone agreed to something once, doesn't mean they're always willing to in the future." 
            
            $ Laura.change_face("angry1", blush = 1) 
            
            ch_Laura "Fine." 
            ch_Laura "I want to kiss you again." 
            ch_Laura "Will you let me?" 
            ch_Player "Yes, please do." 
            
            $ Laura.change_face("sexy", blush = 1) 
            
            pause 1.0 
            
            $ Laura.change_face("kiss1", blush = 1)

            $ Laura.History.update("Player_told_to_ask_to_kiss")
            $ Laura.History.update("quirk_discouraged")

    "[Laura.name] roughly pulls you towards her, and your lips connect."

    $ Laura.change_face("kiss1", blush = 2)

    "Her lips are clumsy, and it's clear she doesn't know what she's doing. . ."

    $ Laura.change_face("kiss1", brows = "furrowed", blush = 2)

    "She makes up for lacking experience with intensity and enthusiasm."

    call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_336

    "Fingers dig into your flesh, nostrils flaring, and her breath turns ragged."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 3)

    "Finally, after a long moment, she lets go."

    $ Laura.History.update("kiss")

    if Laura.History.check("Player_told_to_ask_to_kiss"):
        $ Laura.change_face("confused1", blush = 2)

        ch_Laura ". . ."
        ch_Laura "We will. . . kiss again in the future?"

        $ Laura.change_face("sly", blush = 1)

        ch_Player "Absolutely."
    else:
        $ Laura.change_face("sexy", blush = 2)

        menu:
            extend ""
            "Encourage this behavior (encourage_quirk)":
                ch_Player "I. . . {i}really{/i} liked that." 
                ch_Player "I wouldn't mind if you just. . . kissed me whenever you want. . ." 
                
                $ Laura.change_face("surprised2", blush = 1) 
                
                pause 1.0 
                
                $ Laura.change_face("sly", blush = 1) 
                
                call change_Girl_stat(Laura, "desire", 0) from _call_change_Girl_stat_337 
                
                ch_Laura "Good." 
                ch_Laura "I. . . enjoyed that as well." 
                ch_Laura "Expect it to happen again." 
                
                call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_338

                $ Laura.History.update("quirk_encouraged")
            "Discourage this behavior (discourage_quirk)":
                ch_Player "I. . . really liked that." 
                ch_Player "But could you ask first next time?" 
                
                $ Laura.change_face("confused1", blush = 1) 
                
                pause 1.0 
                
                $ Laura.change_face("neutral", blush = 1) 
                
                ch_Laura "Fine."

                $ Laura.History.update("quirk_discouraged")

    $ Laura.change_face("neutral")

    ch_Laura "I need to go train."
    ch_Laura ". . . bye."

    $ Laura.schedule[time_index] = ["bg_danger", "training"]

    call send_Characters(Laura, "bg_danger", behavior = "training") from _call_send_Characters_97

    $ Laura.History.update("went_on_date_with_Player")
    $ Laura.text_options.remove("ready for that date?")

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

    return