init python:

    def Rogue_first_sex():
        label = "Rogue_first_sex"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Rogue_first_sex:
    $ ongoing_Event = True

    $ Rogue.change_face("worried1", mouth = "smirk")

    "You head towards the mansion, but [Rogue.name] puts an arm on you, holding you back."

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Before we head inside. . . and, ya'know. . ."

    $ Rogue.change_face("smirk2")

    ch_Rogue "Ah'd like to just enjoy the beautiful night with ya. . ."

    $ Rogue.change_face("sexy", eyes = "right")

    "[Rogue.name] takes your hand, and you both lazily wander around the campus grounds, enjoying each other's company and the beauty of your surroundings."

    $ Rogue.change_face("sexy")

    "After a while, [Rogue.name] looks at you with a glint in her eye."

    $ Rogue.change_face("worried1", mouth = "lipbite")

    ch_Rogue "Ah'm ready. . ."

    call remove_Characters(location = Player.home) from _call_remove_Characters_289
    call set_the_scene(location = Player.home) from _call_set_the_scene_374
    call send_Characters(Rogue, Player.home, behavior = "on_date") from _call_send_Characters_267

    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False
    $ has_ejaculation_control = False

    if Rogue.position == "doggy":
        call show_pose(Rogue, "standing") from _call_show_pose_6

    if not Action_screen_showing:
        show screen Action_screen()

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "If ah'm honest. . . ah'm a lot more nervous than ah thought ah'd be. . ."
    ch_Player "We'll take it slow, and I'll be gentle, promise."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "That ain't the reason, and ah trust ya."
    ch_Rogue "Ah've just been anticipatin' this moment for so damn long."

    $ Rogue.change_face("sexy", blush = 1)

    pause 1.0

    $ Rogue.change_face("kiss2", blush = 1)

    "You pull [Rogue.name] into your arms, holding her close as your lips connect."

    $ Rogue.History.update("kiss")

    call change_Girl_stat(Rogue, "desire", 0) from _call_change_Girl_stat_1146

    "She trembles slightly, as a mixture of anticipation and trepidation runs through her veins."

    call take_off_everything_but(Rogue, ["bra", "skirt", "pants", "hose", "underwear", "socks"]) from _call_take_off_everything_but_17

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 1)

    if Rogue.quirk:
        ch_Rogue "Take whatever ya want off of me. . ." 
    else:
        ch_Rogue "Let me help ya with that. . ."

    call take_off_everything_but(Rogue, ["hose", "underwear", "socks"]) from _call_take_off_everything_but_18

    "[Rogue.name] takes everything but her underwear off."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    if Rogue.quirk:
        ch_Rogue "May ah?" 
        
        $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 1) 
        
        "She bends down and dutifully helps you out of your own clothes."
    else:
        $ Rogue.change_face("sly", mouth = "lipbite", blush = 1)

        "She just stands there, waiting for you to undress as well." 
        "You take everything off, exposing yourself to her."

    $ Rogue.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 2)

    ch_Rogue "My lord. . ."
    ch_Rogue "Ah reckon it gets bigger every time ah see it."

    $ Rogue.change_face("worried1", blush = 1)

    ch_Rogue "It's a bit intimidatin' if ah'm honest. . ."
    "She hesitates for a moment, but walks over to the bed and lays down on her back."

    call request_position(Rogue, "missionary", automatic = True) from _call_show_pose_7

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah love you."
    ch_Player "I love you too."

    $ Rogue.change_face("sexy", eyes = "down", blush = 1)

    ch_Player "Are you ready?"

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah am. . . ah'm all yours."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    if Rogue.Clothes["underwear"].string:
        pause 1.0

        call undress(Rogue, "underwear") from _call_undress_12
        
        "You can tell she means it, as she moves her panties to the side, exposing her already soaking wet pussy."
    
    $ Action = ActionClass("sex", Player, Rogue)

    call start_Action(Action) from _call_start_Action_8

    $ Action.mode = 0

    "You bring yourself close, lightly pressing your tip against her."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

    "She shudders as you make contact."
    ch_Player "I'll start slow."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Thank you. . ."

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    $ speed = 0.01
    $ starting_depth = 0.025

    $ Action.mode = 2

    "Slowly, gently, you start easing the tip inside her."

    $ Rogue.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2)

    $ speed = 0.0005
    $ starting_depth = 0.05

    "There's a lot of resistance, and she can't help but wince as you push further inside."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    $ speed = 0.001
    $ starting_depth = 0.075

    ch_Rogue "Ah'm alright, please don't stop."

    $ Rogue.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 1)

    $ speed = 0.0005
    $ starting_depth = 0.1

    "You keep pushing, and [Rogue.name] grits her teeth as the resistance only increases."
    
    $ speed = 0.001
    $ starting_depth = 0.125

    "Still, you keep making slow progress."

    $ Rogue.change_face("worried3", blush = 2)

    $ speed = 0.001
    $ starting_depth = 0.25

    "[Rogue.name] lets out a gasp as you suddenly break through."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Player "Are you okay?"
    ch_Rogue "It didn't hurt too bad. . ."
    ch_Rogue "Ah'd like you to keep goin'."

    $ Rogue.change_face("sexy", eyes = "down", blush = 2)

    $ speed = 0.3
    $ intensity = 0.5
    $ starting_depth = 0.2

    "You oblige and start a slow rhythm."

    $ Rogue.change_face("kiss2", blush = 2)

    "As you continue pumping back and forth, you pull [Rogue.name] into a kiss."

    $ Rogue.History.update("kiss")
    
    $ speed = 0.5
    $ intensity = 0.5

    "She latches onto you, holding you close, squeezing you tightly."
    "She starts to tremble, with each thrust making her twitch more violently than the last."

    $ Rogue.change_face("worried3", blush = 2)

    "Suddenly, [Rogue.name]'s legs tighten around you, as she shudders uncontrollably, tightening around your cock." with orgasm_shake
    
    $ speed = 0.001

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "That was amazin'. . ."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "But don't stop on my account, ah want ya to finish too."

    $ Rogue.change_face("kiss2", blush = 2)

    $ speed = 0.5
    $ intensity = 0.5

    "[Rogue.name] pulls you back down into a kiss and pushes her hips into yours, prompting you to start moving again."

    $ Rogue.History.update("kiss")

    $ Rogue.change_face("sly", mouth = "lipbite", blush = 2)

    if Rogue.quirk:
        ch_Rogue "Please, use me until yer satisfied. . ."
    else:
        ch_Rogue "Don't stop until yer satisfied. . ."

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Rogue "It doesn't really hurt anymore, you can go deeper if ya want."
    
    $ speed = 0.5
    $ intensity = 1.0
    
    "You do and feel yourself drawing ever closer to the edge."

    $ Rogue.change_face("worried2", mouth = "lipbite", blush = 2)

    "She starts to twitch again as well and can't hold her moans in any longer."
    "The sound of her pleasure only forces you to the brink faster, and you can't hold on any longer. . ."

    $ Rogue.change_face("kiss2", blush = 2)

    "[Rogue.name] brings you close for another kiss as she shudders violently, and you're only barely able to pull out in time." with orgasm_shake

    $ Rogue.History.update("kiss")

    $ Action.mode = 0

    $ Rogue.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)
    
    $ Player.orgasming = "cumshot"

    pause 1.0
    
    $ Rogue.spunk["belly"] = True

    "She continues to twitch, as you cum all over her stomach."

    $ Player.orgasming = False

    $ Rogue.change_face("kiss2", blush = 2)

    "She kisses you again, as her body shudders in ecstasy."

    $ Rogue.History.update("kiss")

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah hope that was as good for you as it was for me. . ."

    call stop_all_Actions(close_interface = False) from _call_stop_all_Actions_5

    hide screen Action_screen

    call closing_Action_interface from _call_closing_Action_interface_2
    
    if Rogue.History.check("swallowed_cum"):
        call swallow_cum(Rogue) from _call_swallow_cum_15

        "[Rogue.name] wipes the cum off of her stomach, before eating it." 
    else:
        call clean_cum(Rogue) from _call_clean_cum_3

        "[Rogue.name] cleans the cum off of her stomach."

    call change_Outfit(Rogue, Rogue.Wardrobe.Outfits[Rogue.Outfit.name]) from _call_change_Outfit_22

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah couldn't have wished for anythin' better. . . makin' love with you like that. . ."

    $ Rogue.change_face("worried1", eyes = "right", mouth = "smirk", blush = 1)

    ch_Rogue "It's like a dream ah never thought would come true."

    $ Rogue.change_face("sexy", blush = 2)

    menu:
        extend ""
        "That really was amazing. I'm glad it lived up to your expectations.":
            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1147
        "Yeah, that wasn't too bad. You'll get better the more we do it together.":
            $ Rogue.change_face("worried1", blush = 1)

            call change_Girl_stat(Rogue, "love", 0) from _call_change_Girl_stat_1148

    $ Rogue.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Rogue "Ah know ah say it a lot. . . but ah love you."
    ch_Player "I love you too."

    $ Rogue.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Rogue "Ah hope we can make love together many more times. . ."

    $ lights_on = False

    $ lighting = "moonlight"
    
    call set_the_scene(fade = False, fade_Characters = False) from _call_set_the_scene_375

    $ Rogue.change_face("worried1", eyes = "closed", mouth = "smirk", blush = 1)

    "[Rogue.name] crawls into bed with you, laying her head on your chest."

    $ fade_to_black(0.4)

    "You fall asleep together, more connected than ever."

    jump go_to_sleep

    $ ongoing_Event = False

    return