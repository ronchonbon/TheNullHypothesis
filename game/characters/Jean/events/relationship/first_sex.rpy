init python:

    def Jean_first_sex_part_one():
        label = "Jean_first_sex_part_one"

        conditions = [
            "Jean in Partners",

            "approval_check(Jean, threshold = Jean_thresholds['sex'])",
            
            "day - EventScheduler.Events['Jean_penultimate_quirk'].completed_when >= 3",

            "Player.location == Player.home and not Present",

            "Jean.is_in_normal_mood()"]
            
        sleeping = True

        priority = 99

        return EventClass(label, conditions, sleeping = sleeping, priority = priority)

label Jean_first_sex_part_one:
    $ ongoing_Event = True

    $ fade_to_black(0.4)

    call receive_text(Jean, "Hey") from _call_receive_text_733
    call receive_text(Jean, "Heyyy") from _call_receive_text_734

    $ fade_in_from_black(0.4)

    "Your phone lights up with several notifications, waking you."
    "Blearily fumbling around, you finally grab it and open it up."

    call open_texts(Jean) from _call_open_texts_28
    call receive_text(Jean, "Wake uppppp") from _call_receive_text_735
    call send_text(Jean, "I'm upppp") from _call_send_text_100
    call send_text(Jean, "what's wrong?") from _call_send_text_101
    call receive_text(Jean, "Nothing's wrong") from _call_receive_text_736
    call receive_text(Jean, "I mean something's wrong, kinda") from _call_receive_text_737
    call receive_text(Jean, "Ugh") from _call_receive_text_738
    call receive_text(Jean, "I know it's late but") from _call_receive_text_739
    call receive_text(Jean, "Can we talk?") from _call_receive_text_740

    $ Jean.mandatory_text_options = ["well, now I'm really awake. of course we can talk", "suoier rew  cnaws tokl aaaaaaaa", "really? does it have to be right now?"]
    $ temp = Jean.mandatory_text_options[:]

    while Jean.mandatory_text_options:
        pause

    if Jean.text_history[-1][1] == temp[0]:
        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1101

        call receive_text(Jean, "Ugh") from _call_receive_text_741
        call receive_text(Jean, "Now I feel bad </3") from _call_receive_text_742
        call receive_text(Jean, "Just go back to sleep") from _call_receive_text_743
        call receive_text(Jean, "We can talk tomorrow") from _call_receive_text_744
    elif Jean.text_history[-1][1] == temp[1]:
        $ temp = Jean.Player_petname.capitalize()

        call receive_text(Jean, f"{temp}???") from _call_receive_text_745
        call receive_text(Jean, "Did you just fall back asleep?????") from _call_receive_text_746
        call receive_text(Jean, "It's okay") from _call_receive_text_747
        call receive_text(Jean, "We can just talk tomorrow") from _call_receive_text_748
    elif Jean.text_history[-1][1] == temp[2]:
        call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1102

        call receive_text(Jean, "Ugh") from _call_receive_text_749
        call receive_text(Jean, "I guess not") from _call_receive_text_750
        call receive_text(Jean, "Go back to sleep") from _call_receive_text_751
        call receive_text(Jean, "We can talk tomorrow") from _call_receive_text_752
        
    pause

    hide screen phone_screen

    "You put your phone back down and instantly fall back asleep. . ."

    $ fade_to_black(0.4)

    pause 2.0

    call knock_on_door(times = 2, intensity = 0.25) from _call_knock_on_door_44
    call knock_on_door(times = 2, intensity = 0.5) from _call_knock_on_door_45
    call knock_on_door(times = 2, intensity = 0.75) from _call_knock_on_door_46

    $ fade_in_from_black(0.4)

    "You're startled awake once more, as you hear frantic knocking on your door."

    call receive_text(Jean, "I'm sorry") from _call_receive_text_753
    call receive_text(Jean, "It can't wait") from _call_receive_text_754

    call open_texts(Jean) from _call_open_texts_29
    call receive_text(Jean, "Open upppp") from _call_receive_text_755
    
    pause

    hide screen phone_screen

    $ lights_on = True
    
    $ lighting = "night"

    call set_the_scene(fade = False) from _call_set_the_scene_360

    "Still a bit delirious, you manage to pull yourself out of bed and open the door."

    call send_Characters(Jean, Player.home, behavior = False) from _call_send_Characters_234

    $ Jean.change_face("worried1", mouth = "lipbite")

    ch_Jean "Hey. . ."

    $ Jean.change_face("confused2", mouth = "lipbite")

    pause 1.0

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 1)

    pause 1.0

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Jean "You're only wearing underwear. . ."
    ch_Player "Wha. . ."

    $ Jean.change_face("confused1", mouth = "smirk")

    ch_Player "Oh shit."

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Not like I mind."
    "You're about to find some clothes to put on when [Jean.name] gently sits you on your bed."
    "She takes a seat right next to you."

    $ Jean.change_face("worried1", mouth = "lipbite")

    ch_Jean "I'm sorry for waking you up again. . ."

    $ Jean.change_face("worried1")

    ch_Jean "But I just couldn't get all the thoughts out of my head."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Player "What's going on?"

    $ Jean.change_face("worried1", mouth = "lipbite")

    ch_Jean "It's. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right")

    ch_Jean "It's about you."

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Player "About me?!"
    ch_Jean "Ugh, yes, I can't get it out of my head. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Player "Wha-"
    ch_Jean "Like, our relationship has been amazing so far."

    $ Jean.change_face("worried1")

    ch_Jean "But everything you've been through lately. . ."
    ch_Jean "I'm just sick of it."

    $ Jean.change_face("worried1", eyes = "down")

    ch_Jean "Sick of worrying you might get hurt again, before we can. . ."

    $ Jean.change_face("angry1", eyes = "right", blush = 1)

    ch_Jean "UGH!"

    $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Jean "I don't know why I wanted to wait so long before doing it with you. . ."

    $ Jean.change_face("angry1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Jean "So focused on arbitrary shit."
    ch_Jean "Like, who actually cares."

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Player "[Jean.name], what are you talking about?"

    $ Jean.change_face("perplexed", blush = 1)

    ch_Jean "I'm talking about us!"

    $ Jean.change_face("confused1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Jean "I've been struggling with it for a while now. . ."
    ch_Player "With?"

    $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

    ch_Jean "But I've made up my mind."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "There's no point in waiting, I know I want it to be you."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean "I've known for so long at this point. . ."
    ch_Player "I'm so confused."

    menu:
        extend ""
        "Look, I can tell this is important to you. . . but I really don't know what you're talking about. . .":
            $ Jean.change_face("confused2", blush = 1) 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1103 
            call change_Character_stat(Jean, "trust", 0) from _call_change_Character_stat_1104
                    
            ch_Jean "Oh my god."

            $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

            ch_Jean "[Player.first_name], do I have to spell it out?"

            $ Jean.change_face("angry1", blush = 1)

            "[Jean.name] cups your face with both hands and looks directly into your eyes."
            ch_Jean "I.{w} Want.{w} To.{w} Have.{w} Sex.{w} With.{w} You."
        "Wha. . . wait a minute. Are you talking about. . .?":
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1105

            ch_Player "Are you talking about. . . sex?!"

            $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

            ch_Jean "Oh my god, [Player.first_name]. . ."
            "[Jean.name] cups your face with both hands and looks directly into your eyes."

            $ Jean.change_face("angry1", blush = 1)

            ch_Jean "Yes."
            ch_Jean "I.{w} Want.{w} To.{w} Have.{w} Sex.{w} With.{w} You."
        "Seriously, [Jean.name]. What the hell are you talking about?!":
            $ Jean.change_face("confused2", blush = 1) 
                    
            ch_Jean "Oh my god."

            $ Jean.change_face("angry1", mouth = "lipbite", blush = 1)

            ch_Jean "[Player.first_name], do I have to spell it out?"

            $ Jean.change_face("angry1", blush = 1)

            "[Jean.name] cups your face with both hands and looks directly into your eyes."
            ch_Jean "I.{w} Want.{w} To.{w} Have.{w} Sex.{w} With.{w} You."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "right", blush = 1)

    ch_Jean "I've been a virgin for long enough. . ."
    ch_Player "Oh. . ."

    $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

    ch_Player "Right now?!"
    ch_Jean "I mean, I'm on the pill. . . no reason to wait. . ."

    $ Jean.give_trait("birth_control")

    menu:
        extend ""
        "Well, in that case, I'd love to.":
            $ EventScheduler.Events["Jean_first_sex_part_two"].start()

            jump go_to_sleep
        "It's not that I don't want to, but can we wait?":
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)
            
            ch_Jean "I guess I can wait a little longer. . ." 
            
            $ Jean.change_face("worried1", mouth = "smirk") 
            
            ch_Jean "I'll let you get back to sleep." 
            ch_Jean "You better not make me wait too long." 

            call remove_Characters(Jean) from _call_remove_Characters_266
            
            "You crawl back into bed and are unconscious in moments."

    $ ongoing_Event = False

    return
    
