init python:

    def Laura_first_sex_part_one():
        label = "Laura_first_sex_part_one"

        conditions = [
            "Laura in Partners",
            "approval_check(Laura, threshold = Laura_thresholds['sex'])",
            "EventScheduler.Events['Laura_I_love_you'].completed",
            "day - EventScheduler.Events['Laura_I_love_you'].completed >= 3",
            "Player.location == Player.home",
            "not Present"]
            
        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Laura_first_sex_part_one:
    $ ongoing_Event = True

    "You had some odd dreams last night."
    "You can't recall any details, but [Laura.name] was present throughout most of them."
    "Once you're out of bed, you start the day as normal, brushing your teeth and getting dressed."

    call receive_text(Laura, "I need to talk to you") from _call_receive_text_699
    call receive_text(Laura, "In person") from _call_receive_text_700
    call open_texts(Laura) from _call_open_texts_22
    call receive_text(Laura, "This is important") from _call_receive_text_701
    call send_text(Laura, "everything okay?") from _call_send_text_88
    call receive_text(Laura, "Yes") from _call_receive_text_702
    call receive_text(Laura, "I'm in my room") from _call_receive_text_703
    call receive_text(Laura, "Come over") from _call_receive_text_704
    call send_text(Laura, "be right there") from _call_send_text_89

    pause 1.0

    hide screen phone_screen

    call remove_Characters(location = "bg_hallway") from _call_remove_Characters_115
    call set_the_scene(location = "bg_hallway") from _call_set_the_scene_330

    "You head straight to [Laura.name]'s room."

    call remove_Characters(location = "bg_girls_hallway") from _call_remove_Characters_116
    call set_the_scene(location = "bg_girls_hallway") from _call_set_the_scene_331

    "You arrive outside her door and are about to knock. . ."
    "The door suddenly swings open, and you're dragged inside."

    call remove_Characters(location = Laura.home) from _call_remove_Characters_117
    call send_Characters(Laura, Laura.home, behavior = False) from _call_send_Characters_7
    call set_the_scene(location = Laura.home) from _call_set_the_scene_332

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Player "So. . . what did you want to talk about?"

    $ Laura.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Laura "I. . ."
    ch_Laura ". . . trust you."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

    ch_Laura "I want to have sex with you."
    ch_Player "Wha. . ."

    $ Laura.change_face("furious", eyes = "squint", blush = 2)

    ch_Player "Where's this coming from?!"
    ch_Laura "This has been a long time coming."

    $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Laura "But I've been told a discussion is required beforehand."
    ch_Laura "By Dr. Reyes, and Rogue as well."
    ch_Player "[Cecilia.name], the doctor?"
    ch_Player "And poor [Rogue.name]. . ."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "So, we will talk about it."

    menu:
        extend ""
        "I also think talking about it is a good idea. . .":
            $ Laura.change_face("appalled1", mouth = "lipbite", blush = 2) 
            
            $ Laura.change_face("angry1", eyes = "right", mouth = "lipbite", blush = 2) 
            
            ch_Laura "Good. . ."

            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_934 
            call change_Girl_stat(Laura, "trust", 0) from _call_change_Girl_stat_935
        "Wha. . . I. . . uh. . . yeah, talking is a good idea.":
            $ Laura.change_face("angry1", eyes = "squint", blush = 1) 

            ch_Laura "It is."
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_936
        "Oh god, don't tell me I have to explain this shit to you. . .":
            $ Laura.change_face("angry1", eyes = "squint", blush = 1) 

            ch_Laura "No, you do not."
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_937

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "I am. . . aware of all the considerations. . ."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "After the Juggernaut attacked the institute, [Cecilia.name] noticed my presence watching over you in the infirmary."

    $ Laura.change_face("angry1", eyes = "right", blush = 1)

    ch_Laura "Despite my lack of visible injury, she insisted on a health checkup for me as well."

    $ Laura.change_face("neutral", blush = 1)

    ch_Laura "[Cecilia.name] asked about more than just injuries, if I had ever seen something called a 'gynecologist' or had proper 'sexual education.'"

    $ Laura.change_face("furious", eyes = "right", blush = 1)

    ch_Laura "Cheap trick, using you as bait."

    $ Laura.change_face("suspicious2", blush = 1)

    ch_Laura "I was made aware of several things during the discussion."

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "I am apparently 'hyperfertile', and most standard birth control methods are ineffective due to my powers."

    $ Laura.change_face("angry1", blush = 1)

    ch_Player "Oh, well I guess tha-"
    ch_Laura "Not {i}all{/i} birth control methods."
    ch_Laura "She gave me something called an 'IUD', which turned out to be effective."

    $ Laura.birth_control = True

    ch_Player "Ah. . ."

    $ Laura.change_face("confused1", blush = 1)

    ch_Laura "She also remarked on my lack of something called a 'hymen.'"
    ch_Laura "She said it is not uncommon for this to be lost, even while I'm still a virgin."
    ch_Player "Considering all the training you went through as a child. . ."

    $ Laura.change_face("suspicious1", blush = 1)

    ch_Laura "That was her hypothesis as well."

    $ Laura.change_face("angry1", blush = 1)

    ch_Laura "Now that you are aware of these things. . ."

    $ Laura.change_face("confused1", eyes = "squint", blush = 1)

    ch_Laura "We can have sex?"

    $ Laura.change_face("confused2", blush = 1)

    ch_Player "Heh, well, you kinda ruined the romance a bit. . ."

    $ Laura.change_face("confused1", blush = 1)

    ch_Player "But, I agree, it was important to go over this stuff beforehand."

    menu:
        extend ""
        "If you're comfortable, I'd love to have sex with you." if Player.stamina:
            $ Laura.change_face("sexy", blush = 2)
            
            $ EventScheduler.Events["Laura_first_sex_part_two"].start()
        "If you're comfortable, I'd love to have sex with you." if not Player.stamina:
            pass
        "It's not that I don't want to, but can we wait?":
            $ Laura.change_face("neutral", blush = 1)

            ch_Laura "Fine, we can wait." 
            
            $ Laura.change_face("sexy", blush = 1) 
            
            ch_Laura "Hopefully not too long. . ."

    $ ongoing_Event = False

    return

