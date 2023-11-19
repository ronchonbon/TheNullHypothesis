init python:

    def Jean_I_love_you():
        label = "Jean_I_love_you"

        conditions = [
            "Jean in Partners",

            "approval_check(Jean, threshold = Jean_thresholds['love'])",

            "day - EventScheduler.Events['Jean_penultimate_quirk'].completed_when >= 3",

            "Player.location == Player.home and not Present",

            "Jean.is_in_normal_mood()"]

        waking = True

        priority = 99

        return EventClass(label, conditions, waking = waking, priority = priority)

label Jean_I_love_you:
    $ ongoing_Event = True

    call receive_text(Jean, "Good morning!!! <3") from _call_receive_text_771
    call receive_text(Jean, "You up yet???") from _call_receive_text_772
    call receive_text(Jean, "Helloooooo") from _call_receive_text_773

    "As you wake up, your phone buzzes with several new texts."

    call open_texts(Jean) from _call_open_texts_33
    call receive_text(Jean, "I had a dream about us last night") from _call_receive_text_774
    call receive_text(Jean, "It made me realize something") from _call_receive_text_775

    $ Jean.mandatory_text_options = ["good morning! hope it was a sweet dream", "good morning! hope it was a sexy dream ;)", "oh god, don't tell me you're mad because I cheated on you in a dream or something"]
    $ temp = Jean.mandatory_text_options[:]

    while Jean.mandatory_text_options:
        pause

    if Jean.text_history[-1][1] == temp[0]:
        call receive_text(Jean, "I guess in a way <3") from _call_receive_text_776
    elif Jean.text_history[-1][1] == temp[1]:
        call receive_text(Jean, "You little horndog") from _call_receive_text_777
        call receive_text(Jean, "It wasn't") from _call_receive_text_778
    elif Jean.text_history[-1][1] == temp[2]:
        call receive_text(Jean, "Oh come on") from _call_receive_text_779
        call receive_text(Jean, "You don't really think I'd get mad over something like that") from _call_receive_text_780
        call receive_text(Jean, "Right?") from _call_receive_text_781
        call send_text(Jean, "well") from _call_send_text_102
        call receive_text(Jean, "Whatever") from _call_receive_text_782

    call receive_text(Jean, "Ugh, I woke you up didn't I?") from _call_receive_text_783
    call send_text(Jean, "kinda") from _call_send_text_103
    call receive_text(Jean, "My dream last night wasn't all that happy </3") from _call_receive_text_784
    call receive_text(Jean, "Why don't you get dressed and everything and I'll be right over") from _call_receive_text_785
    call receive_text(Jean, "I need to talk about this in person") from _call_receive_text_786
    call send_text(Jean, "alright") from _call_send_text_104

    pause

    hide screen phone_screen

    "You hop out of bed, and head to the bathroom to brush your teeth."

    call knock_on_door(times = 3) from _call_knock_on_door_54

    "As you're finishing up, someone starts knocking on the door."

    call send_Characters(Jean, Player.home, behavior = False) from _call_send_Characters_249

    $ Jean.change_face("worried1", eyes = "closed", blush = 1)

    "You open the door, and [Jean.name] leaps into your arms."

    $ Jean.change_face("worried1", eyes = "closed", mouth = "kiss", blush = 1)

    "She squeezes you tight for a long moment, before pulling back and kissing you."

    $ Jean.change_face("worried1")

    ch_Player "What was all that for?"

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "I'm just super glad. . ."

    $ Jean.change_face("worried1")

    ch_Player "Glad?"

    $ Jean.change_face("worried1", eyes = "right", mouth = "smirk")

    ch_Jean "Well, my dream. . ."

    $ Jean.change_face("worried1")

    ch_Jean "It was a bad one."
    ch_Jean "You were in it, and bad things kept happening to you."

    $ Jean.change_face("worried1", eyes = "right")

    ch_Jean "Until. . ."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "I know it wasn't real, but it made me realize a couple things."

    if Jean.History.check("quirk_encouraged") >= Jean.History.check("quirk_discouraged"):
        $ Jean.quirk = True

        $ Jean.change_face("worried1", mouth = "lipbite")

        ch_Jean "Big sister is gonna talk for a while, so just listen."

        menu:
            extend ""
            "Okay, I won't interrupt.":
                $ Jean.change_face("worried1")

                ch_Jean "Thanks." 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1112 
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1113
            "Of course, I'm all ears.":
                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Jean "Good boy." 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1114
            "Oh god, don't tell me you're going to start monologuing.":
                $ Jean.change_face("angry1") 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1115

                ch_Jean "Ugh, this is serious." 
                ch_Jean "Just pay attention."

        $ Jean.change_face("worried1", mouth = "smirk")

        ch_Jean "Having you as my boyfriend. . ."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean ". . . as my 'little sibling'. . ."
        ch_Jean "I don't know if you realize how happy it's made me."
        ch_Jean "Having someone to dote on, to spoil, to shower with affection. . ."
        ch_Jean "Someone to have fun with, and relax?" 

        $ Jean.change_face("worried2", mouth = "lipbite", blush = 2)

        ch_Jean "And that person being you of all people?"

        $ Jean.change_face("worried1", mouth = "smirk", blush = 1)

        ch_Jean "My mental health has literally never been better. . ."

        $ Jean.change_face("worried1", eyes = "right")

        ch_Jean ". . . more like my life in general."

        $ Jean.change_face("worried1", blush = 1)
    else:
        $ Jean.quirk = False

        ch_Jean "Having you as my boyfriend. . ."

        $ Jean.change_face("worried1")

        ch_Jean "I don't know if you realize how happy it's made me."

        menu:
            extend ""
            "It's made me happy too, I'm glad.":
                $ Jean.change_face("worried1", mouth = "smirk")

                ch_Jean "It really, {i}really{/i} has." 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1116 
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1117
            "You really mean it? Because it's made me happy too.":
                $ Jean.change_face("worried1", mouth = "lipbite")

                ch_Jean "Of course I mean it." 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1118
            "Good for you. . . I guess. It hasn't been the worst thing in the world.":
                $ Jean.change_face("angry1")

                ch_Jean "I'm not joking around, [Player.first_name]." 
                
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1119

        $ Jean.change_face("worried1")

        ch_Jean "Being excited to spend time with someone. . ."
        ch_Jean "Not worrying about my responsibilities so much, and learning how to have fun with someone?" 

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "And that person being you of all people?"

        $ Jean.change_face("worried1", mouth = "smirk")

        $ temp = Jean.Player_petname.capitalize()

        ch_Jean "[temp], I can't overstate how positive of an impact you've had on my mental health and my life in general."

        $ Jean.change_face("worried1")

    ch_Jean "Before you got here I was always so worried about my grades, my anxiety was through the roof."
    ch_Jean "I had no free time, and could literally never relax."
    ch_Jean "I barely had any friends, everybody thought I was a pushy know-it-all."

    $ Jean.change_face("worried1", mouth = "smirk")

    ch_Jean "But with you. . ."

    $ Jean.change_face("worried1", mouth = "lipbite")

    menu:
        extend ""
        "You don't know how glad it makes me to know that I've been able to have such a positive impact on you. Our relationship means the world to me, and so do you.":
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1120 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1121
        "You know I want nothing more than you to be happy, and I'm so glad that's the case. Our relationship is the most important thing in the world to me, and I'll do whatever I can to keep you happy.":
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1122
        "Look, [Jean.name], I'm not just something you can use to fix whatever problems you're facing. I'm my own person with, with my own struggles too. That being said, I want you to be happy, and am glad our relationship has been helping you with that.":
            call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1123 
            call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1124

    $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    ch_Jean "[Player.first_name], I love you."

    $ Jean.change_face("worried2", blush = 1)

    ch_Jean "You. . . love me too, right?"

    menu:
        extend ""
        "I do. I love you, [Jean.name].":
            pass
        "Are you kidding? I love you so much, [Jean.name].":
            pass
        "Really? No shit, [Jean.name].":
            pass

    $ Jean.change_face("worried1", eyes = "right", mouth = "lipbite", blush = 1)

    ch_Jean "Good. . ."

    if Jean.quirk:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Now come here and give your big sister a kiss."

        $ Jean.change_face("kiss2", blush = 1)

        "She doesn't give you much choice, and pulls you into a deep kiss."

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)
    else:
        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

        ch_Jean "Well. . . you better give me a kiss, then."
        ch_Player "I'd be happy to."

        $ Jean.change_face("kiss2", blush = 1)

        "[Jean.name] pulls you into a deep kiss."

        $ Jean.change_face("worried1", mouth = "lipbite", blush = 1)

    $ Jean.History.update("kiss")
    
    if Jean.quirk:
        $ Jean.change_face("sly", blush = 1)

        ch_Jean "From now on, your big sister is gonna smother you with all the affection, and spoil you every single day."
        ch_Jean "I will {i}always{/i} be there to take care of you."

        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "And I can't wait to explore all the 'fun' things we can do together."
        ch_Jean "I love teasing you, making you twitch. . ."

        menu:
            extend ""
            "Talking like that. . . you're already making me twitch. . .":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1125 
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1126
            "Please do. . . I promise I'll be the best little brother you could ever want.":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1127
            "You better not tease me too much, it gets kinda annoying. . . but yeah, it'll be fun.":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1128

        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

        ch_Jean "And a good little brother will want to make his big sister feel good too. . ."

        $ Jean.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Jean "Don't worry, we'll figure it out together."
    else:
        $ Jean.change_face("sly", mouth = "lipbite", blush = 1)

        ch_Jean "Yum."
        ch_Jean "Ugh, I can't wait to relax in your arms, and explore all the ways we can enjoy each other. . ."

        $ Jean.change_face("sexy", blush = 1)

        ch_Jean "We're gonna make each other feel so good."

        $ Jean.change_face("confused1", mouth = "lipbite", blush = 1)

        menu:
            extend ""
            "I'm also looking forward to it, very much.":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1129 
                call change_Girl_stat(Jean, "trust", 0) from _call_change_Girl_stat_1130
            "I will do my absolute best to make you feel very good.":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1131
            "[Jean.name], we both know you don't really know what you're doing. . . we'll figure it out. . . with lots of practice.":
                call change_Girl_stat(Jean, "love", 0) from _call_change_Girl_stat_1132

        $ Jean.change_face("confused1", eyes = "squint", mouth = "lipbite", blush = 1)

        ch_Jean "We'll figure it out together."

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "For now, I gotta go."
    ch_Jean "Don't miss me too much. . ."

    $ Jean.change_face("sexy", eyes = "right", blush = 1)

    pause 1.0

    $ Jean.change_face("sexy", blush = 1)

    ch_Jean "Actually, scratch that."
    ch_Jean "You better miss me a {i}lot{/i}."

    call remove_Characters(Jean) from _call_remove_Characters_284
    
    $ ongoing_Event = False

    return