init python:

    def Jean_first_sex_part_two():
        label = "Jean_first_sex_part_two"

        conditions = [
            "False"]

        return EventClass(label, conditions)

label Jean_first_sex_part_two:
    $ ongoing_Event = True

    $ has_progression_control = False
    $ has_Action_control = False
    $ has_position_control = False
    $ has_movement_control = False
    $ has_ejaculation_control = False

    if Jean.position == "doggy":
        call show_pose(Jean, "standing") from _call_show_pose_2

    if not Action_screen_showing:
        show screen Action_screen()

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 1)

    ch_Jean "Finally. . ."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "C'mere, [Jean.Player_petname]."

    $ Jean.change_face("kiss2", blush = 1)

    "[Jean.name] pulls you into her embrace, your lips pressed together."

    $ Jean.change_face("kiss1", blush = 2)

    $ Jean.History.update("kiss")

    "You can already feel her excitement. . . and maybe a little bit of trepidation, and she squeezes you tightly."
    "As you run your hands along her slender curves, you start to help her out of her clothes. . ."

    call take_off_everything_but(Jean, ["bra", "skirt", "pants", "hose", "underwear", "socks"]) from _call_take_off_everything_but_15

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 1)

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        ch_Jean "Take your bottoms off already, [Jean.Player_petname]." 
        ch_Jean "Don't keep your big sis' waiting. . ."
    else:
        ch_Jean "Take your bottoms off. . ." 

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 1)

    "You remove everything, exposing yourself to her."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 2)

    ch_Jean "I hope I can handle it. . ."

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
        
        ch_Jean "Now, take mine off for me. . ." 
        "You oblige her and help her out of her bottoms."
    else:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 
        
        "[Jean.name] takes her bottoms off as well."

    call take_off_everything_but(Jean, ["hose", "underwear", "socks"]) from _call_take_off_everything_but_16

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "I can tell you don't need any encouragement down there. . ."

    $ Jean.change_face("kiss1", blush = 2)

    "She pulls you into another kiss, before falling backwards onto the bed, dragging you down with her."

    $ Jean.History.update("kiss")

    call request_position(Jean, "missionary", automatic = True) from _call_show_pose_5

    $ Jean.change_face("sexy", blush = 1)

    if Jean.Clothes["underwear"].string:
        pause 1.0
        
        if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
            $ Jean.change_face("sly", mouth = "lipbite", blush = 1) 
            
            ch_Jean "Open your present, [Jean.Player_petname]. . ." 

            call undress(Jean, "underwear") from _call_undress_10
            
            "She watches attentively, as you move her panties aside, exposing her pussy."
        else:
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1) 

            call undress(Jean, "underwear") from _call_undress_11
            
            "[Jean.name] moves her panties to the side, exposing her pussy."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "Be gentle, okay?"
    ch_Player "Of course."
    ch_Player "Are you ready?"

    $ Jean.change_face("kiss1", blush = 2)

    "She pulls you down into one more kiss. . ."

    $ Jean.History.update("kiss")

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    "Before giving you a small nod."
    ch_Jean "I'm ready."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 1)

    $ Action = ActionClass("sex", Player, Jean)

    call start_Action(Action) from _call_start_Action_6

    $ Action.mode = 0

    "You bring yourself close, lightly pressing your tip against her."

    $ Jean.change_face("worried1", mouth = "lipbite", eyes = "down", blush = 2)

    "She's already soaking wet just in anticipation, but also trembles slightly at your touch out of apprehension."
    
    $ speed = 0.001
    $ starting_depth = 0.025

    $ Action.mode = 2
    
    "Gently, you ease the tip inside her."

    $ Jean.change_face("angry1", eyes = "closed", mouth = "lipbite", blush = 2)

    "There's quite a bit of resistance, and she grimaces as you push farther in." 
    
    $ speed = 0.0005
    $ starting_depth = 0.05

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean "Keep going, it only hurts a little."

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

    $ speed = 0.001
    $ starting_depth = 0.075

    "You do and the resistance only increases."

    $ Jean.change_face("angry1", eyes = "closed", mouth = "kiss", blush = 2)

    $ speed = 0.0005
    $ starting_depth = 0.1

    "She trembles slightly as you enter her deeper and deeper, and she pulls you into a kiss, squeezing you for comfort."

    $ Jean.History.update("kiss")

    $ speed = 0.001
    $ starting_depth = 0.25

    "With both your lips and your bodies locked together, you continue gently easing further and further until finally breaking through the resistance."

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    "She lets out a gasp, but only gives you a gentle smile."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 2)

    ch_Jean "That wasn't so bad. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    ch_Jean "Now, start moving. . ."

    $ Jean.change_face("worried1", eyes = "closed", mouth = "kiss", blush = 2)

    $ speed = 0.3
    $ intensity = 0.5
    $ starting_depth = 0.2

    "She pulls you into another kiss as you pull back slightly, before gently thrusting forward, starting a slow rhythm."

    $ Jean.History.update("kiss")

    "Your lips only part for her to let out small whimpers and moans." 

    $ Jean.change_face("sly", mouth = "lipbite", blush = 2)

    $ speed = 0.5
    $ intensity = 0.5

    ch_Jean "Go faster. . ."

    $ intensity = 1.0

    "You pick up the pace, inadvertently going deeper as well."

    $ speed = 0.001

    $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

    "She jerks in surprise and lets out a peep."
    ch_Jean "Maybe not so deep yet. . ."

    $ Jean.change_face("worried1", mouth = "smirk", blush = 2)

    $ speed = 0.5
    $ intensity = 0.5

    "You pull back a little, maintaining your current pace."

    $ Action = ActionClass("self_touch_pussy", Jean, Jean)

    call start_Action(Action) from _call_start_Action_7

    "She brings her hand down and starts massaging her clit as you continue."
    "It's not long before you feel [Jean.name] begin twitching around your cock."

    $ Jean.change_face("worried1", eyes = "closed", mouth = "kiss", blush = 2)

    $ speed = 1.0
    $ intensity = 0.5

    "She pulls you into another kiss and holds you there, as the twitching and shuddering intensifies."

    $ Jean.History.update("kiss")

    "You're also drawing close to the edge."

    $ Jean.change_face("angry1", mouth = "lipbite", blush = 2)

    ch_Jean "You better not stop. . ."

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 2)

    "[Jean.name] notices the look in your eye. Just as you're about to cum, you pull out." with orgasm_shake

    $ Action.mode = 0

    $ Jean.change_face("worried1", eyes = "down", mouth = "lipbite", blush = 2)

    $ Player.orgasming = "cumshot"

    pause 1.0
    
    $ Jean.spunk["belly"] = 1

    "She continues masturbating and finally orgasms herself, shuddering in ecstasy as you cum all over her stomach." with orgasm_shake

    $ Player.orgasming = None

    $ stop_Actions(Jean, organ = "right_hand")

    $ Jean.change_face("worried1", eyes = "closed", mouth = "kiss", blush = 2)

    "You're pulled into another kiss as she continues to shudder and twitch."

    $ Jean.History.update("kiss")

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "That was. . ."

    call stop_all_Actions(close_interface = False) from _call_stop_all_Actions_4

    hide screen Action_screen

    call closing_Action_interface from _call_closing_Action_interface
    
    if Jean.History.check("swallowed_cum"):
        call swallow_cum(Jean) from _call_swallow_cum_14

        "[Jean.name] wipes the cum off of her stomach, before eating it." 
    else:
        call clean_cum(Jean) from _call_clean_cum_2

        "[Jean.name] cleans the cum off of her stomach."

    call change_Outfit(Jean, Jean.Wardrobe.Outfits[Jean.Outfit.name]) from _call_change_Outfit_16

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "That was amazing. . ."

    $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

    ch_Jean "I'm sure you loved that, huh?"

    menu:
        extend ""
        "I really did. . . I'm glad we could share that together.":
            $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1106
        "That wasn't too bad. Just need more. . . practice.":
            $ Jean.change_face("confused1", blush = 1) 
            
            call change_Character_stat(Jean, "love", 0) from _call_change_Character_stat_1107

    $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

    ch_Jean "We better do that again. . ."

    $ Jean.change_face("sly", blush = 1)

    ch_Jean "{i}Frequently{/i}."

    $ Player.stamina -= 1

    $ Jean.remove_trait("virgin")

    $ Player.History.update("took_virginity")

    $ ongoing_Event = False

    return