init python:

    def Laura_first_sex_part_two():
        label = "Laura_first_sex_part_two"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Laura_first_sex_part_two:
    $ ongoing_Event = True

    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False
    $ has_ejaculation_control = False

    if Laura.position == "doggy":
        call show_pose(Laura, "standing") from _call_show_pose_3

    if not Action_screen_showing:
        show screen Action_screen()

    $ Laura.grool = 2

    $ Laura.change_face("sexy", blush = 1)

    pause 1.0

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "I am comfortable."

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "You have done more than gain my trust."

    $ Laura.change_face("kiss2", blush = 1)

    "[Laura.name] pulls you into a kiss, more gently than normal."
    "It's not gentle for long, as her breath runs ragged, and you pull her in close."

    $ Laura.change_face("kiss1", blush = 2)

    "Your tongues start intertwining, and her hand ventures its way down your torso."
    "She grabs hold of your crotch, meanwhile you also start helping her out of her clothes."

    call take_off_everything_but(Laura, ["bra", "skirt", "pants", "hose", "underwear", "socks"]) from _call_take_off_everything_but_13

    $ Laura.change_face("sexy", eyes = "down", blush = 1)

    if Laura.quirk:
        "[Laura.name] doesn't dally and basically tears your pants off."
    else:
        ch_Laura "Take your pants off. . . please. . ." 
        "You pull them down, exposing yourself to her."

    $ Laura.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    ch_Laura "It really is. . . large. . ."

    $ Laura.History.update("seen_Player_naked")

    call take_off_everything_but(Laura, ["bra", "hose", "underwear", "socks"]) from _call_take_off_everything_but_14

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "I'm ready."

    $ Laura.change_face("sexy", blush = 2)

    "She lays down onto the bed, spreading her legs for you."

    call request_position(Laura, "missionary", automatic = True) from _call_show_pose_4

    $ Laura.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    if Laura.Clothes["underwear"].string:
        pause 1.0

        call undress(Laura, "underwear") from _call_undress_9

        "[Laura.name] moves her [Laura.Clothes[underwear].short_name] to the side, exposing her pussy."

    "She's already soaking wet."

    $ Laura.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Player "I'll start slow, okay?"

    $ Laura.change_face("sexy", blush = 1)

    "She gives you a small nod."

    $ Laura.change_face("sexy", eyes = "down", blush = 2)

    $ Action = ActionClass("sex", Player, Laura)

    call start_Action(Action) from _call_start_Action_5

    $ Action.mode = 0

    "You bring yourself close, lightly pressing your tip against her."

    $ Laura.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

    "Only now do you realize how small she really is."
    "Normally, her short stature is overshadowed by how dangerous she can be. . ."
    "But now, with her being so vulnerable, it's different."

    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Put it in."

    $ Laura.change_face("sexy", eyes = "down", blush = 1)
    
    $ speed = 0.01
    $ starting_depth = 0.025

    $ Action.mode = 2

    "Slowly, you start pushing."

    $ Laura.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2)

    $ speed = 0.0005
    $ starting_depth = 0.05

    "It's a very tight fit, and she lets out a soft growl, prompting you to stop."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

    $ speed = 0.001
    $ starting_depth = 0.075

    ch_Laura "Keep going. . ."

    $ Laura.change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2)

    $ speed = 0.0005
    $ starting_depth = 0.1

    "You oblige and continue pushing yourself inside."
    
    $ speed = 0.001
    $ starting_depth = 0.125

    "The resistance keeps increasing, making it harder the further you go."
    
    $ speed = 0.0005
    $ starting_depth = 0.15
    
    "She urges you to continue, so you do."

    $ Laura.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2)

    $ speed = 0.001
    $ starting_depth = 0.25

    "Finally, you push through the resistance, causing her to let out a whimper."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

    ch_Player "Are you okay?"

    $ Laura.change_face("sexy", blush = 2)

    ch_Laura "Yes, keep going."
    ch_Laura "If I wanted you to stop, I would've told you."

    $ speed = 0.3
    $ intensity = 0.5
    $ starting_depth = 0.2

    "You pull back slightly, before gently thrusting forward, starting a slow rhythm." 

    $ Laura.change_face("worried2", mouth = "lipbite", blush = 2)

    "As you continue, [Laura.name]'s eyes widen in surprise."
    ch_Laura "Go deeper."
    "Right as you do, you can feel her start to twitch and suddenly tightens around your cock." with orgasm_shake

    $ speed = 0.001

    pause 1.0
    
    $ Action.mode = 0

    $ Laura.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2) 

    "Did she. . . orgasm already?"

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    ch_Laura "Hmm. . ."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

    "All of the sudden, it's like a switch was flipped, and she grabs your hips, pulling you right back inside."
    
    $ speed = 0.5
    $ intensity = 1.0

    $ Action.mode = 2

    $ Laura.change_face("angry1", eyes = "down", mouth = "lipbite", blush = 2)

    ch_Laura "{i}Grrrrrr{/i}. . ."
    ch_Laura "Deeper."

    $ Laura.change_face("appalled1", mouth = "lipbite", blush = 2)

    $ intensity = Action.max_intensity[Action.mode - 1]

    "She pulls on your hips again, pulling you all the way down to the hilt."
    "Her eyes light up again, and you can feel yourself drawing close to the edge as well. . ."

    $ Laura.change_face("angry1", mouth = "lipbite", blush = 2)

    $ speed = 1.0

    ch_Laura "Faster."
    "You speed up, and [Laura.name] starts what sounds like a mixture of growling and moaning."
    "She grinds her hips against you, eyes boring into your soul."
    "She starts twitching again, and you're about to blow as well."

    $ Laura.change_face("sly", mouth = "lipbite", blush = 2)

    "[Laura.name] notices the look on your face and starts grinding her hips even faster."
    "Just as you're about to cum, and right as it looks like [Laura.name] orgasms, she pushes you out." with orgasm_shake
    
    $ Action.mode = 0

    $ Laura.change_face("sly", eyes = "down", mouth = "lipbite", blush = 2)

    $ Player.orgasming = "cumshot"

    pause 1.0
    
    $ Laura.spunk["belly"] = True

    "You cum all over her stomach, as she violently shudders in ecstasy."

    $ Player.orgasming = False
    
    $ Laura.change_face("kiss2", blush = 2)

    "She grabs your neck, pulling you down into a kiss, while she continues to twitch uncontrollably."

    $ Laura.change_face("sexy", blush = 2) 

    ch_Laura "I am going to need a {i}lot{/i} of sex with you. . ."

    call stop_all_Actions(close_interface = False) from _call_stop_all_Actions_3

    hide screen Action_screen

    call closing_Action_interface from _call_closing_Action_interface_1
    
    if Laura.History.check("swallowed_cum"):
        call swallow_cum(Laura) from _call_swallow_cum_13

        "[Laura.name] wipes the cum off of her stomach, before eating it." 
    else:
        call clean_cum(Laura) from _call_clean_cum_1

        "[Laura.name] cleans the cum off of her stomach."

    call change_Outfit(Laura, Laura.Wardrobe.Outfits[Laura.Outfit.name]) from _call_change_Outfit_46

    $ Laura.change_face("sly", blush = 2)

    ch_Laura "I enjoyed that {i}very{/i} much."

    menu:
        extend ""
        "That was amazing. I'm glad you enjoyed it as well.":
            $ Laura.change_face("sexy", blush = 1) 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_938
        "That was okay. You'll get better the more we do it together.":
            $ Laura.change_face("confused1", blush = 1) 
            
            call change_Girl_stat(Laura, "love", 0) from _call_change_Girl_stat_939

    $ Laura.change_face("worried1", eyes = "right", blush = 1)

    ch_Laura "So that was. . . 'making love'. . ."

    $ Laura.change_face("worried1", mouth = "smirk")

    ch_Laura "Thank you."
    ch_Laura "I love you."
    ch_Player "I love you too."

    $ Laura.change_face("sexy", blush = 1)

    ch_Laura "I am looking forward to doing that with you {i}many{/i}, {i}many{/i} times."

    if not Laura.History.check("sex"):
        $ Laura.History.update("sex")

    $ Player.stamina -= 1

    $ speed = 1.0
    $ intensity = 1.0
    $ starting_depth = 0.0

    $ ongoing_Event = False

    # call move_location(Player.location) from _call_move_location_6

    return